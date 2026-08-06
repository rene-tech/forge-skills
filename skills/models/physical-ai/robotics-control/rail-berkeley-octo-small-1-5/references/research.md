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

- Research key: `huggingface-co-rail-berkeley-octo-small-1-5-a0c1a13281`
- Independent audit: `revised`
- Researched: `2026-08-06T13:30:30.037912+00:00`

I verified the checkpoint rail-berkeley/octo-small-1.5 (Octo Small 1.5) as a transformer-based diffusion robot policy with an approximate parameter count of 27 million. Primary sources (model card, config, paper, and repository) document a Small/ViT‑S‑equivalent transformer backbone (token embedding size 384, 12 layers, 6 heads, MLP dim 1536) and a DiffusionActionHead that predicts 7‑dimensional continuous actions four steps into the future. The official configuration and paper record a training window_size of 2. Inputs documented for this checkpoint include multiple RGB camera views (primary and wrist) tokenized via a lightweight convolutional encoder (SmallStem16) and then into 16×16 patches (primary → 256 tokens; wrist → 64 tokens). Language instructions are tokenized with a T5 tokenizer and encoded with a T5‑Base encoder (max length 16 in configs). The repository and paper describe large pretraining scale descriptors (preprocessed dataset ≈1.2 TB; ≈800k robot trajectories) and repository-provided finetuning modes (head_only, head_mlp_only, full). Primary canonical sources do not report numeric pixel normalization constants, explicit numeric action bounds/units, calibrated confidence outputs, or an enumerated, creator‑authored list of verified robot hardware platforms for this checkpoint; I list those as evidence gaps below.

## Identity

- Upstream name: rail-berkeley/octo-small-1.5
- Checkpoint/version: rail-berkeley/octo-small-1.5
- Immutable revision: 1ec1bb0c01aa4c5c18cd72f76436e6f4360da108
- Parameter scale: 27 million parameters
- Architecture/head: Transformer-based diffusion policy (Small / ViT‑S equivalent) with token embedding size 384, 12 transformer layers, 6 attention heads, MLP dim 1536; DiffusionActionHead output head predicting continuous actions.
- License: MIT
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://arxiv.org/html/2405.12213v2, https://github.com/octo-models/octo, https://github.com/octo-models/octo/blob/main/LICENSE, https://huggingface.co/rail-berkeley/octo-small-1.5/commit/1ec1bb0c01aa4c5c18cd72f76436e6f4360da108

## Selection

### Recommended

- **Vision-and-language-conditioned short-horizon continuous robot control for robot arms (predicting multi-step 7‑DoF continuous actions conditioned on RGB cameras, language instructions, and optional goal images).** — I found config and model-card evidence that this checkpoint uses a DiffusionActionHead predicting 7‑dimensional continuous actions with prediction horizon 4, accepts multiple RGB camera inputs (primary and wrist) tokenized via SmallStem16, and uses a T5 tokenizer/encoder for language inputs.
  Scope: rail-berkeley/octo-small-1.5
  Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://arxiv.org/html/2405.12213v2, https://github.com/octo-models/octo
- **Short-horizon receding-horizon control where a downstream controller consumes the first action from the model's multi-step (horizon‑4) predictions and replans at each control step.** — The checkpoint configuration documents a prediction horizon of 4 and continuous 7‑D action chunks, which supports receding-horizon execution patterns where a controller executes a subset (e.g., the first) of predicted actions and replans.
  Scope: rail-berkeley/octo-small-1.5
  Evidence: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://huggingface.co/rail-berkeley/octo-small-1.5

### Conditional

- **Finetuning to new robots, morphologies, action spaces, or new sensory inputs using repository-provided finetuning modes.** — Use only documented repository finetuning modes (head_only, head_mlp_only, full) and follow repository finetuning scripts/configs; validate extensively on target hardware and dataset.
  Scope: rail-berkeley/octo-small-1.5 (finetuning modes as documented in the Octo repository)
  Evidence: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- **Inference-mode changes such as temporal ensembling or executing only the first predicted action to trade off robustness vs latency.** — Evidence gap: I did not find canonical repository examples or explicit documented API flags for temporal ensembling or an explicit repository/named API describing 'execute only first predicted action'; treat such modes as requiring downstream validation and custom implementation per deployment.
  Scope: rail-berkeley/octo-small-1.5
  Evidence: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small-1.5, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### Avoid

- **Unconstrained claims of verified robot compatibility or out-of-the-box deployment on specific robot platforms without per-platform validation.** — Evidence gap: I did not find a creator-authored, enumerated list of verified robot platforms or per-platform certification guarantees for Octo Small in the inspected primary sources; therefore avoid asserting out-of-the-box compatibility with specific hardware without independent verification.
  Scope: rail-berkeley/octo-small-1.5
  Evidence: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2

## Input preparation

### Semantic inputs

- RGB camera images: primary and wrist camera observations are accepted as image inputs for this checkpoint. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://arxiv.org/html/2405.12213v2
- Language instructions: tokenized via a T5 tokenizer and encoded with a T5‑Base encoder (language encoder is configured and not finetuned). Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://arxiv.org/html/2405.12213v2
- Optional goal-image inputs and robot state/proprioception are accepted as task/observation inputs as documented by the project README and model config. Sources: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small-1.5

### Accepted formats

- Primary (third-person) camera images are represented as 256×256 RGB images and processed via dataset resize_256_256 as referenced in the checkpoint configuration. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- Wrist camera images correspond to 128×128 RGB images inferred from documented token counts (wrist images yield 64 image tokens when split into 16×16 patches). Sources: https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- Language inputs use a T5 tokenizer with max length configured (task tokenizer max_length = 16 in config). Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### Preprocessing

- Image observations are preprocessed with a lightweight convolutional encoder (SmallStem16) before patching/tokenization. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- Images are split into 16×16 patches for primary images (yielding 256 tokens) and into patches yielding 64 tokens for wrist images as described in the paper and config. Sources: https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- Evidence gap: exact numeric image-normalization constants (per-channel mean/std), explicit augmentation numeric values, and precise augmentation ordering/implementation are not specified in the inspected primary sources. Sources: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://arxiv.org/html/2405.12213v2

### Pre-submit validation

- A history/training window size of 2 timesteps is documented in the checkpoint configuration. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://huggingface.co/rail-berkeley/octo-small-1.5
- Action head dimensionality is 7 and prediction horizon is 4 as specified in the action head configuration; downstream systems must accept 7‑D continuous action vectors and horizon-4 action chunks. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- Evidence gap: explicit numeric bounds, action ranges, or normalized units for joint positions/velocities/efforts are not specified in the inspected primary sources and must be validated before connecting to hardware. Sources: https://huggingface.co/rail-berkeley/octo-small-1.5, https://github.com/octo-models/octo

### Task-specific formatting

- No canonical natural-language prompt templates or model-card prompt examples are provided in the inspected primary sources; language is tokenized to length 16 by the configured T5 tokenizer. Sources: https://huggingface.co/rail-berkeley/octo-small-1.5, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

## Output interpretation

### Outputs

- The model emits multi-step continuous robot action trajectories: 7-dimensional continuous action vectors predicted in chunks with prediction horizon 4 (four-step action chunks). Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://huggingface.co/rail-berkeley/octo-small-1.5
- Output head type is a DiffusionActionHead (a diffusion-based action decoder) as configured in the checkpoint. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### Interpretation

- Predicted multi-step action chunks are intended to be interpreted as short-horizon continuous control proposals; a downstream controller must validate and possibly reproject these outputs to robot-specific joint/effort/velocity ranges before execution. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://github.com/octo-models/octo
- Evidence gap: I did not find checkpoint-provided calibrated confidence scores or probability fields for predicted actions in the inspected primary sources; do not treat outputs as calibrated probabilities without additional calibration. Sources: https://huggingface.co/rail-berkeley/octo-small-1.5, https://github.com/octo-models/octo

### Post-inference validation

- Post-inference validation should include in-situ testing against teleoperated or recorded ground-truth trajectories and stepwise safety checks before any real-world deployment; the project documents evaluation and finetuning flows but does not provide per-platform safety guarantees. Sources: https://github.com/octo-models/octo, https://arxiv.org/html/2405.12213v2
- Evidence gap: no repository- or model-card-documented formal calibration protocol or numeric confidence outputs for runtime gating are present in the inspected primary sources. Sources: https://huggingface.co/rail-berkeley/octo-small-1.5, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### allenai-molmoact2-so100-101 — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: I checked the Octo model card, config, and paper for head-to-head evaluations against the named alternative and did not find any matching dataset/split/metric comparisons.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-smolvla-libero — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: I inspected canonical Octo sources for head-to-head evaluation rows and did not find comparisons against this alternative.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-smolvla-libero-plus — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: I checked the Octo paper, model card, and config for direct head-to-head tables/figures and found none for this alternative.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-smolvla-robocasa — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: I found no head-to-head numeric comparisons in the canonical Octo sources for this alternative.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-smolvla-robotwin — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: Canonical Octo sources do not report head-to-head evaluations against this alternative for the same datasets/metrics.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-smolvla-vlabench — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: I did not find comparable benchmark rows in the Octo paper/config/model card for this alternative.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-xvla-base — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: No head-to-head evaluation was found in the Octo canonical sources for this alternative.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### huggingface-lerobot-xvla-google-robot — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: I checked canonical Octo sources and did not find head-to-head numeric comparisons against this alternative.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### sberroboticscenter-greenvla-2b-base — `insufficient-evidence`

- Task: robotics-control (embodied trajectory evaluation)
- Criteria: No same-dataset / same-metric direct comparison reported in the inspected Octo primary sources for this checkpoint.
- Rationale: Primary Octo sources do not contain head-to-head evaluations with this alternative for matching protocols.
- Comparison conditions: insufficient-evidence
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

## Limitations and safety

### Limitations

- Training-data scale and provenance are described at a dataset-mix level (preprocessed dataset ≈1.2 TB; ≈800k robot trajectories) in the repository and paper; this limits per-dataset composition transparency and may introduce dataset biases. Sources: https://github.com/octo-models/octo, https://arxiv.org/html/2405.12213v2
- License: model code and model weights are released under the MIT License as recorded in the repository LICENSE. Sources: https://github.com/octo-models/octo/blob/main/LICENSE
- Evidence gap: the inspected primary sources do not include an explicit, enumerated list of verified robot platforms or per-platform compatibility guarantees for Octo Small; hardware compatibility must be validated per target platform. Sources: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2
- Evidence gap: explicit numeric pixel-normalization constants (per-channel mean/std), deployment inference-precision settings (e.g., bfloat16 vs float32), and formal runtime calibration procedures are not specified in the inspected primary sources. Sources: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json, https://github.com/octo-models/octo
- Evidence gap: I did not find StaticEmbodiedBench‑VLA exact benchmark rows, numeric values, split names, or evaluation hardware details for this exact checkpoint in the canonical paper or repository; any numeric benchmark claim must be verified at a precise table/figure/locator. Sources: https://arxiv.org/html/2405.12213v2, https://huggingface.co/rail-berkeley/octo-small-1.5, https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json

### Safety

- Evidence gap: I did not find explicit creator-authored safety, privacy, clinical, or dual‑use mitigation procedures (e.g., mandatory human-in-the-loop policies, PHI handling instructions, or runtime safety filters) in the inspected primary sources; conservative human review, in-situ validation, and per-platform safety engineering are required before real-world deployment. Sources: https://github.com/octo-models/octo, https://huggingface.co/rail-berkeley/octo-small-1.5, https://arxiv.org/html/2405.12213v2

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### rail-berkeley/octo-small-1.5 model card (Hugging Face)

- URL: https://huggingface.co/rail-berkeley/octo-small-1.5
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card for the exact checkpoint rail-berkeley/octo-small-1.5; contains checkpoint identity and high-level usage facts.
- Scope: rail-berkeley/octo-small-1.5
- Supports: Octo Small is trained with a window size of 2.
- Supports: Octo Small predicts 7-dimensional actions 4 steps into the future using a diffusion policy.
- Supports: The checkpoint identifier for Octo Small is rail-berkeley/octo-small-1.5.
- Supports: The Hugging Face model card documents acceptance of image and language inputs.

### rail-berkeley/octo-small config.json (Hugging Face repository file, blame view)

- URL: https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Checkpoint-specific configuration file listing tokenizers, observation tokenizers, action head, model hyperparameters, and dataset kwargs for the Small checkpoint.
- Scope: rail-berkeley/octo-small-1.5 (Small variant configuration)
- Supports: Observation tokenizers for primary and wrist images use ImageTokenizer with SmallStem16 encoder.
- Supports: Task tokenizer for language uses LanguageTokenizer with encoder 't5-base' and max_length = 16.
- Supports: Action head is DiffusionActionHead with prediction horizon 4 and action dimension 7.
- Supports: Transformer hyperparameters: token embedding size 384; 12 layers; 6 attention heads; MLP dim 1536; window_size = 2.
- Supports: Dataset configuration references data_mix 'oxe_magic_soup' and data_dir 'resize_256_256'.

### rail-berkeley/octo-small-1.5 repo commit (Hugging Face commits view)

- URL: https://huggingface.co/rail-berkeley/octo-small-1.5/commit/1ec1bb0c01aa4c5c18cd72f76436e6f4360da108
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository commit view showing the model card/config commit SHA associated with the named checkpoint.
- Scope: rail-berkeley/octo-small-1.5 (checkpoint upload/commit)
- Supports: Provides an explicit commit SHA associated with the model card files for this checkpoint.
- Supports: Confirms the model card lists license as MIT and records checkpoint identity facts.

### rail-berkeley/octo-small-1.5 repository tree (Hugging Face)

- URL: https://huggingface.co/rail-berkeley/octo-small-1.5/tree/main
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Official repository tree for the exact checkpoint containing model card, files, and notebooks.
- Scope: rail-berkeley/octo-small-1.5
- Supports: Contains the model card, README, and inference notebooks associated with this checkpoint.

### Octo README (GitHub)

- URL: https://github.com/octo-models/octo
- Publisher: octo-models (GitHub repository)
- Type: `repository`
- Primary because: Official project repository README describing model capabilities, dataset-scale descriptors, finetuning modes, and links to paper/config.
- Scope: Octo project and repository (supports checkpoint usage and finetuning flows)
- Supports: Octo models are transformer-based diffusion policies trained on a diverse mix of ≈800k robot trajectories.
- Supports: The preprocessed Octo pretraining dataset is described at ≈1.2 TB.
- Supports: Octo provides finetuning modes such as head_only, head_mlp_only, and full.
- Supports: Repository documents loading/finetuning using pretrained path hf://rail-berkeley/octo-small-1.5.

### Octo paper (arXiv abstract)

- URL: https://arxiv.org/abs/2405.12213
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv preprint record for the Octo project referencing the full paper.
- Scope: Octo paper (preprint record)
- Supports: Identifies the Octo paper and links to the canonical preprint.
- Supports: Classifies the work under relevant categories (Robotics, Machine Learning).

### Octo paper (arXiv HTML v2 full paper)

- URL: https://arxiv.org/html/2405.12213v2
- Publisher: arXiv
- Type: `paper`
- Primary because: Full-paper canonical HTML for the Octo preprint containing architecture, tokenization, and model-size details.
- Scope: Octo paper (full text)
- Supports: Documents that images are split into 16×16 patches yielding 256 tokens for primary images and 64 tokens for wrist images.
- Supports: States Octo-Small hyperparameters: 12 layers, hidden size 384, MLP size 1536, 6 attention heads, and 27M parameters.
- Supports: Describes transformer-based diffusion policy architecture and tokenization design.

### Octo LICENSE (MIT) on GitHub

- URL: https://github.com/octo-models/octo/blob/main/LICENSE
- Publisher: octo-models (GitHub)
- Type: `official-documentation`
- Primary because: Repository license file specifying the license for code and released model artifacts.
- Scope: Octo project (license)
- Supports: The Octo repository is licensed under the MIT License.

## Evidence gaps

- Exact numeric pixel-normalization constants (per-channel mean/std) are not specified in the inspected primary sources (checked: model card, config.json, repository README, arXiv full paper).
- Exact explicit numeric augmentation parameter values and precise augmentation ordering/implementation are not specified in the inspected primary sources (checked: config.json, repository README, arXiv full paper).
- Deployment/inference numerical precision settings (e.g., bfloat16 vs float32) are not specified in the inspected primary sources (checked: model card, config.json, repository README).
- No explicit creator-authored enumerated list of verified robot platforms or per-platform compatibility guarantees for Octo Small was found in the inspected primary sources (checked: repository README, model card, arXiv paper).
- No canonical natural-language prompt templates, example language prompts, or exact input prompt formatting examples for this checkpoint were found in the inspected primary sources (checked: model card, config.json, repository README, arXiv paper).
- No checkpoint-provided calibrated confidence outputs, probability fields, or formal calibration procedures are documented in the inspected primary sources (checked: model card, config.json, repository README).
- No canonical repository examples or explicit documented API flags for temporal ensembling or an 'execute only first predicted action' inference mode were found in the inspected primary sources (checked: repository README, model card, config.json).
- StaticEmbodiedBench‑VLA exact benchmark table/figure rows, numeric values, split names, and evaluation-hardware details for rail-berkeley/octo-small-1.5 are not present in the inspected primary sources; I checked the arXiv full paper (https://arxiv.org/html/2405.12213v2), the Hugging Face model card (https://huggingface.co/rail-berkeley/octo-small-1.5), and the checkpoint config (https://huggingface.co/rail-berkeley/octo-small/blame/a440bb5ccb1ba53e65854616eea4c6a3e5fa58b4/config.json) and found no precise benchmark locator for this checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
