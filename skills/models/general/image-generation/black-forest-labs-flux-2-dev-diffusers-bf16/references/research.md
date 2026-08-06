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

- Research key: `huggingface-co-black-forest-labs-flux-2-dev-1e027ba417`
- Independent audit: `revised`
- Researched: `2026-08-06T10:43:30.356617+00:00`

FLUX.2 [dev] (checkpoint name: black-forest-labs/FLUX.2-dev) is described in upstream primary sources as a 32 billion-parameter rectified flow transformer for image generation and editing from text and optional reference images. The checkpoint is gated on Hugging Face and distributed under a FLUX Non-Commercial License that restricts commercial uses and competing training/fine-tuning/distillation. Primary upstream documentation includes the Hugging Face model page, the model README, the FLUX Non-Commercial license text, and GitHub documentation for Diffusers integration and runtime guidance. The primary sources do not publish numeric benchmarks for this exact checkpoint nor a detailed I/O contract (tokenization, exact input shapes, stable decoding contract) for the Forge-served Diffusers BF16 wrapper; those are noted as evidence gaps below.

## Identity

- Upstream name: FLUX.2 [dev]
- Checkpoint/version: FLUX.2-dev
- Immutable revision: not reported
- Parameter scale: 32 billion parameters
- Architecture/head: rectified flow transformer
- License: FLUX Non-Commercial License
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-DEV, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

## Selection

### Recommended

- **Text-to-image generation using the Diffusers integration** — Upstream model card and repository documentation state FLUX.2 [dev] can generate images from text prompts and provide example Diffusers-based pipeline code indicating Diffusers usage and torch.bfloat16 for the VAE in example wrappers.
  Scope: FLUX.2-dev (upstream checkpoint as documented on Hugging Face and repository docs); Diffusers-based usage examples noted in the repository documentation
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md

### Conditional

- **Non-commercial research, hobbyist experimentation, and testing in non-production environments** — Must comply with the FLUX Non-Commercial License terms and Acceptable Use Policy; gating and login acceptance on Hugging Face required prior to download/use.
  Scope: FLUX.2-dev upstream checkpoint under the FLUX Non-Commercial License
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md, https://bfl.ai/legal/usage-policy

### Avoid

- **Commercial training, fine-tuning, or distillation to produce a competing model** — The FLUX Non-Commercial License explicitly restricts training/fine-tuning/distillation that would produce a competing FLUX model and limits model use to non-commercial purposes without a separate commercial license.
  Scope: FLUX.2-dev (upstream checkpoint)
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-DEV
- **Commercial deployment or API provisioning of the FLUX.2-dev weights without a commercial license from Black Forest Labs** — Upstream license and model-licenses documentation require a separate commercial license for commercial use; modal and deployment restrictions are stated in the FLUX Non-Commercial License.
  Scope: FLUX.2-dev (upstream checkpoint)
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-DEV

## Input preparation

### Semantic inputs

- Input modalities include text prompts and optional reference images for editing tasks. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md
- Example Diffusers-based pipeline code in upstream docs shows usage of a Flux2Pipeline and remote_text_encoder pattern for producing prompt embeddings (implying text prompts and remote encoder embeddings in examples). Sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md

### Accepted formats

- Evidence gap: The canonical upstream sources do not publish a formal machine-readable accepted-format specification (exact tokenization, image pixel formats, image tensor shapes, or serialized input envelope) for FLUX.2-dev; checked locations: model card, model README, and GitHub docs. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

### Preprocessing

- Evidence gap: Upstream documentation does not supply a complete preprocessing pipeline (exact resizing, normalization constants, tokenizer name/versions, or deterministic featurization steps) for the exact FLUX.2-dev checkpoint; checked model README and GitHub docs. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

### Pre-submit validation

- Evidence gap: Upstream sources do not publish explicit input-validation rules (bounds, disallowed input patterns, max token/image sizes) for the FLUX.2-dev checkpoint; checked model card and repository docs. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

### Task-specific formatting

- Evidence gap: No formal prompt templates, paired-input ordering rules, or canonical task-formatting specification for FLUX.2-dev are published in the upstream model card or repository docs; checked model card and repository documentation. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

## Output interpretation

### Outputs

- Images generated by FLUX.2-dev; the upstream examples and docs show generated images and describe image-generation/editing capability but do not publish a formal output contract (exact tensor shapes, color-channel ordering, or encoded file format guarantees). Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md

### Interpretation

- Interpret outputs conservatively: upstream sources do not provide calibration curves, confidence scores, or numeric quality metrics for outputs of this exact checkpoint. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md, https://huggingface.co/black-forest-labs/FLUX.2-dev

### Post-inference validation

- Evidence gap: No published post-inference validation checklist (sanity checks, watermarking, NSFW filtering pipeline details) for the exact FLUX.2-dev checkpoint found in the model card or repository docs. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### not reported — `insufficient-evidence`

- Task: not reported
- Criteria: No checkpoint-to-checkpoint comparison data for FLUX.2-dev versus named peers is published in the upstream model card or repository docs.
- Rationale: Primary sources do not present direct numeric or protocol-matched comparisons for this exact checkpoint.
- Comparison conditions: Checked model card and repository README/docs for any direct comparisons or benchmark tables; none found for FLUX.2-dev.
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/README.md

## Limitations and safety

### Limitations

- The FLUX Non-Commercial License restricts commercial use and prohibits training/fine-tuning/distillation to create competing models; users must obtain a separate commercial license for commercial deployment or competing-model training. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-DEV
- Access gating and login requirements: users must accept the gating on the Hugging Face repository and authenticate (hf auth) prior to using FLUX.2-dev as described in repository docs. Sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md, https://huggingface.co/black-forest-labs/FLUX.2-dev
- Hardware and precision constraints: upstream docs indicate large VRAM requirements for native runs and reference bf16 use for parts of the pipeline; consumer-quantized variants and remote text-encoder patterns are documented as workarounds. Sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md, https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md

### Safety

- Black Forest Labs evaluated and implemented pre-release and post-release mitigations for misuse risks (including CSAM and non-consensual intimate imagery) as described in upstream documentation and usage policy. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev#usage, https://bfl.ai/legal/usage-policy
- Evidence gap: No detailed upstream publication of a post-inference automated safety-filtering pipeline (implementation, thresholds, or code) for FLUX.2-dev was found in the model card or repository docs. Sources: https://huggingface.co/black-forest-labs/FLUX.2-dev, https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### FLUX.2-dev — model card

- URL: https://huggingface.co/black-forest-labs/FLUX.2-dev
- Publisher: Black Forest Labs
- Type: `model-card`
- Primary because: Canonical Hugging Face model card and gated download/usage entry for the FLUX.2-dev checkpoint; contains capability statements and license pointer.
- Scope: black-forest-labs/FLUX.2-dev (upstream checkpoint/model card)
- Supports: FLUX.2 [dev] is a 32 billion parameter rectified flow transformer
- Supports: Model can generate, edit, and combine images based on text instructions
- Supports: Access requires agreeing to the FLUX Non-Commercial License and Acceptable Use Policy
- Supports: License name and gating information

### FLUX.2-dev README (Hugging Face repository file)

- URL: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md
- Publisher: Black Forest Labs
- Type: `official-documentation`
- Primary because: Repository README hosted with the model on Hugging Face; provides example code and notes about Diffusers usage.
- Scope: black-forest-labs/FLUX.2-dev repository files
- Supports: FLUX.2 [dev] description and example Diffusers code
- Supports: Notes about precision and example pipeline usage

### FLUX.2-dev LICENSE (model repository)

- URL: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md
- Publisher: Black Forest Labs
- Type: `official-documentation`
- Primary because: Canonical license text published alongside the model on Hugging Face that defines the FLUX Non-Commercial License restrictions.
- Scope: license for black-forest-labs/FLUX.2-dev
- Supports: Statement that the model is released under the FLUX Non-Commercial License
- Supports: Restrictions on commercial use and competing training/fine-tuning/distillation

### FLUX model_licenses: LICENSE-FLUX-DEV (GitHub)

- URL: https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-DEV
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Repository-hosted canonical model-license file enumerating model variants covered and license terms for FLUX [dev] models.
- Scope: flux2 repository model_licenses for FLUX.2 [dev]
- Supports: FLUX [dev] model license text and restrictions
- Supports: Enumeration of model variants covered by the FLUX Non-Commercial License

### flux2 GitHub docs: flux2_dev_hf.md

- URL: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md
- Publisher: Black Forest Labs
- Type: `official-documentation`
- Primary because: Repository documentation describing Hugging Face/Diffusers integration, example code, VRAM guidance, and gating/authentication instructions.
- Scope: flux2 repository docs for FLUX.2-dev usage
- Supports: Checkpoint name black-forest-labs/FLUX.2-dev
- Supports: Diffusers pipeline usage and example code
- Supports: VRAM and hardware guidance and login/gating instructions

### flux2 repository top-level LICENSE

- URL: https://github.com/black-forest-labs/flux2/blob/main/LICENSE.md
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Top-level repository license file for the flux2 codebase (distinct from model license); documents repository code license (Apache-2.0).
- Scope: flux2 repository code license
- Supports: Top-level repository license is Apache License Version 2.0 (for code/artifacts where stated)

### Hugging Face repository file list (model tree)

- URL: https://huggingface.co/black-forest-labs/FLUX.2-dev/tree/main
- Publisher: Black Forest Labs
- Type: `official-documentation`
- Primary because: File listing for the upstream model repository that documents available files (model_index.json, weights file sizes) published with the checkpoint.
- Scope: black-forest-labs/FLUX.2-dev repository files and artifacts
- Supports: Repository file listing including model_index.json and approximate model file sizes

### flux pyproject.toml (flux repository)

- URL: https://github.com/black-forest-labs/flux/blob/main/pyproject.toml
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Project metadata and dependency declarations for the FLUX inference codebase; used to verify declared runtime dependencies and Python version constraints.
- Scope: flux repository project configuration
- Supports: Project name, authorship contact, Python version requirement, and listed dependencies

### flux2 GitHub README

- URL: https://github.com/black-forest-labs/flux2/blob/main/README.md
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Repository README describing FLUX.2 releases, family variants, license notes, and release dates/capability summary within the repository.
- Scope: flux2 repository README and release notes
- Supports: Release description for FLUX.2 [dev] and statements about family variants and license distinctions
- Supports: Notes on autoencoder licensing and hardware test environment statements

### Black Forest Labs Usage Policy

- URL: https://bfl.ai/legal/usage-policy
- Publisher: Black Forest Labs
- Type: `official-documentation`
- Primary because: Official usage policy published by Black Forest Labs referenced by upstream documentation for acceptable use and mitigations.
- Scope: organizational usage policy applicable to FLUX models
- Supports: Usage policy statements referenced by upstream documentation and model card

### Cited official first-party source

- URL: https://huggingface.co/black-forest-labs/FLUX.2-dev#usage
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: black-forest-labs-flux-2-dev
- Supports: Exact independently audited claim citation

## Evidence gaps

- No numeric benchmark data (dataset/split/metric/value/conditions) for FLUX.2-dev exact checkpoint found in checked primary sources: https://huggingface.co/black-forest-labs/FLUX.2-dev (checked model card and linked README and repository docs).
- I/O contract details (tokenizer identity/version, exact input tensor shapes, image pixel format, decoding file format, and deterministic preprocessing constants) are not published in the checked primary sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md; https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md.
- Post-inference safety-filter implementation details (automated filtering code, thresholds, watermarking implementation) for the exact FLUX.2-dev checkpoint are not documented in the checked primary sources: https://huggingface.co/black-forest-labs/FLUX.2-dev; https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md.
- No direct checkpoint-to-checkpoint task/protocol-matched comparisons for FLUX.2-dev versus named peer checkpoints found in checked primary sources: https://huggingface.co/black-forest-labs/FLUX.2-dev; https://github.com/black-forest-labs/flux2/blob/main/README.md.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 53 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERCIAL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/pyproject.toml Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/unsloth/FLUX.2-dev-GGUF Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Manusagents/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_dev_hf.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/LICENSE.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Manusagents/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/black-forest-labs/FLUX.2-dev#usage: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
