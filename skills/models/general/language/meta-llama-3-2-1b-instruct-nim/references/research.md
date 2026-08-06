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

- Research key: `build-nvidia-com-meta-llama-3-2-1b-instruct-27b0875952`
- Independent audit: `revised`
- Researched: `2026-07-23T23:09:19.866591+00:00`

Primary upstream and NVIDIA packaging sources identify meta-llama/Llama-3.2-1B-Instruct as an instruction‑tuned, auto‑regressive Transformer family checkpoint in the Llama 3.2 family at ~1B parameters, released under the Llama 3.2 Community License. Hugging Face model page and Meta model-card report benchmark rows for MMLU (bf16, 5-shot), IFEval (bf16), and GSM8K (CoT, 8-shot) tied to the 1B instruct checkpoint; tokenizer artifact files are listed in the Hugging Face dataset/evals listing. NVIDIA Build systemcard and NGC/NIM entries document the NIM packaging, OpenAI-compatible example name and sampling defaults, LoRA support in the NIM packaging, unsupported features (fine-tuning, tool calling) for the packaged NIM, and GPU memory minima/recommendations. Primary sources do not publish an immutable checkpoint SHA/revision for the upstream checkpoint; explicit per-token logprob/logit exposure and an explicit input-truncation (head vs tail) policy are not documented in the checked primary sources (see evidenceGaps).

## Identity

- Upstream name: meta-llama/Llama-3.2-1B-Instruct
- Checkpoint/version: meta-llama/Llama-3.2-1B-Instruct
- Immutable revision: not reported
- Parameter scale: approximately 1 billion parameters
- Architecture/head: Auto-regressive transformer (family-level materials describe an optimized transformer architecture / auto-regressive language model)
- License: Llama 3.2 Community License
- Evidence: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/blob/main/LICENSE.txt

## Selection

### Recommended

- **Instruction-following assistant / chat (question answering, dialogue)** — Checkpoint is described as instruction-tuned and intended for assistant-like chat and instruction-following in the upstream model card and Hugging Face model page.
  Scope: meta-llama/Llama-3.2-1B-Instruct (instruction-tuned 1B)
  Evidence: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- **Summarization and prompt/query rewriting** — Upstream model card and Hugging Face documentation list summarization and prompt rewriting among intended use cases for Llama‑3.2 instruction-tuned models.
  Scope: meta-llama/Llama-3.2-1B-Instruct
  Evidence: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md

### Conditional

- **On-device or constrained-memory deployment using quantized variants (validate accuracy on target tasks)** — Only when using explicitly documented quantized variants (SpinQuant, QLoRA) and after validating accuracy on target tasks because accuracy differs across quantization schemes.
  Scope: Quantized variants of meta-llama/Llama-3.2-1B-Instruct (SpinQuant, QLoRA) as listed in the Hugging Face materials
  Evidence: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals
- **LoRA-based customization via the NVIDIA NIM container (validate outputs after adaptation)** — Only when using the NIM packaging that documents LoRA support; validate outputs after any LoRA adaptation because fine-tuning is not supported in the packaged NIM.
  Scope: NVIDIA NIM packaging of meta-llama/Llama-3.2-1B-Instruct
  Evidence: https://build.nvidia.com/meta/llama-3.2-1b-instruct/systemcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.2-1b-instruct

### Avoid

- **Tasks requiring built-in tool calling when served via the NVIDIA NIM** — NVIDIA Build systemcard explicitly states tool calling is not supported for the 1B NIM packaging.
  Scope: NVIDIA NIM packaging of meta-llama/Llama-3.2-1B-Instruct
  Evidence: https://build.nvidia.com/meta/llama-3.2-1b-instruct/systemcard
- **High-stakes applications requiring highest-accuracy or large-model capabilities without downstream validation** — Meta developer docs indicate lightweight 1B/3B models are not intended to replace larger models for all use cases; use caution and validate for high-stakes tasks.
  Scope: Family-level guidance applied conservatively to meta-llama/Llama-3.2-1B-Instruct
  Evidence: https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama3_2, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- **Applications that violate the Llama 3.2 Community License / Acceptable Use Policy** — License and Acceptable Use constraints govern prohibited or restricted applications; deployments must comply with the license/AUP.
  Scope: meta-llama/Llama-3.2-1B-Instruct (license/AUP applies)
  Evidence: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/blob/main/LICENSE.txt, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

## Input preparation

### Semantic inputs

- Primary documented input type is a single text string or an interactive list-of-messages (roles) format for instruction/chat examples. Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama3_2

### Accepted formats

- NVIDIA Build examples expose an OpenAI-compatible API name 'meta/llama-3.2-1b-instruct' and example sampling parameters in NIM/Forge documentation. Sources: https://build.nvidia.com/meta/llama-3.2-1b-instruct
- Upstream Hugging Face README examples and provided pipelines show use of a list-of-messages format (roles) for instruction/chat and recommend inference with torch.bfloat16 and device_map='auto'. Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals

### Preprocessing

- Hugging Face README examples demonstrate inference examples using torch_dtype=torch.bfloat16 (bf16) and device_map='auto'. Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Tokenizer artifact files (tokenizer.json, tokenizer.model, tokenizer_config.json, special_tokens_map.json) are included in the Hugging Face dataset/evals listing for the 1B instruct checkpoint. Sources: https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals

### Pre-submit validation

- Validate inputs conform to the expected text or messages format and that device/dtype settings match recommended inference settings (e.g., bf16) before submission. Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://build.nvidia.com/meta/llama-3.2-1b-instruct
- When deploying via the NVIDIA NIM, check GPU memory against documented minima and recommended values in the NIM systemcard. Sources: https://build.nvidia.com/meta/llama-3.2-1b-instruct/systemcard

### Task-specific formatting

- Upstream README and Meta developer docs show passing a list of messages with roles such as 'system' and 'user' for instruction/chat generation. Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama3_2
- NVIDIA NIM example configuration documents sampling defaults used in examples (temperature, top_p, max_tokens) for the OpenAI-compatible example name. Sources: https://build.nvidia.com/meta-llama-3.2-1b-instruct, https://build.nvidia.com/meta/llama-3.2-1b-instruct

## Output interpretation

### Outputs

- Served outputs are auto-regressive generated text (token sequence returned as text). Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.2-1b-instruct, https://build.nvidia.com/meta-llama-3.2-1b-instruct

### Interpretation

- Do not interpret returned text as conveying calibrated confidence or token-level probabilities unless explicit per-token logprob/logit exposure is later documented by the serving runtime. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.2-1b-instruct, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct

### Post-inference validation

- Users must perform downstream validation for task-specific acceptance thresholds and calibration because no vendor-prescribed downstream validation/certification procedures were found in the checked primary sources. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

## Public benchmarks

### MMLU (macro-average accuracy, 5-shot)

- Dataset/split: MMLU / 5-shot
- Metric/value: macro-average accuracy / 49.3% (`higher-is-better`)
- Model scope: Llama-3.2-1B-Instruct (bf16, 5-shot) as reported on the Hugging Face model page
- Conditions: Reported as bf16 evaluation and 5-shot prompting on the Hugging Face model page performance table; prompt templates/seeds/harness are not enumerated in that table.
- Source: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Locator: Model page performance table (MMLU bf16 5-shot row)
- Caveat: Hugging Face performance table lists the aggregate 5-shot bf16 number but does not include full evaluation-harness templates, seeds, or scripts in the same table.

### IFEval (instruction-following average accuracy)

- Dataset/split: IFEval / not reported
- Metric/value: average accuracy (prompt/instruction, loose/strict aggregated) / 59.5% (`higher-is-better`)
- Model scope: Llama-3.2-1B-Instruct (bf16) as reported on the Hugging Face model page
- Conditions: Reported on the Hugging Face model page as an IFEval result for the 1B bf16 checkpoint; the exact split/harness location is not enumerated in the performance table.
- Source: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Locator: Model page performance table (IFEval entry)
- Caveat: Hugging Face performance table provides an aggregate IFEval number but does not provide full reproducibility artifacts (templates, seeds, harness) in that same table.

### GSM8K (Chain-of-Thought, exact match)

- Dataset/split: GSM8K / 8-shot
- Metric/value: exact match (em_maj1@1) / 44.4% (`higher-is-better`)
- Model scope: Llama-3.2-1B-Instruct (bf16, CoT, 8-shot) as reported on the Hugging Face model page
- Conditions: Reported as GSM8K CoT 8-shot em_maj1@1 for the 1B bf16 checkpoint on the Hugging Face model page; prompt templates/seeds/harness not enumerated in that table.
- Source: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Locator: Model page performance table (GSM8K CoT 8-shot row)
- Caveat: The performance table documents CoT and 8-shot conditions but does not include full prompt templates or harness code in the same table.

## Comparisons

### allenai-olmo-2-0425-1b-instruct — `insufficient-evidence`

- Task: general instruction-following/chat
- Criteria: No protocol-matched, primary-source numeric comparison (dataset/split/precision/prompting/harness) between meta-llama/Llama-3.2-1B-Instruct and this alternative was found in the checked primary sources.
- Rationale: Checked primary sources report per-checkpoint numbers for Llama 3.2 but do not present head-to-head matched-protocol comparisons against this alternative.
- Comparison conditions: Searched the Hugging Face model page and Meta model-card and the NVIDIA NIM reference for protocol-matched head-to-head numbers; no matched-protocol table found for both exact checkpoints.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct

### allenai-olmo-3-7b-instruct — `insufficient-evidence`

- Task: general instruction-following/chat
- Criteria: Different parameter scales and no direct protocol-matched comparison in checked primary sources.
- Rationale: Primary sources for Llama 3.2 do not contain matched-protocol head-to-head comparisons versus this alternative.
- Comparison conditions: Searched the Meta model-card and NVIDIA NIM reference; no matched-protocol comparisons found.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct

### bigcode-starcoder2-7b — `insufficient-evidence`

- Task: code generation / general language tasks
- Criteria: No protocol-matched, primary-source numeric comparisons for both exact checkpoints were found in the checked primary sources.
- Rationale: Checked primary sources (Meta model-card, NVIDIA NIM reference) lack protocol-matched head-to-head tables comparing the exact checkpoints.
- Comparison conditions: Searched primary model-card and NIM docs for protocol-matched comparisons; none located.
- Evidence: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md

### huggingfacetb-smollm3-3b — `insufficient-evidence`

- Task: general instruction-following/chat
- Criteria: No protocol-matched, primary-source numeric comparison for the exact checkpoints in the checked sources.
- Rationale: Primary sources for Llama 3.2 do not provide matched-protocol head-to-head numbers against this alternative.
- Comparison conditions: Checked Meta model-card and NVIDIA NIM docs; no matched-protocol comparisons present.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct

### meta-llama-3-1-8b-instruct — `insufficient-evidence`

- Task: general instruction-following/chat
- Criteria: Scale differences and missing matched-protocol benchmark rows for both exact checkpoints in checked primary sources.
- Rationale: Llama 3.2 family materials report per-checkpoint numbers but no direct matched-protocol head-to-head comparisons between the exact 1B and 8B instruct checkpoints were found in checked sources.
- Comparison conditions: Searched family model-card and NIM references for head-to-head matched protocols; none located.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct

### meta-llama-3-2-3b-instruct — `insufficient-evidence`

- Task: general instruction-following/chat
- Criteria: Different parameter scales and missing direct protocol-matched comparisons in the checked primary sources.
- Rationale: Family-level entries exist for 3B instruct but no protocol-matched head-to-head comparisons against the exact 1B instruct checkpoint were found in checked sources.
- Comparison conditions: Checked Meta model-card and NVIDIA family catalog entries; no matched-protocol head-to-head tables found.
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.2-1b-instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md

### Other Forge-listed alternatives (aggregated) — `insufficient-evidence`

- Task: general
- Criteria: No protocol-matched, primary-source numeric comparisons for the exact Llama-3.2-1B-Instruct checkpoint versus the other listed alternatives were found in the checked primary sources.
- Rationale: NVIDIA and Meta primary sources assert per-checkpoint performance but do not provide protocol-matched, per-checkpoint head-to-head tables against each Forge alternative in the checked primary sources.
- Comparison conditions: Searched Meta model-card and NVIDIA NIM references for matched-protocol comparisons; none located.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct

## Limitations and safety

### Limitations

- The checked primary sources do not publish an immutable upstream revision identifier (checkpoint SHA or exact checksum) for meta-llama/Llama-3.2-1B-Instruct. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Canonical tokenizer artifact path and explicit tokenization rules (merges/vocabulary ordering) for the exact 1B instruct checkpoint are not specified in the checked upstream model card or Hugging Face model page; the Hugging Face dataset/evals listing does include tokenizer files but an explicit canonical checkpoint tokenizer implementation path and merges/vocab ordering are not documented in the model card. Sources: https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- Some reported benchmark rows (MMLU, IFEval, GSM8K) are published as aggregate numbers in the Hugging Face performance table but the checked primary-source fragments do not include full evaluation-harness artifacts (exact prompt templates, seeds, harness scripts) required for exact reproducibility. Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals
- Explicit documentation that the NIM serving interface returns per-token log probabilities or token-level logits was not found in the checked primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.2-1b-instruct, https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct
- Exact truncation/cropping policy (head vs tail truncation) for inputs exceeding the maximum sequence length is not documented in the checked primary sources. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

### Safety

- The Llama-3.2-1B-Instruct checkpoint was safety-fine-tuned using the same mitigations reported for the Llama 3 family (family-level safety fine-tuning statements). Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- License and Acceptable Use Policy prohibit certain uses (deployments must comply with the Llama 3.2 Community License and any stated AUP restrictions). Sources: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/blob/main/LICENSE.txt, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Evidence gap: No upstream-prescribed, model-specific privacy/PHI handling procedure was found in the checked primary sources; organizational privacy/PHI procedures remain required. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model page: meta-llama/Llama-3.2-1B-Instruct

- URL: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Publisher: Hugging Face (meta-llama organization)
- Type: `repository`
- Primary because: Canonical upstream model page and performance table for the meta-llama/Llama-3.2-1B-Instruct checkpoint; contains benchmark rows, README guidance, and links to model artifacts.
- Scope: meta-llama/Llama-3.2-1B-Instruct
- Supports: Checkpoint identity and parameter scale
- Supports: Benchmark rows: MMLU (bf16 5-shot 49.3%), IFEval (bf16 59.5%), GSM8K (CoT 8-shot 44.4%)
- Supports: Recommended inference dtype examples (bf16) and pipeline snippets

### Meta Llama-3.2 model card (GitHub): MODEL_CARD.md

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- Publisher: meta-llama (GitHub repository)
- Type: `model-card`
- Primary because: Official Llama 3.2 family model card containing family- and checkpoint-level descriptions, architecture statement, and intended uses.
- Scope: Llama 3.2 family and checkpoint-level entries
- Supports: Architecture: optimized auto-regressive transformer (family-level)
- Supports: Instruction-tuning and alignment approach (SFT and RLHF family-level statements)
- Supports: Intended use cases and release metadata

### Hugging Face dataset / evals page: Llama-3.2-1B-Instruct-evals

- URL: https://huggingface.co/datasets/meta-llama/Llama-3.2-1B-Instruct-evals
- Publisher: Hugging Face (meta-llama datasets)
- Type: `repository`
- Primary because: Dataset/evals listing associated with the checkpoint; contains tokenizer artifact file names and some evaluation metadata.
- Scope: Llama-3.2-1B-Instruct evals/artifacts
- Supports: Tokenizer artifact filenames (tokenizer.json, tokenizer.model, tokenizer_config.json, special_tokens_map.json)
- Supports: Evaluation dataset references tied to the checkpoint

### NVIDIA NIM reference: meta-llama-3_2-1b-instruct

- URL: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-1b-instruct
- Publisher: NVIDIA API documentation
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM API reference documenting the packaged NIM for the meta-llama Llama-3.2-1B-Instruct offering and related packaging/benchmark notes.
- Scope: NIM packaging for meta-llama-3_2-1b-instruct
- Supports: Identification of the NIM packaging and readiness statements
- Supports: Operational/packaging notes referenced for the NIM

### NVIDIA NGC container listing: llama-3.2-1b-instruct (nim/meta container)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.2-1b-instruct
- Publisher: NVIDIA NGC (nim/meta container listing)
- Type: `official-documentation`
- Primary because: Official NGC/NIM container listing describing the NIM container packaging for Llama-3.2-1B-Instruct.
- Scope: NIM container for Llama-3.2-1B-Instruct
- Supports: Identification of the NIM container packaging
- Supports: Statements about readiness for commercial use and packaged model identity

### Build.nvidia.com model page for meta/llama-3.2-1b-instruct (NIM example/entry)

- URL: https://build.nvidia.com/meta-llama-3.2-1b-instruct
- Publisher: NVIDIA Build (Forge)
- Type: `official-documentation`
- Primary because: Forge/NIM example page demonstrating the OpenAI-compatible API name and sampling defaults for the NIM.
- Scope: NIM example/entry for meta/llama-3.2-1b-instruct
- Supports: OpenAI-compatible example API name 'meta/llama-3.2-1b-instruct'
- Supports: Example sampling defaults (temperature, top_p, max_tokens) used in NIM examples

### Build.nvidia.com systemcard for meta/llama-3.2-1b-instruct

- URL: https://build.nvidia.com/meta-llama-3.2-1b-instruct/systemcard
- Publisher: NVIDIA Build (Forge)
- Type: `official-documentation`
- Primary because: NVIDIA Build systemcard documenting serving constraints, LoRA support, unsupported features, and GPU memory minima/recommended values for the NIM packaging.
- Scope: NIM systemcard for meta/llama-3.2-1b-instruct
- Supports: LoRA customization support and note that fine-tuning and tool calling are not supported in the packaged NIM
- Supports: Minimum and recommended GPU memory values for bf16 and operational guidance

### Meta developer docs: Llama3_2 model-cards and prompt formats

- URL: https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama3_2
- Publisher: Meta (developer documentation)
- Type: `official-documentation`
- Primary because: Official Meta developer documentation describing Llama 3.2 family prompt formats, role tokens, quantized-model guidance, and family-level responsible-use notes.
- Scope: Llama 3.2 family guidance
- Supports: Prompt format tokens and role conventions (system/user/assistant/ipython)
- Supports: Family-level notes that lightweight 1B/3B models do not support built-in tools and guidance on quantized-model usage

### Hugging Face LICENSE file for meta-llama/Llama-3.2-1B-Instruct

- URL: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/blob/main/LICENSE.txt
- Publisher: Hugging Face / Meta distribution
- Type: `official-documentation`
- Primary because: Canonical license text distributed alongside the checkpoint on the upstream model page.
- Scope: Llama 3.2 Community License for the 1B instruct checkpoint
- Supports: License name and key license provisions (Llama 3.2 Community License text and attribution/compliance notes)

### NVIDIA NIM support matrix (hardware/requirements)

- URL: https://docs.nvidia.com/nim/large-language-models/1.1.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA NIM support matrix documenting supported hardware microarchitectures relevant to NIM-packaged models.
- Scope: NIM hardware support and related requirements
- Supports: Supported hardware microarchitectures relevant to running NIM-packaged Llama 3.2 models

### Cited official first-party source

- URL: https://build.nvidia.com/meta/llama-3.2-1b-instruct
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: meta-llama-3-2-1b-instruct
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://build.nvidia.com/meta/llama-3.2-1b-instruct/systemcard
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: meta-llama-3-2-1b-instruct
- Supports: Exact independently audited claim citation

## Evidence gaps

- Immutable upstream checkpoint SHA/checksum or exact release-tag for meta-llama/Llama-3.2-1B-Instruct is not published in the checked primary sources (no SHA/checksum located on the Hugging Face model page, GitHub model-card, or NIM references).
- Exact canonical tokenizer implementation path and full tokenization rules (merges/vocab ordering and explicit canonical tokenizer release tied to the 1B instruct checkpoint) are not specified in the upstream model-card or model page; Hugging Face dataset listing provides tokenizer files but a canonical tokenizer artifact path and merges/vocab ordering tied explicitly to the checkpoint are not documented.
- Full evaluation-harness artifacts (exact prompt templates, seeds, harness scripts) required to exactly reproduce the Hugging Face performance-table benchmark rows (MMLU, IFEval, GSM8K) are not included in the checked primary-source performance tables.
- Explicit documentation that the NIM serving interface returns per-token log probabilities or token-level logits is not present in the checked primary sources; absence of documentation constitutes an evidence gap for token-level logprob exposure.
- Exact truncation/cropping policy (head vs tail truncation) for inputs longer than the documented maximum sequence length is not specified in the checked primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://developer.nvidia.com/blog/llama-3-2-full-stack-optimizations-unlock-high-performance-on-nvidia-gpus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/discussions/20 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama3_2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama3_2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://build.nvidia.com/meta/llama-3.2-1b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/meta/llama-3.2-1b-instruct/systemcard: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
