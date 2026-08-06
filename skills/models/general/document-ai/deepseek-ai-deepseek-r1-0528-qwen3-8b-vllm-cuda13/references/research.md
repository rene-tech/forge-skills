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

- Research key: `huggingface-co-deepseek-ai-deepseek-r1-0528-qwen3-8b-4600e20454`
- Independent audit: `revised`
- Researched: `2026-08-06T11:31:37.632192+00:00`

DeepSeek-R1-0528-Qwen3-8B is an upstream Hugging Face checkpoint named DeepSeek-R1-0528-Qwen3-8B with architecture string recorded as Qwen3ForCausalLM in the canonical config.json. The canonical config.json (Hugging Face blob) lists model_type "qwen3" and max_position_embeddings = 131072. The canonical tokenizer_config.json (Hugging Face blob) documents tokenizer settings including add_bos_token = false, add_eos_token = false, explicit BOS/EOS/PAD token contents, and model_max_length = 131072. The canonical LICENSE file (Hugging Face blob) contains the MIT license text. The Hugging Face model card for the exact checkpoint contains a benchmark table that lists multiple numeric results (e.g., LiveCodeBench, AIME 2024/2025, MMLU variants); those benchmark rows are recorded on the model card but the model card does not provide protocol details such as dataset split, seeds, or full evaluation scripts within the inspected primary files. Where the canonical files are silent about parameter-count, immutable revision identifier, prompt templates, runtime toggles, or safety/data provenance, those items are recorded as evidence gaps with the exact primary URLs inspected.

## Identity

- Upstream name: DeepSeek-R1-0528-Qwen3-8B
- Checkpoint/version: DeepSeek-R1-0528-Qwen3-8B
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Qwen3ForCausalLM
- License: MIT
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/LICENSE

## Selection

### Recommended

- **Long-context text reasoning and long-context-aware tasks** — The canonical config.json and tokenizer_config.json on the model's Hugging Face repository indicate support for very large context windows: max_position_embeddings = 131072 (config.json) and model_max_length = 131072 (tokenizer_config.json).
  Scope: DeepSeek-R1-0528-Qwen3-8B
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json

### Conditional

- **Enable_thinking / chain-of-thought style runtimes or explicit chat templates** — Evidence gap: canonical repository documentation and files for this exact checkpoint do not enumerate an enable_thinking parameter, chain-of-thought runtime toggle, or canonical chat/prompt templates. Any use depending on such runtime-specific toggles or distilled behavioral guarantees requires downstream validation, explicit prompt templates, and evaluation scripts not present in the inspected primary sources (see the inspected model card and repository files).
  Scope: DeepSeek-R1-0528-Qwen3-8B
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### Avoid

- **Multimodal inputs (image input)** — Evidence gap: canonical primary sources for this exact checkpoint do not document image or other multimodal input support; tokenizer and config files indicate a text tokenizer and tokenizer settings only (no image encoders or multimodal adapters listed in the canonical files).
  Scope: DeepSeek-R1-0528-Qwen3-8B
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json

## Input preparation

### Semantic inputs

- Evidence gap: canonical primary sources for this checkpoint do not enumerate semantic input categories beyond textual inputs; no canonical multimodal/image input semantics are specified in the inspected files. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### Accepted formats

- Evidence gap: canonical upstream accepted input formats (file types, markup, or structured input schemas) are not enumerated in the primary repository files examined (model card and repository blobs were inspected). Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### Preprocessing

- Tokenizer/config-based preprocessing: tokenizer settings declared in the canonical tokenizer_config.json include add_bos_token = false, add_eos_token = false; explicit BOS token content = "<｜begin▁of▁sentence｜>", EOS token content = "<｜end▁of▁sentence｜>", PAD token content = "<｜end▁of▁sentence｜>", and model_max_length = 131072. The canonical config.json also lists max_position_embeddings = 131072. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json

### Pre-submit validation

- Evidence gap: canonical upstream input-validation rules (bounds checks, ambiguous-case handling, or explicit invalid-input behavior) are not provided in the inspected primary repository files. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json

### Task-specific formatting

- Evidence gap: canonical prompt templates, chat-format specifications, or required paired-input order for specific tasks are not present in the canonical repository files inspected for this checkpoint. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

## Output interpretation

### Outputs

- Evidence gap: the inspected primary files do not enumerate a structured response envelope, score units, or non-textual outputs for this checkpoint; outputs should be treated as free-form text unless downstream wrappers provide additional structure. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json

### Interpretation

- Evidence gap: no canonical guidance on interpreting numeric outputs, calibrating probabilities, or aggregating scores was found in the inspected primary repository files. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### Post-inference validation

- Evidence gap: no canonical post-inference validation harnesses or evaluation scripts were present in the inspected primary files for this checkpoint; downstream validation is required to verify quality for specific tasks. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

## Public benchmarks

### LiveCodeBench

- Dataset/split: LiveCodeBench / not reported
- Metric/value: Pass@1 / 73.3% (`higher-is-better`)
- Model scope: DeepSeek-R1-0528-Qwen3-8B
- Conditions: As listed in the benchmark table on the Hugging Face model card; the model card lists the numeric value but does not provide per-row protocol details (splits, seeds, or evaluation scripts) within the inspected primary files.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Locator: benchmark table on the model card
- Caveat: No protocol-level details (dataset split, seed, or evaluation script) present in the inspected primary files for this benchmark row.

### AIME 2024

- Dataset/split: AIME 2024 / not reported
- Metric/value: Pass@1 / 91.4% (`higher-is-better`)
- Model scope: DeepSeek-R1-0528-Qwen3-8B
- Conditions: As listed in the benchmark table on the Hugging Face model card; protocol details not provided in the inspected primary files.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Locator: benchmark table on the model card
- Caveat: No protocol-level details (dataset split, seed, or evaluation script) present in the inspected primary files for this benchmark row.

### AIME 2025

- Dataset/split: AIME 2025 / not reported
- Metric/value: Pass@1 / 87.5% (`higher-is-better`)
- Model scope: DeepSeek-R1-0528-Qwen3-8B
- Conditions: As listed in the benchmark table on the Hugging Face model card; protocol details not provided in the inspected primary files.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Locator: benchmark table on the model card
- Caveat: No protocol-level details (dataset split, seed, or evaluation script) present in the inspected primary files for this benchmark row.

### GPQA-Diamond

- Dataset/split: GPQA-Diamond / not reported
- Metric/value: Pass@1 / 81.0% (`higher-is-better`)
- Model scope: DeepSeek-R1-0528-Qwen3-8B
- Conditions: As listed in the benchmark table on the Hugging Face model card; protocol details not provided in the inspected primary files.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Locator: benchmark table on the model card
- Caveat: No protocol-level details (dataset split, seed, or evaluation script) present in the inspected primary files for this benchmark row.

### MMLU-Redux

- Dataset/split: MMLU-Redux / not reported
- Metric/value: EM / 93.4% (`higher-is-better`)
- Model scope: DeepSeek-R1-0528-Qwen3-8B
- Conditions: As listed in the benchmark table on the Hugging Face model card; protocol details not provided in the inspected primary files.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Locator: benchmark table on the model card
- Caveat: No protocol-level details (dataset split, seed, or evaluation script) present in the inspected primary files for this benchmark row.

## Comparisons

### allenai-olmo-2-1124-7b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: unspecified / protocol-matched benchmarking
- Criteria: Head-to-head benchmark under identical protocol
- Rationale: Evidence gap: canonical primary sources for DeepSeek-R1-0528-Qwen3-8B provide benchmark rows on the model card, but protocol-matched primary evidence for both this checkpoint and the alternative (identical dataset/split/metric/seed and evaluation script) was not identified within the inspected primary files; therefore a direct head-to-head comparison under matched protocol cannot be derived from the inspected primary sources.
- Comparison conditions: Evidence gap: missing protocol-matched dataset/split/metric locators and evaluation scripts in the inspected primary sources for the alternative and/or this checkpoint.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### bytedance-seed-oss-36b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: unspecified / protocol-matched benchmarking
- Criteria: Head-to-head benchmark under identical protocol
- Rationale: Evidence gap: canonical primary sources for DeepSeek-R1-0528-Qwen3-8B provide benchmark rows on the model card, but protocol-matched primary evidence for both this checkpoint and the alternative (identical dataset/split/metric/seed and evaluation script) was not identified within the inspected primary files; therefore a direct head-to-head comparison under matched protocol cannot be derived from the inspected primary sources.
- Comparison conditions: Evidence gap: missing protocol-matched dataset/split/metric locators and evaluation scripts in the inspected primary sources for the alternative and/or this checkpoint.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### deepseek-ai-deepseek-r1-distill-qwen-14b — `insufficient-evidence`

- Task: unspecified / protocol-matched benchmarking
- Criteria: Head-to-head benchmark under identical protocol
- Rationale: Evidence gap: canonical primary sources for DeepSeek-R1-0528-Qwen3-8B provide benchmark rows on the model card, but protocol-matched primary evidence for both this checkpoint and the alternative (identical dataset/split/metric/seed and evaluation script) was not identified within the inspected primary files; therefore a direct head-to-head comparison under matched protocol cannot be derived from the inspected primary sources.
- Comparison conditions: Evidence gap: missing protocol-matched dataset/split/metric locators and evaluation scripts in the inspected primary sources for the alternative and/or this checkpoint.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### qwen-qwen3-8b — `insufficient-evidence`

- Task: unspecified / protocol-matched benchmarking
- Criteria: Head-to-head benchmark under identical protocol
- Rationale: Evidence gap: canonical primary sources for DeepSeek-R1-0528-Qwen3-8B provide benchmark rows on the model card, but protocol-matched primary evidence for both this checkpoint and the alternative (identical dataset/split/metric/seed and evaluation script) was not identified within the inspected primary files; therefore a direct head-to-head comparison under matched protocol cannot be derived from the inspected primary sources.
- Comparison conditions: Evidence gap: missing protocol-matched dataset/split/metric locators and evaluation scripts in the inspected primary sources for the alternative and/or this checkpoint.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

## Limitations and safety

### Limitations

- Evidence gap: the inspected canonical model card and repository files do not include per-benchmark protocol-level artifacts (dataset splits, random seeds, or evaluation scripts) for the numeric benchmark rows listed on the model card; the benchmark table entries on the model card lack the full protocol disclosure needed for exact reproducibility. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Evidence gap: the canonical repository files inspected (config.json and tokenizer_config.json) do not include a published parameter-count field or an immutable revision identifier for this checkpoint; parameter scale and an immutable revision are therefore recorded as not reported in the inspected primary files. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json
- Evidence gap: the canonical repository files inspected do not provide a documented reconciliation of base-model lineage versus this checkpoint's LICENSE (no explicit multi-license or lineage reconciliation file was found in the inspected primary files). Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/LICENSE, https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

### Safety

- Evidence gap: canonical safety, privacy, and data-handling requirements (including training-data provenance, red-team results, and usage restrictions) are not enumerated in the primary repository files inspected for this checkpoint. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### DeepSeek-R1-0528-Qwen3-8B

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
- Publisher: DeepSeek
- Type: `model-card`
- Primary because: Canonical upstream Hugging Face model card page for the exact checkpoint; hosts the model card benchmark table and links to repository blobs.
- Scope: DeepSeek-R1-0528-Qwen3-8B
- Supports: hosting of the canonical checkpoint and model-card benchmark table
- Supports: high-level model metadata and links to repository files

### DeepSeek-R1-0528-Qwen3-8B config.json

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json
- Publisher: DeepSeek
- Type: `repository`
- Primary because: Canonical upstream configuration file listing architecture string, model_type, and numeric architecture details including max_position_embeddings.
- Scope: DeepSeek-R1-0528-Qwen3-8B
- Supports: architecture (Qwen3ForCausalLM)
- Supports: model_type (qwen3)
- Supports: max_position_embeddings = 131072
- Supports: numerical architecture fields (hidden_size, num_hidden_layers, num_attention_heads, etc.)

### DeepSeek-R1-0528-Qwen3-8B tokenizer_config.json

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json
- Publisher: DeepSeek
- Type: `repository`
- Primary because: Canonical tokenizer configuration file indicating tokenizer settings, BOS/EOS/PAD token contents, add_bos_token/add_eos_token flags, and model_max_length.
- Scope: DeepSeek-R1-0528-Qwen3-8B
- Supports: tokenizer settings (add_bos_token = false, add_eos_token = false)
- Supports: explicit BOS/EOS/PAD token contents
- Supports: tokenizer-declared model_max_length = 131072

### DeepSeek-R1-0528-Qwen3-8B LICENSE

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/LICENSE
- Publisher: DeepSeek
- Type: `repository`
- Primary because: Canonical LICENSE file for the exact checkpoint repository containing the MIT license text.
- Scope: DeepSeek-R1-0528-Qwen3-8B
- Supports: license statement (MIT)

## Evidence gaps

- I checked https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B and its benchmark table (model card 'benchmark table'); the table lists numeric rows but the inspected primary files do not include per-row protocol artifacts (dataset splits, seeds, or evaluation scripts) required for exact reproducibility.
- I checked https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json and did not find a published parameter_count field or an immutable revision identifier; parameter-scale and revision are therefore recorded as not reported.
- I checked https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/tokenizer_config.json and https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/config.json for any declarations of multimodal/image input support or image encoder adapters and found none; no canonical multimodal input support is documented in the inspected primary files.
- I checked https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B and https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/blob/main/LICENSE for any explicit reconciliation of base-model lineage versus this checkpoint's LICENSE and found no such reconciliation document in the inspected primary files.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 94 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12]: $.sources[12]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12]: $.sources[12]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].sourceType: $.sources[12].sourceType: 'model-discussion' is not in ['paper', 'model-card', 'repository', 'official-documentation', 'technical-report'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13]: $.sources[13]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13]: $.sources[13]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14]: $.sources[14]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14]: $.sources[14]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15]: $.sources[15]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15]: $.sources[15]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses unapproved repository owner 'samuelchristlie' for this exact model scope: $.sources[3] uses unapproved repository owner 'samuelchristlie' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary host ollama.com: $.sources[5] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/discussions/5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'bentoml' for this exact model scope: $.sources[14] uses unapproved repository owner 'bentoml' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/discussions/11 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ollama.com/sam860/deepseek-r1-0528-qwen3:8b-Q4_K_M Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/discussions/11 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/discussions/11 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ibm-granite/granite-4.1-8b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/microsoft/phi-4-mini-instruct/deploy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
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
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B/discussions/11 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].split must say 'not reported' or name the split: $.benchmarks[0].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].split must say 'not reported' or name the split: $.benchmarks[1].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].split must say 'not reported' or name the split: $.benchmarks[3].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].split must say 'not reported' or name the split: $.benchmarks[4].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].split must say 'not reported' or name the split: $.benchmarks[5].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].split must say 'not reported' or name the split: $.benchmarks[6].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].split must say 'not reported' or name the split: $.benchmarks[7].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].split must say 'not reported' or name the split: $.benchmarks[8].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].split must say 'not reported' or name the split: $.benchmarks[9].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].split must say 'not reported' or name the split: $.benchmarks[10].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
