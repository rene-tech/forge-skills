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

- Research key: `huggingface-co-stabilityai-stable-video-diffusion-img2vid-xt-d9acf75eb0`
- Independent audit: `revised`
- Researched: `2026-08-06T13:58:14.877261+00:00`

Primary repository and model-card evidence show a checkpoint file named svd_xt.safetensors with reported file size 9,559,625,980 bytes and SHA256 b2652c23d64a1da5f14d55011b9b6dce55f2e72e395719f1cd1f8a079b00a451 (blob blame locator). The Hugging Face model page and the repository README describe the SVD family as image-conditioned image-to-video latent diffusion models and explicitly document SVD‑XT as fine-tuned to produce 25 frames at 576×1024; the repository/readme also state the original SVD variant was trained for 14 frames. The checked primary sources do not report an exact parameter count for the svd_xt.safetensors checkpoint, do not contain checkpoint-scoped numeric benchmark table rows tied to svd_xt.safetensors, do not document emitted per-frame calibrated confidence/probability scores or explicit per-frame metadata fields, and do not specify a container/codec format used by any official demo/pipeline for generated videos; these items are recorded as evidence gaps. The arXiv preprint for Stable Video Diffusion (arXiv:2311.15127) is included as upstream-family documentation in the checked set but does not provide checkpoint-scoped numeric rows for svd_xt.safetensors in the checked primary sources.

## Identity

- Upstream name: Stable Video Diffusion XT (SVD-XT)
- Checkpoint/version: svd_xt.safetensors
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Latent diffusion image-to-video model (SVD family); repository and model-card describe a generative image-to-video latent diffusion checkpoint (image-conditioned img2vid).
- License: not reported
- Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blame/0fa137231bc6717ea4551951b2a942c46cf50051/svd_xt.safetensors, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md, https://arxiv.org/abs/2311.15127

## Selection

### Recommended

- **Image-to-video generation (short clips conditioned on a single input image)** — The official Hugging Face model page and the repository README describe the released SVD and SVD‑XT checkpoints as image-conditioned img2vid latent diffusion models and explicitly document SVD‑XT as fine‑tuned to produce 25 frames at 576×1024.
  Scope: svd_xt.safetensors (stabilityai/stable-video-diffusion-img2vid-xt repository)
  Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Conditional

- **Text-to-video synthesis using SVD-family methods** — The checked primary sources document image-conditioned img2vid capabilities for the SVD family and explicitly describe SVD‑XT as image-conditioned; the checked primary sources do not provide checkpoint-scoped documentation that svd_xt.safetensors supports text conditioning. Verify checkpoint-scoped documentation before treating svd_xt.safetensors as text-conditioned.
  Scope: Family-level (SVD/SVD‑XT) wording in model card/README vs. svd_xt.safetensors checkpoint (repository evidence documents image conditioning primarily).
  Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Avoid

- **Long-duration video generation substantially beyond the checkpoint's fine-tuned frame count (e.g., >>25 frames)** — Repository/model-card statements document SVD trained for 14 frames and SVD‑XT fine‑tuned to 25 frames; there is no checkpoint-scoped canonical evidence in the checked primary sources that svd_xt.safetensors supports coherent generation of substantially longer sequences without further fine‑tuning or architectural extension.
  Scope: svd_xt.safetensors (stabilityai/stable-video-diffusion-img2vid-xt repository)
  Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- **Relying on emitted per-frame calibrated confidence/probability scores from the checkpoint or demo pipeline** — The checked primary sources (model page and README) do not document emission of calibrated per-frame confidence/probability scores or explicit per-frame metadata fields emitted by the checkpoint or demo code.
  Scope: svd_xt.safetensors (stabilityai/stable-video-diffusion-img2vid-xt repository)
  Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

## Input preparation

### Semantic inputs

- Primary conditioning input documented is a single still image used as the context frame for image-to-video synthesis. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Accepted formats

- Repository and model page describe generation at resolution 576×1024 and document SVD‑XT producing 25 frames at 576×1024. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Preprocessing

- Repository-level wording identifies SVD and SVD‑XT as image-conditioned img2vid checkpoints and documents generation/resolution expectations (576×1024) but does not provide a detailed, checkpoint-scoped preprocessing prescription reconciling encoder input size vs. generation resolution in the checked blobs. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Pre-submit validation

- Validate that input image orientation/resolution matches the model-page/README recommended generation orientation (reported generation at 576×1024) when using the checkpoint under img2vid settings. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- Confirm that the requested num_frames aligns with the checkpoint's documented fine‑tuned frame count for temporal coherence assumptions (SVD‑XT documented as 25 frames in the repository/model page). Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Task-specific formatting

- Repository README and model page usage examples and descriptions express pipeline usage for image-conditioned generation accepting an image conditioning frame and parameters controlling frame count; the checked README blob is the canonical committed usage documentation available in the checked sources. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt

## Output interpretation

### Outputs

- Primary output described in repository and model page is a short sequence of decoded video frames (a short video clip); repository/model-page text documents SVD‑XT producing 25 frames at 576×1024. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Interpretation

- Checked canonical repository/model-page/README do not document emission of calibrated per-frame confidence/probability scores as part of the checkpoint outputs; no checkpoint-scoped primary evidence of such emitted per-frame calibrated scores was found in the checked sources. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Post-inference validation

- Post-inference checks should include confirming produced frame count equals requested/expected frame count (checkpoint documented: 25 frames for SVD‑XT), confirming decoded frame resolution matches documented generation resolution (576×1024), and verifying watermark presence if using the released demo/inference code which the model page/README report enables image-level watermarking by default. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### genmo-mochi-1-preview — `insufficient-evidence`

- Task: image-to-video generation
- Criteria: No primary-source checkpoint-scoped repository/model-card evidence for the alternative was checked in the assembled primary evidence set; therefore no protocol-matched numeric or qualitative comparison is supported.
- Rationale: The assembled primary evidence contains checkpoint-scoped documentation only for svd_xt.safetensors in the checked sources; the alternative model lacks corresponding primary evidence in the checked findings to enable a task- and protocol-matched comparison.
- Comparison conditions: A valid comparison would require primary-source, checkpoint-scoped model-card or repository documentation for both models under the same evaluation protocol; such documentation is absent for the alternative in the checked findings.
- Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v — `insufficient-evidence`

- Task: image-to-video generation
- Criteria: No primary-source checkpoint-scoped repository/model-card evidence for the alternative was checked in the assembled primary evidence set; therefore no protocol-matched numeric or qualitative comparison is supported.
- Rationale: Only primary evidence for svd_xt.safetensors and repository/model-page wording was included in the checked findings; the alternative lacks corresponding primary evidence in the checked set.
- Comparison conditions: A protocol-matched comparison requires matched checkpoint-scoped evaluation details for both models; such details are absent for the alternative in the checked findings.
- Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

## Limitations and safety

### Limitations

- Checkpoint-scoped frame count training limits: repository/model-page statements document SVD trained to generate 14 frames and SVD‑XT fine‑tuned to 25 frames; this constrains direct applicability to much longer sequences without further fine‑tuning. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- Evidence gap: Exact parameter count for the svd_xt.safetensors checkpoint is not reported in the checked primary sources (model page, repository README, commit/blob blame). Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blame/0fa137231bc6717ea4551951b2a942c46cf50051/svd_xt.safetensors
- Evidence gap: No checkpoint-scoped numeric benchmark rows (dataset/split/metric/value tied to svd_xt.safetensors) were found in the checked canonical sources (model card and repository README). Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- Evidence gap: The checked canonical sources do not document the container or codec format used for storing/generated videos produced by the official demo or pipeline for svd_xt.safetensors. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

### Safety

- Released inference and demo code enable image-level watermarking by default (repository/model-page statement). Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- Evidence gap: The checked primary sources do not publish a canonical repository LICENSE.md blob or explicit license text in the checked locators; the model card references a commercial-use policy link but the checked sources do not provide an explicit LICENSE.md blob URL or license text to confirm exact license wording. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- Evidence gap: Red-team or trustworthiness evaluation reports referenced by model-page/README wording are not published as detailed reports in the checked primary repository blobs; the checked model card/README mention evaluations but do not contain linked, published red-team reports in the checked locators. Sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt, https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Stable Video Diffusion XT — Hugging Face model page

- URL: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt
- Publisher: Stability AI / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model landing page for the stable-video-diffusion-img2vid-xt checkpoint; contains repository-level descriptions of SVD and SVD‑XT, reported frame counts, runtime notes, watermarking statement, and links to repository artifacts.
- Scope: stabilityai/stable-video-diffusion-img2vid-xt (model card / repository landing page)
- Supports: Model described as image-conditioned latent video diffusion (img2vid)
- Supports: SVD and SVD‑XT frame-count and resolution statements (SVD: 14 frames; SVD‑XT: 25 frames at 576×1024) as expressed on the model page
- Supports: Statement that released inference/demo code enables image-level watermarking by default
- Supports: Reference to commercial-use policy on model page

### Model README (specific commit blob) for stable-video-diffusion-img2vid-xt

- URL: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md
- Publisher: Stability AI / Hugging Face (repository)
- Type: `repository`
- Primary because: Repository README blob at a specific commit provides the canonical committed README content describing checkpoint scope, finetuning (SVD -> SVD-XT), frame counts, and usage notes.
- Scope: stabilityai/stable-video-diffusion-img2vid-xt README (specific commit blob)
- Supports: SVD described as finetuned from an SVD Image-to-Video model (14 frames) and SVD‑XT as fine‑tuned to produce 25 frames (README wording)
- Supports: Model type described as a generative image-to-video model in the README
- Supports: Repository usage and runtime notes, including watermarking mention

### svd_xt.safetensors (repository blob blame locator showing file metadata)

- URL: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blame/0fa137231bc6717ea4551951b2a942c46cf50051/svd_xt.safetensors
- Publisher: Stability AI / Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository blob blame locator provides the canonical file locator and file metadata (file size and SHA256) for svd_xt.safetensors.
- Scope: stabilityai/stable-video-diffusion-img2vid-xt (svd_xt.safetensors blob blame locator showing file metadata)
- Supports: Existence of svd_xt.safetensors file in the repository
- Supports: File size: 9,559,625,980 bytes reported in blob blame view
- Supports: SHA256 checksum: b2652c23d64a1da5f14d55011b9b6dce55f2e72e395719f1cd1f8a079b00a451 reported in blob blame view

### Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets (arXiv:2311.15127)

- URL: https://arxiv.org/abs/2311.15127
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical upstream preprint that documents Stable Video Diffusion approaches included as family-level research context; included to cross-check family-level claims where referenced by the repository/model card.
- Scope: Upstream paper/preprint for Stable Video Diffusion family
- Supports: Upstream family-level documentation for Stable Video Diffusion (arXiv preprint identifier and content).

## Evidence gaps

- Evidence gap: No checkpoint-scoped immutable release manifest or published release tag/manifest listing svd_xt.safetensors was found in the checked primary sources (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blame/0fa137231bc6717ea4551951b2a942c46cf50051/svd_xt.safetensors).
- Evidence gap: Exact parameter count for the svd_xt.safetensors checkpoint is not reported in the checked primary sources (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blame/0fa137231bc6717ea4551951b2a942c46cf50051/svd_xt.safetensors).
- Evidence gap: No checkpoint-scoped numeric benchmark rows (dataset, split, metric, numeric value) tied to svd_xt.safetensors were found in the checked primary sources (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md , https://arxiv.org/abs/2311.15127).
- Evidence gap: The checked primary sources do not document emission of per-frame calibrated confidence/probability scores or explicit per-frame metadata fields emitted by the checkpoint or demo code (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md).
- Evidence gap: The checked primary sources do not document the container or codec format used for storing/generated videos produced by the official demo or pipeline for svd_xt.safetensors (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md).
- Evidence gap: Red-team/trustworthiness evaluation reports referenced in model-page wording or README are not published in the checked primary repository blobs (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md).
- Evidence gap: The checked primary sources do not contain an explicit repository LICENSE.md blob URL or explicit license text at the checked locators; the model card references a commercial-use policy but the canonical LICENSE.md blob was not present in the checked primary locators (checked URLs: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt , https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/a6850e05151b7471db8fec08463fab0f09a280d3/README.md).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 12 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/discussions/86/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'aws-samples' for this exact model scope: $.sources[14] uses unapproved repository owner 'aws-samples' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
