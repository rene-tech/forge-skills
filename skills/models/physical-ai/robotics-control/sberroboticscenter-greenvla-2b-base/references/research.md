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

- Research key: `huggingface-co-sberroboticscenter-greenvla-2b-base-cec19986f2`
- Independent audit: `revised`
- Researched: `2026-08-06T10:13:40.333855+00:00`

The SberRoboticsCenter/GreenVLA-2b-base checkpoint (revision 8a511e28507447508dd80eae1b6a12e64021409a) is documented on its Hugging Face model page, README, and config blobs as a Vision-Language-Action (VLA) model of approximately 2 billion parameters. The repository config and commits declare inference_mode = "flow_matching", precision = "bfloat16", input image_keys ["base_0_rgb","left_wrist_0_rgb","right_wrist_0_rgb"], image_shape [448, 448], tokenizer_max_length = 832, normalization_mode = "quantile", and a set of flow-matching and action-space flags (for example state_noise_amplitude = 0.1, state_dropout_prob = 0.5, n_action_steps = 10, max_action_dim = 48). The README and commit metadata list VLM capabilities (Visual Question Answering, object pointing, bounding-box prediction, scene description) and state that the checkpoint provides autoregressive discrete action prediction via FAST token-based action generation. The checkpoint primary sources do not publish a robot_state schema (field names, units, ordering), an explicit robot_action output JSON schema or token→action decoding table, checkpoint-scoped numeric benchmarks, prompt templates for paired image+text+robot_state inputs, or post-inference deployment safety procedures; these are recorded as evidence gaps tied to the inspected README/config/commit artifacts.

## Identity

- Upstream name: SberRoboticsCenter/Qwen3-VL-2B-Instruct-action
- Checkpoint/version: SberRoboticsCenter/GreenVLA-2b-base
- Immutable revision: 8a511e28507447508dd80eae1b6a12e64021409a
- Parameter scale: approximately 2 billion parameters
- Architecture/head: Vision-Language-Action (VLA); inference_mode="flow_matching" (as declared in checkpoint config)
- License: apache-2.0
- Evidence: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blame/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commits/main, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/58aeae14740bcc313e1915a200e7ce8fa0cca3df, https://huggingface.co/SberRoboticsCenter/Qwen3-VL-2B-Instruct-action/tree/main, https://huggingface.co/SberRoboticsCenter/Qwen3-VL-2B-Instruct-action/commit/4d37394bf15a027d06bf1b4409824da736bb7065, https://arxiv.org/abs/2602.00919, https://huggingface.co/SberRoboticsCenter/GreenVLA-5b-base-stride-4/blob/20c1599c0dd528273f40a494a66757e918ce806f/README.md

## Selection

### Recommended

- **Vision-language instruction following to generate discrete robot actions from image+text inputs (research / controlled evaluation)** — Repository README and commit metadata describe VLA capabilities and autoregressive FAST token-based discrete action generation; config.json defines image_keys, image_shape, and tokenizer_max_length consistent with image+text inputs.
  Scope: SberRoboticsCenter/GreenVLA-2b-base (checkpoint revision 8a511e28507447508dd80eae1b6a12e64021409a)
  Evidence: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- **Visual question answering and scene description in robotics research contexts (non-safety-critical evaluation)** — README and commit list VLM capabilities including Visual Question Answering and scene description for the checkpoint.
  Scope: SberRoboticsCenter/GreenVLA-2b-base
  Evidence: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

### Conditional

- **Embodiment-specific policy tuning and deployment (requires embodiment mapping and safety validation)** — Requires explicit embodiment mapping into the unified action space, development of embodiment masks and slot mappings, and extensive hardware safety validation prior to physical deployment; checkpoint repository does not publish per-robot mapping artifacts, while the family paper describes the unified action-space abstraction.
  Scope: SberRoboticsCenter/GreenVLA-2b-base (requires downstream embodiment adapter/mapper)
  Evidence: https://arxiv.org/abs/2602.00919, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json

### Avoid

- **Direct deployment on physical robots without embodiment mapping and hardware safety validation** — Evidence gap: primary repository and config do not document deployment safety guidance, runtime safety checks, or per-robot action-slot mappings required to safely bridge model outputs to actuator commands.
  Scope: SberRoboticsCenter/GreenVLA-2b-base
  Evidence: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json

## Input preparation

### Semantic inputs

- Text prompts in natural language describing tasks or instructions; tokenizer_max_length is 832 as declared in config.json. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Image observations provided under image_keys ["base_0_rgb","left_wrist_0_rgb","right_wrist_0_rgb"] with declared image_shape [448, 448]. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Robot_state input semantics (field names beyond image_keys, units, ordering, and numerical ranges) are not specified in the checkpoint primary sources. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json

### Accepted formats

- Images: config.json declares image inputs via image_keys and an image_shape of [448, 448]; exact image file encodings (JPEG/PNG) are not specified in primary sources. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md
- Text: tokenizer_max_length is 832 as declared in config.json; the config does not enumerate exact tokenizer encoding details beyond max length. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Robot_state: Evidence gap: primary sources do not specify a robot_state format/schema or units. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

### Preprocessing

- Image preprocessing: images are declared with shape [448, 448]; normalization_mode is declared as "quantile" in config.json. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Text preprocessing: enforce tokenizer_max_length <= 832 as declared in config.json. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Model config documents training/flow settings such as state_noise_amplitude=0.1 and state_dropout_prob=0.5 which relate to flow-matching behavior; these are configuration flags but do not define operational input normalization for deployment. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/58aeae14740bcc313e1915a200e7ce8fa0cca3df

### Pre-submit validation

- Validate textual input token length does not exceed tokenizer_max_length (832) before inference (tokenizer_max_length declared in config.json). Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Validate presence of required image_keys ["base_0_rgb","left_wrist_0_rgb","right_wrist_0_rgb"] and that images conform to the declared image_shape [448, 448] prior to submission. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Robot_state validation rules (expected fields, ranges, units, and ordering) are not specified in primary sources; Evidence gap: robot_state validation unspecified. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

### Task-specific formatting

- Config enables control metadata fields via add_control_mode and add_embodiment_name flags (both declared true in config.json); include those control fields in paired input where required by downstream embodiment mapping. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Evidence gap: README/config do not provide explicit prompt templates, example prompts, or exact paired-input ordering for image+text+robot_state inputs for this checkpoint. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

## Output interpretation

### Outputs

- Primary sources state the model generates actions autoregressively using FAST token-based action generation for discrete control (discrete action tokens). Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md
- Evidence gap: primary sources do not document exact robot_action output JSON schema, field names, token-to-action decoding table, or numeric action slot ranges for this checkpoint. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

### Interpretation

- ArXiv description of Green-VLA presents a unified action space mapping Φ_e and an embodiment mask m_e that determine which action slots apply for a robot; interpreting discrete action tokens requires mapping to that unified action space per-embodiment (family-level formalism, not checkpoint-scoped artifact). Sources: https://arxiv.org/abs/2602.00919
- Do not assume numeric meanings for action token indices without using an embodiment mapping and mask as described in the Green-VLA paper; the checkpoint repo does not publish per-robot slot mappings for this checkpoint (evidence gap). Sources: https://arxiv.org/abs/2602.00919, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json

### Post-inference validation

- Evidence gap: post-inference validation, calibration, and safety checks (sanity checks on actions, clamping, collision checks) are not defined in the checkpoint primary sources and must be implemented downstream by integrators. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### SberRoboticsCenter/Qwen3-VL-2B-Instruct-action — `insufficient-evidence`

- Task: vision-language instruction following / base VLM comparison
- Criteria: Different model roles: Qwen3-VL-2B-Instruct-action is referenced as the upstream base VLM; GreenVLA-2b-base is a VLA policy checkpoint built on that base. No same-protocol numeric evaluation comparing the upstream VLM and this checkpoint for identical datasets/splits is published in the checkpoint primary sources.
- Rationale: Config and README identify an upstream base VLM but do not provide protocol-matched, checkpoint-scoped benchmark tables for direct comparison; the arXiv paper provides family-level formalism but not checkpoint-scoped same-protocol numeric comparisons tied to this checkpoint.
- Comparison conditions: Inspected README, config.json, checkpoint commit, and upstream repository landing but found no checkpoint-scoped benchmark rows for identical protocols.
- Evidence: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/Qwen3-VL-2B-Instruct-action/tree/main, https://arxiv.org/abs/2602.00919

## Limitations and safety

### Limitations

- Evidence gap: The primary repository does not enumerate explicit limitations for GreenVLA-2b-base (known failure modes, safety margins, per-embodiment constraints) beyond high-level family descriptions. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a

### Safety

- Evidence gap: No explicit safety, privacy, or deployment warnings or required human-in-the-loop mitigations are documented in the checkpoint primary sources; integrators must apply hardware safety engineering and human review before physical deployment. Sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json, https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blame/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### GreenVLA-2b-base (landing)

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Hugging Face model landing page for the exact checkpoint repository.
- Scope: GreenVLA-2b-base
- Supports: GreenVLA-2b-base

### GreenVLA-2b-base README

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md
- Publisher: SberRoboticsCenter
- Type: `official-documentation`
- Primary because: Primary README content describing model family, capabilities, and linked citation; used to verify capabilities, parameter-scale statement, and absence of checkpoint-scoped benchmarks and robot_state schema.
- Scope: GreenVLA-2b-base
- Supports: GreenVLA-2b-base
- Supports: family description
- Supports: capabilities statement
- Supports: parameter scale (approximate)

### GreenVLA-2b-base config.json

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Config file enumerating model_type, inference_mode, precision, image_shape, image_keys, tokenizer_max_length, normalization_mode, and other checkpoint flags.
- Scope: GreenVLA-2b-base
- Supports: model_type
- Supports: inference_mode
- Supports: precision
- Supports: image_shape
- Supports: image_keys
- Supports: tokenizer_max_length
- Supports: normalization_mode
- Supports: state_noise_amplitude
- Supports: state_dropout_prob
- Supports: add_control_mode
- Supports: add_embodiment_name
- Supports: default_temperature
- Supports: n_obs_steps
- Supports: n_action_steps
- Supports: max_state_dim
- Supports: max_action_dim
- Supports: add_action_space_factorization
- Supports: apply_noise_to_state_for_flow_matching
- Supports: mask_padded_actions
- Supports: enable_learnable_layer_combination
- Supports: layer_combination_init
- Supports: ce_loss_weight

### GreenVLA-2b-base commit 8a511e28507447508dd80eae1b6a12e64021409a

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Exact commit referenced as the checkpoint revision and containing descriptive commit metadata used to verify claimed revision-level facts and capabilities.
- Scope: GreenVLA-2b-base
- Supports: checkpoint revision
- Supports: capabilities statement
- Supports: parameter scale (approximate)

### GreenVLA-2b-base commits index

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commits/main
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Repository commits index showing commit history and initial release commit metadata.
- Scope: GreenVLA-2b-base
- Supports: commit history
- Supports: initial release hash

### GreenVLA-2b-base README blame

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blame/main/README.md
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Blame view showing README provenance and license metadata.
- Scope: GreenVLA-2b-base
- Supports: README citation
- Supports: license

### GreenVLA-2b-base commit 58aeae14740bcc313e1915a200e7ce8fa0cca3df

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/58aeae14740bcc313e1915a200e7ce8fa0cca3df
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Commit containing config.json edits and explicit config key values used to verify config fields.
- Scope: GreenVLA-2b-base
- Supports: config.json key values
- Supports: inference_mode
- Supports: precision
- Supports: image_shape

### SberRoboticsCenter/Qwen3-VL-2B-Instruct-action (upstream repo)

- URL: https://huggingface.co/SberRoboticsCenter/Qwen3-VL-2B-Instruct-action/tree/main
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Upstream base VLM repository referenced by the GreenVLA checkpoint config/commit; used only as upstream-checkpoint evidence.
- Scope: Qwen3-VL-2B-Instruct-action
- Supports: upstream base model reference

### SberRoboticsCenter/Qwen3-VL-2B-Instruct-action README commit (upstream reference)

- URL: https://huggingface.co/SberRoboticsCenter/Qwen3-VL-2B-Instruct-action/commit/4d37394bf15a027d06bf1b4409824da736bb7065
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Upstream repository commit used to verify upstream base model references from the GreenVLA repositories.
- Scope: Qwen3-VL-2B-Instruct-action
- Supports: upstream base model reference

### Green-VLA arXiv preprint (2602.00919)

- URL: https://arxiv.org/abs/2602.00919
- Publisher: arXiv / SberRoboticsCenter authors
- Type: `paper`
- Primary because: ArXiv preprint providing the staged Green-VLA training recipe and unified action-space formalism; used as family-level upstream evidence for formalism (Φ_e, m_e).
- Scope: GreenVLA family (paper-level)
- Supports: unified action space
- Supports: staged training recipe
- Supports: family-level formalism

### GreenVLA-5b-base README (cross-reference)

- URL: https://huggingface.co/SberRoboticsCenter/GreenVLA-5b-base-stride-4/blob/20c1599c0dd528273f40a494a66757e918ce806f/README.md
- Publisher: SberRoboticsCenter
- Type: `repository`
- Primary because: Related GreenVLA family README used as corroborating first-party documentation mentioning GreenVLA-2b-base parameter scale.
- Scope: GreenVLA-5b-base (family cross-reference)
- Supports: parameter scale cross-reference

## Evidence gaps

- Evidence gap: The primary repository does not specify a robot_state schema (field names, units, ordering) for inputs to this checkpoint. Files/paths inspected: README.md blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md), config.json blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json), and commit 8a511e28507447508dd80eae1b6a12e64021409a (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a).
- Evidence gap: Exact robot_action output JSON schema, token→action decoding table, and per-slot numeric ranges are not provided in the checkpoint primary sources. Files/paths inspected: README.md blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md), config.json blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json), commit 8a511e28507447508dd80eae1b6a12e64021409a (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a).
- Evidence gap: No checkpoint-scoped public numeric benchmark rows (dataset/split/metric/value) were found for SberRoboticsCenter/GreenVLA-2b-base in the README, config.json, commit metadata, or commits index. Files/paths inspected: README.md blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md), config.json blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json), commit page (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a), commits index (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commits/main), and arXiv paper abstract (https://arxiv.org/abs/2602.00919) for family-level claims.
- Evidence gap: Prompt templates and exact paired-input formatting examples for image+text+robot_state are not present in the primary README/config; files/paths inspected: README.md blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md), config.json blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json), commit 8a511e28507447508dd80eae1b6a12e64021409a (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/commit/8a511e28507447508dd80eae1b6a12e64021409a).
- Evidence gap: Post-inference validation and deployment safety procedures are not specified in the checkpoint primary sources; files/paths inspected: README.md blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/README.md), config.json blob (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blob/main/config.json), blame view (https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base/blame/main/README.md).
- Evidence gap: Comparison-specific evidence gap for protocol-matched numeric comparisons between SberRoboticsCenter/GreenVLA-2b-base and SberRoboticsCenter/Qwen3-VL-2B-Instruct-action. Files/paths inspected: GreenVLA README and config (README blob and config.json blob), GreenVLA commits index and commit 8a511e28507447508dd80eae1b6a12e64021409a, upstream Qwen3-VL-2B-Instruct-action repository (https://huggingface.co/SberRoboticsCenter/Qwen3-VL-2B-Instruct-action/tree/main), and Green-VLA arXiv abstract (https://arxiv.org/abs/2602.00919).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 25 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation: $.inputPreparation: missing required property acceptedFormats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property preprocessing Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property taskSpecificFormatting Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property validation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[3] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[4] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[5] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[6] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[7] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[8] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[9] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[10] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[11] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'collections' for this exact model scope: $.sources[13] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[14] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_robocasa Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
