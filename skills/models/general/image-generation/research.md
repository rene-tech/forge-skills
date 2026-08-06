# Image Generation model selection

- Category: `general`
- Group: `image-generation`
- Independent audit: `revised`
- Researched: `2026-07-23T21:28:15.088113+00:00`

Text-to-image and image-editing generation that produce raster image artifacts (PNG/JPG/JPEG) from text prompts and optionally from reference images. Excludes video generation, non-image modalities, and any checkpoint/wrapper other than the exact Forge slugs listed in the expected scope. The dossier is limited to properties and operational metadata that are documented in the supplied research findings primary sources; where a primary source does not specify a property, that property is an evidence gap.

## Questions to answer before selecting

- Do you require explicit NVIDIA NIM-hosted model IDs or NGC container availability for deployment on Forge-managed infrastructure (yes/no)? (Check NIM model listing and NGC container pages in the dossier.)
- Do you require text-only generation, or text+image (image editing / inpainting) support?
- Do you require an explicitly documented target resolution (e.g., native 1024×1024) from the model's primary source?
- Do you require low-diffusion-step / distilled single- or few-step operation (yes/no)?
- Do you require explicit primary-source statements about commercial licensing or 'ready for commercial use' (yes/no)?
- Do you require multilingual/logographic prompt fidelity (e.g., Chinese) documented by the vendor?
- Must the selected model be the exact Forge wrapper variant (Diffusers wrapper, NIM container, or CPU-offload variant) named in the expected scope?

## Comparability rules

- Only compare metrics when the compared entries are the exact same checkpoint/wrapper/versionKey/task head as named in Forge (e.g., a 'diffusers' wrapper variant vs an NIM container variant may not be comparable unless primary sources document equivalence).
- Inference configuration (sampler/algorithm, diffusion steps, guidance scale, scheduler, target resolution/aspect ratio, seed policy, and any postprocessing such as upscaling) must match exactly between runs before comparing numeric metrics; if the primary source omits any of these, mark as evidence gap.
- Compare only models evaluated on the same dataset name and split with the same sample-selection and prompt lists; if the primary source does not document dataset/split/protocol, mark as evidence gap.
- Do not transfer evaluation claims across regimes (base vs SFT vs distilled vs CPU-offload) unless the primary sources explicitly state equivalence.

## Conditional routing

### Prefer `black-forest-labs-flux-2-klein-4b` when I need prompt-driven image editing / inpainting that accepts text+image inputs on Forge single‑GPU-managed variants (interactive editing workflows).

- Why: The Black Forest Labs Hugging Face model card and NIM container entries in the supplied findings document that FLUX.2-klein-4B accepts Text and Image inputs and is published as a Flux.2-klein-4B container; these primary sources provide checkpoint-level evidence of text+image editing capability and Diffusers load instructions.
- Alternative: qwen-qwen-image-edit
- Alternative: black-forest-labs-flux-1-kontext-dev
- Alternative: black-forest-labs-flux-1-dev
- Alternative: black-forest-labs-flux-2-klein-base-4b-diffusers
- Alternative: black-forest-labs-flux-2-klein-4b-diffusers
- Alternative: black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b, https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html

### Prefer `qwen-qwen-image` when I need strong multilingual text rendering and vendor-documented multilingual capability (alphabetic and logographic scripts).

- Why: The Qwen-Image NIM/build entry and the Qwen Hugging Face entry in the supplied findings document Qwen‑Image as a text-to-image foundation model with advanced multilingual text rendering; those primary sources are the available vendor-supplied primary evidence for the multilingual claim.
- Alternative: qwen-qwen-image-edit
- Alternative: stabilityai-stable-diffusion-3-5-large
- Alternative: tongyi-mai-z-image-turbo
- Alternative: black-forest-labs-flux-2-dev-diffusers-bf16
- Evidence: https://build.nvidia.com/qwen/qwen-image, https://huggingface.co/Qwen/Qwen-Image, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit

### Prefer `black-forest-labs-flux-2-klein-4b` when I require an image-generation model that is explicitly listed with NIM model profile IDs and NIM-supported variants for managed deployment on NVIDIA NIM / Forge-managed infrastructure.

- Why: The NVIDIA NIM support matrix and NGC catalog entries in the supplied findings list FLUX.2-klein (model ID black-forest-labs/flux.2-klein-4b) and FLUX.1 variants with minimal/recommended GPU memory and supported precisions; these are the primary NIM/NGC evidence of managed deployment support.
- Alternative: black-forest-labs-flux-1-dev
- Alternative: black-forest-labs-flux-1-kontext-dev
- Alternative: black-forest-labs-flux-1-schnell
- Alternative: qwen-qwen-image
- Alternative: qwen-qwen-image-edit
- Alternative: stabilityai-stable-diffusion-3-5-large
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/black-forest-labs/containers/flux.1-dev/-, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b

### Prefer `insufficient-evidence` when I require a low‑VRAM CPU‑offload Diffusers variant specifically named in Forge (low-GPU-memory/offload runtime).

- Why: The supplied findings include the Hugging Face FLUX.2-klein-4B entry but do not contain a primary-source NIM/NGC or vendor model card that documents an exact Forge-serving slug named black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload; therefore the CPU-offload variant properties for that exact Forge slug cannot be verified from the supplied primary sources.
- Alternative: black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload
- Alternative: black-forest-labs-flux-2-klein-4b-diffusers
- Alternative: black-forest-labs-flux-2-klein-base-4b-diffusers
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B

### Prefer `insufficient-evidence` when I require an explicitly documented distilled / very-low-step single- or few-step operation (e.g., single-step distilled models).

- Why: The supplied findings do not include primary-source benchmark tables or model-card lines that report single-step FID/GenEval numbers for SANA-Sprint or other distilled claims tied to the exact Forge-serving slugs; therefore preference cannot be established from the supplied primary sources.
- Alternative: nvlabs-sana-sprint-1-6b
- Alternative: black-forest-labs-flux-1-schnell
- Alternative: hidream-ai-hidream-i1-fast
- Evidence: https://github.com/NVlabs/Sana, https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard

### Prefer `black-forest-labs-flux-2-klein-4b-diffusers` when I require a Diffusers-hosted vendor model card / Diffusers wrapper variant (Hugging Face Diffusers compatibility) as the canonical primary-source for a candidate.

- Why: The Hugging Face FLUX.2-klein-4B model card in the supplied findings documents Diffusers load instructions (Flux2KleinPipeline) and references bfloat16 usage, supporting the Diffusers-hosted wrapper claim for the HF checkpoint.
- Alternative: black-forest-labs-flux-2-dev-diffusers-bf16
- Alternative: black-forest-labs-flux-2-klein-base-4b-diffusers
- Alternative: black-forest-labs-flux-2-klein-4b
- Evidence: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B

### Prefer `black-forest-labs-flux-1-dev` when I require models that are explicitly listed in the NVIDIA NIM support matrix for minimal system requirements and supported precisions.

- Why: The NIM support matrix in the supplied findings lists minimal and recommended GPU/memory and supported precisions for FLUX.1-dev and FLUX.1-schnell, providing primary-source operational-requirements evidence.
- Alternative: black-forest-labs-flux-1-kontext-dev
- Alternative: black-forest-labs-flux-1-schnell
- Alternative: black-forest-labs-flux-2-klein-4b
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/black-forest-labs/containers/flux.1-dev/-

### Prefer `insufficient-evidence` when I need to decide among models for which no primary-source vendor model card or NIM/NGC serving documentation is present in the supplied findings.

- Why: For several Forge candidate slugs in the expected scope the supplied findings do not contain a canonical primary-source model card, NIM model page, or NGC container page documenting the exact Forge-serving wrapper/checkpoint/versionKey; therefore preference cannot be established from the supplied primary sources.
- Alternative: kandinskylab-kandinsky-5-0-t2i-lite-sft
- Alternative: pixart-alpha-pixart-sigma-xl-2-1024-ms
- Alternative: stabilityai-stable-diffusion-xl-base-1-0
- Alternative: hidream-ai-hidream-i1-fast
- Alternative: tongyi-mai-z-image-turbo
- Alternative: black-forest-labs-flux-2-dev-diffusers-bf16
- Alternative: black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload
- Alternative: black-forest-labs-flux-2-klein-base-4b-diffusers
- Alternative: nvlabs-sana-sprint-1-6b
- Alternative: black-forest-labs-flux-1-schnell
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html

## Benchmark taxonomy

### Photorealistic text-to-image generation (fixed target resolution: 1024×1024 where supported by the model primary source).

- Datasets: Evidence gap: no primary-source dataset/split documented in the supplied findings (e.g., GenEval / DPG-Bench / HPSv2.1 not present in the supplied primary sources for the exact Forge-serving slugs).
- Metrics: Evidence gap: FID (primary-source reported FID not found in the supplied findings for exact Forge slugs), Evidence gap: GenEval score (no primary-source GenEval numbers for exact Forge slugs in the supplied findings), Evidence gap: Human A/B preference (requires primary-source human-study protocol; none found in the supplied findings)
- Compare only when: Exact model wrapper/checkpoint/versionKey must match the Forge slug naming.
- Compare only when: Inference config must match (sampler/algorithm, diffusion steps, guidance scale, seed policy, and any postprocessing). If these are not present in primary sources, report as evidence gap.

### Low-step / distilled high-throughput generation (single-step or few-step distilled operation).

- Datasets: Evidence gap: no primary-source distilled-evaluation dataset/split documented in the supplied findings
- Metrics: Evidence gap: FID with explicit sampling steps (primary-source sampling steps and sampler name not present for distilled claims in supplied findings), Evidence gap: Latency (operational GPU/runtime measurement is Forge metadata and must be separately measured; no primary-source runtime latencies present in the supplied findings for exact Forge-serving slugs)
- Compare only when: Use the exact number of diffusion steps reported by each primary source; if the primary source does not list sampler name or steps, do not compare—mark as evidence gap.

### Image editing / inpainting (text+image conditioning).

- Datasets: Evidence gap: no primary-source common editing benchmark split listed in the supplied findings
- Metrics: Evidence gap: Human A/B edit-fidelity preference (no primary-source human-study protocol in supplied findings), Evidence gap: LPIPS or other perceptual metrics with implementation/version details absent from supplied findings
- Compare only when: Ensure same input image preprocessing, mask semantics, and 'strength' conditioning as defined by the model's primary source; if the primary source omits these, mark as evidence gap.

### Safety & prohibited-content robustness testing (adversarial/prohibited prompts).

- Datasets: Evidence gap: no primary-source adversarial/prohibited-content test suites or splits documented in the supplied findings
- Metrics: Evidence gap: Safety-filter firing rates (requires vendor primary-source filter descriptions; not present in the supplied findings), Evidence gap: Qualitative human adjudication (requires documented protocol; not present in the supplied findings)
- Compare only when: Report the same safety filtering pipeline and thresholds as described in the primary source; if different or unspecified, mark as evidence gap.

## Primary sources

- [NVIDIA NIM Visual GenAI getting-started](https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html) — NVIDIA NIM documentation; supports The FLUX.1-dev container name listed is nvcr.io/nim/black-forest-labs/flux.1-dev:1.2.3., The FLUX.1-Kontext-dev container name is nvcr.io/nim/black-forest-labs/flux.1-kontext-dev:1.1.4., The FLUX.1-schnell container name is nvcr.io/nim/black-forest-labs/flux.1-schnell:1.1.4., The FLUX.2-klein-4B container name is nvcr.io/nim/black-forest-labs/flux.2-klein-4b:1.0.2-variant., The Stable Diffusion 3.5 Large container name is nvcr.io/nim/stabilityai/stable-diffusion-3.5-large:1.1.1.
- [NVIDIA NIM Visual GenAI support matrix (latest)](https://docs.nvidia.com/nim/visual-genai/latest/support-matrix.html) — NVIDIA NIM documentation; supports In the NVIDIA Support Matrix, FLUX.1-dev model ID is black-forest-labs/flux.1-dev and publisher is Black Forest Labs., Minimal system requirements for FLUX.1-dev are 16 GB GPU memory, 40 GB RAM; recommended are 32 GB GPU memory, 64 GB RAM., In the NVIDIA Support Matrix, FLUX.2-klein model ID is black-forest-labs/flux.2-klein-4b and publisher is Black Forest Labs.
- [NGC catalog: FLUX.1-dev container](https://catalog.ngc.nvidia.com/orgs/nim/black-forest-labs/containers/flux.1-dev/-) — NVIDIA NGC (catalog); supports The FLUX.1-dev container houses a collection of generative image AI models creating high quality, realistic images., The FLUX.1-dev container components are ready for non-commercial use., The container version for FLUX.1-dev is nvcr.io/nim/black-forest-labs/flux.1-dev:latest.
- [NGC team container: FLUX.1-Kontext-dev](https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-kontext-dev) — NVIDIA NGC (catalog); supports FLUX.1-Kontext container includes the FLUX.1-Kontext model for changing existing images based on an edit instruction without any finetuning., The container version for FLUX.1-Kontext-dev is nvcr.io/nim/black-forest-labs/flux.1-kontext-dev:latest., FLUX.1-Kontext is not owned or developed by NVIDIA; it was developed by a third party.
- [Build: FLUX.1-schnell (NVIDIA build model page)](https://build.nvidia.com/black-forest-labs/flux_1-schnell) — NVIDIA build (Black Forest Labs hosting); supports FLUX.1-schnell is a distilled image generation model that produces high quality images at fast speeds.
- [NGC team container: FLUX.2-klein-4B](https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.2-klein-4b) — NVIDIA NGC (catalog); supports The FLUX.2-klein-4B container houses Flux.2 [klein] 4B, the fastest Black Forest Labs image model to date., Flux.2 [klein] 4B unifies generation and editing in a single compact architecture and supports multi-reference editing., The FLUX.2-klein-4B container components are ready for commercial and non-commercial use.
- [FLUX.2-klein-4B Hugging Face model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) — Black Forest Labs (Hugging Face model card); supports FLUX.2-klein-4B fits in approximately 13 GB VRAM and is accessible on NVIDIA RTX 3090, RTX 4070, and above., FLUX.2-klein-4B has 4 billion parameters., The FLUX.2-klein-4B model can be loaded with Diffusers via Flux2KleinPipeline.from_pretrained("black-forest-labs/FLUX.2-klein-4B").
- [FLUX.2-dev Hugging Face model card](https://huggingface.co/black-forest-labs/FLUX.2-dev) — Black Forest Labs (Hugging Face model card); supports FLUX.2 [dev] is a 32 billion parameter rectified flow transformer capable of generating, editing, and combining images based on text instructions., FLUX.2 [dev] is available in Diffusers and ComfyUI and has a reference implementation on GitHub.
- [HiDream-I1-Fast Hugging Face model card](https://huggingface.co/HiDream-ai/HiDream-I1-Fast) — HiDream-ai (Hugging Face model card); supports HiDream-I1-Fast achieved an averaged HPSv2.1 benchmark score of 33.82, with category scores: Animation 35.05, Concept‑art 33.74, Painting 33.88, Photo 32.61.
- [HiDream-I1 paper (preprint)](https://arxiv.org/html/2505.22705v1) — arXiv (paper preprint); supports HiDream-I1 has three variants: Full (>50 diffusion steps), Dev (28 diffusion steps), and Fast (14 diffusion steps)., HiDream-I1-Fast, using 14 diffusion steps, is intended for real‑time applications.
- [Kandinsky-5.0 T2I Lite Hugging Face model card](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite) — KandinskyLab (Hugging Face model card); supports Kandinsky 5.0 Image Lite is a lineup of 6 billion parameter image models., Kandinsky 5.0 models support 1K resolution (e.g., 1024×1024).
- [NVlabs Sana GitHub repository](https://github.com/NVlabs/Sana) — NVlabs (GitHub repository); supports Sana is a series of efficient diffusion models for high‑resolution image and video generation., Sana‑1.6B achieves 1.0 samples/s throughput with 1.2 s latency (reported in the supplied findings).
- [PixArt-Sigma-XL-2-1024-MS Hugging Face model card](https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS) — PixArt-alpha (Hugging Face model card); supports PixArt‑Sigma‑XL‑2‑1024‑MS can directly generate 1024 px, 2K, and 4K images from text prompts within a single sampling process.
- [Build: Qwen-Image (NVIDIA build page)](https://build.nvidia.com/qwen/qwen-image) — NVIDIA build (Qwen); supports Qwen‑Image is a text‑to‑image foundation model with advanced multilingual text rendering, supporting English and Chinese scripts., Qwen‑Image input type is text; output type is raster image formats (e.g., png, jpg, jpeg).
- [NGC team container: Qwen-Image-Edit](https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit) — NVIDIA NGC (catalog); supports Qwen‑Image‑Edit is the image editing version of Qwen‑Image, built upon the 20 B Qwen‑Image model.
- [NGC team container: Stable Diffusion 3.5 Large](https://catalog.ngc.nvidia.com/orgs/nim/teams/stabilityai/containers/stable-diffusion-3.5-large) — NVIDIA NGC (catalog); supports Stable Diffusion 3.5 Large is an 8 billion parameter base model that produces high‑quality images and includes Depth and Canny ControlNets for controllability., Stable Diffusion 3.5 Large release dates and NIM packaging are documented in the supplied findings.
- [Build: Stable Diffusion 3.5 Large (NVIDIA build page)](https://build.nvidia.com/stabilityai/stable-diffusion-3_5-large) — NVIDIA build (Stability AI); supports Stable Diffusion 3.5 Large is ready for non‑commercial use; commercial use requires contacting Stability AI (stated in the supplied findings).
- [Z-Image-Turbo Hugging Face model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) — Tongyi-MAI (Hugging Face model card); supports Z‑Image‑Turbo model uses 8 inference steps, provides very high visual quality, and low diversity (as reported in the supplied findings).
- [Qwen-Image Hugging Face model card](https://huggingface.co/Qwen/Qwen-Image) — Qwen (Hugging Face model card); supports Qwen‑Image on HuggingFace demonstrates strong general capabilities in image generation and editing, with exceptional performance in Chinese text rendering.
- [Stable Diffusion 3.5 Large Hugging Face model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) — Stability AI (Hugging Face model card); supports Stable Diffusion 3.5 Large on HuggingFace is a Multimodal Diffusion Transformer (MMDiT) model with improved image quality, typography, complex prompt understanding, and resource efficiency., Stable Diffusion 3.5 Large on HuggingFace is released under the Stability Community License.
- [Stable Diffusion XL Base 1.0 Hugging Face model card](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) — Stability AI (Hugging Face model card); supports Stable Diffusion XL 1.0 base model consists of an ensemble of expert pipelines for latent diffusion, where the base model generates noisy latents that are refined by a separate refinement model.
- [Build: FLUX.1-schnell (NVIDIA build model page) — cited revision/file](https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard) — NVIDIA build (Black Forest Labs hosting); supports Exact audited claim citation
- [Exact official starting source declared by Forge](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://github.com/HiDream-ai/HiDream-I1) — github.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/docs/diffusers/api/pipelines/kandinsky5_image) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/pixart_sigma) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Exact primary-source benchmark tables (FID, GenEval, DPG‑Bench, HPSv2.1) tied to the exact Forge-serving slugs listed are not present in the supplied findings; dataset splits, sample counts, seeds, CLIP/reference model versions, and sampler details are missing for Forge-serving slugs.
- Evidence gap: Exact token limits / maximum text-context window for nearly all Forge slugs are unspecified in the supplied findings.
- Evidence gap: Exact maximum reference image resolution and pixel-dimension hard limits for many Forge slugs (beyond a few HF model-card resolution notes) are not documented in the supplied findings.
- Evidence gap: Exact sampler/scheduler names, diffusion step counts used to produce any primary-source quality metrics, and guidance-scale settings are missing for most Forge-serving slugs in the supplied findings.
- Evidence gap: For the Forge slug black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload there is no primary-source NIM/NGC or vendor model card in the supplied findings documenting that exact Forge-serving wrapper/versionKey.
- Evidence gap: Primary-source statements of commercial licensing or explicit commercial-use permissions for several slugs are not present in the supplied findings (where licensing is referenced, the supplied findings often point to container or support-matrix governance rather than direct model-card license text).
- Evidence gap: Upstream-checkpoint provenance linking NVIDIA-served containers to an upstream Hugging Face or GitHub checkpoint for every Forge slug is incomplete in the supplied findings; some HF entries exist (FLUX.2-klein, FLUX.2-dev), but many Forge-serving slugs lack an explicit mapping in the supplied primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 5 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[22].primary must be true: $.sources[22].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[27].primary must be true: $.sources[27].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://github.com/HiDream-ai/HiDream-I1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/docs/diffusers/api/pipelines/kandinsky5_image: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/pixart_sigma: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
