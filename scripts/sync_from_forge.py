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
    return "\n".join(lines)


def skill_markdown(
    model: dict[str, Any],
    skill: dict[str, Any],
    *,
    category: str,
    group: str,
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
        "- Load `$use-nebius` for direct Nebius operations.",
        "",
        "## Progressive references",
        "",
        "- `references/evidence.md` — benchmark/source scope.",
        "- `references/forge-model.json` — complete public Forge model snapshot.",
        "- `references/forge-skill.json` — complete exact-skill API snapshot.",
        f"- Repository file: {skill['repositoryFileUrl']}",
        "",
    ]
    return "\n".join(lines)


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

    for model in sorted(models, key=lambda item: str(item["slug"])):
        slug = str(model["slug"])
        skill = skills[slug]
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
        )
        skill_path = directory / "SKILL.md"
        skill_path.write_text(markdown, encoding="utf-8")
        write_json(references / "forge-model.json", model)
        write_json(references / "forge-skill.json", skill)
        (references / "evidence.md").write_text(
            evidence_markdown(skill, model),
            encoding="utf-8",
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
        readme = generated_root / category / group / "README.md"
        lines = [
            f"# {group.replace('-', ' ').title()}",
            "",
            f"Category: `{category}` · exact model/version skills: {len(items)}",
            "",
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
    print(
        json.dumps(
            {
                "models": len(entries),
                "categories": len(hierarchy),
                "groups": len(group_entries),
                "reviewed": len(research["reviewed"]),
                "sourceLinked": len(research["source-linked"]),
                "pendingReview": len(research["pending-review"]),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
