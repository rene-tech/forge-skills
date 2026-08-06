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

- Research key: `huggingface-co-allenai-molmoact2-so100-101-5e93e3bd97`
- Independent audit: `revised`
- Researched: `2026-08-06T10:25:13.236964+00:00`

Checkpoint MolmoAct2-SO100_101 (allenai/MolmoAct2-SO100_101) is a MolmoAct2-family fine-tune on the SO-100/101 mixture providing a continuous-action policy head for SO-100/101 robot embodiments. Primary checkpoint evidence (Hugging Face model card, AllenAI GitHub, and the MolmoAct2 paper preprint) documents: (1) the checkpoint is fine-tuned on SO-100/101 with absolute joint-pose control and annotated language instructions; (2) sample usage on the model card shows processor/model loading via trust_remote_code and a sample robot_state NumPy float32 array; and (3) the arXiv preprint reports task-level accuracy numbers for MolmoAct2-SO100/101 across named tasks. The primary sources inspected do not publish a checkpoint-scoped parameter count, model-weight license text, an explicit per-field JSON schema for robot_action outputs, nor an exhaustive runtime/serving/quantization recipe for this exact checkpoint. All conclusions in this dossier are scoped to the exact checkpoint and the canonical primary sources listed in Sources.

## Identity

- Upstream name: allenai/MolmoAct2-SO100_101
- Checkpoint/version: MolmoAct2-SO100_101
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: MolmoAct2 family: VLM backbone with a flow-matching continuous-action expert that conditions on the VLM key-value cache through a per-layer connection.
- License: not reported
- Evidence: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://arxiv.org/html/2605.02881v1, https://github.com/allenai/molmoact2

## Selection

### Recommended

- **SO-100/SO-101 policy inference producing continuous robot actions (robot-scale joint targets) for tasks similar to the provided sample prompts.** — The Hugging Face model card and the AllenAI repository list MolmoAct2-SO100_101 as a checkpoint fine-tuned on the SO-100/101 mixture intended for SO-100/101 inference with absolute joint-pose control and annotated language instructions.
  Scope: allenai/MolmoAct2-SO100_101
  Evidence: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2
- **Further fine-tuning of the MolmoAct2-SO100_101 checkpoint for target embodiments or task mixtures.** — The Hugging Face model card and the AllenAI repository indicate the checkpoint is intended both for inference and as a starting point for further fine-tuning on target embodiments or mixtures.
  Scope: allenai/MolmoAct2-SO100_101
  Evidence: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2

### Conditional

- **Use as a starting point for downstream fine-tuning or evaluation in new robot embodiments only after explicit downstream validation.** — Downstream validation, adaptation, and testing on the target embodiment are required because the checkpoint was trained on the SO-100/101 mixture and performance varies across embodiments; the canonical sources document intended fine-tuning and empirically verified deployments only on specific embodiments.
  Scope: allenai/MolmoAct2-SO100_101
  Evidence: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2

### Avoid

- **Evidence gap: No checkpoint-specific published avoid-use boundaries.** — Evidence gap: The inspected primary sources do not publish explicit, checkpoint-scoped avoid-use guidance (for example, a published statement forbidding unsupervised hardware execution for this exact checkpoint was not found in the inspected sources).
  Scope: allenai/MolmoAct2-SO100_101
  Evidence: https://huggingface.co/allenai/MolmoAct2-SO100_101

## Input preparation

### Semantic inputs

- Language instruction (task string) is used by the checkpoint; the model card provides a sample task prompt such as "Move the arm towards the lemon, grasp it, lift it up, and drop it into the red bowl." Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101
- Visual observations (images) are accepted as inputs; the model card includes sample image assets (assets/sample_realsense_top_rgb.png and assets/sample_realsense_side_rgb.png) indicating image inputs are part of the input modality. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101
- Robot state is provided as a NumPy array in the sample usage example; the model card example shows a robot_state array with dtype float32 in the example code. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101

### Accepted formats

- Sample usage code on the model card demonstrates images referenced as sample assets and a robot_state NumPy array being used; the model card shows processor/model loading with trust_remote_code=True. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101

### Preprocessing

- Sample usage code defines a robot_state NumPy array with explicit numeric values and dtype float32; the model card sample demonstrates passing robot_state as a NumPy array (dtype float32 in the example). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101
- The model card example shows loading processor/model with AutoProcessor.from_pretrained(repo_id, trust_remote_code=True) and AutoModelForImageTextToText.from_pretrained(repo_id) in sample usage code. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101

### Pre-submit validation

- Evidence gap: The inspected primary sources do not publish a formal input-validation checklist (for example, exhaustive bounds on image resolution, camera slot counts, or robot_state dimensionality). Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card page content). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101

### Task-specific formatting

- The model card provides a sample task prompt in its usage examples but does not publish a formal, explicit instruction-head prompt template in the inspected primary sources. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101

## Output interpretation

### Outputs

- The model card includes a "Continuous Actions" section; the documented output modality for the checkpoint in the inspected sources is continuous robot actions (robot-scale joint targets / continuous-action outputs). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101

### Interpretation

- Interpret continuous outputs as the checkpoint's intended continuous-action output format for SO-100/101 inference as described by the model card's "Continuous Actions" section. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101
- Evidence gap: The inspected primary sources do not publish explicit calibration or confidence-score semantics for raw model outputs of this exact checkpoint. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card) and https://arxiv.org/html/2605.02881v1 (paper preprint results). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://arxiv.org/html/2605.02881v1

### Post-inference validation

- Evidence gap: The inspected primary sources do not publish a checkpoint-scoped post-inference calibration, sanity, or downstream validation protocol (for example, exact simulation rollout checks or numeric acceptance thresholds) for allenai/MolmoAct2-SO100_101. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 and https://github.com/allenai/molmoact2 (repository documentation). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2

## Public benchmarks

### Apple on plate

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 100.0% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101; training uses annotated language instructions, absolute joint-pose actions, and a 30-step action chunk at 30 Hz.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)
- Caveat: The paper lists task-level accuracies for MolmoAct2-SO100/101 but does not publish per-task splits or exact evaluation scripts in the inspected locator.

### Pipette in tray

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 86.7% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)
- Caveat: The paper lists task-level accuracies but does not provide split names or raw per-episode data at the inspected locator.

### Red cube in tape roll

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 93.3% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Knife in box

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 93.3% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Objects in bowl

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 62.0% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Fork on plate

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 70.0% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Stack blocks

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 20.0% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Tissues in basket

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 73.3% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Pen on notebook

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 86.7% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

### Block in box

- Dataset/split: SO-100/101 task set (SO-100/101 mixture) / not reported
- Metric/value: accuracy / 33.3% (`higher-is-better`)
- Model scope: MolmoAct2-SO100/101
- Conditions: Reported in the MolmoAct2 paper preprint for MolmoAct2-SO100/101.
- Source: https://arxiv.org/html/2605.02881v1
- Locator: arXiv HTML v1 paper results section (MolmoAct2-SO100/101 task accuracies)

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Parameter count for this exact checkpoint is not reported in the inspected primary sources. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://arxiv.org/html/2605.02881v1, https://github.com/allenai/molmoact2
- Evidence gap: No explicit per-field JSON schema for robot_action outputs (field names, units, timestamps, score/confidence fields) for this exact checkpoint was found in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card "Continuous Actions" section) and https://github.com/allenai/molmoact2 (repository). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2
- Evidence gap: Exact runtime/serving constraints (supported precisions, quantization recipes, required runtime libraries) for this exact checkpoint are not documented in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card) and https://github.com/allenai/molmoact2 (repository). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2
- Evidence gap: Exact input-shape bounds (image resolution, exact number of camera slots accepted, robot_state vector dimensionality) for allenai/MolmoAct2-SO100_101 are not fully enumerated in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card), https://github.com/allenai/molmoact2 (repository), and https://arxiv.org/html/2605.02881v1 (paper). Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2, https://arxiv.org/html/2605.02881v1
- Evidence gap: The inspected primary sources do not publish a checkpoint-scoped post-inference calibration or confidence semantics for the model outputs of MolmoAct2-SO100_101. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 and https://arxiv.org/html/2605.02881v1. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://arxiv.org/html/2605.02881v1

### Safety

- Evidence gap: The inspected primary sources do not publish checkpoint-scoped safety instructions or data-handling rules for allenai/MolmoAct2-SO100_101. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card) and https://huggingface.co/allenai/MolmoAct2 (MolmoAct2 family model card) which provides family-level safety guidance such as human supervision and careful validation but does not publish checkpoint-scoped safety rules. Sources: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://huggingface.co/allenai/MolmoAct2

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MolmoAct2-SO100_101 model card (Hugging Face)

- URL: https://huggingface.co/allenai/MolmoAct2-SO100_101
- Publisher: Hugging Face / AllenAI
- Type: `model-card`
- Primary because: Official Hugging Face model card page for the exact checkpoint allenai/MolmoAct2-SO100_101; contains sample usage, sample inputs, and a "Continuous Actions" section relevant to checkpoint behavior and usage.
- Scope: allenai/MolmoAct2-SO100_101 checkpoint; usage examples, sample inputs, and continuous-action section described on the page.
- Supports: identity.upstreamName
- Supports: identity.checkpoint
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: inputPreparation
- Supports: outputInterpretation
- Supports: limitations
- Supports: safety

### MolmoAct2 paper preprint (arXiv HTML v1)

- URL: https://arxiv.org/html/2605.02881v1
- Publisher: arXiv / MolmoAct2 authors
- Type: `paper`
- Primary because: Official paper preprint that reports numeric task-level results for MolmoAct2-SO100/101 and training/scale/dataset statistics for the SO-100/101 mixture.
- Scope: MolmoAct2-SO100/101 reported results and training/dataset protocol in the preprint
- Supports: benchmarks
- Supports: researchSummary
- Supports: limitations
- Supports: identity.architecture
- Supports: inputPreparation

### allenai/molmoact2 repository (GitHub)

- URL: https://github.com/allenai/molmoact2
- Publisher: AllenAI (GitHub repository)
- Type: `repository`
- Primary because: Official AllenAI code repository that lists checkpoint names, deployment notes, and repository-level documentation for MolmoAct2 and specific fine-tuned checkpoints including MolmoAct2-SO100_101.
- Scope: Repository documentation and checkpoint listings for MolmoAct2 family including MolmoAct2-SO100_101
- Supports: identity.upstreamName
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: inputPreparation
- Supports: limitations

### MolmoAct2 documentation (Hugging Face Lerobot docs)

- URL: https://huggingface.co/docs/lerobot/en/molmoact2
- Publisher: Hugging Face documentation / LeRobot
- Type: `official-documentation`
- Primary because: Official documentation pages for MolmoAct2 family describing benchmark-level performance for the original MolmoAct2 and family-level guidance.
- Scope: MolmoAct2 family documentation and benchmark summaries
- Supports: researchSummary
- Supports: limitations
- Supports: identity.architecture

### MolmoAct2 family model card (Hugging Face)

- URL: https://huggingface.co/allenai/MolmoAct2
- Publisher: Hugging Face / AllenAI
- Type: `model-card`
- Primary because: Family-level Hugging Face model card providing safety guidance, intended use statements, and notes about deployment variability across embodiments.
- Scope: MolmoAct2 family model card; family-level safety and deployment guidance
- Supports: safety
- Supports: conditionalUseCases
- Supports: recommendedUseCases
- Supports: limitations

## Evidence gaps

- No primary-source numeric benchmark results absent: (satisfied) numeric task-level results for MolmoAct2-SO100/101 were found in https://arxiv.org/html/2605.02881v1 (paper results section).
- Parameter count (parameterScale) for the MolmoAct2-SO100_101 checkpoint is not reported in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card), https://github.com/allenai/molmoact2 (repository), https://arxiv.org/html/2605.02881v1 (paper).
- No explicit per-field JSON schema for robot_action outputs (field names, units, timestamps, score fields) for this exact checkpoint was found in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 (model card "Continuous Actions" section) and https://github.com/allenai/molmoact2 (repository).
- No explicit calibration or confidence score semantics for outputs of MolmoAct2-SO100_101 were published in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 and https://arxiv.org/html/2605.02881v1 (paper results).
- Exact runtime/serving constraints (supported precisions, quantization recipes, required runtime libraries) for this checkpoint are not documented in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101 and https://github.com/allenai/molmoact2.
- Exact input-shape bounds (image resolution, exact number of camera slots accepted, robot_state vector dimensionality) for allenai/MolmoAct2-SO100_101 are not fully enumerated in the inspected primary sources. Checked: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2, and https://arxiv.org/html/2605.02881v1.
- Comparative, like-for-like numeric benchmark comparisons between allenai/MolmoAct2-SO100_101 and other Forge candidates cannot be performed from the inspected primary sources because comparable checkpoint-level results for other Forge candidates are not published in these canonical sources. Checked: https://arxiv.org/html/2605.02881v1 and https://huggingface.co/allenai/MolmoAct2-SO100_101.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 27 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'collections' for this exact model scope: $.sources[9] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'lerobot' for this exact model scope: $.sources[10] uses unapproved repository owner 'lerobot' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'irenegracekp' for this exact model scope: $.sources[11] uses unapproved repository owner 'irenegracekp' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses unapproved repository owner 'blog' for this exact model scope: $.sources[16] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses forbidden secondary URL https: $.sources[16] uses forbidden secondary URL https://huggingface.co/blog/smolvla Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary host medium.com: $.sources[17] uses forbidden secondary host medium.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'nikodembartnik' for this exact model scope: $.sources[18] uses unapproved repository owner 'nikodembartnik' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20].primary must be true: $.sources[20].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-DROID Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-DROID Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/MolmoAct2-LIBERO Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
