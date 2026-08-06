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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-2-klein-92a9193a26`
- Independent audit: `revised`
- Researched: `2026-07-23T22:25:27.637237+00:00`

I verified the NGC/NIM container listing and the upstream Hugging Face repository files included in the research findings. The named upstream artifact is black-forest-labs/FLUX.2-klein-4B (model repo and model_index.json show pipeline and component classes). The model is described in primary sources as a 4B‑parameter rectified‑flow/flow‑matching diffusion transformer (Flux2Transformer2DModel) with a Qwen‑family text encoder/tokenizer component and an AutoencoderKLFlux2 VAE; the repository contains an Apache‑2.0 LICENSE.md for the klein‑4B repo. The NGC container listing documents an nvcr.io NIM container for flux.2-klein-4b that packages the model for NVIDIA runtime; NGC states the container houses the klein 4B model, supports multi‑reference editing, and recommends safety guardrails. I did not find any file‑level upstream ↔ NIM binary provenance (checksum/commit mapping) in the checked primary URLs, nor did I find dataset‑anchored numeric benchmark tables for the exact klein‑4B checkpoint in the checked primary model or NIM pages. Several runtime and implementation details (exact tokenizer/vocab artifacts applied at serving time, numeric image preprocessing constants, explicit per‑pixel output numeric ranges, explicit batching limits) are not specified in the inspected primary files; I record precise evidence gaps pointing to the exact URLs/paths I checked.

## Identity

- Upstream name: black-forest-labs/FLUX.2-klein-4B
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 4B
- Architecture/head: Rectified‑flow / flow‑matching diffusion transformer backbone (Flux2Transformer2DModel) combined with a vision‑language/text encoder component (Qwen3ForCausalLM) and associated VAE; scheduler: FlowMatchEulerDiscreteScheduler
- License: Apache-2.0 (as present in the repository LICENSE.md for the FLUX.2‑klein‑4B model)
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/transformer/config.json, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/model_index.json, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

## Selection

### Recommended

- **Text-to-image generation (creative and photorealistic)** — Primary model repository and NGC container listing describe text‑to‑image as a supported mode and show a pipeline and text encoder components that implement text conditioning.
  Scope: black-forest-labs/FLUX.2-klein-4B (upstream model repository) and the NIM container that houses it
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/model_index.json
- **Image-to-image editing and multi-reference image conditioning (inpainting, style transfer, object manipulation)** — The NGC container listing and the upstream model page describe multi‑reference editing capability and image editing/generation support; model_index.json lists pipeline and VAE components appropriate for image editing workflows.
  Scope: black-forest-labs/FLUX.2-klein-4B (upstream) and the NIM container packaging
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/model_index.json
- **Low‑latency consumer‑GPU inference workflows (memory‑constrained deployments)** — The upstream model page and NGC listing report that the klein‑4B variant fits in approximately 13 GB VRAM and that the NIM container targets low‑latency, sub‑second inference; NGC packaging documents offloading/runtime options to support constrained GPU memory.
  Scope: black-forest-labs/FLUX.2-klein-4B as packaged in the NIM container nvcr.io/nim/black-forest-labs/flux.2-klein-4b
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

### Conditional

- **Commercial deployment without additional safety mitigations** — The NGC container components are listed as ready for commercial and non‑commercial use but the NIM container is governed by NVIDIA Software License Agreement and Product‑Specific Terms; deployers must ensure compliance with NVIDIA terms and implement content filtering and access controls as recommended.
  Scope: NIM container nvcr.io/nim/black-forest-labs/flux.2-klein-4b (as listed on NGC) and upstream repository
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- **Use in sensitive domains (medical, legal, forensic) requiring domain validation** — Primary sources do not publish domain‑specific safety calibration or clinical validation; domain expert review and additional validation are required before use in sensitive contexts.
  Scope: black-forest-labs/FLUX.2-klein-4B (upstream) and the NIM container
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

### Avoid

- **Generation of child sexual abuse material (CSAM) or non‑consensual intimate imagery (NCII)** — Upstream model card states Black Forest Labs evaluated and mitigated risks including CSAM and NCII and recommends preservation of mitigations and safety controls; deployers must avoid uses that attempt to circumvent those mitigations.
  Scope: black-forest-labs/FLUX.2-klein-4B (upstream model card) and NIM container packaging
  Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

## Input preparation

### Semantic inputs

- Accepted input modalities are text prompts and reference images (multi‑reference conditioning is described in primary sources). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

### Accepted formats

- Primary sources describe raster image inputs/outputs and VAE decoding to standard image file formats (PNG, JPG/JPEG) for produced images. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Example runtime/app code enforces a MAX_IMAGE_SIZE of 1024 for the provided Spaces app. Sources: https://huggingface.co/spaces/black-forest-labs/FLUX.2-klein-4B/blob/main/app.py

### Preprocessing

- Primary repository and NGC container pages do not publish exact numeric image preprocessing transforms (resize interpolation, per‑channel mean/std normalization, pixel value scaling). Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/transformer/config.json
- Example Spaces app code sets runtime dtype to torch.bfloat16 and selects device='cuda' if available; MAX_IMAGE_SIZE and MAX_SEED constants are defined in the app example. Sources: https://huggingface.co/spaces/black-forest-labs/FLUX.2-klein-4B/blob/main/app.py

### Pre-submit validation

- Primary sources do not publish explicit batching limits, maximal batch size, or per‑request dimension/channel validation rules for the NIM container or upstream model artifact in the checked files. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Model repository includes model_index.json and transformer config but does not include an explicit tokenizer/vocabulary file mapping for klein‑4B at the inspected paths; tokenizer class name (Qwen2TokenizerFast) appears in model_index.json but explicit tokenizer artifact/files were not verified in the inspected paths. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/model_index.json, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/transformer/config.json

### Task-specific formatting

- Primary model card and repository assert multi‑reference conditioning capability but do not provide a canonical prompt template or exact paired‑input ordering for multi‑reference conditioning in the inspected files. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b
- Transformer config file documents Flux2Transformer2DModel parameters for the diffusion transformer but does not specify explicit tokenization parameters for image/text conditioning at the inspected path. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/transformer/config.json

## Output interpretation

### Outputs

- Model produces raster images via VAE decoding into standard image file formats (PNG/JPG) as described in primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B

### Interpretation

- Primary sources do not specify numeric per‑pixel output ranges or explicit denormalization/clipping steps in the inspected files; treat pixel numeric semantics as unspecified unless downstream code documents them. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

### Post-inference validation

- Primary sources do not provide automated post‑inference quality checks or a published calibration metric for generated images; authors and NGC documentation recommend human review and downstream safety filtering. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### black-forest-labs-flux-1-dev — `insufficient-evidence`

- Task: Text-to-image / image editing (general)
- Criteria: No primary‑source, same‑protocol head‑to‑head evaluation table or dataset/split anchored numeric comparison between FLUX.2‑klein‑4B and the FLUX.1 family artifact was found in the inspected primary pages.
- Rationale: I checked the upstream FLUX.2 klein model page and the NGC container listing for named head‑to‑head numeric comparisons and found none; therefore a protocol‑matched comparison is not supported by the inspected primary sources.
- Comparison conditions: Checked the Hugging Face model card and the NGC container listing for protocol‑matched numeric evaluations; none were present.
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

## Limitations and safety

### Limitations

- Primary sources recommend implementing content filtering, abuse monitoring, and access controls because the model can generate inaccurate, offensive, or otherwise inappropriate content; deployers should apply robust safety guardrails. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- FLUX.2‑klein‑4B upstream repository contains an Apache‑2.0 LICENSE.md describing the Apache License Version 2.0 terms for that repository; license statements for other family variants (e.g., any 9B variant) are not present in the inspected files. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md
- Evidence gap: The inspected primary sources did not contain an explicit file‑level checksum, commit hash, or release tag that maps the NIM/NGC container binary to a specific Hugging Face checkpoint file; I checked the NGC container listing page and the upstream Hugging Face model repository paths. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B

### Safety

- Implement conservative safety measures (content filtering, abuse monitoring, access control, and human review) when deploying FLUX.2‑klein‑4B; primary sources explicitly recommend such guardrails. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Primary sources state Black Forest Labs evaluated and mitigated risks including CSAM and NCII prior to release; operators should preserve and enforce those mitigations. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Evidence gap: The inspected primary files do not publish domain‑specific safety calibration procedures or clinical validation protocols required for medical/legal/forensic deployments. Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: FLUX.2-klein-4B

- URL: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Publisher: Black Forest Labs (Hugging Face model page host)
- Type: `model-card`
- Primary because: Official upstream model repository and model card for FLUX.2‑klein‑4B; contains overview, safety statements, and links to repository files used in this dossier.
- Scope: black-forest-labs/FLUX.2-klein-4B (upstream model card and repository root)
- Supports: identity.upstreamName
- Supports: recommendedUseCases
- Supports: avoidUseCases
- Supports: safety
- Supports: outputInterpretation.outputs
- Supports: inputPreparation.semanticInputs

### Hugging Face repository: FLUX.2-klein-4B transformer config

- URL: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/transformer/config.json
- Publisher: Black Forest Labs (Hugging Face repository file)
- Type: `repository`
- Primary because: Transformer configuration file published in the official repository documenting Flux2Transformer2DModel parameters and diffusion configuration elements.
- Scope: transformer/config.json in black-forest-labs/FLUX.2-klein-4B
- Supports: identity.architecture
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.interpretation

### Hugging Face repository: FLUX.2-klein-4B LICENSE file

- URL: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md
- Publisher: Black Forest Labs (via Hugging Face)
- Type: `repository`
- Primary because: Canonical LICENSE.md file present in the official model repository documenting Apache License Version 2.0 for the klein‑4B repository.
- Scope: LICENSE.md in black-forest-labs/FLUX.2-klein-4B
- Supports: identity.license
- Supports: limitations

### Hugging Face repository: FLUX.2-klein-4B model_index.json

- URL: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/model_index.json
- Publisher: Black Forest Labs (via Hugging Face repository)
- Type: `repository`
- Primary because: Model index file documents pipeline class, required diffusers version, scheduler, text encoder, tokenizer, transformer, and VAE components used by the model.
- Scope: model_index.json in black-forest-labs/FLUX.2-klein-4B
- Supports: identity.architecture
- Supports: inputPreparation.semanticInputs
- Supports: recommendedUseCases

### Hugging Face Spaces app: FLUX.2-klein-4B (app.py)

- URL: https://huggingface.co/spaces/black-forest-labs/FLUX.2-klein-4B/blob/main/app.py
- Publisher: Black Forest Labs (Spaces repository)
- Type: `repository`
- Primary because: Published example application code showing runtime dtype, device selection, MAX_IMAGE_SIZE, and MAX_SEED constants used in the example app.
- Scope: Spaces example app code for FLUX.2-klein-4B (app.py)
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation.outputs

### NGC catalog: flux.2-klein-4b container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NGC/NGC catalog listing for the NIM container that packages the FLUX.2‑klein‑4B model for NVIDIA runtimes; documents container scope, recommended guardrails, and runtime packaging details.
- Scope: NIM/NGC container nvcr.io/nim/black-forest-labs/flux.2-klein-4b
- Supports: identity.parameterScale
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: limitations
- Supports: safety

## Evidence gaps

- Evidence gap: No file‑level checksum, commit hash, release tag, or explicit mapping proving binary equivalence between the NIM container (https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b) and a specific Hugging Face checkpoint file was found at the inspected URLs.
- Evidence gap: The inspected upstream repository files and the NGC container listing do not publish dataset‑anchored numeric benchmark tables (metric name, dataset/split, checkpoint tag) for the exact klein‑4B checkpoint; I checked the model card main page (https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) and the NGC container listing (https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b).
- Evidence gap: Exact tokenizer artifact files (tokenizer vocab files) applied at serving time were not found at the inspected repository paths; model_index.json lists tokenizer class name Qwen2TokenizerFast (https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/model_index.json) but explicit tokenizer/vocab file paths were not verified in the inspected files.
- Evidence gap: Primary sources inspected (transformer config, model_index.json, app.py) do not specify precise numeric image preprocessing constants (resize interpolation algorithm, per‑channel mean/std normalization, pixel scaling or channel ordering). Files checked include https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/transformer/config.json and https://huggingface.co/spaces/black-forest-labs/FLUX.2-klein-4B/blob/main/app.py.
- Evidence gap: Primary sources inspected do not specify explicit per‑pixel numeric output range semantics (uint8 0–255 vs float 0–1) or explicit postprocessing denormalization steps; checked files include https://huggingface.co/black-forest-labs/FLUX.2-klein-4B and https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b.
- Evidence gap: No authoritative public primary‑source statement was found in the inspected files regarding licensing for other FLUX.2 variants (for example a 9B variant); the klein‑4B repository contains an Apache‑2.0 LICENSE.md (https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md) but I did not find a primary‑source license file for a 9B variant in the inspected URLs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 21 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://inferencebench.io/blog/flux2-klein-4b-image-generation-benchmark Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-nvfp4/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B/discussions/2/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary URL https: $.sources[15] uses forbidden secondary URL https://developer.nvidia.com/blog/scaling-nvfp4-inference-for-flux-2-on-nvidia-blackwell-data-center-gpus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary URL https: $.sources[17] uses forbidden secondary URL https://inferencebench.io/blog/flux2-klein-4b-image-generation-benchmark Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/HiDream-ai/HiDream-I1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/pixart_sigma Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
