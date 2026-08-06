---
name: use-forge-nvidia-gliner-pii-nim
description: Use exact Forge model nvidia-gliner-pii-nim for text to entities. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA GLiNER PII

- Model slug: `nvidia-gliner-pii-nim`
- Family: `nvidia-gliner-pii`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / multimodal-and-specialized`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-open-model-license; apache-2.0`
- Research status: `source-linked`

## Purpose

NVIDIA GLiNER PII NIM for extracting personally identifiable information spans from text; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave5.

## Use this exact model when

- Use this exact `nvidia-gliner-pii-nim` version when the task supplies text and needs entities.
- NVIDIA GLiNER PII NIM for extracting personally identifiable information spans from text; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave5.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['entities'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (textarea; optional; default 'John Doe can be reached at john.doe@example.com or +1 555 0100 in New York.'): Input text
- `threshold` (number; optional; bounds 0..1; default 0.5): Threshold
- `chunk_length` (number; optional; bounds 1..2048; default 384): Chunk length
- `overlap` (number; optional; bounds 0..512; default 128): Overlap

Route: `POST /v1/chat/completions`

```json
{
  "chunk_length": "{{chunk_length}}",
  "flat_ner": false,
  "messages": [
    {
      "content": "{{messages}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "overlap": "{{overlap}}",
  "threshold": "{{threshold}}"
}
```

## Exact output

- `entities`

## Required workflow

1. Load this skill and pin model slug `nvidia-gliner-pii-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-gliner-pii-59057755e4`
- Recommended: Automated detection and redaction of Personally Identifiable Information (PII) and Protected Health Information (PHI) in structured and unstructured UTF-8 text for enterprise/regulatory workflows — NVIDIA model-card and NIM documentation state the model is intended to detect and classify PII/PHI and to emit span-level annotations with confidence scores across 55+ categories, making it suitable as a component in redaction workflows.
- Recommended: Integration as a PII detection/masking guardrail in NeMo Guardrails-based pipelines for input/output monitoring and masking — NeMo Guardrails documentation references the model identifier and documents request/response fields and default thresholding behavior, supporting integration as a Guardrails component.
- Avoid: Using the model as a generative language model for text synthesis or instruction-following — Primary-source facts describe GLiNER PII as a non-generative span-tagging model that performs span-level entity annotation rather than text generation.
- Avoid: Non-text input modalities (audio, image) without upstream conversion to UTF-8 text — All primary-source facts indicate the checkpoint accepts UTF-8 text strings as input; no primary evidence indicates the checkpoint accepts raw audio or images.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 2048.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-gliner-pii-nim`
- Routes: `/v1/models/nvidia-gliner-pii-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-gliner-pii-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-gliner-pii-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/multimodal-and-specialized/nvidia-gliner-pii-nim/SKILL.md
