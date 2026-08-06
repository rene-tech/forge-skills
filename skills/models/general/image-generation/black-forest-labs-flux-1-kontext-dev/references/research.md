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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-1-kontex-9e23211569`
- Independent audit: `revised`
- Researched: `2026-07-23T23:00:28.244401+00:00`

Upstream checkpoint evidence available in the Hugging Face repository and the FLUX.1 Kontext technical report shows FLUX.1-Kontext-dev (Hugging Face id black-forest-labs/FLUX.1-Kontext-dev) is a 12B-parameter rectified flow transformer family model intended for multimodal (text+image) in-context image editing and generation. Model weights are published under the FLUX.1 [dev] Non‑Commercial License. NVIDIA documents and NGC/NGC-catalog entries list an NIM container tag nvcr.io/nim/black-forest-labs/flux.1-kontext-dev (examples in v1.4.1 and 'latest') that packages this model for serving; however, an immutable upstream revision identifier (git commit, safetensors checksum, or explicit mapping) connecting the NVIDIA NIM package tag nvcr.io/nim/black-forest-labs/flux.1-kontext-dev:1.1.3 to a specific upstream safetensors/commit was not reported in the inspected authoritative primary sources. The arXiv technical report and upstream repository describe tasks, architecture, and example use (including 1024×1024 examples), but inspected primary sources do not provide per-checkpoint numeric benchmark tables explicitly labeled for the FLUX.1-Kontext-dev checkpoint (see evidence gaps). Where NVIDIA packaging/NGC model cards present runtime or packaging claims, those are reported as packaging/runtime evidence separate from upstream-checkpoint evidence.

## Identity

- Upstream name: FLUX.1 Kontext [dev]
- Checkpoint/version: FLUX.1-Kontext-dev (Hugging Face id: black-forest-labs/FLUX.1-Kontext-dev; referenced by NVIDIA NIM container nvcr.io/nim/black-forest-labs/flux.1-kontext-dev)
- Immutable revision: not reported
- Parameter scale: 12 billion parameters
- Architecture/head: rectified flow transformer (flow-based/flow-matching transformer for image generation/editing)
- License: FLUX.1 [dev] Non‑Commercial License for model weights; repository/inference-code license not reported in inspected primary sources
- Evidence: https://arxiv.org/html/2506.15742v2, https://arxiv.org/abs/2506.15742, https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard, https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4

## Selection

### Recommended

- **Instruction-driven in-context image editing (local inpainting and masked/targeted modification)** — The FLUX.1 Kontext technical report and the upstream Hugging Face model repository describe the model and demonstrate examples and usage patterns oriented to in-context image editing and masked/local edits.
  Scope: FLUX.1-Kontext-dev (upstream checkpoint as published at Hugging Face: black-forest-labs/FLUX.1-Kontext-dev)
  Evidence: https://arxiv.org/html/2506.15742v2, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md
- **Iterative multi-turn edits preserving character and composition consistency (multi-step editing workflows)** — The technical report documents character consistency and multi-turn editing as design goals and evaluation directions; the upstream README and examples describe multi-step editing use patterns.
  Scope: FLUX.1-Kontext-dev (upstream checkpoint as published at Hugging Face)
  Evidence: https://arxiv.org/html/2506.15742v2, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md
- **Text-to-image generation and global style transfer at example generation sizes (e.g., 1024×1024 as used in paper/examples)** — The paper and repository examples demonstrate text-to-image and image-to-image operations at 1024×1024 in reported examples and timing statements.
  Scope: FLUX.1-Kontext-dev (upstream checkpoint as published at Hugging Face)
  Evidence: https://arxiv.org/html/2506.15742v2, https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md

### Conditional

- **Commercial deployment or redistribution** — Requires obtaining separate commercial license/terms from Black Forest Labs; upstream model weights are published under a FLUX.1 [dev] Non‑Commercial License which restricts commercial/production use.
  Scope: FLUX.1-Kontext-dev (upstream checkpoint as published at Hugging Face) and NVIDIA-packaged artifacts referencing that checkpoint
  Evidence: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- **Low‑VRAM inference using vendor-quantized / TensorRT variants** — Use vendor-provided quantized/TensorRT artifacts and validate fidelity/quality for target tasks because quantization/optimizations may alter precision and quality; treat packaging/runtime artifacts as separate artifacts requiring validation.
  Scope: NVIDIA NIM-packaged TensorRT/quantized variants and Hugging Face-hosted NVFP4 quantized repository page associated with FLUX.1-Kontext-dev
  Evidence: https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- **Interactive applications requiring safety filtering** — Implement documented pre/post safety filters and manual review; inspected primary sources describe risk-evaluation and mitigation work but do not publish quantitative false-positive/false-negative operating points, therefore runtime review and validation are required.
  Scope: FLUX.1-Kontext-dev (upstream checkpoint) and Diffusers/hosted integrations used to deploy it
  Evidence: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard

### Avoid

- **Using model outputs to train, fine‑tune, distill, or create a competitive model for commercial/production purposes** — Model weights are distributed under the FLUX.1 [dev] Non‑Commercial License which restricts non‑commercial/non‑production use; redistribution or commercial use requires separate commercial terms from publisher.
  Scope: FLUX.1-Kontext-dev (Hugging Face: black-forest-labs/FLUX.1-Kontext-dev)
  Evidence: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
- **Assuming outputs can be used commercially without obtaining a vendor/publisher commercial license** — Upstream license artifacts and the NVIDIA model card indicate weights are distributed under a Non‑Commercial license and commercial terms must be obtained from publisher for commercial deployment or redistribution.
  Scope: FLUX.1-Kontext-dev (Hugging Face and NVIDIA packaging)
  Evidence: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- **Expecting automatic preservation of input DPI or arbitrary input resolutions without preprocessing** — Upstream documentation and packaging describe supported sizes and example usage but do not publish authoritative guarantees that arbitrary input DPI or arbitrary resolutions are preserved without explicit preprocessing; users should validate preprocessing/resolution behavior.
  Scope: FLUX.1-Kontext-dev (Hugging Face and NVIDIA packaging)
  Evidence: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html

## Input preparation

### Semantic inputs

- The checkpoint accepts multimodal conditioning consisting of a text prompt (string) and an image (2D RGB array) as inputs for editing/generation. Sources: https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev, https://arxiv.org/html/2506.15742v2
- Text prompts are used to express edit instructions, style guidance, and object/character references that condition generation and editing behavior. Sources: https://arxiv.org/html/2506.15742v2, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md

### Accepted formats

- Image inputs and outputs are RGB images; examples and API reference list supported example generation sizes including 1024×1024 used in paper examples. Sources: https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev
- Upstream model repository indicates availability via integrations (e.g., Diffusers/hosted integrations) but does not itself enforce a singular request schema for all runtimes; NVIDIA packaging provides a separate API/interface. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard, https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev

### Preprocessing

- Repository examples and the technical report demonstrate generation at 1024×1024 and show example resizing to model example sizes; explicit low-level resizing/padding algorithmic rules for the upstream checkpoint are not specified in the inspected upstream README or paper. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://arxiv.org/html/2506.15742v2
- NVIDIA packaging and API reference expose runtime-serving input shapes and interfaces which are distinct from upstream repository examples; treat runtime-serving preprocessing behavior as packaging/runtime-specific and validate against NVIDIA docs when using the NIM service. Sources: https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard

### Pre-submit validation

- Confirm rights under the FLUX.1 [dev] Non‑Commercial License before downloading or using weights; obtain commercial terms from the publisher for commercial deployment. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
- When using quantized/vendor-optimized variants, validate image fidelity for target tasks because quantization/optimizations can change precision/quality; treat quantized artifacts as separate artifacts requiring validation. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html

### Task-specific formatting

- For masked edits and inpainting, upstream examples and packaging reference inpaint/masked-editing modes; users should use the inpainting/masked-editing pipeline or runtime mode exposed by the chosen integration or serving interface. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- Loading the upstream checkpoint from the Hugging Face repo is demonstrated in repository README/examples; runtime device placement and pipeline-loading are integration-specific. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md

## Output interpretation

### Outputs

- Primary model output is a generated RGB image at example generation sizes used in paper and examples (1024×1024 cited in upstream examples and technical report). Sources: https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev
- Packaged quantized/TensorRT variants referenced by NVIDIA and a Hugging Face NVFP4 page are alternate inference-weight artifacts intended to reduce VRAM and latency; these artifacts may differ in file size and runtime characteristics from upstream safetensors weights and require fidelity validation. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard

### Interpretation

- No per-output numerical confidence or calibrated probability scores for generated images are published in the inspected upstream model card or technical report; generated images should be treated as model outputs requiring downstream validation and human review for sensitive uses. Sources: https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard

### Post-inference validation

- Apply integrity safety checks and manual review for sensitive or regulated content; upstream README and NVIDIA packaging/model card describe risk-evaluation and mitigation practices but do not publish quantitative FPR/FNR operating points in inspected primary sources. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- When using quantized/vendor-optimized variants, perform fidelity/visual-quality validation because quantization and optimization can trade precision for speed/memory benefits. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: general image generation/editing comparisons vs FLUX.1-dev
- Criteria: No matched dataset/split/metric/protocol published in the inspected arXiv technical report or upstream repository that provides head-to-head numeric comparisons for the exact FLUX.1-Kontext-dev checkpoint and FLUX.1-dev under comparable protocol.
- Rationale: ArXiv and upstream repositories provide family-level descriptions but do not present per-checkpoint matched numeric tables for these exact checkpoints in the inspected primary sources.
- Comparison conditions: Inspected arXiv HTML v2 evaluation descriptions and the Hugging Face model repository for per-checkpoint numeric head-to-head tables; no explicit matched per-checkpoint table located.
- Evidence: https://arxiv.org/html/2506.15742v2, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev

### insufficient-evidence — `insufficient-evidence`

- Task: general image generation/editing comparisons vs HiDream-I1 Fast
- Criteria: No primary matched dataset/protocol was found in inspected FLUX.1 primary sources for direct comparison to HiDream-I1 Fast.
- Rationale: Upstream FLUX.1 documentation focuses on Kontext family evaluation; no per-checkpoint matched numeric comparison tables were found in inspected sources.
- Comparison conditions: Checked arXiv HTML v2, NVIDIA packaging/model card, and Hugging Face model repository for per-checkpoint matched comparisons; none found.
- Evidence: https://arxiv.org/html/2506.15742v2, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev

### insufficient-evidence — `insufficient-evidence`

- Task: general image generation/editing comparisons vs Stable Diffusion variants or other listed peers
- Criteria: No primary matched head-to-head benchmark published in inspected FLUX.1 primary sources for direct comparisons to these peers; upstream FLUX.1 evidence lacks per-checkpoint numeric tables for matched peer comparison in inspected locations.
- Rationale: ArXiv and Hugging Face model docs for FLUX.1-Kontext-dev do not provide required matched numeric head-to-head tables against these peers in inspected locations.
- Comparison conditions: Inspected arXiv HTML v2 and Hugging Face FLUX.1-Kontext-dev repository and NVIDIA packaging; no head-to-head per-checkpoint numeric comparisons found.
- Evidence: https://arxiv.org/html/2506.15742v2, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html

## Limitations and safety

### Limitations

- Model weights are distributed under a FLUX.1 [dev] Non‑Commercial License that restricts use to non-commercial/non-production scenarios; users must obtain commercial terms from the publisher for commercial use. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
- Evidence gap: No per-checkpoint immutable upstream revision identifier (git commit hash, model safetensors checksum, or release tag) mapping the NVIDIA NIM package tag nvcr.io/nim/black-forest-labs/flux.1-kontext-dev:1.1.3 to an immutable upstream artifact was found in the inspected primary sources. Sources: https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main
- Evidence gap: No per-checkpoint numeric metric tables (dataset/split/metric/value) for the FLUX.1-Kontext-dev checkpoint were published in the inspected upstream technical report or repository locations; the arXiv technical report and upstream materials discuss family-level evaluation and example results but do not present per-checkpoint labeled numeric tables for this dev checkpoint in inspected sources. Sources: https://arxiv.org/html/2506.15742v2, https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev
- Quantization and vendor TensorRT/SVDQuant optimizations are provided for inference/runtime (packaged by NVIDIA and referenced by an upstream NVFP4 page); these optimizations can alter VRAM usage, speed, and may introduce fidelity/precision tradeoffs requiring user validation. Sources: https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4
- Evidence gap: The inspected primary sources do not publish quantitative false-positive/false-negative operating points or numeric detection-performance metrics for pre/post safety filters or any integrity checker described in upstream safety notes. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- Evidence gap: The inspected upstream repository and model card do not report an explicit license file for inference code or inference scripts (e.g., an Apache-2.0 license for code) in the inspected file locations. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev

### Safety

- Upstream license and repository documentation require acceptance of the FLUX.1 [dev] Non‑Commercial License terms for weights and impose content-use obligations; commercial licensing must be obtained from publisher. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
- Diffusers/hosted integrations and the upstream README reference risk-evaluation and recommend implementing pre/post filters and integrity checks for deployed applications; however, inspected primary sources do not publish quantitative error rates for these mitigations. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- Packaged quantized/runtime variants exist and are intended for inference; users must perform provenance and fidelity validation and adhere to license restrictions when deploying those artifacts. Sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4, https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### ArXiv HTML v2 of FLUX.1 Kontext

- URL: https://arxiv.org/html/2506.15742v2
- Publisher: arXiv
- Type: `technical-report`
- Primary because: Canonical arXiv HTML preprint used to inspect architecture, task descriptions, and example evaluation descriptions for FLUX.1 Kontext.
- Scope: FLUX.1 Kontext technical report (HTML v2)
- Supports: identity.architecture
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs

### ArXiv abstract page for FLUX.1 Kontext

- URL: https://arxiv.org/abs/2506.15742
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv abstract/preprint identifier for the FLUX.1 Kontext technical report.
- Scope: FLUX.1 Kontext technical report (abs)
- Supports: identity.architecture
- Supports: researchSummary

### ArXiv PDF (v2) of FLUX.1 Kontext

- URL: https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf
- Publisher: arXiv
- Type: `technical-report`
- Primary because: Canonical PDF used to confirm architecture, example resolutions, and example timings.
- Scope: FLUX.1 Kontext technical report (PDF v2)
- Supports: identity.architecture
- Supports: researchSummary
- Supports: inputPreparation.acceptedFormats
- Supports: outputInterpretation.outputs

### Hugging Face model page: FLUX.1-Kontext-dev

- URL: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev
- Publisher: Black Forest Labs (Hugging Face model repository)
- Type: `repository`
- Primary because: Canonical upstream model repository entry for the dev checkpoint, used to confirm checkpoint identifier, README, and repository metadata.
- Scope: FLUX.1-Kontext-dev (Hugging Face)
- Supports: identity
- Supports: inputPreparation
- Supports: recommendedUseCases
- Supports: limitations
- Supports: safety

### Hugging Face model tree (repository files and safetensors)

- URL: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main
- Publisher: Black Forest Labs (Hugging Face repo)
- Type: `repository`
- Primary because: Repository file listing used to confirm presence of weight artifacts and repository structure.
- Scope: FLUX.1-Kontext-dev repository artifacts
- Supports: identity
- Supports: inputPreparation.taskSpecificFormatting

### Hugging Face model README (repository README present in repo)

- URL: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md
- Publisher: Black Forest Labs (Hugging Face repo)
- Type: `official-documentation`
- Primary because: Canonical README in the upstream model repository used to support usage examples, safety notes, and integration statements.
- Scope: FLUX.1-Kontext-dev README
- Supports: inputPreparation
- Supports: recommendedUseCases
- Supports: outputInterpretation
- Supports: safety

### Hugging Face LICENSE.md for FLUX.1-Kontext-dev

- URL: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md
- Publisher: Black Forest Labs (Hugging Face repo)
- Type: `official-documentation`
- Primary because: Canonical license text for the dev checkpoint as published in the upstream repository.
- Scope: FLUX.1-Kontext-dev license
- Supports: identity.license
- Supports: limitations
- Supports: safety

### Black Forest Labs GitHub: LICENSE-FLUX1-dev

- URL: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
- Publisher: Black Forest Labs (GitHub)
- Type: `repository`
- Primary because: Publisher-hosted license file referenced by the model project; used to confirm model-weight license presence.
- Scope: FLUX.1 [dev] model license (GitHub)
- Supports: identity.license
- Supports: limitations
- Supports: safety

### Hugging Face quantized variant repository: FLUX.1-Kontext-dev-NVFP4

- URL: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4
- Publisher: Black Forest Labs (Hugging Face repo)
- Type: `repository`
- Primary because: Upstream-hosted quantized variant page referenced for quantized artifact evidence.
- Scope: Quantized NVFP4 variant of FLUX.1-Kontext-dev
- Supports: conditionalUseCases
- Supports: limitations
- Supports: outputInterpretation

### Hugging Face NVFP4 README (quantized variant)

- URL: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev-NVFP4/blob/main/README.md
- Publisher: Black Forest Labs (Hugging Face repo)
- Type: `official-documentation`
- Primary because: Quantized variant README used to confirm presence of NVFP4 artifacts and reference to main repository.
- Scope: FLUX.1-Kontext-dev NVFP4 README
- Supports: identity
- Supports: conditionalUseCases

### NVIDIA NIM / NGC container listing and packaging notes (visual-genai NIM getting-started v1.4.1)

- URL: https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: NVIDIA NIM documentation listing the NIM container tag and packaging notes for FLUX.1-Kontext-dev used to corroborate packaging/runtime evidence.
- Scope: NGC container packaging for flux.1-kontext-dev (v1.4.1 docs)
- Supports: identity.evidenceUrls
- Supports: conditionalUseCases
- Supports: limitations
- Supports: outputInterpretation

### NVIDIA NIM / visual-genai getting-started (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Latest NVIDIA NIM documentation referencing the packaged NIM and container versions; used as packaging/runtime evidence.
- Scope: NGC/NIM packaging and versioning notes (latest)
- Supports: identity.evidenceUrls
- Supports: conditionalUseCases

### NVIDIA API reference for black-forest-labs-flux_1-kontext-dev

- URL: https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev
- Publisher: NVIDIA API documentation
- Type: `official-documentation`
- Primary because: NVIDIA API reference listing input types (Text, Image) and model capabilities; used as packaging/runtime API evidence separate from upstream checkpoint claims.
- Scope: NGC/NIM API reference for flux_1-kontext-dev
- Supports: inputPreparation.semanticInputs
- Supports: identity
- Supports: conditionalUseCases
- Supports: outputInterpretation.outputs

### NVIDIA build model card: FLUX.1 Kontext (NGC/modelcard)

- URL: https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard
- Publisher: NVIDIA build site
- Type: `model-card`
- Primary because: Vendor-hosted model card used to corroborate packaging/runtime testing details and to separate packaging evidence from upstream checkpoint.
- Scope: NGC-packaged model card for flux.1-kontext-dev
- Supports: identity
- Supports: researchSummary
- Supports: conditionalUseCases
- Supports: safety
- Supports: outputInterpretation

### NGC catalog entry for flux.1-kontext-dev

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-kontext-dev
- Publisher: NGC catalog (NVIDIA)
- Type: `official-documentation`
- Primary because: NGC catalog entry describing the NIM container for FLUX.1-Kontext-dev and its feature descriptions used to corroborate container naming and feature claims.
- Scope: NGC catalog entry for flux.1-kontext-dev
- Supports: identity
- Supports: researchSummary
- Supports: conditionalUseCases

### NVIDIA NIM release notes (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/release-notes.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Release notes used to corroborate NIM support and packaging/version history references for the model.
- Scope: NGC/NIM release notes (latest)
- Supports: conditionalUseCases
- Supports: limitations

## Evidence gaps

- Evidence gap: No per-checkpoint immutable upstream revision identifier (git commit hash, model safetensors checksum, or release tag) mapping the NVIDIA NIM package version nvcr.io/nim/black-forest-labs/flux.1-kontext-dev:1.1.3 to an immutable upstream artifact was found in the inspected authoritative primary sources. Inspected: NVIDIA NIM getting-started v1.4.1 (https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html), NVIDIA build model card (https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard), and Hugging Face repository tree (https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main) — no explicit immutable upstream revision mapping to the NIM tag was reported in these sources.
- Evidence gap: No per-checkpoint numeric benchmark tables (dataset / split / metric / value) explicitly labeled for the FLUX.1-Kontext-dev checkpoint were found in the inspected canonical primary sources. Inspected: ArXiv HTML v2 (https://arxiv.org/html/2506.15742v2) and ArXiv PDF v2 (https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf) and the Hugging Face model page (https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev) — evaluation descriptions and family-level examples are present but no per-checkpoint numeric tables explicitly attributed to the dev checkpoint were located in these inspected sections.
- Evidence gap: No canonical numeric latency/throughput benchmark tables under a reproducible protocol for the upstream checkpoint were published in the inspected primary sources; NVIDIA packaging/model card and arXiv provide qualitative or example timing statements but not a reproducible numeric throughput table for the upstream checkpoint. Inspected: ArXiv HTML v2 (https://arxiv.org/html/2506.15742v2), ArXiv PDF v2 (https://arxiv-dataset.storage.googleapis.com/arxiv/arxiv/pdf/2506/2506.15742v2.pdf), and NVIDIA documents (https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html, https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard).
- Evidence gap: No published quantitative false-positive/false-negative operating points or numeric detection-performance metrics for upstream safety mitigations (pre/post filters or integrity checker) were found in the inspected primary sources. Inspected: Hugging Face README (https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md) and NVIDIA build model card (https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard) — safety mitigations are described qualitatively but operating-point metrics are not published.
- Evidence gap: The inspected primary sources do not report an explicit inference-code or repository code license (for example, an Apache-2.0 inference-code license) in the repository locations inspected; only the FLUX.1 [dev] Non‑Commercial model-weight license is directly evidenced. Inspected: Hugging Face repository tree (https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/tree/main) and GitHub model_licenses path (https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev).
- Evidence gap: No authoritative upstream Diffusers pipeline documentation or exact pipeline argument/formatting table for the FLUX.1-Kontext-dev checkpoint was found in inspected canonical primary sources; users should consult integration docs at the chosen integration/runtime and validate formatting. Inspected: Hugging Face README (https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md) and NVIDIA documentation (https://docs.nvidia.com/nim/visual-genai/1.4.1/getting-started.html) — explicit Diffusers API argument tables for this checkpoint were not present in these inspected locations.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 38 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://bfl.ai/blog/flux-1-kontext-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://blogs.nvidia.com/blog/rtx-ai-garage-flux-kontext-nim-microservice-siggraph Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20].primary must be true: $.sources[20].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21] uses forbidden secondary URL https: $.sources[21] uses forbidden secondary URL https://developer.nvidia.com/blog/optimizing-flux-1-kontext-for-image-editing-with-low-precision-quantization Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[22] uses forbidden secondary URL https: $.sources[22] uses forbidden secondary URL https://bfl.ai/blog/flux-1-kontext Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24] uses forbidden secondary URL https: $.sources[24] uses forbidden secondary URL https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/discussions/6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24].primary must be true: $.sources[24].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://kie.ai/features/flux-1-kontext-dev-api Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://kie.ai/features/flux-1-kontext-dev-api Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-Dev/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-Dev/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-dev/discussions/43 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-Dev/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://kie.ai/features/flux-1-kontext-dev-api Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-Dev/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-Dev/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].value must contain a reported numeric result: $.benchmarks[0].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].value must contain a reported numeric result: $.benchmarks[1].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
