from __future__ import annotations

import json
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import research_catalog  # noqa: E402


class ResearchPlanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = json.loads(
            (ROOT / "catalog" / "models.json").read_text(encoding="utf-8")
        )
        cls.units = research_catalog.model_units(cls.catalog)

    def test_every_exact_model_is_covered_once(self) -> None:
        covered = [
            model["slug"]
            for unit in self.units
            for model in unit["forgeModels"]
        ]
        expected = [model["slug"] for model in self.catalog["models"]]
        self.assertEqual(sorted(covered), sorted(expected))
        self.assertEqual(len(covered), len(set(covered)))

    def test_tavily_request_retries_rate_limit_without_losing_request(self) -> None:
        rate_limit = research_catalog.HTTPError(
            "https://api.tavily.com/research",
            429,
            "rate limited",
            {"Retry-After": "0"},
            io.BytesIO(b'{"detail":"slow down"}'),
        )
        response = io.BytesIO(b'{"request_id":"preserved"}')

        with (
            patch.object(
                research_catalog,
                "urlopen",
                side_effect=[rate_limit, response],
            ),
            patch.object(research_catalog.time, "sleep") as sleep,
        ):
            payload = research_catalog.tavily_request(
                "POST",
                "research",
                api_key="tvly-test",
                payload={"input": "bounded"},
            )

        self.assertEqual(payload["request_id"], "preserved")
        sleep.assert_called_once_with(1.0)

    def test_exact_source_serving_variants_share_research(self) -> None:
        matching = [
            unit
            for unit in self.units
            if unit["sourceUrls"]
            == ["https://huggingface.co/facebook/esm2_t33_650M_UR50D"]
        ]
        self.assertEqual(len(matching), 1)
        self.assertEqual(
            {item["slug"] for item in matching[0]["forgeModels"]},
            {
                "facebook-esm-2-650m",
                "facebook-esm-2-650m-protein-embedding",
            },
        )

    def test_generic_vendor_pages_do_not_merge_unrelated_models(self) -> None:
        visual_genai = [
            unit
            for unit in self.units
            if unit["sourceUrls"]
            == [
                "https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html"
            ]
        ]
        self.assertGreater(len(visual_genai), 1)
        for unit in visual_genai:
            self.assertEqual(len(unit["modelFamilies"]), 1)

    def test_provider_schemas_keep_full_local_validation_separate(self) -> None:
        schema = json.loads(
            (ROOT / "research" / "model-research.schema.json").read_text(
                encoding="utf-8"
            )
        )
        provider = research_catalog.provider_schema(schema)
        self.assertEqual(set(provider), {"properties", "required"})
        serialized = json.dumps(provider)
        self.assertNotIn('"additionalProperties"', serialized)
        self.assertIn('"description"', serialized)
        self.assertIn('"type"', serialized)
        self.assertIn("title", provider["properties"]["sources"]["items"]["properties"])

    def test_audit_schema_embeds_the_complete_corrected_dossier(self) -> None:
        audit = research_catalog.audit_schema(self.units[0])
        self.assertEqual(next(iter(audit["properties"])), "correctedDossier")
        self.assertEqual(audit["required"][0], "correctedDossier")
        corrected = audit["properties"]["correctedDossier"]
        self.assertIn("identity", corrected["properties"])
        self.assertIn(
            "sourceLocator",
            corrected["properties"]["benchmarks"]["items"]["properties"],
        )
        provider = research_catalog.provider_schema(audit)
        serialized = json.dumps(provider)
        self.assertNotIn('"additionalProperties"', serialized)
        self.assertIn('"correctedDossier"', serialized)
        self.assertIn(
            "independently verified",
            audit["properties"]["correctedDossier"]["description"],
        )
        self.assertNotIn(
            "evidenceUrls",
            audit["properties"]["issues"]["items"]["required"],
        )

    def test_audit_retry_includes_deterministic_validation_feedback(self) -> None:
        prompt = research_catalog.audit_prompt(
            self.units[0],
            {"family": self.units[0]["key"]},
            retry_feedback=["$.sources[0] uses a forbidden secondary host"],
        )
        self.assertIn("previous audit attempt failed", prompt)
        self.assertIn("forbidden secondary host", prompt)
        self.assertIn("third-party mirrors or reuploads", prompt)
        self.assertIn("exact member of", prompt)
        self.assertIn("Evidence gap:", prompt)
        self.assertIn("plain string", prompt)
        self.assertIn("Do not wrap it", prompt)
        self.assertIn("different cloud provider's hosted-API", prompt)
        self.assertIn("do not establish the NVIDIA NIM or", prompt)
        self.assertIn("remove or replace it everywhere", prompt)

    def test_manual_primary_source_hints_are_included_in_model_prompt(self) -> None:
        starcoder = next(
            unit
            for unit in self.units
            if unit["key"]
            == "build-nvidia-com-bigcode-starcoder2-7b-b4e247a817"
        )
        prompt = research_catalog.model_prompt(starcoder, self.catalog)

        self.assertIn("Manual primary-source spot-check hints", prompt)
        self.assertIn("Table 9", prompt)
        self.assertIn("StarCoder2-7B", prompt)

    def test_required_manual_benchmark_hint_is_a_publication_gate(self) -> None:
        starcoder = next(
            unit
            for unit in self.units
            if unit["key"]
            == "build-nvidia-com-bigcode-starcoder2-7b-b4e247a817"
        )
        dossier = {
            "family": starcoder["key"],
            "identity": {
                "upstreamName": "StarCoder2-7B",
                "checkpoint": "bigcode/starcoder2-7b",
                "architecture": "Transformer",
            },
            "sources": [
                {
                    "url": "https://arxiv.org/html/2402.19173",
                    "primary": True,
                }
            ],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }

        errors = research_catalog.semantic_model_errors(starcoder, dossier)
        self.assertTrue(
            any("requires an exact benchmark row" in error for error in errors),
            errors,
        )

        dossier["benchmarks"] = [
            {
                "modelScope": "StarCoder2-7B",
                "split": "test",
                "sourceLocator": "Table 9, StarCoder2-7B row",
                "sourceUrl": "https://arxiv.org/html/2402.19173",
                "value": "35.4",
            }
        ]
        errors = research_catalog.semantic_model_errors(starcoder, dossier)
        self.assertFalse(
            any("requires an exact benchmark row" in error for error in errors),
            errors,
        )

    def test_audit_accepts_flat_and_legacy_provider_shapes(self) -> None:
        unit = self.units[0]
        flat = {
            "family": unit["key"],
            "researchSummary": "summary",
        }
        dossier, metadata, dropped = research_catalog.extract_audited_dossier(
            unit,
            flat,
        )
        self.assertEqual(dossier, flat)
        self.assertEqual(metadata, {})
        self.assertEqual(dropped, [])

        legacy = {
            "verdict": "revised",
            "correctedDossier": {
                "family": unit["key"],
                "identity": {"checkpointRevision": "provider-only alias"},
            },
            "researchSummary": "merged from a provider spill",
            "think_sources": ["internal provider scratch field"],
        }
        dossier, metadata, dropped = research_catalog.extract_audited_dossier(
            unit,
            legacy,
        )
        self.assertEqual(dossier["family"], unit["key"])
        self.assertEqual(
            dossier["researchSummary"],
            "merged from a provider spill",
        )
        self.assertNotIn("checkpointRevision", dossier["identity"])
        self.assertNotIn("think_sources", dossier)
        self.assertEqual(dropped, ["$.identity.checkpointRevision"])
        self.assertEqual(metadata["verdict"], "revised")

    def test_audit_losslessly_flattens_evidence_url_wrappers(self) -> None:
        unit = self.units[0]
        flat = {
            "family": unit["key"],
            "identity": {
                "evidenceUrls": [
                    {"url": "https://example.com/model"},
                ]
            },
        }

        dossier, _, normalized = research_catalog.extract_audited_dossier(unit, flat)

        self.assertEqual(
            dossier["identity"]["evidenceUrls"],
            ["https://example.com/model"],
        )
        self.assertEqual(
            normalized,
            ["normalized:$.identity.evidenceUrls[0]"],
        )

    def test_audit_losslessly_flattens_evidence_gap_statement_wrappers(self) -> None:
        unit = self.units[0]
        flat = {
            "family": unit["key"],
            "evidenceGaps": [
                {"statement": "Evidence gap: exact result not reported."},
            ],
        }

        dossier, _, normalized = research_catalog.extract_audited_dossier(unit, flat)

        self.assertEqual(
            dossier["evidenceGaps"],
            ["Evidence gap: exact result not reported."],
        )
        self.assertEqual(
            normalized,
            ["normalized:$.evidenceGaps[0]"],
        )

    def test_reconcile_only_indexes_child_of_verified_first_party_source(self) -> None:
        dossier = {
            "identity": {
                "evidenceUrls": [
                    "https://huggingface.co/vendor/model/blob/main/config.json",
                    "https://example.com/unrelated",
                ]
            },
            "sources": [
                {
                    "title": "Exact model",
                    "url": "https://huggingface.co/vendor/model",
                    "publisher": "Vendor",
                    "sourceType": "model-card",
                    "primary": True,
                    "primaryReason": "First party.",
                    "modelScope": "vendor/model",
                    "supports": ["identity"],
                }
            ],
        }

        reconciled, urls = research_catalog.reconcile_cited_child_sources(
            {"kind": "model"},
            dossier,
        )

        self.assertEqual(
            urls,
            ["https://huggingface.co/vendor/model/blob/main/config.json"],
        )
        self.assertEqual(len(reconciled["sources"]), 2)
        self.assertNotIn(
            "https://example.com/unrelated",
            {item["url"] for item in reconciled["sources"]},
        )

    def test_reconcile_indexes_ngc_child_of_verified_container_source(self) -> None:
        root = (
            "https://catalog.ngc.nvidia.com/orgs/nim/bigcode/"
            "containers/starcoder2-7b/2.0.6"
        )
        child = f"{root}/governing-terms"
        dossier = {
            "limitations": [{"evidenceUrls": [child]}],
            "sources": [
                {
                    "title": "Exact NGC container release",
                    "url": root,
                    "publisher": "NVIDIA",
                    "sourceType": "official-documentation",
                    "primary": True,
                    "primaryReason": "First-party NVIDIA container record.",
                    "modelScope": "bigcode/starcoder2-7b NIM 2.0.6",
                    "supports": ["runtime identity"],
                }
            ],
        }

        reconciled, urls = research_catalog.reconcile_cited_child_sources(
            {"kind": "model"},
            dossier,
        )

        self.assertEqual(urls, [child])
        self.assertEqual(reconciled["sources"][1]["url"], child)

    def test_group_child_source_reconciliation_uses_group_schema(self) -> None:
        dossier = {
            "decisionRules": [
                {
                    "evidenceUrls": [
                        "https://github.com/vendor/model/blob/main/README.md"
                    ]
                }
            ],
            "sources": [
                {
                    "title": "Exact model",
                    "url": "https://github.com/vendor/model",
                    "publisher": "Vendor",
                    "primary": True,
                    "supports": ["model selection"],
                }
            ],
        }

        reconciled, urls = research_catalog.reconcile_cited_child_sources(
            {"kind": "group"},
            dossier,
        )

        self.assertEqual(
            urls,
            ["https://github.com/vendor/model/blob/main/README.md"],
        )
        child = reconciled["sources"][1]
        self.assertEqual(
            set(child),
            {"title", "url", "publisher", "primary", "supports"},
        )

    def test_child_source_reconciliation_quarantines_malformed_parent(self) -> None:
        child = "https://huggingface.co/vendor/model/blob/main/config.json"
        dossier = {
            "identity": {"evidenceUrls": [child]},
            "sources": [
                {
                    "url": "https://huggingface.co/vendor/model",
                    "publisher": "Vendor",
                    "sourceType": "model-card",
                    "primary": True,
                    "primaryReason": "First party.",
                    "modelScope": "vendor/model",
                    "supports": ["identity"],
                }
            ],
        }

        reconciled, urls = research_catalog.reconcile_cited_child_sources(
            {"kind": "model"},
            dossier,
        )

        self.assertEqual(urls, [])
        self.assertEqual(reconciled, dossier)

    def test_reconcile_indexes_cited_allowlisted_official_source(self) -> None:
        source_url = (
            "https://docs.nvidia.com/nim/nemo-retriever/"
            "text-embedding/2.2.0/use-the-api-openai.html"
        )
        dossier = {
            "inputPreparation": {
                "acceptedFormats": [
                    {"statement": "OpenAI-compatible text input.", "evidenceUrls": [source_url]}
                ]
            },
            "sources": [],
        }

        reconciled, urls = research_catalog.reconcile_cited_official_sources(
            {
                "kind": "model",
                "key": "nvidia-embedder",
                "modelFamilies": ["nvidia-embedder"],
                "sourceUrls": ["https://build.nvidia.com/nvidia/embedder"],
            },
            dossier,
        )

        self.assertEqual(urls, [source_url])
        self.assertEqual(reconciled["sources"][0]["url"], source_url)
        self.assertEqual(
            reconciled["sources"][0]["sourceType"],
            "official-documentation",
        )

    def test_reconcile_does_not_index_secondary_or_unrelated_citations(self) -> None:
        blog_url = (
            "https://developer.nvidia.com/blog/"
            "turn-complex-documents-into-usable-data"
        )
        unrelated_url = "https://example.com/model"
        dossier = {
            "limitations": [
                {"statement": "Claim.", "evidenceUrls": [blog_url, unrelated_url]}
            ],
            "sources": [],
        }

        reconciled, urls = research_catalog.reconcile_cited_official_sources(
            {
                "kind": "model",
                "key": "model",
                "modelFamilies": ["model"],
                "sourceUrls": ["https://build.nvidia.com/nvidia/model"],
            },
            dossier,
        )

        self.assertEqual(urls, [])
        self.assertEqual(reconciled, dossier)

    def test_group_official_source_reconciliation_uses_group_schema(self) -> None:
        source_url = "https://huggingface.co/nvidia/Cosmos-Reason2-8B"
        dossier = {
            "decisionRules": [
                {"evidenceUrls": [source_url]},
            ],
            "sources": [],
        }

        reconciled, urls = research_catalog.reconcile_cited_official_sources(
            {
                "kind": "group",
                "key": "physical-ai--physical-ai",
                "forgeModels": [
                    {
                        "sourceUrl": "https://huggingface.co/nvidia/Cosmos-Reason2-8B"
                    }
                ],
            },
            dossier,
        )

        self.assertEqual(urls, [source_url])
        self.assertEqual(
            set(reconciled["sources"][0]),
            {"title", "url", "publisher", "primary", "supports"},
        )

    def test_group_rules_require_and_cover_exact_forge_candidate_slugs(self) -> None:
        unit = {
            "kind": "group",
            "key": "general--example",
            "category": "general",
            "group": "example",
            "forgeModels": [
                {
                    "slug": "forge-model-a",
                    "sourceUrl": "https://huggingface.co/creator/model-a",
                },
                {
                    "slug": "forge-model-b",
                    "sourceUrl": "https://huggingface.co/creator/model-b",
                },
            ],
        }
        dossier = {
            "category": "general",
            "group": "example",
            "sources": [
                {
                    "url": "https://huggingface.co/creator/model-a",
                    "primary": True,
                },
                {
                    "url": "https://huggingface.co/creator/model-b",
                    "primary": True,
                },
            ],
            "decisionRules": [
                {
                    "prefer": "creator/model-a",
                    "alternatives": ["forge-model-a because it is smaller"],
                    "evidenceUrls": [
                        "https://huggingface.co/creator/model-a",
                    ],
                }
            ],
        }

        errors = research_catalog.semantic_group_errors(unit, dossier)

        self.assertTrue(any(".prefer must be an exact Forge" in e for e in errors))
        self.assertTrue(any(".alternatives[0]" in e for e in errors))
        self.assertTrue(any("forge-model-b" in e and "do not cover" in e for e in errors))

        dossier["decisionRules"] = [
            {
                "prefer": "forge-model-a",
                "alternatives": ["forge-model-b"],
                "evidenceUrls": [
                    "https://huggingface.co/creator/model-a",
                    "https://huggingface.co/creator/model-b",
                ],
            }
        ]
        self.assertEqual(
            research_catalog.semantic_group_errors(unit, dossier),
            [],
        )

        dossier["decisionRules"] = [
            {
                "prefer": "forge-model-a",
                "alternatives": [
                    "forge-model-a",
                    "forge-model-b",
                    "forge-model-b",
                ],
                "evidenceUrls": [
                    "https://huggingface.co/creator/model-a",
                    "https://huggingface.co/creator/model-b",
                ],
            }
        ]
        errors = research_catalog.semantic_group_errors(unit, dossier)
        self.assertTrue(any("must not contain duplicates" in e for e in errors))
        self.assertTrue(any("must not repeat the preferred" in e for e in errors))

    def test_malformed_group_rule_is_reported_without_crashing_semantics(self) -> None:
        unit = {
            "kind": "group",
            "key": "general--example",
            "category": "general",
            "group": "example",
            "forgeModels": [],
        }
        dossier = {
            "category": "general",
            "group": "example",
            "sources": [],
            "decisionRules": ["not-an-object"],
        }

        errors = research_catalog.validate_dossier(unit, dossier)

        self.assertTrue(
            any("$.decisionRules[0]: expected object" in error for error in errors),
            errors,
        )

        dossier["sources"] = ["not-an-object"]
        dossier["decisionRules"] = [{"prefer": "", "alternatives": "not-a-list"}]
        malformed_collection_errors = research_catalog.validate_dossier(unit, dossier)
        self.assertTrue(
            any("$.sources[0]: expected object" in error for error in malformed_collection_errors),
            malformed_collection_errors,
        )
        self.assertTrue(
            any(
                "$.decisionRules[0].alternatives: expected array" in error
                for error in malformed_collection_errors
            ),
            malformed_collection_errors,
        )

    def test_group_sources_reject_aggregators_and_unapproved_repositories(self) -> None:
        unit = {
            "kind": "group",
            "key": "general--example",
            "category": "general",
            "group": "example",
            "forgeModels": [
                {
                    "slug": "forge-model-a",
                    "modelFamily": "creator-model-a",
                    "sourceUrl": "https://huggingface.co/creator/model-a",
                }
            ],
        }
        base_dossier = {
            "category": "general",
            "group": "example",
            "decisionRules": [
                {
                    "prefer": "forge-model-a",
                    "alternatives": [],
                    "evidenceUrls": [],
                }
            ],
        }
        cases = (
            (
                "https://benchmarklist.com/benchmarks/example",
                "uses forbidden secondary host",
            ),
            (
                "https://huggingface.co/hunyuanvideo-community/reupload",
                "third-party mirror/example repository",
            ),
            (
                "https://github.com/vllm-project/runtime-example",
                "uses unapproved repository owner",
            ),
            (
                "https://huggingface.co/models?other=example",
                "uses forbidden secondary URL",
            ),
        )
        for url, expected in cases:
            dossier = {
                **base_dossier,
                "sources": [
                    {
                        "url": "https://huggingface.co/creator/model-a",
                        "primary": True,
                    },
                    {"url": url, "primary": True},
                ],
            }

            with self.subTest(url=url):
                errors = research_catalog.semantic_group_errors(unit, dossier)
                self.assertTrue(
                    any(expected in error for error in errors),
                    errors,
                )

    def test_group_repository_owners_include_every_exact_candidate(self) -> None:
        unit = {
            "forgeModels": [
                {
                    "modelFamily": "qwen-qwen-image",
                    "sourceUrl": "https://huggingface.co/Qwen/Qwen-Image",
                },
                {
                    "modelFamily": "black-forest-labs-flux",
                    "sourceUrl": "https://github.com/black-forest-labs/flux",
                },
            ]
        }

        owners = research_catalog.allowed_repository_owners(unit)

        self.assertIn("qwen", owners)
        self.assertIn("black-forest-labs", owners)
        self.assertNotIn("unrelated-user", owners)

    def test_malformed_model_shapes_are_reported_without_semantic_crash(self) -> None:
        unit = {
            "kind": "model",
            "key": "exact-model",
            "modelFamilies": [],
            "sourceUrls": [],
        }
        dossier = {
            "family": "exact-model",
            "identity": "not-an-object",
            "sources": ["not-an-object"],
            "benchmarks": ["not-an-object"],
            "recommendedUseCases": ["not-an-object"],
            "inputPreparation": "not-an-object",
            "outputInterpretation": "not-an-object",
        }

        errors = research_catalog.validate_dossier(unit, dossier)

        self.assertTrue(any("$.identity: expected object" in error for error in errors))
        self.assertTrue(any("$.sources[0]: expected object" in error for error in errors))

    def test_reconcile_indexes_exact_non_generic_forge_starting_source(self) -> None:
        unit = {
            "kind": "model",
            "key": "starcoder",
            "modelFamilies": ["bigcode-starcoder2-7b"],
            "sourceUrls": [
                "https://build.nvidia.com/bigcode/starcoder2-7b",
                "https://build.nvidia.com",
            ],
        }
        dossier = {"sources": []}

        reconciled, urls = research_catalog.reconcile_required_starting_sources(
            unit,
            dossier,
        )

        self.assertEqual(
            urls,
            ["https://build.nvidia.com/bigcode/starcoder2-7b"],
        )
        self.assertEqual(len(reconciled["sources"]), 1)

    def test_reconcile_preserves_trailing_slash_in_exact_starting_source(
        self,
    ) -> None:
        source_url = "https://docs.nvidia.com/nim/bionemo/genmol/latest/"
        unit = {
            "kind": "model",
            "key": "genmol",
            "modelFamilies": ["nvidia-genmol"],
            "sourceUrls": [source_url],
        }

        reconciled, urls = research_catalog.reconcile_required_starting_sources(
            unit,
            {"sources": []},
        )

        self.assertEqual(urls, [source_url])
        self.assertEqual(reconciled["sources"][0]["url"], source_url)

    def test_group_reconcile_indexes_every_exact_candidate_source(self) -> None:
        unit = {
            "kind": "group",
            "key": "general--language",
            "forgeModels": [
                {
                    "slug": "forge-model-a",
                    "sourceUrl": "https://huggingface.co/creator/model-a",
                },
                {
                    "slug": "forge-model-b",
                    "sourceUrl": "https://build.nvidia.com/creator/model-b",
                },
                {
                    "slug": "forge-model-c",
                    "sourceUrl": "https://build.nvidia.com",
                },
            ],
        }

        reconciled, urls = research_catalog.reconcile_required_starting_sources(
            unit,
            {"sources": []},
        )

        self.assertEqual(
            urls,
            [
                "https://huggingface.co/creator/model-a",
                "https://build.nvidia.com/creator/model-b",
            ],
        )
        self.assertEqual(
            {item["url"] for item in reconciled["sources"]},
            set(urls),
        )
        self.assertTrue(
            all(
                set(item)
                == {"title", "url", "publisher", "primary", "supports"}
                for item in reconciled["sources"]
            )
        )

    def test_reconcile_adds_structured_human_reviewed_primary_evidence(self) -> None:
        row = {
            "task": "Code generation",
            "dataset": "HumanEval",
            "split": "test",
            "metric": "pass@1",
            "value": "35.4",
            "direction": "higher-is-better",
            "modelScope": "StarCoder2-7B",
            "conditions": "Greedy decoding",
            "sourceUrl": "https://arxiv.org/html/2402.19173",
            "sourceLocator": "Table 9",
            "caveats": [],
        }
        unit = {
            "kind": "model",
            "key": "starcoder2",
            "modelFamilies": ["bigcode-starcoder2-7b"],
            "manualReviewHints": [
                {
                    "sourceUrl": "https://arxiv.org/html/2402.19173",
                    "sourceTitle": "The StarCoder2 paper",
                    "publisher": "BigCode",
                    "sourceType": "paper",
                    "benchmarkRows": [row],
                }
            ],
        }

        reconciled, repaired = research_catalog.reconcile_manual_review_evidence(
            unit,
            {"sources": [], "benchmarks": []},
        )

        self.assertEqual(reconciled["sources"][0]["url"], row["sourceUrl"])
        self.assertEqual(reconciled["benchmarks"], [row])
        self.assertEqual(len(repaired), 2)

    def test_reconcile_adds_human_reviewed_creator_source_without_benchmark(
        self,
    ) -> None:
        source_url = "https://docs.thehive.ai/reference/deepfake-detection-1"
        unit = {
            "kind": "model",
            "key": "hive-deepfake",
            "modelFamilies": ["hive-deepfake-image-detection"],
            "manualReviewHints": [
                {
                    "requireSource": True,
                    "sourceUrl": source_url,
                    "sourceTitle": "Deepfake Detection",
                    "publisher": "Hive",
                    "sourceType": "official-documentation",
                }
            ],
        }

        reconciled, repaired = research_catalog.reconcile_manual_review_evidence(
            unit,
            {"sources": [], "benchmarks": []},
        )

        self.assertEqual(reconciled["sources"][0]["url"], source_url)
        self.assertEqual(reconciled["benchmarks"], [])
        self.assertEqual(repaired, [source_url])
        self.assertIn(
            "primary-source provenance",
            reconciled["sources"][0]["supports"][0],
        )

    def test_manual_model_benchmarks_do_not_add_fields_to_group_dossiers(
        self,
    ) -> None:
        dossier = {
            "category": "general",
            "group": "embeddings",
            "sources": [],
        }

        reconciled, repaired = research_catalog.reconcile_manual_review_evidence(
            {
                "kind": "group",
                "key": "general--embeddings",
                "manualReviewHints": [],
            },
            dossier,
        )

        self.assertEqual(reconciled, dossier)
        self.assertEqual(repaired, [])
        self.assertNotIn("benchmarks", reconciled)

    def test_invalid_benchmark_placeholders_are_discarded(self) -> None:
        dossier = {
            "benchmarks": [
                {"value": "not reported"},
                {"value": "Evidence gap: no result"},
                {"value": "35.4"},
            ]
        }

        normalized, discarded = (
            research_catalog.discard_invalid_benchmark_placeholders(dossier)
        )

        self.assertEqual(normalized["benchmarks"], [{"value": "35.4"}])
        self.assertEqual(
            discarded,
            ["discarded:$.benchmarks[0]", "discarded:$.benchmarks[1]"],
        )

    def test_benchmark_cleanup_does_not_add_model_fields_to_group_dossiers(
        self,
    ) -> None:
        dossier = {
            "category": "physical-ai",
            "group": "physical-ai",
            "sources": [],
        }

        normalized, discarded = (
            research_catalog.discard_invalid_benchmark_placeholders(dossier)
        )

        self.assertEqual(normalized, dossier)
        self.assertEqual(discarded, [])
        self.assertNotIn("benchmarks", normalized)

    def test_unreferenced_forbidden_source_is_discarded(self) -> None:
        dossier = {
            "sources": [
                {
                    "url": "https://developer.nvidia.com/blog/secondary",
                    "primary": True,
                },
                {
                    "url": "https://huggingface.co/owner/model",
                    "primary": True,
                },
            ],
            "decisionRules": [
                {
                    "evidenceUrls": ["https://huggingface.co/owner/model"],
                }
            ],
        }

        normalized, discarded = (
            research_catalog.discard_unreferenced_forbidden_sources(dossier)
        )

        self.assertEqual(
            [source["url"] for source in normalized["sources"]],
            ["https://huggingface.co/owner/model"],
        )
        self.assertEqual(discarded, ["discarded:$.sources[0]"])

    def test_cited_forbidden_source_remains_for_strict_validation(self) -> None:
        url = "https://developer.nvidia.com/blog/secondary"
        dossier = {
            "sources": [{"url": url, "primary": True}],
            "decisionRules": [{"evidenceUrls": [url]}],
        }

        normalized, discarded = (
            research_catalog.discard_unreferenced_forbidden_sources(dossier)
        )

        self.assertEqual(normalized, dossier)
        self.assertEqual(discarded, [])

    def test_flat_audit_metadata_is_derived_from_the_correction(self) -> None:
        draft = {
            "dossier": {"family": "before"},
            "validation": {"errors": ["$.sources must contain a primary source"]},
        }
        verdict, summary, issues = research_catalog.derived_audit_metadata(
            draft,
            {"family": "after"},
            {},
            ["$.think_sources"],
        )
        self.assertEqual(verdict, "revised")
        self.assertIn("Independent primary-source verification", summary)
        self.assertEqual(len(issues), 2)
        self.assertIn("primary source", issues[0]["issue"])
        self.assertEqual(issues[1]["path"], "$.think_sources")

    def test_audit_prompt_repeats_manual_review_hints_after_retry_feedback(self) -> None:
        unit = {
            "kind": "model",
            "key": "exact-model",
            "manualReviewHints": [
                {
                    "sourceUrl": "https://arxiv.org/html/1234.5678",
                    "sourceLocator": "Table 9",
                    "requireBenchmark": True,
                }
            ],
        }

        prompt = research_catalog.audit_prompt(
            unit,
            {"family": "exact-model"},
            retry_feedback=["manual benchmark is missing"],
        )

        feedback_index = prompt.index("manual benchmark is missing")
        repeated_hint_index = prompt.rindex("https://arxiv.org/html/1234.5678")
        self.assertGreater(repeated_hint_index, feedback_index)
        self.assertIn("Non-negotiable manual-review hints", prompt)

    def test_group_audit_prompt_repeats_exact_slug_checklist_last(self) -> None:
        unit = {
            "kind": "group",
            "key": "general--example",
            "category": "general",
            "group": "example",
            "forgeModels": [
                {"slug": "exact-model-a"},
                {"slug": "exact-model-b"},
            ],
        }

        prompt = research_catalog.audit_prompt(
            unit,
            {"category": "general", "group": "example"},
            retry_feedback=["exact-model-b was not covered"],
        )

        checklist_index = prompt.rindex("final exact Forge candidate checklist")
        self.assertGreater(checklist_index, prompt.index("exact-model-b was not covered"))
        self.assertGreater(prompt.rindex('"exact-model-a"'), checklist_index)
        self.assertGreater(prompt.rindex('"exact-model-b"'), checklist_index)

    def test_best_audit_attempt_revalidates_against_current_policy(self) -> None:
        unit = {"kind": "group", "key": "general--example"}
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            attempt_dir = root / "group" / unit["key"]
            attempt_dir.mkdir(parents=True)
            (attempt_dir / "weaker.json").write_text(
                json.dumps(
                    {
                        "requestId": "weaker",
                        "dossier": {"group": "weaker", "freshErrors": 3},
                        "validationErrors": [],
                    }
                ),
                encoding="utf-8",
            )
            (attempt_dir / "stronger.json").write_text(
                json.dumps(
                    {
                        "requestId": "stronger",
                        "dossier": {"group": "stronger", "freshErrors": 1},
                        "validationErrors": ["stale", "stale", "stale"],
                    }
                ),
                encoding="utf-8",
            )
            (attempt_dir / "malformed.json").write_text("{", encoding="utf-8")

            with (
                patch.object(research_catalog, "AUDIT_ATTEMPT_RESULTS", root),
                patch.object(
                    research_catalog,
                    "validate_dossier",
                    side_effect=lambda _unit, dossier: [
                        f"fresh-{index}"
                        for index in range(dossier["freshErrors"])
                    ],
                ),
            ):
                result = research_catalog.best_audit_attempt(unit)

        self.assertIsNotNone(result)
        self.assertEqual(result["requestId"], "stronger")
        self.assertEqual(result["validationErrors"], ["fresh-0"])

    def test_retry_feedback_preserves_equal_strength_failure_history(self) -> None:
        unit = {"kind": "model", "key": "example"}
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            attempt_dir = root / "model" / unit["key"]
            attempt_dir.mkdir(parents=True)
            for name, errors in (
                ("missing-gap", ["missing benchmark evidence gap"]),
                ("secondary-source", ["forbidden secondary source"]),
                ("weaker", ["one", "two"]),
            ):
                (attempt_dir / f"{name}.json").write_text(
                    json.dumps(
                        {
                            "requestId": name,
                            "dossier": {"currentErrors": errors},
                        }
                    ),
                    encoding="utf-8",
                )

            with (
                patch.object(research_catalog, "AUDIT_ATTEMPT_RESULTS", root),
                patch.object(
                    research_catalog,
                    "validate_dossier",
                    side_effect=lambda _unit, dossier: dossier["currentErrors"],
                ),
            ):
                feedback = research_catalog.audit_attempt_retry_feedback(unit)

        self.assertCountEqual(
            feedback,
            ["missing benchmark evidence gap", "forbidden secondary source"],
        )
        self.assertNotIn("one", feedback)
        self.assertNotIn("two", feedback)

    def test_public_result_redacts_provider_request_ids(self) -> None:
        payload = {
            "provenance": {
                "provider": "Tavily Research",
                "requestId": "result",
                "draftRequestId": "draft",
                "auditRequestId": "audit",
                "promptSha256": "0" * 64,
            }
        }

        redacted = research_catalog.redact_public_provider_request_ids(payload)

        self.assertEqual(payload["provenance"]["requestId"], "result")
        self.assertEqual(
            redacted["provenance"],
            {
                "provider": "Tavily Research",
                "promptSha256": "0" * 64,
            },
        )

    def test_submission_slots_never_exceed_the_active_bound(self) -> None:
        state = {
            "jobs": {
                "draft:model:a": {"status": "in_progress"},
                "draft:model:b": {"status": "created"},
                "draft:model:c": {"status": "pending"},
                "draft:model:d": {"status": "completed"},
                "draft:model:e": {"status": "failed"},
            }
        }
        selected = set(state["jobs"])
        active, available = research_catalog.available_submission_slots(
            state,
            selected,
            max_active=2,
        )
        self.assertEqual(active, 3)
        self.assertEqual(available, 0)

    def test_model_and_group_controllers_use_distinct_state_files(self) -> None:
        self.assertNotEqual(
            research_catalog.state_path("models"),
            research_catalog.state_path("groups"),
        )
        self.assertEqual(
            research_catalog.state_path("models").name,
            "jobs-models.json",
        )

    def test_accepted_output_is_revalidated_against_current_contract(self) -> None:
        unit = self.units[0]
        path = research_catalog.output_path(unit)
        original_exists = path.exists()
        original = path.read_bytes() if original_exists else None
        try:
            research_catalog.write_json(
                path,
                {
                    "validation": {"status": "accepted"},
                    "audit": {"verdict": "accepted"},
                    "dossier": {"family": unit["key"]},
                },
            )
            self.assertFalse(research_catalog.has_accepted_output(unit))
        finally:
            if original_exists and original is not None:
                path.write_bytes(original)
            else:
                path.unlink(missing_ok=True)

    def test_audit_attempt_history_path_cannot_escape_state_directory(self) -> None:
        path = research_catalog.audit_attempt_path(
            self.units[0],
            "../../provider/request",
        )
        self.assertTrue(path.is_relative_to(research_catalog.AUDIT_ATTEMPT_RESULTS))
        self.assertNotIn("..", path.name)

    def test_community_discussions_and_paper_mirrors_are_not_primary(self) -> None:
        unit = self.units[0]
        dossier = {
            "family": unit["key"],
            "sources": [
                {
                    "url": "https://huggingface.co/vendor/model/discussions/5",
                    "primary": True,
                },
                {
                    "url": "https://rivaslab.org/teaching/paper.pdf",
                    "primary": True,
                },
                {
                    "url": "https://developer.nvidia.com/blog/model-summary",
                    "primary": True,
                },
                {
                    "url": "https://ollama.com/library/example-model",
                    "primary": True,
                },
                {
                    "url": "https://ai.azure.com/catalog/models/example-model",
                    "primary": True,
                },
                {
                    "url": "https://huggingface.co/papers/2401.00001",
                    "primary": True,
                },
                {
                    "url": "https://hf-mirror.com/vendor/example-model",
                    "primary": True,
                },
            ],
            "benchmarks": [],
            "limitations": [],
            "safety": [],
        }
        errors = research_catalog.semantic_model_errors(unit, dossier)
        self.assertTrue(
            any("huggingface.co/vendor/model/discussions/5" in error for error in errors),
            errors,
        )
        self.assertTrue(
            any("rivaslab.org" in error for error in errors),
            errors,
        )
        self.assertTrue(
            any("developer.nvidia.com" in error for error in errors),
            errors,
        )
        self.assertTrue(
            any("ollama.com" in error for error in errors),
            errors,
        )
        self.assertTrue(
            any("ai.azure.com" in error for error in errors),
            errors,
        )

    def test_empty_benchmark_and_comparison_lists_require_specific_gaps(self) -> None:
        unit = {"key": "example-model", "sourceUrls": ["https://example.com/model"]}
        dossier = {
            "family": "example-model",
            "sources": [
                {
                    "url": "https://example.com/model",
                    "primary": True,
                }
            ],
            "benchmarks": [],
            "comparisons": [],
            "limitations": [],
            "safety": [],
            "evidenceGaps": [],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertIn(
            "$.benchmarks is empty without a benchmark-specific evidence gap",
            errors,
        )
        self.assertIn(
            "$.comparisons is empty without a comparison-specific evidence gap",
            errors,
        )

    def test_documented_benchmark_and_comparison_gaps_are_accepted(self) -> None:
        unit = {"key": "example-model", "sourceUrls": ["https://example.com/model"]}
        dossier = {
            "family": "example-model",
            "sources": [
                {
                    "url": "https://example.com/model",
                    "primary": True,
                }
            ],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [
                {
                    "evidenceUrls": ["https://example.com/model"],
                }
            ],
            "avoidUseCases": [{}],
            "limitations": [
                {
                    "statement": "Evidence gap: no additional limitation was reported.",
                    "evidenceUrls": [],
                }
            ],
            "safety": [
                {
                    "statement": "Forge policy: require human review.",
                    "evidenceUrls": [],
                }
            ],
            "inputPreparation": {
                "semanticInputs": [
                    {
                        "statement": "An exact input claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
                "acceptedFormats": [
                    {
                        "statement": "An exact format claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
                "preprocessing": [
                    {
                        "statement": "An exact preprocessing claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
                "validation": [
                    {
                        "statement": "An exact input validation claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
            },
            "outputInterpretation": {
                "outputs": [
                    {
                        "statement": "An exact output claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
                "interpretation": [
                    {
                        "statement": "An exact interpretation claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
                "validation": [
                    {
                        "statement": "An exact output validation claim.",
                        "evidenceUrls": ["https://example.com/model"],
                    }
                ],
            },
            "evidenceGaps": [
                (
                    "Evidence gap: no exact-checkpoint benchmark was reported in "
                    "the checked model-card Evaluation section at "
                    "https://example.com/model."
                ),
                "Evidence gap: no protocol-matched peer comparison was reported.",
            ],
        }

        self.assertEqual(
            research_catalog.semantic_model_errors(unit, dossier),
            [],
        )

    def test_empty_benchmark_gap_must_name_checked_source_and_locator(self) -> None:
        unit = {"key": "example-model", "sourceUrls": []}
        dossier = {
            "family": "example-model",
            "sources": [],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [
                "Evidence gap: no exact-checkpoint benchmark was reported.",
                "Evidence gap: no protocol-matched peer comparison was reported.",
            ],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertTrue(
            any("naming the exact primary-source URL" in error for error in errors),
            errors,
        )

    def test_empty_benchmark_gap_accepts_exact_checked_sections_plural(self) -> None:
        unit = {"key": "example-model", "sourceUrls": []}
        dossier = {
            "family": "example-model",
            "sources": [],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [
                (
                    "Evidence gap: no exact-checkpoint benchmark was reported at "
                    "https://example.com/model after checking the Evaluation and "
                    "Benchmark results sections."
                ),
                "Evidence gap: no protocol-matched peer comparison was reported.",
            ],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertFalse(
            any("naming the exact primary-source URL" in error for error in errors),
            errors,
        )

    def test_generic_vendor_landing_page_is_not_required_as_dossier_evidence(self) -> None:
        unit = {
            "key": "example-model",
            "sourceUrls": ["https://build.nvidia.com"],
        }
        dossier = {
            "family": "example-model",
            "sources": [
                {
                    "url": "https://docs.nvidia.com/nim/example/model-card.html",
                    "primary": True,
                }
            ],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [
                {
                    "evidenceUrls": [
                        "https://docs.nvidia.com/nim/example/model-card.html"
                    ],
                }
            ],
            "avoidUseCases": [{}],
            "limitations": [
                {
                    "statement": "Evidence gap: no further limitation was reported.",
                    "evidenceUrls": [],
                }
            ],
            "safety": [
                {
                    "statement": "Forge policy: require human review.",
                    "evidenceUrls": [],
                }
            ],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [
                "Evidence gap: no exact-checkpoint benchmark was reported.",
                "Evidence gap: no protocol-matched peer comparison was reported.",
                "Evidence gap: semantic input type was not reported.",
                "Evidence gap: accepted input format was not reported.",
                "Evidence gap: preprocessing was not reported.",
                "Evidence gap: input validation bounds were not reported.",
                "Evidence gap: output shape was not reported.",
                "Evidence gap: output interpretation was not reported.",
                "Evidence gap: post-inference output validation was not reported.",
            ],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertFalse(
            any("official starting source" in error for error in errors),
            errors,
        )

    def test_instruct_variant_cannot_be_replaced_by_base_checkpoint_identity(self) -> None:
        unit = {
            "key": "llama-instruct",
            "modelFamilies": ["meta-llama-3-1-70b-instruct"],
            "sourceUrls": [],
        }
        dossier = {
            "family": "llama-instruct",
            "identity": {
                "upstreamName": "Llama 3.1 70B",
                "checkpoint": "Llama-3.1-70B",
                "architecture": "decoder-only transformer",
            },
            "sources": [],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertIn(
            "$.identity must preserve the covered Instruct checkpoint/task suffix",
            errors,
        )

    def test_nvidia_packaged_third_party_requires_creator_primary_source(self) -> None:
        unit = {
            "key": "starcoder",
            "modelFamilies": ["bigcode-starcoder2-7b"],
            "sourceUrls": ["https://build.nvidia.com/bigcode/starcoder2-7b"],
        }
        nvidia_only = {
            "family": "starcoder",
            "sources": [
                {
                    "url": "https://build.nvidia.com/bigcode/starcoder2-7b",
                    "primary": True,
                },
                {
                    "url": "https://docs.nvidia.com/nim/example.html",
                    "primary": True,
                },
                {
                    "url": "https://research.nvidia.com/publication/example",
                    "primary": True,
                },
            ],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }

        errors = research_catalog.semantic_model_errors(unit, nvidia_only)

        self.assertTrue(
            any("original creator's primary source" in error for error in errors),
            errors,
        )
        with_creator = json.loads(json.dumps(nvidia_only))
        with_creator["sources"].append(
            {
                "url": "https://huggingface.co/bigcode/starcoder2-7b",
                "primary": True,
            }
        )
        creator_errors = research_catalog.semantic_model_errors(unit, with_creator)
        self.assertFalse(
            any("original creator's primary source" in error for error in creator_errors),
            creator_errors,
        )

    def test_cross_provider_api_contract_cannot_transfer_to_nim(self) -> None:
        provider_url = (
            "https://alibabacloud.com/help/en/model-studio/"
            "qwen-image-edit-api"
        )
        unit = {
            "key": "qwen-image-edit",
            "modelFamilies": ["qwen-qwen-image-edit"],
            "sourceUrls": [],
        }
        dossier = {
            "family": "qwen-image-edit",
            "sources": [{"url": provider_url, "primary": True}],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {
                "acceptedFormats": [
                    {
                        "statement": "The hosted API accepts PNG and JPEG images.",
                        "evidenceUrls": [provider_url],
                    }
                ]
            },
            "outputInterpretation": {},
            "evidenceGaps": [],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertTrue(
            any("different cloud provider's hosted API" in error for error in errors),
            errors,
        )
        dossier["inputPreparation"]["acceptedFormats"][0]["statement"] = (
            "This provider-specific contract does not establish the NVIDIA NIM "
            "request format."
        )
        scoped_errors = research_catalog.semantic_model_errors(unit, dossier)
        self.assertFalse(
            any(
                "different cloud provider's hosted API" in error
                for error in scoped_errors
            ),
            scoped_errors,
        )

    def test_support_forums_aggregators_and_mirrors_are_secondary(self) -> None:
        unit = {"key": "example", "modelFamilies": [], "sourceUrls": []}
        for url in (
            "https://forums.developer.nvidia.com/t/example/1",
            "https://gromacs.bioexcel.eu/t/community-benchmark/1",
            "https://openapi.city/providers/nvidia-nim",
            "https://deeplearning.ai/the-batch/model-summary",
            "https://en.bioerrorlog.work/entry/model-paper",
            "https://mcpservers.org/agent-skills/vendor/model",
            "https://hub.docker.com/layers/example/image",
            "https://sourceforge.net/projects/example.mirror",
            "https://docs.vllm.ai/projects/example",
        ):
            dossier = {
                "family": "example",
                "sources": [{"url": url, "primary": True}],
                "benchmarks": [],
                "comparisons": [],
                "recommendedUseCases": [],
                "avoidUseCases": [],
                "limitations": [],
                "safety": [],
                "inputPreparation": {},
                "outputInterpretation": {},
                "evidenceGaps": [],
            }

            with self.subTest(url=url):
                errors = research_catalog.semantic_model_errors(unit, dossier)
                self.assertTrue(
                    any("uses forbidden secondary host" in error for error in errors),
                    errors,
                )

        self_described_secondary = {
            "family": "example",
            "sources": [
                {
                    "url": "https://official.example/model",
                    "primary": True,
                    "primaryReason": (
                        "Third-party documentation copied from a support forum."
                    ),
                }
            ],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }
        errors = research_catalog.semantic_model_errors(
            unit, self_described_secondary
        )
        self.assertTrue(
            any("describes itself as secondary evidence" in error for error in errors),
            errors,
        )

    def test_third_party_repository_mirrors_are_secondary(self) -> None:
        unit = {"key": "example", "modelFamilies": [], "sourceUrls": []}
        for url in (
            "https://github.com/ana-oprescu/GreenLLMs",
            "https://github.com/UFResearchComputing/MolMIM-NIM",
            "https://huggingface.co/calcuis/sd3.5-large-gguf",
            "https://huggingface.co/NousResearch/example",
            "https://huggingface.co/GaleneAI/example",
        ):
            dossier = {
                "family": "example",
                "sources": [{"url": url, "primary": True}],
                "benchmarks": [],
                "comparisons": [],
                "recommendedUseCases": [],
                "avoidUseCases": [],
                "limitations": [],
                "safety": [],
                "inputPreparation": {},
                "outputInterpretation": {},
                "evidenceGaps": [],
            }

            with self.subTest(url=url):
                errors = research_catalog.semantic_model_errors(unit, dossier)
                self.assertTrue(
                    any(
                        "third-party mirror/example repository" in error
                        for error in errors
                    ),
                    errors,
                )

    def test_repository_owner_must_match_exact_model_scope(self) -> None:
        qwen_unit = {
            "key": "qwen-image",
            "modelFamilies": ["qwen-qwen-image"],
            "sourceUrls": [],
        }
        self.assertIn("qwen", research_catalog.allowed_repository_owners(qwen_unit))
        self.assertNotIn(
            "unrelated-user",
            research_catalog.allowed_repository_owners(qwen_unit),
        )

        nvidia_unit = {
            "key": "nv-embedqa",
            "modelFamilies": ["nvidia-llama-3-2-nv-embedqa-1b-v2-nim"],
            "sourceUrls": [],
        }
        self.assertIn(
            "nvidia-ai-blueprints",
            research_catalog.allowed_repository_owners(nvidia_unit),
        )

        exact_source_unit = {
            "key": "custom",
            "modelFamilies": ["custom-model"],
            "sourceUrls": ["https://github.com/creator-org/custom-model"],
        }
        self.assertIn(
            "creator-org",
            research_catalog.allowed_repository_owners(exact_source_unit),
        )

        esmc_unit = {
            "key": "biohub-esmc-600m",
            "modelFamilies": ["biohub-esmc-600m-protein-embedding"],
            "sourceUrls": ["https://huggingface.co/biohub/ESMC-600M"],
        }
        self.assertIn(
            "evolutionaryscale",
            research_catalog.allowed_repository_owners(esmc_unit),
        )

        dossier = {
            "family": "qwen-image",
            "sources": [
                {
                    "url": "https://github.com/unrelated-user/qwen-reupload",
                    "primary": True,
                }
            ],
            "benchmarks": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }
        errors = research_catalog.semantic_model_errors(qwen_unit, dossier)
        self.assertTrue(
            any("uses unapproved repository owner" in error for error in errors),
            errors,
        )

    def test_generic_nvidia_build_source_detects_third_party_family(self) -> None:
        third_party = {
            "sourceUrls": ["https://build.nvidia.com"],
            "modelFamilies": ["meta-llama-3.1-70b-instruct"],
        }
        nvidia_owned = {
            "sourceUrls": ["https://build.nvidia.com"],
            "modelFamilies": ["nvidia-nv-embedqa-e5"],
        }

        self.assertTrue(
            research_catalog.requires_original_creator_source(third_party)
        )
        self.assertFalse(
            research_catalog.requires_original_creator_source(nvidia_owned)
        )

    def test_benchmark_gap_cannot_masquerade_as_numeric_result(self) -> None:
        unit = {"key": "example", "sourceUrls": [], "modelFamilies": []}
        dossier = {
            "family": "example",
            "sources": [],
            "benchmarks": [
                {
                    "modelScope": "example",
                    "split": "unspecified",
                    "sourceLocator": "not reported",
                    "value": "Evidence gap: no exact result was reported",
                }
            ],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }

        errors = research_catalog.semantic_model_errors(unit, dossier)

        self.assertIn(
            "$.benchmarks[0].value must contain a reported numeric result",
            errors,
        )
        self.assertTrue(
            any("sourceLocator must identify" in error for error in errors),
            errors,
        )

    def test_benchmark_locator_rejects_generic_table_or_paper_identifier(self) -> None:
        unit = {"key": "example", "sourceUrls": [], "modelFamilies": []}

        def errors_for(locator: str) -> list[str]:
            return research_catalog.semantic_model_errors(
                unit,
                {
                    "family": "example",
                    "sources": [],
                    "benchmarks": [
                        {
                            "modelScope": "example",
                            "split": "test",
                            "sourceLocator": locator,
                            "value": "42",
                        }
                    ],
                    "comparisons": [],
                    "recommendedUseCases": [],
                    "avoidUseCases": [],
                    "limitations": [],
                    "safety": [],
                    "inputPreparation": {},
                    "outputInterpretation": {},
                    "evidenceGaps": [],
                },
            )

        self.assertTrue(
            any(
                "sourceLocator must identify" in error
                for error in errors_for("Evaluation table (arXiv)")
            )
        )
        self.assertTrue(
            any(
                "sourceLocator must identify" in error
                for error in errors_for("arXiv abs 2402.19173")
            )
        )
        self.assertFalse(
            any(
                "sourceLocator must identify" in error
                for error in errors_for("Table 5, query latency row")
            )
        )

    def test_paper_benchmark_locator_requires_number_or_named_heading(self) -> None:
        unit = {"key": "example", "sourceUrls": [], "modelFamilies": []}
        base = {
            "family": "example",
            "sources": [],
            "comparisons": [],
            "recommendedUseCases": [],
            "avoidUseCases": [],
            "limitations": [],
            "safety": [],
            "inputPreparation": {},
            "outputInterpretation": {},
            "evidenceGaps": [],
        }

        def errors_for(locator: str) -> list[str]:
            dossier = json.loads(json.dumps(base))
            dossier["benchmarks"] = [
                {
                    "modelScope": "example",
                    "split": "test",
                    "sourceLocator": locator,
                    "sourceUrl": "https://arxiv.org/abs/1234.5678",
                    "value": "42",
                }
            ]
            return research_catalog.semantic_model_errors(unit, dossier)

        self.assertTrue(
            any(
                "sourceLocator for a paper" in error
                for error in errors_for(
                    "arXiv benchmarking table/section reporting runtime microbenchmarks"
                )
            )
        )
        self.assertFalse(
            any(
                "sourceLocator for a paper" in error
                for error in errors_for("Table 5, runtime microbenchmarks")
            )
        )

    def test_bionemo_and_nvidia_agent_skill_mappings_are_scoped(self) -> None:
        esm_unit = next(
            unit
            for unit in self.units
            if any(
                item["slug"] == "facebook-esm-2-650m-protein-embedding"
                for item in unit["forgeModels"]
            )
        )
        mappings = research_catalog.mapped_agent_skills(esm_unit)
        self.assertEqual({item["relation"] for item in mappings}, {"agent-integration"})
        self.assertIn("never as model-quality", mappings[0]["notes"])

        maisi_unit = next(
            unit
            for unit in self.units
            if any(item["slug"] == "nvidia-maisi-nim" for item in unit["forgeModels"])
        )
        mappings = research_catalog.mapped_agent_skills(maisi_unit)
        self.assertEqual(
            {item["relation"] for item in mappings},
            {"related-model-workflow"},
        )

        cosmos_embed_unit = next(
            unit
            for unit in self.units
            if any(item["slug"] == "nvidia-cosmos-embed1" for item in unit["forgeModels"])
        )
        mappings = research_catalog.mapped_agent_skills(cosmos_embed_unit)
        self.assertEqual(
            {item["relation"] for item in mappings},
            {"exact-model"},
        )
        self.assertEqual(
            {skill["name"] for item in mappings for skill in item["skills"]},
            {"tao-finetune-cosmos-embed"},
        )

        nemotron_embed_unit = next(
            unit
            for unit in self.units
            if any(
                item["slug"] == "nvidia-llama-nemotron-embed-1b-v2-nim"
                for item in unit["forgeModels"]
            )
        )
        mappings = research_catalog.mapped_agent_skills(nemotron_embed_unit)
        self.assertEqual(
            {skill["name"] for item in mappings for skill in item["skills"]},
            {"nemotron-retrieval-recipes"},
        )

        mapping_payload = json.loads(
            (ROOT / "research" / "upstream-agent-skills.json").read_text(
                encoding="utf-8"
            )
        )
        catalog_slugs = {item["slug"] for item in self.catalog["models"]}
        mapped_slugs = {
            slug
            for mapping in mapping_payload["modelMappings"]
            for slug in mapping["forgeSlugs"]
        }
        self.assertLessEqual(mapped_slugs, catalog_slugs)
        nvidia_revision = mapping_payload["sources"][0]["revision"]
        bionemo_revision = mapping_payload["sources"][1]["revision"]
        for mapping in mapping_payload["modelMappings"]:
            for skill in mapping["skills"]:
                if "github.com/NVIDIA/skills" in skill["url"]:
                    self.assertIn(nvidia_revision, skill["url"])
                if "github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit" in skill["url"]:
                    self.assertIn(bionemo_revision, skill["url"])

        boltz_unit = next(
            unit
            for unit in self.units
            if any(
                item["slug"] == "boltz2-nim"
                for item in unit["forgeModels"]
            )
        )
        mappings = research_catalog.mapped_agent_skills(boltz_unit)
        skill_names = {
            skill["name"]
            for mapping in mappings
            for skill in mapping["skills"]
        }
        self.assertTrue(
            {"boltz2-nim", "drug-discovery-pipeline"} <= skill_names,
            skill_names,
        )


if __name__ == "__main__":
    unittest.main()
