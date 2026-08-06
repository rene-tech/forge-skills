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

- Research key: `huggingface-co-qwen-qwen3-14b-245877f208`
- Independent audit: `revised`
- Researched: `2026-08-06T09:15:17.660678+00:00`

Checkpoint-scoped dossier for the upstream Qwen3-14B model (checkpoint name Qwen3-14B). Primary-source evidence confirms: model identity and architecture parameters (40 layers, GQA heads), tokenizer configuration (Qwen2Tokenizer, special tokens, model_max_length = 131072), two reported context-length figures (native 32,768 tokens vs. extended 131,072 via YaRN per GGUF page), and an Apache-2.0 LICENSE file for the GGUF artifact. Primary sources do not present checkpoint-scoped numeric benchmarks or direct task/protocol comparisons for the exact Forge-served runtime variants; canonical prompt templates and a formalized output-score calibration contract are not present in the inspected upstream artifacts. All factual claims below are explicitly tied to the listed primary-source locators.

## Identity

- Upstream name: Qwen3-14B
- Checkpoint/version: Qwen3-14B
- Immutable revision: d17b97ca036704c156b50686b3f4551e224bbe03
- Parameter scale: 14.8 billion total parameters; 13.2 billion non-embedding parameters
- Architecture/head: Causal/dense transformer; 40 layers; group query attention (GQA) with 40 query heads and 8 key/value heads; causal LM
- License: Apache-2.0 (as stated in the Qwen3-14B-GGUF LICENSE file)
- Evidence: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B/blob/d17b97ca036704c156b50686b3f4551e224bbe03/config.json, https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B-GGUF/blob/main/LICENSE, https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json

## Selection

### Recommended

- **Instruction-following text generation** — Upstream model card and Qwen3-14B-GGUF documentation describe Qwen3-14B as a causal text-generation model designed for instruction-following and related text-generation tasks.
  Scope: Qwen3-14B
  Evidence: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF
- **Agent-style multi-turn interaction and reasoning over text** — Upstream descriptions in the official model card and the Qwen3 series documentation indicate agent-style capabilities and multi-turn reasoning as intended uses for Qwen3-14B.
  Scope: Qwen3-14B
  Evidence: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF

### Conditional

- **Long-context summarization or reasoning using extended context** — Requires using the YaRN extension or equivalent mechanism referenced by the Qwen3-14B-GGUF repository to handle contexts up to 131,072 tokens; otherwise, native context length is 32,768 tokens. Ensure the runtime preserves the upstream tokenizer and context-handling behavior.
  Scope: Qwen3-14B (native 32,768 tokens; extended up to 131,072 tokens via YaRN per GGUF page)
  Evidence: https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json

### Avoid

- **Non-text modalities or expecting a structured numeric/serialized output contract** — Evidence gap: upstream primary sources inspected do not document support for multimodal inputs/outputs or a formal structured numeric output schema for Qwen3-14B.
  Scope: Qwen3-14B
  Evidence: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF

## Input preparation

### Semantic inputs

- The model consumes textual inputs intended for generation and reasoning tasks. Sources: https://huggingface.co/Qwen/Qwen3-14B

### Accepted formats

- Plain text natural-language inputs for causal text generation; no upstream primary artifact documents multimodal input acceptance for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-14B

### Preprocessing

- Tokenizer: Qwen2Tokenizer as specified in the tokenizer_config.json. Sources: https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json
- Tokenizer configuration includes model_max_length = 131072 (tokenizer_config.json). Sources: https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json
- Model native context length is reported as 32,768 tokens and an extended context up to 131,072 tokens is documented via the YaRN extension on the Qwen3-14B-GGUF page (two context-length figures present in upstream artifacts). Sources: https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json
- Special tokens defined in tokenizer_config.json include '<|im_start|>', '<|im_end|>', and '<|object_ref_start|>'; pad and eos tokens are specified in tokenizer_config.json. Sources: https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json

### Pre-submit validation

- Input validation should ensure inputs are encoded with the upstream tokenizer (Qwen2Tokenizer); tokenizer error handling mode is 'replace' per tokenizer_config.json. Sources: https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json
- Validate that context lengths do not exceed the intended native or explicitly extended limits depending on whether YaRN or other extensions are used. Sources: https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json

### Task-specific formatting

- Upstream tokenizer defines conversation/segment special tokens ('<|im_start|>', '<|im_end|>') which can be used to delimit turns; no single canonical prompt template is provided in the inspected upstream artifacts. Sources: https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-14B

## Output interpretation

### Outputs

- Primary upstream artifacts characterize Qwen3-14B as a causal language model producing textual outputs (text generation). No structured output schema is specified. Sources: https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B

### Interpretation

- The upstream artifacts do not specify calibrated confidence scores or numeric reliability metrics as part of the model's default output contract; interpret generated text conservatively and validate downstream as needed. Sources: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF

### Post-inference validation

- Evidence gap: upstream sources inspected do not provide formal post-inference validation or calibration procedures tied to Qwen3-14B; downstream human or automated validation is required for factuality and alignment. Sources: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The inspected upstream primary sources do not provide an exhaustive, single consolidated list of limitations for Qwen3-14B; checkpoint-scoped benchmark numbers and direct protocol-matched comparisons to other checkpoints are not available in the checked artifacts. Sources: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B/blob/d17b97ca036704c156b50686b3f4551e224bbe03/config.json

### Safety

- Evidence gap: explicit upstream safety, privacy, and dual-use constraints for Qwen3-14B are not exhaustively enumerated in the inspected model card or GGUF repository; the GGUF artifact includes an Apache-2.0 LICENSE file but not a detailed safety policy. Sources: https://huggingface.co/Qwen/Qwen3-14B, https://huggingface.co/Qwen/Qwen3-14B-GGUF, https://huggingface.co/Qwen/Qwen3-14B-GGUF/blob/main/LICENSE

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-14B model card

- URL: https://huggingface.co/Qwen/Qwen3-14B
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model page describing the Qwen3-14B checkpoint and intended usage.
- Scope: Qwen3-14B
- Supports: text-generation
- Supports: instruction-following
- Supports: agent-style multi-turn interaction
- Supports: multilingual support

### Qwen3-14B config.json (repo, specific commit)

- URL: https://huggingface.co/Qwen/Qwen3-14B/blob/d17b97ca036704c156b50686b3f4551e224bbe03/config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository config defining architecture and runtime-related keys for the Qwen3-14B checkpoint (commit referenced).
- Scope: Qwen3-14B
- Supports: architecture keys and runtime settings

### Qwen3-14B tokenizer_config.json

- URL: https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Official tokenizer configuration for the Qwen3-14B checkpoint (tokenizer class, special tokens, model_max_length and token-handling flags).
- Scope: Qwen3-14B
- Supports: tokenizer class
- Supports: model_max_length
- Supports: special tokens
- Supports: tokenizer error handling

### Qwen3-14B-GGUF repository page

- URL: https://huggingface.co/Qwen/Qwen3-14B-GGUF
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: GGUF artifact repository for Qwen3-14B; contains statements about parameter counts, layer counts, native and extended context lengths, and available quantization formats.
- Scope: Qwen3-14B (GGUF artifact)
- Supports: parameter counts
- Supports: layer counts
- Supports: native context length (32,768 tokens)
- Supports: extended context via YaRN (131,072 tokens)
- Supports: available quantization formats

### Qwen3-14B-GGUF LICENSE

- URL: https://huggingface.co/Qwen/Qwen3-14B-GGUF/blob/main/LICENSE
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: License file associated with the Qwen3-14B GGUF artifact declaring Apache License, Version 2.0.
- Scope: Qwen3-14B (GGUF artifact)
- Supports: license

## Evidence gaps

- Benchmarks: Checked https://huggingface.co/Qwen/Qwen3-14B (model card) — no checkpoint-scoped benchmark tables, figures, or numeric rows for Qwen3-14B were found on the model card page.
- Benchmarks: Checked https://huggingface.co/Qwen/Qwen3-14B-GGUF (GGUF repo) and https://huggingface.co/Qwen/Qwen3-14B/blob/d17b97ca036704c156b50686b3f4551e224bbe03/config.json — no checkpoint-scoped numeric benchmark tables or protocol-matched evaluation tables were found in these repository artifacts.
- Comparisons: Checked https://huggingface.co/Qwen/Qwen3-14B and https://huggingface.co/Qwen/Qwen3-14B-GGUF — no direct, checkpoint-scoped task-and-protocol-matched comparisons between Qwen3-14B and other named checkpoints were present in the inspected upstream artifacts.
- Serving/runtime wrappers (vLLM variants): Evidence gap: inspected upstream artifacts (https://huggingface.co/Qwen/Qwen3-14B and https://huggingface.co/Qwen/Qwen3-14B-GGUF) do not document runtime-induced behavioral or benchmark differences attributable to specific vLLM versions (e.g., vllm-0.10.2-cuda12.8 or vllm-0.21.0-cuda13). No primary-source locator in the checked artifacts documents such runtime-difference claims.
- Canonical prompts/templates: Checked https://huggingface.co/Qwen/Qwen3-14B and https://huggingface.co/Qwen/Qwen3-14B-GGUF — no single canonical prompt template or exhaustive instruction-format specification for Qwen3-14B was found in the inspected upstream artifacts.
- Output contract and calibration: Checked https://huggingface.co/Qwen/Qwen3-14B and https://huggingface.co/Qwen/Qwen3-14B-GGUF — upstream artifacts do not provide a formalized output schema (shapes/units) or calibrated confidence-score semantics for Qwen3-14B.
- Tokenizer/context-length ambiguity: Checked https://huggingface.co/Qwen/Qwen3-14B/blob/main/tokenizer_config.json (model_max_length = 131072) and https://huggingface.co/Qwen/Qwen3-14B-GGUF (native context length = 32,768 tokens; extended via YaRN to 131,072) — both locators are present and indicate two related but distinct context-length claims (native vs. extended), creating an explicit evidence note rather than a resolved single value.
- Limitations and safety policies: Checked https://huggingface.co/Qwen/Qwen3-14B and https://huggingface.co/Qwen/Qwen3-14B-GGUF (including LICENSE) — no exhaustive upstream safety/privacy/dual-use policy document tied to the checkpoint was found in these inspected artifacts.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
