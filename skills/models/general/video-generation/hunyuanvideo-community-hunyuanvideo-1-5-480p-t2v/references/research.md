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

- Research key: `huggingface-co-docs-diffusers-v0-38-0-en-api-pipelines-hunyuan-video15-0154145706`
- Independent audit: `revised`
- Researched: `2026-08-06T11:27:57.480415+00:00`

HunyuanVideo-1.5 is documented in the audited primary sources as a lightweight text-to-video and image-to-video generation model family with an author-stated parameter scale of ~8.3 billion and components including a DiT-style transformer with selective and sliding tile attention (SSTA), glyph-aware text encoding, and an efficient video super-resolution component. The audited upstream repository and Hugging Face model page provide usage examples (including a Diffusers pretrained identifier referencing a 720p T2V artifact) and an example generation setting that uses 50 inference steps. The canonical technical report (arXiv) and upstream artifacts were checked for numeric benchmark tables and for an explicit named checkpoint string matching "HunyuanVideo-1.5-480P-T2V"; the audited findings do not contain a primary-source table of numeric evaluation metrics for the exact callable checkpoint nor an explicit upstream naming of the exact 480P checkpoint string, so those points are recorded as evidence gaps. Licensing is governed by the Tencent Hunyuan Community License as published in the repository LICENSE file.

## Identity

- Upstream name: HunyuanVideo-1.5
- Checkpoint/version: Evidence gap: No primary source in the audited findings explicitly names a checkpoint string "HunyuanVideo-1.5-480P-T2V"; the available upstream pretrained identifier example references a 720p T2V artifact (see repository usage).
- Immutable revision: not reported
- Parameter scale: 8.3 billion parameters
- Architecture/head: DiT (Diffusion Transformer) with selective and sliding tile attention (SSTA); glyph-aware text encoding; progressive pre-training and post-training; includes an efficient video super-resolution component
- License: Tencent Hunyuan Community License
- Evidence: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE, https://huggingface.co/docs/diffusers/en/using-diffusers/callback, https://arxiv.org/abs/2511.18870

## Selection

### Recommended

- **Short-form text-to-video generation for rapid prototyping and social/web content** — Primary upstream artifacts document text-to-video capability and lightweight video generation with consumer-GPU efficiency, supporting short-form video generation workflows.
  Scope: Upstream HunyuanVideo-1.5 family (as documented by repository and model page); treat as upstream-checkpoint evidence when used via wrappers.
  Evidence: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://huggingface.co/tencent/HunyuanVideo-1.5, https://arxiv.org/abs/2511.18870
- **Image-to-video (I2V) generation using the HunyuanVideo-1.5 I2V pipeline variant** — Primary sources describe both text-to-video and image-to-video capabilities for the family and document an I2V workflow in the Diffusers pipeline documentation and upstream repository.
  Scope: Upstream HunyuanVideo-1.5 I2V variant as described in Diffusers documentation and the repository
  Evidence: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- **Consumer-GPU inference using published HunyuanVideo-1.5 variants (e.g., 720p example shown upstream)** — Upstream documentation and the model page indicate the family is designed to run efficiently on consumer-grade GPUs and provide example generation settings (including an example using 50 inference steps).
  Scope: Upstream HunyuanVideo-1.5 artifacts and example pretrained identifiers
  Evidence: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

### Conditional

- **Adjust inference step counts or use distilled variants for faster inference** — Evidence gap: The audited primary sources do not provide authoritative, general-purpose recommended step ranges for "step-distilled" vs "CFG-distilled" variants (e.g., claims like 8–12 steps for step-distilled I2V or 50 steps for CFG-distilled variants are not present in the audited findings). The upstream repository contains an example invocation using 50 inference steps; any deployment using non-default step counts or distilled variants should be validated on held prompts and checked against the specific upstream variant documentation.
  Scope: Upstream HunyuanVideo-1.5 example usage (repository example with 50 inference steps) and unspecified distilled variants
  Evidence: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

### Avoid

- **Clinical, PHI-bearing, or safety-critical decision-making workflows** — Evidence gap: The audited primary sources do not provide domain-specific validation, clinical disclaimers, or governance documentation for use in medical or other safety-critical contexts; no primary-source statements were found that establish clinical validation for HunyuanVideo-1.5 for such uses.
  Scope: Upstream HunyuanVideo-1.5 family (checked technical report and model page for domain-specific clinical validation and governance)
  Evidence: https://arxiv.org/abs/2511.18870, https://huggingface.co/tencent/HunyuanVideo-1.5, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

## Input preparation

### Semantic inputs

- Primary semantic input: text prompt for text-to-video (T2V) generation. Sources: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://arxiv.org/abs/2511.18870
- Optional semantic input: conditioning image for image-to-video (I2V) workflows as supported by the family. Sources: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

### Accepted formats

- Evidence gap: The audited primary sources do not provide a comprehensive, explicit list of accepted input file formats or an authoritative statement naming a 480p checkpoint string. The upstream repository demonstrates and references a 720p T2V pretrained identifier in examples; no primary-source claim for a "HunyuanVideo-1.5-480P-T2V" exact checkpoint string was found in the audited findings. Sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

### Preprocessing

- Evidence gap: The audited primary sources do not include an explicit, code-level upstream description of per-pipeline pixel preprocessing parameters (e.g., exact resize, normalization, or dtype rules) for I2V/T2V; callers should follow the pipeline implementation in the upstream repository for concrete preprocessing steps. Sources: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

### Pre-submit validation

- Evidence gap: No primary-source input-validation rules (bounds, forbidden content filters, or format checks) were found in the audited findings; implementers should consult the upstream repository code and model page for any runtime checks and apply additional application-level validation. Sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

### Task-specific formatting

- Evidence gap: The audited findings do not document an upstream API contract stating that pipeline guider behavior (e.g., pipe.guider API or guidance_scale semantics) is implemented in a manner that relocates guidance handling from a guidance_scale argument to a guider object; callers should inspect the upstream Diffusers pipeline implementation for exact runtime parameter locations. Sources: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- Evidence gap: The audited findings do not provide authoritative pairings of specific tokenizer + text-encoder modules (for example, Qwen2.5-VLTextModel + Qwen2Tokenizer or ByT5Tokenizer + T5 encoder) as a required mapping in primary upstream documentation; the repository acknowledges contributions from Qwen-VL but does not publish a definitive tokenizer/text-encoder pairing mapping in the audited findings. Sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

## Output interpretation

### Outputs

- Evidence gap: The audited primary sources do not supply a single authoritative, numeric output contract (shape, unit, or file container) for the callable Forge-wrapped artifact; upstream examples indicate video outputs with frame counts and fps in example invocations but no standardized output file format or exact pixel shape is specified for a named 480p checkpoint in the audited findings. Sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

### Interpretation

- Evidence gap: The audited findings do not define a guaranteed semantic meaning for model scores or produced artifacts beyond example-quality assertions; consumers should treat outputs as generative media without calibrated likelihood scores and perform downstream validation for application-specific interpretation. Sources: https://arxiv.org/abs/2511.18870, https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md

### Post-inference validation

- Evidence gap: The audited primary sources do not provide post-inference calibration or quality thresholds (e.g., no numeric PSNR/LPIPS thresholds published for the exact upstream checkpoints); implementers should perform held-prompt validation and human review for production deployments. Sources: https://arxiv.org/abs/2511.18870, https://huggingface.co/tencent/HunyuanVideo-1.5

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### No directly comparable upstream checkpoint with a validated numeric benchmark was identified in the audited findings — `insufficient-evidence`

- Task: Text-to-video visual quality and motion coherence
- Criteria: No primary-source numeric benchmark rows for the exact callable upstream checkpoint were found; therefore no primary-evidence head-to-head comparison is supported.
- Rationale: The audited sources (technical report, upstream repository, and model page) describe capability and qualitative quality but do not publish machine-readable benchmark tables for an exact named checkpoint that can be compared here.
- Comparison conditions: Checked canonical technical report (arXiv), upstream repository, and Hugging Face model page for numeric benchmark tables or per-checkpoint measured metrics; none were found for a directly comparable row.
- Evidence: https://arxiv.org/abs/2511.18870, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

## Limitations and safety

### Limitations

- The Tencent Hunyuan Community License restricts use to specified territories and requires adherence to an Acceptable Use Policy; license terms impose distribution and attribution requirements and disclaim warranties. Sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE
- Evidence gap: No primary-source documentation was found in the audited findings demonstrating domain-specific validation, safety guarantees, or clinical suitability for HunyuanVideo-1.5; users must not assume clinical or safety-critical readiness without further validation. Sources: https://arxiv.org/abs/2511.18870, https://huggingface.co/tencent/HunyuanVideo-1.5

### Safety

- The upstream LICENSE indicates a limited, territory-bound license and includes Acceptable Use Policy constraints; downstream users must review the Tencent Hunyuan Community License before redistribution or service deployment. Sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE
- Evidence gap: The audited primary sources do not publish a dedicated, model-specific safety mitigation checklist (content filters, PII/PHI handling, or deployment gating); implementers must apply independent safety review and content-moderation practices. Sources: https://arxiv.org/abs/2511.18870, https://huggingface.co/tencent/HunyuanVideo-1.5

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Diffusers pipeline documentation: HunyuanVideo-1.5 pipeline (repository docs)

- URL: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md
- Publisher: huggingface.co / diffusers repository
- Type: `official-documentation`
- Primary because: Official Diffusers project documentation file describing the HunyuanVideo pipeline and model family.
- Scope: HunyuanVideo-1.5 pipeline documentation and API reference
- Supports: Model family capabilities (T2V/I2V), architecture claims (DiT with SSTA, glyph-aware text encoding), and usage context as stated in the upstream documentation.

### HunyuanVideo-1.5 upstream repository (Tencent-Hunyuan)

- URL: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- Publisher: Tencent Hunyuan
- Type: `repository`
- Primary because: First-party upstream implementation repository for HunyuanVideo-1.5 containing example usage and model artifacts.
- Scope: Upstream repository, example usage, and pretrained identifiers
- Supports: Example usage (pretrained identifier referencing 720p T2V), example inference settings (including an example using 50 inference steps), repository-level LICENSE file reference.

### HunyuanVideo-1.5 model page (Hugging Face)

- URL: https://huggingface.co/tencent/HunyuanVideo-1.5
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Official Hugging Face model hosting page for HunyuanVideo-1.5 containing model metadata and citation information.
- Scope: Hosted model card describing HunyuanVideo-1.5
- Supports: Parameter scale claim (~8.3B), model capability statements (T2V/I2V) and usage commentary.

### HunyuanVideo-1.5 LICENSE (Tencent Hunyuan Community License)

- URL: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE
- Publisher: Tencent Hunyuan
- Type: `repository`
- Primary because: The repository LICENSE file is the primary publisher artifact for license and usage terms.
- Scope: Upstream repository license for HunyuanVideo-1.5
- Supports: License name (Tencent Hunyuan Community License), territorial restrictions, distribution and attribution obligations, and warranty disclaimers.

### Diffusers callbacks documentation

- URL: https://huggingface.co/docs/diffusers/en/using-diffusers/callback
- Publisher: huggingface.co / diffusers docs
- Type: `official-documentation`
- Primary because: Official Diffusers documentation on callbacks which affect pipeline execution and denoising steps.
- Scope: Diffusers callback behavior relevant to pipeline runtime
- Supports: Callback concept and behavior in Diffusers pipelines (execution at end of denoising steps, ability to affect subsequent steps).

### HunyuanVideo 1.5 technical report (arXiv preprint)

- URL: https://arxiv.org/abs/2511.18870
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical technical report/preprint announcing HunyuanVideo 1.5 and describing model capabilities.
- Scope: Technical report for HunyuanVideo-1.5
- Supports: Technical-report-level descriptions of the model family, capability statements, and the canonical citation entry for the model.

### Exact official starting source declared by Forge

- URL: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: hunyuanvideo-community-hunyuanvideo-1-5
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No primary-source statement in the audited findings explicitly names a checkpoint string "HunyuanVideo-1.5-480P-T2V"; checked the upstream repository and model page for an exact 480p checkpoint identifier and did not find it (checked repository root and model-card). See: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5
- Evidence gap: No primary-source numeric benchmark table or per-checkpoint numeric evaluation rows for the exact callable upstream checkpoint were found in the technical report, upstream repository, or model page. Checked: https://arxiv.org/abs/2511.18870, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5
- Evidence gap: The audited findings do not publish authoritative, general-purpose recommended step ranges for "step-distilled" vs "CFG-distilled" variants (e.g., claims like 8–12 steps for step-distilled I2V). Checked: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- Evidence gap: The audited findings do not provide explicit tokenizer + text-encoder pairing tables (for example, a required Qwen2.5-VLTextModel + Qwen2Tokenizer pairing); checked repository and model page for explicit pairing guidance. See: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5
- Evidence gap: The audited findings do not include a per-pipeline, code-level preprocessing specification (exact resize, normalization, dtype) for I2V/T2V beyond repository examples; callers should inspect implementation for exact preprocessing. Checked: https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/hunyuan_video15.md, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- Evidence gap: No primary-source model-specific safety mitigation checklist (content filters, PII/PHI handling, or deployment gating) was found in the audited findings; implementers must apply independent safety review. Checked: https://arxiv.org/abs/2511.18870, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://huggingface.co/tencent/HunyuanVideo-1.5

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'phr00t' for this exact model scope: $.sources[7] uses unapproved repository owner 'phr00t' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://api.emergentmind.com/papers/2511.18870 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/tree/main/ComfyUI Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/tree/main/ComfyUI Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/tree/main/ComfyUI Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
