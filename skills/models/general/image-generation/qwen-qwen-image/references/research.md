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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-qwen-qwen-image-d3119f508b`
- Independent audit: `revised`
- Researched: `2026-07-23T22:33:47.174526+00:00`

This dossier is scoped to the NVIDIA NIM Visual GenAI model entry for Forge slug qwen-qwen-image and the NVIDIA-served Qwen-Image runtime. NVIDIA documentation verifies that the Qwen-Image NIM uses the NIM_MODEL_VERSION selector and defaults to qwen-image-2512 when that variable is unset in the latest getting-started documentation. NVIDIA describes Qwen-Image as a 20B-parameter text-to-image foundation-model family, while upstream-checkpoint evidence supports multilingual complex text rendering and general text-to-image generation, with Apache 2.0 reported for the upstream model. Verified runtime evidence supports deployment via NVIDIA NIM, precision selection, and text-to-image usage boundaries, but the checked primary sources do not provide checkpoint-scoped benchmark tables, exact request/response payload schemas, prompt-length limits, tokenizer details, or post-training calibration metrics for this exact NVIDIA-served scope.

## Identity

- Upstream name: Qwen-Image
- Checkpoint/version: qwen-image-2512
- Immutable revision: not reported
- Parameter scale: Qwen-Image is described by NVIDIA as a family of 20‑billion‑parameter text‑to‑image foundation models; checkpoint-specific parameter count for qwen-image-2512 is not separately reported in the verified sources.
- Architecture/head: NVIDIA-served Qwen-Image is documented as a text-to-image foundation model. Upstream-checkpoint evidence also states that Qwen-Image integrates vision-language encoding with diffusion-based generation.
- License: Upstream checkpoint license: Apache 2.0 is reported for Qwen-Image. NVIDIA container/runtime licensing: NVIDIA NIM containers are governed by the NVIDIA Software License Agreement, Product-Specific Terms for NVIDIA AI Products, and the NVIDIA Open Model License Agreement; the NGC container page also notes commercial and non-commercial readiness. The verified sources do not provide a single reconciled statement mapping model-weight versus container-runtime rights beyond those separate notices.
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://huggingface.co/Qwen/Qwen-Image, https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-, https://build.nvidia.com/qwen/qwen-image/modelcard

## Selection

### Recommended

- **Multilingual text-to-image generation with strong text rendering emphasis** — NVIDIA overview documentation describes Qwen-Image as a text-to-image foundation model with strong capabilities in complex text rendering for English and Chinese, high-resolution output, and versatile styles. The upstream Qwen-Image model card also states strong capabilities in complex text rendering for alphabetic and logographic scripts.
  Scope: NVIDIA-served Qwen-Image default runtime when NIM_MODEL_VERSION is unset (qwen-image-2512), with upstream-checkpoint capability evidence from Qwen-Image.
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://huggingface.co/Qwen/Qwen-Image
- **Self-hosted NVIDIA NIM deployment for Qwen-Image text-to-image inference** — NVIDIA getting-started documentation explicitly documents the Qwen-Image NIM runtime, the NIM_MODEL_VERSION selector, and that the container defaults to qwen-image-2512 when unset.
  Scope: NVIDIA NIM Visual GenAI runtime for Qwen-Image
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html

### Conditional

- **Using alternate precision modes in production deployment** — Only use bf16, fp8, or nvfp4 after validating quality and hardware compatibility in the target deployment, because NVIDIA documents these as supported visual GenAI precisions but does not provide checkpoint-scoped quality tradeoff data here.
  Scope: NVIDIA NIM runtime for Qwen-Image
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- **Generating higher-resolution images within deployment policy controls** — Validate generated-image pixel limits in deployment because NVIDIA documents a configurable maximum number of pixels to generate, but the checked findings do not provide Qwen-Image-specific default values or recommended quality settings for this exact model.
  Scope: NVIDIA NIM Visual GenAI configuration as applied to Qwen-Image runtime
  Evidence: https://docs.nvidia.com/nim/visual-genai/1.6.0/configuration.html

### Avoid

- **Using base Qwen-Image for image-editing workflows that require image inputs** — NVIDIA documents Qwen-Image as a text-to-image foundation-model family, while Qwen-Image-Edit is separately documented as the image-editing family built on Qwen-Image.
  Scope: Base Qwen-Image versus Qwen-Image-Edit family boundary
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://docs.nvidia.com/nim/visual-genai/1.6.0/models.html
- **Deploying the NVIDIA NIM container without guardrails and safety mechanisms** — The NGC Qwen-Image container page states that users are responsible for model inputs and outputs and must implement guardrails and safety mechanisms before deployment.
  Scope: NVIDIA NIM Qwen-Image container/runtime
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-

## Input preparation

### Semantic inputs

- The base Qwen-Image NVIDIA NIM scope is a text-to-image model family, so the supported semantic input is text prompting for image generation. Sources: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://docs.nvidia.com/nim/visual-genai/1.6.0/models.html

### Accepted formats

- Accepted semantic input format for this base model scope is text input; no verified NVIDIA primary source in the checked scope establishes image input for base Qwen-Image. Sources: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://docs.nvidia.com/nim/visual-genai/1.6.0/models.html

### Preprocessing

- Before serving, select the model version through NIM_MODEL_VERSION if a non-default version is desired; otherwise the Qwen-Image NIM defaults to qwen-image-2512 when unset. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- If deploying with precision controls, set precision only among the documented supported visual GenAI precisions bf16, fp8, and nvfp4. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html

### Pre-submit validation

- Validate whether deployment settings attempt unsupported offloading policies, because disk, system_ram, and none offloading policies are documented as not supported by Qwen-Image NIMs. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- For deployment configurations that govern generated image size, validate against the configured maximum number of pixels allowed for generated output images. Sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/configuration.html

### Task-specific formatting

- Use the base Qwen-Image runtime for text-to-image generation tasks; do not transfer the image-input editing contract from Qwen-Image-Edit to base Qwen-Image. Sources: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://docs.nvidia.com/nim/visual-genai/1.6.0/models.html

## Output interpretation

### Outputs

- The model output modality for this Forge model scope is image output from a text-to-image model. Sources: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://build.nvidia.com/qwen/qwen-image/modelcard

### Interpretation

- Interpret outputs as generated images conditioned on text prompts; the verified primary sources do not provide calibrated confidence scores, logits, or uncertainty values for generated images. Sources: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://build.nvidia.com/qwen/qwen-image/modelcard

### Post-inference validation

- Perform human and application-level review of generated outputs before deployment use, because NVIDIA states that users are responsible for model inputs and outputs and must implement guardrails and safety mechanisms. Sources: https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### qwen-qwen-image-edit — `tradeoff`

- Task: Base text-to-image generation versus image-editing workflows
- Criteria: Task specialization and input modality differ: Qwen-Image is documented as text-to-image, while Qwen-Image-Edit is documented as image editing built on Qwen-Image.
- Rationale: Primary NVIDIA sources support a task-boundary comparison, not a numeric head-to-head benchmark. The evidence supports choosing the edit family when image-editing capability is required, and the base family when text-to-image generation is the target task.
- Comparison conditions: Not a matched benchmark protocol; this is a scope and capability comparison derived from NVIDIA family descriptions.
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://docs.nvidia.com/nim/visual-genai/1.6.0/models.html

## Limitations and safety

### Limitations

- The verified primary sources do not report a checkpoint-specific immutable revision for qwen-image-2512 in this NVIDIA-served scope. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://huggingface.co/Qwen/Qwen-Image
- The verified primary sources do not provide exact request payload schema details, prompt templates, tokenizer identity, prompt-length limits, or batching limits for this exact NVIDIA-served Qwen-Image scope. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://build.nvidia.com/qwen/qwen-image/modelcard, https://huggingface.co/Qwen/Qwen-Image
- No checkpoint-scoped public benchmark table with exact dataset, split, metric, and value for qwen-image-2512 was verified in the checked NVIDIA getting-started page, NVIDIA overview/models pages, upstream model card, or arXiv technical report entry. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://huggingface.co/Qwen/Qwen-Image, https://arxiv.org/abs/2508.02324
- The verified sources separate upstream Apache 2.0 model licensing from NVIDIA container/runtime license terms, but do not provide a single authoritative reconciliation of those layers for this packaged deployment scope. Sources: https://huggingface.co/Qwen/Qwen-Image, https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-

### Safety

- Users are responsible for model inputs and outputs and must implement guardrails and safety mechanisms before deployment. Sources: https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-
- Deployment should preserve NVIDIA container license and access-control requirements because NVIDIA NIM containers are governed by NVIDIA license terms distinct from the upstream Apache 2.0 model license. Sources: https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-, https://huggingface.co/Qwen/Qwen-Image

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NIM Visual GenAI getting-started (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA documentation for the exact NIM runtime scope, including Qwen-Image model-version selection and default behavior.
- Scope: NVIDIA NIM Visual GenAI runtime for Qwen-Image and Qwen-Image-Edit
- Supports: identity.checkpoint default behavior when NIM_MODEL_VERSION is unset
- Supports: recommended self-hosted NIM deployment use case
- Supports: input preprocessing and validation for model-version and precision selection
- Supports: runtime limitations and evidence gaps for undocumented request details

### NVIDIA NIM Visual GenAI configuration (1.6.0)

- URL: https://docs.nvidia.com/nim/visual-genai/1.6.0/configuration.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA configuration reference documenting generated-pixel limits and image-count controls relevant to NIM runtime behavior.
- Scope: NVIDIA NIM Visual GenAI configuration surface applicable to Qwen-Image runtime
- Supports: conditional use case for deployment with generated-pixel controls
- Supports: input validation for generated pixel limits

### NVIDIA NIM Visual GenAI models page (1.6.0)

- URL: https://docs.nvidia.com/nim/visual-genai/1.6.0/models.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA model catalog page describing Qwen-Image and Qwen-Image-Edit family task scope and parameter scale.
- Scope: NVIDIA-supported Visual GenAI model families including Qwen-Image and Qwen-Image-Edit
- Supports: identity.parameterScale family statement
- Supports: recommended text-to-image use case
- Supports: avoid-use boundary for editing tasks
- Supports: comparison to Qwen-Image-Edit
- Supports: input semantic scope for base model

### NVIDIA NIM Visual GenAI overview (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA overview page describing Qwen-Image capabilities and Qwen-Image-Edit specialization.
- Scope: NVIDIA Visual GenAI product/model overview for Qwen-Image family
- Supports: identity.parameterScale family statement
- Supports: recommended multilingual text-to-image use case
- Supports: avoid-use boundary for editing tasks
- Supports: comparison to Qwen-Image-Edit
- Supports: output modality and interpretation scope
- Supports: input semantic scope for base model

### Hugging Face model card: Qwen-Image

- URL: https://huggingface.co/Qwen/Qwen-Image
- Publisher: Qwen
- Type: `model-card`
- Primary because: Canonical upstream model card for the Qwen-Image checkpoint family used to preserve upstream-checkpoint capability and license evidence.
- Scope: Upstream Qwen-Image checkpoint family
- Supports: identity.upstreamName
- Supports: identity.license upstream Apache 2.0 layer
- Supports: recommended multilingual text-to-image use case as upstream evidence
- Supports: limitations about missing revision and undocumented tokenizer/prompt details

### Qwen-Image technical report (arXiv abstract)

- URL: https://arxiv.org/abs/2508.02324
- Publisher: arXiv / original study authors
- Type: `technical-report`
- Primary because: Canonical preprint entry for the original Qwen-Image technical report within the allowed primary-source set.
- Scope: Original upstream Qwen-Image technical report scope
- Supports: limitations documenting absence of checkpoint-scoped usable benchmarks in checked primary sources
- Supports: research summary on upstream technical-report inspection

### NGC catalog entry for Qwen-Image container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/qwen/containers/qwen-image/-
- Publisher: NVIDIA NGC
- Type: `repository`
- Primary because: Official NVIDIA NGC container page for the exact packaged Qwen-Image runtime scope.
- Scope: NVIDIA-packaged Qwen-Image NIM container/runtime
- Supports: identity.license NVIDIA container/runtime layer
- Supports: avoid-use boundary requiring guardrails
- Supports: output validation and safety responsibilities
- Supports: commercial/non-commercial readiness note

### Build NVIDIA Qwen-Image model card

- URL: https://build.nvidia.com/qwen/qwen-image/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card page for the Qwen-Image service scope, used here only for directly supported architecture and output-modality statements.
- Scope: NVIDIA Build model card for Qwen-Image
- Supports: identity.architecture upstream-served description
- Supports: output modality and interpretation scope
- Supports: limitations on undocumented request details

## Evidence gaps

- Benchmark evidence gap: after checking https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html (Qwen-Image section), https://huggingface.co/Qwen/Qwen-Image (model card), https://arxiv.org/abs/2508.02324 (technical report abstract page), and https://docs.nvidia.com/nim/visual-genai/latest/overview.html (Qwen-Image overview text), no usable checkpoint-scoped benchmark table, figure, dataset/split, metric, and value for qwen-image-2512 was found.
- Comparison evidence gap: beyond the task-scope comparison against Qwen-Image-Edit, the checked primary sources do not provide matched-protocol head-to-head comparisons between qwen-image-2512 and other Forge peer models in https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://huggingface.co/Qwen/Qwen-Image, or https://arxiv.org/abs/2508.02324.
- Input contract evidence gap: the checked primary sources do not specify exact NVIDIA NIM request payload fields, official prompt templates, tokenizer identity, accepted text length limits, or batching limits for this exact Qwen-Image serving scope.
- Output contract evidence gap: the checked primary sources do not specify exact NVIDIA NIM response object schema, image file encoding details, or per-request image-count defaults for this exact Qwen-Image serving scope.
- Revision evidence gap: the checked primary sources do not report an immutable upstream revision identifier for qwen-image-2512 in this NVIDIA-served scope.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-image-edit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
