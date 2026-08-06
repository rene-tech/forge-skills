# Audited model research

## Contents

- [Identity](#identity)
- [Selection](#selection)
- [Input preparation](#input-preparation)
- [Output interpretation](#output-interpretation)
- [Public benchmarks](#public-benchmarks)
- [Comparisons](#comparisons)
- [Limitations and safety](#limitations-and-safety)
- [Related upstream agent skills](#related-upstream-agent-skills)
- [Primary sources](#primary-sources)
- [Evidence gaps](#evidence-gaps)

- Research key: `build-nvidia-com-microsoft-phi-4-mini-instruct-deploy-81bff52c7d`
- Independent audit: `revised`
- Researched: `2026-07-23T21:05:07.042006+00:00`

This dossier documents the Forge-served identifier microsoft-phi-4-mini-instruct nim-1-12-0 by referencing NVIDIA packaging and canonical upstream publications present in the inspected evidence set. Primary NVIDIA sources (NGC catalog entry and NVIDIA Build deploy page) identify a Phi‑4‑Mini‑Instruct NIM container and a container version noted as 1.12.0 in the inspected materials; the NVIDIA NIM API reference enumerates supported API endpoints (tokenize/detokenize, generate, generative_scoring, chat/completions/responses) and lists extended context claims. The canonical Phi‑4 technical report (arXiv and Microsoft Research PDF) contains family-level architecture, safety/RAI discussion, and benchmark tables for the Phi‑4 family (including RAI benchmark rows for 8K and 16K context lengths). Where the inspected primary sources do not provide checkpoint-scoped facts for the exact microsoft-phi-4-mini-instruct nim-1-12-0 artifact (for example: explicit parameter scale for the mini variant, an upstream-model LICENSE artifact for this exact checkpoint, numeric special-token IDs, or an exact per-container JSON HTTP payload schema for nim-1-12-0), this dossier records explicit evidence gaps naming the exact primary URLs that were inspected.

## Identity

- Upstream name: Phi-4-Mini-Instruct
- Checkpoint/version: microsoft-phi-4-mini-instruct nim-1-12-0
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://build.nvidia.com/microsoft/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct

## Selection

### Recommended

- **Instruction-following and general multilingual chat/dialog** — NVIDIA NGC catalog describes the Phi‑4‑Mini‑Instruct container as an instruction-tuned model suitable for dialogue and instruction-following use; the NVIDIA Build deploy page identifies the corresponding NIM deploy artifact.
  Scope: microsoft-phi-4-mini-instruct nim-1-12-0
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://build.nvidia.com/microsoft/phi-4-mini-instruct
- **Reasoning, mathematics, and code-generation research / developer experimentation** — NVIDIA NGC catalog and the Phi‑4 technical report (arXiv / Microsoft Research PDF) present Phi‑4 family strengths and intended capability areas emphasizing reasoning, math, and code-generation; these are described at family level in the technical report and are represented in the NGC container description for the mini-instruct packaging.
  Scope: Phi-4 family (upstream) and microsoft-phi-4-mini-instruct nim-1-12-0 when the NIM container is used as an upstream checkpoint wrapper
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf

### Conditional

- **Long-context instruction tasks (engineering/research workloads) relying on 128K context** — NIM/container metadata states extended 128K context support at the catalog/API level; however, the exact runtime VRAM/memory tradeoffs, per-deployment configuration requirements, and whether the microsoft-phi-4-mini-instruct nim-1-12-0 container enables the full 128K context for all target hardware are not specified in the inspected sources and must be validated in the target runtime.
  Scope: microsoft-phi-4-mini-instruct nim-1-12-0 (NIM container / NGC catalog context claim)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct
- **Use of token-level scoring or log-probability-based reranking via NIM generative scoring** — NIM API reference documents a generative_scoring endpoint that returns log-probability scores (requires a specific vLLM version per the API reference); verify that the microsoft-phi-4-mini-instruct container exposes and enables that endpoint in the deployed/containerized configuration before relying on log-probability outputs.
  Scope: NIM API features applicable to microsoft-phi-4-mini-instruct nim-1-12-0
  Evidence: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html

### Avoid

- **High-stakes clinical decision making or handling protected health information without expert governance** — The Phi‑4 technical report documents safety/RAI concerns and recommends governance and post-training safety alignment; the inspected primary sources do not provide clinical-use endorsement or PHI‑handling operational guidance for the specific NIM-wrapped checkpoint.
  Scope: microsoft-phi-4-mini-instruct nim-1-12-0
  Evidence: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf

## Input preparation

### Semantic inputs

- Primary accepted input modality is natural-language text prompts for instruction-following and chat-style interactions; NIM API reference and NGC catalog list text-based endpoints and chat/completion APIs. Sources: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct

### Accepted formats

- NIM API reference and NGC catalog present inputs as plain text strings and expose chat/completions endpoints; the inspected findings do not include a canonical per-container JSON-HTTP payload schema for microsoft-phi-4-mini-instruct nim-1-12-0. Sources: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct

### Preprocessing

- The NVIDIA NIM API reference documents tokenize and detokenize endpoints and a low-level generate endpoint; the inspected findings do not include container-scoped pre-tokenization numeric mappings for special tokens. Sources: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html

### Pre-submit validation

- The inspected primary sources do not provide exhaustive input-validation rules (bounds, disallowed characters, canonical normalization) for the microsoft-phi-4-mini-instruct checkpoint; downstream validation per deployment is recommended. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct

### Task-specific formatting

- The inspected findings include NIM chat/completions endpoints for multi-turn chat; the provided evidence set does not include a repository tokenizer_config.json or explicit chat_template artifact for the mini-instruct checkpoint in the findings, therefore any canonical chat-template must be validated against upstream tokenizer files not present in these findings. Sources: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct

## Output interpretation

### Outputs

- Primary output type documented in the inspected NIM API reference is natural-language text via chat/completions/responses endpoints; the API also documents tokenization and scoring endpoints that return token IDs or log-probability scores under certain vLLM versions. Sources: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html

### Interpretation

- Outputs should be interpreted as natural-language responses subject to the typical LLM limitations described in the Phi‑4 technical report; family-level safety/RAI analysis is present in the arXiv/Microsoft report and should inform deployment-specific calibration and evaluation. Sources: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf

### Post-inference validation

- The inspected primary sources do not prescribe an exact post-inference calibration protocol for the microsoft-phi-4-mini-instruct container; adopt benchmark-based validation and downstream task-specific checks prior to production use. Sources: https://arxiv.org/html/2412.08905v1, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct

## Public benchmarks

### Responsible AI (RAI) suite scores (family-level)

- Dataset/split: RAI benchmark (PhiBench/internal RAI benchmarks as reported in technical report) / not reported
- Metric/value: Recall / 100.0% (8K context, Phi-4 family) (`higher-is-better`)
- Model scope: Phi-4 family (upstream)
- Conditions: Family-level benchmark table entry in the Phi-4 technical report; reported for 8K context. The inspected findings do not tie this numeric row to the microsoft-phi-4-mini-instruct nim-1-12-0 NIM container.
- Source: https://arxiv.org/html/2412.08905v1
- Locator: RAI benchmark table (8K context row) in arXiv HTML
- Caveat: Result is reported at Phi‑4 family level in the technical report and is not explicitly attributed to the NIM-wrapped nim-1-12-0 checkpoint in the inspected findings.

### Responsible AI (RAI) suite scores (family-level)

- Dataset/split: RAI benchmark (PhiBench/internal RAI benchmarks as reported in technical report) / not reported
- Metric/value: RAG / 58.1% (8K context, Phi-4 family) (`higher-is-better`)
- Model scope: Phi-4 family (upstream)
- Conditions: Family-level benchmark table entry in the Phi-4 technical report; reported for 8K context. The inspected findings do not tie this numeric row to the microsoft-phi-4-mini-instruct nim-1-12-0 NIM container.
- Source: https://arxiv.org/html/2412.08905v1
- Locator: RAI benchmark table (8K context row) in arXiv HTML
- Caveat: Result is reported at Phi‑4 family level in the technical report and is not explicitly attributed to the NIM-wrapped nim-1-12-0 checkpoint in the inspected findings.

### Responsible AI (RAI) suite scores (family-level)

- Dataset/split: RAI benchmark (PhiBench/internal RAI benchmarks as reported in technical report) / not reported
- Metric/value: Recall / 99.0% (16K context, Phi-4 family) (`higher-is-better`)
- Model scope: Phi-4 family (upstream)
- Conditions: Family-level benchmark table entry in the Phi-4 technical report; reported for 16K context. The inspected findings do not tie this numeric row to the microsoft-phi-4-mini-instruct nim-1-12-0 NIM container.
- Source: https://arxiv.org/html/2412.08905v1
- Locator: RAI benchmark table (16K context row) in arXiv HTML
- Caveat: Result is reported at Phi‑4 family level in the technical report and is not explicitly attributed to the NIM-wrapped nim-1-12-0 checkpoint in the inspected findings.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Benchmark numeric claims for the exact nim-1-12-0 NIM-wrapped checkpoint are not verifiable from the inspected primary sources at the exact table/cell level; family-level Phi‑4 benchmark tables appear in the technical report but do not explicitly map rows to the NIM container tag. Sources: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct
- Evidence gap: The inspected findings do not provide explicit numeric mappings for tokenizer special-token IDs for the mini-instruct checkpoint; do not assume numeric token IDs without direct verification against upstream tokenizer artifacts. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct
- The technical report and NIM catalog document extended context claims but do not enumerate per-deployment VRAM/runtime tradeoffs for achieving 128K context in all configurations; validate memory and performance in target deployment environments. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct

### Safety

- The Phi‑4 technical report documents safety alignment processes, red-team testing, and RAI evaluation and recommends governance and evaluation across deployment contexts; apply governance and RAI processes for high-risk domains. Sources: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf
- The NIM container and API materials reference runtime and licensing guidance at the container level; reconcile container/runtime license or terms with upstream model artifact licensing prior to deployment (evidence of container-level license/terms present in catalog/API materials). Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://build.nvidia.com/microsoft/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NGC: Phi-4 mini-instruct container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct
- Publisher: NVIDIA NGC
- Type: `repository`
- Primary because: NGC catalog entry documents the Phi‑4‑Mini‑Instruct container, its container version, and descriptive metadata used to identify the NIM-wrapped checkpoint.
- Scope: microsoft-phi-4-mini-instruct nim-1-12-0
- Supports: deployment
- Supports: context-length
- Supports: description
- Supports: versioning

### Build.NVIDIA: Microsoft Phi-4 Mini Instruct deploy

- URL: https://build.nvidia.com/microsoft/phi-4-mini-instruct
- Publisher: NVIDIA Build
- Type: `official-documentation`
- Primary because: NVIDIA Build deploy page is the Forge-declared deploy starting source and documents the NIM-wrapped deploy identity used by Forge.
- Scope: microsoft-phi-4-mini-instruct nim-1-12-0
- Supports: deployment
- Supports: versioning

### NVIDIA NIM API reference: microsoft-phi-4-mini-instruct

- URL: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NIM API reference lists endpoints (tokenize, detokenize, generate, generative_scoring, chat/completions, responses) and describes API-level guidance that is applicable to NIM-wrapped checkpoints.
- Scope: microsoft-phi-4-mini-instruct nim-1-12-0 (NIM API reference)
- Supports: api-reference
- Supports: input-output-types
- Supports: context-length
- Supports: runtime-guidance

### NVIDIA NIM API reference (general LLM API reference)

- URL: https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: General NIM LLM API reference describing tokenize/detokenize and generation endpoints used across NIM containers; referenced to corroborate API capabilities listed for the microsoft-phi-4-mini-instruct reference page.
- Scope: NIM API (general)
- Supports: api-reference
- Supports: tokenize-detokenize
- Supports: generate-endpoints

### Phi-4 technical report (arXiv abstract)

- URL: https://arxiv.org/abs/2412.08905
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv listing for the Phi‑4 technical report; used to identify the canonical preprint and access formal bibliographic metadata.
- Scope: Phi-4 family (upstream)
- Supports: paper-metadata

### Phi-4 technical report (arXiv HTML)

- URL: https://arxiv.org/html/2412.08905v1
- Publisher: arXiv
- Type: `paper`
- Primary because: HTML rendering of the Phi‑4 preprint containing benchmark tables and safety/RAI discussion; used to extract family-level benchmark rows and safety statements.
- Scope: Phi-4 family (upstream)
- Supports: architecture
- Supports: safety
- Supports: benchmarks

### Phi-4 technical report (Microsoft Research PDF)

- URL: https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf
- Publisher: Microsoft Research
- Type: `technical-report`
- Primary because: Canonical Microsoft Research technical report PDF for the Phi‑4 family; contains architecture notes, training context, and safety/RAI benchmarking discussion referenced in this dossier.
- Scope: Phi-4 family (upstream)
- Supports: architecture
- Supports: training
- Supports: safety
- Supports: benchmarks

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/microsoft/phi-4-mini-instruct/deploy
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: microsoft-phi-4-mini-instruct
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Parameter-scale evidence gap: The inspected primary sources did not report a parameter count for the Phi‑4 Mini Instruct checkpoint. Checked sources: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct.
- Upstream-license evidence gap: The inspected evidence set did not include an explicit upstream model LICENSE file or canonical upstream license statement for the exact microsoft-phi-4-mini-instruct checkpoint in the provided findings; checked: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://build.nvidia.com/microsoft/phi-4-mini-instruct, https://arxiv.org/abs/2412.08905.
- Tokenizer token-ID evidence gap: The inspected findings do not provide explicit numeric token ID integers for any specialized tokens used by Phi‑4 or Phi‑4‑Mini‑Instruct; files that would usually contain numeric mappings (tokenizer artifacts) were not available in the provided findings. Checked: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct.
- I/O schema evidence gap: The NVIDIA NIM API reference enumerates endpoints (tokenize, detokenize, chat/completions, generate, generative_scoring) but the inspected findings do not include a canonical, container-scoped JSON-HTTP payload schema or an exact per-container request/response schema for microsoft-phi-4-mini-instruct nim-1-12-0. Checked: https://docs.api.nvidia.com/nim/reference/microsoft-phi-4-mini-instruct, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://build.nvidia.com/microsoft/phi-4-mini-instruct.
- Benchmark-specific evidence gap for nim-1-12-0: No primary-source table/cell was found that explicitly reports numeric benchmark rows for the exact nim-1-12-0 NIM-wrapped checkpoint in the inspected findings. Family-level benchmarks exist in the technical report (arXiv/Microsoft PDF) but do not explicitly tie numeric rows to the named NIM container tag. Checked: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct.
- Comparisons evidence gap: No primary-source head-to-head benchmark was found that compares microsoft-phi-4-mini-instruct nim-1-12-0 to other Forge candidate slugs under an identical protocol in the inspected findings. Checked: https://arxiv.org/html/2412.08905v1, https://microsoft.com/en-us/research/wp-content/uploads/2024/12/P4TechReport.pdf, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-4-mini-instruct, https://build.nvidia.com/microsoft/phi-4-mini-instruct.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 27 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[11]: $.sources[11]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/microsoft/phi-4-mini-instruct/deploy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary URL https: $.sources[9] uses forbidden secondary URL https://skywork.ai/blog/models/microsoft-phi-4-mini-instruct-free-chat-online-skywork-ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Phi-4-mini-instruct/commits/refs%2Fpr%2F43/.gitattributes Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Phi-4-mini-instruct/commits/refs%2Fpr%2F43/.gitattributes Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ibm-granite/granite-4.1-8b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/mistralai/Devstral-Small-2507 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openbmb/MiniCPM4-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openbmb/MiniCPM5-1B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-0.6B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-1.7B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/microsoft/phi-4-mini-instruct/deploy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
