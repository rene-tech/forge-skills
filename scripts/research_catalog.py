#!/usr/bin/env python3
"""Research and validate every Forge model skill against primary sources.

The script keeps scientific/model-quality evidence separate from Forge runtime
contracts. Multiple Forge serving variants may share one upstream dossier only
when they point to the same exact upstream source. Generic source pages are
split by model family so unrelated models cannot inherit one another's claims.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "models.json"
MODEL_SCHEMA_PATH = ROOT / "research" / "model-research.schema.json"
GROUP_SCHEMA_PATH = ROOT / "research" / "group-research.schema.json"
MODEL_AUDIT_SCHEMA_PATH = ROOT / "research" / "model-audit.schema.json"
GROUP_AUDIT_SCHEMA_PATH = ROOT / "research" / "group-audit.schema.json"
UPSTREAM_SKILLS_PATH = ROOT / "research" / "upstream-agent-skills.json"
MANUAL_REVIEW_HINTS_PATH = ROOT / "research" / "manual-review-hints.json"
STATE_DIR = ROOT / "research" / ".state"
LEGACY_STATE_PATH = STATE_DIR / "jobs.json"
DRAFT_RESULTS = ROOT / "research" / ".state" / "drafts"
AUDIT_RESULTS = ROOT / "research" / ".state" / "audits"
AUDIT_ATTEMPT_RESULTS = ROOT / "research" / ".state" / "audit-attempts"
MODEL_RESULTS = ROOT / "research" / "models"
GROUP_RESULTS = ROOT / "research" / "groups"
TAVILY_BASE_URL = "https://api.tavily.com"

GENERIC_SOURCE_URLS = {
    "https://build.nvidia.com",
    "https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html",
    "https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html",
}

FORBIDDEN_SECONDARY_HOSTS = {
    "benchmarklist.com",
    "www.benchmarklist.com",
    "medium.com",
    "towardsdatascience.com",
    "paperswithcode.com",
    "emergentmind.com",
    "www.emergentmind.com",
    "wikipedia.org",
    "www.wikipedia.org",
    "reddit.com",
    "www.reddit.com",
    "rivaslab.org",
    "www.rivaslab.org",
    "ollama.com",
    "www.ollama.com",
    "ai.azure.com",
    "api-inference.huggingface.co",
    "aws.amazon.com",
    "cgc.chancloud.com",
    "docs.cloud.sdu.dk",
    "docs.datarobot.com",
    "docs.vllm.ai",
    "deeplearning.ai",
    "en.bioerrorlog.work",
    "events.plgrid.pl",
    "forums.developer.nvidia.com",
    "gromacs.bioexcel.eu",
    "hf-mirror.com",
    "hub.docker.com",
    "jetson-ai-lab.com",
    "mcpservers.org",
    "openapi.city",
    "paddlenlp.readthedocs.io",
    "sites.google.com",
    "sourceforge.net",
    "sunagawalab.ethz.ch",
}
FORBIDDEN_SECONDARY_PATH_PATTERNS = (
    re.compile(r"^/[^/]+/[^/]+/discussions(?:/|$)"),
    re.compile(r"^/blog(?:/|$)"),
    re.compile(r"^/models/?$"),
    re.compile(r"^/papers(?:/|$)"),
)
FORBIDDEN_PRIMARY_SOURCE_DESCRIPTOR_PATTERNS = (
    re.compile(r"\bcommunity-posted\b", re.IGNORECASE),
    re.compile(r"\bsupport forum\b", re.IGNORECASE),
    re.compile(r"\bthird-party (?:capture|documentation|mirror)\b", re.IGNORECASE),
    re.compile(r"\bsecondary capture\b", re.IGNORECASE),
    re.compile(r"\bmirror listing\b", re.IGNORECASE),
)
FORBIDDEN_SECONDARY_REPOSITORIES = {
    ("github.com", "becksteinlab"),
    ("github.com", "ana-oprescu"),
    ("github.com", "envy-ai"),
    ("github.com", "ufresearchcomputing"),
    ("huggingface.co", "calcuis"),
    ("huggingface.co", "galeneai"),
    ("huggingface.co", "hunyuanvideo-community"),
    ("huggingface.co", "ig1"),
    ("huggingface.co", "nousresearch"),
}
REPOSITORY_OWNER_ALIASES = (
    ("abhinand", {"abhinand", "abhinand5"}),
    ("black-forest-labs", {"black-forest-labs"}),
    ("bigcode", {"bigcode", "bigcode-project"}),
    ("biohub-esmc", {"biohub", "evolutionaryscale"}),
    ("boltz", {"jwohlwend"}),
    ("cogvideo", {"thudm", "zai-org"}),
    ("colabfold", {"sokrypton"}),
    ("deepmind", {"deepmind", "google-deepmind"}),
    ("dnabert", {"magics-lab", "zhihan1996"}),
    ("diffdock", {"gcorso"}),
    ("facebook", {"facebook", "facebookresearch"}),
    ("genmo", {"genmo", "genmoai"}),
    ("gromacs", {"gromacs"}),
    ("google-hear", {"google", "google-health"}),
    ("hidream", {"hidream-ai"}),
    ("hive", {"hive-ai"}),
    ("hunyuanvideo", {"tencent", "tencent-hunyuan"}),
    ("ipd-rfdiffusion", {"rosettacommons"}),
    ("kandinsky", {"kandinskylab"}),
    ("lightricks", {"lightricks"}),
    ("llama", {"meta-llama"}),
    ("maisi", {"project-monai"}),
    ("meta-llama", {"meta", "meta-llama"}),
    ("mit-ast", {"mit", "yuangongnd"}),
    ("microsoft", {"microsoft"}),
    ("mistral", {"mistralai"}),
    (
        "nvidia",
        {
            "nvidia",
            "nvidia-ai-blueprints",
            "nvidia-bionemo",
            "nvidia-cosmos",
            "nvidia-medtech",
            "nvlabs",
        },
    ),
    ("nvclip", {"openai"}),
    ("octo", {"octo-models", "rail-berkeley"}),
    ("openai", {"openai"}),
    ("openfold", {"aqlaboratory", "jwohlwend"}),
    ("openmoss", {"openmoss", "openmoss-team"}),
    ("pixart", {"pixart-alpha"}),
    ("qwen", {"qwen", "qwenlm"}),
    ("skyreels", {"skywork"}),
    ("stability", {"stabilityai"}),
    ("tongyi-mai", {"tongyi-mai"}),
)
CROSS_PROVIDER_API_PATTERNS = (
    ("alibabacloud.com", re.compile(r"^/help/.*/model-studio/", re.IGNORECASE)),
    ("docs.aws.amazon.com", re.compile(r"/bedrock/", re.IGNORECASE)),
    ("cloud.google.com", re.compile(r"^/vertex-ai/", re.IGNORECASE)),
    (
        "learn.microsoft.com",
        re.compile(r"/azure/(?:ai-services|machine-learning|ai-foundry)/", re.IGNORECASE),
    ),
)
CROSS_PROVIDER_NON_TRANSFER_MARKERS = (
    "does not establish the nvidia nim",
    "does not establish forge",
    "does not apply to the nvidia nim",
    "does not apply to forge",
    "must not be transferred to the nvidia nim",
    "must not be transferred to forge",
    "provider-specific and not the nvidia nim",
    "provider-specific and not forge",
)
SOURCE_LOCATOR_MARKER_RE = re.compile(
    r"\b(tables?|figures?|figs?\.?|sections?|appendix|appendices|pages?|headings?|readme|repository|paths?|lines?)\b",
    re.IGNORECASE,
)
GENERIC_SOURCE_LOCATOR_RE = re.compile(
    r"^(?:the )?(?:evaluation|results?|benchmarks?) "
    r"(?:table|section)(?: \([^)]*\))?$",
    re.IGNORECASE,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"


def source_scope(entry: dict[str, Any]) -> str:
    source = str(entry.get("sourceUrl") or "").rstrip("/")
    if source in GENERIC_SOURCE_URLS:
        return f"{source}#{entry['modelFamily']}"
    return source


def research_key(scope: str) -> str:
    source, _, family = scope.partition("#")
    parsed = urlparse(source)
    readable = "-".join(
        part
        for part in (
            parsed.netloc.removeprefix("www."),
            parsed.path.strip("/"),
            family,
        )
        if part
    )
    base = slugify(readable)
    digest = sha256_text(scope)[:10]
    if len(base) > 92:
        base = base[:92].rstrip("-")
    return f"{base}-{digest}"


def requires_original_creator_source(unit: dict[str, Any]) -> bool:
    """Return whether Forge starts from NVIDIA packaging of a third-party model."""

    build_publishers: set[str] = set()
    has_generic_build_source = False
    for raw_url in unit.get("sourceUrls") or []:
        normalized_url = str(raw_url).rstrip("/")
        if normalized_url == "https://build.nvidia.com":
            has_generic_build_source = True
            continue
        parsed = urlparse(normalized_url)
        if parsed.netloc.lower() != "build.nvidia.com":
            continue
        path_parts = [part.lower() for part in parsed.path.split("/") if part]
        if path_parts:
            build_publishers.add(path_parts[0])
    if any(publisher != "nvidia" for publisher in build_publishers):
        return True
    if not has_generic_build_source:
        return False
    return any(
        not str(family).lower().startswith("nvidia-")
        for family in unit.get("modelFamilies") or []
    )


def has_original_creator_source(sources: list[dict[str, Any]]) -> bool:
    """Require evidence outside NVIDIA-operated documentation and packaging."""

    for source in sources:
        if not isinstance(source, dict):
            continue
        parsed = urlparse(str(source.get("url") or ""))
        host = parsed.netloc.lower()
        if host == "nvidia.com" or host.endswith(".nvidia.com"):
            continue
        if host == "github.com":
            path_parts = [part.lower() for part in parsed.path.split("/") if part]
            if path_parts and path_parts[0] != "nvidia":
                return True
            continue
        if host:
            return True
    return False


def repository_owner(url: str) -> tuple[str, str] | None:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    parts = [part for part in parsed.path.split("/") if part]
    if host in {"github.com", "raw.githubusercontent.com"} and parts:
        return host, parts[0].lower()
    if host == "huggingface.co" and parts:
        if parts[0].lower() in {"docs", "learn", "papers", "tasks"}:
            return None
        index = 1 if parts[0].lower() in {"datasets", "spaces"} else 0
        if len(parts) > index:
            return host, parts[index].lower()
    return None


def self_described_secondary_source(source: dict[str, Any]) -> bool:
    descriptor = " ".join(
        str(source.get(field) or "")
        for field in ("title", "publisher", "primaryReason")
    )
    return any(
        pattern.search(descriptor)
        for pattern in FORBIDDEN_PRIMARY_SOURCE_DESCRIPTOR_PATTERNS
    )


def allowed_repository_owners(unit: dict[str, Any]) -> set[str]:
    owners = {
        "huggingface",
        "nvidia",
        "nvidia-ai-blueprints",
        "nvidia-bionemo",
        "nvidia-cosmos",
        "nvidia-medtech",
        "nvlabs",
    }
    forge_models = [
        item for item in unit.get("forgeModels") or [] if isinstance(item, dict)
    ]
    model_families = list(unit.get("modelFamilies") or []) + [
        str(item.get("modelFamily") or "") for item in forge_models
    ]
    identity_text = " ".join(str(item) for item in model_families).lower()
    for marker, aliases in REPOSITORY_OWNER_ALIASES:
        if marker in identity_text:
            owners.update(alias.lower() for alias in aliases)
    reviewed_urls = (
        list(unit.get("sourceUrls") or [])
        + [str(item.get("sourceUrl") or "") for item in forge_models]
        + [
            str(hint.get("sourceUrl") or "")
            for hint in unit.get("manualReviewHints") or []
            if isinstance(hint, dict)
        ]
    )
    for url in reviewed_urls:
        parsed_owner = repository_owner(str(url))
        if parsed_owner:
            owners.add(parsed_owner[1])
    return owners


def model_units(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    manual_hints = (
        read_json(MANUAL_REVIEW_HINTS_PATH).get("models", {})
        if MANUAL_REVIEW_HINTS_PATH.is_file()
        else {}
    )
    grouped: dict[str, list[dict[str, Any]]] = {}
    for entry in catalog["models"]:
        grouped.setdefault(source_scope(entry), []).append(entry)

    units: list[dict[str, Any]] = []
    for scope, entries in sorted(grouped.items()):
        ordered = sorted(entries, key=lambda item: item["slug"])
        unit = {
                "kind": "model",
                "key": research_key(scope),
                "sourceScope": scope,
                "sourceUrls": sorted(
                    {str(item["sourceUrl"]) for item in ordered if item.get("sourceUrl")}
                ),
                "modelFamilies": sorted({str(item["modelFamily"]) for item in ordered}),
                "categories": sorted({str(item["category"]) for item in ordered}),
                "groups": sorted({str(item["group"]) for item in ordered}),
                "forgeModels": [
                    {
                        "slug": item["slug"],
                        "displayName": item["displayName"],
                        "description": item["description"],
                        "modelFamily": item["modelFamily"],
                        "version": item["version"],
                        "versionKey": item["versionKey"],
                        "category": item["category"],
                        "group": item["group"],
                        "inputModalities": item["inputModalities"],
                        "outputModalities": item["outputModalities"],
                        "license": item["license"],
                        "sourceUrl": item["sourceUrl"],
                    }
                    for item in ordered
                ],
            }
        if unit["key"] in manual_hints:
            unit["manualReviewHints"] = manual_hints[unit["key"]]
        units.append(unit)
    return units


def group_units(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for entry in catalog["models"]:
        grouped.setdefault((entry["category"], entry["group"]), []).append(entry)
    return [
        {
            "kind": "group",
            "key": f"{category}--{group}",
            "category": category,
            "group": group,
            "forgeModels": [
                {
                    "slug": item["slug"],
                    "displayName": item["displayName"],
                    "description": item["description"],
                    "modelFamily": item["modelFamily"],
                    "versionKey": item["versionKey"],
                    "inputModalities": item["inputModalities"],
                    "outputModalities": item["outputModalities"],
                    "license": item["license"],
                    "sourceUrl": item["sourceUrl"],
                }
                for item in sorted(items, key=lambda value: value["slug"])
            ],
        }
        for (category, group), items in sorted(grouped.items())
    ]


def mapped_agent_skills(unit: dict[str, Any]) -> list[dict[str, Any]]:
    payload = read_json(UPSTREAM_SKILLS_PATH)
    slugs = {item["slug"] for item in unit["forgeModels"]}
    return [
        mapping
        for mapping in payload["modelMappings"]
        if slugs.intersection(mapping["forgeSlugs"])
    ]


def peers_for_model(unit: dict[str, Any], catalog: dict[str, Any]) -> list[dict[str, Any]]:
    own = {item["slug"] for item in unit["forgeModels"]}
    groups = {
        (item["category"], item["group"])
        for item in unit["forgeModels"]
    }
    peers = [
        {
            "slug": item["slug"],
            "displayName": item["displayName"],
            "modelFamily": item["modelFamily"],
            "category": item["category"],
            "group": item["group"],
            "sourceUrl": item["sourceUrl"],
        }
        for item in catalog["models"]
        if item["slug"] not in own and (item["category"], item["group"]) in groups
    ]
    return peers


def model_prompt(unit: dict[str, Any], catalog: dict[str, Any]) -> str:
    variants = json.dumps(unit["forgeModels"], indent=2, ensure_ascii=False)
    peers = json.dumps(peers_for_model(unit, catalog), indent=2, ensure_ascii=False)
    upstream_skills = json.dumps(
        mapped_agent_skills(unit), indent=2, ensure_ascii=False
    )
    manual_hints = json.dumps(
        unit.get("manualReviewHints") or [],
        indent=2,
        ensure_ascii=False,
    )
    return f"""
Produce a deep, checkpoint-scoped research dossier for Forge research key
`{unit["key"]}`. Set the output `family` field to exactly `{unit["key"]}`.

Covered Forge serving variants:
{variants}

Candidate alternatives in the same Forge task group:
{peers}

Related upstream agent skills, if any:
{upstream_skills}

Manual primary-source spot-check hints to independently verify:
{manual_hints}

Research the exact upstream checkpoint, model version, or service named by the
covered variants. Establish:

1. what the model is designed for, strong recommended uses, conditional uses,
   and tasks to avoid;
2. semantic inputs, accepted upstream formats, exact preprocessing,
   validation, tokenization/featurization, task prompts, bounds, batching, and
   truncation/cropping behavior;
3. exact output objects, units/shapes/scores, valid interpretation,
   calibration or confidence limits, and downstream validation;
4. public benchmark results with task, dataset, split, metric, numeric value,
   direction, conditions, and exact checkpoint/model scope;
5. evidence-backed task-specific comparisons with relevant listed Forge peers,
   including quality, modality, context/input limits, latency or memory only
   when comparable primary measurements exist, licensing, and deployment
   constraints;
6. scientific, data, architecture, evaluation, license, operational, safety,
   privacy, clinical, and dual-use limitations; and
7. explicit evidence gaps wherever exact evidence is absent.

Evidence rules:

- Use only primary sources: official model cards, creator/vendor
  documentation, official repositories, original papers, or original technical
  reports. Do not use blogs, press summaries, Reddit, Wikipedia,
  Papers-with-Code, leaderboard mirrors, or secondary benchmark summaries.
- Support forums, API aggregators, marketplace listings, third-party runtime
  guides, and package/container/checkpoint mirrors are not primary sources,
  even when they reproduce official text or artifacts.
- Explicitly exclude Emergent Mind and other model explainers, even if they
  quote a primary paper or repository.
- Use the creator/publisher's canonical paper URL, not a university mirror;
  Hugging Face community discussions and issue threads are not primary
  evidence. Third-party Hugging Face mirrors or reuploads are secondary even
  when they copy an official checkpoint.
- Start from every supplied source URL and follow its official paper,
  repository, documentation, and license links.
- Treat each covered variant's `modelFamily`, `displayName`, version, and task
  suffix (`Instruct`, embedding, reranker, classifier, adapter, quantization,
  task head, and so on) as identity constraints. A base checkpoint is not a
  substitute for its Instruct/task-tuned sibling. When NVIDIA packages a
  third-party model, locate the original creator's exact checkpoint card,
  repository, and paper instead of stopping at NVIDIA, another cloud host, or
  a similarly named base model.
- Every URL placed in any `evidenceUrls` or `sourceUrl` field must also appear
  exactly once in the top-level `sources` list. Do not cite a URL that is
  absent from `sources`.
- Do not transfer a result across parameter scales, checkpoints, adapters,
  task heads, quantizations, wrappers, NIM versions, or serving runtimes.
- A different cloud provider's hosted-API documentation does not establish
  the NVIDIA NIM or Forge input/output contract. Prefer the exact creator and
  serving-runtime documentation. If a provider-specific source is retained
  for explicitly scoped context, every claim citing it must say in that same
  claim that the contract does not establish the NVIDIA NIM or Forge contract.
- A NIM, inference server, or Forge wrapper may serve an unchanged named
  upstream checkpoint. When primary identity evidence proves that relationship,
  research the underlying checkpoint's original model card, repository, and
  paper. Its checkpoint-scoped quality results remain relevant when labeled
  with that upstream checkpoint and evaluation protocol; do not present them
  as a benchmark of the serving container, wrapper, quantization, or Forge
  runtime.
- Do not call a model globally better. Comparisons must name the task,
  criterion, and protocol. Use `insufficient-evidence` when protocols differ.
- Record exact numeric benchmark values only when the primary source exposes
  the dataset/split, metric, model scope, and conditions. Otherwise put the
  missing fact in `evidenceGaps`.
- Keep upstream model behavior separate from the Forge HTTP/request contract
  and from Forge GPU latency/readiness probes. Forge operational probes are not
  model-quality evidence.
- Related agent skills may inform tool routing, payload checks, fixtures,
  validation, and deployment workflow only when their exact model scope
  matches. A deterministic BioNeMo integration harness is not scientific
  evidence. Preserve any upstream revision and relation.
- For healthcare/life-science models, be explicit about research-only versus
  clinical use, PHI/proprietary-data handling, and necessary expert review.

Return only data conforming to the supplied schema. A benchmark list may be
empty only when `evidenceGaps` explicitly records that exact-checkpoint
benchmark evidence could not be found after checking the starting source,
canonical model card/repository, and original paper. That benchmark gap must
name the exact primary-source URL and the table, figure, section, appendix,
page, heading, or repository path checked. A comparison list may be empty only
when `evidenceGaps` explicitly records the missing comparison evidence. Never
use a serving-package distinction as a reason to omit checkpoint-scoped
upstream evidence when the package-to-checkpoint identity is proven.
""".strip()


def group_prompt(unit: dict[str, Any]) -> str:
    models = json.dumps(unit["forgeModels"], indent=2, ensure_ascii=False)
    return f"""
Produce a deep model-selection dossier for Forge category `{unit["category"]}`
and group `{unit["group"]}`. Set output `category` and `group` to those exact
values.

Exact Forge candidates:
{models}

Define the task precisely and give an agent the questions and conditional
decision rules needed to choose among these exact candidates. Research the
official source of every candidate. Build a benchmark taxonomy that identifies
which datasets, splits, metrics, prompts, fine-tuning regimes, input shapes,
and evaluation conditions must match before results can be compared.

Use only primary sources: official model cards/documentation/repositories and
original papers or technical reports. Do not use blogs, Wikipedia,
Papers-with-Code, leaderboard mirrors, vendor press summaries, or other
secondary aggregations. Third-party Hugging Face mirrors or reuploads are
secondary even when they copy an official checkpoint. Never transfer a claim
across checkpoints, parameter scales, adapters, quantizations, wrappers, NIM
versions, or task heads.

Every decision rule must be use-case- and criterion-specific. `prefer` must be
one exact `slug` from the candidate list or the literal
`insufficient-evidence`; never return an upstream repository ID, display name,
family, or a model that is absent from Forge. Every `alternatives` item must be
one distinct exact candidate `slug`, never the preferred slug, with any
conditional explanation expressed as a separate decision rule. Do not
duplicate alternatives. Collectively, the decision rules must mention every
exact Forge candidate at least once in `prefer` or `alternatives`. Cite primary
evidence for all sides, and include every non-generic candidate `sourceUrl` in
the top-level `sources` list. Every decision-rule `evidenceUrls` value must
appear exactly in that list. Include quality, modality, input/context limits,
output semantics, license, safety, and operational fit where supported. Use
`insufficient-evidence` instead of declaring a winner when evaluations are not
comparable. Forge latency and GPU support may later be layered onto this
dossier, but they are not public model-quality evidence.

Return only data conforming to the supplied schema.
""".strip()


def audit_prompt(
    unit: dict[str, Any],
    draft: dict[str, Any],
    *,
    retry_feedback: list[str] | None = None,
) -> str:
    expected_schema = (
        "model-research.schema.json"
        if unit["kind"] == "model"
        else "group-research.schema.json"
    )
    scope = json.dumps(unit, indent=2, ensure_ascii=False)
    draft_text = json.dumps(draft, indent=2, ensure_ascii=False)
    mandatory_manual_hints = json.dumps(
        unit.get("manualReviewHints") or [],
        indent=2,
        ensure_ascii=False,
    )
    exact_candidate_checklist = (
        json.dumps(
            [model["slug"] for model in unit.get("forgeModels") or []],
            indent=2,
            ensure_ascii=False,
        )
        if unit["kind"] == "group"
        else "Not applicable to a model dossier."
    )
    feedback = (
        "\n\nA previous audit attempt failed these deterministic local gates. "
        "Correct every item in the new complete dossier:\n- "
        + "\n- ".join(retry_feedback)
        if retry_feedback
        else ""
    )
    return f"""
Independently audit and correct a draft Forge research dossier. This is a
source-verification task, not a rewrite for style.

Expected scope:
{scope}

Draft dossier:
{draft_text}

Open and verify every cited source. Search for the authoritative primary source
when the draft cites a secondary source. Apply all of these gates:

1. Remove every blog, explainer, Wikipedia page, Reddit thread,
   Papers-with-Code page, leaderboard mirror, press summary, or other secondary
   source. Emergent Mind is explicitly forbidden. A source cannot become
   primary merely because the draft labels it primary.
   Also replace university paper mirrors with the canonical publisher/preprint
   URL and remove Hugging Face community discussions, issue threads, and
   third-party mirrors or reuploads of an official checkpoint.
   Support forums, API aggregators, marketplace listings, third-party runtime
   guides, and package/container/checkpoint mirrors are also secondary.
   When removing a secondary or unapproved URL, remove or replace it everywhere:
   the top-level source index and every benchmark, comparison, decision rule,
   input/output, limitation, and safety `evidenceUrls` field. Never leave a
   claim pointing to a URL omitted from the corrected source index.
2. Verify that every claim applies to the exact checkpoint, parameter scale,
   task head, adapter, precision, NIM/service version, and runtime named in the
   expected scope. Remove or narrow transferred family-level claims. When a
   NIM, server, or wrapper is proven by primary identity evidence to serve an
   unchanged named upstream checkpoint, retain verified checkpoint-scoped
   evidence from that checkpoint's original model card, repository, and paper;
   label it as upstream-checkpoint evidence rather than a serving-runtime
   benchmark.
   Reject a base-model source substituted for an Instruct, task-tuned,
   adapter, embedding, reranking, classifier, or quantized checkpoint. For a
   third-party checkpoint packaged by NVIDIA, verify the creator's exact
   checkpoint source as well as the NVIDIA serving source.
   A different cloud provider's hosted-API limits or request shape do not
   establish the NVIDIA NIM or Forge contract. Remove them, or state directly
   in every claim citing them that they do not establish the NVIDIA NIM or
   Forge contract.
3. Verify every numeric benchmark directly at the cited table, figure,
   section, appendix, model-card heading, or repository path. Remove any row
   whose exact checkpoint, dataset/split, metric, value, or conditions cannot
   be verified. A paper's result for an attached structure head is not
   automatically a benchmark of a base embedding checkpoint. When a benchmark
   requires a downstream head or service not exposed by the listed Forge
   variants, either remove it or state that dependency explicitly in
   `modelScope`, `conditions`, and `caveats`; never imply the callable Forge
   output produced that result.
4. Verify input preprocessing, bounds, prompt templates, output shapes/units,
   score interpretation, pooling, normalization, and validation from official
   code or documentation. Convert ambiguity into an evidence gap.
5. Ensure comparisons are task- and protocol-specific and cite primary
   evidence for both sides. Use insufficient-evidence when protocols differ.
6. Preserve model-weight versus code-license distinctions and all
   healthcare/life-science safety, privacy, clinical, proprietary-data, and
   expert-review boundaries.
7. Keep upstream model evidence separate from Forge request/runtime metadata.
   Forge latency and GPU probes are operational evidence, not model quality.
8. Set the corrected dossier identity fields exactly as required by
   `{expected_schema}`. For a model dossier, `family` must be exactly
   `{unit["key"]}`. For a group dossier, category/group must exactly match the
   expected scope.
9. Before returning, construct the top-level `sources` list first and ensure
   every URL in every `evidenceUrls` or `sourceUrl` field is an exact member of
   that list. Remove unsupported citations rather than adding a secondary
   source. Every source entry must be genuinely primary and have
   `primary: true`.
10. For every limitation or safety item with an empty `evidenceUrls` array,
    begin the statement with the literal prefix `Evidence gap:` or
    `Forge policy:`. Do not present an uncited claim as established fact.
11. In a group dossier, every `benchmarkTaxonomy[].datasets[]` entry must be a
    plain string containing the dataset name, optional version, and optional
    split. Never return a nested dataset object; keep URLs in `sources`.
12. A model dossier must give at least one recommended use, one avoid-use
    boundary, one limitation, and one safety/data-handling rule. Its semantic
    input, accepted format, preprocessing, input validation, output,
    interpretation, and post-output validation sections must each contain a
    sourced statement or have a section-specific entry in `evidenceGaps`.
    Recommended uses must always cite primary evidence. Any uncited atomic
    input/output statement must begin `Evidence gap:` or `Forge policy:`.
13. In a group dossier, every decision-rule `prefer` must be one exact Forge
    candidate `slug` from the expected scope or the literal
    `insufficient-evidence`. Every `alternatives` item must be one exact
    candidate slug distinct from `prefer`, never an upstream repository ID,
    display name, family, or prose. Do not repeat alternatives. Collectively
    mention every exact Forge candidate at least once.
    Include each candidate's non-generic official `sourceUrl` in `sources`.

Return only the complete corrected dossier conforming exactly to
`{expected_schema}`. Do not wrap it in `correctedDossier`, `audit`, `verdict`,
`summary`, or `issues`; the runner derives audit provenance and verdict after
the corrected dossier passes every local gate. Every required dossier field
must be present even when evidence is weak. Before leaving `benchmarks` empty,
check the official starting source, canonical model card/repository, and
original paper and add a benchmark-specific `evidenceGaps` entry. Before
leaving `comparisons` empty, add a comparison-specific `evidenceGaps` entry.
Prefer explicit gaps over unsupported claims, but do not discard verified
upstream-checkpoint evidence merely because Forge serves it through a NIM,
server, or wrapper.
{feedback}

Non-negotiable manual-review hints for this exact scope are repeated here
because they must survive correction of a long draft. Open the named primary
source, independently verify the exact locator and scoped values, and satisfy
every required source/benchmark instruction before returning:
{mandatory_manual_hints}

For a group dossier, this is the final exact Forge candidate checklist.
Every string must appear verbatim in `prefer` or `alternatives`; do not replace
it with a display name, upstream ID, family, or prose:
{exact_candidate_checklist}
""".strip()


def provider_schema(schema: dict[str, Any]) -> dict[str, Any]:
    """Convert full JSON Schema to Tavily Research's accepted subset."""

    def clean(value: Any) -> Any:
        if isinstance(value, list):
            return [clean(item) for item in value]
        if not isinstance(value, dict):
            return value
        cleaned: dict[str, Any] = {}
        for key, child in value.items():
            if key in {"$schema", "additionalProperties"}:
                continue
            if key == "title" and "properties" in value:
                continue
            cleaned[key] = clean(child)
        return cleaned

    cleaned = clean(schema)
    return {
        "properties": cleaned["properties"],
        "required": cleaned["required"],
    }


def audit_schema(unit: dict[str, Any]) -> dict[str, Any]:
    if unit["kind"] == "model":
        audit = read_json(MODEL_AUDIT_SCHEMA_PATH)
        dossier = read_json(MODEL_SCHEMA_PATH)
    else:
        audit = read_json(GROUP_AUDIT_SCHEMA_PATH)
        dossier = read_json(GROUP_SCHEMA_PATH)
    dossier["description"] = (
        "The complete independently verified and corrected research dossier."
    )
    properties = audit["properties"]
    audit["properties"] = {
        "correctedDossier": dossier,
        **{
            key: value
            for key, value in properties.items()
            if key != "correctedDossier"
        },
    }
    audit["required"] = [
        "correctedDossier",
        *[key for key in audit["required"] if key != "correctedDossier"],
    ]
    return audit


def prune_to_schema(
    value: Any,
    schema: dict[str, Any],
    path: str = "$",
) -> tuple[Any, list[str]]:
    dropped: list[str] = []
    if isinstance(value, dict) and isinstance(schema.get("properties"), dict):
        normalized: dict[str, Any] = {}
        properties = schema["properties"]
        for key, child in value.items():
            if key not in properties:
                if schema.get("additionalProperties") is False:
                    dropped.append(f"{path}.{key}")
                    continue
                normalized[key] = child
                continue
            normalized_child, child_drops = prune_to_schema(
                child,
                properties[key],
                f"{path}.{key}",
            )
            normalized[key] = normalized_child
            dropped.extend(child_drops)
        return normalized, dropped
    if isinstance(value, list) and isinstance(schema.get("items"), dict):
        normalized_items: list[Any] = []
        for index, child in enumerate(value):
            normalized_child, child_drops = prune_to_schema(
                child,
                schema["items"],
                f"{path}[{index}]",
            )
            normalized_items.append(normalized_child)
            dropped.extend(child_drops)
        return normalized_items, dropped
    return value, dropped


def normalize_provider_shapes(
    value: Any,
    path: str = "$",
) -> tuple[Any, list[str]]:
    """Apply only lossless normalizations for recurring provider wrappers."""

    normalized_paths: list[str] = []
    if isinstance(value, list):
        normalized_items = []
        for index, child in enumerate(value):
            if (
                path.endswith(".evidenceGaps")
                and isinstance(child, dict)
                and set(child) == {"statement"}
                and isinstance(child["statement"], str)
            ):
                normalized_items.append(child["statement"])
                normalized_paths.append(f"{path}[{index}]")
                continue
            normalized_child, child_paths = normalize_provider_shapes(
                child,
                f"{path}[{index}]",
            )
            normalized_items.append(normalized_child)
            normalized_paths.extend(child_paths)
        return normalized_items, normalized_paths
    if not isinstance(value, dict):
        return value, normalized_paths
    normalized: dict[str, Any] = {}
    for key, child in value.items():
        child_path = f"{path}.{key}"
        if key == "evidenceUrls" and isinstance(child, list):
            urls = []
            for index, item in enumerate(child):
                if isinstance(item, dict) and set(item) == {"url"} and isinstance(
                    item["url"], str
                ):
                    urls.append(item["url"])
                    normalized_paths.append(f"{child_path}[{index}]")
                else:
                    urls.append(item)
            normalized[key] = urls
            continue
        normalized_child, child_paths = normalize_provider_shapes(child, child_path)
        normalized[key] = normalized_child
        normalized_paths.extend(child_paths)
    return normalized, normalized_paths


def extract_audited_dossier(
    unit: dict[str, Any],
    structured: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    """Accept legacy audit envelopes and the flat dossier-only audit contract."""

    schema_path = MODEL_SCHEMA_PATH if unit["kind"] == "model" else GROUP_SCHEMA_PATH
    schema = read_json(schema_path)
    allowed = set(schema["properties"])
    provider_audit = (
        structured
        if isinstance(structured.get("correctedDossier"), dict)
        else {}
    )
    nested = provider_audit.get("correctedDossier") or {}
    dossier = (
        dict(nested)
        if provider_audit and isinstance(nested, dict)
        else dict(structured)
    )
    if provider_audit:
        for key in allowed:
            if key not in dossier and key in structured:
                dossier[key] = structured[key]
    normalized_shapes, normalized_paths = normalize_provider_shapes(dossier)
    normalized, dropped = prune_to_schema(normalized_shapes, schema)
    return (
        normalized,
        provider_audit,
        [*[f"normalized:{path}" for path in normalized_paths], *dropped],
    )


def reconcile_cited_child_sources(
    unit: dict[str, Any],
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    """Index cited first-party child URLs without changing dossier claims."""

    reconciled = json.loads(json.dumps(dossier))
    sources = reconciled.get("sources") or []
    source_urls = {str(item.get("url") or "") for item in sources}
    missing_urls = sorted(
        {
            url
            for url in _all_evidence_urls(reconciled)
            if url and url not in source_urls
        }
    )
    repaired_urls: list[str] = []
    allowed_hosts = {
        "huggingface.co",
        "github.com",
        "build.nvidia.com",
        "catalog.ngc.nvidia.com",
        "docs.nvidia.com",
    }
    required_parent_fields = ["title", "publisher"]
    if unit["kind"] == "model":
        required_parent_fields.extend(["sourceType", "modelScope"])
    for url in missing_urls:
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc.lower() not in allowed_hosts:
            continue
        parent = next(
            (
                item
                for item in sources
                if item.get("primary") is True
                and all(
                    isinstance(item.get(field), str)
                    and str(item.get(field)).strip()
                    for field in required_parent_fields
                )
                and url.startswith(str(item.get("url") or "").rstrip("/") + "/")
                and urlparse(str(item.get("url") or "")).netloc.lower()
                == parsed.netloc.lower()
            ),
            None,
        )
        if parent is None:
            continue
        indexed_source = {
            "title": f"{parent['title']} — cited revision/file",
            "url": url,
            "publisher": parent["publisher"],
            "primary": True,
            "supports": ["Exact audited claim citation"],
        }
        if unit["kind"] == "model":
            indexed_source.update(
                {
                    "sourceType": parent["sourceType"],
                    "primaryReason": (
                        "Exact revision/file URL beneath the independently verified "
                        "first-party source indexed by this dossier."
                    ),
                    "modelScope": parent["modelScope"],
                }
            )
        sources.append(indexed_source)
        source_urls.add(url)
        repaired_urls.append(url)
    reconciled["sources"] = sources
    return reconciled, repaired_urls


def reconcile_cited_official_sources(
    unit: dict[str, Any],
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    """Index cited allowlisted first-party URLs without changing any claim."""

    reconciled = json.loads(json.dumps(dossier))
    sources = reconciled.get("sources") or []
    source_urls = {
        str(item.get("url") or "") for item in sources if isinstance(item, dict)
    }
    repaired_urls: list[str] = []
    nvidia_first_party_hosts = {
        "build.nvidia.com",
        "catalog.ngc.nvidia.com",
        "docs.api.nvidia.com",
        "docs.nvidia.com",
        "nvidia-cosmos.github.io",
        "research.nvidia.com",
    }
    declared_urls = [
        *[str(url) for url in unit.get("sourceUrls") or []],
        *[
            str(model.get("sourceUrl") or "")
            for model in unit.get("forgeModels") or []
            if isinstance(model, dict)
        ],
        *[
            str(hint.get("sourceUrl") or "")
            for hint in unit.get("manualReviewHints") or []
            if isinstance(hint, dict)
        ],
    ]
    declared_hf_publishers = {
        path_parts[0].lower()
        for url in declared_urls
        if (parsed := urlparse(url)).netloc.lower() == "huggingface.co"
        and (path_parts := [part for part in parsed.path.split("/") if part])
    }
    for url in sorted(set(_all_evidence_urls(reconciled)) - source_urls):
        parsed = urlparse(url)
        path_parts = [part for part in parsed.path.split("/") if part]
        host = parsed.netloc.lower()
        allowlisted = host in nvidia_first_party_hosts or (
            host == "huggingface.co"
            and path_parts
            and path_parts[0].lower() in declared_hf_publishers | {"nvidia"}
        )
        forbidden = host in FORBIDDEN_SECONDARY_HOSTS or any(
            pattern.search(parsed.path)
            for pattern in FORBIDDEN_SECONDARY_PATH_PATTERNS
        )
        if parsed.scheme != "https" or not allowlisted or forbidden:
            continue
        indexed_source = {
            "title": "Cited official first-party source",
            "url": url,
            "publisher": host,
            "primary": True,
            "supports": ["Exact independently audited claim citation"],
        }
        if unit.get("kind") == "model":
            indexed_source.update(
                {
                    "sourceType": (
                        "model-card"
                        if host == "huggingface.co"
                        else "official-documentation"
                    ),
                    "primaryReason": (
                        "The independent audit cited this exact URL and its host "
                        "is narrowly allowlisted as a first-party model or vendor "
                        "documentation source."
                    ),
                    "modelScope": ", ".join(
                        unit.get("modelFamilies") or [unit["key"]]
                    ),
                }
            )
        sources.append(indexed_source)
        source_urls.add(url)
        repaired_urls.append(url)
    reconciled["sources"] = sources
    return reconciled, repaired_urls


def reconcile_required_starting_sources(
    unit: dict[str, Any],
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    """Index exact non-generic official sources already declared by Forge."""

    reconciled = json.loads(json.dumps(dossier))
    sources = reconciled.get("sources") or []
    source_urls = {str(item.get("url") or "") for item in sources}
    repaired_urls: list[str] = []
    allowed_hosts = {
        "build.nvidia.com",
        "huggingface.co",
        "github.com",
        "catalog.ngc.nvidia.com",
        "docs.nvidia.com",
    }
    required_urls = list(unit.get("sourceUrls") or [])
    if unit.get("kind") == "group":
        required_urls.extend(
            str(model.get("sourceUrl") or "")
            for model in unit.get("forgeModels") or []
        )
    for url in dict.fromkeys(required_urls):
        official_url = str(url)
        parsed = urlparse(official_url)
        if (
            not official_url
            or official_url.rstrip("/") in GENERIC_SOURCE_URLS
            or official_url in source_urls
            or parsed.scheme != "https"
            or parsed.netloc.lower() not in allowed_hosts
        ):
            continue
        indexed_source = {
            "title": "Exact official starting source declared by Forge",
            "url": official_url,
            "publisher": parsed.netloc,
            "primary": True,
            "supports": ["Forge-to-upstream exact-version identity"],
        }
        if unit.get("kind") == "model":
            indexed_source.update(
                {
                    "sourceType": "official-documentation",
                    "primaryReason": (
                        "The Forge exact-version catalog declares this first-party "
                        "URL as the official source for the covered serving variant."
                    ),
                    "modelScope": ", ".join(
                        unit.get("modelFamilies") or [unit["key"]]
                    ),
                }
            )
        sources.append(indexed_source)
        source_urls.add(official_url)
        repaired_urls.append(official_url)
    reconciled["sources"] = sources
    return reconciled, repaired_urls


def reconcile_manual_review_evidence(
    unit: dict[str, Any],
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    """Apply primary evidence rows that were independently reviewed by a human."""

    reconciled = json.loads(json.dumps(dossier))
    if unit.get("kind") != "model":
        return reconciled, []
    sources = reconciled.get("sources") or []
    source_urls = {
        str(item.get("url") or "") for item in sources if isinstance(item, dict)
    }
    benchmarks = reconciled.get("benchmarks") or []
    benchmark_keys = {
        (
            str(item.get("sourceUrl") or ""),
            str(item.get("sourceLocator") or ""),
            str(item.get("task") or ""),
            str(item.get("metric") or ""),
        )
        for item in benchmarks
        if isinstance(item, dict)
    }
    repaired: list[str] = []
    for hint in unit.get("manualReviewHints") or []:
        if not isinstance(hint, dict):
            continue
        source_url = str(hint.get("sourceUrl") or "")
        rows = hint.get("benchmarkRows") or []
        if (
            (rows or hint.get("requireSource"))
            and source_url
            and source_url not in source_urls
        ):
            sources.append(
                {
                    "title": str(hint.get("sourceTitle") or "Manually reviewed primary source"),
                    "url": source_url,
                    "publisher": str(hint.get("publisher") or urlparse(source_url).netloc),
                    "sourceType": str(hint.get("sourceType") or "paper"),
                    "primary": True,
                    "primaryReason": (
                        "A human reviewer opened this primary source and verified "
                        "the structured benchmark rows and exact locator recorded "
                        "in research/manual-review-hints.json."
                    ),
                    "modelScope": ", ".join(
                        unit.get("modelFamilies") or [unit["key"]]
                    ),
                    "supports": (
                        ["Manually verified exact-checkpoint benchmark evidence"]
                        if rows
                        else [
                            "Manually verified primary-source provenance and "
                            "scope guidance"
                        ]
                    ),
                }
            )
            source_urls.add(source_url)
            repaired.append(source_url)
        for row in rows:
            if not isinstance(row, dict):
                continue
            key = (
                str(row.get("sourceUrl") or ""),
                str(row.get("sourceLocator") or ""),
                str(row.get("task") or ""),
                str(row.get("metric") or ""),
            )
            if key in benchmark_keys:
                continue
            benchmarks.append(row)
            benchmark_keys.add(key)
            repaired.append(
                f"{row.get('sourceUrl')}#{row.get('sourceLocator')}:{row.get('metric')}"
            )
    reconciled["sources"] = sources
    reconciled["benchmarks"] = benchmarks
    return reconciled, repaired


def discard_invalid_benchmark_placeholders(
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    """Discard rows that cannot represent a numeric benchmark result."""

    normalized = json.loads(json.dumps(dossier))
    if "benchmarks" not in normalized:
        return normalized, []
    kept: list[Any] = []
    discarded: list[str] = []
    for index, benchmark in enumerate(normalized.get("benchmarks") or []):
        if not isinstance(benchmark, dict):
            kept.append(benchmark)
            continue
        value = str(benchmark.get("value") or "").strip()
        if value and re.search(r"\d", value) and not value.lower().startswith(
            ("evidence gap:", "not reported", "unknown")
        ):
            kept.append(benchmark)
            continue
        discarded.append(f"discarded:$.benchmarks[{index}]")
    normalized["benchmarks"] = kept
    return normalized, discarded


def discard_unreferenced_forbidden_sources(
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    """Remove forbidden secondary sources only when no dossier claim cites them."""

    normalized = json.loads(json.dumps(dossier))
    cited_urls = set(_all_evidence_urls(normalized))
    kept: list[Any] = []
    discarded: list[str] = []
    for index, source in enumerate(normalized.get("sources") or []):
        if not isinstance(source, dict):
            kept.append(source)
            continue
        url = str(source.get("url") or "")
        parsed = urlparse(url)
        forbidden = (
            parsed.netloc.lower() in FORBIDDEN_SECONDARY_HOSTS
            or any(
                pattern.search(parsed.path)
                for pattern in FORBIDDEN_SECONDARY_PATH_PATTERNS
            )
        )
        if forbidden and url not in cited_urls:
            discarded.append(f"discarded:$.sources[{index}]")
            continue
        kept.append(source)
    normalized["sources"] = kept
    return normalized, discarded


def reconcile_dossier_sources(
    unit: dict[str, Any],
    dossier: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    reconciled, discarded_sources = discard_unreferenced_forbidden_sources(dossier)
    reconciled, child_urls = reconcile_cited_child_sources(unit, reconciled)
    reconciled, official_urls = reconcile_cited_official_sources(unit, reconciled)
    reconciled, starting_urls = reconcile_required_starting_sources(
        unit,
        reconciled,
    )
    reconciled, manual_evidence = reconcile_manual_review_evidence(unit, reconciled)
    reconciled, discarded_benchmarks = discard_invalid_benchmark_placeholders(
        reconciled
    )
    return reconciled, [
        *discarded_sources,
        *child_urls,
        *official_urls,
        *starting_urls,
        *manual_evidence,
        *discarded_benchmarks,
    ]


def derived_audit_metadata(
    draft_result: dict[str, Any],
    dossier: dict[str, Any],
    provider_audit: dict[str, Any],
    dropped_paths: list[str] | None = None,
) -> tuple[str, str, list[dict[str, Any]]]:
    draft = draft_result["dossier"]
    changed = json.dumps(draft, sort_keys=True, ensure_ascii=False) != json.dumps(
        dossier,
        sort_keys=True,
        ensure_ascii=False,
    )
    provider_verdict = provider_audit.get("verdict")
    verdict = (
        str(provider_verdict)
        if provider_verdict in {"accepted", "revised"}
        else ("revised" if changed else "accepted")
    )
    draft_errors = [
        str(item)
        for item in draft_result.get("validation", {}).get("errors", [])
    ]
    provider_summary = str(provider_audit.get("auditSummary") or "").strip()
    summary = provider_summary or (
        "Independent primary-source verification returned a complete "
        f"{'corrected' if changed else 'confirmed'} dossier that passed all "
        f"local schema, source, and checkpoint-scope gates; {len(draft_errors)} "
        "deterministic draft defect(s) were supplied to the audit."
    )
    provider_issues = provider_audit.get("issues")
    issues = (
        list(provider_issues)
        if isinstance(provider_issues, list) and provider_issues
        else [
            {
                "severity": "medium",
                "path": error.split(":", 1)[0],
                "issue": error,
                "resolution": (
                    "The independently audited dossier corrected or removed "
                    "the failing draft field and passed the same gate."
                ),
                "evidenceUrls": [],
            }
            for error in draft_errors
        ]
    )
    for path in dropped_paths or []:
        normalized = path.startswith("normalized:")
        reconciled = path.startswith("reconciled:")
        issues.append(
            {
                "severity": "low",
                "path": path.removeprefix("normalized:").removeprefix("reconciled:"),
                "issue": (
                    "Audited claim cited a first-party child URL omitted from the source index."
                    if reconciled
                    else (
                        "Provider wrapped an evidence URL in a single-key object."
                        if normalized
                        else "Provider returned a field outside the published dossier schema."
                    )
                ),
                "resolution": (
                    "The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed."
                    if reconciled
                    else (
                        "The runner losslessly flattened the URL wrapper before validation."
                        if normalized
                        else (
                            "The runner removed the unsupported field before validation; "
                            "no accepted dossier field was replaced."
                        )
                    )
                ),
                "evidenceUrls": (
                    [path.removeprefix("reconciled:")]
                    if reconciled
                    else []
                ),
            }
        )
    return verdict, summary, issues


def _find_tavily_key(value: Any) -> str | None:
    if isinstance(value, dict):
        for key in ("api_key", "apiKey", "tavily_api_key", "TAVILY_API_KEY"):
            candidate = value.get(key)
            if isinstance(candidate, str) and candidate.startswith("tvly-"):
                return candidate
        for child in value.values():
            found = _find_tavily_key(child)
            if found:
                return found
    if isinstance(value, list):
        for child in value:
            found = _find_tavily_key(child)
            if found:
                return found
    return None


def resolve_tavily_key() -> str:
    if os.getenv("TAVILY_API_KEY"):
        return str(os.environ["TAVILY_API_KEY"])
    for path in (
        Path.home() / ".tavily" / "config.json",
        Path.home() / ".config" / "tavily" / "config.json",
        Path.home() / ".config" / "tvly" / "config.json",
        Path.home() / ".openclaw" / "openclaw.json",
    ):
        if path.is_file():
            found = _find_tavily_key(read_json(path))
            if found:
                return found
    raise RuntimeError(
        "Tavily API key not found; set TAVILY_API_KEY or configure an approved "
        "Tavily/OpenClaw credential source"
    )


def tavily_request(
    method: str,
    endpoint: str,
    *,
    api_key: str,
    payload: dict[str, Any] | None = None,
    timeout: float = 300,
    max_transient_attempts: int = 6,
) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        f"{TAVILY_BASE_URL}/{endpoint.lstrip('/')}",
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    for attempt in range(1, max_transient_attempts + 1):
        try:
            with urlopen(request, timeout=timeout) as response:
                return json.load(response)
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            transient = exc.code in {429, 500, 502, 503, 504}
            if not transient or attempt >= max_transient_attempts:
                raise RuntimeError(f"Tavily HTTP {exc.code}: {detail}") from exc
            try:
                retry_after = float((exc.headers or {}).get("Retry-After") or 0)
            except (TypeError, ValueError):
                retry_after = 0
            delay = min(30.0, max(retry_after, float(2 ** (attempt - 1))))
            print(
                json.dumps(
                    {
                        "tavilyTransientStatus": exc.code,
                        "retryAttempt": attempt,
                        "retryInSeconds": delay,
                    }
                ),
                flush=True,
            )
            time.sleep(delay)
        except URLError as exc:
            if attempt >= max_transient_attempts:
                raise RuntimeError(f"Tavily request failed: {exc}") from exc
            delay = min(30.0, float(2 ** (attempt - 1)))
            print(
                json.dumps(
                    {
                        "tavilyTransientNetworkError": True,
                        "retryAttempt": attempt,
                        "retryInSeconds": delay,
                    }
                ),
                flush=True,
            )
            time.sleep(delay)
    raise AssertionError("unreachable Tavily retry loop")


def state_path(kind: str) -> Path:
    if kind not in {"models", "groups", "all"}:
        raise ValueError(f"unsupported state kind: {kind}")
    return STATE_DIR / f"jobs-{kind}.json"


def load_state(kind: str) -> dict[str, Any]:
    path = state_path(kind)
    if path.is_file():
        return read_json(path)
    if LEGACY_STATE_PATH.is_file():
        legacy = read_json(LEGACY_STATE_PATH)
        marker = {"models": ":model:", "groups": ":group:"}.get(kind)
        jobs = {
            key: value
            for key, value in (legacy.get("jobs") or {}).items()
            if marker is None or marker in key
        }
        return {"schemaVersion": "1.1.0", "jobs": jobs}
    return {"schemaVersion": "1.1.0", "jobs": {}}


def available_submission_slots(
    state: dict[str, Any],
    selected_job_keys: set[str],
    max_active: int,
) -> tuple[int, int]:
    active_count = sum(
        1
        for job_key, job in state["jobs"].items()
        if job_key in selected_job_keys
        and job.get("status") not in {"completed", "failed", "rejected"}
    )
    return active_count, max(0, max_active - active_count)


def state_job_key(unit: dict[str, Any]) -> str:
    return f"{unit['kind']}:{unit['key']}"


def phase_job_key(unit: dict[str, Any], phase: str) -> str:
    return f"{phase}:{state_job_key(unit)}"


def output_path(unit: dict[str, Any]) -> Path:
    if unit["kind"] == "model":
        return MODEL_RESULTS / f"{unit['key']}.json"
    return GROUP_RESULTS / unit["category"] / f"{unit['group']}.json"


def has_accepted_output(unit: dict[str, Any]) -> bool:
    path = output_path(unit)
    if not path.is_file():
        return False
    payload = read_json(path)
    return (
        payload.get("validation", {}).get("status") == "accepted"
        and payload.get("audit", {}).get("verdict") in {"accepted", "revised"}
        and not validate_dossier(unit, payload.get("dossier") or {})
    )


def draft_path(unit: dict[str, Any]) -> Path:
    return DRAFT_RESULTS / unit["kind"] / f"{unit['key']}.json"


def audit_path(unit: dict[str, Any]) -> Path:
    return AUDIT_RESULTS / unit["kind"] / f"{unit['key']}.json"


def audit_attempt_path(unit: dict[str, Any], request_id: str) -> Path:
    safe_request_id = re.sub(r"[^A-Za-z0-9_-]+", "_", request_id)
    return (
        AUDIT_ATTEMPT_RESULTS
        / unit["kind"]
        / unit["key"]
        / f"{safe_request_id}.json"
    )


def best_audit_attempt(unit: dict[str, Any]) -> dict[str, Any] | None:
    """Return the strongest correction under the current validation policy."""

    attempt_dir = AUDIT_ATTEMPT_RESULTS / unit["kind"] / unit["key"]
    candidates: list[tuple[int, int, dict[str, Any]]] = []
    if not attempt_dir.is_dir():
        return None
    for path in attempt_dir.glob("*.json"):
        try:
            payload = read_json(path)
            if not isinstance(payload, dict):
                continue
            dossier = payload.get("dossier")
            if not isinstance(dossier, dict):
                continue
            current_errors = validate_dossier(unit, dossier)
            payload["validationErrors"] = current_errors
            candidates.append(
                (len(current_errors), -path.stat().st_mtime_ns, payload)
            )
        except (OSError, ValueError, json.JSONDecodeError):
            continue
    if not candidates:
        return None
    return min(candidates, key=lambda item: (item[0], item[1]))[2]


def audit_attempt_retry_feedback(unit: dict[str, Any]) -> list[str]:
    """Keep equally strong corrections from oscillating between old failures."""

    attempt_dir = AUDIT_ATTEMPT_RESULTS / unit["kind"] / unit["key"]
    candidates: list[list[str]] = []
    if not attempt_dir.is_dir():
        return []
    for path in attempt_dir.glob("*.json"):
        try:
            payload = read_json(path)
            dossier = payload.get("dossier") if isinstance(payload, dict) else None
            if not isinstance(dossier, dict):
                continue
            candidates.append(validate_dossier(unit, dossier))
        except (OSError, ValueError, json.JSONDecodeError):
            continue
    if not candidates:
        return []
    minimum = min(len(errors) for errors in candidates)
    feedback: list[str] = []
    for errors in candidates:
        if len(errors) != minimum:
            continue
        for error in errors:
            if error not in feedback:
                feedback.append(error)
    return feedback


def submit_unit(
    unit: dict[str, Any],
    *,
    catalog: dict[str, Any],
    api_key: str,
    model: str,
    phase: str,
    draft: dict[str, Any] | None = None,
    retry_feedback: list[str] | None = None,
) -> tuple[dict[str, Any], str, str]:
    if phase == "draft":
        schema_path = (
            MODEL_SCHEMA_PATH if unit["kind"] == "model" else GROUP_SCHEMA_PATH
        )
        schema = read_json(schema_path)
        prompt = (
            model_prompt(unit, catalog)
            if unit["kind"] == "model"
            else group_prompt(unit)
        )
    elif phase == "audit" and draft is not None:
        schema_path = (
            MODEL_SCHEMA_PATH if unit["kind"] == "model" else GROUP_SCHEMA_PATH
        )
        schema = read_json(schema_path)
        prompt = audit_prompt(
            unit,
            draft,
            retry_feedback=retry_feedback,
        )
    else:
        raise ValueError(f"invalid research phase {phase!r}")
    response = tavily_request(
        "POST",
        "/research",
        api_key=api_key,
        payload={
            "input": prompt,
            "model": model,
            "citation_format": "numbered",
            "output_schema": provider_schema(schema),
        },
    )
    request_id = str(response["request_id"])
    return response, request_id, sha256_text(prompt)


def extract_dossier(response: dict[str, Any]) -> dict[str, Any]:
    for key in ("content", "result", "output", "answer"):
        value = response.get(key)
        if isinstance(value, dict):
            return value
        if isinstance(value, str):
            stripped = value.strip()
            if stripped.startswith("```"):
                stripped = re.sub(r"^```(?:json)?\s*|\s*```$", "", stripped)
            try:
                parsed = json.loads(stripped)
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
    raise ValueError(
        "completed research response did not contain a structured dossier"
    )


def validate_schema_value(
    value: Any, schema: dict[str, Any], path: str = "$"
) -> list[str]:
    errors: list[str] = []
    expected_type = schema.get("type")
    type_checks = {
        "object": lambda item: isinstance(item, dict),
        "array": lambda item: isinstance(item, list),
        "string": lambda item: isinstance(item, str),
        "boolean": lambda item: isinstance(item, bool),
        "number": lambda item: isinstance(item, (int, float))
        and not isinstance(item, bool),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
    }
    if expected_type and not type_checks[expected_type](value):
        return [f"{path}: expected {expected_type}, got {type(value).__name__}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not in {schema['enum']!r}")
    if isinstance(value, dict):
        required = set(schema.get("required") or [])
        missing = required - set(value)
        errors.extend(f"{path}: missing required property {key}" for key in sorted(missing))
        properties = schema.get("properties") or {}
        if schema.get("additionalProperties") is False:
            errors.extend(
                f"{path}: unexpected property {key}"
                for key in sorted(set(value) - set(properties))
            )
        for key, child in value.items():
            if key in properties:
                errors.extend(
                    validate_schema_value(child, properties[key], f"{path}.{key}")
                )
    if isinstance(value, list) and "items" in schema:
        for index, child in enumerate(value):
            errors.extend(
                validate_schema_value(child, schema["items"], f"{path}[{index}]")
            )
    return errors


def _all_evidence_urls(value: Any) -> Iterable[str]:
    if isinstance(value, list):
        for item in value:
            yield from _all_evidence_urls(item)
        return
    if not isinstance(value, dict):
        return
    for key, child in value.items():
        if key == "evidenceUrls" and isinstance(child, list):
            yield from (str(item) for item in child)
        elif key == "sourceUrl" and isinstance(child, str):
            yield child
        else:
            yield from _all_evidence_urls(child)


def _evidence_claims(
    value: Any, path: str = "$"
) -> Iterable[tuple[str, dict[str, Any]]]:
    if isinstance(value, list):
        for index, item in enumerate(value):
            yield from _evidence_claims(item, f"{path}[{index}]")
        return
    if not isinstance(value, dict):
        return
    if isinstance(value.get("evidenceUrls"), list):
        yield path, value
    for key, child in value.items():
        if key != "evidenceUrls":
            yield from _evidence_claims(child, f"{path}.{key}")


def is_cross_provider_api_url(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    return any(
        (host == expected_host or host.endswith(f".{expected_host}"))
        and path_pattern.search(parsed.path)
        for expected_host, path_pattern in CROSS_PROVIDER_API_PATTERNS
    )


def semantic_model_errors(unit: dict[str, Any], dossier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if dossier.get("family") != unit["key"]:
        errors.append(
            f"$.family must equal research key {unit['key']!r}, got {dossier.get('family')!r}"
        )
    identity = dossier.get("identity") or {}
    if not isinstance(identity, dict):
        identity = {}
    identity_text = " ".join(
        str(identity.get(field) or "")
        for field in ("upstreamName", "checkpoint", "architecture")
    ).lower()
    family_text = " ".join(str(item) for item in unit.get("modelFamilies") or []).lower()
    if "instruct" in family_text and "instruct" not in identity_text:
        errors.append(
            "$.identity must preserve the covered Instruct checkpoint/task suffix"
        )
    raw_sources = dossier.get("sources") or []
    sources = [source for source in raw_sources if isinstance(source, dict)]
    approved_repository_owners = allowed_repository_owners(unit)
    if not sources:
        errors.append("$.sources must contain at least one primary source")
    if requires_original_creator_source(unit) and not has_original_creator_source(
        sources
    ):
        errors.append(
            "$.sources must include the original creator's primary source for "
            "this third-party model packaged by NVIDIA"
        )
    source_urls = {str(item.get("url") or "") for item in sources}
    if len(source_urls) != len(sources):
        errors.append("$.sources must not contain duplicate URLs")
    for required_url in unit.get("sourceUrls") or []:
        if required_url.rstrip("/") in GENERIC_SOURCE_URLS:
            continue
        if required_url not in source_urls:
            errors.append(f"official starting source is absent from $.sources: {required_url}")
    for index, source in enumerate(sources):
        url = str(source.get("url") or "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"$.sources[{index}].url must be an absolute HTTPS URL")
        if parsed.netloc.lower() in FORBIDDEN_SECONDARY_HOSTS:
            errors.append(f"$.sources[{index}] uses forbidden secondary host {parsed.netloc}")
        path_parts = [part.lower() for part in parsed.path.split("/") if part]
        if path_parts and (
            parsed.netloc.lower(),
            path_parts[0],
        ) in FORBIDDEN_SECONDARY_REPOSITORIES:
            errors.append(
                f"$.sources[{index}] uses a third-party mirror/example repository {url}"
            )
        parsed_owner = repository_owner(url)
        if (
            parsed_owner is not None
            and parsed_owner[1] not in approved_repository_owners
        ):
            errors.append(
                f"$.sources[{index}] uses unapproved repository owner "
                f"{parsed_owner[1]!r} for this exact model scope"
            )
        if any(pattern.search(parsed.path) for pattern in FORBIDDEN_SECONDARY_PATH_PATTERNS):
            errors.append(f"$.sources[{index}] uses forbidden secondary URL {url}")
        if self_described_secondary_source(source):
            errors.append(
                f"$.sources[{index}] describes itself as secondary evidence"
            )
        if source.get("primary") is not True:
            errors.append(f"$.sources[{index}].primary must be true")
    for url in _all_evidence_urls(dossier):
        if url and url not in source_urls:
            errors.append(f"evidence URL is absent from $.sources: {url}")
    for path, claim in _evidence_claims(dossier):
        cross_provider_urls = [
            str(url)
            for url in claim.get("evidenceUrls") or []
            if is_cross_provider_api_url(str(url))
        ]
        if not cross_provider_urls:
            continue
        claim_text = " ".join(
            str(value)
            for key, value in claim.items()
            if key != "evidenceUrls"
        ).lower()
        if not any(
            marker in claim_text
            for marker in CROSS_PROVIDER_NON_TRANSFER_MARKERS
        ):
            errors.append(
                f"{path} cites a different cloud provider's hosted API without "
                "stating in the same claim that its contract does not establish "
                "the NVIDIA NIM or Forge contract"
            )
    for index, benchmark in enumerate(dossier.get("benchmarks") or []):
        if not isinstance(benchmark, dict):
            continue
        if not str(benchmark.get("modelScope") or "").strip():
            errors.append(f"$.benchmarks[{index}].modelScope must not be empty")
        if str(benchmark.get("split") or "").strip().lower() in {
            "",
            "unknown",
            "unspecified",
        }:
            errors.append(
                f"$.benchmarks[{index}].split must say 'not reported' or name the split"
            )
        source_locator = str(benchmark.get("sourceLocator") or "").strip()
        if not source_locator:
            errors.append(f"$.benchmarks[{index}].sourceLocator must not be empty")
        elif (
            source_locator.lower() in {"not reported", "unknown", "unspecified"}
            or not SOURCE_LOCATOR_MARKER_RE.search(source_locator)
            or GENERIC_SOURCE_LOCATOR_RE.fullmatch(source_locator)
        ):
            errors.append(
                f"$.benchmarks[{index}].sourceLocator must identify the exact "
                "table, figure, section, appendix, page, heading, or repository path"
            )
        benchmark_source = urlparse(str(benchmark.get("sourceUrl") or ""))
        paper_source = (
            benchmark_source.netloc.lower()
            in {"arxiv.org", "www.biorxiv.org", "biorxiv.org"}
            or benchmark_source.path.lower().endswith(".pdf")
        )
        if paper_source and not re.search(
            r"(?:\d|table\s+[a-z]\b|appendix\s+[a-z]\b|[\"'`])",
            source_locator,
            re.IGNORECASE,
        ):
            errors.append(
                f"$.benchmarks[{index}].sourceLocator for a paper must include "
                "a numbered/named table, figure, section, appendix, page, or heading"
            )
        value = str(benchmark.get("value") or "").strip()
        if (
            not value
            or value.lower().startswith(("evidence gap:", "not reported", "unknown"))
            or not re.search(r"\d", value)
        ):
            errors.append(
                f"$.benchmarks[{index}].value must contain a reported numeric result"
            )
    for hint_index, hint in enumerate(unit.get("manualReviewHints") or []):
        hint_url = str(hint.get("sourceUrl") or "")
        hint_locator = str(hint.get("sourceLocator") or "").strip().lower()
        if hint.get("requireSource") and hint_url not in source_urls:
            errors.append(
                f"manualReviewHints[{hint_index}] requires primary source "
                f"{hint_url} in $.sources"
            )
        if hint.get("requireBenchmark"):
            matching_rows = [
                benchmark
                for benchmark in dossier.get("benchmarks") or []
                if isinstance(benchmark, dict)
                and str(benchmark.get("sourceUrl") or "") == hint_url
                and (
                    not hint_locator
                    or hint_locator
                    in str(benchmark.get("sourceLocator") or "").lower()
                )
            ]
            if not matching_rows:
                errors.append(
                    f"manualReviewHints[{hint_index}] requires an exact benchmark "
                    f"row from {hint_url} at {hint.get('sourceLocator')}"
                )
    evidence_gaps = [
        str(item).strip().lower() for item in dossier.get("evidenceGaps") or []
    ]
    if not dossier.get("benchmarks") and not any(
        "benchmark" in item or "evaluation result" in item
        for item in evidence_gaps
    ):
        errors.append(
            "$.benchmarks is empty without a benchmark-specific evidence gap"
        )
    if not dossier.get("benchmarks"):
        benchmark_gaps = [
            item
            for item in dossier.get("evidenceGaps") or []
            if "benchmark" in str(item).lower()
            or "evaluation result" in str(item).lower()
        ]
        if not any(
            "https://" in str(item)
            and SOURCE_LOCATOR_MARKER_RE.search(str(item))
            for item in benchmark_gaps
        ):
            errors.append(
                "$.benchmarks is empty without an evidence gap naming the exact "
                "primary-source URL and checked table/figure/section/page/heading/path"
            )
    if not dossier.get("comparisons") and not any(
        "compar" in item or "peer" in item or "alternative" in item
        for item in evidence_gaps
    ):
        errors.append(
            "$.comparisons is empty without a comparison-specific evidence gap"
        )
    for section in ("recommendedUseCases", "avoidUseCases", "limitations", "safety"):
        if not dossier.get(section):
            errors.append(f"$.{section} must contain at least one scoped item")
    for index, item in enumerate(dossier.get("recommendedUseCases") or []):
        if not isinstance(item, dict):
            continue
        if not item.get("evidenceUrls"):
            errors.append(
                f"$.recommendedUseCases[{index}].evidenceUrls must not be empty"
            )
    required_claim_sections = (
        ("inputPreparation", "semanticInputs", ("semantic input", "input type")),
        ("inputPreparation", "acceptedFormats", ("accepted format", "input format")),
        ("inputPreparation", "preprocessing", ("preprocess", "tokeniz", "featur")),
        ("inputPreparation", "validation", ("input validation", "input bound")),
        ("outputInterpretation", "outputs", ("output",)),
        ("outputInterpretation", "interpretation", ("interpret",)),
        ("outputInterpretation", "validation", ("output validation", "post-inference")),
    )
    for parent, section, gap_markers in required_claim_sections:
        parent_payload = dossier.get(parent) or {}
        items = (
            parent_payload.get(section) or []
            if isinstance(parent_payload, dict)
            else []
        )
        if not items and not any(
            any(marker in gap for marker in gap_markers) for gap in evidence_gaps
        ):
            errors.append(
                f"$.{parent}.{section} is empty without a section-specific evidence gap"
            )
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            if item.get("evidenceUrls"):
                continue
            statement = str(item.get("statement") or "").strip().lower()
            if not (
                statement.startswith("evidence gap:")
                or statement.startswith("forge policy:")
            ):
                errors.append(
                    f"$.{parent}.{section}[{index}] without evidence must be "
                    "labeled as a Forge policy or evidence gap"
                )
    for section in ("limitations", "safety"):
        for index, item in enumerate(dossier.get(section) or []):
            if not isinstance(item, dict):
                continue
            if item.get("evidenceUrls"):
                continue
            statement = str(item.get("statement") or "").lower()
            if "forge policy" not in statement and "evidence gap" not in statement:
                errors.append(
                    f"$.{section}[{index}] without evidence must be labeled "
                    "as a Forge policy or evidence gap"
                )
    return errors


def semantic_group_errors(unit: dict[str, Any], dossier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if dossier.get("category") != unit["category"]:
        errors.append("$.category does not match the planned category")
    if dossier.get("group") != unit["group"]:
        errors.append("$.group does not match the planned group")
    raw_sources = dossier.get("sources") or []
    sources = [source for source in raw_sources if isinstance(source, dict)]
    approved_repository_owners = allowed_repository_owners(unit)
    source_urls = {str(source.get("url") or "") for source in sources}
    normalized_source_urls = {url.rstrip("/") for url in source_urls}
    if not source_urls:
        errors.append("$.sources must contain at least one primary source")
    for index, source in enumerate(raw_sources):
        if not isinstance(source, dict):
            continue
        parsed = urlparse(str(source.get("url") or ""))
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"$.sources[{index}].url must be an absolute HTTPS URL")
        if parsed.netloc.lower() in FORBIDDEN_SECONDARY_HOSTS:
            errors.append(f"$.sources[{index}] uses forbidden secondary host {parsed.netloc}")
        path_parts = [part.lower() for part in parsed.path.split("/") if part]
        if path_parts and (
            parsed.netloc.lower(),
            path_parts[0],
        ) in FORBIDDEN_SECONDARY_REPOSITORIES:
            errors.append(
                f"$.sources[{index}] uses a third-party mirror/example repository "
                f"{source.get('url') or ''}"
            )
        parsed_owner = repository_owner(str(source.get("url") or ""))
        if (
            parsed_owner is not None
            and parsed_owner[1] not in approved_repository_owners
        ):
            errors.append(
                f"$.sources[{index}] uses unapproved repository owner "
                f"{parsed_owner[1]!r} for this Forge model group"
            )
        if any(pattern.search(parsed.path) for pattern in FORBIDDEN_SECONDARY_PATH_PATTERNS):
            errors.append(
                f"$.sources[{index}] uses forbidden secondary URL "
                f"{source.get('url') or ''}"
            )
        if self_described_secondary_source(source):
            errors.append(
                f"$.sources[{index}] describes itself as secondary evidence"
            )
        if source.get("primary") is not True:
            errors.append(f"$.sources[{index}].primary must be true")
    candidate_slugs = {
        str(model.get("slug") or "") for model in unit.get("forgeModels") or []
    }
    mentioned_slugs: set[str] = set()
    decision_rules = dossier.get("decisionRules") or []
    if not decision_rules:
        errors.append("$.decisionRules must contain exact Forge routing rules")
    for index, rule in enumerate(decision_rules):
        if not isinstance(rule, dict):
            continue
        preferred = str(rule.get("prefer") or "")
        if preferred == "insufficient-evidence":
            pass
        elif preferred not in candidate_slugs:
            errors.append(
                f"$.decisionRules[{index}].prefer must be an exact Forge "
                "candidate slug or 'insufficient-evidence'"
            )
        else:
            mentioned_slugs.add(preferred)
        alternatives = rule.get("alternatives") or []
        if not isinstance(alternatives, list):
            continue
        if len(set(alternatives)) != len(alternatives):
            errors.append(
                f"$.decisionRules[{index}].alternatives must not contain duplicates"
            )
        for alternative_index, alternative in enumerate(alternatives):
            if alternative not in candidate_slugs:
                errors.append(
                    f"$.decisionRules[{index}].alternatives[{alternative_index}] "
                    "must be an exact Forge candidate slug"
                )
            else:
                mentioned_slugs.add(alternative)
            if alternative == preferred:
                errors.append(
                    f"$.decisionRules[{index}].alternatives[{alternative_index}] "
                    "must not repeat the preferred Forge slug"
                )
        for url in rule.get("evidenceUrls") or []:
            if url not in source_urls:
                errors.append(f"decision-rule evidence URL is absent from $.sources: {url}")
    missing_candidates = sorted(candidate_slugs - mentioned_slugs)
    if missing_candidates:
        errors.append(
            "$.decisionRules do not cover exact Forge candidate slugs: "
            + ", ".join(missing_candidates)
        )
    for model in unit.get("forgeModels") or []:
        source_url = str(model.get("sourceUrl") or "").rstrip("/")
        if not source_url or source_url in GENERIC_SOURCE_URLS:
            continue
        if source_url not in normalized_source_urls:
            errors.append(
                "$.sources is missing exact Forge candidate sourceUrl for "
                f"{model.get('slug')}: {source_url}"
            )
    return errors


def validate_dossier(unit: dict[str, Any], dossier: dict[str, Any]) -> list[str]:
    schema_path = MODEL_SCHEMA_PATH if unit["kind"] == "model" else GROUP_SCHEMA_PATH
    errors = validate_schema_value(dossier, read_json(schema_path))
    errors.extend(
        semantic_model_errors(unit, dossier)
        if unit["kind"] == "model"
        else semantic_group_errors(unit, dossier)
    )
    return errors


def envelope(
    unit: dict[str, Any],
    *,
    response: dict[str, Any],
    dossier: dict[str, Any],
    prompt_sha256: str,
    provider_model: str,
    errors: list[str],
) -> dict[str, Any]:
    return {
        "schemaVersion": "1.0.0",
        "researchKey": unit["key"],
        "kind": unit["kind"],
        "researchedAt": utc_now(),
        "sourceScope": unit.get("sourceScope"),
        "sourceUrls": unit.get("sourceUrls") or [],
        "coveredForgeModels": unit["forgeModels"],
        "upstreamAgentSkills": mapped_agent_skills(unit)
        if unit["kind"] == "model"
        else [],
        "provenance": {
            "provider": "Tavily Research",
            "model": provider_model,
            "requestId": response.get("request_id"),
            "promptSha256": prompt_sha256,
        },
        "validation": {
            "status": "accepted" if not errors else "rejected",
            "errors": errors,
        },
        "dossier": dossier,
    }


def redact_public_provider_request_ids(payload: dict[str, Any]) -> dict[str, Any]:
    """Keep provider request IDs in ignored state, not public evidence."""

    redacted = json.loads(json.dumps(payload))
    provenance = redacted.get("provenance")
    if isinstance(provenance, dict):
        for field in ("requestId", "draftRequestId", "auditRequestId"):
            provenance.pop(field, None)
    return redacted


def selected_units(
    kind: str, catalog: dict[str, Any], only: set[str], limit: int | None
) -> list[dict[str, Any]]:
    units = []
    if kind in {"models", "all"}:
        units.extend(model_units(catalog))
    if kind in {"groups", "all"}:
        units.extend(group_units(catalog))
    if only:
        units = [unit for unit in units if unit["key"] in only]
    if limit is not None:
        units = units[:limit]
    return units


def reset_unit(unit: dict[str, Any], state: dict[str, Any]) -> None:
    for path in (draft_path(unit), audit_path(unit), output_path(unit)):
        path.unlink(missing_ok=True)
    for phase in ("draft", "audit"):
        state["jobs"].pop(phase_job_key(unit, phase), None)


def command_plan(args: argparse.Namespace) -> int:
    catalog = read_json(CATALOG_PATH)
    models = model_units(catalog)
    groups = group_units(catalog)
    print(
        json.dumps(
            {
                "exactForgeModels": len(catalog["models"]),
                "upstreamResearchUnits": len(models),
                "comparisonGroups": len(groups),
                "modelUnitsWithMultipleServingVariants": sum(
                    len(unit["forgeModels"]) > 1 for unit in models
                ),
            },
            indent=2,
        )
    )
    return 0


def command_submit(args: argparse.Namespace) -> int:
    catalog = read_json(CATALOG_PATH)
    units = selected_units(
        args.kind, catalog, set(args.only or []), args.limit
    )
    api_key = resolve_tavily_key()
    state = load_state(args.kind)
    if args.force:
        for unit in units:
            reset_unit(unit, state)
        write_json(state_path(args.kind), state)

    selected_job_keys = {
        phase_job_key(unit, phase)
        for unit in units
        for phase in ("draft", "audit")
    }
    active_count, available_slots = available_submission_slots(
        state,
        selected_job_keys,
        args.max_active,
    )
    if available_slots == 0:
        print(
            json.dumps(
                {
                    "activeBeforeSubmit": active_count,
                    "maxActive": args.max_active,
                    "submittedCount": 0,
                },
                sort_keys=True,
            )
        )
        return 0
    candidates: list[
        tuple[dict[str, Any], str, dict[str, Any] | None, list[str]]
    ] = []
    for unit in units:
        if has_accepted_output(unit):
            continue
        draft_validation_errors: list[str] = []
        if draft_path(unit).is_file():
            phase = "audit"
            draft_payload = read_json(draft_path(unit))
            draft = draft_payload["dossier"]
            draft_validation_errors = [
                str(item)
                for item in draft_payload.get("validation", {}).get("errors", [])
            ]
        else:
            phase = "draft"
            draft = None
        job_key = phase_job_key(unit, phase)
        existing = state["jobs"].get(job_key, {})
        seeded_from_attempt = False
        if (
            phase == "audit"
            and existing.get("status") == "completed"
            and output_path(unit).is_file()
        ):
            output_payload = read_json(output_path(unit))
            current_errors = validate_dossier(
                unit,
                output_payload.get("dossier") or {},
            )
            if current_errors:
                existing = {
                    **existing,
                    "status": "rejected",
                    "validationErrors": current_errors,
                }
                state["jobs"][job_key] = existing
        if (
            phase == "audit"
            and existing.get("status") in {"failed", "rejected"}
            and existing.get("schemaMode") == "dossier-v1"
        ):
            prior_attempt = best_audit_attempt(unit)
            if prior_attempt is not None:
                draft = prior_attempt["dossier"]
                draft_validation_errors = audit_attempt_retry_feedback(unit) or [
                    str(item)
                    for item in prior_attempt.get("validationErrors") or []
                ]
                seeded_from_attempt = True
        if existing.get("status") not in {None, "failed", "rejected"}:
            continue
        if int(existing.get("attempt") or 0) >= args.max_attempts:
            continue
        existing_validation_errors = (
            []
            if seeded_from_attempt
            or (
                phase == "audit"
                and existing.get("schemaMode") != "dossier-v1"
            )
            else [
                str(item)
                for item in existing.get("validationErrors") or []
            ]
        )
        retry_feedback = list(
            dict.fromkeys(
                [
                    *draft_validation_errors,
                    *existing_validation_errors,
                ]
            )
        )
        candidates.append(
            (
                unit,
                phase,
                draft,
                retry_feedback,
            )
        )
        if len(candidates) >= available_slots:
            break

    def submit(
        candidate: tuple[
            dict[str, Any],
            str,
            dict[str, Any] | None,
            list[str],
        ]
    ) -> tuple[dict[str, Any], str, dict[str, Any]]:
        unit, phase, draft, retry_feedback = candidate
        response, request_id, prompt_hash = submit_unit(
            unit,
            catalog=catalog,
            api_key=api_key,
            model=args.model,
            phase=phase,
            draft=draft,
            retry_feedback=retry_feedback,
        )
        prior = state["jobs"].get(phase_job_key(unit, phase), {})
        return unit, phase, {
            "requestId": request_id,
            "status": response.get("status") or "pending",
            "submittedAt": utc_now(),
            "providerModel": args.model,
            "promptSha256": prompt_hash,
            "phase": phase,
            "attempt": int(prior.get("attempt") or 0) + 1,
            "schemaMode": "dossier-v1" if phase == "audit" else "draft-v1",
        }

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(submit, candidate): candidate for candidate in candidates
        }
        for future in as_completed(futures):
            unit, phase, job = future.result()
            job_key = phase_job_key(unit, phase)
            state["jobs"][job_key] = job
            write_json(state_path(args.kind), state)
            print(
                json.dumps(
                    {
                        "submitted": job_key,
                        "requestId": job["requestId"],
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    print(
        json.dumps(
            {
                "activeBeforeSubmit": active_count,
                "maxActive": args.max_active,
                "submittedCount": len(candidates),
            },
            sort_keys=True,
        )
    )
    return 0


def command_poll(args: argparse.Namespace) -> int:
    catalog = read_json(CATALOG_PATH)
    units = selected_units(args.kind, catalog, set(args.only or []), args.limit)
    by_job_key = {
        phase_job_key(unit, phase): (unit, phase)
        for unit in units
        for phase in ("draft", "audit")
    }
    state = load_state(args.kind)
    api_key = resolve_tavily_key()
    active = [
        (job_key, job)
        for job_key, job in state["jobs"].items()
        if job_key in by_job_key
        and job.get("status") not in {"completed", "failed", "rejected"}
    ]

    def poll(
        item: tuple[str, dict[str, Any]]
    ) -> tuple[str, dict[str, Any], dict[str, Any]]:
        job_key, job = item
        response = tavily_request(
            "GET",
            f"/research/{quote(str(job['requestId']), safe='')}",
            api_key=api_key,
            timeout=120,
        )
        return job_key, job, response

    completed = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(poll, item): item[0] for item in active}
        for future in as_completed(futures):
            job_key, job, response = future.result()
            status = str(response.get("status") or "unknown")
            job["status"] = status
            job["lastPolledAt"] = utc_now()
            if status == "completed":
                unit, phase = by_job_key[job_key]
                structured = extract_dossier(response)
                if phase == "draft":
                    errors = validate_dossier(unit, structured)
                    result = envelope(
                        unit,
                        response=response,
                        dossier=structured,
                        prompt_sha256=job["promptSha256"],
                        provider_model=job["providerModel"],
                        errors=errors,
                    )
                    result["validation"]["status"] = "draft"
                    write_json(draft_path(unit), result)
                    job["status"] = "completed"
                    job["validationErrors"] = errors
                else:
                    dossier, provider_audit, dropped_paths = extract_audited_dossier(
                        unit,
                        structured,
                    )
                    dossier, reconciled_urls = reconcile_dossier_sources(unit, dossier)
                    dropped_paths.extend(
                        f"reconciled:{url}" for url in reconciled_urls
                    )
                    errors = validate_dossier(unit, dossier)
                    if provider_audit.get("verdict") == "rejected":
                        errors.append("independent audit verdict was rejected")
                    draft_result = read_json(draft_path(unit))
                    verdict, audit_summary, issues = derived_audit_metadata(
                        draft_result,
                        dossier,
                        provider_audit,
                        dropped_paths,
                    )
                    request_id = str(
                        response.get("request_id")
                        or job.get("requestId")
                        or "unknown"
                    )
                    write_json(
                        audit_attempt_path(unit, request_id),
                        {
                            "requestId": request_id,
                            "schemaMode": job.get("schemaMode"),
                            "promptSha256": job.get("promptSha256"),
                            "providerModel": job.get("providerModel"),
                            "dossier": dossier,
                            "droppedPaths": dropped_paths,
                            "validationErrors": errors,
                            "providerAudit": provider_audit,
                        },
                    )
                    audit_record = {
                        "verdict": verdict,
                        "auditSummary": audit_summary,
                        "issues": issues,
                        "correctedDossier": dossier,
                        "validationErrors": errors,
                        "requestId": request_id,
                    }
                    write_json(audit_path(unit), audit_record)
                    if not errors:
                        result = envelope(
                            unit,
                            response=response,
                            dossier=dossier,
                            prompt_sha256=job["promptSha256"],
                            provider_model=job["providerModel"],
                            errors=[],
                        )
                        result["provenance"]["draftRequestId"] = draft_result[
                            "provenance"
                        ]["requestId"]
                        result["provenance"]["auditRequestId"] = response.get(
                            "request_id"
                        )
                        result["audit"] = {
                            "verdict": verdict,
                            "summary": audit_summary,
                            "issues": issues,
                        }
                        write_json(
                            output_path(unit),
                            redact_public_provider_request_ids(result),
                        )
                    job["status"] = "completed" if not errors else "rejected"
                    job["validationErrors"] = errors
                completed += 1
            elif status == "failed":
                job["error"] = response.get("error")
            state["jobs"][job_key] = job
            write_json(state_path(args.kind), state)
            print(
                json.dumps(
                    {
                        "job": job_key,
                        "status": job["status"],
                        "validationErrors": len(job.get("validationErrors") or []),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    print(
        json.dumps(
            {"polledCount": len(active), "completedCount": completed},
            sort_keys=True,
        )
    )
    return 0


def command_run_locked(args: argparse.Namespace) -> int:
    if args.force:
        catalog = read_json(CATALOG_PATH)
        units = selected_units(
            args.kind, catalog, set(args.only or []), args.limit
        )
        state = load_state(args.kind)
        for unit in units:
            reset_unit(unit, state)
        write_json(state_path(args.kind), state)
        args.force = False
    while True:
        command_submit(args)
        command_poll(args)
        state = load_state(args.kind)
        catalog = read_json(CATALOG_PATH)
        units = selected_units(
            args.kind, catalog, set(args.only or []), args.limit
        )
        if all(has_accepted_output(unit) for unit in units):
            return 0
        terminal_failures = []
        for unit in units:
            if has_accepted_output(unit):
                continue
            for phase in ("draft", "audit"):
                status = state["jobs"].get(
                    phase_job_key(unit, phase), {}
                ).get("status")
                attempts = int(
                    state["jobs"].get(
                        phase_job_key(unit, phase), {}
                    ).get("attempt")
                    or 0
                )
                if (
                    status in {"failed", "rejected"}
                    and attempts >= args.max_attempts
                ):
                    terminal_failures.append(phase_job_key(unit, phase))
        if terminal_failures:
            print(
                json.dumps(
                    {"terminalFailures": terminal_failures},
                    sort_keys=True,
                )
            )
            return 1
        time.sleep(args.poll_seconds)


def command_run(args: argparse.Namespace) -> int:
    lock_path = state_path(args.kind).with_suffix(".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w", encoding="utf-8") as lock_file:
        try:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print(
                json.dumps(
                    {
                        "error": "research controller already running",
                        "kind": args.kind,
                        "lockPath": str(lock_path.relative_to(ROOT)),
                    },
                    sort_keys=True,
                )
            )
            return 2
        return command_run_locked(args)


def command_validate(args: argparse.Namespace) -> int:
    catalog = read_json(CATALOG_PATH)
    units = selected_units(args.kind, catalog, set(args.only or []), args.limit)
    failures: dict[str, list[str]] = {}
    missing: list[str] = []
    covered_slugs: set[str] = set()
    for unit in units:
        path = output_path(unit)
        if not path.is_file():
            missing.append(state_job_key(unit))
            continue
        payload = read_json(path)
        dossier = payload.get("dossier") or {}
        errors = validate_dossier(unit, dossier)
        if payload.get("audit", {}).get("verdict") not in {"accepted", "revised"}:
            errors.append("missing accepted/revised independent audit")
        if errors:
            failures[state_job_key(unit)] = errors
        if unit["kind"] == "model":
            covered_slugs.update(item["slug"] for item in unit["forgeModels"])
    expected_slugs = (
        {item["slug"] for item in catalog["models"]}
        if args.kind in {"models", "all"} and not args.only and args.limit is None
        else covered_slugs
    )
    missing_slugs = sorted(expected_slugs - covered_slugs)
    print(
        json.dumps(
            {
                "checked": len(units),
                "missingDossiers": missing,
                "validationFailures": failures,
                "missingExactModelCoverage": missing_slugs,
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 1 if missing or failures or missing_slugs else 0


def command_prepare_publication(args: argparse.Namespace) -> int:
    catalog = read_json(CATALOG_PATH)
    units = selected_units(args.kind, catalog, set(args.only or []), args.limit)
    updated = 0
    redacted_count = 0
    checked = 0
    for unit in units:
        path = output_path(unit)
        if not path.is_file():
            continue
        checked += 1
        payload = read_json(path)
        if unit["kind"] == "model":
            payload["upstreamAgentSkills"] = mapped_agent_skills(unit)
        redacted = redact_public_provider_request_ids(payload)
        if redacted != payload:
            redacted_count += 1
        if redacted != payload:
            payload = redacted
        original = read_json(path)
        if payload != original:
            write_json(path, payload)
            updated += 1
    print(
        json.dumps(
            {
                "checked": checked,
                "updatedPayloads": updated,
                "redactedPayloads": redacted_count,
            },
            sort_keys=True,
        )
    )
    return 0


def command_recover_audit(args: argparse.Namespace) -> int:
    if args.kind == "all" or len(args.only or []) != 1:
        raise ValueError("recover-audit requires one --only key and a concrete kind")
    catalog = read_json(CATALOG_PATH)
    units = selected_units(args.kind, catalog, set(args.only), None)
    if len(units) != 1:
        raise ValueError("recover-audit selection did not resolve exactly one unit")
    unit = units[0]
    attempt_file = audit_attempt_path(unit, args.request_id)
    if not attempt_file.is_file():
        raise ValueError("requested preserved audit attempt does not exist")
    attempt = read_json(attempt_file)
    dossier, repaired_urls = reconcile_dossier_sources(unit, attempt["dossier"])
    errors = validate_dossier(unit, dossier)
    if errors:
        print(
            json.dumps(
                {"recovered": False, "validationErrors": errors},
                indent=2,
            )
        )
        return 1
    prompt_sha256 = args.prompt_sha256 or attempt.get("promptSha256")
    provider_model = args.provider_model or attempt.get("providerModel")
    if not prompt_sha256 or not provider_model:
        raise ValueError(
            "recover-audit requires recorded or explicit prompt/model provenance"
        )
    draft_result = read_json(draft_path(unit))
    dropped_paths = [
        *[str(item) for item in attempt.get("droppedPaths") or []],
        *[f"reconciled:{url}" for url in repaired_urls],
    ]
    verdict, audit_summary, issues = derived_audit_metadata(
        draft_result,
        dossier,
        attempt.get("providerAudit") or {},
        dropped_paths,
    )
    response = {"request_id": args.request_id}
    result = envelope(
        unit,
        response=response,
        dossier=dossier,
        prompt_sha256=str(prompt_sha256),
        provider_model=str(provider_model),
        errors=[],
    )
    result["provenance"]["draftRequestId"] = draft_result["provenance"]["requestId"]
    result["provenance"]["auditRequestId"] = args.request_id
    result["provenance"]["localRecovery"] = {
        "kind": "first-party-child-source-index",
        "reconciledSourceUrls": repaired_urls,
    }
    result["audit"] = {
        "verdict": verdict,
        "summary": audit_summary,
        "issues": issues,
    }
    write_json(
        output_path(unit),
        redact_public_provider_request_ids(result),
    )
    write_json(
        audit_path(unit),
        {
            "verdict": verdict,
            "auditSummary": audit_summary,
            "issues": issues,
            "correctedDossier": dossier,
            "validationErrors": [],
            "requestId": args.request_id,
            "localRecovery": result["provenance"]["localRecovery"],
        },
    )
    state = load_state(args.kind)
    job_key = phase_job_key(unit, "audit")
    if job_key in state["jobs"]:
        state["jobs"][job_key]["status"] = "completed"
        state["jobs"][job_key]["validationErrors"] = []
        state["jobs"][job_key]["recoveredFromRequestId"] = args.request_id
        write_json(state_path(args.kind), state)
    print(
        json.dumps(
            {
                "recovered": True,
                "requestId": args.request_id,
                "reconciledSourceUrls": repaired_urls,
                "output": str(output_path(unit).relative_to(ROOT)),
            },
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("plan")

    def add_selection(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument(
            "--kind", choices=("models", "groups", "all"), default="all"
        )
        subparser.add_argument("--only", action="append")
        subparser.add_argument("--limit", type=int)

    for command in ("submit", "poll", "run"):
        subparser = subparsers.add_parser(command)
        add_selection(subparser)
        subparser.add_argument("--workers", type=int, default=6)
        subparser.add_argument("--model", choices=("mini", "pro", "auto"), default="pro")
        subparser.add_argument("--force", action="store_true")
        subparser.add_argument(
            "--max-active",
            type=int,
            default=8,
            help="maximum pending/in-progress provider jobs for this selection",
        )
        subparser.add_argument(
            "--max-attempts",
            type=int,
            default=3,
            help="maximum submissions per draft or audit phase",
        )
        if command == "run":
            subparser.add_argument("--poll-seconds", type=float, default=15)
    validate = subparsers.add_parser("validate")
    add_selection(validate)
    prepare_publication = subparsers.add_parser("prepare-publication")
    add_selection(prepare_publication)
    recover = subparsers.add_parser("recover-audit")
    add_selection(recover)
    recover.add_argument("--request-id", required=True)
    recover.add_argument("--prompt-sha256")
    recover.add_argument(
        "--provider-model",
        choices=("mini", "pro", "auto"),
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "plan":
            return command_plan(args)
        if args.command == "submit":
            return command_submit(args)
        if args.command == "poll":
            return command_poll(args)
        if args.command == "run":
            return command_run(args)
        if args.command == "validate":
            return command_validate(args)
        if args.command == "prepare-publication":
            return command_prepare_publication(args)
        if args.command == "recover-audit":
            return command_recover_audit(args)
    except (RuntimeError, ValueError, KeyError) as exc:
        print(f"research_catalog: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
