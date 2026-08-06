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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-stabilityai-stable-diffusion-3-e2f0f75a5d`
- Independent audit: `revised`
- Researched: `2026-07-23T23:02:34.348126+00:00`

The upstream Hugging Face model card and file tree describe Stable Diffusion 3.5 Large (stabilityai/stable-diffusion-3.5-large) as a Multimodal Diffusion Transformer (MMDiT) text-to-image model released under the Stability AI Community License. The official model file tree lists sd3.5_large.safetensors (16.5 GB) and example decoded output (sd3.5_large_demo.png). I found no publisher-declared immutable checksum (SHA256 or safetensors checksum), no checkpoint tag string (e.g., "1.1.0"), and no parameter-count or checkpoint-scoped dataset benchmark rows in the inspected upstream model card and file tree. A companion repository (stable-diffusion-3.5-large-tensorrt) publishes ONNX/TensorRT exports and repository-level microbenchmarks (BF16 and FP8) with explicit timing rows for 30 steps at 1024×1024; those timings are repository-level artifacts and are not linked in the inspected primary upstream model files to an immutable upstream safetensors checksum.

## Identity

- Upstream name: stabilityai/stable-diffusion-3.5-large
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Multimodal Diffusion Transformer (MMDiT)
- License: Stability AI Community License
- Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main, https://arxiv.org/pdf/2403.03206

## Selection

### Recommended

- **High-quality text-to-image generation for creative media, concept art, and prototyping (single-prompt synthesis).** — The official Hugging Face model card describes the checkpoint as an MMDiT text-to-image model and provides example outputs and usage recommendations for local/self-hosted inference tools.
  Scope: stabilityai/stable-diffusion-3.5-large (upstream model repository and model card)
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- **Performance-oriented inference experiments using ONNX/TensorRT exports provided in the stable-diffusion-3.5-large-tensorrt repository (repository-level optimized inference artifacts).** — The stable-diffusion-3.5-large-tensorrt repository publishes ONNX exports for T5, MMDiT, and VAE components and reports repository-level end-to-end timing profiles for BF16 and FP8 inference flows.
  Scope: stable-diffusion-3.5-large-tensorrt repository exports (repository-level ONNX/TensorRT artifacts; BF16 and FP8 flows)
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md

### Conditional

- **FP8-precision inference using the ONNX/TensorRT artifacts in the stable-diffusion-3.5-large-tensorrt repository.** — Treat timing and numerical-stability claims as repository-level; validate functional parity and numerical stability for your workloads before production use.
  Scope: stable-diffusion-3.5-large-tensorrt repository exports (ONNX/FP8) — repository-level artifacts
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md
- **Local inference and experimentation using the sd3.5_large.safetensors weight file listed in the Hugging Face model tree.** — Obtain and review the Stability AI Community License for commercial/revenue-threshold implications; verify model-weight provenance with the publisher because no immutable checksum was published in the inspected upstream model file tree.
  Scope: stabilityai/stable-diffusion-3.5-large (upstream model file tree)
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/LICENSE.md

### Avoid

- **Clinical or regulated medical decision-making (diagnosis, treatment recommendation).** — Evidence gap: the checked primary sources do not publish checkpoint-scoped clinical validation or regulatory approval documentation for the upstream checkpoint.
  Scope: stabilityai/stable-diffusion-3.5-large (upstream model card and file tree)
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

## Input preparation

### Semantic inputs

- The primary canonical input is a text prompt (string) for text-to-image generation; the model is described as a text-to-image MMDiT. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large

### Accepted formats

- The upstream model card and file tree provide model artifacts and example decoded images (demo PNG), but do not publish a provider-level input-API specification in the inspected locations. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

### Preprocessing

- The Hugging Face model repository file tree lists tokenizer and text_encoder artifacts alongside weights, indicating bundled tokenizer/encoder artifacts are provided. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

### Pre-submit validation

- Evidence gap: the inspected upstream model file tree and model card do not publish an immutable checksum (SHA256 or safetensors checksum) for sd3.5_large.safetensors; verify provenance with the publisher before claiming exact-bit reproducibility. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- Evidence gap: the inspected upstream materials do not document numeric tokenizer token limits or deterministic truncation behavior for the bundled tokenizer/encoder artifacts; validate long-prompt handling empirically prior to production. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

### Task-specific formatting

- Evidence gap: the checked primary sources do not publish a canonical prompt-template or multi-input pairing format for the checkpoint in the inspected locations; apply input formatting per your chosen inference framework. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

## Output interpretation

### Outputs

- The model repository includes example decoded raster-image outputs (e.g., sd3.5_large_demo.png); the upstream artifacts do not publish per-image confidence or probability scores. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

### Interpretation

- Generated images are raw generative samples; no per-sample calibrated confidence or quality scores are provided in the inspected upstream artifacts. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

### Post-inference validation

- Recommended downstream validation: human review for quality and safety/legal compliance because the checked upstream artifacts do not provide automated per-sample legal or safety certifications. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large
- Evidence gap: the checked upstream primary sources do not publish checkpoint-scoped numeric calibration or per-image quality metrics for the checkpoint; build QA pipelines accordingly. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

## Public benchmarks

### inference microbenchmark: end-to-end generation (30 steps) at 1024×1024

- Dataset/split: inference microbenchmark (no dataset) / not reported
- Metric/value: total wall-clock latency (ms) for 30 steps at 1024×1024 / 8101.83 ms (`lower-is-better`)
- Model scope: stable-diffusion-3.5-large-tensorrt repository ONNX/BF16 export (repository-level microbenchmark)
- Conditions: 13.83 ms CLIP‑G + 5.66 ms CLIP‑L + 8.55 ms T5 + 7945 ms for 30 MMDiT steps + 97.17 ms VAE decoder = total 8101.83 ms on NVIDIA H100 using BF16 (as reported in repository README refs/pr/9).
- Source: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md
- Locator: README (refs/pr/9) BF16 timing row
- Caveat: Repository-level microbenchmark reported in the tensorrt repository; the checked sources do not tie this timing to an immutable upstream safetensors SHA.
- Caveat: Not a dataset-scale or perceptual-quality benchmark; measures runtime for a specific step count, resolution, and precision on H100.

### inference microbenchmark: end-to-end generation (30 steps) at 1024×1024

- Dataset/split: inference microbenchmark (no dataset) / not reported
- Metric/value: total wall-clock latency (ms) for 30 steps at 1024×1024 / 5708.69 ms (`lower-is-better`)
- Model scope: stable-diffusion-3.5-large-tensorrt repository ONNX/FP8 export (repository-level microbenchmark)
- Conditions: 16.80 ms CLIP‑G + 6.91 ms CLIP‑L + 8.56 ms T5 + 5604.97 ms for 30 MMDiT steps + 36.91 ms VAE decoder = total 5708.69 ms on NVIDIA H100 using FP8 (as reported in repository README refs/pr/9).
- Source: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md
- Locator: README (refs/pr/9) FP8 timing row
- Caveat: Repository-level microbenchmark reported in the tensorrt repository; the checked sources do not tie this timing to an immutable upstream safetensors SHA.
- Caveat: Not a dataset-scale or perceptual-quality benchmark; measures runtime for a specific step count, resolution, and precision on H100.

## Comparisons

### black-forest-labs-flux-1-dev — `insufficient-evidence`

- Task: text-to-image generation quality and prompt adherence
- Criteria: No checkpoint-scoped, like-for-like numeric benchmark rows or head-to-head comparisons were found in the checked primary sources for SD3.5 Large versus the alternative.
- Rationale: The inspected upstream model card, file tree, and tensorrt repository do not contain matched-protocol benchmark tables or direct comparisons to this alternative.
- Comparison conditions: Checked model card and repository for checkpoint-scoped, matched-protocol comparisons; none were found.
- Evidence: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md

## Limitations and safety

### Limitations

- Evidence gap: No immutable model-weight checksum (SHA256 or safetensors checksum) for sd3.5_large.safetensors was published in the official Hugging Face model file tree inspected. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- Evidence gap: The inspected upstream model card and file tree do not publish checkpoint-scoped dataset benchmark tables or numeric perceptual-quality metrics under matched evaluation protocols. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- Evidence gap: Tokenizer numeric token limits and explicit truncation/default behavior for the bundled tokenizer/encoder artifacts are not documented in the inspected upstream repository locations; validate long-prompt handling empirically. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- Repository-level inference microbenchmarks (BF16/FP8 ONNX exports) are provided in the tensorrt repository but are not explicitly tied in the inspected upstream materials to an immutable upstream safetensors SHA. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- Evidence gap: The inspected upstream materials do not publish decoded-latent tensor shapes or explicit VAE latent dimensionality numeric specifications for the checkpoint. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main

### Safety

- Upstream artifacts do not include checkpoint-scoped clinical validation or regulatory approvals; conservative human-review and domain-specific expert review are recommended for sensitive domains (medical, identifiable-person imagery, PII, defamation). Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large, https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- The Stability AI Community License contains a commercial/revenue-threshold description of permitted commercial use; review the license for obligations prior to commercial deployment. Sources: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/LICENSE.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Stable Diffusion 3.5 Large model card (Hugging Face)

- URL: https://huggingface.co/stabilityai/stable-diffusion-3.5-large
- Publisher: Stability AI (hosted on Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face-hosted model card describing the SD3.5 Large checkpoint and high-level architecture (MMDiT) and usage guidance.
- Scope: stabilityai/stable-diffusion-3.5-large (model card)
- Supports: Model name and high-level architecture claim (MMDiT)
- Supports: Description of the checkpoint as a text-to-image model and usage guidance
- Supports: Absence of an explicit checkpoint tag and absence of an immutable checksum in the inspected card

### SD3.5 Large model file tree (Hugging Face repository tree view)

- URL: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main
- Publisher: Stability AI (hosted on Hugging Face)
- Type: `repository`
- Primary because: Official Hugging Face-hosted model file tree listing weights and example outputs (sd3.5_large.safetensors, sd3.5_large_demo.png) and repository artifacts.
- Scope: stabilityai/stable-diffusion-3.5-large (model file tree)
- Supports: Presence of sd3.5_large.safetensors (file listed with size 16.5 GB)
- Supports: Presence of example output sd3.5_large_demo.png
- Supports: Indication that tokenizer and text_encoder artifacts are bundled in the repository
- Supports: Absence of an immutable checksum published in the inspected file tree

### LICENSE.md for stabilityai/stable-diffusion-3.5-large (Hugging Face repository)

- URL: https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/LICENSE.md
- Publisher: Stability AI (hosted on Hugging Face)
- Type: `official-documentation`
- Primary because: Official license text accompanying the published checkpoint artifact in the upstream model repository.
- Scope: stabilityai/stable-diffusion-3.5-large (LICENSE file)
- Supports: Stability AI Community License wording and definitions of Research, Non-Commercial, and Commercial Purpose

### stable-diffusion-3.5-large-tensorrt repository README (refs/pr/9) (Hugging Face)

- URL: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F9/README.md
- Publisher: Stability AI (hosted on Hugging Face)
- Type: `repository`
- Primary because: Repository providing ONNX/TensorRT exports and repository-level microbenchmarks for SD3.5 Large components; contains explicit timing rows for BF16 and FP8 flows.
- Scope: stable-diffusion-3.5-large-tensorrt (repository refs/pr/9 README)
- Supports: ONNX exports of T5, MMDiT, and VAE in BF16 and MMDiT in FP8
- Supports: Repository-level reported microbenchmark timings for 30 steps at 1024×1024 (BF16 and FP8) with explicit per-component breakdowns

### stable-diffusion-3.5-large-tensorrt repository README (refs/pr/8) (Hugging Face)

- URL: https://huggingface.co/stabilityai/stable-diffusion-3.5-large-tensorrt/blob/refs%2Fpr%2F8/README.md
- Publisher: Stability AI (hosted on Hugging Face)
- Type: `repository`
- Primary because: Repository branch/PR README documenting TensorRT/ONNX implementation details and collaboration context for the optimized implementation.
- Scope: stable-diffusion-3.5-large-tensorrt (repository refs/pr/8 README)
- Supports: Description of the TensorRT-optimized implementation and collaboration context

### ArXiv preprint: Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (arXiv:2403.03206)

- URL: https://arxiv.org/pdf/2403.03206
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint referenced by the model card for architecture-related claims.
- Scope: architectural background relevant to MMDiT/SD3.5
- Supports: Architectural and diffusion-transformer related methods cited in the model card

## Evidence gaps

- Evidence gap: No immutable model-weight checksum (SHA256 or safetensors checksum) for sd3.5_large.safetensors was published in the inspected upstream Hugging Face model file tree.
- Evidence gap: No checkpoint-scoped dataset benchmark rows (dataset name, split, metric, numeric value, and evaluation protocol) were found in the inspected upstream model card or file tree.
- Evidence gap: Tokenizer numeric token limits and explicit truncation/default behavior for the bundled tokenizer/encoder artifacts are not documented in the inspected upstream repository locations.
- Evidence gap: The inspected upstream materials do not publish decoded-latent tensor shapes or explicit VAE latent dimensionality numeric specifications for the checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 24 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://huggingface.co/stabilityai/stable-diffusion-3-medium-diffusers/discussions/22 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses forbidden secondary URL https: $.sources[16] uses forbidden secondary URL https://github.com/Acly/krita-ai-diffusion/discussions/1328 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary host emergentmind.com: $.sources[17] uses forbidden secondary host emergentmind.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses forbidden secondary URL https: $.sources[18] uses forbidden secondary URL https://encord.com/blog/stable-diffusion-3-text-to-image-model Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25].primary must be true: $.sources[25].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.aws.amazon.com/console/sagemaker/ Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/HiDream-ai/HiDream-I1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/api/pipelines/kandinsky5_image Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/Sana Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
