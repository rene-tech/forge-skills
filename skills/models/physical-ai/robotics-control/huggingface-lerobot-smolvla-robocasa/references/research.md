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

- Research key: `huggingface-co-lerobot-smolvla-robocasa-88ddb05336`
- Independent audit: `revised`
- Researched: `2026-08-06T12:08:14.255398+00:00`

Primary upstream evidence verifies the exact checkpoint upstreamName lerobot/smolvla_robocasa at revision b828f0619690645c9e306cedcc09e17b422339e4 (Hugging Face model page and the commit page). Family-level description on the model card and commit-scoped metadata identify SmolVLA as a compact vision-language-action policy suitable for RoboCasa use. The commit metadata (commit page) lists chunk_size=50, n_action_steps=50, output_features includes an action feature type ACTION with shape [12], max_state_dim=32, max_action_dim=32, resize_imgs_with_padding=[512,512], and normalization_mapping mapping VISUAL->IDENTITY, STATE->MEAN_STD, ACTION->MEAN_STD. The primary findings do not report a parameter count, do not provide an explicit model-weight or code license string on the commit page, and do not include any checkpoint-scoped public benchmark table rows, serialized request schema, explicit robot-state field names, action units/bounds, or calibrated output-confidence semantics.

## Identity

- Upstream name: lerobot/smolvla_robocasa
- Checkpoint/version: lerobot/smolvla_robocasa
- Immutable revision: b828f0619690645c9e306cedcc09e17b422339e4
- Parameter scale: not reported
- Architecture/head: SmolVLA-family vision-language-action policy
- License: not reported
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4, https://github.com/huggingface/lerobot/issues/1377

## Selection

### Recommended

- **Use as a RoboCasa robotics policy checkpoint within the LeRobot framework** — The Hugging Face model card identifies the checkpoint as lerobot/smolvla_robocasa and describes SmolVLA as a compact vision-language-action model trained/pushed using LeRobot (model-card).
  Scope: lerobot/smolvla_robocasa
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa
- **Family-level SmolVLA fine-tuning or adaptation workflows using the LeRobot toolchain (apply cautiously to this checkpoint)** — The model card indicates SmolVLA family intent and that the model was trained/pushed with LeRobot; this supports family-level fine-tuning/adaptation guidance but not checkpoint-scoped templates.
  Scope: Family-level SmolVLA guidance cautiously applied to lerobot/smolvla_robocasa
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa
- **RoboCasa-targeted development using the training-data lineage stated in the checkpoint commit metadata** — The commit metadata lists pretrained_path 'lerobot/smolvla_base' and identifies the checkpoint as tied to RoboCasa-target training metadata (commit page).
  Scope: lerobot/smolvla_robocasa revision b828f0619690645c9e306cedcc09e17b422339e4
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### Conditional

- **Deployment on consumer-grade hardware (validate runtime suitability before production)** — Model card asserts deployability on consumer-grade hardware but the commit metadata does not provide checkpoint-specific latency, memory, throughput, or control-loop validation; downstream runtime validation required.
  Scope: lerobot/smolvla_robocasa (checkpoint page claim applied cautiously)
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- **Integrating checkpoint where exact observation/action schema compatibility matters** — Commit metadata lists chunk_size=50, n_action_steps=50, max_state_dim=32, max_action_dim=32 and action shape [12], but the serialized request schema and exact field names are not provided; downstream validation required.
  Scope: lerobot/smolvla_robocasa revision b828f0619690645c9e306cedcc09e17b422339e4
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### Avoid

- **Selecting this checkpoint on the basis of verified public benchmark superiority** — No checkpoint-scoped public benchmark table rows (dataset, split, metric, value) were present in the checked primary sources for lerobot/smolvla_robocasa.
  Scope: lerobot/smolvla_robocasa
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4, https://github.com/huggingface/lerobot/issues/1377
- **Treating the checkpoint as a fully specified control-interface contract (serialized request schema, robot-state field names, action units/bounds, confidence semantics)** — Commit metadata and model card provide configuration values but do not expose a full serialized request schema, explicit robot-state field names, action units or bounds, or output-confidence semantics for this checkpoint.
  Scope: lerobot/smolvla_robocasa
  Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

## Input preparation

### Semantic inputs

- The model accepts vision (multi-camera) inputs as part of SmolVLA family behavior (family-level description in model card). Sources: https://huggingface.co/lerobot/smolvla_robocasa
- The model accepts robot sensorimotor state as an input (family-level SmolVLA description on the model card). Sources: https://huggingface.co/lerobot/smolvla_robocasa
- The model conditions on a natural-language instruction (family-level SmolVLA description on the model card). Sources: https://huggingface.co/lerobot/smolvla_robocasa

### Accepted formats

- Hugging Face model card provides usage instructions for inference via libraries, inference providers, notebooks, and local applications (no checkpoint-scoped serialized request schema provided). Sources: https://huggingface.co/lerobot/smolvla_robocasa
- Evidence gap: The primary findings do not specify the full serialized request schema or explicit robot-state field names for this checkpoint. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### Preprocessing

- Images are resized with padding to [512, 512] (commit metadata lists resize_imgs_with_padding = [512, 512]). Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Normalization mapping in commit metadata: VISUAL -> IDENTITY. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Normalization mapping in commit metadata: STATE -> MEAN_STD. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Normalization mapping in commit metadata: ACTION -> MEAN_STD. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- pad_language_to is set to 'max_length' and add_image_special_tokens is false in the commit metadata. Sources: https://github.com/huggingface/lerobot/issues/1377, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### Pre-submit validation

- Validate that inputs do not exceed configured dimensional caps: max_state_dim = 32 and max_action_dim = 32 (commit metadata). Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4, https://github.com/huggingface/lerobot/issues/1377
- Evidence gap: The primary findings do not specify batching limits, truncation behavior beyond pad_language_to, or an exact observation-history length (n_obs_steps is reported in an issue snippet but full serialized schema is absent). Sources: https://github.com/huggingface/lerobot/issues/1377, https://huggingface.co/lerobot/smolvla_robocasa

### Task-specific formatting

- Family-level documentation (model card) states SmolVLA conditions on natural language, multi-camera views, and robot state to generate an action chunk; no checkpoint-scoped prompt template is provided. Sources: https://huggingface.co/lerobot/smolvla_robocasa
- Evidence gap: No exact official prompt template or serialized request example for lerobot/smolvla_robocasa was found in the checked primary sources. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

## Output interpretation

### Outputs

- Commit metadata lists an output feature named 'action' with type 'ACTION' and shape [12]. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Commit metadata lists chunk_size = 50 and n_action_steps = 50 (these configure action-chunk length at the checkpoint level). Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Family-level documentation describes outputs as action chunks (model card). Sources: https://huggingface.co/lerobot/smolvla_robocasa

### Interpretation

- Interpret the model outputs as robot-action feature vectors (the commit metadata and model card describe action generation; no confidence-score semantics are provided). Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Evidence gap: The primary findings do not specify action units, explicit action bounds, or calibrated confidence semantics for outputs. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### Post-inference validation

- Post-inference validation should confirm downstream consumers interpret outputs consistent with type ACTION and shape [12], and apply ACTION normalization (commit metadata maps ACTION -> MEAN_STD). Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Evidence gap: The primary findings do not describe calibrated quality, robustness checks, or acceptance/rejection rules for individual actions. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://github.com/huggingface/lerobot/issues/1377

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### allenai/MolmoAct2-SO100_101 — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows were found comparing lerobot/smolvla_robocasa to this alternative on the same dataset/split/metric.
- Rationale: Checked the checkpoint's model card and commit metadata; neither contains a protocol-matched benchmark row comparing the exact checkpoints.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### lerobot/smolvla_libero — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: Model card and commit page do not present direct comparative benchmark rows between lerobot/smolvla_robocasa and lerobot/smolvla_libero.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### lerobot/smolvla_libero_plus — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### lerobot/smolvla_robotwin — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### lerobot/smolvla_vlabench — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### lerobot/xvla-base — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### lerobot/xvla-google-robot — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### rail-berkeley/octo-small-1.5 — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### SberRoboticsCenter/GreenVLA-2b-base — `insufficient-evidence`

- Task: Robotics-control comparison
- Criteria: No protocol-matched primary benchmark rows comparing these exact checkpoints were present in the checked sources.
- Rationale: No direct comparison rows or protocol-matched evaluations found on the checkpoint's model card or commit page.
- Comparison conditions: No shared dataset/split/metric rows present in the checked sources.
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

## Limitations and safety

### Limitations

- No checkpoint-scoped public benchmark rows (dataset, split, metric, numeric value) were found in the checked primary sources. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Parameter count for this exact checkpoint is not reported in the checked primary sources. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- The checked primary findings do not provide a full serialized input contract (explicit robot-state field names or complete request schema). Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://github.com/huggingface/lerobot/issues/1377
- Action units, explicit action bounds, and confidence-score semantics for outputs are not specified in the checked primary sources. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4, https://huggingface.co/lerobot/smolvla_robocasa
- The commit metadata's 'license' field is null; no distinct code license or model-weight license string is reported in the checked primary sources. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4

### Safety

- Evidence gap: The checked primary sources do not report checkpoint-specific safety-validation criteria, action-filtering rules, or calibrated acceptance/rejection rules for model outputs. Sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Evidence gap: Because action units and bounds are not reported, downstream human review and controlled validation are recommended before safety-critical actuation. Sources: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Evidence gap: The checked primary sources do not specify privacy, clinical, or biosecurity handling requirements for this checkpoint. Sources: https://huggingface.co/lerobot/smolvla_robocasa

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### lerobot/smolvla_robocasa

- URL: https://huggingface.co/lerobot/smolvla_robocasa
- Publisher: Hugging Face LeRobot
- Type: `model-card`
- Primary because: Official upstream model page for the exact checkpoint named in scope; contains family description and usage instructions.
- Scope: lerobot/smolvla_robocasa
- Supports: identity
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: avoidUseCases
- Supports: inputPreparation
- Supports: outputInterpretation
- Supports: limitations
- Supports: safety

### smolvla_robocasa commit b828f0619690645c9e306cedcc09e17b422339e4

- URL: https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4
- Publisher: Hugging Face LeRobot
- Type: `model-card`
- Primary because: Official commit page for the exact checkpoint revision; contains checkpoint-scoped configuration metadata (chunk_size, n_action_steps, output_features, normalization mapping, max dims, resize settings).
- Scope: lerobot/smolvla_robocasa revision b828f0619690645c9e306cedcc09e17b422339e4
- Supports: identity
- Supports: researchSummary
- Supports: conditionalUseCases
- Supports: inputPreparation
- Supports: outputInterpretation
- Supports: limitations
- Supports: safety

### GitHub issue: lerobot #1377

- URL: https://github.com/huggingface/lerobot/issues/1377
- Publisher: GitHub - Hugging Face/lerobot
- Type: `repository`
- Primary because: Repository issue page included in the provided research findings and containing additional reported configuration snippets used as primary evidence in this dossier.
- Scope: lerobot/smolvla family/config snippets
- Supports: inputPreparation
- Supports: limitations
- Supports: researchSummary

## Evidence gaps

- Evidence gap: No checkpoint-scoped public benchmark rows (dataset, split, metric, numeric value) found in the checked primary URLs: https://huggingface.co/lerobot/smolvla_robocasa (model card), https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4 (commit page), https://github.com/huggingface/lerobot/issues/1377 (repo issue).
- Evidence gap: Parameter count for lerobot/smolvla_robocasa is not reported in the checked primary sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4.
- Evidence gap: The full serialized input schema and explicit robot-state field names for this checkpoint are not present in the checked primary sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4.
- Evidence gap: Action units, explicit action bounds, and calibrated output-confidence semantics are not present in the checked primary sources: https://huggingface.co/lerobot/smolvla_robocasa, https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4.
- Evidence gap: A distinct code license or model-weight license string is not reported in the commit metadata (license field is null) at https://huggingface.co/lerobot/smolvla_robocasa/commit/b828f0619690645c9e306cedcc09e17b422339e4.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://huggingface.co/papers/2506.01844 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[2] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[3] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[2] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[2] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[5] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[5] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[3] without evidence must be labeled as a Forge policy or evidence gap: $.safety[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
