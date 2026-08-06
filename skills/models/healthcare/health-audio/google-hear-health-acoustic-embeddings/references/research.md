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

- Research key: `huggingface-co-google-hear-084246ebc4`
- Independent audit: `revised`
- Researched: `2026-08-06T11:42:38.217629+00:00`

HeAR (Health Acoustic Representations) is a Vision-Transformer-style masked autoencoder developed by Google Health to produce low-dimensional embeddings of two-second health-acoustic audio clips (e.g., coughs, breaths). Primary sources describe training by reconstructing masked spectrogram patches and evaluating embeddings via linear-probe downstream tasks. Canonical primary sources (Google model card, Hugging Face model pages, Google-Health repositories, arXiv preprint) do not report an immutable upstream checkpoint identifier, revision hash, or explicit per-dataset/split numeric benchmark tables for the exact upstream checkpoint. Low-level featurization hyperparameters (explicit STFT/mel/log-mel parameters) are not specified in the inspected primary locations; the google-health README documents an API payload shape (JSON instances of 32,000 floats representing 2 s at 16 kHz) and cropping/zero-padding guidance for 2 s clips, but wrapper-specific request/response schema for the Forge wrapper was not found in the reviewed sources. Model-weight versus code-license distinction is reported in the primary repositories: weights governed by Health AI Developer Foundations terms and repository code under Apache-2.0. Evidence checked: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://huggingface.co/google/hear-pytorch, https://github.com/Google-Health/hear, https://github.com/google-health/hear, https://arxiv.org/abs/2403.02522

## Identity

- Upstream name: HeAR (Health Acoustic Representations)
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Vision Transformer (Large) trained with a masked autoencoding objective (masked spectrogram-patch reconstruction encoder)
- License: Model weights: Health AI Developer Foundations License; Repository/code: Apache-2.0
- Evidence: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://huggingface.co/google/hear-pytorch, https://github.com/Google-Health/hear, https://github.com/google-health/hear, https://arxiv.org/abs/2403.02522

## Selection

### Recommended

- **Generate embeddings for two-second health-acoustic audio clips to be used as input features for downstream supervised classifiers or linear-probe evaluations (research use).** — Primary sources describe HeAR as producing low-dimensional representations of two-second audio clips and evaluating those embeddings via linear probes on health acoustic tasks, indicating suitability as feature inputs for downstream classifiers and linear-probe evaluation.
  Scope: google/hear (upstream HeAR encoder as described in Google model card, Hugging Face model page, and arXiv preprint).
  Evidence: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://arxiv.org/abs/2403.02522

### Conditional

- **Supporting research into screening or monitoring workflows for respiratory-related conditions (augmentation, feature extraction for task-specific models).** — Primary sources indicate HeAR is intended for research and requires independent downstream task-specific validation and appropriate regulatory/compliance review before clinical use; any clinical deployment must follow independent evaluation.
  Scope: google/hear (upstream HeAR encoder as described in primary sources).
  Evidence: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://arxiv.org/abs/2403.02522

### Avoid

- **On-device deployment in constrained hardware where model size is a constraint (production on-device inference without adaptation).** — Primary-source documentation states the current HeAR model size is large and not suitable for on-device deployment without further research or adaptation.
  Scope: google/hear (upstream HeAR model as described in primary sources).
  Evidence: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- **Encoding audio segments significantly longer than two seconds without downstream adaptation or segmentation.** — Primary sources state HeAR’s primary training and encoder scope target two-second audio clips and document cropping/zero-padding guidance for 2 s inputs; they do not document support for longer-duration inputs without adaptation.
  Scope: google/hear (upstream HeAR model as described in primary sources).
  Evidence: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://developers.google.com/health-ai-developer-foundations/hear/model-card

## Input preparation

### Semantic inputs

- Two-second health-acoustic audio clips (biological sounds such as coughs and breaths) are the intended input entity for the upstream HeAR encoder. Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://arxiv.org/abs/2403.02522

### Accepted formats

- Primary sources do not specify accepted file/container types (e.g., WAV/FLAC) for the upstream model pages; the google-health repository README documents an API payload shape expectation (JSON 'instances' of numeric waveform samples) for an upstream service endpoint. Sources: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md

### Preprocessing

- HeAR is trained using masked spectrogram-patch reconstruction; the encoder is a ViT-style architecture operating on spectrogram patches according to primary-source descriptions. Sources: https://arxiv.org/abs/2403.02522, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- The google-health README documents that audio longer than 2 seconds should be cropped and shorter clips zero-padded before sending to the API, and that no additional preprocessing (e.g., cough detection) is applied by the upstream API; however, exact low-level spectrogram/STFT/mel/log-mel hyperparameters are not specified in the inspected primary sources. Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://huggingface.co/google/hear, https://arxiv.org/abs/2403.02522

### Pre-submit validation

- The google-health README defines per-instance shape expectations for an upstream API (JSON 'instances' with up to four sub-lists each containing exactly 32,000 floating-point numbers representing 2 s at 16 kHz) and prescribes cropping/zero-padding conventions; primary sources do not provide exhaustive per-input validation rules (e.g., explicit sample-rate validation behavior, channel-count checks) beyond these documented expectations. Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear
- Evidence gap: Exact low-level featurization hyperparameters required to reproduce the spectrogram inputs (STFT/window/hop sizes, mel-bin counts, log-mel scaling parameters, normalization details, deterministic cropping/truncation/slide-overlap rules) are not specified in the checked primary-source files/pages. Sources: https://arxiv.org/abs/2403.02522, https://huggingface.co/google/hear, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://github.com/Google-Health/hear

### Task-specific formatting

- Upstream repository README documents an API input shape: a JSON payload with an 'instances' key containing a list of up to four sub-lists, each with exactly 32,000 floating-point numbers (2 s at 16 kHz). This is upstream service documentation and not a documented Forge wrapper request/response schema. Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- Evidence gap: The Forge wrapper hear-tensorflow-1-0-0-wrapper-20260706 request/response JSON schema, exact field names, or wrapper-specific flags were not found in the inspected primary sources; the documented input shape above is upstream service documentation, not wrapper-specific documentation. Sources: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/hear

## Output interpretation

### Outputs

- HeAR produces low-dimensional embeddings for two-second audio clips (the primary sources describe embeddings but do not report a canonical numeric embedding dimensionality in the inspected facts). Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://arxiv.org/abs/2403.02522

### Interpretation

- Primary sources describe embeddings as features to be used for downstream supervised tasks and evaluated via linear probes; the upstream sources do not define calibrated probability semantics or a canonical normalization/calibration procedure for the embeddings in the inspected materials. Sources: https://arxiv.org/abs/2403.02522, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear

### Post-inference validation

- Primary sources describe evaluation via linear probes and task-specific classifiers, implying downstream validation is required; they do not provide a canonical post-embedding calibration, thresholding, or failure-mode handling procedure (e.g., NaN/Inf handling) in the inspected sources. Sources: https://arxiv.org/abs/2403.02522, https://huggingface.co/google/hear
- Evidence gap: Explicit per-embedding calibration procedures, embedding-failure handling behavior, and authoritative normalization semantics for embeddings are not documented in the checked primary sources. Sources: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/hear

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: per-dataset/split numeric comparisons of HeAR against named alternatives
- Criteria: Missing per-checkpoint numeric benchmark tables and immutable checkpoint identifiers that would allow protocol-matched comparisons (per-dataset/split metrics tied to exact checkpoint).
- Rationale: Primary sources do not publish per-dataset/split numeric benchmark tables tied to an immutable upstream checkpoint; therefore direct numeric comparisons to alternatives under matched protocol cannot be supported from the inspected primary sources.
- Comparison conditions: Checked arXiv paper, Google model card, Hugging Face model pages, and repository READMEs for per-checkpoint numeric tables; none were found at the examined locators.
- Evidence: https://arxiv.org/abs/2403.02522, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md

## Limitations and safety

### Limitations

- HeAR is designed primarily for two-second audio clips; primary sources repeatedly state the two-second clip design constraint which may limit performance on longer sequences. Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- Model size: primary sources state the current HeAR model is large and unsuitable for direct on-device deployment without further research or adaptation. Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- Potential demographic and recording-device biases are documented as limitations in primary sources. Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear
- Inconsistent reporting of training-data scale across primary sources: the google-health README states training on approximately 175,000 hours of 2-second clips while the HeAR repository states training on more than 300 million two-second clips, indicating an ambiguity in primary-source reporting. Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://github.com/Google-Health/hear, https://github.com/google-health/hear
- Evidence gap: The canonical immutable upstream checkpoint identifier (checksum or revision string) for the checkpoint corresponding to the Forge wrapper was not found in the inspected primary-source locators. Sources: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://arxiv.org/abs/2403.02522, https://github.com/Google-Health/hear

### Safety

- Primary sources list potential demographic and recording-device biases and explicitly note limitations related to these biases. Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear
- Privacy: the google-health README documents that Google does not retain copies of any audio files sent to the HeAR API (privacy-related operational claim). Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- Primary sources do not provide an explicit canonical statement labelling the upstream HeAR checkpoint as research-only or non-diagnostic at the inspected locators. Sources: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://arxiv.org/abs/2403.02522
- Requirement: Independent clinical validation and regulatory/compliance review are required before any clinical or diagnostic use, per the upstream documentation's statements that downstream technology must undergo adequate clinical validation before real-world healthcare use. Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://developers.google.com/health-ai-developer-foundations/hear/model-card
- Contact point: repository documentation supplies a contact (health_acoustic_representations@google.com) for inquiries as documented in the google-health README. Sources: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### HeAR model card — Google Health AI Developer Foundations

- URL: https://developers.google.com/health-ai-developer-foundations/hear/model-card
- Publisher: Google Developers / Google Health
- Type: `official-documentation`
- Primary because: Official first-party model card and documentation authored by Google Health describing HeAR model design, intended clip length, intended uses, and limitations.
- Scope: HeAR upstream model (google/hear) as described in the model card
- Supports: HeAR is a health acoustic foundation model pre-trained to represent non-semantic respiratory sounds and generates low-dimensional representations of two-second audio clips.
- Supports: Lists potential applications (screening, monitoring) and notes limitations including clip-length constraint and possible demographic/recording-device biases.
- Supports: States access is governed by the Health AI Developer Foundations terms of use.

### Hugging Face model page: google/hear

- URL: https://huggingface.co/google/hear
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Canonical hosted model page for the upstream HeAR TensorFlow SavedModel; contains model description, intended clip length, and access/license notes.
- Scope: google/hear (upstream TensorFlow SavedModel hosted on Hugging Face)
- Supports: Describes HeAR as a health acoustic foundation model for two-second clips and notes access requires agreeing to Health AI Developer Foundations terms of use.
- Supports: Confirms use for downstream linear-probe evaluations and that embeddings are produced (dimension not asserted in inspected facts).

### Google-Health repository: health_acoustic_representations README (google-health repo)

- URL: https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md
- Publisher: Google-Health (GitHub repository)
- Type: `repository`
- Primary because: First-party repository README describing HeAR model name, training objective, intended 2 s clip usage, API input-shape guidance, and limitations.
- Scope: Implementation notes and operational documentation related to HeAR within the google-health repository
- Supports: Documents that HeAR’s primary training uses two-second audio clips and that after training the encoder generates low-dimensional embeddings of 2-second clips.
- Supports: States training-reported scale (~175,000 hours of 2-second clips) and includes API input-shape guidance (JSON 'instances' with sub-lists of 32,000 floats representing 2 s at 16 kHz), cropping/zero-padding guidance, and that Google does not retain copies of audio sent to the API.

### Hugging Face model page: google/hear-pytorch

- URL: https://huggingface.co/google/hear-pytorch
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Hosted PyTorch variant page mirroring upstream HeAR descriptions and confirming alternate implementation availability.
- Scope: google/hear-pytorch (PyTorch variant of upstream model)
- Supports: Confirms a PyTorch variant is available and access is governed by Health AI Developer Foundations terms of use.
- Supports: States repository code licensing distinction (model weights under Health AI Developer Foundations terms; code under Apache-2.0).

### Google-Health HeAR repository (supporting code and materials)

- URL: https://github.com/Google-Health/hear
- Publisher: Google-Health (GitHub repository)
- Type: `repository`
- Primary because: Official HeAR repository containing supporting code, materials, and statements about training scale and license.
- Scope: HeAR supporting code and materials (official repository)
- Supports: States HeAR was trained on more than 300 million two-second audio clips (reporting a training-scale figure in the repository).
- Supports: Confirms licensing: model weights under Health AI Developer Foundations License; repository code under Apache-2.0.
- Supports: Includes notebooks and deployment notes for using the model from Hugging Face and Vertex AI.

### Google-Health HeAR repository (alternate URL)

- URL: https://github.com/google-health/hear
- Publisher: Google-Health (GitHub repository)
- Type: `repository`
- Primary because: Alternate canonical repository URL for HeAR that contains the same repository facts about training scale and materials.
- Scope: HeAR supporting code and materials (official repository)
- Supports: States HeAR was trained on more than 300 million two-second audio clips.

### HeAR research paper (arXiv record)

- URL: https://arxiv.org/abs/2403.02522
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint record describing HeAR architecture, large training corpus, masked-spectrogram reconstruction training, and linear-probe evaluation approach.
- Scope: HeAR upstream model as described in the arXiv preprint
- Supports: Describes HeAR architecture and masked spectrogram-patch reconstruction training objective and evaluation via linear probes across health acoustic tasks.

## Evidence gaps

- Evidence gap: Canonical immutable upstream checkpoint identifier (checksum or revision string) for the exact HeAR checkpoint corresponding to the Forge wrapper was not found in the inspected primary-source locators (checked: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/hear, https://github.com/google-health/hear).
- Evidence gap: Per-dataset and per-split numeric benchmark tables (dataset, split, metric name, numeric value with evaluation protocol) tied to the exact upstream HeAR checkpoint are not published at the inspected primary-source locators (checked: https://arxiv.org/abs/2403.02522 [paper main text/figures], https://developers.google.com/health-ai-developer-foundations/hear/model-card [entire page], https://huggingface.co/google/hear [model page], https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md [repository README], https://github.com/Google-Health/hear and https://github.com/google-health/hear [HeAR repository READMEs]).
- Evidence gap: Exact low-level featurization/preprocessing hyperparameters required to reproduce spectrogram inputs (STFT/window/hop sizes, mel-bin counts, log-mel scaling, normalization, deterministic cropping/truncation/overlap rules) were not specified at the inspected primary-source locators (checked: https://arxiv.org/abs/2403.02522, https://huggingface.co/google/hear, https://github.com/Google-Health/google-health/blob/master/health_acoustic_representations/README.md, https://github.com/Google-Health/hear).
- Evidence gap: Exact Forge wrapper hear-tensorflow-1-0-0-wrapper-20260706 request/response JSON schema, field names, example wrapper call signatures, and wrapper-specific flags are not present in the inspected primary sources (checked: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/hear).
- Evidence gap: Explicit canonical statements labelling the upstream HeAR checkpoint as research-only or explicitly non-diagnostic were not found at the inspected primary-source locators (checked: https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://huggingface.co/google/hear, https://arxiv.org/abs/2403.02522).
- Evidence gap: Canonical per-embedding calibration procedures, embedding-failure mode handling (e.g., NaN/Inf behavior), and authoritative normalization semantics are not documented in the checked primary sources (checked: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear/model-card, https://github.com/Google-Health/hear).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[12] uses unapproved repository owner 'hearbenchmark' for this exact model scope: $.sources[12] uses unapproved repository owner 'hearbenchmark' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
