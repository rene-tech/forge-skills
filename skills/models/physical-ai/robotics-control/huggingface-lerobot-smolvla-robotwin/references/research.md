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

- Research key: `huggingface-co-lerobot-smolvla-robotwin-74d33dc92d`
- Independent audit: `revised`
- Researched: `2026-08-06T12:44:52.431152+00:00`

Checkpoint-scoped primary evidence for lerobot/smolvla_robotwin in the inspected canonical repository files and model hub page is limited to the model hub listing and the repository config.json. The config.json (lerobot/smolvla_robotwin blob/main/config.json) declares: pretrained_path = "lerobot/smolvla_base" (indicating this checkpoint is fine-tuned from an upstream base), type = "smolvla", input feature shapes observation.images.camera1/2/3 = [3, 256, 256], observation.state shape = [6], output action shape = [14], chunk_size = 50, n_action_steps = 50, max_state_dim = 32, max_action_dim = 32, resize_imgs_with_padding = [512, 512], normalization mappings VISUAL → IDENTITY, STATE → MEAN_STD, ACTION → MEAN_STD, tokenizer_max_length = 48, tokenizer-related artifacts are not listed in the checkpoint files inspected, optimizer and scheduler hyperparameters (learning rate, betas, eps, weight_decay, grad_clip_norm, warmup_steps, decay_steps, decay_lr) are present in the config.json, device and runtime flags (device="cuda", use_amp=false, use_peft=false, push_to_hub=true, use_cache=true, attention_mode="cross_attn", freeze_vision_encoder=false, train_expert_only=false, train_state_proj=true) are declared, and the VLM model name used is declared as "HuggingFaceTB/SmolVLM2-500M-Video-Instruct" with load_vlm_weights = true. The config.json explicitly sets "license" = null. The Hugging Face model hub page (lerobot/smolvla_robotwin) is the canonical listing entry point. Upstream family-level context (SmolVLA paper on arXiv and the lerobot/smolvla_base model page) exist and were inspected only as upstream/family context; no checkpoint-scoped numeric benchmark rows, immutable checkpoint locator (file name, release tag, commit hash), tokenizer artifact files, or declared parameter-count for this exact checkpoint were found in the inspected checkpoint-scoped primary sources.

## Identity

- Upstream name: lerobot/smolvla_robotwin
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: type = "smolvla" (as declared in config.json)
- License: null (config.json sets "license" = null; no declared model-weight license text present in inspected checkpoint-scoped primary source)
- Evidence: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json, https://huggingface.co/lerobot/smolvla_robotwin

## Selection

### Recommended

- **Evidence gap: No creator-published recommended-use statement for lerobot/smolvla_robotwin was found in the inspected checkpoint-scoped primary source.** — The checkpoint config.json contains configuration keys describing input/output feature shapes, temporal parameters, and runtime flags but does not contain an explicit creator-published 'intended use' or recommended-use section for this checkpoint.
  Scope: lerobot/smolvla_robotwin (blob/main/config.json)
  Evidence: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Conditional


### Avoid

- **Avoid use in safety-critical deployments that require a declared model-weight license, an immutable checkpoint revision, or explicit creator-published safety guidance.** — The checkpoint-scoped config.json sets "license" to null (no declared model-weight license text) and the inspected checkpoint-scoped primary files do not include an immutable checkpoint version tag or commit hash; therefore provenance and licensing are not verifiably documented for this checkpoint.
  Scope: lerobot/smolvla_robotwin (blob/main/config.json)
  Evidence: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

## Input preparation

### Semantic inputs

- Input feature observation.images.camera1 is declared as type VISUAL with shape [3, 256, 256] in the checkpoint config. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Input feature observation.images.camera2 is declared as type VISUAL with shape [3, 256, 256] in the checkpoint config. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Input feature observation.images.camera3 is declared as type VISUAL with shape [3, 256, 256] in the checkpoint config. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Input feature observation.state is declared as type STATE with shape [6] in the checkpoint config (config also declares max_state_dim = 32). Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Accepted formats

- Visual inputs are declared as type "VISUAL" with per-camera shape [3, 256, 256] in the checkpoint config. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- State inputs are declared as type "STATE" with shape [6] in the checkpoint config; checkpoint config also declares max_state_dim = 32. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Preprocessing

- resize_imgs_with_padding is set to [512, 512] in the checkpoint config. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Normalization mappings are declared in the checkpoint config as: VISUAL → IDENTITY; STATE → MEAN_STD; ACTION → MEAN_STD. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Temporal/chunking parameters are declared in the checkpoint config: chunk_size = 50 and n_action_steps = 50. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- tokenizer_max_length is set to 48 in the checkpoint config. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Pre-submit validation

- Evidence gap: The inspected checkpoint-scoped primary source (config.json) does not include an explicit input JSON/HTTP contract, example request payloads, or a formal request schema; only feature shapes and normalization mappings are declared. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Task-specific formatting

- Evidence gap: The inspected checkpoint-scoped primary source (config.json) does not list tokenizer artifact files (tokenizer.json, vocab files, tokenizer_config.json) or tokenization implementation for this checkpoint; only tokenizer_max_length is present. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

## Output interpretation

### Outputs

- Policy output configuration declared in the checkpoint config: action feature is of type ACTION with shape [14]; chunk_size = 50; n_action_steps = 50; max_action_dim = 32. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Interpretation

- Evidence gap: The checkpoint-scoped primary source (config.json) does not define units for action parameters, coordinate-frame conventions, or an output JSON schema for action payloads. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Post-inference validation

- Evidence gap: The checkpoint-scoped primary source (config.json) does not provide post-inference validation rules, bounds checks, or example output validation guidance for action outputs. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### lerobot/smolvla_base — `insufficient-evidence`

- Task: robot-policy evaluation (checkpoint-scoped numeric benchmarks)
- Criteria: No checkpoint-scoped numeric benchmark rows or same-protocol evaluation entries for lerobot/smolvla_robotwin were found to enable a protocol-matched quantitative comparison to lerobot/smolvla_base; upstream-family results exist in the SmolVLA paper but are not scoped to this fine-tuned checkpoint.
- Rationale: The lerobot/smolvla_robotwin config.json declares pretrained_path = "lerobot/smolvla_base" indicating a fine-tune relationship, but the inspected checkpoint-scoped primary files do not contain numeric benchmark results or evaluation protocol details that would support a direct numeric comparison under the same protocol.
- Comparison conditions: Protocol-matched comparison is not possible from checkpoint-scoped primary evidence; any comparison would require explicit checkpoint-scoped evaluation artifacts for lerobot/smolvla_robotwin or re-evaluation under a documented protocol.
- Evidence: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json, https://huggingface.co/lerobot/smolvla_base, https://arxiv.org/pdf/2506.01844

## Limitations and safety

### Limitations

- The checkpoint config.json sets "license" to null; no declared model-weight license text for this checkpoint was found in the inspected checkpoint-scoped primary source. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Evidence gap: Exact immutable checkpoint locator (file name, release tag, git commit hash, or other immutable revision) for lerobot/smolvla_robotwin is not present in the inspected checkpoint-scoped primary source. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Evidence gap: Tokenizer artifact files (tokenizer.json, vocab files, tokenizer_config.json) and tokenization implementation for lerobot/smolvla_robotwin are not present in the inspected checkpoint-scoped primary files; only tokenizer_max_length is declared in config.json. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Evidence gap: Parameter count (number of model parameters / model scale) for lerobot/smolvla_robotwin is not reported in the inspected checkpoint-scoped primary source; upstream-family or upstream-base parameter-count claims (if any) were not used as checkpoint-scoped evidence for this fine-tuned checkpoint. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

### Safety

- Evidence gap: No creator-published safety, privacy, adversarial, or deployment guidance specific to the lerobot/smolvla_robotwin checkpoint was found in the inspected checkpoint-scoped primary source. Sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### lerobot/smolvla_robotwin config.json (model repository file)

- URL: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json
- Publisher: lerobot (Hugging Face model repository)
- Type: `repository`
- Primary because: This checkpoint-scoped config.json contains the checkpoint's declared pretrained_path, input/output feature shapes, normalization mappings, tokenizer_max_length, policy temporal parameters, runtime flags, optimizer/scheduler hyperparameters, and the explicit license = null field used for checkpoint-scoped claims and evidence gaps.
- Scope: lerobot/smolvla_robotwin (blob/main/config.json)
- Supports: "pretrained_path" = "lerobot/smolvla_base"
- Supports: "type" = "smolvla"
- Supports: input features: observation.images.camera1/camera2/camera3 shape [3, 256, 256]
- Supports: input feature: observation.state shape [6]
- Supports: output feature: action shape [14]
- Supports: "chunk_size" = 50
- Supports: "n_action_steps" = 50
- Supports: "max_state_dim" = 32
- Supports: "max_action_dim" = 32
- Supports: "resize_imgs_with_padding" = [512, 512]
- Supports: "normalization" mappings: VISUAL → IDENTITY, STATE → MEAN_STD, ACTION → MEAN_STD
- Supports: "tokenizer_max_length" = 48
- Supports: optimizer hyperparameters (learning rate, betas, eps, weight_decay, grad_clip_norm)
- Supports: scheduler parameters (warmup_steps, decay_steps, decay learning rate)
- Supports: "device" = "cuda"
- Supports: "use_amp" = false
- Supports: "use_peft" = false
- Supports: "push_to_hub" = true
- Supports: "attention_mode" = "cross_attn"
- Supports: "use_cache" = true
- Supports: "freeze_vision_encoder" = false
- Supports: "train_expert_only" = false
- Supports: "train_state_proj" = true
- Supports: "vlm_model_name" = "HuggingFaceTB/SmolVLM2-500M-Video-Instruct"
- Supports: "load_vlm_weights" = true
- Supports: "license" = null

### lerobot/smolvla_robotwin (model page)

- URL: https://huggingface.co/lerobot/smolvla_robotwin
- Publisher: lerobot (Hugging Face model repository)
- Type: `official-documentation`
- Primary because: The Hugging Face model page is the canonical checkpoint listing and hub page; it is the declared starting source for the checkpoint and references the repository files used for checkpoint-scoped claims.
- Scope: lerobot/smolvla_robotwin (model hub page)
- Supports: Canonical model hub listing for lerobot/smolvla_robotwin
- Supports: Entry point to checkpoint-scoped files (config.json and other repository files)

### lerobot/smolvla_base model page (upstream base model)

- URL: https://huggingface.co/lerobot/smolvla_base
- Publisher: lerobot (Hugging Face model repository)
- Type: `repository`
- Primary because: Upstream base-model repository listed in the checkpoint config.json as pretrained_path; used strictly as upstream-checkpoint evidence for base-model identity and configuration context, not as checkpoint-scoped evidence for lerobot/smolvla_robotwin.
- Scope: lerobot/smolvla_base (model hub page)
- Supports: Upstream base-model identity and config references
- Supports: Context for pretrained_path declared by lerobot/smolvla_robotwin

### SmolVLA paper (arXiv PDF)

- URL: https://arxiv.org/pdf/2506.01844
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical arXiv preprint for SmolVLA used as upstream family-level evidence for architecture and evaluation protocol descriptions; inspected only for family/upstream context and not attributed as checkpoint-scoped evidence unless the paper explicitly reports results for this exact checkpoint.
- Scope: SmolVLA family (arXiv preprint)
- Supports: Family-level architectural and benchmark descriptions for SmolVLA used as upstream context

### LeRobot GitHub LICENSE (project-level license file)

- URL: https://github.com/huggingface/lerobot/blob/main/LICENSE
- Publisher: Hugging Face (GitHub repository)
- Type: `repository`
- Primary because: Project-level LICENSE file for the LeRobot repository; supports project-code license statements but does not override the checkpoint-scoped "license" = null in the checkpoint config.json.
- Scope: huggingface/lerobot (LICENSE)
- Supports: LeRobot project-level licensing statements (project code license text and patent grant) as published in the repository LICENSE file

### LeRobot pyproject.toml (project metadata including license field)

- URL: https://github.com/huggingface/lerobot/blob/main/pyproject.toml
- Publisher: Hugging Face (GitHub repository)
- Type: `repository`
- Primary because: Project metadata file listing the project license as Apache-2.0; used as upstream project evidence regarding repository packaging metadata but not documented as the model-weight license for the checkpoint.
- Scope: huggingface/lerobot (pyproject.toml)
- Supports: Project-level license field set to Apache-2.0 in pyproject.toml (project packaging metadata)

## Evidence gaps

- Evidence gap: Exact immutable checkpoint locator (file name, release tag, git commit hash, or other immutable revision) for lerobot/smolvla_robotwin is not present in the inspected checkpoint-scoped primary source (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: Tokenizer artifact files (tokenizer.json, vocab files, tokenizer_config.json) and tokenization implementation for lerobot/smolvla_robotwin are not present in the inspected checkpoint-scoped primary files; only tokenizer_max_length is declared in config.json (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: Parameter count (number of model parameters / model scale) for lerobot/smolvla_robotwin is not reported in the inspected checkpoint-scoped primary source; upstream-base parameter-count claims (if any) were not used as checkpoint-scoped evidence for this fine-tuned checkpoint (checked sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json, https://huggingface.co/lerobot/smolvla_base).
- Evidence gap: No creator-published recommended-use statement for lerobot/smolvla_robotwin was found in the inspected checkpoint-scoped primary source (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: No creator-published safety, privacy, adversarial, or deployment guidance specific to lerobot/smolvla_robotwin was found in the inspected checkpoint-scoped primary files (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: No checkpoint-scoped numeric benchmark results (dataset/split/metric/value) or same-protocol benchmark tables for lerobot/smolvla_robotwin were found in the inspected checkpoint-scoped primary files (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json); upstream family-level benchmarks exist in the SmolVLA paper (https://arxiv.org/pdf/2506.01844) but are not scoped to this exact fine-tuned checkpoint.
- Evidence gap: No explicit input JSON/HTTP contract, example request payloads, or formal request schema for lerobot/smolvla_robotwin were found in the inspected checkpoint-scoped primary files (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: No checkpoint-scoped declaration of action-parameter units, coordinate-frame conventions, or an output JSON schema for action payloads for lerobot/smolvla_robotwin was found in the inspected primary files (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: No post-inference validation rules, bounds checks, or example output validation guidance for this checkpoint were found in the inspected checkpoint-scoped primary files (https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json).
- Evidence gap: No checkpoint-scoped comparisons with numeric, protocol-matched benchmarks for lerobot/smolvla_robotwin were found; therefore protocol-matched numeric comparison is not possible from checkpoint-scoped primary evidence (checked sources: https://huggingface.co/lerobot/smolvla_robotwin/blob/main/config.json; upstream context: https://arxiv.org/pdf/2506.01844).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/lerobot/smolvla_robotwin Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1] uses unapproved repository owner 'arrow-hf' for this exact model scope: $.sources[1] uses unapproved repository owner 'arrow-hf' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2] uses unapproved repository owner 'collections' for this exact model scope: $.sources[2] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
