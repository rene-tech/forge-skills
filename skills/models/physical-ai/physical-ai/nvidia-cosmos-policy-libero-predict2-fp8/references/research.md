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

- Research key: `github-com-nvlabs-cosmos-policy-32ec0570b0`
- Independent audit: `revised`
- Researched: `2026-07-23T23:50:11.398213+00:00`

This dossier is scoped to upstream primary evidence for the LIBERO checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B and to the Forge family nvidia-cosmos-policy-libero-predict2 only insofar as those Forge variants appear to wrap that upstream checkpoint. Primary sources support that the upstream checkpoint is a 2B-parameter diffusion-transformer policy fine-tuned from Cosmos-Predict2-2B-Video2World for robot manipulation and control in simulation, with text, multi-view RGB images, and proprioceptive state as inputs and action-sequence, future-state, and value outputs. Primary benchmark evidence exists for the upstream LIBERO checkpoint, but the provided findings do not establish immutable provenance linking each Forge runtime slug to a specific unchanged upstream artifact, and several important operational semantics remain unspecified, including exact coordinate frames, action units, tokenizer mapping, and calibration semantics for value outputs.

## Identity

- Upstream name: nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- Checkpoint/version: nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- Immutable revision: 80d313c30401f92d3695136473d8e8a46515531d
- Parameter scale: 2 billion parameters
- Architecture/head: diffusion transformer with latent video diffusion; policy model fine-tuned from nvidia/Cosmos-Predict2-2B-Video2World
- License: Model weights: NVIDIA One-Way Noncommercial License (NSCLv1) as stated in the checkpoint README/model card. Code: the inspected cosmos-policy repository LICENSE file is a separate repository license artifact; the research findings do not specify an authoritative checkpoint-scoped code-license name for this dossier beyond that separate file, so code-license naming remains not fully resolved from the provided findings.
- Evidence: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/commits/80d313c30401f92d3695136473d8e8a46515531d, https://github.com/NVlabs/cosmos-policy/blob/main/LICENSE

## Selection

### Recommended

- **Simulation research and development for robot manipulation and control on LIBERO task suites** — The checkpoint model card describes the use case as Physical AI robot manipulation and control in simulation environments, the LIBERO repository documentation identifies this exact pretrained checkpoint for LIBERO tasks, and the checkpoint reports a 98.5% average success rate across four LIBERO task suites.
  Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B; evidence does not prove benchmark equivalence for each Forge wrapper variant.
  Evidence: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md, https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md

### Conditional

- **Using the listed Forge variants as wrappers for LIBERO policy inference** — Only conditionally appropriate if downstream verification confirms that the specific Forge variant serves the unchanged upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B; the provided findings do not supply immutable provenance from each Forge slug to an exact upstream artifact or repo revision.
  Scope: Forge variants nvidia-cosmos-policy-libero-predict2-b300-fast-action, nvidia-cosmos-policy-libero-predict2-b300-optimized, nvidia-cosmos-policy-libero-predict2-cuda12, nvidia-cosmos-policy-libero-predict2-cuda13, and nvidia-cosmos-policy-libero-predict2-fp8.
  Evidence: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md, https://github.com/nvlabs/cosmos-policy, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/commits/80d313c30401f92d3695136473d8e8a46515531d
- **Real-world robot testing or deployment** — Only after explicit downstream validation, environment-specific calibration, and safety review. The inspected primary evidence in this dossier documents simulation-focused use and does not specify real-world deployment validation details for the exact LIBERO checkpoint.
  Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B and any Forge wrapper claiming to expose it.
  Evidence: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md, https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md

### Avoid

- **Clinical or healthcare decision-making** — Primary evidence describes the checkpoint for research and development and Physical AI robot manipulation/control, with no clinical validation, healthcare approval, or PHI-handling guidance in the provided findings.
  Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B and any Forge wrapper claiming to expose it.
  Evidence: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md
- **Assuming that all listed Forge runtime variants are benchmark-equivalent to the reported upstream checkpoint without separate provenance verification** — The provided findings identify the upstream checkpoint and some repository references to it, but do not provide primary immutable provenance linking each Forge slug to a specific unchanged upstream checkpoint artifact or exact repository revision.
  Scope: Forge variants nvidia-cosmos-policy-libero-predict2-b300-fast-action, nvidia-cosmos-policy-libero-predict2-b300-optimized, nvidia-cosmos-policy-libero-predict2-cuda12, nvidia-cosmos-policy-libero-predict2-cuda13, and nvidia-cosmos-policy-libero-predict2-fp8.
  Evidence: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md, https://github.com/nvlabs/cosmos-policy, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/commits/80d313c30401f92d3695136473d8e8a46515531d

## Input preparation

### Semantic inputs

- The checkpoint accepts text input representing a natural-language task description. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- The checkpoint accepts multi-view image observations. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- The checkpoint accepts proprioceptive state input with dimension 9. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json

### Accepted formats

- Image inputs are specified as RGB images at resolution [224,224] with views named "agentview" and "eye_in_hand". Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- Proprioception input is specified with components gripper_joints, end_effector_position, and quaternion. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- LIBERO usage in the repository references a dataset statistics file at "nvidia/Cosmos-Policy-LIBERO-Predict2-2B/libero_dataset_statistics.json" and a T5 embedding file at "nvidia/Cosmos-Policy-LIBERO-Predict2-2B/libero_t5_embeddings.pkl". Sources: https://github.com/nvlabs/cosmos-policy

### Preprocessing

- Repository/config evidence indicates use_wrist_image = True for the LIBERO setup. Sources: https://github.com/nvlabs/cosmos-policy
- The provided findings specify a LIBERO dataset statistics file and LIBERO T5 text embeddings artifact for the exact checkpoint workflow. Sources: https://github.com/nvlabs/cosmos-policy

### Pre-submit validation

- Inputs should match the documented LIBERO task-suite workflow and named task suites supported by the repository documentation. Sources: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md
- Text input should be provided as a natural-language task description string, images should match the documented RGB [224,224] view format, and proprioception should match the documented 9-dimensional structure before submission. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json

### Task-specific formatting

- The LIBERO repository documentation identifies task suite names libero_spatial, libero_object, libero_goal, and libero_10 for this checkpoint workflow. Sources: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md
- The checkpoint path used in repository code is set to "nvidia/Cosmos-Policy-LIBERO-Predict2-2B". Sources: https://github.com/nvlabs/cosmos-policy

## Output interpretation

### Outputs

- The checkpoint outputs an action sequence. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- The action output specification in config.json is dimension 7, horizon 16, with components end_effector_6dof and gripper. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- The checkpoint outputs future state predictions and a value estimate. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B

### Interpretation

- Action outputs should be interpreted as policy action-sequence predictions for robot manipulation/control rather than as human-readable categorical labels. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- Future state predictions and value estimates are model outputs, but the provided findings do not specify calibrated probability semantics, coordinate frames, or physical units for these outputs. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json

### Post-inference validation

- Post-inference validation should check that outputs conform to the documented action shape and modality contract in config.json before downstream use. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- For benchmark-oriented validation, compare downstream LIBERO evaluation results against the reported task-suite success rates rather than assuming wrapper/runtime equivalence from deployment metadata. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md

## Public benchmarks

### Robot manipulation policy evaluation on LIBERO task suites

- Dataset/split: LIBERO / not reported
- Metric/value: average success rate across four LIBERO task suites / 98.5% (`higher-is-better`)
- Model scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B; not direct evidence for any specific Forge runtime wrapper.
- Conditions: Reported as an aggregate across four LIBERO task suites for the checkpoint. Repository documentation identifies task suites libero_spatial, libero_object, libero_goal, and libero_10, while the model card states the aggregate is across four LIBERO task suites; the provided findings do not give an immutable upstream evaluation script locator for the exact aggregate computation.
- Source: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- Locator: Model card page statement: "The model achieves a 98.5% average success rate across four LIBERO task suites."
- Caveat: This is upstream checkpoint evidence, not proof that each Forge wrapper variant reproduces the same result.
- Caveat: The provided findings do not include per-suite numeric values from a primary source in the allowed final source set.
- Caveat: Repository task-suite naming in findings lists libero_spatial, libero_object, libero_goal, and libero_10, which should not be conflated with unstated alternative suite names without separate primary evidence.

### LIBERO task-suite selection for checkpoint evaluation

- Dataset/split: LIBERO / not reported
- Metric/value: context on supported task-suite identifiers; no numeric value reported at this locator / Task suite names: libero_spatial, libero_object, libero_goal, libero_10 (`context-only`)
- Model scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B workflow in the official cosmos-policy repository.
- Conditions: This row is contextual protocol evidence for evaluation scope rather than a performance score.
- Source: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md
- Locator: Repository path LIBERO.md: statement identifying the pretrained checkpoint and task suite names for LIBERO tasks.
- Caveat: This is not a numeric benchmark result.
- Caveat: The source helps scope the evaluation protocol but does not itself report a metric value.

## Comparisons

### Other robot manipulation policy families — `insufficient-evidence`

- Task: Head-to-head selection against other policy families for LIBERO tasks
- Criteria: The provided primary findings for this dossier do not include protocol-matched, checkpoint-scoped head-to-head primary evidence with exact alternative checkpoint identities retained in the allowed source set.
- Rationale: Although some excluded secondary sources discuss broader comparisons, the retained primary sources in this corrected dossier establish only the upstream checkpoint's own stated LIBERO result and task scope, not a directly comparable protocol-matched comparison against named alternative checkpoints within the allowed evidence set.
- Comparison conditions: Use insufficient-evidence unless a primary source in the final source set reports both the exact LIBERO checkpoint result and a named alternative under matched conditions.
- Evidence: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md

## Limitations and safety

### Limitations

- The checkpoint is documented for research and development use and for Physical AI robot manipulation/control in simulation environments, which narrows the evidence base for other deployment settings. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md
- The provided findings do not establish immutable provenance linking each listed Forge variant slug to a specific unchanged upstream checkpoint artifact or exact repository revision. Sources: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md, https://github.com/nvlabs/cosmos-policy, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/commits/80d313c30401f92d3695136473d8e8a46515531d
- The provided findings do not specify exact coordinate-frame conventions, physical units for action components, or calibrated semantics for value estimates. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- License evidence is checkpoint-scoped for model weights but not fully resolved for code-license naming within this dossier from the provided findings; users should not infer a single identical license regime for both weights and code. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md, https://github.com/NVlabs/cosmos-policy/blob/main/LICENSE

### Safety

- No clinical-use approval or PHI/data-handling procedures are specified in the provided primary findings; do not use this checkpoint for healthcare deployment without external clinical validation and data-governance review. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md
- Because the checkpoint is documented for research and development use, downstream users should apply environment-specific safety review before any real-world robotic deployment. Sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Cosmos-Policy-LIBERO-Predict2-2B model card

- URL: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party checkpoint model card for the exact upstream model in scope.
- Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- Supports: Identity
- Supports: parameter scale
- Supports: architecture summary
- Supports: intended use
- Supports: input/output modality summary
- Supports: LIBERO aggregate benchmark claim

### Cosmos-Policy-LIBERO-Predict2-2B config.json

- URL: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/config.json
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party checkpoint repository file specifying architecture and input/output schema details for the exact model.
- Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B configuration
- Supports: Architecture
- Supports: base model mapping
- Supports: parameter count
- Supports: input specifications
- Supports: output specifications

### Cosmos-Policy-LIBERO-Predict2-2B README

- URL: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blob/main/README.md
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party checkpoint README providing weight-license and use-case information for the exact model.
- Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B README
- Supports: Model-weight license
- Supports: use case
- Supports: release date
- Supports: training objective description
- Supports: hardware tested

### Cosmos-Policy-LIBERO-Predict2-2B commit page

- URL: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/commits/80d313c30401f92d3695136473d8e8a46515531d
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party checkpoint repository commit page used as immutable revision evidence in the provided findings.
- Scope: Upstream checkpoint nvidia/Cosmos-Policy-LIBERO-Predict2-2B revision evidence
- Supports: Revision evidence

### cosmos-policy LIBERO documentation

- URL: https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md
- Publisher: NVlabs / NVIDIA
- Type: `repository`
- Primary because: First-party repository documentation for the LIBERO workflow using the exact upstream checkpoint named in this dossier.
- Scope: Official LIBERO workflow for cosmos-policy
- Supports: Checkpoint identification
- Supports: LIBERO task-suite identifiers
- Supports: evaluation workflow scope

### cosmos-policy repository root

- URL: https://github.com/nvlabs/cosmos-policy
- Publisher: NVlabs / NVIDIA
- Type: `repository`
- Primary because: First-party repository root referenced in the findings for checkpoint path and associated artifact names.
- Scope: Official cosmos-policy repository
- Supports: Checkpoint path in code
- Supports: dataset statistics artifact name
- Supports: T5 embeddings artifact name
- Supports: use_wrist_image setting

### cosmos-policy README

- URL: https://github.com/NVlabs/cosmos-policy/blob/main/README.md
- Publisher: NVlabs / NVIDIA
- Type: `repository`
- Primary because: First-party repository README containing official runtime resource statements for Cosmos Policy tasks.
- Scope: Official cosmos-policy repository README
- Supports: Inference resource statements

### cosmos-policy LICENSE

- URL: https://github.com/NVlabs/cosmos-policy/blob/main/LICENSE
- Publisher: NVlabs / NVIDIA
- Type: `repository`
- Primary because: First-party repository license file, relevant to distinguishing repository code licensing from model-weight licensing.
- Scope: Official cosmos-policy repository license artifact
- Supports: Code-license distinction

### Exact official starting source declared by Forge

- URL: https://github.com/NVlabs/cosmos-policy
- Publisher: github.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-cosmos-policy-libero-predict2
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The provided findings do not supply primary immutable provenance linking each Forge variant slug (nvidia-cosmos-policy-libero-predict2-b300-fast-action, nvidia-cosmos-policy-libero-predict2-b300-optimized, nvidia-cosmos-policy-libero-predict2-cuda12, nvidia-cosmos-policy-libero-predict2-cuda13, nvidia-cosmos-policy-libero-predict2-fp8) to a specific unchanged upstream checkpoint artifact or exact repository revision.
- Evidence gap: The provided findings do not specify tokenizer artifact identity or tokenizer-to-checkpoint mapping for nvidia/Cosmos-Policy-LIBERO-Predict2-2B.
- Evidence gap: The provided findings do not specify exact coordinate frames or physical units for action-output components.
- Evidence gap: The provided findings do not specify calibration semantics or numerical interpretation guidance for the value estimate output.
- Evidence gap: The provided findings do not provide a primary source in the final allowed source set with per-suite LIBERO numeric breakdowns for this checkpoint.
- Evidence gap: The provided findings do not provide comparison-ready primary evidence against named alternative checkpoints under protocol-matched conditions within the allowed final source set.
- Evidence gap: The provided findings do not fully resolve a checkpoint-scoped code-license name separate from the repository LICENSE artifact, so weight-license and code-license equivalence should not be assumed.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://github.com/NVlabs/cosmos-policy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://huggingface.co/blog/nvidia/cosmos-predict-2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason1-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano-Reasoner Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super-Reasoner Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://github.com/NVlabs/cosmos-policy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
