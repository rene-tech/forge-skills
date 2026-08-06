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

- Research key: `huggingface-co-lerobot-xvla-base-b834a228b7`
- Independent audit: `revised`
- Researched: `2026-08-06T12:22:22.185611+00:00`

Authoritative primary sources for lerobot/xvla-base present the checkpoint as the X-VLA base model (a soft-prompted, flow-matching Vision‑Language‑Action Transformer) with a reported parameter scale of 0.9 billion parameters. Primary documentation (Hugging Face docs and the repository) describes a two-phase training workflow (Phase I pretraining on ~290,000 episodes from Droid, Robomind, and Agibot spanning seven platforms and five arm types; Phase II domain adaptation using soft prompts). The inspected primary sources describe action-dimensionality handling: a pretrained compatibility max_action_dim of 20, padding of lower-dimensional dataset actions to 20 during training, and trimming to the real action dimension at deployment; an `auto` action mode is described for dimension detection. The processor/implementation-level files and docs describe three visual inputs as default and extraction of end-effector position (3D), axis-angle orientation (3D), and gripper joint positions (2D) into observation.state. The canonical preprint, model card, and docs identify X-VLA as soft-prompted and flow-matching. Primary sources do not report an immutable checkpoint artifact name or commit hash for lerobot/xvla-base, do not provide checkpoint-scoped numeric benchmark tables for lerobot/xvla-base itself, and do not provide tokenizer configuration or explicit image normalization (mean/std) or full robot_state field units and ordering for the base checkpoint. Where the canonical primary sources are silent, explicit evidence gaps are recorded.

## Identity

- Upstream name: lerobot/xvla-base
- Checkpoint/version: lerobot/xvla-base
- Immutable revision: not reported
- Parameter scale: 0.9 billion parameters
- Architecture/head: Soft-prompted, flow-matching Vision‑Language‑Action transformer (X-VLA)
- License: Repository LICENSE file states MIT; other repo-adjacent metadata referenced in findings claimed Apache-2.0 (evidence conflict — see evidenceUrls)
- Evidence: https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla, https://arxiv.org/abs/2510.10274

## Selection

### Recommended

- **Foundation policy pretraining and backbone for cross-embodiment research (Phase I pretrained backbone for downstream Phase II adaptation).** — Hugging Face docs and the model card present the checkpoint as the X-VLA base model intended for Phase I pretraining and as a pretrained backbone for Phase II adaptation; the paper and docs describe soft prompts and cross-embodiment methodology supporting this use.
  Scope: lerobot/xvla-base
  Evidence: https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base, https://arxiv.org/abs/2510.10274
- **Research and development of soft-prompted cross-embodiment policies and Phase II domain-adaptation experiments (simulation and multi-platform pretraining research).** — The canonical paper and Hugging Face docs describe soft prompts as the mechanism to represent hardware/domain variation and document Phase II domain adaptation practices, indicating the base checkpoint is suitable as a research backbone for soft-prompt and cross-embodiment method development.
  Scope: lerobot/xvla-base (used as pretrained backbone for Phase II soft-prompt adaptation)
  Evidence: https://arxiv.org/abs/2510.10274, https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base

### Conditional

- **Adaptation to a specific real robot platform for safe deployment (Phase II domain adaptation and postprocessing to match robot action space).** — Requires Phase II domain-adaptation per the docs: introduce and optimize soft prompts for the target embodiment and apply postprocessing to trim the model's 20-dimensional outputs to the robot's real action dimension. Follow Phase II best-practice guidance in the docs (soft prompts encode hardware configuration while the backbone is adapted/frozen as documented).
  Scope: lerobot/xvla-base as Phase I pretrained backbone, followed by Phase II adaptation
  Evidence: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- **Using learned soft prompts to represent a new hardware embodiment or domain for policy fine-tuning.** — Create and train soft-prompt embeddings during Phase II adaptation to encode embodiment/domain differences; follow the documentation's Phase II recommendations.
  Scope: lerobot/xvla-base backbone with new soft prompts trained during Phase II
  Evidence: https://arxiv.org/abs/2510.10274, https://huggingface.co/docs/lerobot/en/xvla

### Avoid

- **Direct deployment of the raw base checkpoint as a final real-robot controller without Phase II adaptation or appropriate action postprocessing.** — Primary documentation describes the base checkpoint as offering a 20-dimensional output for pretrained compatibility and documents padding/trimming behavior (20↔real_dim) and an `auto` action mode; the base checkpoint is presented as a pretrained backbone that requires Phase II adaptation and appropriate postprocessing for deployment.
  Scope: lerobot/xvla-base
  Evidence: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- **Assuming numeric benchmarked performance (checkpoint-scoped success rates) for lerobot/xvla-base without Phase II evaluation.** — Hugging Face documentation reports numeric results for other named checkpoints (e.g., lerobot/xvla-libero, lerobot/xvla-widowx, lerobot/xvla-folding) but does not attribute checkpoint-scoped numeric evaluation tables to lerobot/xvla-base in the inspected canonical sources.
  Scope: lerobot/xvla-base
  Evidence: https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base

## Input preparation

### Semantic inputs

- Inputs accepted by X-VLA include text, multi-view images, and robot_state/proprioceptive data. Sources: https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla
- X-VLA treats each hardware setup as a 'task' and represents embodiment/domain differences via learnable soft-prompt embeddings during Phase II adaptation. Sources: https://arxiv.org/abs/2510.10274, https://huggingface.co/docs/lerobot/en/xvla

### Accepted formats

- Primary sources document the conceptual modalities (text, images, robot_state) but do not specify file-level image formats or tokenizer file names for the base checkpoint in the inspected canonical sources. Sources: https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- The project supports multiple camera views and defaults to three visual inputs; the docs reference configuration (e.g., num_image_views) to control number of views. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot

### Preprocessing

- During training, dataset actions with smaller dimensionality are padded up to the pretrained compatibility dimension (max_action_dim = 20); at deployment predicted 20-dimensional outputs are trimmed to the dataset/robot real action dimension; an `auto` action mode for dimension detection and pad/trim behavior is described in the docs. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- Processor-level implementation extracts end-effector position (3D), converts orientation into axis-angle (3D), and extracts gripper joint positions (2D) from robot_state and maps them into observation.state; image pipeline multiplies image values by 255 as part of scaling (the processor pipeline also includes image flipping/rotation behavior). Sources: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla
- Default expectation is for three visual inputs (image, image2, image3) and a mechanism exists to add empty/masked camera slots when fewer cameras are present; rename-map support maps source image keys to the policy's expected keys. Sources: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla

### Pre-submit validation

- Primary sources do not provide explicit numeric ranges, units, or schema-level ordering for robot_state fields (units for end-effector positions, axis-angle units, or joint position units are not specified in the inspected canonical sources). Sources: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla
- Primary sources do not supply a tokenizer configuration or tokenizer files for text inputs for the lerobot/xvla-base checkpoint in the inspected canonical locations. Sources: https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot
- Image normalization parameters (means, standard deviations, and color-space conventions) are not specified for the base checkpoint in the inspected canonical sources. Sources: https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot

### Task-specific formatting

- Canonical docs describe X-VLA configuration and training phases; project documentation references model installation (e.g., pip install) and configuration knobs to control image-view count and action-dimension handling, but the inspected canonical sources do not expose an explicit example prompt template or tokenizer spec for text inputs tied to the base checkpoint. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot
- The canonical documentation describes Phase I/Phase II workflow and mapping of dataset/domain IDs (domain ID list and enumerations are published in the docs). Sources: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot

## Output interpretation

### Outputs

- The pretrained compatibility output dimension is described as 20 (max_action_dim = 20); model training pads/produces 20-dimensional action vectors and loss is computed only on the real action dimensions; postprocessing trims predictions to the target robot's real action dimension. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- Processor-level mappings place extracted robot_state features into observation.state suitable for downstream policy consumption (end-effector position 3D, orientation axis-angle 3D, gripper joints 2D), forming input to the action head. Sources: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla

### Interpretation

- Primary sources do not provide calibrated probabilistic semantics, confidence scores, or per-action uncertainty metrics for lerobot/xvla-base outputs; outputs are described as continuous action vectors with MSE training loss on real dims. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot

### Post-inference validation

- Primary sources do not specify per-action safety thresholds, post-inference calibration procedures, or formal safety checks to convert raw model outputs into low-level robot motor commands for the base checkpoint; practitioners are directed to perform Phase II adaptation and postprocessing but no numeric safety thresholds are published in the inspected canonical sources. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- No immutable checkpoint artifact name, file-level model snapshot, or commit hash for lerobot/xvla-base was reported in the inspected canonical sources. Sources: https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla, https://arxiv.org/abs/2510.10274
- Tokenizer configuration and tokenizer files for text inputs are not present in the inspected canonical sources for the base checkpoint. Sources: https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot
- Image preprocessing normalization parameters (means/stds), explicit color-space conventions, and explicit accepted image file formats are not specified for the base checkpoint in the inspected canonical sources. Sources: https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- Robot_state units and full schema ordering (units for positions, orientation conventions, joint units) are not fully specified in the inspected canonical sources despite processor-level extraction being described. Sources: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla
- No checkpoint-scoped numeric benchmark tables or figures for lerobot/xvla-base were found; numeric evaluation tables in docs/paper are attributed to other named checkpoints (e.g., libero, widowx, folding) rather than to the base checkpoint. Sources: https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base, https://arxiv.org/abs/2510.10274
- Evidence conflict regarding license: the repository LICENSE file referenced in canonical sources indicates an MIT license, while some repo-adjacent metadata referenced in findings claimed Apache-2.0 (this conflict is recorded; see evidenceUrls). Sources: https://github.com/huggingface/lerobot, https://huggingface.co/lerobot/xvla-base

### Safety

- Primary sources inspected do not contain explicit, checkpoint-scoped safety, privacy, or human-in-the-loop deployment constraints for using lerobot/xvla-base as a deployed robot controller. Sources: https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot
- Forge policy: Require human supervision, staged simulation verification, platform-specific safety checks (limits, timeout/failsafe, and actuator saturation checks), and conservative sandboxed trials before any physical deployment of policies derived from lerobot/xvla-base.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### LeRobot X-VLA Base model card (Hugging Face)

- URL: https://huggingface.co/lerobot/xvla-base
- Publisher: Hugging Face (LeRobot project model card)
- Type: `model-card`
- Primary because: First-party Hugging Face model card for the lerobot/xvla-base checkpoint; contains high-level checkpoint description and installation reference.
- Scope: lerobot/xvla-base
- Supports: X-VLA conceptual description and base checkpoint identity
- Supports: Parameter scale claim (0.9 billion parameters)
- Supports: Conceptual modality support (text, image, robot_state)
- Supports: Installation reference (pip install)

### LeRobot repository (official GitHub repository)

- URL: https://github.com/huggingface/lerobot
- Publisher: GitHub / huggingface/lerobot
- Type: `repository`
- Primary because: Official project repository maintained by the project owners; contains documentation, processor/implementation code, rename-map behavior, and repository LICENSE file referenced in findings.
- Scope: lerobot/xvla-base (implementation and docs)
- Supports: Processor-level extraction of robot_state features and image processing steps
- Supports: Action-dimension handling (pad to 20, trim to real_dim, auto mode described in docs)
- Supports: Repository LICENSE file (reported in repository)
- Supports: Documentation source files describing num_image_views, rename-map behavior, and training/Phase II guidance

### LeRobot X-VLA documentation (Hugging Face docs)

- URL: https://huggingface.co/docs/lerobot/en/xvla
- Publisher: Hugging Face / LeRobot docs
- Type: `official-documentation`
- Primary because: Official documentation describing X-VLA design, Phase I/Phase II training workflow, dataset composition, domain IDs, and example checkpoint results (for other checkpoints).
- Scope: X-VLA family and lerobot/xvla-base references in docs
- Supports: Parameter scale (0.9 billion)
- Supports: Phase I pretraining details (290,000 episodes; datasets named)
- Supports: Phase II domain adaptation description and soft-prompt approach
- Supports: Action-dimension handling (max_action_dim=20, pad/trim, auto mode)
- Supports: Reported numeric results for other named checkpoints (libero, widowx, folding) (but not for base checkpoint)

### X-VLA paper (arXiv preprint)

- URL: https://arxiv.org/abs/2510.10274
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing X-VLA architecture, soft-prompt methodology, and high-level experimental design as referenced by project documentation.
- Scope: X-VLA architecture and methodology (paper-level description)
- Supports: Soft-prompt approach and cross-embodiment claims
- Supports: Architectural description (soft-prompted, flow-matching VLA transformer)
- Supports: High-level training workflow (Phase I/Phase II)

## Evidence gaps

- Evidence gap: No immutable checkpoint artifact name, file-level model snapshot name, or commit hash for lerobot/xvla-base was found in the inspected canonical primary locations: https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla, https://arxiv.org/abs/2510.10274.
- Evidence gap: No checkpoint-scoped numeric benchmark tables or figures for lerobot/xvla-base were found in the inspected canonical primary locations (the docs report numeric results for other named checkpoints but not for lerobot/xvla-base): https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base, https://arxiv.org/abs/2510.10274.
- Evidence gap: Tokenizer configuration, tokenizer files, or explicit text tokenization details for lerobot/xvla-base are not present in the inspected canonical primary locations: https://huggingface.co/lerobot/xvla-base, https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla.
- Evidence gap: Image normalization parameters (means/stds), explicit color-space conventions, and accepted image file formats for the base checkpoint are not specified in the inspected canonical primary locations: https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot.
- Evidence gap: Full robot_state schema with explicit field names, ordering, units, and numeric ranges (units for positions/orientations/joints) are not fully specified in the inspected canonical primary locations despite processor-level extraction being described: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base.
- Evidence gap: No explicit, checkpoint-scoped API implementation citation (e.g., a published select_action function code example tied to lerobot/xvla-base) was found in the inspected canonical primary locations: https://github.com/huggingface/lerobot, https://huggingface.co/lerobot/xvla-base, https://huggingface.co/docs/lerobot/en/xvla.
- Evidence gap: No primary-source statements specifying deterministic vs. stochastic inference modes, sampling/decoding settings, or runtime flags for action-dimension auto-detection beyond the documented pad/trim/auto behavior were found in the inspected canonical primary locations: https://github.com/huggingface/lerobot, https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base.
- Evidence gap: License metadata ambiguity/conflict: the repository LICENSE file referenced in the project's canonical repository indicates MIT but other repo-adjacent metadata in the findings claimed Apache-2.0; the canonical primary locations inspected for license evidence were: https://github.com/huggingface/lerobot, https://huggingface.co/lerobot/xvla-base.
- Evidence gap: Documentation does not provide per-action safety thresholds, post-inference calibration procedures, or explicit low-level controller safety checks for direct deployment of lerobot/xvla-base; inspected locations: https://huggingface.co/docs/lerobot/en/xvla, https://github.com/huggingface/lerobot, https://huggingface.co/lerobot/xvla-base.
- Evidence gap: No checkpoint-scoped head-to-head comparisons between lerobot/xvla-base and named external peer models (Forge peers) are present in the inspected canonical primary locations; comparisons in docs are for other internal checkpoints or are family-level descriptions, not checkpoint-scoped comparisons: https://huggingface.co/docs/lerobot/en/xvla, https://huggingface.co/lerobot/xvla-base, https://arxiv.org/abs/2510.10274.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[3] uses forbidden secondary URL https: $.sources[3] uses forbidden secondary URL https://huggingface.co/papers/2510.10274 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'arclab-mit' for this exact model scope: $.sources[6] uses unapproved repository owner 'arclab-mit' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
