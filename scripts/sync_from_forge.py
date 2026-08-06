#!/usr/bin/env python3
"""Generate portable, exact-model skills from the public Forge API."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


DEFAULT_API_BASE = "https://forge.nebius.cloud/api/proxy"
DEFAULT_REPOSITORY = "https://github.com/rene-tech/forge-skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-base", default=DEFAULT_API_BASE)
    parser.add_argument("--output-root", default=".")
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    parser.add_argument("--repository-ref", default="main")
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--generated-at")
    parser.add_argument(
        "--allow-missing-research",
        action="store_true",
        help=(
            "Bootstrap only: generate source-linked skills without audited "
            "research. Active publication must not use this flag."
        ),
    )
    return parser.parse_args()


def fetch_json(url: str) -> Any:
    request = Request(url, headers={"User-Agent": "forge-skills-sync/1.0"})
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def fetch_all_models(api_base: str) -> list[dict[str, Any]]:
    models: list[dict[str, Any]] = []
    offset = 0
    while True:
        query = urlencode(
            {"include_variants": "true", "limit": 200, "offset": offset}
        )
        payload = fetch_json(f"{api_base.rstrip('/')}/v1/models?{query}")
        page = payload.get("models") or []
        models.extend(page)
        offset += len(page)
        if not page or offset >= int(payload.get("total") or len(models)):
            return models


def fetch_exact_skills(
    api_base: str,
    slugs: list[str],
    *,
    workers: int,
) -> dict[str, dict[str, Any]]:
    def load(slug: str) -> tuple[str, dict[str, Any]]:
        encoded = quote(slug, safe="")
        return slug, fetch_json(
            f"{api_base.rstrip('/')}/v1/model-skills/{encoded}"
        )

    loaded: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        futures = {executor.submit(load, slug): slug for slug in slugs}
        for future in as_completed(futures):
            slug, payload = future.result()
            loaded[slug] = payload
    return loaded


def slugify(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "uncategorized"


def group_for(model: dict[str, Any], skill: dict[str, Any]) -> str:
    declared_group = str(skill.get("group") or "").strip()
    if declared_group:
        return slugify(declared_group)
    category = slugify(str(model.get("category") or "uncategorized"))
    if category in {"healthcare", "life-science"}:
        return slugify(str(skill.get("domain") or "scientific-models"))
    if category == "earth-observation":
        return "earth-observation"

    inputs = {str(item).lower() for item in model.get("modality_input") or []}
    outputs = {str(item).lower() for item in model.get("modality_output") or []}
    text = " ".join(
        [
            str(model.get("slug") or ""),
            str(model.get("name") or ""),
            *[str(item) for item in model.get("tags") or []],
        ]
    ).lower()

    if category == "physical-ai":
        if "robot_action" in outputs or "robot_state" in inputs:
            return "robotics-control"
        if "video" in outputs:
            return "world-video-generation"
        if "image" in outputs:
            return "world-image-generation"
        return "physical-ai"

    if "embedding" in outputs:
        return "embeddings"
    if outputs.intersection({"ranking", "score", "scores", "similarity"}):
        return "retrieval-and-reranking"
    if "video" in outputs:
        return "video-generation"
    if "image" in outputs:
        return "image-generation" if "text" in inputs else "vision"
    if "audio" in inputs or "audio" in outputs:
        return "audio"
    if inputs.intersection({"image", "video"}) and "text" in outputs:
        return "vision-language"
    if outputs.intersection({"classification", "detection", "layout"}):
        return "classification-and-detection"
    if "document" in inputs or any(
        marker in text for marker in ("ocr", "parse", "document")
    ):
        return "document-ai"
    if "text" in outputs:
        return "language"
    return "multimodal-and-specialized"


def normalized_text(value: Any, fallback: str) -> str:
    text = " ".join(str(value or "").split())
    return text or fallback


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def portable_skill_name(model_slug: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", model_slug.lower()).strip("-")
    candidate = f"use-forge-{normalized or 'model'}"
    if len(candidate) <= 63:
        return candidate
    digest = sha256(candidate)[:8]
    return f"{candidate[:54].rstrip('-')}-{digest}"


def yaml_scalar(value: str) -> str:
    return value.replace("\n", " ").replace("\r", " ").strip()


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def require_public_research_provenance(payload: dict[str, Any], path: Path) -> None:
    provenance = payload.get("provenance")
    if not isinstance(provenance, dict):
        return
    leaked = sorted(
        field
        for field in ("requestId", "draftRequestId", "auditRequestId")
        if provenance.get(field)
    )
    if leaked:
        raise ValueError(
            f"research contains provider request IDs ({', '.join(leaked)}): "
            f"{path}; run research_catalog.py prepare-publication"
        )


def load_research_by_slug(
    root: Path,
    expected_slugs: set[str],
    *,
    allow_missing: bool,
) -> dict[str, dict[str, Any]]:
    by_slug: dict[str, dict[str, Any]] = {}
    for path in sorted((root / "research" / "models").glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        require_public_research_provenance(payload, path)
        if payload.get("validation", {}).get("status") != "accepted":
            if allow_missing:
                continue
            raise ValueError(f"research validation is not accepted: {path}")
        if payload.get("audit", {}).get("verdict") not in {"accepted", "revised"}:
            if allow_missing:
                continue
            raise ValueError(f"research has no accepted independent audit: {path}")
        for model in payload.get("coveredForgeModels") or []:
            slug = str(model["slug"])
            if slug in by_slug:
                raise ValueError(f"model research is duplicated for {slug}")
            by_slug[slug] = payload
    missing = sorted(expected_slugs - set(by_slug))
    extra = sorted(set(by_slug) - expected_slugs)
    if extra:
        raise ValueError(
            "research references models absent from the live catalog: "
            + ", ".join(extra)
        )
    if missing and not allow_missing:
        raise ValueError(
            "audited research is required before skill publication; missing: "
            + ", ".join(missing)
        )
    return by_slug


def load_group_research(
    root: Path,
    expected_groups: set[tuple[str, str]],
    *,
    allow_missing: bool,
) -> dict[tuple[str, str], dict[str, Any]]:
    by_group: dict[tuple[str, str], dict[str, Any]] = {}
    for path in sorted((root / "research" / "groups").glob("*/*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        require_public_research_provenance(payload, path)
        if payload.get("validation", {}).get("status") != "accepted":
            if allow_missing:
                continue
            raise ValueError(f"group research validation is not accepted: {path}")
        if payload.get("audit", {}).get("verdict") not in {"accepted", "revised"}:
            if allow_missing:
                continue
            raise ValueError(
                f"group research has no accepted independent audit: {path}"
            )
        dossier = payload.get("dossier") or {}
        key = (str(dossier.get("category")), str(dossier.get("group")))
        if key in by_group:
            raise ValueError(f"group research is duplicated for {key[0]}/{key[1]}")
        by_group[key] = payload
    missing = sorted(expected_groups - set(by_group))
    extra = sorted(set(by_group) - expected_groups)
    if extra:
        raise ValueError(
            "research references groups absent from the live catalog: "
            + ", ".join(f"{category}/{group}" for category, group in extra)
        )
    if missing and not allow_missing:
        raise ValueError(
            "audited group research is required before skill publication; missing: "
            + ", ".join(f"{category}/{group}" for category, group in missing)
        )
    return by_group


def research_statement_lines(items: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for item in items:
        urls = item.get("evidenceUrls") or []
        suffix = f" Sources: {', '.join(urls)}" if urls else ""
        lines.append(f"- {item['statement']}{suffix}")
    return lines


def render_markdown_lines(lines: list[str]) -> str:
    """Render generated Markdown without whitespace-only artifacts."""

    return "\n".join(line.rstrip() for line in lines).rstrip() + "\n"


def research_markdown(research: dict[str, Any]) -> str:
    dossier = research["dossier"]
    identity = dossier["identity"]
    lines = [
        "# Audited model research",
        "",
        "## Contents",
        "",
        "- [Identity](#identity)",
        "- [Selection](#selection)",
        "- [Input preparation](#input-preparation)",
        "- [Output interpretation](#output-interpretation)",
        "- [Public benchmarks](#public-benchmarks)",
        "- [Comparisons](#comparisons)",
        "- [Limitations and safety](#limitations-and-safety)",
        "- [Related upstream agent skills](#related-upstream-agent-skills)",
        "- [Primary sources](#primary-sources)",
        "- [Evidence gaps](#evidence-gaps)",
        "",
        f"- Research key: `{research['researchKey']}`",
        f"- Independent audit: `{research['audit']['verdict']}`",
        f"- Researched: `{research['researchedAt']}`",
        "",
        dossier["researchSummary"],
        "",
        "## Identity",
        "",
        f"- Upstream name: {identity['upstreamName']}",
        f"- Checkpoint/version: {identity['checkpoint']}",
        f"- Immutable revision: {identity['revision']}",
        f"- Parameter scale: {identity['parameterScale']}",
        f"- Architecture/head: {identity['architecture']}",
        f"- License: {identity['license']}",
        f"- Evidence: {', '.join(identity['evidenceUrls'])}",
        "",
        "## Selection",
        "",
        "### Recommended",
        "",
    ]
    for item in dossier["recommendedUseCases"]:
        lines.extend(
            [
                f"- **{item['useCase']}** — {item['why']}",
                f"  Scope: {item['modelScope']}",
                f"  Evidence: {', '.join(item['evidenceUrls'])}",
            ]
        )
    lines.extend(["", "### Conditional", ""])
    for item in dossier["conditionalUseCases"]:
        lines.extend(
            [
                f"- **{item['useCase']}** — {item['conditions']}",
                f"  Scope: {item['modelScope']}",
                f"  Evidence: {', '.join(item['evidenceUrls'])}",
            ]
        )
    lines.extend(["", "### Avoid", ""])
    for item in dossier["avoidUseCases"]:
        evidence = ", ".join(item["evidenceUrls"]) or "documented evidence gap"
        lines.extend(
            [
                f"- **{item['useCase']}** — {item['reason']}",
                f"  Scope: {item['modelScope']}",
                f"  Evidence: {evidence}",
            ]
        )
    lines.extend(["", "## Input preparation", ""])
    for heading, key in (
        ("Semantic inputs", "semanticInputs"),
        ("Accepted formats", "acceptedFormats"),
        ("Preprocessing", "preprocessing"),
        ("Pre-submit validation", "validation"),
        ("Task-specific formatting", "taskSpecificFormatting"),
    ):
        lines.extend(
            [
                f"### {heading}",
                "",
                *research_statement_lines(dossier["inputPreparation"][key]),
                "",
            ]
        )
    lines.extend(["## Output interpretation", ""])
    for heading, key in (
        ("Outputs", "outputs"),
        ("Interpretation", "interpretation"),
        ("Post-inference validation", "validation"),
    ):
        lines.extend(
            [
                f"### {heading}",
                "",
                *research_statement_lines(dossier["outputInterpretation"][key]),
                "",
            ]
        )
    lines.extend(["## Public benchmarks", ""])
    if not dossier["benchmarks"]:
        lines.extend(
            [
                "No checkpoint-matched public benchmark row passed the evidence gate.",
                "",
            ]
        )
    for benchmark in dossier["benchmarks"]:
        lines.extend(
            [
                f"### {benchmark['task']}",
                "",
                f"- Dataset/split: {benchmark['dataset']} / {benchmark['split']}",
                (
                    f"- Metric/value: {benchmark['metric']} / "
                    f"{benchmark['value']} (`{benchmark['direction']}`)"
                ),
                f"- Model scope: {benchmark['modelScope']}",
                f"- Conditions: {benchmark['conditions']}",
                f"- Source: {benchmark['sourceUrl']}",
                f"- Locator: {benchmark['sourceLocator']}",
                *[f"- Caveat: {item}" for item in benchmark["caveats"]],
                "",
            ]
        )
    lines.extend(["## Comparisons", ""])
    if not dossier["comparisons"]:
        lines.extend(["No evidence-safe direct comparison is available.", ""])
    for comparison in dossier["comparisons"]:
        lines.extend(
            [
                (
                    f"### {comparison['alternative']} — "
                    f"`{comparison['verdict']}`"
                ),
                "",
                f"- Task: {comparison['task']}",
                f"- Criteria: {comparison['criteria']}",
                f"- Rationale: {comparison['rationale']}",
                f"- Comparison conditions: {comparison['comparisonConditions']}",
                f"- Evidence: {', '.join(comparison['evidenceUrls'])}",
                "",
            ]
        )
    lines.extend(
        [
            "## Limitations and safety",
            "",
            "### Limitations",
            "",
            *research_statement_lines(dossier["limitations"]),
            "",
            "### Safety",
            "",
            *research_statement_lines(dossier["safety"]),
            "",
            "## Related upstream agent skills",
            "",
        ]
    )
    if research.get("upstreamAgentSkills"):
        for mapping in research["upstreamAgentSkills"]:
            lines.extend(
                [
                    f"### `{mapping['relation']}`",
                    "",
                    mapping["notes"],
                    *[
                        f"- [{skill['name']}]({skill['url']})"
                        for skill in mapping["skills"]
                    ],
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "No exact or related NVIDIA/BioNeMo agent skill is mapped.",
                "",
            ]
        )
    lines.extend(
        [
            "## Primary sources",
            "",
        ]
    )
    for source in dossier["sources"]:
        lines.extend(
            [
                f"### {source['title']}",
                "",
                f"- URL: {source['url']}",
                f"- Publisher: {source['publisher']}",
                f"- Type: `{source['sourceType']}`",
                f"- Primary because: {source['primaryReason']}",
                f"- Scope: {source['modelScope']}",
                *[f"- Supports: {item}" for item in source["supports"]],
                "",
            ]
        )
    lines.extend(
        [
            "## Evidence gaps",
            "",
            *[f"- {item}" for item in dossier["evidenceGaps"]],
            "",
            "## Independent audit",
            "",
            research["audit"]["summary"],
            "",
            *[
                (
                    f"- `{issue['severity']}` {issue['path']}: "
                    f"{issue['issue']} Resolution: {issue['resolution']}"
                )
                for issue in research["audit"]["issues"]
            ],
            "",
        ]
    )
    return render_markdown_lines(lines)


def group_research_markdown(research: dict[str, Any]) -> str:
    dossier = research["dossier"]
    lines = [
        f"# {dossier['group'].replace('-', ' ').title()} model selection",
        "",
        f"- Category: `{dossier['category']}`",
        f"- Group: `{dossier['group']}`",
        f"- Independent audit: `{research['audit']['verdict']}`",
        f"- Researched: `{research['researchedAt']}`",
        "",
        dossier["taskDefinition"],
        "",
        "## Questions to answer before selecting",
        "",
        *[f"- {item}" for item in dossier["selectionQuestions"]],
        "",
        "## Comparability rules",
        "",
        *[f"- {item}" for item in dossier["comparabilityRules"]],
        "",
        "## Conditional routing",
        "",
    ]
    for rule in dossier["decisionRules"]:
        lines.extend(
            [
                f"### Prefer `{rule['prefer']}` when {rule['when']}",
                "",
                f"- Why: {rule['because']}",
                *[f"- Alternative: {item}" for item in rule["alternatives"]],
                f"- Evidence: {', '.join(rule['evidenceUrls'])}",
                "",
            ]
        )
    lines.extend(["## Benchmark taxonomy", ""])
    for benchmark in dossier["benchmarkTaxonomy"]:
        lines.extend(
            [
                f"### {benchmark['task']}",
                "",
                f"- Datasets: {', '.join(benchmark['datasets'])}",
                f"- Metrics: {', '.join(benchmark['metrics'])}",
                *[
                    f"- Compare only when: {item}"
                    for item in benchmark["comparisonConditions"]
                ],
                "",
            ]
        )
    lines.extend(["## Primary sources", ""])
    for source in dossier["sources"]:
        lines.extend(
            [
                f"- [{source['title']}]({source['url']}) — "
                f"{source['publisher']}; supports {', '.join(source['supports'])}",
            ]
        )
    lines.extend(
        [
            "",
            "## Evidence gaps",
            "",
            *[f"- {item}" for item in dossier["evidenceGaps"]],
            "",
            "## Independent audit",
            "",
            research["audit"]["summary"],
            "",
            *[
                (
                    f"- `{issue['severity']}` {issue['path']}: "
                    f"{issue['issue']} Resolution: {issue['resolution']}"
                )
                for issue in research["audit"]["issues"]
            ],
            "",
        ]
    )
    return render_markdown_lines(lines)


def openai_yaml(skill_name: str, display_name: str, slug: str) -> str:
    short = f"Use and evaluate {display_name}"
    if len(short) > 64:
        short = f"Use and evaluate Forge model {slug}"[:64].rstrip()
    if len(short) < 25:
        short = f"{short} on Forge"
    prompt = (
        f"Use ${skill_name} to select, format a request for, run, and "
        f"interpret {display_name} on Forge."
    )
    return "\n".join(
        [
            "interface:",
            f"  display_name: {yaml_quote(display_name)}",
            f"  short_description: {yaml_quote(short)}",
            f"  default_prompt: {yaml_quote(prompt)}",
            "",
        ]
    )


def evaluation_cases(
    skill_name: str,
    skill: dict[str, Any],
    research: dict[str, Any] | None,
) -> dict[str, Any]:
    recommended = (
        research["dossier"]["recommendedUseCases"][0]["useCase"]
        if research and research["dossier"]["recommendedUseCases"]
        else skill["purpose"]
    )
    avoid = (
        research["dossier"]["avoidUseCases"][0]["useCase"]
        if research and research["dossier"]["avoidUseCases"]
        else "a task outside the declared input/output modalities"
    )
    return {
        "schemaVersion": "1.0.0",
        "skill": skill_name,
        "modelSlug": skill["modelSlug"],
        "cases": [
            {
                "id": "exact-model-run",
                "shouldActivate": True,
                "prompt": (
                    f"Use Forge model {skill['modelSlug']} for this task: "
                    f"{recommended}. Show the exact request format and explain the output."
                ),
                "expectedBehavior": [
                    "Loads the exact model skill, not the full catalog.",
                    "Validates the live Forge route before inference.",
                    "Uses the exact request fields and bounds.",
                    "Loads audited research before interpreting model quality or output meaning.",
                ],
            },
            {
                "id": "model-selection",
                "shouldActivate": True,
                "prompt": (
                    f"Should I use {skill['modelSlug']} or another Forge model "
                    f"for {recommended}?"
                ),
                "expectedBehavior": [
                    "Loads the exact research reference and the matching group dossier.",
                    "Makes only task- and protocol-scoped comparisons.",
                    "States insufficient evidence when public protocols are not comparable.",
                ],
            },
            {
                "id": "decline-mismatched-task",
                "shouldActivate": True,
                "prompt": (
                    f"Use {skill['modelSlug']} for {avoid}, even if it is not "
                    "validated for that task."
                ),
                "expectedBehavior": [
                    "Does not invent support or a benchmark.",
                    "Explains the exact limitation or evidence gap.",
                    "Routes to a better task-group candidate when evidence supports one.",
                ],
            },
        ],
    }


def field_line(field: dict[str, Any]) -> str:
    requirement = "required" if field.get("required") else "optional"
    details = [str(field.get("fieldType") or "unknown"), requirement]
    if field.get("minimum") is not None or field.get("maximum") is not None:
        details.append(
            f"bounds {field.get('minimum', '—')}..{field.get('maximum', '—')}"
        )
    if field.get("choices"):
        details.append(
            "choices " + ", ".join(map(str, field["choices"][:20]))
        )
    if field.get("default") is not None:
        details.append(f"default {field['default']!r}")
    return (
        f"- `{field['key']}` ({'; '.join(details)}): "
        f"{field.get('label') or field['key']}"
    )


def evidence_markdown(
    skill: dict[str, Any],
    model: dict[str, Any],
    research: dict[str, Any] | None,
) -> str:
    claims = skill.get("benchmarkClaims") or []
    lines = [
        "# Evidence",
        "",
        f"- Research status: `{skill['publicEvidenceStatus']}`",
        (
            "- Policy: Forge runtime latency/throughput evidence is operational "
            "placement data, not model-quality evidence."
        ),
        "",
    ]
    if research:
        lines.extend(
            [
                "## Deep research",
                "",
                f"- Research key: `{research['researchKey']}`",
                f"- Independent audit: `{research['audit']['verdict']}`",
                (
                    "- Full checkpoint-scoped selection, input/output, benchmark, "
                    "comparison, limitation, and safety evidence: `research.md`."
                ),
                "",
            ]
        )
    if claims:
        lines.extend(["## Reviewed public benchmark claims", ""])
        for claim in claims:
            lines.extend(
                [
                    f"### {claim['sourceTitle']}",
                    "",
                    f"- Primary source: {claim['sourceUrl']}",
                    f"- Checked: {claim['checkedAt']}",
                    f"- Model/checkpoint scope: {claim['modelScope']}",
                    f"- Dataset and split: {claim['dataset']} / {claim['split']}",
                    f"- Metric and value: {claim['metric']} / {claim['value']}",
                    f"- Direction: {claim['direction']}",
                    f"- Provenance: {claim['provenance']}",
                    f"- Conditions: {claim['conditions']}",
                    *[f"- Caveat: {item}" for item in claim.get("caveats") or []],
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "## Public quality evidence",
                "",
                (
                    "No independently reviewed public benchmark claim is attached "
                    "to this exact Forge model/version. Do not invent a result, "
                    "transfer a family result, or imply that operational Forge "
                    "probes establish model quality."
                ),
                "",
            ]
        )
    source_url = str(model.get("source_url") or "").strip()
    lines.extend(["## Sources", ""])
    if source_url:
        lines.append(f"- Exact model source/model card: {source_url}")
    for reference in skill.get("references") or []:
        line = f"- {reference['title']}: {reference['url']} ({reference['kind']})"
        if line not in lines:
            lines.append(line)
    lines.extend(
        [
            "",
            (
                "The complete public Forge model and exact-skill snapshots are "
                "in `forge-model.json` and `forge-skill.json`."
            ),
            "",
        ]
    )
    return render_markdown_lines(lines)


def skill_markdown(
    model: dict[str, Any],
    skill: dict[str, Any],
    *,
    category: str,
    group: str,
    research: dict[str, Any] | None,
) -> str:
    slug = skill["modelSlug"]
    description = normalized_text(
        skill.get("shortDescription"),
        f"Use exact Forge model {slug}.",
    )
    frontmatter_description = yaml_scalar(
        f"Use exact Forge model {slug} for "
        f"{', '.join(skill.get('inputModalities') or ['declared input'])} to "
        f"{', '.join(skill.get('outputModalities') or ['declared output'])}. "
        "Load when selecting, calling, comparing, interpreting, or deploying "
        "this specific version."
    )
    claims = skill.get("benchmarkClaims") or []
    skill_name = portable_skill_name(slug)
    route = (
        f"{skill.get('inferenceMethod', 'POST')} {skill['inferencePath']}"
        if skill.get("inferencePath")
        else "Resolve from the live inference-routes API"
    )
    research_lines: list[str]
    if research:
        dossier = research["dossier"]
        research_lines = [
            f"- Audited research: `{research['audit']['verdict']}`",
            f"- Research key: `{research['researchKey']}`",
            *[
                f"- Recommended: {item['useCase']} — {item['why']}"
                for item in dossier["recommendedUseCases"][:3]
            ],
            *[
                f"- Avoid: {item['useCase']} — {item['reason']}"
                for item in dossier["avoidUseCases"][:3]
            ],
            (
                "- Before selecting against another model, transforming user "
                "data, interpreting outputs, or citing quality, read "
                "`references/research.md`."
            ),
        ]
    else:
        research_lines = [
            "- Audited checkpoint research is not attached.",
            "- Do not make model-quality or comparative claims.",
        ]
    lines = [
        "---",
        f"name: {skill_name}",
        f"description: {frontmatter_description}",
        "---",
        "",
        f"# {skill['displayName']}",
        "",
        f"- Model slug: `{slug}`",
        f"- Family: `{skill['modelFamily']}`",
        f"- Version: `{skill['version']}` (`{skill['versionKey']}`)",
        f"- Hierarchy: `models / {category} / {group}`",
        f"- Stability: `{skill['stability']}`",
        f"- Default eligible: `{str(skill['defaultEligible']).lower()}`",
        f"- License: `{skill.get('license') or 'not-declared'}`",
        f"- Research status: `{skill['publicEvidenceStatus']}`",
        "",
        "## Purpose",
        "",
        skill["purpose"],
        "",
        "## Use this exact model when",
        "",
        *[f"- {item}" for item in skill.get("whenToUse") or []],
        "",
        "## Do not use it when",
        "",
        *[f"- {item}" for item in skill.get("whenNotToUse") or []],
        "",
        "## Exact request contract",
        "",
        *(
            [field_line(field) for field in skill.get("inputFields") or []]
            or ["- Resolve required fields from the live route before use."]
        ),
        "",
        f"Route: `{route}`",
        "",
        "```json",
        json.dumps(skill.get("requestTemplate") or {}, indent=2, sort_keys=True),
        "```",
        "",
        "## Exact output",
        "",
        *[
            f"- `{item}`"
            for item in (
                skill.get("outputFields")
                or skill.get("outputModalities")
                or ["resolve from live route"]
            )
        ],
        "",
        "## Required workflow",
        "",
        *[
            f"{index}. {item}"
            for index, item in enumerate(skill.get("workflow") or [], 1)
        ],
        "",
        "## Evidence",
        "",
        skill["benchmarkEvidenceNote"],
        (
            f"Read `references/evidence.md` for {len(claims)} reviewed "
            "public claim(s) and their exact scope."
            if claims
            else (
                "Read `references/evidence.md` and the linked primary source "
                "before making a model-quality comparison."
            )
        ),
        "",
        "## Audited model guidance",
        "",
        *research_lines,
        "",
        "## Limitations",
        "",
        *[f"- {item}" for item in skill.get("limitations") or []],
        "",
        "## Safety",
        "",
        *[f"- {item}" for item in skill.get("safety") or []],
        "",
        "## Live Forge and Serverless",
        "",
        f"- Model: `{skill['liveContract']['modelUrl']}`",
        f"- Routes: `{skill['liveContract']['inferenceRoutesUrl']}`",
        f"- Regional deployment: `{skill['liveContract']['regionalDeploymentUrl']}`",
        f"- Serverless handoff: `{skill['liveContract']['deployGuideUrl']}`",
        (
            "- Load `$use-nebius` and `$nebius-forge-model-deployment` "
            "for a user-owned endpoint."
        ),
        "",
        "## Progressive references",
        "",
        (
            "- `../research.md` — audited task-group selection and "
            "comparability rules."
        ),
        "- `../research.json` — machine-readable task-group dossier.",
        "- `references/evidence.md` — benchmark/source scope.",
        *(
            [
                "- `references/research.md` — full audited model-use dossier.",
                "- `references/research.json` — machine-readable audited dossier.",
            ]
            if research
            else []
        ),
        "- `references/forge-model.json` — complete public Forge model snapshot.",
        "- `references/forge-skill.json` — complete exact-skill API snapshot.",
        f"- Repository file: {skill['repositoryFileUrl']}",
        "",
    ]
    return render_markdown_lines(lines)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    root = Path(args.output_root).resolve()
    generated_at = args.generated_at or datetime.now(timezone.utc).isoformat()
    models = fetch_all_models(args.api_base)
    skills = fetch_exact_skills(
        args.api_base,
        [str(model["slug"]) for model in models],
        workers=args.workers,
    )
    expected_slugs = {str(model["slug"]) for model in models}
    research_by_slug = load_research_by_slug(
        root,
        expected_slugs,
        allow_missing=args.allow_missing_research,
    )
    expected_groups = {
        (
            slugify(
                str(
                    skills[str(model["slug"])].get("category")
                    or model.get("category")
                    or "uncategorized"
                )
            ),
            group_for(model, skills[str(model["slug"])]),
        )
        for model in models
    }
    research_by_group = load_group_research(
        root,
        expected_groups,
        allow_missing=args.allow_missing_research,
    )

    generated_root = root / "skills" / "models"
    if generated_root.exists():
        shutil.rmtree(generated_root)
    generated_root.mkdir(parents=True)

    entries: list[dict[str, Any]] = []
    hierarchy: dict[str, dict[str, dict[str, list[str]]]] = {}
    research: dict[str, list[str]] = {
        "reviewed": [],
        "source-linked": [],
        "pending-review": [],
    }
    group_entries: dict[tuple[str, str], list[dict[str, Any]]] = {}
    group_catalog: list[dict[str, Any]] = []

    for model in sorted(models, key=lambda item: str(item["slug"])):
        slug = str(model["slug"])
        skill = skills[slug]
        model_research = research_by_slug.get(slug)
        category = slugify(
            str(skill.get("category") or model.get("category") or "uncategorized")
        )
        group = group_for(model, skill)
        family = str(model.get("model_family") or slug)
        declared_path = Path(
            str(
                skill.get("repositoryPath")
                or (
                    f"skills/models/{category}/{group}/"
                    f"{slugify(slug)}/SKILL.md"
                )
            )
        )
        expected_prefix = Path("skills") / "models" / category / group
        if declared_path.name != "SKILL.md" or expected_prefix not in declared_path.parents:
            raise ValueError(f"unsafe portable repository path for {slug}: {declared_path}")
        directory = root / declared_path.parent
        references = directory / "references"
        references.mkdir(parents=True, exist_ok=True)

        markdown = skill_markdown(
            model,
            skill,
            category=category,
            group=group,
            research=model_research,
        )
        skill_path = directory / "SKILL.md"
        skill_path.write_text(markdown, encoding="utf-8")
        write_json(references / "forge-model.json", model)
        write_json(references / "forge-skill.json", skill)
        (references / "evidence.md").write_text(
            evidence_markdown(skill, model, model_research),
            encoding="utf-8",
        )
        if model_research:
            write_json(references / "research.json", model_research)
            (references / "research.md").write_text(
                research_markdown(model_research),
                encoding="utf-8",
            )
        agents = directory / "agents"
        agents.mkdir(parents=True, exist_ok=True)
        (agents / "openai.yaml").write_text(
            openai_yaml(
                portable_skill_name(slug),
                str(skill["displayName"]),
                slug,
            ),
            encoding="utf-8",
        )
        evals = directory / "evals"
        evals.mkdir(parents=True, exist_ok=True)
        write_json(
            evals / "evals.json",
            evaluation_cases(
                portable_skill_name(slug),
                skill,
                model_research,
            ),
        )

        status = str(skill.get("publicEvidenceStatus") or "pending-review")
        if status not in research:
            status = "pending-review"
        research[status].append(slug)
        relative_path = skill_path.relative_to(root).as_posix()
        entry = {
            "slug": slug,
            "skillName": portable_skill_name(slug),
            "displayName": skill["displayName"],
            "description": skill["shortDescription"],
            "path": relative_path,
            "category": category,
            "group": group,
            "modelFamily": family,
            "version": skill["version"],
            "versionKey": skill["versionKey"],
            "inputModalities": skill.get("inputModalities") or [],
            "outputModalities": skill.get("outputModalities") or [],
            "stability": skill["stability"],
            "defaultEligible": skill["defaultEligible"],
            "license": skill.get("license"),
            "researchStatus": status,
            "deepResearchStatus": (
                model_research["audit"]["verdict"]
                if model_research
                else "missing"
            ),
            "researchKey": (
                model_research["researchKey"] if model_research else None
            ),
            "researchDossierPath": (
                f"{declared_path.parent.as_posix()}/references/research.json"
                if model_research
                else None
            ),
            "upstreamAgentSkillCount": (
                len(model_research.get("upstreamAgentSkills") or [])
                if model_research
                else 0
            ),
            "groupResearchPath": (
                f"skills/models/{category}/{group}/research.json"
                if (category, group) in research_by_group
                else None
            ),
            "publicBenchmarkClaimCount": len(skill.get("benchmarkClaims") or []),
            "sourceUrl": model.get("source_url"),
            "forgeModelUrl": skill["liveContract"]["modelUrl"],
            "forgeSkillApiUrl": f"/v1/model-skills/{quote(slug, safe='')}",
            "forgeSkillDownloadUrl": (
                f"/v1/model-skills/{quote(slug, safe='')}/markdown?download=true"
            ),
            "contentSha256": sha256(markdown),
        }
        entries.append(entry)
        group_entries.setdefault((category, group), []).append(entry)
        (
            hierarchy.setdefault(category, {})
            .setdefault(group, {})
            .setdefault(family, [])
            .append(slug)
        )

    for (category, group), items in group_entries.items():
        group_directory = generated_root / category / group
        readme = group_directory / "README.md"
        group_research = research_by_group.get((category, group))
        if group_research:
            write_json(group_directory / "research.json", group_research)
            (group_directory / "research.md").write_text(
                group_research_markdown(group_research),
                encoding="utf-8",
            )
        lines = [
            f"# {group.replace('-', ' ').title()}",
            "",
            f"Category: `{category}` · exact model/version skills: {len(items)}",
            "",
            *(
                [
                    "[Audited model-selection dossier](research.md)",
                    "",
                ]
                if group_research
                else [
                    "Audited model-selection research is not yet attached.",
                    "",
                ]
            ),
            *[
                (
                    f"- [{item['displayName']}]"
                    f"({item['slug']}/SKILL.md) — `{item['versionKey']}` · "
                    f"{item['researchStatus']}"
                )
                for item in sorted(items, key=lambda item: item["displayName"])
            ],
            "",
        ]
        readme.write_text("\n".join(lines), encoding="utf-8")
        group_catalog.append(
            {
                "category": category,
                "group": group,
                "modelCount": len(items),
                "modelSlugs": sorted(item["slug"] for item in items),
                "researchStatus": (
                    group_research["audit"]["verdict"]
                    if group_research
                    else "missing"
                ),
                "researchPath": (
                    f"skills/models/{category}/{group}/research.json"
                    if group_research
                    else None
                ),
                "researchMarkdownPath": (
                    f"skills/models/{category}/{group}/research.md"
                    if group_research
                    else None
                ),
            }
        )

    catalog = {
        "schemaVersion": "1.0.0",
        "generatedAt": generated_at,
        "sourceApi": args.api_base.rstrip("/"),
        "repository": args.repository.rstrip("/"),
        "repositoryRef": args.repository_ref,
        "total": len(entries),
        "models": entries,
    }
    write_json(root / "catalog" / "models.json", catalog)
    write_json(
        root / "catalog" / "hierarchy.json",
        {
            "schemaVersion": "1.0.0",
            "generatedAt": generated_at,
            "total": len(entries),
            "categories": hierarchy,
        },
    )
    write_json(
        root / "catalog" / "research-status.json",
        {
            "schemaVersion": "1.0.0",
            "generatedAt": generated_at,
            "reviewedCount": len(research["reviewed"]),
            "sourceLinkedCount": len(research["source-linked"]),
            "pendingReviewCount": len(research["pending-review"]),
            **research,
        },
    )
    write_json(
        root / "catalog" / "groups.json",
        {
            "schemaVersion": "1.0.0",
            "generatedAt": generated_at,
            "total": len(group_catalog),
            "groups": sorted(
                group_catalog,
                key=lambda item: (item["category"], item["group"]),
            ),
        },
    )
    print(
        json.dumps(
            {
                "models": len(entries),
                "categories": len(hierarchy),
                "groups": len(group_entries),
                "reviewed": len(research["reviewed"]),
                "sourceLinked": len(research["source-linked"]),
                "pendingReview": len(research["pending-review"]),
                "deepResearched": len(research_by_slug),
                "deepResearchedGroups": len(research_by_group),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
