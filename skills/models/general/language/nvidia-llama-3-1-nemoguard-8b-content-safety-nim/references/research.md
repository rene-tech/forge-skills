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

- Research key: `build-nvidia-com-nvidia-llama-3-1-nemoguard-8b-content-safety-15a952b714`
- Independent audit: `revised`
- Researched: `2026-07-23T22:40:37.838168+00:00`

NVIDIA publishes nvidia/llama-3.1-nemoguard-8b-content-safety as a LoRA/PEFT-tuned content-safety moderator derived from the multilingual Llama-3.1-8B-Instruct base. The Hugging Face model page and README describe the checkpoint purpose (classifying user prompts and LLM responses as safe or unsafe and returning violated category labels per a vendor taxonomy) and show example JSON outputs. An adapter_config.json file declaring LoRA hyperparameters and target_modules is present in the repository. NIM documentation (index, prompt-template, release-notes) documents NIM packaging, prompt templates, and a release note asserting an increased context length (v1.10.1: 8K -> 128K). Primary sources inspected do not provide an explicit immutable tuned-weights artifact identifier pairing with adapter_config.json, nor do they publish tokenizer internals specific to the tuned checkpoint. The inspected primary sources do not publish numeric benchmark table rows explicitly scoped to this tuned checkpoint (dataset/split/metric/model-tag/conditions).

## Identity

- Upstream name: multilingual Llama-3.1-8B-Instruct (Meta)
- Checkpoint/version: nvidia/llama-3.1-nemoguard-8b-content-safety
- Immutable revision: 943c14d
- Parameter scale: 8B
- Architecture/head: Transformer (Llama-3.1-8B-Instruct base; LoRA/PEFT tuned safety adapter)
- License: NVIDIA Open Model License Agreement and the Llama 3.1 Community License Agreement
- Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/release-notes.html, https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/deploy

## Selection

### Recommended

- **Content moderation / safety classification of user prompts and LLM responses** — Hugging Face model repository and README blobs and the NIM prompt-template documentation describe this checkpoint as a content safety moderator that classifies prompts and model responses as safe or unsafe and returns violated category labels per the vendor taxonomy; example prompt templates and example output JSON are provided.
  Scope: nvidia/llama-3.1-nemoguard-8b-content-safety
  Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/prompt-template.html
- **Integration into NIM/NemoGuard microservice safety pipelines for moderated agent workflows** — NIM/container deploy documentation and build.nvidia deploy page document NIM packaging and container invocation patterns appropriate for integration into guarded inference pipelines.
  Scope: NIM container packaging for nvidia/llama-3.1-nemoguard-8b-content-safety
  Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/deploy, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html

### Conditional

- **High-context-length moderation (very long context)** — Before relying on extended-context (128K) functionality, confirm the deployed NIM/container release and target runtime engine build document the deterministic mapping of the extended-context claim to specific runtime engines, quantization modes, and serving modes; the release notes assert increased context length but do not deterministically map that claim to exact runtime builds/quantization/serving modes in the inspected sources.
  Scope: NIM/container release (release notes v1.10.1) for the llama-3-1-nemoguard-8b-contentsafety packaging
  Evidence: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/release-notes.html, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html
- **Assuming full multilingual parity with the upstream base for moderation use across languages** — Validate language coverage for the specific NIM/container variant and release before assuming multilingual parity with the upstream base; NIM docs assert the model is derived from a multilingual upstream base but the tuned-checkpoint language coverage is not explicitly detailed in the inspected primary sources.
  Scope: NIM/container packaging for nvidia/llama-3.1-nemoguard-8b-content-safety
  Evidence: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety

### Avoid

- **Assuming vendor-published numeric benchmark tables exist for this exact LoRA-tuned checkpoint and using them as-is for selection/tuning decisions** — Inspected primary sources do not publish numeric benchmark table rows scoped to the exact tuned checkpoint (dataset/split/metric/model-tag/conditions) for nvidia/llama-3.1-nemoguard-8b-content-safety; upstream Llama-3.1-8B-Instruct materials are upstream-checkpoint evidence only and do not substitute for tuned-checkpoint evidence.
  Scope: nvidia/llama-3.1-nemoguard-8b-content-safety
  Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2
- **Using the checkpoint as a general-purpose high-reasoning/math assistant without validation** — Vendor materials frame Nemoguard as a moderation/judge model intended to classify safety risks rather than as a general-purpose high-reasoning assistant; the model card and README emphasize content-safety classification.
  Scope: nvidia/llama-3.1-nemoguard-8b-content-safety
  Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md

## Input preparation

### Semantic inputs

- Input is a text instruction/prompt representing content to be classified; prompts follow a vendor-provided taxonomy instruction and include the user input to be moderated. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/prompt-template.html

### Accepted formats

- Text instruction prompts formatted per the vendor prompt-template and invoked via the NIM microservice endpoints as documented in the NIM deploy/getting-started pages. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/deploy, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/prompt-template.html

### Preprocessing

- Adapter configuration (adapter_config.json) documents LoRA hyperparameters and target_modules; standard LoRA/PEFT tooling is referenced for applying the adapter to the upstream base during inference or merge. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety
- Evidence gap: The research did not find an explicit immutable tuned-weights artifact identifier (immutable filename, signed release artifact, or single immutable hash) pairing with adapter_config.json in the inspected primary repository locations. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json
- Evidence gap: Tokenizer internals and exact tokenizer artifact for the tuned checkpoint (vocab file, tokenizer_config, merges, or an explicit pointer confirming the upstream tokenizer is unchanged) were not found in the inspected repository blobs. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json

### Pre-submit validation

- Validate inputs are text and conform to the taxonomy prompt format; confirm deployed NIM/container release before trusting extended-context or release-dependent behavior. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/deploy

### Task-specific formatting

- Prompt templates include an instruction with taxonomy, the user input, and a response instruction; sample prompts instruct the LLM to format the response as JSON fields such as 'User Safety', 'Response Safety', and 'Safety Categories'. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/prompt-template.html, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md

## Output interpretation

### Outputs

- Output is structured as categorical moderation judgments with JSON fields such as 'User Safety', 'Response Safety', and 'Safety Categories' listing violated taxonomy categories when unsafe. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/prompt-template.html

### Interpretation

- Treat outputs as taxonomy-aligned categorical labels (safe vs unsafe and taxonomy categories); do not assume numeric calibration, recommended probability thresholds, or confidence-interval semantics absent vendor-provided calibration guidance. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html

### Post-inference validation

- Post-inference: verify category IDs/names against the vendor taxonomy and confirm the NIM/container release before trusting results in production pipelines. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety
- Evidence gap: Numeric calibration guidance, recommended probability thresholds, or confidence-interval guidance for category outputs was not found in the inspected primary sources. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Content moderation / safety classification
- Criteria: No checkpoint-scoped vendor-published numeric benchmark rows or matched-protocol comparisons were found for nvidia/llama-3.1-nemoguard-8b-content-safety in the inspected primary sources.
- Rationale: Inspected Hugging Face model page, README blobs, adapter_config.json, commits page, and NIM docs do not contain numeric benchmark rows explicitly scoped to the tuned checkpoint; upstream base-model materials are upstream-checkpoint evidence only and cannot be conflated with tuned-checkpoint results.
- Comparison conditions: N/A - no matching checkpoint-scoped benchmark rows found.
- Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html

## Limitations and safety

### Limitations

- Evidence gap: The inspected primary sources do not publish an explicit immutable tuned-weights artifact identifier (immutable filename, signed release artifact, or single immutable hash) that pairs with adapter_config.json for the LoRA/PEFT adapter. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json
- Evidence gap: Tokenizer internals and a tuned-checkpoint tokenizer artifact (vocab file, tokenizer_config, merges, or explicit pointer confirming use of the upstream tokenizer) are not present in the inspected repository blobs. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json
- Evidence gap: No vendor-published numeric benchmark table rows scoped to the exact tuned checkpoint (dataset/split/metric/model-tag/conditions) were found at the inspected primary locators. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/release-notes.html
- Evidence gap: Checkpoint-scoped matched-protocol comparisons to other named checkpoints were not found in inspected primary sources. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html

### Safety

- Primary safety function: classifies content as safe or unsafe and returns violated category labels when unsafe, aligned to the vendor's content-harm taxonomy. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md
- Training dataset attribution: NIM documentation states the model was trained using the Nemotron Content Safety Dataset V2 (formerly Aegis AI Content Safety Dataset 2.0) described as a curated collection of approximately 30 thousand dialog samples; this dataset attribution is asserted in the NIM documentation index. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html
- Operational safety guidance: vendor docs position the NIM for guarded deployments (NemoGuard) and reference evaluator harnesses; no tuned-checkpoint numeric calibration guidance was published in the inspected sources. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/release-notes.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model: nvidia/llama-3.1-nemoguard-8b-content-safety

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety
- Publisher: NVIDIA (Hugging Face upload)
- Type: `model-card`
- Primary because: Official vendor-hosted Hugging Face model repository describing the tuned checkpoint, purpose, and example outputs.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety
- Supports: identity.evidenceUrls
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.interpretation
- Supports: safety

### Hugging Face README blob (commit db1c750)

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/db1c7503ae2db4ded65332272834d3e7a3192a5c/README.md
- Publisher: NVIDIA (Hugging Face repository blob)
- Type: `model-card`
- Primary because: Exact README blob in the Hugging Face repository that contains prompt examples, example output JSON, and format guidance for the exact checkpoint.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (README blob: db1c750)
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.outputs
- Supports: recommendedUseCases
- Supports: identity.evidenceUrls

### Hugging Face adapter_config.json (lora-adapter blob)

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json
- Publisher: NVIDIA (Hugging Face repository blob)
- Type: `repository`
- Primary because: Adapter configuration JSON in the checkpoint repository declaring LoRA/PEFT hyperparameters and target modules for the tuned checkpoint.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (adapter_config.json blob)
- Supports: identity.evidenceUrls
- Supports: inputPreparation.preprocessing
- Supports: limitations

### Hugging Face commits (refs/pr/2)

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2
- Publisher: NVIDIA (Hugging Face repository metadata)
- Type: `repository`
- Primary because: Repository commit history showing commit SHAs and upload actions relevant to the tuned checkpoint artifacts.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (commits refs/pr/2)
- Supports: identity.evidenceUrls
- Supports: limitations

### NIM documentation index: Llama-3.1 NemoGuard 8B ContentSafety (1.0.0)

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM documentation index describing the NIM/container, dataset attribution, multilingual support claim, and high-level usage/packaging.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (NIM docs)
- Supports: identity.evidenceUrls
- Supports: safety
- Supports: limitations
- Supports: researchSummary
- Supports: conditionalUseCases

### NIM prompt-template documentation (latest)

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/prompt-template.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: NIM prompt-template documentation showing the official prompt structure and instruction-to-JSON formatting guidance.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (prompt-template)
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.outputs

### NIM release notes: llama-3-1-nemoguard-8b-contentsafety (latest)

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/release-notes.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: NIM release notes documenting container release changes and asserting a context-length increase for the NIM packaging.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (release-notes)
- Supports: conditionalUseCases
- Supports: limitations
- Supports: researchSummary

### Build NVIDIA NIM deploy page for the NIM container

- URL: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/deploy
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: NIM container deploy documentation describing runtime invocation variables and endpoints for the served NIM.
- Scope: nvidia/llama-3.1-nemoguard-8b-content-safety (deploy)
- Supports: inputPreparation.semanticInputs
- Supports: recommendedUseCases
- Supports: identity.evidenceUrls
- Supports: limitations

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-content-safety
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-llama-3-1-nemoguard-8b-content-safety
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Immutable tuned-weights artifact identifier (immutable filename, signed release artifact, or single immutable hash) for the LoRA/PEFT adapter used by nvidia/llama-3.1-nemoguard-8b-content-safety was not found in the inspected primary locations: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/commits/refs%2Fpr%2F2, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json.
- Evidence gap: Tokenizer internals and exact tokenizer artifact for the tuned checkpoint (vocab file, tokenizer_config, merges, or explicit pointer confirming use of the upstream tokenizer) were not found at the inspected repository blobs: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety/blob/0ef9fa805d78e7a30958f0324d733dd5d4098d97/llama-3.1-nemoguard-8b-content-safety-lora-adapter/adapter_config.json.
- Evidence gap: Checkpoint-scoped numeric benchmark table rows for nvidia/llama-3.1-nemoguard-8b-content-safety (dataset/split/metric/model-tag/conditions) were not found at the inspected canonical locations: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html (checked model card README blobs, adapter_config.json blob, and NIM docs index).
- Evidence gap: Checkpoint-scoped matched-protocol comparisons between nvidia/llama-3.1-nemoguard-8b-content-safety and other named checkpoints were not found at the inspected primary locations: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html.
- Evidence gap: Numeric calibration guidance, recommended probability thresholds, or confidence-interval guidance for category outputs for this tuned checkpoint were not found at the inspected primary locations: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html.
- Evidence gap: Precise deterministic mapping of the NIM/container extended-context claim (128K) to specific runtime engines, builds, quantization modes, and serving modes for this tuned NIM/container was not found at the inspected primary locations: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/release-notes.html and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/1.0.0/index.html.
- Evidence gap: Exact tokenizer artifact URL or explicit upstream-tokenizer pointer for the tuned checkpoint was not found in the inspected repository blobs: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety (checked repository root and listed blobs).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 19 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-content-safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://generalanalysis.com/blog/ga-guard-series Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19] uses forbidden secondary URL https: $.sources[19] uses forbidden secondary URL https://premai.io/blog/breaking-the-pareto-frontier-with-prem-ai-miniguard-v0-1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24].primary must be true: $.sources[24].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25].primary must be true: $.sources[25].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[26].primary must be true: $.sources[26].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[27] uses forbidden secondary URL https: $.sources[27] uses forbidden secondary URL https://developer.nvidia.com/blog/how-to-safeguard-ai-agents-for-customer-service-with-nvidia-nemo-guardrails Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVIDIA-AI-Blueprints/rag Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVIDIA-AI-Blueprints/rag Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.sources[8]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-content-safety: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
