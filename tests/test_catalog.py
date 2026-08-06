from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from scripts.sync_from_forge import require_public_research_provenance


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "models.json"


class CatalogTest(unittest.TestCase):
    def test_published_markdown_has_no_trailing_whitespace(self) -> None:
        for path in sorted(ROOT.glob("skills/**/*.md")):
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.endswith("\n"), str(path))
            self.assertFalse(text.endswith("\n\n"), str(path))
            for line_number, line in enumerate(text.splitlines(), start=1):
                self.assertEqual(
                    line,
                    line.rstrip(),
                    f"{path}:{line_number}",
                )

    def test_public_research_rejects_provider_request_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "research.json"
            with self.assertRaisesRegex(
                ValueError, "run research_catalog.py prepare-publication"
            ):
                require_public_research_provenance(
                    {
                        "provenance": {
                            "provider": "Tavily Research",
                            "requestId": "provider-request",
                        }
                    },
                    path,
                )
        require_public_research_provenance(
            {
                "provenance": {
                    "provider": "Tavily Research",
                    "promptSha256": "0" * 64,
                }
            },
            Path("research.json"),
        )

    def test_every_catalog_entry_has_a_valid_exact_skill(self) -> None:
        payload = json.loads(CATALOG.read_text(encoding="utf-8"))
        self.assertEqual(payload["total"], len(payload["models"]))
        self.assertEqual(
            len({item["slug"] for item in payload["models"]}),
            payload["total"],
        )
        self.assertEqual(
            len({item["path"] for item in payload["models"]}),
            payload["total"],
        )
        for item in payload["models"]:
            self.assertLessEqual(len(item["skillName"]), 63)
            path = ROOT / item["path"]
            self.assertTrue(path.is_file(), item["slug"])
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\nname: "))
            self.assertRegex(item["skillName"], r"^[a-z0-9-]+$")
            self.assertIn(f"Model slug: `{item['slug']}`", text)
            self.assertRegex(item["contentSha256"], r"^[0-9a-f]{64}$")
            self.assertTrue(
                (path.parent / "references" / "forge-model.json").is_file()
            )
            self.assertTrue(
                (path.parent / "references" / "forge-skill.json").is_file()
            )
            self.assertTrue(
                (path.parent / "references" / "evidence.md").is_file()
            )
            self.assertTrue((path.parent / "agents" / "openai.yaml").is_file())
            self.assertTrue((path.parent / "evals" / "evals.json").is_file())
            if item.get("deepResearchStatus") in {"accepted", "revised"}:
                self.assertTrue(
                    (path.parent / "references" / "research.json").is_file()
                )
                self.assertTrue(
                    (path.parent / "references" / "research.md").is_file()
                )

    def test_hierarchy_contains_every_model_once(self) -> None:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        hierarchy = json.loads(
            (ROOT / "catalog" / "hierarchy.json").read_text(encoding="utf-8")
        )
        slugs: list[str] = []
        for groups in hierarchy["categories"].values():
            for families in groups.values():
                for models in families.values():
                    slugs.extend(models)
        self.assertEqual(sorted(slugs), sorted(item["slug"] for item in catalog["models"]))

    def test_group_catalog_covers_hierarchy(self) -> None:
        hierarchy = json.loads(
            (ROOT / "catalog" / "hierarchy.json").read_text(encoding="utf-8")
        )
        groups = json.loads(
            (ROOT / "catalog" / "groups.json").read_text(encoding="utf-8")
        )
        expected = {
            (category, group)
            for category, grouped in hierarchy["categories"].items()
            for group in grouped
        }
        actual = {
            (item["category"], item["group"]) for item in groups["groups"]
        }
        self.assertEqual(actual, expected)

    def test_hand_authored_skills_have_portable_frontmatter(self) -> None:
        for path in sorted((ROOT / "skills").glob("**/SKILL.md")):
            text = path.read_text(encoding="utf-8")
            match = re.match(
                r"^---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n",
                text,
            )
            self.assertIsNotNone(match, str(path))
            self.assertLessEqual(len(match.group(1)), 63)

    def test_nebius_router_has_executable_forge_serverless_leaf(self) -> None:
        router = (ROOT / "skills" / "nebius" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        deployment = (
            ROOT
            / "skills"
            / "nebius"
            / "forge-model-deployment"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        endpoint = (
            ROOT / "skills" / "nebius" / "serverless-endpoints" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("$nebius-forge-model-deployment", router)
        self.assertIn("longer than 64 characters", deployment)
        self.assertIn("$nebius-serverless-endpoints", deployment)
        self.assertIn("nebius ai endpoint create", endpoint)


if __name__ == "__main__":
    unittest.main()
