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

- Research key: `huggingface-co-lerobot-xvla-google-robot-123e023f09`
- Independent audit: `revised`
- Researched: `2026-08-06T12:40:42.770104+00:00`

The inspected canonical repository blobs for lerobot/xvla-google-robot (config.json PR blob and repository tree/commits) show a Florence2 text encoder (florence_config.model_type = "florence2") with tokenizer settings (tokenizer_name = "facebook/bart-large", tokenizer_max_length = 1024, tokenizer_padding_side = "right"). The checkpoint config exposes multimodal policy settings: use_proprio = true, num_image_views = 3, empty_cameras = 1, n_action_steps = 30, normalization_mapping that maps STATE->IDENTITY, ACTION->IDENTITY, VISUAL->MEAN_STD, and action_mode = "ee6d". The repository also contains a model weight blob at a committed path (model.safetensors at commit 6c9e9c9028638289c2e02d8a1fc0b8063cdd303b). The inspected config blobs do not publish a parameter count, an explicit code-or-weight license entry, per-output coordinate-frame or de-normalization mappings to hardware units, per-feature on-disk image dtype/encoding, explicit image preprocessing/resizing/interpolation contracts, prompt templates, or checkpoint-scoped numeric benchmarks. Where fields are absent or ambiguous in the canonical blobs, I record evidence gaps and list the exact Hugging Face repository blobs and commit pages inspected.

## Identity

- Upstream name: lerobot/xvla-google-robot
- Checkpoint/version: not reported
- Immutable revision: 6c9e9c9028638289c2e02d8a1fc0b8063cdd303b
- Parameter scale: not reported
- Architecture/head: Text encoder: Florence2 (florence_config.model_type = "florence2"); Vision encoder: not reported in inspected config blobs.
- License: not reported
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/6c9e9c9028638289c2e02d8a1fc0b8063cdd303b/model.safetensors, https://huggingface.co/lerobot/xvla-google-robot/commits/main/config.json

## Selection

### Recommended

- **Research experimentation with multimodal vision-language-action policies adapted for Google Robot-like platforms (non-safety-critical research, simulation, and offline evaluation).** — The repository config declares X-VLA policy settings (florence_config.model_type = "florence2"), tokenizer settings (facebook/bart-large, max length 1024), multimodal flags (use_proprio = true, num_image_views = 3), and an action_mode identifier ("ee6d"), which together indicate this checkpoint is a vision-language-action policy artifact appropriate for research/fine-tuning and integration experiments rather than direct hardware actuation.
  Scope: lerobot/xvla-google-robot upstream repository blobs (config.json PR blob and repository tree/weights)
  Evidence: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/6c9e9c9028638289c2e02d8a1fc0b8063cdd303b/model.safetensors

### Conditional

- **Real-robot control on Google Robot-like embodiments (only after embodiment-specific downstream validation and verification of coordinate frames, command units, gripper conventions, and de-normalization mappings).** — Require explicit downstream validation of coordinate frames, command units, gripper conventions, and de-normalization mappings from the action tensor to hardware commands; the inspected canonical config and README blobs do not publish a hardware-safe actuation contract or de-normalization mapping.
  Scope: lerobot/xvla-google-robot upstream repository blobs
  Evidence: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main
- **Using the checkpoint as a compatibility or fine-tuning target inside LeRobot pipelines (research/fine-tuning workflows).** — Apply only with task-specific validation and verification; the canonical README/config expose architecture and tokenizer settings appropriate for adaptation but do not publish checkpoint-scoped transfer metrics or a fine-tuning recipe tied to this exact commit.
  Scope: lerobot/xvla-google-robot upstream repository blobs
  Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### Avoid

- **Sending model outputs directly to physical robot actuators without human supervision, embodiment-specific de-normalization, and hardware safety interlocks.** — Primary sources inspected do not publish coordinate-frame conventions, command-unit mappings, gripper conventions, or an explicit hardware-safe actuation contract for this checkpoint; therefore direct actuation would exceed the documented evidence.
  Scope: lerobot/xvla-google-robot upstream repository blobs
  Evidence: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main

## Input preparation

### Semantic inputs

- The checkpoint accepts textual, visual (image), and proprioceptive/robot-state inputs (multimodal vision-language-action policy). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main
- Proprioceptive inputs are enabled according to the config (use_proprio = true). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- The config declares multiple image observations and an empty-camera count (num_image_views = 3, empty_cameras = 1). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### Accepted formats

- Tokenizer declared as "facebook/bart-large" with tokenizer_max_length = 1024 and tokenizer_padding_side = "right". Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Evidence gap: exact image feature keys, per-feature channel/height/width shapes, and official on-disk image dtype/encoding are not specified in the inspected canonical repository blobs. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main

### Preprocessing

- Evidence gap: explicit image preprocessing steps (resize/pad parameters, interpolation, and color-space conversion) are not specified in the inspected config or repository README blobs. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main
- Evidence gap: explicit state normalization and action de-normalization numeric mappings to hardware units are not published in the inspected canonical files (normalization_mapping entries exist but do not define hardware-unit conversions). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### Pre-submit validation

- Verify that textual inputs do not exceed tokenizer_max_length (1024) before encoding. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Evidence gap: the canonical repository blobs do not document how to handle image inputs that do not match any declared on-disk shape or how to treat excess state dimensions—these behaviors require downstream validation. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main

### Task-specific formatting

- Evidence gap: no official prompt template, instruction-format contract, or episode-packing specification was found in the inspected README/config blobs. Sources: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

## Output interpretation

### Outputs

- The checkpoint config declares n_action_steps = 30 and action_mode = "ee6d" (policy/action-sequence settings present in config.json). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Normalization mapping declarations in the config map STATE->IDENTITY, ACTION->IDENTITY, and VISUAL->MEAN_STD, indicating how some modality-level normalization is intended but not how to de-normalize to hardware units. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### Interpretation

- The model outputs should be interpreted as policy action outputs for downstream systems; the canonical blobs do not provide per-output uncertainty semantics or hardware-unit mappings. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main

### Post-inference validation

- Before hardware execution, downstream validation must ensure generated actions conform to embodiment expectations, numeric range limits, and hardware safety constraints because such mappings are not provided in the canonical repository blobs. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### lerobot/xvla-base — `insufficient-evidence`

- Task: embodiment-specialization for Google Robot platform (robot-control policy transfer/adaptation)
- Criteria: embodiment specialization for Google Robot platforms
- Rationale: No protocol-aligned, checkpoint-scoped numeric benchmark evidence for either lerobot/xvla-google-robot or lerobot/xvla-base was found in the inspected canonical repository blobs for this checkpoint.
- Comparison conditions: No aligned numeric benchmark or protocol evidence present in the checked model repository tree or config blobs.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### allenai/MolmoAct2-SO100_101 — `insufficient-evidence`

- Task: task-aligned robot-control quality comparison
- Criteria: task-aligned robot-control quality
- Rationale: No primary-source, protocol-aligned benchmark evidence for the alternative was present in the checked canonical sources for this dossier; no direct numeric comparison is verifiable from the inspected blobs.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources for this checkpoint scope.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### lerobot/smolvla_libero — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### lerobot/smolvla_libero_plus — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### lerobot/smolvla_robocasa — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### lerobot/smolvla_robotwin — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### lerobot/smolvla_vlabench — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### rail-berkeley/octo-small-1.5 — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### SberRoboticsCenter/GreenVLA-2b-base — `insufficient-evidence`

- Task: robot-control quality comparison
- Criteria: robot-control quality
- Rationale: No protocol- or checkpoint-aligned numeric benchmark evidence was found in the inspected primary sources to support a quantitative comparison.
- Comparison conditions: No aligned primary evidence for the alternative exists in the examined sources.
- Evidence: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

## Limitations and safety

### Limitations

- Evidence gap: An explicit, published model-weight or artifact hash identifying a single immutable released checkpoint artifact is not present in the inspected config.json or README blobs (the repository contains a model weight blob at a committed path but the config.json does not publish a canonical artifact-hash field). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/blob/6c9e9c9028638289c2e02d8a1fc0b8063cdd303b/model.safetensors
- Evidence gap: Parameter count (parameterScale) for this exact checkpoint is not specified in the inspected config or README blobs. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main
- Evidence gap: No checkpoint-scoped public numeric benchmark (table/figure/section/row) tied to this exact repository revision was found in the checked primary sources. Sources: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Evidence gap: The inspected config/README do not specify coordinate-frame conventions, gripper conventions, command units, or explicit de-normalization mappings from ACTION tensor values to hardware commands. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main
- Evidence gap: The canonical blobs do not resolve explicit per-image-feature shapes versus preprocessing resize settings (no explicit per-feature image shapes or preprocessing resolution found). Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main
- Evidence gap: No runtime operational measurements (latency, throughput, control frequency, memory footprint) for this exact checkpoint were published in the inspected primary sources. Sources: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json

### Safety

- Forge policy: Do not send generated actions directly to physical hardware without human oversight, embodiment-specific de-normalization, and hardware safety interlocks because the inspected canonical repository blobs do not provide a safe-actuation contract.
- Evidence gap: The inspected canonical blobs do not publish an upstream privacy or data-handling statement for captured camera observations and robot logs; treat such data according to applicable data-protection practices. Sources: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Use embodiment-specific validation for Google Robot platforms because the checkpoint is described in the repository as adapted for Google Robot-like embodiments while exact frame and command semantics are not specified in the canonical blobs. Sources: https://huggingface.co/lerobot/xvla-google-robot/tree/main, https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Evidence gap: License for model weights and code is not specified in the inspected config.json (license field is null); downstream deployers should verify licensing before reuse. Sources: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/lerobot/xvla-google-robot/tree/main

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### lerobot/xvla-google-robot config.json (PR blob)

- URL: https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json
- Publisher: Hugging Face / LeRobot
- Type: `repository`
- Primary because: Configuration artifact exposing checkpoint-scoped architecture, tokenizer, multimodal settings, action_mode, n_action_steps, normalization mappings, and other configuration parameters used as direct primary evidence.
- Scope: lerobot/xvla-google-robot upstream repository (config.json PR blob)
- Supports: architecture (florence_config entries)
- Supports: tokenizer name and tokenizer_max_length
- Supports: multimodal flags (use_proprio, num_image_views, empty_cameras)
- Supports: action_mode and n_action_steps
- Supports: normalization_mapping entries

### lerobot/xvla-google-robot repository tree (main)

- URL: https://huggingface.co/lerobot/xvla-google-robot/tree/main
- Publisher: Hugging Face / LeRobot
- Type: `repository`
- Primary because: Repository root/tree view used to verify which files are present alongside the checkpoint (README, config, and integration instructions) and general repository-level provenance.
- Scope: lerobot/xvla-google-robot upstream repository (tree/main)
- Supports: presence of README/instructions
- Supports: presence of model files and usage instructions

### lerobot/xvla-google-robot commit history (config.json)

- URL: https://huggingface.co/lerobot/xvla-google-robot/commits/main/config.json
- Publisher: Hugging Face / LeRobot
- Type: `repository`
- Primary because: Commit-history view for config.json used to verify commit events and short commit prefixes referenced in the repository.
- Scope: lerobot/xvla-google-robot upstream repository (config.json commit history)
- Supports: revision/commit history evidence for config.json changes

### lerobot/xvla-google-robot commit page (specific commit)

- URL: https://huggingface.co/lerobot/xvla-google-robot/commits/d5d78f35bf78372900ccf0ab84615a92a52ba575
- Publisher: Hugging Face / LeRobot
- Type: `repository`
- Primary because: Specific commit page inspected to verify commit metadata referenced by the repository.
- Scope: lerobot/xvla-google-robot upstream repository (specific commit view)
- Supports: specific commit metadata

### lerobot/xvla-google-robot model weights blob (committed path)

- URL: https://huggingface.co/lerobot/xvla-google-robot/blob/6c9e9c9028638289c2e02d8a1fc0b8063cdd303b/model.safetensors
- Publisher: Hugging Face / LeRobot
- Type: `repository`
- Primary because: Committed model weight artifact path observed in the repository (used as evidence that a weights blob exists at a specific committed path).
- Scope: lerobot/xvla-google-robot upstream repository (weights blob at commit 6c9e9c9... )
- Supports: presence of model weight file at a committed path

### Exact official starting source declared by Forge

- URL: https://huggingface.co/lerobot/xvla-google-robot
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: huggingface-lerobot-xvla
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: An explicit published model-weight artifact hash or single canonical immutable artifact identifier is not declared in the repository config.json or README blobs; inspected https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and https://huggingface.co/lerobot/xvla-google-robot/tree/main and found no canonical artifact-hash field.
- Evidence gap: Parameter count (parameterScale) for this exact checkpoint is not reported in the inspected config or README blobs; inspected https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and https://huggingface.co/lerobot/xvla-google-robot/tree/main and found no parameter-count entry.
- Evidence gap: No checkpoint-scoped public numeric benchmark rows tied to this exact repository revision were found in the inspected model repository files; inspected https://huggingface.co/lerobot/xvla-google-robot/tree/main and https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and found no benchmark tables or numeric results.
- Evidence gap: Coordinate-frame conventions, gripper conventions, command-unit mappings, and explicit de-normalization mappings from ACTION tensor values to hardware commands are not specified in the inspected canonical blobs; inspected https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and https://huggingface.co/lerobot/xvla-google-robot/tree/main and found no such mappings.
- Evidence gap: Exact per-image-feature shapes versus preprocessing resize settings (on-disk image shapes, dtypes, and explicit resize/pad rules) are not resolved in the inspected canonical files; inspected https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and https://huggingface.co/lerobot/xvla-google-robot/tree/main and found no explicit per-feature image-shape or preprocessing contract.
- Evidence gap: No official prompt template, instruction-format contract, or episode-packing specification was found in the inspected README/config blobs; inspected https://huggingface.co/lerobot/xvla-google-robot/tree/main and https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and found none.
- Evidence gap: Tokenizer truncation/truncation-semantics when textual inputs exceed tokenizer_max_length (1024) are not documented in the inspected config blobs; inspected https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and found no truncation-policy field.
- Evidence gap: No latency, throughput, memory, control-frequency, batching, or episode-window operational measurements for this exact checkpoint are published in the inspected primary sources; inspected https://huggingface.co/lerobot/xvla-google-robot/tree/main and https://huggingface.co/lerobot/xvla-google-robot/blob/refs%2Fpr%2F1/config.json and found no runtime measurements.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses unapproved repository owner '2toinf' for this exact model scope: $.sources[6] uses unapproved repository owner '2toinf' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner '2toinf' for this exact model scope: $.sources[7] uses unapproved repository owner '2toinf' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/lerobot/xvla-google-robot: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
