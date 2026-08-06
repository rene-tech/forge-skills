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

- Research key: `build-nvidia-com-qwen-qwen-2-5-7b-instruct-94e0f4a536`
- Independent audit: `revised`
- Researched: `2026-07-23T23:18:06.533432+00:00`

Primary upstream evidence shows an instruction-tuned checkpoint named Qwen2.5-7B-Instruct hosted at the Hugging Face repository (7B parameter class) and associated repository blobs (config.json, tokenizer_config.json, LICENSE). NVIDIA NIM documentation lists a supported-models entry and a NIM model identifier for qwen/qwen-2.5-7b-instruct (version tag present in NVIDIA docs). Official repository blobs verify tokenizer configuration and context-length fields; the repository LICENSE file contains Apache-2.0 text but does not specify applicability to model weights. Primary sources checked do not expose an explicit NVIDIA-published byte-level SHA/manifest tying a served NIM artifact to the upstream checkpoint, nor do the checked primary model-card and NVIDIA pages provide canonical benchmark table rows for this exact instruct checkpoint; protocol-level Forge/NIM request/response and canonical prompt/chat-format contracts are also not documented in the inspected primary blobs and NVIDIA pages.

## Identity

- Upstream name: Qwen2.5-7B-Instruct
- Checkpoint/version: Qwen2.5-7B-Instruct
- Immutable revision: not reported
- Parameter scale: 7 billion parameters
- Architecture/head: not reported
- License: Apache-2.0 (LICENSE file present in repository; applicability to model weights not reported)
- Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/tokenizer_config.json, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/_include/models.html, https://huggingface.co/Qwen/Qwen2.5-7B

## Selection

### Recommended

- **Assistant/chat and instruction-following text generation** — The upstream Hugging Face model card identifies the checkpoint as instruction-tuned and appropriate for instruction-following / chat-style generation.
  Scope: Qwen2.5-7B-Instruct (upstream Hugging Face model card)
  Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Conditional

- **BF16-specific deployment** — Deploy only on BF16-capable hardware and validated serving stacks; upstream config and NVIDIA docs indicate BF16 support but do not prove runtime enforcement by Forge/NIM.
  Scope: Qwen2.5-7B-Instruct upstream config and NVIDIA NIM listing
  Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html

### Avoid

- **High-stakes clinical or safety-critical decision making** — Evidence gap: the inspected primary sources do not provide clinical validation, certification, or safety-critical readiness statements for this exact checkpoint; do not rely on the model as the sole basis for safety-critical decisions without domain validation.
  Scope: Qwen2.5-7B-Instruct upstream checkpoint scope
  Evidence: documented evidence gap
- **Substituting the Qwen2.5-7B base checkpoint for the Instruct checkpoint in conversation workloads** — Base-model evidence is a separate upstream checkpoint and should not be substituted for the instruction-tuned checkpoint without explicit evidence; keep base-versus-instruct claims scoped to their respective checkpoints.
  Scope: Boundary between Qwen2.5-7B (base) and Qwen2.5-7B-Instruct (instruct)
  Evidence: https://huggingface.co/Qwen/Qwen2.5-7B

## Input preparation

### Semantic inputs

- The model consumes text prompts (instruction-tuned generation). Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Accepted formats

- Text is the supported input modality described by the upstream model card for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Preprocessing

- Tokenization and tokenizer behavior are governed by the repository tokenizer assets (tokenizer_config.json) and the upstream config.json; special tokens and max model length are declared in tokenizer_config.json. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Pre-submit validation

- Validate sequence-length and sliding-window assumptions against the upstream tokenizer_config.json and config.json before deployment; the inspected blobs declare maximum lengths and related fields but do not document Forge/NIM enforcement. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Task-specific formatting

- Evidence gap: the inspected primary sources do not provide a canonical NVIDIA Forge or NIM prompt template, chat-format contract, or exact prompt-response pairing for this model scope.

## Output interpretation

### Outputs

- The upstream model is an instruction-tuned language model that produces text output for causal generation tasks (instruction-following / chat-style outputs as implied by the model card). Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Interpretation

- Generated text should be treated as unconstrained model generation rather than calibrated confidence; no primary-source contract for calibrated probabilities or confidence calibration was found in the inspected blobs and pages. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Post-inference validation

- Post-inference validation (domain-specific checks, human review, or downstream testing) is required because the inspected primary sources do not provide correctness guarantees or calibrated confidence contracts for this exact checkpoint. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Evidence gap: No NVIDIA-published byte-level SHA/manifest was found in the inspected primary sources that proves bytewise identity between the NVIDIA-served NIM artifact and the upstream Hugging Face checkpoint files. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/_include/models.html, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Evidence gap: No primary-source benchmark table row (exact checkpoint, dataset split, metric, numeric value, and table/figure/section locator) for Qwen2.5-7B-Instruct was found in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html
- Evidence gap: The upstream repository LICENSE file contains Apache-2.0 text but does not explicitly state applicability to model weights distinct from repository code/artifacts in the inspected LICENSE blob. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE

### Safety

- Forge policy: Do not use this model as the sole basis for clinical, medical, or other safety-critical decisions without qualified human review and domain-specific validation.
- Forge policy: Do not submit sensitive personal, regulated, or proprietary text unless your deployment and data-governance review explicitly approve that handling path.
- Evidence gap: No primary-source clinical validation or certification statements for this exact checkpoint were found in the inspected primary sources (listed in evidenceUrls). Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NIM supported models (1.15.0) - supported-models listing

- URL: https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party NVIDIA documentation listing the supported NIM models and build/runtime guidance (NIM model identifier and version evidence).
- Scope: NVIDIA NIM supported-models entry for qwen/qwen-2.5-7b-instruct
- Supports: NIM model identifier and version evidence
- Supports: runtime hardware/precision guidance
- Supports: NIM-supported-precision and GPU configuration statements

### NVIDIA NIM models include (1.15.0) - include/models.html

- URL: https://docs.nvidia.com/nim/large-language-models/1.15.0/_include/models.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party NVIDIA documentation fragment that lists the qwen/qwen-2.5-7b-instruct entry and provider/version column data.
- Scope: NVIDIA NIM model identifier qwen/qwen-2.5-7b-instruct and associated version tag
- Supports: NIM model identifier
- Supports: NIM version tag evidence
- Supports: provider metadata for the NIM entry

### Qwen2.5-7B-Instruct model card (Hugging Face)

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Official upstream model card page for the exact instruct checkpoint that identifies the checkpoint name and instruction-tuned scope.
- Scope: Qwen2.5-7B-Instruct upstream checkpoint
- Supports: upstream checkpoint identity
- Supports: instruction-tuned usage/recommended use evidence
- Supports: general model-card metadata

### Qwen2.5-7B-Instruct config.json (repository blob)

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Official upstream repository configuration file blob for the exact instruct checkpoint used to verify runtime-relevant fields.
- Scope: Qwen2.5-7B-Instruct configuration blob
- Supports: configuration and runtime-relevant fields
- Supports: context-related config values and usage instructions

### Qwen2.5-7B-Instruct LICENSE (repository blob)

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Official upstream repository license file for the instruct repository.
- Scope: Qwen2.5-7B-Instruct repository license blob
- Supports: license text evidence
- Supports: license applicability limitation (absence of explicit weight-applicability statement)

### Qwen2.5-7B-Instruct tokenizer_config.json (repository blob)

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/tokenizer_config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Official upstream tokenizer configuration blob for the instruct checkpoint used to verify tokenizer class, special tokens, and max model length.
- Scope: Qwen2.5-7B-Instruct tokenizer configuration
- Supports: tokenizer class name and tokenizer special tokens
- Supports: maximum model length and tokenizer parameters

### Qwen2.5-7B (base) model card (upstream boundary comparison)

- URL: https://huggingface.co/Qwen/Qwen2.5-7B
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Official upstream base-model page used strictly as a scoped comparison boundary between base and instruct checkpoints.
- Scope: Qwen2.5-7B base checkpoint (comparison boundary only)
- Supports: base-model identity for scoped comparison boundary

### NVIDIA NIM supported models (1.8.0) - supported-models listing

- URL: https://docs.nvidia.com/nim/large-language-models/1.8.0/supported-models.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Earlier NVIDIA NIM supported-models documentation present in the reviewed primary-source set (used to cross-check hardware/precision guidance).
- Scope: NVIDIA NIM supported-models entries for Qwen2.5 7B Instruct
- Supports: hardware and precision guidance
- Supports: supported GPU count and precision notes

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/qwen/qwen-2.5-7b-instruct
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: qwen-2-5-7b-instruct
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No primary-source benchmark table row was found for Qwen2.5-7B-Instruct in the inspected primary URLs: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (model card headings and files), https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json (config blob), https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html (NIM supported-models listing). I inspected the model-card headings/files and the cited NVIDIA NIM supported-models pages and found no exact checkpoint-level table/figure/section locator containing dataset, split, metric, and numeric value for this instruct checkpoint.
- Evidence gap: The inspected primary URLs (https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/_include/models.html, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) did not publish an explicit byte-level SHA/manifest mapping proving bytewise identity between any NVIDIA-served NIM artifact and the upstream checkpoint blobs.
- Evidence gap: The upstream LICENSE blob (https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE) contains Apache-2.0 text but does not explicitly state applicability to model weights versus repository code/artifacts.
- Evidence gap: No canonical NVIDIA Forge or NIM request/response schema, prompt template, or chat-format contract for this exact model scope was found in the inspected primary URLs: https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/_include/models.html, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json.
- Evidence gap: No protocol-matched primary-source comparisons against non-Qwen alternatives for this exact Qwen2.5-7B-Instruct checkpoint were found in the inspected primary URLs (https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html); comparisons are therefore marked as insufficient-evidence in this dossier.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/qwen/qwen-2.5-7b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/qwen/qwen-2.5-7b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
