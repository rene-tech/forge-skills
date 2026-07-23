from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "models.json"


class CatalogTest(unittest.TestCase):
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

    def test_hand_authored_skills_have_portable_frontmatter(self) -> None:
        for path in sorted((ROOT / "skills").glob("**/SKILL.md")):
            text = path.read_text(encoding="utf-8")
            match = re.match(
                r"^---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n",
                text,
            )
            self.assertIsNotNone(match, str(path))
            self.assertLessEqual(len(match.group(1)), 63)


if __name__ == "__main__":
    unittest.main()
