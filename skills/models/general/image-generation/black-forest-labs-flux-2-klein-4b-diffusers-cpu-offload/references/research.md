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

- Research key: `huggingface-co-black-forest-labs-flux-2-klein-4b-618d859d80`
- Independent audit: `revised`
- Researched: `2026-08-06T11:04:22.488039+00:00`

Scoped to the exact upstream checkpoint black-forest-labs/FLUX.2-klein-4B (4B rectified flow transformer). Primary upstream evidence (Hugging Face model page and the checkpoint tokenizer file) and provider/runtime evidence (NVIDIA NGC container page, NVIDIA NIM API reference, NVIDIA build page, NVIDIA support matrix) corroborate: 4B parameter scale, rectified flow transformer architecture, Apache-2.0 license per the Hugging Face page, capabilities for text-to-image generation and image editing including multi-reference editing, and published tokenizer special tokens and tokenizer model_max_length. Primary gaps from inspected canonical sources: no checkpoint-level numeric benchmark tables naming the exact FLUX.2 Klein 4B checkpoint were found at the inspected locations; there are conflicting or divergent VRAM/system-requirement indications between the Hugging Face model page (approx. 13 GB VRAM) and NVIDIA support matrix (48 GB minimal), and no primary-source documentation was found that publish formalized intrinsic numeric confidence scores, calibration semantics, or precise accepted image-file format/channel-order/pixel-size bounds for image-conditioning inputs for the exact checkpoint.

## Identity

- Upstream name: black-forest-labs/FLUX.2-klein-4B
- Checkpoint/version: black-forest-labs/FLUX.2-klein-4B
- Immutable revision: not reported
- Parameter scale: 4B
- Architecture/head: rectified flow transformer
- License: Apache-2.0
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blame/refs%2Fpr%2F2/tokenizer/tokenizer_config.json, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://build.nvidia.com/black-forest-labs, https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html

## Selection

### Recommended

- **Text-to-image generation (text prompts)** — The Hugging Face model page lists text-to-image generation as a supported capability for the FLUX.2 Klein 4B checkpoint; NVIDIA provider documentation and build page also describe the checkpoint as intended for image-generation workflows.
  Scope: upstream checkpoint: black-forest-labs/FLUX.2-klein-4B
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://build.nvidia.com/black-forest-labs
- **Image editing and multi-reference image-conditioned editing** — The Hugging Face model page indicates image editing and multi-reference editing capabilities for the Klein 4B checkpoint; NVIDIA provider pages and the NVIDIA build page report unified generation and editing capabilities for the packaged model.
  Scope: upstream checkpoint: black-forest-labs/FLUX.2-klein-4B
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://build.nvidia.com/black-forest-labs

### Conditional


### Avoid

- **Use for clinical, medical, or other safety‑critical decision‑making** — Evidence gap: no primary-source documentation in the inspected canonical sources indicates clinical validation, regulatory approval, or validated clinical performance for this checkpoint. Checked primary locations for checkpoint-level clinical/regulated claims: Hugging Face model page and NVIDIA provider pages (NIM API reference, NGC container entry, NVIDIA build page).
  Scope: upstream checkpoint: black-forest-labs/FLUX.2-klein-4B
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://build.nvidia.com/black-forest-labs

## Input preparation

### Semantic inputs

- Accepted upstream semantic inputs include text prompts; the checkpoint is documented for text‑to‑image generation and image editing (image-conditioning capability is documented as a model feature). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://build.nvidia.com/black-forest-labs

### Accepted formats

- Evidence gap: exact accepted image-file formats (e.g., PNG, JPEG), required channel ordering (RGB/BGR), and explicit pixel-size/resolution bounds for image-conditioning inputs are not documented in the inspected canonical sources at the checked locations. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html, https://build.nvidia.com/black-forest-labs

### Preprocessing

- Tokenizer and tokenization resources for the exact checkpoint are published in the Hugging Face checkpoint: the tokenizer configuration lists model_max_length and special tokens; the tokenizer file was inspected for special-token definitions and settings. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blame/refs%2Fpr%2F2/tokenizer/tokenizer_config.json, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- The tokenizer configuration inspected defines special tokens and tokenizer runtime settings including a very large model_max_length value and explicit special-token names (see tokenizer_config.json). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blame/refs%2Fpr%2F2/tokenizer/tokenizer_config.json

### Pre-submit validation

- Evidence gap: explicit upstream input-validation rules (exact accepted image file formats, pixel-size bounds, required channel order, and any mandatory prompt token-length limits beyond the tokenizer's model_max_length) are not documented at the inspected canonical sources and files. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html, https://build.nvidia.com/black-forest-labs

### Task-specific formatting

- Evidence gap: no canonical, standardized prompt templates, mandatory control tokens, or mandatory prompt-formatting conventions for text prompts are published at the inspected canonical sources for the exact checkpoint (checked Hugging Face model page and NVIDIA provider pages). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://build.nvidia.com/black-forest-labs

## Output interpretation

### Outputs

- The upstream checkpoint produces raster image outputs for generation and editing tasks (image outputs). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://build.nvidia.com/black-forest-labs, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

### Interpretation

- Evidence gap: intrinsic numeric confidence scores or calibrated confidence semantics for generated images are not described in the inspected canonical sources. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://build.nvidia.com/black-forest-labs

### Post-inference validation

- Evidence gap: no formalized post-inference calibration procedures, score-normalization guidance, or numeric thresholds for output filtering are published in the inspected canonical provider or upstream checkpoint sources. Sources: https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://build.nvidia.com/black-forest-labs

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### black-forest-labs-flux-1-dev — `insufficient-evidence`

- Task: image-generation
- Criteria: No protocol-matched, checkpoint-level numeric benchmark for a direct comparison was found in the inspected canonical sources for both exact checkpoints under a shared dataset/split/metric/protocol.
- Rationale: Insufficient primary-source, checkpoint-level numeric benchmark data naming both the exact FLUX.2 Klein 4B checkpoint and the listed alternative under a shared dataset/split/metric/protocol in the inspected canonical sources.
- Comparison conditions: Evidence gap: required dataset/split/metric/protocol details and checkpoint-level numeric tables are not present in the inspected canonical sources for an apples-to-apples comparison.
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html

## Limitations and safety

### Limitations

- The upstream Klein 4B checkpoint is published under the Apache-2.0 license per the Hugging Face model page. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- There is a documented inconsistency between upstream and provider system/VRAM statements: the Hugging Face model page reports the model fits in approximately 13 GB of VRAM, while the NVIDIA support matrix lists minimal system/GPU-memory requirements of 48 GB for FLUX.2‑klein; this conflict is present in the inspected canonical sources and could not be reconciled from those sources alone. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html
- Evidence gap: checkpoint-level numeric benchmark tables (dataset, split, metric, numeric value) naming the exact FLUX.2 Klein 4B checkpoint were not found at the inspected canonical locations (model card pages, provider pages, and checked files). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://build.nvidia.com/black-forest-labs

### Safety

- Provider/runtime documentation indicates users are responsible for implementing guardrails, content filtering, abuse monitoring, and access controls when deploying provider-packaged containers; follow provider guidance when deploying the packaged checkpoint. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html
- Evidence gap: no primary-source documentation at the inspected canonical sources specifies formal numeric thresholds or exact implementation details for provider guardrail models or Cosmos guardrail behavior for this checkpoint. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://build.nvidia.com/black-forest-labs, https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### FLUX.2 Klein 4B Hugging Face model page

- URL: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Publisher: Black Forest Labs
- Type: `model-card`
- Primary because: Canonical upstream checkpoint page for the FLUX.2 Klein 4B model card and files.
- Scope: upstream checkpoint: black-forest-labs/FLUX.2-klein-4B
- Supports: identity
- Supports: recommended-use
- Supports: outputs
- Supports: input-prep
- Supports: license

### Tokenizer configuration for FLUX.2-klein-4B (tokenizer_config.json, inspected via blame/pr path)

- URL: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blame/refs%2Fpr%2F2/tokenizer/tokenizer_config.json
- Publisher: Black Forest Labs
- Type: `model-card`
- Primary because: Canonical tokenizer configuration file published in the checkpoint repository; contains special-token definitions and tokenizer settings used by the checkpoint.
- Scope: upstream checkpoint files: tokenizer_config.json
- Supports: tokenizer
- Supports: input-prep
- Supports: preprocessing

### NVIDIA NGC container catalog for FLUX.2 Klein 4B

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NGC container catalog entry documenting the container that packages the Klein 4B checkpoint and provider runtime metadata.
- Scope: provider/runtime container: nvcr.io/nim/black-forest-labs/flux.2-klein-4b
- Supports: provider-runtime
- Supports: safety
- Supports: identity

### NVIDIA NIM API reference for FLUX.2‑klein (visual-genai)

- URL: https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Provider-side NIM reference documenting the packaged checkpoint and runtime-level guidance (versioned API reference).
- Scope: provider/runtime: NIM reference for black-forest-labs-flux_2-klein-4b
- Supports: provider-runtime
- Supports: recommended-use
- Supports: safety
- Supports: identity

### NVIDIA NIM API reference (older version) for FLUX.2‑klein

- URL: https://docs.nvidia.com/nim/visual-genai/1.4.0/api/flux.2-klein.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Archived/older provider-side NIM API reference page for FLUX.2‑klein used to cross-check provider documentation across versions.
- Scope: provider/runtime: NIM reference (older version) for black-forest-labs-flux_2-klein-4b
- Supports: provider-runtime
- Supports: identity

### NVIDIA build model pages (Black Forest Labs entry)

- URL: https://build.nvidia.com/black-forest-labs
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA-hosted model catalog and vendor page describing the packaged FLUX.2 Klein 4B checkpoint and capabilities.
- Scope: provider/runtime: NVIDIA build pages for Black Forest Labs models
- Supports: identity
- Supports: recommended-use
- Supports: provider-runtime
- Supports: safety

### NVIDIA NIM support matrix for Visual GenAI

- URL: https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Provider-side support matrix listing minimal and recommended system requirements and supported precisions for FLUX.2‑klein.
- Scope: provider/runtime: NIM support matrix
- Supports: provider-runtime
- Supports: limitations
- Supports: identity

## Evidence gaps

- Evidence gap: no checkpoint-level numeric benchmark tables (dataset, split, metric, numeric value) naming the exact FLUX.2 Klein 4B checkpoint were found at the inspected primary locations. Checked locations and exact paths/headings: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B (model card page: checked 'Evaluation' or README benchmarking sections), https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b (NGC container page: checked container description and metadata fields), https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html (NIM API reference: checked capability and examples sections), and https://build.nvidia.com/black-forest-labs (NVIDIA build model page: checked the model description and statistics sections).
- Evidence gap: exact accepted image-file formats, required channel ordering (RGB/BGR), and explicit pixel-size or resolution bounds for image-conditioning inputs are not documented at the inspected primary locations. Checked exact locations: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B (model card page), https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html (NIM API reference page), https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b (NGC container description), https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html (support matrix), and https://build.nvidia.com/black-forest-labs (NVIDIA build model page).
- Evidence gap: intrinsic numeric confidence scores or calibrated confidence semantics for generated images are not described in the inspected canonical sources. Checked exact locations: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B (model card page), https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html (NIM API reference), https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b (NGC container), and https://build.nvidia.com/black-forest-labs (NVIDIA build model page).
- Evidence gap: precise Forge/NVIDIA serving-variant runtime keys, CUDA/runtime version mapping, and explicit behavioral differences between diffusers vs cpu-offload serving variants for the Forge candidate slugs could not be found in the inspected primary provider pages. Checked exact locations: https://docs.nvidia.com/nim/visual-genai/1.5.2/api/flux.2-klein.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, and https://build.nvidia.com/black-forest-labs.
- Evidence gap: exact reconciled GPU memory/VRAM requirement values for the exact FLUX.2 Klein 4B checkpoint could not be resolved from the inspected primary sources due to conflicting statements. Checked exact locations: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B (model card page: 'fits in approximately 13 GB of VRAM'), and https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html (support matrix: lists minimal GPU memory as 48 GB).
- Evidence gap: precise upstream immutable model-weight revision or release tag for black-forest-labs/FLUX.2-klein-4B is not reported in the inspected primary sources. Checked exact locations: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B (model page) and the provider pages: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b and https://build.nvidia.com/black-forest-labs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 43 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: unexpected property preprocessing Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
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
- `medium` $.sources[11]: $.sources[11]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12]: $.sources[12]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12]: $.sources[12]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary host hf-mirror.com: $.sources[11] uses forbidden secondary host hf-mirror.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.sources[6]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
