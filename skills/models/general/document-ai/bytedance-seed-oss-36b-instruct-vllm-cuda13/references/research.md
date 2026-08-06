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

- Research key: `huggingface-co-bytedance-seed-seed-oss-36b-instruct-e3a0d537dd`
- Independent audit: `revised`
- Researched: `2026-08-06T08:50:44.591996+00:00`

Seed-OSS-36B-Instruct is the instruction‑tuned 36B checkpoint in the ByteDance Seed-OSS family. Checkpoint-scoped repository files inspected on the Hugging Face model page and HF repo blobs report a SeedOssForCausalLM causal decoder architecture with num_hidden_layers=64, hidden_size=5120, num_attention_heads=80, num_key_value_heads=8, head_dim=128, intermediate_size=27648, vocab_size=155136, torch_dtype="bfloat16", max_position_embeddings=524288, hidden_act="silu", rope_scaling.rope_type="default" and rope_theta=10000000.0 (from the repo config.json). The repo includes a chat_template.jinja that defines special tokens and a thinking_budget placeholder, and a generation_config.json (specific blob inspected) that sets bos_token_id=0, pad_token_id=1, eos_token_id=2 with default temperature=1.1 and top_p=0.95. The Hugging Face model page contains a benchmark table listing multiple dataset scores for this exact instruct checkpoint. There is a documented conflict between the checkpoint config.json (hidden_act="silu") and the README blob that describes SwiGLU activation; this conflict is recorded as an evidence gap. Multiple operational semantics required for deployment (detailed preprocessing sequence, enforcement behavior for inputs > max_position_embeddings, tokenizer artifact path/recipe, and quantization/precision validation) are not documented in the checkpoint-scoped files inspected and are recorded as evidence gaps with exact file URLs checked.

## Identity

- Upstream name: Seed-OSS-36B-Instruct
- Checkpoint/version: Seed-OSS-36B-Instruct
- Immutable revision: ca038a544ccc5deed9dae9dd4215763a453728c5
- Parameter scale: 36B
- Architecture/head: SeedOssForCausalLM (decoder-only causal Transformer, checkpoint-scoped config.json model_type "seed_oss")
- License: not reported
- Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blame/ca038a544ccc5deed9dae9dd4215763a453728c5/README.md, https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

## Selection

### Recommended

- **Instruction‑following and chat-style generation (instruct/checkpoint canonical formatting)** — The HF model page identifies this checkpoint as the Instruct variant and the repository includes a chat_template.jinja that defines canonical chat tokens and thinking_budget mapping, indicating repository intent and formatting for instruction/chat usage.
  Scope: Seed-OSS-36B-Instruct (checkpoint blobs inspected)
  Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/chat_template.jinja
- **Long-context tasks that require large context windows (use checkpoint defaults with downstream validation)** — The checkpoint config.json reports max_position_embeddings=524288 and repository/model-card materials and release README describe long-context design goals for the Seed-OSS family; the config.json value supports using the checkpoint for very long contexts subject to downstream validation of enforcement semantics.
  Scope: Seed-OSS-36B-Instruct (checkpoint config.json inspected)
  Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json

### Conditional

- **Reproducing evaluation results using checkpoint defaults** — Use the checkpoint-scoped generation_config.json defaults when reproducing reported generation behavior; confirm any evaluation uses these defaults and document deviations.
  Scope: Seed-OSS-36B-Instruct (specific generation_config.json blob inspected)
  Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/5f4e324c9eda5e01d05eda9f328aadcac39309b4/generation_config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- **Deployments using precision-modifying runtimes or quantization (4-bit/8-bit) or alternative attention implementations** — Validate per-deployment numeric fidelity, attention semantics, and downstream task performance after any quantization or runtime change; the checkpoint-scoped files inspected do not provide per-precision validation or quantization guidance.
  Scope: Seed-OSS-36B-Instruct (checkpoint); runtime/quantization wrappers are external and require separate validation
  Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

### Avoid

- **Clinical, medical, or PHI-sensitive applications without explicit upstream clinical validation or PHI-handling guidance** — Evidence gap: the checkpoint-scoped model card and HF repo README/MODEL_CARD blobs inspected do not provide explicit clinical validation, PHI handling policies, or deployment guidance for medical use; do not assume clinical safety or PHI suitability from upstream checkpoint files alone.
  Scope: Seed-OSS-36B-Instruct (checkpoint-scoped files inspected)
  Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blame/ca038a544ccc5deed9dae9dd4215763a453728c5/README.md

## Input preparation

### Semantic inputs

- Natural-language plain-text prompts and instruction/chat-style messages per the model card and README are the intended semantic inputs for this instruct checkpoint. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md

### Accepted formats

- Plain text prompts consumed as token sequences by the checkpoint; special chat tokens and placeholders are defined in the repository chat_template.jinja. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/chat_template.jinja

### Preprocessing

- Evidence gap: the checkpoint-scoped repository files inspected do not provide a detailed, ordered input-preprocessing recipe (normalization, lowercasing, byte-level rules, or exact tokenization call sequence). Config.json and the model page were inspected but do not document an exact step-by-step tokenization/normalization pipeline. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct

### Pre-submit validation

- Evidence gap: config.json declares max_position_embeddings=524288 but the checkpoint-scoped files inspected do not document enforcement semantics (truncate vs error vs sliding window) for inputs exceeding that length; downstream validation is required for inputs > 524,288 tokens. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct

### Task-specific formatting

- The repository provides chat_template.jinja defining canonical chat tokens (<seed:bos>, <seed:eos>, <seed:pad>, <seed:tool_call>, </seed:tool_call>, <seed:think>, </seed:think>) and a thinking_budget placeholder; use this template for reproducible instruction/chat formatting following repository examples. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/chat_template.jinja

## Output interpretation

### Outputs

- The checkpoint emits causal text-token sequences; generation defaults and special token ids (bos_token_id=0, pad_token_id=1, eos_token_id=2) and sampling defaults (temperature=1.1, top_p=0.95) are present in the inspected generation_config.json blob. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/5f4e324c9eda5e01d05eda9f328aadcac39309b4/generation_config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct

### Interpretation

- Evidence gap: the checkpoint-scoped files inspected do not provide an upstream canonical calibration method to map generated token sequences to calibrated probabilities, decision thresholds, or application-level labels; downstream systems should implement and validate calibration. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/refs%2Fpr%2F9/MODEL_CARD.md

### Post-inference validation

- Evidence gap: the checkpoint-scoped repository files inspected do not include post-inference sanity-check procedures (e.g., hallucination filters or canonical calibration steps); implement task-specific validation and safety checks in downstream pipelines. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

## Public benchmarks

### Korean benchmark reporting (KORBench)

- Dataset/split: KORBench / not reported
- Metric/value: score / 74.8 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (checkpoint-scoped benchmark table on HF model page)
- Conditions: As listed in the Hugging Face model page benchmark table; protocol details not expanded in checkpoint blobs inspected.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: The model page lists the benchmark score but the inspected checkpoint blobs do not include an evaluation recipe in the repository files checked.

### HLE reporting

- Dataset/split: HLE / not reported
- Metric/value: score / 13.9 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (checkpoint-scoped benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: No checkpoint-scoped evaluation recipe found in the repository files inspected to reproduce this metric.

### LiveCodeBench reporting

- Dataset/split: LiveCodeBench v6 / 02/2025-05/2025
- Metric/value: score / 66.8 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark entry listed on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: No checkpoint-scoped evaluation recipe present in repository blobs inspected.

### IFEval reporting

- Dataset/split: IFEval / not reported
- Metric/value: score / 86.3 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: Repository files inspected do not include a reproducible evaluation script or exact split metadata for this entry.

### TAU1 reporting (Retail)

- Dataset/split: TAU1-Retail / not reported
- Metric/value: score / 63 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: No checkpoint-scoped evaluation recipe found in repository blobs inspected.

### TAU1 reporting (Airline)

- Dataset/split: TAU1-Airline / not reported
- Metric/value: score / 49 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: Repository blobs inspected do not contain an evaluation recipe to reproduce this entry.

### SWE‑Bench Verified (OpenHands)

- Dataset/split: SWE-Bench Verified (OpenHands) / not reported
- Metric/value: score / 41.8 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: No checkpoint-scoped evaluation script or split metadata found in the inspected repository files.

### MMMLU reporting

- Dataset/split: MMMLU / not reported
- Metric/value: score / 84.3 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: No checkpoint-scoped evaluation recipe included in the repository blobs inspected.

### RULER (128K) reporting

- Dataset/split: RULER (128K) / not reported
- Metric/value: score / 94.5 (`higher-is-better`)
- Model scope: Seed-OSS-36B-Instruct (benchmark table on HF model page)
- Conditions: As listed on the model page benchmark table.
- Source: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Locator: benchmark table on the Hugging Face model page
- Caveat: No checkpoint-scoped evaluation recipe or exact protocol details found in the inspected repository files.

## Comparisons

### Seed-OSS-36B-Base — `insufficient-evidence`

- Task: instruction-following / benchmark reporting
- Criteria: No protocol-matched, checkpoint-scoped side-by-side table comparing Seed-OSS-36B-Instruct and Seed-OSS-36B-Base under identical evaluation settings was found in the inspected HF checkpoint blobs or the ByteDance-Seed GitHub README.
- Rationale: The HF model page and family README describe family variants and report benchmark tables for the instruct checkpoint, but a matched-protocol paired table for instruct vs base at checkpoint scope was not present in the inspected repository files.
- Comparison conditions: Require a primary-source paired-protocol table or reproducible recipe for both checkpoints to prefer one over the other.
- Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

### insufficient-evidence — `insufficient-evidence`

- Task: external-model benchmark parity checks
- Criteria: No protocol-matched checkpoint-scoped comparisons with external checkpoints were located in the inspected HF checkpoint repository or family README; primary evidence for both sides under the same protocol is required.
- Rationale: Benchmarks for the instruct checkpoint appear on the HF model page, but comparable, protocol-matched entries for external models were not present in the checkpoint-scoped files inspected.
- Comparison conditions: Obtain reproducible evaluation recipes and matched protocols for both sides before making a selection.
- Evidence: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

## Limitations and safety

### Limitations

- Evidence gap: the checkpoint-scoped HF model card and README blobs inspected do not enumerate detailed failure modes, known hallucination patterns, or domain-specific limitations for Seed-OSS-36B-Instruct; downstream users must empirically evaluate failure modes for target tasks. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blame/ca038a544ccc5deed9dae9dd4215763a453728c5/README.md
- There is a documented configuration mismatch: the checkpoint config.json sets hidden_act="silu" while the checkpoint README blob describes SwiGLU activation; the repository files inspected do not provide a reconciliation note for this conflict. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md
- Evidence gap: an explicit tokenizer artifact path or detailed tokenizer recipe (tokenizer.json blob) was not found among the checkpoint-scoped files inspected; config.json reports vocab_size but a checkpoint-scoped tokenizer file and exact tokenization steps are not documented in the blobs checked. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct

### Safety

- Evidence gap: no explicit upstream checkpoint-scoped medical/clinical/PHI guidance, safety policy, or privacy-preserving deployment instructions for Seed-OSS-36B-Instruct are present in the HF model page or README blobs inspected; do not assume clinical suitability without external validation and institutional review. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blame/ca038a544ccc5deed9dae9dd4215763a453728c5/README.md
- Evidence gap: the checkpoint-scoped files inspected do not document quantization, precision tradeoffs, or per-precision safety validation procedures; any deployment using quantized runtimes requires separate validation and safety review. Sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct, https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Seed-OSS-36B-Instruct (Hugging Face model page)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Official Hugging Face model page for the exact Seed-OSS-36B-Instruct checkpoint; contains the checkpoint-scoped model card and links to repository blobs and the benchmark table used in this dossier.
- Scope: Seed-OSS-36B-Instruct
- Supports: Checkpoint identity and high-level model-card content; benchmark table entries for the instruct checkpoint; links to checkpoint-scoped repository blobs.

### Seed-OSS-36B-Instruct config.json (HF repo, main blob)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json
- Publisher: huggingface.co
- Type: `repository`
- Primary because: Checkpoint-scoped config.json inside the HF repository; authoritative for numeric architecture fields and config entries inspected for this dossier.
- Scope: Seed-OSS-36B-Instruct
- Supports: num_hidden_layers, hidden_size, num_attention_heads, num_key_value_heads, head_dim, intermediate_size, vocab_size, max_position_embeddings, hidden_act, rope_scaling entries, rope_theta, torch_dtype, transformers_version

### Seed-OSS-36B-Instruct generation_config.json (HF repo, specific blob)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/5f4e324c9eda5e01d05eda9f328aadcac39309b4/generation_config.json
- Publisher: huggingface.co
- Type: `repository`
- Primary because: Checkpoint-scoped generation_config.json blob inspected for generation defaults and special token ids.
- Scope: Seed-OSS-36B-Instruct
- Supports: bos_token_id, pad_token_id, eos_token_id, default temperature and top_p sampling parameters, transformers_version recorded in generation_config.json

### Seed-OSS-36B-Instruct chat_template.jinja (HF repo, main blob)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/chat_template.jinja
- Publisher: huggingface.co
- Type: `repository`
- Primary because: Checkpoint-scoped chat template providing canonical prompt tokens, thinking_budget placeholder, and chat formatting used by repository examples.
- Scope: Seed-OSS-36B-Instruct
- Supports: Definitions of <seed:bos>, <seed:eos>, <seed:pad>, <seed:tool_call>, </seed:tool_call>, <seed:think>, </seed:think>, and thinking_budget placeholder

### Seed-OSS-36B-Instruct README (HF repo blob, blame locator)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blame/ca038a544ccc5deed9dae9dd4215763a453728c5/README.md
- Publisher: huggingface.co
- Type: `repository`
- Primary because: Checkpoint README blob at the inspected revision/blame locator referenced in the draft; documents release notes and relation of instruct variant to base variants at that revision.
- Scope: Seed-OSS-36B-Instruct (specific blob/revision)
- Supports: Release statements linking Seed-OSS-36B-Instruct to family releases; repository-level descriptive text inspected for this dossier

### Seed-OSS-36B-Instruct README (HF repo blob, alternative blob)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md
- Publisher: huggingface.co
- Type: `repository`
- Primary because: Checkpoint README blob inspected which contains architecture descriptions (RoPE, GQA, RMSNorm, SwiGLU) used to compare against config.json entries for conflicts.
- Scope: Seed-OSS-36B-Instruct
- Supports: Readme-level architecture description that references RoPE, GQA, RMSNorm, and SwiGLU (not reconciled with config.json)

### ByteDance-Seed seed-oss GitHub README (official family-level README)

- URL: https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md
- Publisher: ByteDance-Seed
- Type: `repository`
- Primary because: Official ByteDance-Seed family-level README maintained by the model authors; provides family-level release context and design goals referenced by the HF model page.
- Scope: bytedance-seed-oss-36b-instruct (family-level)
- Supports: Family-level release context, design goals (long-context, reasoning), and references to family releases inspected for context in this dossier

### Seed-OSS-36B-Instruct MODEL_CARD.md (HF repo blob referenced by the model page)

- URL: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/refs%2Fpr%2F9/MODEL_CARD.md
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: MODEL_CARD.md blob referenced by the HF model page; inspected as part of checkpoint-scoped documentation and used where MODEL_CARD content was required.
- Scope: Seed-OSS-36B-Instruct
- Supports: Checkpoint-scoped model-card content as presented in the repository blob referenced on the model page

## Evidence gaps

- Evidence gap: the checkpoint-scoped repository files inspected do not include a detailed, ordered input preprocessing/tokenization recipe (normalization sequence, lowercasing, byte-level rules, or exact tokenization call sequence). Files inspected: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct and https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json
- Evidence gap: the checkpoint-scoped repository files inspected (config.json and README blobs) declare max_position_embeddings=524288 but do not document enforcement semantics for inputs longer than that limit (truncate vs error vs sliding window). Files inspected: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json and https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- Evidence gap: the repository blobs inspected include conflicting activation descriptions (README blob describes SwiGLU while the checkpoint config.json sets hidden_act="silu"); no reconciliation note was found in the inspected blobs. Files inspected: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md and https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json
- Evidence gap: an explicit tokenizer artifact path or detailed tokenizer.json recipe was not located among the checkpoint-scoped blobs inspected; config.json reports vocab_size but a tokenizer.json blob and exact tokenization steps were not documented in the files checked. Files inspected: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct and https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/main/config.json
- Evidence gap: checkpoint-scoped files inspected do not provide per-precision quantization validation or guidance for 4-bit/8-bit inference; deployments using quantized runtimes require separate validation. Files inspected: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct and https://github.com/ByteDance-Seed/seed-oss/blob/master/README.md

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 39 deterministic draft defect(s) were supplied to the audit.

- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Base/discussions/2/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/discussions/26/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/5f4e324c9eda5e01d05eda9f328aadcac39309b4/generation_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openrouter.ai/bytedance/seed-oss-36b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct/blob/4de17dbeae770cd9f5e49ab8875e5dcb19a80424/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hf.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
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
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openrouter.ai/bytedance/seed-oss-36b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
