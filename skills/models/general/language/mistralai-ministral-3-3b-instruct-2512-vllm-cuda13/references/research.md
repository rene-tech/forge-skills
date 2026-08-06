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

- Research key: `huggingface-co-mistralai-ministral-3-3b-instruct-2512-463ef33dd1`
- Independent audit: `revised`
- Researched: `2026-08-06T12:47:29.719796+00:00`

I verified checkpoint-scoped artifacts available in the provided findings for Ministral-3-3B-Instruct-2512. Checkpoint blobs present in the inspected Hugging Face repository include a config.json (revision b4b0163a32c9...), a SYSTEM_PROMPT.txt blob, a README and ancillary files (chat_template.jinja, consolidated.safetensors). The config.json blob documents model_type "ministral3", architecture class "Mistral3ForConditionalGeneration", text_config.max_position_embeddings = 262144, and quantization metadata listing quant_method = "fp8". A separate ONNX variant README (ONNX variant repository blob at commit 0dc70c2e...) reports variant-level benchmark numbers but does not provide a checkpoint-scoped evaluation protocol in the inspected blob. A GGUF artifact page in the findings reports quantization levels and an FP8 VRAM-fit claim. Where the inspected artifacts do not provide checkpoint-scoped statements (exhaustive safety guidance, formal input-validation procedures, tokenizer blob presence, or head-to-head numeric benchmarks in the main checkpoint repository/config), I record explicit evidence gaps and cite the exact blobs inspected.

## Identity

- Upstream name: Ministral-3-3B-Instruct-2512
- Checkpoint/version: Ministral-3-3B-Instruct-2512
- Immutable revision: b4b0163a32c9867d2424ac10b40fe0db6fa95110
- Parameter scale: 3B
- Architecture/head: Mistral3ForConditionalGeneration
- License: Apache-2.0
- Evidence: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt, https://hf.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-ONNX/blob/0dc70c2ecc585ae0710287d070842ae8fac290ad/README.md, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-BF16/commit/8df721b37ecc8b369b84aa27dfb58396fbc39097

## Selection

### Recommended

- **Chat and instruction-focused natural-language generation** — The repository and ONNX-variant README describe this artifact as an instruct post-trained variant intended for instruction/chat tasks; repository files include an explicit SYSTEM_PROMPT and chat template supporting instruction-style usage.
  Scope: Ministral-3-3B-Instruct-2512 (upstream checkpoint blobs inspected)
  Evidence: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-ONNX/blob/0dc70c2ecc585ae0710287d070842ae8fac290ad/README.md, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt
- **Local/edge deployment using quantized variants to reduce VRAM** — The checkpoint config.json contains quantization metadata (quant_method = "fp8") and a GGUF artifact page in the findings lists quantization levels and an FP8 VRAM-fit claim, supporting variant-scoped deployment for lower-VRAM scenarios.
  Scope: Ministral-3-3B-Instruct-2512 (FP8/quantized variants as represented in variant artifacts)
  Evidence: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json, https://hf.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF

### Conditional


### Avoid

- **High-stakes clinical, safety-critical, or other regulated decision-making without human expert review** — Evidence gap: The inspected checkpoint-scoped upstream artifacts (repository tree, config.json blob, and SYSTEM_PROMPT blob) do not provide checkpoint-scoped documentation, validation, or certification procedures for clinical or regulated high-stakes use.
  Scope: Ministral-3-3B-Instruct-2512
  Evidence: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt

## Input preparation

### Semantic inputs

- Natural-language prompts for chat and instruction tasks (system/user/assistant style), as evidenced by a SYSTEM_PROMPT and a chat template file in the repository. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt

### Accepted formats

- Role-formatted text prompts (system/user/assistant) and templates (chat_template.jinja) are present in the repository and are the documented prompt-format artifacts in the inspected checkpoint repository. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt

### Preprocessing

- Configuration field text_config.max_position_embeddings = 262144 documents the checkpoint's configured maximum context length. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json
- The checkpoint config.json lists quantization metadata with quant_method = "fp8" (quantization metadata present in the config blob). Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json
- Evidence gap: A tokenizer.json blob or checkpoint-scoped tokenizer artifact was not identified in the provided findings; the repository tree was inspected for tokenizer artifacts but a tokenizer.json locator was not in the provided facts. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main

### Pre-submit validation

- Evidence gap: No checkpoint-scoped formal input-validation procedures (schema validation, automated ambiguity rejection, or explicit bounds checks) are documented in the inspected repository tree, config.json blob, or SYSTEM_PROMPT blob. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt

### Task-specific formatting

- SYSTEM_PROMPT.txt in the repository is an explicit system-prompt example artifact for this checkpoint and a usable role-template. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt
- The repository contains a chat_template.jinja file which provides a prompt/template artifact for instruction/chat formatting. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main

## Output interpretation

### Outputs

- Default outputs are natural-language text; the checkpoint is described as an instruct post-trained variant for chat/instruction-style generation in repository and ONNX-variant README artifacts. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-ONNX/blob/0dc70c2ecc585ae0710287d070842ae8fac290ad/README.md

### Interpretation

- Treat outputs as text conditioned on prompt and system-template; no checkpoint-scoped formal interpretation-to-structured-data mapping is documented in the inspected blobs. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json

### Post-inference validation

- Evidence gap: No checkpoint-scoped post-inference quality-calibration or structured-output validation procedures are present in the inspected repository blobs. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json

## Public benchmarks

### Aggregate ONNX-variant benchmark suite reported in ONNX README

- Dataset/split: ONNX README reported suites: Arena Hard, WildBench, MATH, MM MTBench / not reported
- Metric/value: Arena Hard / WildBench / MATH Maj@1 / MM MTBench (per-README reported scores) / Arena Hard 0.305; WildBench 56.8; MATH Maj@1 0.830; MM MTBench 7.83 (`context-only`)
- Model scope: Ministral-3-3B-Instruct-2512 (ONNX variant README)
- Conditions: Reported in the ONNX variant README; variant-specific conditions and exact protocol not described in the inspected checkpoint repository blobs.
- Source: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-ONNX/blob/0dc70c2ecc585ae0710287d070842ae8fac290ad/README.md
- Locator: README.md (ONNX variant repository blob at commit 0dc70c2ecc585ae0710287d070842ae8fac290ad)
- Caveat: Results are reported in an ONNX-variant README; the main checkpoint repository/config do not provide an evaluation protocol to directly compare these numbers with other checkpoint-scoped benchmarks.
- Caveat: No dataset splits or exact prompting/evaluation protocol are specified in the ONNX README blob inspected.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Evidence gap: The inspected checkpoint-scoped artifacts (repository tree, config.json blob) do not document the training data or provide exhaustive safety/usage restrictions for this exact checkpoint. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json
- The checkpoint config and variant artifacts indicate FP8 quantization metadata and a large configured context window, but vendor-certified VRAM/latency deployment guarantees are not documented in the checkpoint blobs inspected; VRAM/latency claims are variant-dependent in the examined variant artifacts. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json, https://hf.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-ONNX/blob/0dc70c2ecc585ae0710287d070842ae8fac290ad/README.md

### Safety

- Evidence gap: The inspected checkpoint-scoped upstream artifacts (repository tree, config.json, SYSTEM_PROMPT) do not include an exhaustive safety or data-handling policy for this exact checkpoint; no checkpoint-scoped clinical or regulated-use guidance was found in the provided blobs. Sources: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json, https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Ministral-3-3B-Instruct-2512 (Hugging Face repository tree/main)

- URL: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/tree/main
- Publisher: Mistral AI / Hugging Face
- Type: `repository`
- Primary because: Canonical upstream repository tree for the exact checkpoint containing README, SYSTEM_PROMPT.txt, chat_template.jinja, and repository blobs inspected in the findings.
- Scope: Ministral-3-3B-Instruct-2512
- Supports: Repository contains README, SYSTEM_PROMPT.txt, chat_template.jinja, consolidated.safetensors, and config.json (repository-level artifacts)
- Supports: Presence of instruction-posttrained checkpoint blobs and template artifacts

### Ministral-3-3B-Instruct-2512 config.json (checkpoint blob, revision b4b0163a32c9...)

- URL: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/b4b0163a32c9867d2424ac10b40fe0db6fa95110/config.json
- Publisher: Mistral AI / Hugging Face
- Type: `repository`
- Primary because: Exact checkpoint-scoped config.json blob present in the provided findings documenting architecture and configuration fields.
- Scope: Ministral-3-3B-Instruct-2512
- Supports: model_type = "ministral3" and architecture = "Mistral3ForConditionalGeneration"
- Supports: text_config.max_position_embeddings = 262144
- Supports: quantization metadata listing quant_method = "fp8"
- Supports: hidden_size = 3072, intermediate_size = 9216, num_hidden_layers = 26, num_attention_heads = 32, num_key_value_heads = 8 (as present in the config blob)

### Ministral-3-3B-Instruct-2512 SYSTEM_PROMPT.txt (repository blob)

- URL: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512/blob/1bca1cbe7ccc1d7e102f04e88ddc2daa16e7b738/SYSTEM_PROMPT.txt
- Publisher: Mistral AI / Hugging Face
- Type: `repository`
- Primary because: Checkpoint-scoped SYSTEM_PROMPT artifact present in the repository tree in the provided findings.
- Scope: Ministral-3-3B-Instruct-2512
- Supports: Presence of a SYSTEM_PROMPT.txt example for the instruct checkpoint
- Supports: System-prompt wording and template artifact stored in repository blob

### Ministral-3-3B-Instruct-2512 ONNX README (ONNX variant repository blob)

- URL: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-ONNX/blob/0dc70c2ecc585ae0710287d070842ae8fac290ad/README.md
- Publisher: Mistral AI / Hugging Face
- Type: `repository`
- Primary because: ONNX-variant README blob in the provided findings reporting variant-scoped benchmark numbers and variant artifacts.
- Scope: Ministral-3-3B-Instruct-2512 (ONNX variant)
- Supports: ONNX-variant reported benchmark scores (Arena Hard, WildBench, MATH, MM MTBench) as documented in the README blob
- Supports: Statements describing the instruct post‑trained variant and variant artifacts (vision encoder ONNX files, embed_tokens ONNX files)

### Ministral-3-3B-Instruct-2512 BF16 branch commit (BF16 variant blob)

- URL: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-BF16/commit/8df721b37ecc8b369b84aa27dfb58396fbc39097
- Publisher: Mistral AI / Hugging Face
- Type: `repository`
- Primary because: BF16 variant branch commit blob included in the provided findings documenting BF16 variant config/README notes.
- Scope: Ministral-3-3B-Instruct-2512 (BF16 variant)
- Supports: BF16 branch README commit notes about architecture and launchability (vLLM and Transformers)
- Supports: BF16 variant-specific config semantics referenced in the commit blob

### Ministral-3-3B-Instruct-2512 GGUF artifact page (quantization/edge artifact)

- URL: https://hf.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF
- Publisher: Mistral AI / Hugging Face
- Type: `repository`
- Primary because: GGUF artifact page present in the provided findings documenting quantization levels and a VRAM-fit claim for FP8 in the findings.
- Scope: Ministral-3-3B-Instruct-2512 (GGUF/quantized artifact)
- Supports: GGUF page lists quantization levels (4-bit, 5-bit, 8-bit, 16-bit) in the provided findings
- Supports: GGUF page asserts FP8 VRAM-fit and edge-deployment design in the provided findings

### Exact official starting source declared by Forge

- URL: https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: mistralai-ministral-3-3b-instruct-2512
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Benchmarks: Evidence gap: No checkpoint-scoped, upstream canonical numeric benchmark table or figure published in the inspected checkpoint repository README or config.json blobs for this exact checkpoint; an ONNX-variant README reports variant-scoped numbers but lacks protocol detail.
- Comparisons: Evidence gap: No checkpoint-scoped primary-source head-to-head comparisons were found in the inspected blobs.
- Inputs: Evidence gap: No checkpoint-scoped formal input validation procedures (schema checks, ambiguity rejection, or automated bounds checks) are documented in the inspected repository tree, config.json blob, or SYSTEM_PROMPT blob.
- Tokenizer: Evidence gap: A tokenizer.json checkpoint-scoped blob was not identified in the provided findings (repository tree inspected in the provided facts did not list a tokenizer.json locator).
- Outputs: Evidence gap: No checkpoint-scoped formal post-inference validation or calibration procedures are documented in the inspected repository blobs (README, config.json, SYSTEM_PROMPT).
- Safety: Evidence gap: No checkpoint-scoped, exhaustive safety, privacy, biosecurity, or clinical-use guidance is present in the inspected repository blobs (repository tree, config.json, SYSTEM_PROMPT) for this exact checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 35 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: unexpected property modelRevision Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.findings Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
