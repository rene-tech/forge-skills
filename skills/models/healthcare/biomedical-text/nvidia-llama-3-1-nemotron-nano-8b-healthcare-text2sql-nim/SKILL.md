---
name: use-forge-nvidia-llama-3-1-nemotron-nano-8b-healthcare-cad98c48
description: Use exact Forge model nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim for text, schema to sql, text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Llama 3.1 Nemotron Nano 8B Healthcare Text2SQL

- Model slug: `nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim`
- Family: `nvidia-healthcare-text2sql`
- Version: `1.15.1` (`nim-1-15-1-candidate`)
- Hierarchy: `models / healthcare / biomedical-text`
- Stability: `testing`
- Default eligible: `true`
- License: `NVIDIA AI Product/NIM; NVIDIA Open Model; Llama 3.3 Community License`
- Research status: `source-linked`

## Purpose

NVIDIA's Llama 3.1 Nemotron Nano 8B Healthcare Text2SQL NIM translates natural-language healthcare analytics questions plus DDL into SQL.

## Use this exact model when

- Use this exact `nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim` version when the task supplies text, schema and needs sql, text.
- NVIDIA's Llama 3.1 Nemotron Nano 8B Healthcare Text2SQL NIM translates natural-language healthcare analytics questions plus DDL into SQL.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'schema'] → ['sql', 'text'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Based on DDL statements, instructions, and the current date, generate a SQL query in sqlite to answer the question.\nIf the question cannot be answered using the available tables and columns in the DDL, return only: None.\nToday is 2026-05-25 00:00:00\nDDL statements:\nDROP TABLE IF EXISTS diagnosis;\nCREATE TABLE diagnosis (\n  diagnosisid INT NOT NULL PRIMARY KEY,\n  patientunitstayid INT NOT NULL,\n  diagnosisname VARCHAR(200) NOT NULL,\n  diagnosistime TIMESTAMP NOT NULL,\n  icd9code VARCHAR(100)\n);\nInstructions:\n- Use only the provided schema.\n- Return only the SQL query.\n- Do not provide medical advice or patient-specific interpretation.\nquestion: How many distinct patients have at least one diagnosis recorded?'): DDL, instructions, and question
- `temperature` (number; optional; bounds 0..2; default 0): Temperature
- `top_p` (number; optional; bounds 0..1; default 1): Top P
- `max_tokens` (number; optional; bounds 1..1024; default 256): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "detailed thinking off. Generate SQL only for the supplied schema. Do not provide medical advice or clinical interpretation.",
      "role": "system"
    },
    {
      "content": "{{prompt}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `sql`
- `text`

## Required workflow

1. Load this skill and pin model slug `nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim` with version key `nim-1-15-1-candidate`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim`
- Routes: `/v1/models/nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-text/nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql-nim/SKILL.md
