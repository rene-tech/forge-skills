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

- Research key: `github-com-nvlabs-cosmos-policy-blob-main-aloha-md-93a4d0fefa`
- Independent audit: `revised`
- Researched: `2026-08-06T08:56:30.682902+00:00`

Checked primary upstream artifacts (Hugging Face model page, commit-level README, and base config.json) identify a base checkpoint named nvidia/Cosmos-Policy-ALOHA-Predict2-2B with a 2B-parameter diffusion-transformer architecture; some artifacts also describe latent video diffusion when characterizing the fine-tuned video-to-world head (see identity.evidenceUrls). The base-checkpoint commit README reports a 93.6% average completion rate across the ALOHA suite (commit f04a4f98...), and the base config.json lists per-task completion rates (put_x_on_plate: 1.0; fold_shirt: 0.995; put_candies_in_bowl: 0.896; put_candy_in_ziploc_bag: 0.854; average: 0.936). A separate planning-value checkpoint (nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B) is published and primary artifacts report a 12.5 percentage-point average improvement_over_base when planning-mode rollouts use the planning checkpoint alongside the base policy (see planning-model commit). Official config blobs enumerate descriptive input/output keys and dimensions (text task description string; three 224×224 RGB views top_down/left_wrist/right_wrist; proprioception dim 14; action dim 14; horizon 50; value dim 1). The models are released under NSCLv1. Primary artifacts do not publish machine-readable tokenizer identity/vocabulary/tokenization scripts, a machine-readable low-level output JSON/tensor schema with explicit units/timing, dataset split identifiers/number of trials/random seeds for reported ALOHA benchmarks, nor any Forge-container-to-upstream-checkpoint mapping; these are recorded explicitly as evidence gaps in evidenceGaps.

## Identity

- Upstream name: nvidia/Cosmos-Policy-ALOHA-Predict2-2B
- Checkpoint/version: Cosmos-Policy-ALOHA-Predict2-2B
- Immutable revision: f04a4f98abb32f4dc935087f5d09fb256493c69a
- Parameter scale: 2B
- Architecture/head: diffusion-transformer (research artifacts additionally describe latent video diffusion; see evidenceUrls for both descriptions)
- License: NVIDIA One‑Way Noncommercial License (NSCLv1)
- Evidence: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json

## Selection

### Recommended

- **Research and development of bimanual robot manipulation policies and evaluation on the ALOHA platform (contact-rich manipulation, imitation from human teleoperation demonstrations).** — Primary model artifacts and repository guidance document the checkpoint as a 2B-parameter policy fine-tuned from a Predict2-2B video foundation model on ALOHA teleoperation data and provide ALOHA experiment guidance and example evaluation scripts suitable for R&D evaluation.
  Scope: nvidia/Cosmos-Policy-ALOHA-Predict2-2B (revision f04a4f98abb32f4dc935087f5d09fb256493c69a)
  Evidence: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a, https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md

### Conditional

- **Model-based planning via rollouts (best-of-N search) using the base policy together with the companion planning/value checkpoint.** — Requires deploying Cosmos-Policy-ALOHA-Predict2-2B together with Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B and using the planning-mode procedure described in the planning-model commit-level artifact; reported planning improvements apply only when the companion planning checkpoint and planning configuration are used.
  Scope: Cosmos-Policy-ALOHA-Predict2-2B used together with Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B (planning-model commit d97a4c9a6e9861154e230a8b4650289fb067c5da)
  Evidence: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da

### Avoid

- **Commercial deployment without obtaining an appropriate commercial license.** — Primary checkpoint artifacts declare the NVIDIA One‑Way Noncommercial License (NSCLv1) for the base and planning checkpoints, which restricts commercial use per the model README/config artifacts.
  Scope: nvidia/Cosmos-Policy-ALOHA-Predict2-2B and nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B
  Evidence: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B

## Input preparation

### Semantic inputs

- Text: natural-language task description (string). Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://arxiv.org/html/2601.16163v1
- Images: multi-view RGB frames with named views top_down, left_wrist, right_wrist at resolution 224×224. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://arxiv.org/html/2601.16163v1
- Proprioception: numeric state vector with dimension 14 (7 joints per arm). Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://arxiv.org/html/2601.16163v1

### Accepted formats

- Accepted input modalities documented in checkpoint artifacts: text (string task description), RGB images (224×224 three-view frames), and proprioception (dimension 14). Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B

### Preprocessing

- Project guidance and checkpoint config note that training/evaluation uses precomputed T5 embeddings for task descriptions. Sources: https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json
- Evidence gap: Tokenizer identity, vocabulary, and tokenization scripts for Cosmos-Policy-ALOHA-Predict2-2B are not published in the inspected primary artifacts.

### Pre-submit validation

- Users should validate hardware/precision compatibility and available VRAM as stated in checkpoint artifacts; base config.json lists bf16 inference precision and approximate VRAM requirement, and planning-model commit lists recommended GPU counts and planning-mode latency observations. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da
- Evidence gap: Dataset split identifiers, number of trials per task, and random seeds used to produce the reported ALOHA benchmark numbers are not published in the inspected primary artifacts.

### Task-specific formatting

- ALOHA experiment guidance and example evaluation scripts are provided in the NVlabs cosmos-policy ALOHA.md file; the guidance references preprocessed dataset nvidia/ALOHA-Cosmos-Policy and mentions using precomputed embeddings for task descriptions. Sources: https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md, https://huggingface.co/datasets/nvidia/ALOHA-Cosmos-Policy

## Output interpretation

### Outputs

- Action outputs: candidate action sequence with action dimension 14 and horizon 50 timesteps; components correspond to left/right arm joints and grippers and control frequency 25 Hz (descriptive keys present in base config.json). Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://arxiv.org/html/2601.16163v1
- Future proprioception output: predicted future_proprioception with dimension 14 as described in base and planning config-level artifacts. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json
- Future images output: multi-view future_images at resolution 224×224 for the three named views as described in base config.json. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json
- Value output: scalar (dim 1) representing expected cumulative reward for an action sequence as described in base and planning artifacts. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da

### Interpretation

- Reported benchmark metrics in primary artifacts are per-task completion/success rates or averages over the ALOHA suite; they are descriptive summary performance metrics and are not low-level guarantees. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da

### Post-inference validation

- Evidence gap: Primary artifacts do not publish a machine-readable low-level output JSON/tensor schema with explicit field units or timing semantics beyond descriptive config.json keys; downstream validation procedures for low-level action outputs are not provided in the inspected primary artifacts.

## Public benchmarks

### ALOHA bimanual manipulation (suite average)

- Dataset/split: ALOHA-Cosmos-Policy / not reported
- Metric/value: average completion rate / 93.6% (`higher-is-better`)
- Model scope: nvidia/Cosmos-Policy-ALOHA-Predict2-2B (commit f04a4f98abb32f4dc935087f5d09fb256493c69a)
- Conditions: Reported as a suite average in the base-checkpoint commit-level README and the base checkpoint config.json; the primary artifacts do not publish dataset split identifiers, per-task trial counts, or random seeds at the same locator.
- Source: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a
- Locator: commit/f04a4f98abb32f4dc935087f5d09fb256493c69a: README.md — heading reporting "93.6% average completion rate"
- Caveat: Evidence gap: Dataset split identifiers, number of trials, and random seeds for this reported ALOHA-suite average are not published in the checked commit README or base config.json.

### ALOHA bimanual manipulation (planning-model average improvement)

- Dataset/split: ALOHA-Cosmos-Policy (planning rollouts) / not reported
- Metric/value: average completion rate improvement_over_base / improvement_over_base: 0.125 (12.5 percentage points average increase) (`higher-is-better`)
- Model scope: nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B (commit d97a4c9a6e9861154e230a8b4650289fb067c5da) used with the base checkpoint
- Conditions: Benchmarks reported in the planning-model commit-level artifact depend on using the companion planning checkpoint and the documented planning-mode procedure; per-task base-policy rows and full evaluation protocol details (splits/trials/seeds) are not published at the same locator in the inspected artifacts.
- Source: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da
- Locator: commit/d97a4c9a6e9861154e230a8b4650289fb067c5da: README.md — reported planning-model benchmark summary and improvement_over_base
- Caveat: Evidence gap: The planning-model commit-level artifact reports average improvement_over_base but does not publish the base-policy per-task rows at the same JSON pointer or the full evaluation protocol necessary to reconcile numeric differences.

## Comparisons

### nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B — `prefer-alternative`

- Task: ALOHA bimanual manipulation under planning-mode rollout evaluation
- Criteria: Reported average task score improvement when using the companion planning model with the base policy under the documented planning-mode.
- Rationale: Primary planning-model commit reports a 12.5 percentage-point average increase over the base policy when planning rollouts use the planning checkpoint alongside the base policy; both the planning-model commit and the base-checkpoint commit are the primary sources for these claims.
- Comparison conditions: Requires the planning checkpoint and planning-mode procedure documented in the planning-model commit; reported improvements are conditional on using the companion checkpoint and planning procedure rather than the base policy alone.
- Evidence: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a

## Limitations and safety

### Limitations

- License restricts commercial use: primary checkpoint artifacts declare NSCLv1 for the base and planning checkpoints and therefore restrict commercial deployment unless a separate commercial license is obtained. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B
- Evidence gap: Tokenizer identity, vocabulary, and tokenization scripts for Cosmos-Policy-ALOHA-Predict2-2B are not published in the inspected primary artifacts.
- Evidence gap: Exact low-level output JSON/tensor schema (field names, units, and timing semantics) is not provided in the inspected primary artifacts.
- Evidence gap: Dataset split identifiers, number of trials per task, and random seeds for the reported ALOHA benchmark results are not published in the inspected primary artifacts. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da
- Evidence gap: Mapping between Forge/container variant names (for example: b300-optimized, cuda12, cuda13) and upstream checkpoint identity or configuration is not documented in the inspected primary artifacts.

### Safety

- The model card and checkpoint README label the base and planning models for research-and-development use and indicate release under NSCLv1; commercial restrictions apply per the checkpoint documentation. Sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B
- Evidence gap: Detailed downstream safety checks, calibration guidance, and explicit operational safety validation procedures for low-level action outputs are not provided in the inspected primary artifacts.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Cosmos-Policy ALOHA checkpoint model page (root)

- URL: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official Hugging Face model page for the base checkpoint listing checkpoint identity, high-level README, and license.
- Scope: Cosmos-Policy-ALOHA-Predict2-2B (root model-card)
- Supports: Architecture description and 2B parameter scale
- Supports: License declaration (NSCLv1)
- Supports: High-level training/evaluation and intended-use statements

### Cosmos-Policy ALOHA checkpoint commit README (base) (commit f04a4f98...)

- URL: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/commit/f04a4f98abb32f4dc935087f5d09fb256493c69a
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Commit-level README containing the base-checkpoint ALOHA-suite average claim and checkpoint-specific statements.
- Scope: Cosmos-Policy-ALOHA-Predict2-2B (commit f04a4f98...)
- Supports: Reported ALOHA benchmark summary (93.6% average completion rate)
- Supports: Statement that checkpoint was fine-tuned on ALOHA teleoperation data
- Supports: Checkpoint-specific metadata referenced by identity

### Cosmos-Policy base config.json (refs/pr/2)

- URL: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/refs%2Fpr%2F2/config.json
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Base checkpoint config.json containing input/output keys, dimensions, diffusion hyperparameters, and training metadata.
- Scope: Cosmos-Policy-ALOHA-Predict2-2B config.json (refs/pr/2)
- Supports: Input specification (text field, image resolution and views, proprioception dim 14)
- Supports: Action output dim/horizon and control frequency (descriptive keys)
- Supports: Per-task benchmark rows and average reported in config
- Supports: Training metadata (50,000 steps, 185 demonstrations, hardware)

### Cosmos-Policy ALOHA Planning model page (root)

- URL: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official Hugging Face model page for the planning/value checkpoint.
- Scope: Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B (root model-card)
- Supports: Planning-model identity and intended use
- Supports: License declaration (NSCLv1)
- Supports: Reference to planning-mode usage with base policy

### Cosmos-Policy ALOHA Planning model commit README (commit d97a4c9a...)

- URL: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/commit/d97a4c9a6e9861154e230a8b4650289fb067c5da
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Commit-level planning-model README containing reported planning improvement_over_base, recommended GPU guidance, and latency observations.
- Scope: Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B (commit d97a4c9a...)
- Supports: Reported 12.5 percentage-point average improvement_over_base when used for planning
- Supports: Recommended hardware and planning-mode latency observations
- Supports: Statement that planning model is intended to be used together with the base policy

### Cosmos Policy paper (arXiv HTML v1)

- URL: https://arxiv.org/html/2601.16163v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical project preprint referenced by the project and model documentation for platform and benchmark protocol details.
- Scope: Cosmos Policy paper (preprint HTML v1)
- Supports: Method summary and training/evaluation context (action chunk size 50 timesteps, control frequency 25 Hz, input modalities)
- Supports: Training recipe metadata referenced by checkpoint artifacts

### ALOHA-Cosmos-Policy dataset (Hugging Face datasets page)

- URL: https://huggingface.co/datasets/nvidia/ALOHA-Cosmos-Policy
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official dataset page documenting the training dataset used for the ALOHA checkpoints.
- Scope: ALOHA-Cosmos-Policy dataset
- Supports: Dataset identity used to train Cosmos-Policy-ALOHA-Predict2-2B
- Supports: Dataset modality and provenance metadata

### NVlabs cosmos-policy repository ALOHA experiment guidance (ALOHA.md)

- URL: https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md
- Publisher: NVlabs
- Type: `repository`
- Primary because: Project repository file providing experiment guidance and notes about preprocessing (T5 embeddings) used with ALOHA data; referenced by checkpoint authors.
- Scope: ALOHA experiment guidance and preprocessing notes
- Supports: Training/evaluation guidance and note about precomputing T5 embeddings for task descriptions
- Supports: Pointers to example evaluation scripts and experiment guidance
- Supports: Reference to deployment/evaluation workflow

### NVlabs cosmos-policy repository RoboCasa evaluation notes (ROBOCASA.md)

- URL: https://github.com/NVlabs/cosmos-policy/blob/main/ROBOCASA.md
- Publisher: NVlabs
- Type: `repository`
- Primary because: Repository evaluation notes referenced by the project; contains evaluation script defaults and seed examples relevant to related evaluations.
- Scope: ROBOCASA evaluation guidance
- Supports: Example evaluation defaults (50 trials per task, example seeds) referenced by project evaluation scripts

## Evidence gaps

- Evidence gap: Tokenizer identity, vocabulary, and tokenization scripts used by Cosmos-Policy-ALOHA-Predict2-2B are not published in the inspected primary artifacts (checked: base config.json, base commit README, model page, ALOHA.md).
- Evidence gap: Machine-readable low-level output JSON/tensor schema (explicit field names, units, and timing semantics) is not provided in the inspected primary artifacts (checked: base config.json and planning-model commit-level README).
- Evidence gap: Dataset split identifiers, number of trials per task, and random seeds used to produce the reported ALOHA benchmark numbers are not published in the inspected primary artifacts (checked: base commit README and planning-model commit README).
- Evidence gap: A manifest or mapping that ties Forge/container variant names (for example: b300-optimized, cuda12, cuda13) to an exact upstream checkpoint revision or configuration is not documented in the inspected primary artifacts.
- Evidence gap: The planning-model commit reports improvement_over_base but the inspected artifacts do not publish the base-policy per-task rows at the same pointer nor the full evaluation protocol necessary to reconcile numeric differences between base README and planning commit-level summaries.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
