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

- Research key: `huggingface-co-docs-diffusers-api-pipelines-kandinsky5-image-e9e2461bb8`
- Independent audit: `revised`
- Researched: `2026-08-06T11:26:55.050481+00:00`

kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers is an Image Lite supervised fine-tuned Kandinsky 5.0-family Diffusers checkpoint (reported as a 6 billion parameter Image Lite model). The checkpoint's model_index.json declares the Diffusers pipeline class Kandinsky5T2IPipeline and lists its main components (Kandinsky5Transformer3DModel transformer, AutoencoderKL VAE, primary text encoder Qwen2_5_VLForConditionalGeneration, secondary text encoder CLIPTextModel, and FlowMatchEulerDiscreteScheduler). The checkpoint repository blobs (model README, text_encoder README and config) document processor/tokenizer and text-encoder configuration (including YaRN-related entries and image resize parameter semantics such as rounding resized dimensions to a multiple of 28). The canonical arXiv preprint HTML (v1 and v2) states family-level license (MIT) and documents family-level limitations and that the authors did not ship built-in content-filtering; the inspected checkpoint blobs do not publish an immutable checkpoint revision/hash, checkpoint-scoped numeric benchmarks, or runtime metrics for this exact Diffusers checkpoint—those absences are recorded as evidence gaps.

## Identity

- Upstream name: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Checkpoint/version: Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Immutable revision: not reported
- Parameter scale: 6 billion parameters
- Architecture/head: Diffusers Kandinsky5T2IPipeline with components declared in model_index.json: Kandinsky5Transformer3DModel (transformer), AutoencoderKL (VAE), primary text encoder Qwen2_5_VLForConditionalGeneration, secondary text encoder CLIPTextModel, and FlowMatchEulerDiscreteScheduler (scheduler)
- License: MIT (as stated in arXiv v1 and v2)
- Evidence: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true, https://arxiv.org/html/2511.14993v1, https://arxiv.org/html/2511.14993v2

## Selection

### Recommended

- **Text-to-image generation (single prompt or batched prompts → generated image artifacts)** — The model repository README and model_index.json identify this checkpoint as a Kandinsky5 text-to-image checkpoint (Kandinsky5T2IPipeline) and the repository README describes the Kandinsky 5.0 Image Lite family and T2I usage.
  Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
  Evidence: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true

### Conditional

- **Extended-context or length-extrapolated text conditioning using YaRN-enabled text encoder configuration** — Enable YaRN per the checkpoint text_encoder README/config and validate memory, performance, and task-specific impact in your runtime; the checkpoint text_encoder README notes YaRN impacts but does not publish runtime measurements or recommended runtime limits.
  Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers (text_encoder configuration blobs)
  Evidence: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/config.json

### Avoid

- **Assuming checkpoint-scoped numeric benchmarks for model selection** — No checkpoint-scoped numeric benchmark tables (dataset, split, metric, numeric value, and experiment conditions) are present in the inspected primary sources for this exact Diffusers checkpoint.
  Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
  Evidence: https://arxiv.org/abs/2511.14993, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true
- **Relying on built-in content-filtering or assuming the checkpoint enforces content-safety** — The canonical arXiv preprint (v1 and v2) documents that authors did not implement built-in content-filtering systems and places responsibility on users; the checkpoint blobs do not provide checkpoint-scoped content-filtering mechanisms.
  Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers (family- and checkpoint-level inspection)
  Evidence: https://arxiv.org/html/2511.14993v1, https://arxiv.org/html/2511.14993v2, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers

## Input preparation

### Semantic inputs

- Primary input modality is text prompts for text-to-image generation (single prompt or batched prompts as per repository usage descriptions). Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json
- The checkpoint uses dual text-encoder conditioning: a primary Qwen2_5_VLForConditionalGeneration encoder and a secondary CLIPTextModel encoder as declared in model_index.json, implying text tokenization/processing via the referenced processors/tokenizers. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md

### Accepted formats

- The checkpoint is published and documented as a text-to-image Diffusers checkpoint (T2I); the model repository and model_index.json identify the pipeline and its intended T2I usage. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json

### Preprocessing

- Text preprocessing/tokenization for the primary and secondary encoders is indicated by the model_index.json and the text_encoder README (references to Qwen2VLProcessor and CLIP tokenizer usage are present in the repository blobs). Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md
- Image resize handling and rounding behavior: the text_encoder README documents that resized_height and resized_width are rounded to the nearest multiple of 28 and that images may be resized to fit within min_pixels and max_pixels while preserving aspect ratio. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md

### Pre-submit validation

- The inspected repository blobs (model README, text_encoder README, model_index.json) document processor and size semantics but do not provide a canonical strict input-rejection validator API or a complete upstream-enforced bounds list for all out-of-range inputs for this checkpoint. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json

### Task-specific formatting

- The checkpoint repository describes text-to-image usage patterns and the presence of dual encoders and processor configuration (text_encoder README and model_index.json); the inspected blobs do not publish special prompt-control tokens or canonical prompt templates beyond the repository's descriptions of encoder/processor usage. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers

## Output interpretation

### Outputs

- This checkpoint produces generated image artifacts as its primary output (text-to-image generation), as documented by the model README and model_index.json which identify the checkpoint as an Image Lite T2I model. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true

### Interpretation

- The inspected primary artifacts do not document calibrated per-image probabilities, logits, or numeric confidence scores returned by this checkpoint; generated images should be treated as opaque generated artifacts and require application-level QA or calibration if numeric confidences are needed. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://arxiv.org/abs/2511.14993

### Post-inference validation

- The checkpoint blobs and the canonical preprint do not provide canonical post-inference numeric calibration or quality thresholds for this checkpoint; downstream users must apply their own perceptual-quality and content-policy validation. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://arxiv.org/html/2511.14993v1

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Family-level limitations documented in the canonical preprint include challenges in text-visual alignment, long-term temporal modelling, and generalization across visual domains (family-level limitations reported in the paper). Sources: https://arxiv.org/html/2511.14993v1, https://arxiv.org/html/2511.14993v2
- Evidence gap: No immutable checkpoint revision/hash for kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers was reported in the inspected model card or model_index.json blobs. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json
- Evidence gap: Checkpoint-scoped numeric benchmark results (dataset names, splits, metrics, numeric values, and experiment conditions) for kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers are not present in the inspected primary sources. Sources: https://arxiv.org/abs/2511.14993, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true

### Safety

- The canonical arXiv preprint (v1 and v2) states the authors deliberately did not implement built-in content-filtering systems and places responsibility on users for ethical and legal use of generated content. Sources: https://arxiv.org/html/2511.14993v1, https://arxiv.org/html/2511.14993v2
- Evidence gap: No checkpoint-scoped privacy, clinical, biosecurity mitigations, or detailed data-handling requirements are published in the inspected repository blobs for this exact checkpoint; downstream deployments requiring such mitigations must perform their own audits. Sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://arxiv.org/abs/2511.14993

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Kandinsky 5.0 T2I Lite SFT — model card

- URL: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Publisher: kandinskylab (Hugging Face model repo)
- Type: `model-card`
- Primary because: Official Hugging Face model repository and model card for the exact checkpoint identifier; contains the checkpoint README and metadata blobs for this checkpoint.
- Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Supports: checkpoint identifier and repository-level README
- Supports: family-level descriptive text about Kandinsky 5.0 Image Lite

### Model model_index.json (model repo blob)

- URL: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json
- Publisher: kandinskylab (Hugging Face model repo files)
- Type: `repository`
- Primary because: model_index.json lists the Diffusers pipeline class and the exact component class names and scheduler for this checkpoint, providing component-level identity for the Diffusers pipeline.
- Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Supports: pipeline class: Kandinsky5T2IPipeline
- Supports: transformer component: Kandinsky5Transformer3DModel
- Supports: VAE component: AutoencoderKL
- Supports: text encoder: Qwen2_5_VLForConditionalGeneration
- Supports: secondary text encoder: CLIPTextModel
- Supports: scheduler: FlowMatchEulerDiscreteScheduler
- Supports: diffusers version reference for the checkpoint

### Model text_encoder README (model repo blob)

- URL: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md
- Publisher: kandinskylab (Hugging Face model repo files)
- Type: `repository`
- Primary because: Repository-level README for the model's text encoder and processor configuration; documents YaRN settings, context-length configuration, and image resize/config parameters used by the checkpoint.
- Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers (text_encoder configuration)
- Supports: text encoder configuration entries including YaRN settings and original_max_position_embeddings
- Supports: processor/tokenizer usage guidance
- Supports: image resizing parameters (min_pixels, max_pixels, resized_height, resized_width) and rounding behavior
- Supports: large-context configuration notes

### Model README (model repo blob)

- URL: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true
- Publisher: kandinskylab (Hugging Face model repo files)
- Type: `repository`
- Primary because: Repository-level README describing the Kandinsky 5.0 family and the Image Lite checkpoint (6B) and intended usage for the checkpoint.
- Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Supports: family and checkpoint descriptive metadata (Image Lite 6B)
- Supports: high-level usage guidance for the checkpoint

### text_encoder config.json (model repo blob)

- URL: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/config.json
- Publisher: kandinskylab (Hugging Face model repo files)
- Type: `repository`
- Primary because: Configuration blob for the checkpoint's text_encoder providing concrete config fields (rope/mrope sections, sliding window sizes, torch_dtype, vision_config parameters) used by the checkpoint.
- Scope: kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers (text_encoder config)
- Supports: text_encoder configuration parameters (rope/mrope, sliding_window, torch_dtype, vision_config details)

### Kandinsky 5.0 paper (arXiv abstract)

- URL: https://arxiv.org/abs/2511.14993
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv abstract/entry for the Kandinsky 5.0 preprint; entry point to the canonical preprint content describing the family.
- Scope: Kandinsky 5.0 family
- Supports: paper metadata and canonical preprint reference for Kandinsky 5.0

### Kandinsky 5.0 paper (arXiv v1 HTML)

- URL: https://arxiv.org/html/2511.14993v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Versioned canonical preprint HTML (v1) containing family-level descriptions, license statement, and limitations.
- Scope: Kandinsky 5.0 family (v1)
- Supports: family-level architecture, limitations, and license statement (MIT)
- Supports: statement that authors did not include built-in content-filtering

### Kandinsky 5.0 paper (arXiv v2 HTML)

- URL: https://arxiv.org/html/2511.14993v2
- Publisher: arXiv
- Type: `paper`
- Primary because: Versioned canonical preprint HTML (v2) containing family-level descriptions and parameter-scale statements.
- Scope: Kandinsky 5.0 family (v2)
- Supports: family-level model lineups and parameter-scale statements
- Supports: family-level descriptions of training and post-training stages

### Diffusers repo commit that added the checkpoint (GitHub commit)

- URL: https://github.com/huggingface/diffusers/commit/d0c54e5563c3245b57d2b374e8e334da77305c05
- Publisher: Hugging Face diffusers (GitHub)
- Type: `repository`
- Primary because: GitHub commit referenced in the findings that documents adding the named kandinskylab checkpoint to the diffusers repository listing (serves as an official implementation-level artifact in the inspected evidence set).
- Scope: Diffusers repository evidence referencing kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Supports: repository-level commit that references addition of the 6B SFT Kandinsky-5.0-T2I-Lite-sft-Diffusers checkpoint

### Exact official starting source declared by Forge

- URL: https://huggingface.co/docs/diffusers/api/pipelines/kandinsky5_image
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: kandinskylab-kandinsky-5-0
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric benchmark results (dataset names, splits, exact metrics, numeric values, and experiment conditions) for kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers were found at the following primary locators checked: https://arxiv.org/abs/2511.14993, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true
- Evidence gap: No immutable checkpoint revision or immutable checksum/hash for kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers was published in these primary blobs: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json
- Evidence gap: Operational runtime metrics (latency, memory usage, GPU requirements, throughput) for this exact Diffusers checkpoint are not published in the inspected primary sources: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/README.md?code=true, https://github.com/huggingface/diffusers/commit/d0c54e5563c3245b57d2b374e8e334da77305c05
- Evidence gap: The inspected primary artifacts do not publish calibrated per-image probabilities, logits, or numeric confidence outputs returned by this checkpoint: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://arxiv.org/abs/2511.14993
- Evidence gap: Exact training-data composition, dataset-level provenance, and per-dataset contribution numbers for the SFT/post-training stages of this exact checkpoint are not reported at these primary locators: https://arxiv.org/abs/2511.14993, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json
- Evidence gap: Precise prompt-engineering templates or special control tokens beyond repository-described processor/encoder usage are not published in the inspected blobs: https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/text_encoder/README.md, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers
- Evidence gap (comparisons): No verified, protocol-matching comparison rows for this exact checkpoint against named alternatives were present in the inspected primary sources. Sources checked: https://arxiv.org/abs/2511.14993, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers, https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers/blob/main/model_index.json

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2] uses forbidden secondary URL https: $.sources[2] uses forbidden secondary URL https://huggingface.co/papers/2511.14993 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/docs/diffusers/api/pipelines/kandinsky5_image: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
