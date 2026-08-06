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

- Research key: `huggingface-co-lerobot-smolvla-vlabench-d6edd20a8d`
- Independent audit: `revised`
- Researched: `2026-08-06T12:56:58.688011+00:00`

SmolVLA is presented in the inspected primary sources as a compact, efficient vision-language-action family intended for robotics. The Hugging Face model card for lerobot/smolvla_vlabench and the official SmolVLA documentation state the family-level design: multimodal inputs (multiple camera views, the robot's sensorimotor state, and a natural-language instruction) are encoded into contextual features that condition an action expert producing action chunks. LeRobot VLABench documentation describes the benchmark/task surfaces and how LeRobot exposes tasks. The inspected primary checkpoint-scoped materials do not report an exact checkpoint revision identifier, a distinct model-weights license, parameter-scale metadata tied to this checkpoint, a serialized input/output schema for the checkpoint, or checkpoint-matched numeric benchmark rows explicitly naming lerobot/smolvla_vlabench.

## Identity

- Upstream name: SmolVLA
- Checkpoint/version: lerobot/smolvla_vlabench
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: SmolVLA is described as a compact, efficient vision-language-action (VLA) family; the upstream documentation states the architecture accepts multiple camera views, the robot's current sensorimotor state, and a natural-language instruction and encodes these inputs into contextual features used to condition an action expert that generates an action chunk.
- License: not reported
- Evidence: https://huggingface.co/lerobot/smolvla_vlabench, https://huggingface.co/docs/lerobot/en/smolvla, https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx, https://arxiv.org/abs/2506.01844

## Selection

### Recommended

- **Research evaluation and prototyping of language-conditioned robotic manipulation policies using LeRobot/VLABench surfaces** — The Hugging Face model card for lerobot/smolvla_vlabench provides instructions to use the checkpoint with libraries, inference providers, notebooks, and local applications; SmolVLA documentation states the family is designed for easy fine-tuning on LeRobot datasets and to accelerate development.
  Scope: lerobot/smolvla_vlabench
  Evidence: https://huggingface.co/lerobot/smolvla_vlabench, https://huggingface.co/docs/lerobot/en/smolvla
- **Exploratory local prototyping of compact SmolVLA-family policies with LeRobot tooling** — SmolVLA is described as compact and deployable for efficient robotics experimentation; LeRobot/VLABench documentation provides the evaluation surfaces and tooling to run policies.
  Scope: lerobot/smolvla_vlabench (family-level design applied to this checkpoint)
  Evidence: https://huggingface.co/docs/lerobot/en/smolvla, https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx, https://huggingface.co/lerobot/smolvla_vlabench

### Conditional

- **Applying the checkpoint to specific VLABench tasks (primitive or composite) after explicit downstream validation** — Only after explicit task-level evaluation and validation within LeRobot/VLABench; the checkpoint is presented as a pretrained policy pushed to the Hub but the inspected checkpoint-scoped materials do not provide numeric, checkpoint-matched benchmarks for specific VLABench tasks.
  Scope: lerobot/smolvla_vlabench
  Evidence: https://huggingface.co/lerobot/smolvla_vlabench, https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx

### Avoid

- **Using the checkpoint for clinical, medical, or regulated decision-making** — Forge policy: do not use this robotics-control checkpoint for clinical or regulated decision support without dedicated validation and certification; the inspected primary checkpoint-scoped sources do not report such validations for lerobot/smolvla_vlabench.
  Scope: lerobot/smolvla_vlabench upstream checkpoint
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- SmolVLA/lerobot/smolvla_vlabench accepts multimodal inputs comprising multiple camera views, the robot’s current sensorimotor state, and a natural-language instruction. Sources: https://huggingface.co/docs/lerobot/en/smolvla, https://huggingface.co/lerobot/smolvla_vlabench
- LeRobot VLABench documentation describes the VLABench task surfaces and how LeRobot exposes tasks; LeRobot exposes VLABench tasks for selection via its interfaces. Sources: https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx
- Evidence gap: a serialized robot_state schema (exact field names, types, units, and ordering) for lerobot/smolvla_vlabench is not provided in the inspected primary sources.

### Accepted formats

- The checkpoint is described as a SmolVLA-family pretrained policy pushed to the Hugging Face Hub and intended to be used with LeRobot/VLABench tooling; primary sources describe the multimodal input types but do not publish a single, exact serialized upstream input format (JSON/protobuf/binary) for the checkpoint. Sources: https://huggingface.co/lerobot/smolvla_vlabench, https://huggingface.co/docs/lerobot/en/smolvla, https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx
- Evidence gap: the audited primary sources do not define a formal serialized upstream input schema (exact field names, types, ordering, or units) for combined text+image+robot_state inputs for lerobot/smolvla_vlabench.

### Preprocessing

- SmolVLA documentation and the model card describe the family/checkpoint design intent but do not specify checkpoint-specific preprocessing parameters (image normalization mean/std, tokenizer identity and parameters, robot-state normalization/scaling). Sources: https://huggingface.co/docs/lerobot/en/smolvla, https://huggingface.co/lerobot/smolvla_vlabench
- Evidence gap: exact preprocessing details required by lerobot/smolvla_vlabench (precise image normalization values, tokenization parameters, and robot-state scaling) are not reported in the inspected primary sources.

### Pre-submit validation

- Before using the checkpoint on a task, verify that the target task is included in the VLABench scope exposed by LeRobot; LeRobot documentation organizes tasks and exposes them for selection. Sources: https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx, https://huggingface.co/lerobot/smolvla_vlabench
- Evidence gap: the inspected primary checkpoint-scoped sources do not provide formal input bounds, schema validation rules, or explicit handling for invalid or out-of-range input cases for lerobot/smolvla_vlabench.

### Task-specific formatting

- LeRobot VLABench documentation describes how VLABench tasks and evaluation surfaces are organized and exposed via LeRobot tooling; the model card references the full documentation for running and evaluating the checkpoint with LeRobot. Sources: https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx, https://huggingface.co/lerobot/smolvla_vlabench

## Output interpretation

### Outputs

- SmolVLA encodes multimodal inputs into contextual features that are used to condition an action expert which generates action chunks (family-level design described in the SmolVLA documentation). Sources: https://huggingface.co/docs/lerobot/en/smolvla, https://huggingface.co/lerobot/smolvla_vlabench
- Evidence gap: the inspected primary sources do not provide a formal, checkpoint-scoped output schema (JSON/protobuf), per-component units, explicit dimensionality, or clipping rules for lerobot/smolvla_vlabench outputs.

### Interpretation

- Interpret model outputs as policy actions that must be validated and safety-checked within the LeRobot/VLABench environment before any real-robot actuation; do not assume units, bounds enforcement, or safety clipping without downstream verification. Sources: https://huggingface.co/lerobot/smolvla_vlabench, https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx

### Post-inference validation

- Require task-level success testing and safety validation within the LeRobot/VLABench environment prior to real-robot deployment since checkpoint-scoped output guarantees are not provided in the inspected sources. Sources: https://huggingface.co/lerobot/smolvla_vlabench, https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx
- Evidence gap: no checkpoint-specific post-inference sanity checks, action-clipping rules, or safety filters for lerobot/smolvla_vlabench are documented in the inspected primary sources.

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### SmolVLA family-level comparisons (paper) — `insufficient-evidence`

- Task: family-level robotics evaluation (reported in the SmolVLA paper)
- Criteria: family-level experimental comparisons reported by the authors; no checkpoint-scoped, protocol-matched comparison was found for lerobot/smolvla_vlabench in the inspected primary sources.
- Rationale: The SmolVLA arXiv preprint provides family-level experimental comparisons, but the inspected checkpoint-scoped artifacts (model card and LeRobot docs) do not present protocol-matched, numeric comparisons that explicitly tie those family-level results to the exact Hub checkpoint lerobot/smolvla_vlabench.
- Comparison conditions: Family-level evaluation reported in the arXiv preprint; no exact-checkpoint (lerobot/smolvla_vlabench) protocol-matched comparison located in the checked primary sources.
- Evidence: https://arxiv.org/abs/2506.01844, https://huggingface.co/lerobot/smolvla_vlabench

## Limitations and safety

### Limitations

- Evidence gap: an exact checkpoint revision identifier (e.g., git commit SHA or weights-file fingerprint) for lerobot/smolvla_vlabench is not reported in the inspected primary sources.
- Evidence gap: a distinct model-weights license statement separate from code licensing is not present in the inspected primary sources for lerobot/smolvla_vlabench.
- Evidence gap: a detailed architecture specification (layer counts, encoder/backbone, tokenizer identity and parameters) for the SmolVLA instance corresponding to lerobot/smolvla_vlabench is not reported in the inspected primary sources.
- Evidence gap: no checkpoint-matched numeric benchmark rows (dataset/split/metric/value with evaluation conditions) explicitly naming lerobot/smolvla_vlabench were found in the inspected primary sources.
- Evidence gap: the inspected primary sources do not publish a formal serialized input or output schema (exact JSON/protobuf schema, field order, types, or units) bound to the lerobot/smolvla_vlabench checkpoint.

### Safety

- Forge policy: require human supervision, physical safety interlocks, and task-level constraints before any real-robot actuation when using lerobot/smolvla_vlabench because the inspected primary checkpoint-scoped documentation does not provide deployment safety certifications or fail-safe guarantees.
- Evidence gap: the inspected primary sources do not describe privacy, data-retention, or proprietary-data handling guarantees specific to lerobot/smolvla_vlabench.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### lerobot/smolvla_vlabench model card

- URL: https://huggingface.co/lerobot/smolvla_vlabench
- Publisher: Hugging Face / LeRobot
- Type: `model-card`
- Primary because: First-party Hugging Face model card for the exact upstream checkpoint named in the audit scope; contains checkpoint identity and usage description tied to the Hub artifact.
- Scope: Exact upstream checkpoint lerobot/smolvla_vlabench
- Supports: identity.checkpoint
- Supports: recommendedUseCases
- Supports: researchSummary
- Supports: inputPreparation.acceptedFormats
- Supports: outputInterpretation.interpretation

### LeRobot VLABench documentation (repo source)

- URL: https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx
- Publisher: Hugging Face / LeRobot (repository)
- Type: `repository`
- Primary because: First-party repository documentation describing VLABench benchmark structure, task surfaces, and LeRobot tooling used to run and evaluate policies.
- Scope: LeRobot VLABench evaluation surfaces and observation/action schemas (repository docs)
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.validation
- Supports: recommendedUseCases
- Supports: researchSummary

### LeRobot documentation: SmolVLA docs (Hugging Face docs build)

- URL: https://huggingface.co/docs/lerobot/en/smolvla
- Publisher: Hugging Face / LeRobot (official docs)
- Type: `official-documentation`
- Primary because: First-party Hugging Face documentation describing SmolVLA family usage patterns and high-level input semantics used for interpretation of the family/checkpoint.
- Scope: SmolVLA family documentation (official docs build)
- Supports: identity.upstreamName
- Supports: architecture
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs

### SmolVLA family-level evaluation (arXiv preprint)

- URL: https://arxiv.org/abs/2506.01844
- Publisher: arXiv
- Type: `paper`
- Primary because: Author-published preprint containing family-level experimental comparisons and results reported by the model authors.
- Scope: SmolVLA family-level evaluation and experiments (paper)
- Supports: researchSummary
- Supports: comparisons

## Evidence gaps

- Exact checkpoint revision identifier (e.g., git commit SHA or weights-file fingerprint) for lerobot/smolvla_vlabench is not reported in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench).
- Model-weights license (distinct from code license) for lerobot/smolvla_vlabench is not disclosed in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench).
- Parameter scale for the exact checkpoint lerobot/smolvla_vlabench is not reported in the inspected primary sources (checked https://huggingface.co/docs/lerobot/en/smolvla and https://huggingface.co/lerobot/smolvla_vlabench).
- A serialized input schema (exact JSON/protobuf schema, field names, types, ordering, and units) for combined text+image+robot_state inputs for lerobot/smolvla_vlabench is not provided in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench and https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx).
- Checkpoint-specific preprocessing details (exact image normalization mean/std, tokenizer parameters, robot-state normalization/scaling) for lerobot/smolvla_vlabench are not reported in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench and https://huggingface.co/docs/lerobot/en/smolvla).
- A formal output contract (JSON schema, per-component units, clipping rules) for lerobot/smolvla_vlabench outputs is not provided in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench and https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx).
- No numeric benchmark rows/tables/figures explicitly matched to the exact checkpoint name lerobot/smolvla_vlabench with dataset/split/metric/value/conditions were found in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench and https://arxiv.org/abs/2506.01844).
- No protocol-matched comparisons that explicitly evaluate lerobot/smolvla_vlabench against named alternatives under identical dataset/split/metric/eval-mode were found in the inspected primary sources (checked https://arxiv.org/abs/2506.01844 and https://huggingface.co/lerobot/smolvla_vlabench).
- Post-inference sanity checks, action-clipping rules, or safety filters specific to lerobot/smolvla_vlabench are not documented in the inspected primary sources (checked https://github.com/huggingface/lerobot/blob/main/docs/source/vlabench.mdx and https://huggingface.co/lerobot/smolvla_vlabench).
- Privacy, retention, or proprietary-data handling guarantees tied to lerobot/smolvla_vlabench are not described in the inspected primary sources (checked https://huggingface.co/lerobot/smolvla_vlabench).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses forbidden secondary URL https: $.sources[3] uses forbidden secondary URL https://huggingface.co/papers/2506.01844 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'blog' for this exact model scope: $.sources[7] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://huggingface.co/blog/smolvla Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'katsukiono' for this exact model scope: $.sources[11] uses unapproved repository owner 'katsukiono' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
