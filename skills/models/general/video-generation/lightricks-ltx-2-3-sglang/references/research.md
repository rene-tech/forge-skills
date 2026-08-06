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

- Research key: `huggingface-co-lightricks-ltx-2-3-4bb7928cc7`
- Independent audit: `revised`
- Researched: `2026-07-24T00:01:06.934074+00:00`

LTX-2.3 (upstream name LTX-2.3) is described in the inspected primary sources as a DiT-based audio‑video foundation model intended to generate synchronized video and audio from text and/or image inputs. The Hugging Face model card and README blobs document multiple checkpoint artifacts (including full/dev and distilled variants) and upscaler artifacts; the README blob lists runtime stack requirements. The repository LICENSE blob (dated January 5, 2026 in the inspected blob) states licensing terms including a commercial‑use provision for entities meeting a revenue threshold. The project site and a technical report in the inspected findings describe architecture-level claims including a reported ~22B parameter scale; however, several low-level operational details (exact tokenizer vocabulary, exact numeric inference defaults, precise latent tensor shapes, explicit I/O bounds, creator-published numeric benchmark tables, and deterministic seed/replicability instructions) are not present in the inspected primary sources and are recorded as evidence gaps below.

## Identity

- Upstream name: LTX-2.3
- Checkpoint/version: ltx-2.3-22b-dev; ltx-2.3-22b-distilled; ltx-2.3-22b-distilled-1.1; ltx-2.3-22b-distilled-lora-384; ltx-2.3-spatial-upscaler-x2-1.1; ltx-2.3-temporal-upscaler-x2-1.0
- Immutable revision: not reported
- Parameter scale: 22B total (reported by the project site and related project materials in the inspected findings)
- Architecture/head: DiT-based (diffusion transformer) asymmetric dual‑stream joint audio‑video model with bidirectional cross‑attention between audio and video streams (described as a DiT-based audio‑video foundation model in the inspected primary sources)
- License: LTX-2 Community License Agreement (see LICENSE blob in the Hugging Face repository; license blob includes a commercial‑use provision for entities meeting a revenue threshold)
- Evidence: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://huggingface.co/Lightricks/LTX-2.3/blob/main/LICENSE, https://huggingface.co/Lightricks/LTX-2.3/blame/ead7cbeade7d01d8cf21c919f24358501baa301a/LICENSE, https://huggingface.co/Lightricks/LTX-2.3/commits/main, https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf, https://ltx.io

## Selection

### Recommended

- **Text-to-video generation with synchronized audio** — The Hugging Face model card and the README blob for LTX-2.3 describe support for text-to-video and joint audio-video generation and identify the model as an audio-video DiT-based foundation model.
  Scope: LTX-2.3 checkpoints (as named in the model card and README blob)
  Evidence: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- **Image-conditioned video generation (image-to-video / image+text-to-video)** — The Hugging Face model card and README blob list image-to-video and image+text-to-video among supported tasks and pipeline tags.
  Scope: LTX-2.3 checkpoints (as named in the model card and README blob)
  Evidence: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

### Conditional

- **Use distilled checkpoints for lower‑compute, faster inference (quality vs speed tradeoff)** — Validate output quality on representative prompts for the specific distilled artifact before deployment; the README blob documents distilled variants but does not publish creator-run numeric head-to-head benchmarks in the inspected primary sources.
  Scope: ltx-2.3-22b-distilled and ltx-2.3-22b-distilled-1.1 (as listed in the README blob)
  Evidence: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://huggingface.co/Lightricks/LTX-2.3

### Avoid

- **Unvalidated clinical, medical, or safety‑critical decision‑making** — Upstream model card and README do not provide clinical validation, PHI handling guidance, or certifications for clinical use; no creator‑published clinical use approvals were found in the inspected primary sources.
  Scope: LTX-2.3 checkpoints (as named in the inspected primary sources)
  Evidence: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

## Input preparation

### Semantic inputs

- Natural-language text prompts are accepted as a primary conditioning modality for text-to-video and joint audio-video generation (text-to-video). Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Image inputs are supported for image-conditioned video generation (image-to-video, image+text-to-video), as listed among supported tasks and pipeline tags. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Gemma 3 is referenced in the project materials as the multilingual text encoder used by the project (project site lists Gemma 3 text encoder assets and multi-layer feature aggregation); the inspected README blob does not document tokenizer vocabulary or tokenization algorithm details. Sources: https://ltx.io, https://huggingface.co/Lightricks/LTX-2.3

### Accepted formats

- The model card and README blob list supported pipelines such as text-to-video and image-to-video and expose pipeline tags; users should supply the modality inputs (text and/or image) expected by those pipelines. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- The inspected primary sources document runtime requirements for executing example pipelines (runtime stack constraints are provided in the README blob). Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

### Preprocessing

- The README blob documents runtime/dependency constraints (e.g., Python, CUDA, PyTorch versions) for running the provided code and examples; however, the README blob does not provide exhaustive low-level normalization/resizing or resampling commands in the inspected blobs. Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Evidence gap: exact numeric inference default hyperparameters (for example default stage‑1 num_frames, frame_rate, num_inference_steps, guidance_scale, output_type) are not specified in the inspected README blob or model card; these numeric defaults could not be located in the inspected primary sources. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Evidence gap: exact tokenizer vocabulary, tokenizer version, special tokens, and tokenization algorithm are not specified in the inspected primary sources (model card, README blob, project site). Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://ltx.io
- Evidence gap: precise input bounds (explicit max frames, explicit max resolution, explicit max tokens) are not documented in the inspected primary sources. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Evidence gap: exact tensor shapes for video/audio latents, numeric buffer formats, and recommended file/codec/container formats for output (e.g., mp4/h.264) are not specified in the inspected primary sources. Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://huggingface.co/Lightricks/LTX-2.3

### Pre-submit validation

- Evidence gap: the inspected primary sources do not provide prescriptive input validation rules (for example explicit max token length, exact image dimension limits, or formal input sanitization checks) for user inputs; these checks are not documented in the model card or README blob. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

### Task-specific formatting

- Evidence gap: the inspected README blob and model card do not contain an explicit, canonical prompt template or a fully enumerated example prompt/pair-input format required by the upstream pipelines; no exact prompt template was located in the inspected primary sources. Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://huggingface.co/Lightricks/LTX-2.3

## Output interpretation

### Outputs

- Primary output modalities documented in the inspected primary sources are video and audio (joint generation). Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Evidence gap: the inspected primary sources do not define a calibrated confidence score or likelihood scalar for generated video/audio outputs; no calibrated probability output contract is documented in the model card or README blob. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

### Interpretation

- Interpret generation hyperparameters as tradeoffs between speed and quality; the README blob documents the existence of multiple checkpoint variants (full/dev and distilled) and upscalers which implies tradeoffs, but exact numeric calibrated tradeoff tables are not present in the inspected primary sources. Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://huggingface.co/Lightricks/LTX-2.3

### Post-inference validation

- Evidence gap: the inspected primary sources do not publish prescriptive post‑inference QA procedures or checkpoint‑scoped validation pipelines (for example automated perceptual metrics, test suites, or pass/fail thresholds); users must perform downstream validation. Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://huggingface.co/Lightricks/LTX-2.3

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### Wan2.2 — `insufficient-evidence`

- Task: Image-to-video / speed-quality tradeoff
- Criteria: No creator-published head-to-head numeric benchmark comparing LTX-2.3 to Wan2.2 was found in the inspected primary sources; community reports exist but are not part of the canonical primary sources used here.
- Rationale: The inspected primary sources (Hugging Face model card and README blob) do not contain controlled numeric comparisons to Wan2.2; therefore there is insufficient primary-source evidence to prefer LTX-2.3 or Wan2.2 on standardized numeric criteria.
- Comparison conditions: No primary-source, creator-run comparisons for the named checkpoints under matched protocol (quantization, sampler, steps) were located in the checked materials.
- Evidence: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

## Limitations and safety

### Limitations

- License restriction: the LTX-2 Community License Agreement in the LICENSE blob (dated January 5, 2026 in the inspected blob) includes a commercial‑use provision requiring commercial entities meeting a revenue threshold to obtain a paid commercial‑use license. Sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/LICENSE, https://huggingface.co/Lightricks/LTX-2.3/blame/ead7cbeade7d01d8cf21c919f24358501baa301a/LICENSE
- Evidence gap: the inspected primary sources do not publish creator-run numeric benchmarks (dataset/split/metric/value) for LTX-2.3; no comparable numeric performance tables were located in the model card, README blob, or technical report. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md, https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf
- Evidence gap: precise architecture parameterization breakdown (for example an exact 14B video + 5B audio numeric split summing to 22B) is reported on the project site and project materials but is not present in the Hugging Face model card README blob; users should treat the exact internal breakdown as unverified unless confirmed by an explicit upstream author statement in the inspected primary sources. Sources: https://ltx.io, https://huggingface.co/Lightricks/LTX-2.3

### Safety

- Evidence gap: the inspected primary sources (model card and README blob) do not provide creator‑provided clinical or PHI handling guidance; no upstream documentation qualifying the model for clinical use was found in the checked primary sources. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Evidence gap: the inspected primary sources do not prescribe an upstream-mandated safety QA checklist or an exhaustive mitigation protocol; users must perform their own safety review and downstream validation. Sources: https://huggingface.co/Lightricks/LTX-2.3, https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Lightricks / LTX-2.3 (Hugging Face model card)

- URL: https://huggingface.co/Lightricks/LTX-2.3
- Publisher: Lightricks (Hugging Face model host)
- Type: `model-card`
- Primary because: Official Hugging Face model card for LTX-2.3 containing high-level capability claims and links to blobs.
- Scope: LTX-2.3 model card (general model metadata and supported tasks)
- Supports: Identity (model name LTX-2.3, high-level capability: audio-video generation)
- Supports: Supported tasks list (text-to-video, image-to-video, joint audio-video)
- Supports: Pointer to README blob and other repo artifacts

### Lightricks / LTX-2.3 README (Hugging Face blob main/README.md)

- URL: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md
- Publisher: Lightricks (Hugging Face repo blob)
- Type: `model-card`
- Primary because: Exact README blob for the LTX-2.3 Hugging Face repository listing artifacts and runtime notes.
- Scope: LTX-2.3 README blob (primary README content committed to the model repo)
- Supports: Checkpoint artifact listings (names of available artifacts and variants)
- Supports: Runtime/dependency requirements documented in the blob
- Supports: High-level usage notes

### Lightricks / LTX-2.3 LICENSE (Hugging Face blob)

- URL: https://huggingface.co/Lightricks/LTX-2.3/blob/main/LICENSE
- Publisher: Lightricks (Hugging Face repo blob)
- Type: `official-documentation`
- Primary because: Canonical LICENSE blob within the Hugging Face repository containing the named license and the cited commercial‑use provision.
- Scope: LTX-2.3 LICENSE blob (canonical license text in the model repository)
- Supports: License name and text
- Supports: Commercial‑use threshold provision and license date

### Lightricks / LTX-2.3 LICENSE (blame view)

- URL: https://huggingface.co/Lightricks/LTX-2.3/blame/ead7cbeade7d01d8cf21c919f24358501baa301a/LICENSE
- Publisher: Lightricks (Hugging Face repo blob)
- Type: `official-documentation`
- Primary because: Blame view of the LICENSE blob as hosted on Hugging Face to show the exact blob and date used in the inspection.
- Scope: LTX-2.3 LICENSE blob (blame view for provenance of the license blob)
- Supports: License provenance, date, and specific commercial-use sentence cited in the dossier

### Lightricks / LTX-2.3 commits (commits/main)

- URL: https://huggingface.co/Lightricks/LTX-2.3/commits/main
- Publisher: Lightricks (Hugging Face commits view)
- Type: `model-card`
- Primary because: Hugging Face commits history page for the LTX-2.3 repo used to inspect commit timeline and uploaded artifacts.
- Scope: LTX-2.3 commits history (repository commits listing)
- Supports: Location for commit history and artifact upload timeline (checked for commit evidence)
- Supports: Reference for provenance of README and LICENSE blob revisions

### LTX-2 Technical Report (project PDF)

- URL: https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf
- Publisher: LTX project (videos.ltx.io)
- Type: `technical-report`
- Primary because: Project technical report published by the LTX project describing the underlying LTX/LTX-2 architecture (used to verify architecture-level claims where present).
- Scope: LTX-2 technical report (project-hosted PDF describing architecture and background)
- Supports: Architecture-level description and pointer to LTX-2 paper/preprint
- Supports: Context for the DiT-based audio-video architecture claims

### LTX official site (ltx.io)

- URL: https://ltx.io
- Publisher: LTX project (ltx.io)
- Type: `official-documentation`
- Primary because: Official project site pages used by the project to describe architecture-level claims and encoder assets (Gemma 3) referenced in the inspected findings.
- Scope: Official LTX project site (project-level architecture and feature descriptions)
- Supports: Project-level architecture descriptions (used to verify parameter-scale and architecture breakdown claims present on the project site)
- Supports: Reference to Gemma 3 text encoder assets per project materials

## Evidence gaps

- Evidence gap: exact tokenizer vocabulary, tokenizer version, special tokens, and tokenization algorithm are not specified in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md , https://ltx.io).
- Evidence gap: exact numeric inference defaults (for example default stage-1 num_frames, frame_rate, num_inference_steps, guidance_scale, output_type) are not present in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md).
- Evidence gap: precise tensor shapes for video/audio latents, numeric buffer formats, and decoder I/O shapes are not documented in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md , https://huggingface.co/Lightricks/LTX-2.3).
- Evidence gap: explicit input bounds (maximum frames, maximum resolution, maximum tokens) are not specified in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md).
- Evidence gap: explicit recommended file/codec/container formats and bitrates for output audio/video are not specified in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md).
- Evidence gap: deterministic-seed handling and reproducibility instructions (seed semantics and recommended usage for deterministic runs) are not documented in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md).
- Evidence gap: creator-published numeric benchmark tables (dataset/split/metric/value) for LTX-2.3 were not found in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md , https://videos.ltx.io/LTX-2/grants/LTX_2_Technical_Report_compressed.pdf).
- Evidence gap: exact repository commit SHAs that uploaded specific safetensors artifacts (for example a precise commit SHA mapping to ltx-2.3-22b-dev.safetensors) were not located in an explicit commit blob in the inspected primary sources; the commits history page was checked but specific SHA-to-artifact mappings are not reported in the inspected blobs (checked: https://huggingface.co/Lightricks/LTX-2.3/commits/main).
- Evidence gap: an upstream-published, checkpoint-scoped head-to-head numeric comparison between LTX-2.3 and other named peer checkpoints (for example Wan2.2) under a controlled protocol was not found in the inspected primary sources (checked: https://huggingface.co/Lightricks/LTX-2.3 , https://huggingface.co/Lightricks/LTX-2.3/blob/main/README.md).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 21 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation: $.inputPreparation: unexpected property featurization Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property tokenization Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'sgl-project' for this exact model scope: $.sources[8] uses unapproved repository owner 'sgl-project' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary URL https: $.sources[9] uses forbidden secondary URL https://huggingface.co/Lightricks/LTX-2.3/discussions/27 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary URL https: $.sources[10] uses forbidden secondary URL https://huggingface.co/Lightricks/LTX-2.3/discussions/8 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'cpuai' for this exact model scope: $.sources[11] uses unapproved repository owner 'cpuai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary URL https: $.sources[13] uses forbidden secondary URL https://veevid.ai/blog/ltx-2-3-complete-guide Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses forbidden secondary URL https: $.sources[14] uses forbidden secondary URL https://digitalapplied.com/blog/ltx-2-3-open-source-ai-video-generation-synchronized-audio Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses unapproved repository owner 'mickj' for this exact model scope: $.sources[17] uses unapproved repository owner 'mickj' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-2.3/blob/main/LICENSE Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
