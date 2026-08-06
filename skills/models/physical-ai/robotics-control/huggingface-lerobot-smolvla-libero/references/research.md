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

- Research key: `huggingface-co-lerobot-smolvla-libero-13a04e8a43`
- Independent audit: `revised`
- Researched: `2026-08-06T12:08:14.235460+00:00`

The official Hugging Face repository for lerobot/smolvla_libero identifies the checkpoint as a compact SmolVLA-family vision-language-action model (model card / README). The repository-hosted configuration (config.json) declares runtime and model flags and payload-level normalization and dimensionality constraints: device="cuda", use_amp=false, use_peft=false, push_to_hub=true, repo_id="pepijn223/smolvla_libero", pretrained_path="lerobot/smolvla_base", chunk_size=50, n_action_steps=50, num_steps=10, tokenizer_max_length=48, normalization_mapping mapping VISUAL->"IDENTITY", STATE->"MEAN_STD", ACTION->"MEAN_STD", max_state_dim=32, max_action_dim=32, and resize_imgs_with_padding=[512,512]. The model card/README presents human-facing claims about compact/efficient design and deployability but does not present numeric benchmark tables in the examined primary artifacts. The examined primary artifacts (model card / config.json) do not report an explicit immutable checkpoint revision, parameter count, or a LICENSE file. The repository configuration references a pretrained_path (lerobot/smolvla_base) but the canonical upstream repository for that pretrained_path was not inspected as part of these primary-artifact checks and therefore is treated as upstream-checkpoint metadata (not verified here).

## Identity

- Upstream name: lerobot/smolvla_libero
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Vision-language-action (SmolVLA-family) stack
- License: not reported
- Evidence: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

## Selection

### Recommended

- **Research and development on compact vision-language-action policy modeling (SmolVLA-family) and LIBERO-style sensorimotor policy experiments** — The model card/README characterizes the checkpoint as a compact, efficient SmolVLA-family vision-language-action model and the repository config.json documents normalization mappings, tokenizer_max_length, and dimensionality flags that match vision-language-action research payloads.
  Scope: lerobot/smolvla_libero
  Evidence: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Conditional

- **Integrate into real-robot control workflows only after implementer validation and creation of a full action decoding and platform-specific safety pipeline** — Config.json declares normalization mapping ACTION->"MEAN_STD" and max_action_dim but the examined primary artifacts do not publish an end-to-end, execution-safe action-to-robot-command decoder, coordinate-frame specification, units, or rate limits; implementers must create and validate those runtime mappings and safety checks before hardware execution.
  Scope: lerobot/smolvla_libero
  Evidence: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Avoid

- **Clinical, medical, or other regulated safety‑critical decision making** — The examined primary artifacts (model card / config.json) do not present documentation of clinical validation, PHI handling, or domain-specific expert-review processes for this checkpoint.
  Scope: lerobot/smolvla_libero
  Evidence: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

## Input preparation

### Semantic inputs

- The configuration declares a normalization_mapping that includes keys VISUAL, STATE, and ACTION. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- The configuration declares a maximum state dimensionality via max_state_dim = 32. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- The configuration declares a maximum action dimensionality via max_action_dim = 32. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- The configuration declares tokenizer_max_length = 48 indicating a textual input length bound. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Accepted formats

- Images / visual inputs: the configuration sets resize_imgs_with_padding to [512, 512], indicating images should be resized/padded to that resolution before further processing. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- State observations: the configuration exposes a max_state_dim of 32; callers should provide dense numeric state vectors within that dimensionality bound. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Text inputs: the configuration includes tokenizer_max_length = 48 as the declared maximum token length; however, serialized tokenizer artifacts are not published in the examined primary artifacts (see evidence gaps). Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Preprocessing

- Images are to be resized with padding to [512, 512] as indicated by config.json's resize_imgs_with_padding field. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Normalization mapping in config.json assigns VISUAL -> "IDENTITY" and STATE/ACTION -> "MEAN_STD", indicating different normalization methods per feature group. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Pre-submit validation

- Callers should validate that provided state vectors do not exceed max_state_dim (32) and that action vectors conform to max_action_dim (32) before inference because these bounds are declared in config.json. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Evidence gap: Serialized tokenizer and feature-extractor artifacts required to deterministically reproduce tokenization and vision preprocessing were not found in the examined primary artifacts (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json). Sources: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Task-specific formatting

- Config.json declares various runtime and model flags (device, use_amp, use_peft, push_to_hub, pretrained_path, chunk_size, n_action_steps, num_steps) and normalization mapping, but the examined primary artifacts do not include canonical end-to-end JSON payload examples or prompt templates. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero

## Output interpretation

### Outputs

- Config.json declares a normalization mapping for ACTION -> "MEAN_STD" and sets max_action_dim = 32, indicating the model emits an action feature group bounded by that dimensionality. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Interpretation

- ACTION outputs are denormalized under a MEAN_STD convention as declared in config.json, but the examined primary artifacts do not publish a canonical execution-level decoder mapping (coordinate frames, units, joint vs end-effector mapping, or rate limits) required to safely convert denormalized tensors to robot commands. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero
- Primary sources do not publish per-action confidence scores or probabilistic calibration metadata for action outputs in the examined artifacts. Sources: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

### Post-inference validation

- Integrators must implement and validate normalization/denormalization consistent with config.json's mapping, and must create platform-specific safety checks (coordinate-frame verification, units, and rate limiting) prior to executing actions on hardware because the examined primary artifacts do not provide a complete execution-safe mapping. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero
- Evidence gap: No canonical per-action calibration/confidence semantics or probabilistic calibration metadata were found in the examined primary artifacts; downstream calibration and validation are required (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json). Sources: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Config.json documents normalization mapping and maximum dimensionalities (max_state_dim=32, max_action_dim=32) but the repository does not include canonical inference examples to reconcile run-time payload variants; implementers must exercise caution when providing inputs that differ from declared mappings. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero
- Evidence gap: No canonical upstream checkpoint revision hash, release tag, or immutable identifier for the model weights was reported in the examined repository artifacts (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json). Sources: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Evidence gap: The examined repository artifacts do not include an explicit license file or an explicit license declaration for model weights and/or code (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json). Sources: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Evidence gap: The examined primary artifacts do not provide a complete action postprocessing contract (coordinate frames, units, joint vs end-effector mapping, or per-action rate limits); implementers must supply and validate these mappings before execution. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero

### Safety

- Evidence gap: The provided primary artifacts do not publish explicit safety, privacy, clinical, or dual-use mitigation guidance for this checkpoint; conservative operational handling and human-in-the-loop safeguards are advised (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Implementers bear responsibility for safe integration and pre-execution validation (coordinate-frame checks, rate limiting, and platform-specific safety tests) because the examined primary artifacts do not define a full execution-safe action decoder mapping. Sources: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### LeRobot SmolVLA Libero model page

- URL: https://huggingface.co/lerobot/smolvla_libero
- Publisher: LeRobot / Hugging Face model hub
- Type: `model-card`
- Primary because: Official Hugging Face model repository root hosted by the upstream owner; serves as the model card and repository entry for this checkpoint.
- Scope: lerobot/smolvla_libero
- Supports: Human-facing model card / README content describing SmolVLA as a compact/efficient vision-language-action model and general repository metadata

### Checkpoint configuration (config.json) for lerobot/smolvla_libero

- URL: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Publisher: LeRobot / Hugging Face repository
- Type: `repository`
- Primary because: Repository-hosted checkpoint configuration describing declared input/output feature groups, normalization mapping, resize settings, and runtime flags.
- Scope: lerobot/smolvla_libero (config.json)
- Supports: Defines device, use_amp, use_peft, push_to_hub, repo_id, pretrained_path, chunk_size, n_action_steps, num_steps, tokenizer_max_length, normalization_mapping (VISUAL/STATE/ACTION), max_state_dim=32, max_action_dim=32, resize_imgs_with_padding=[512,512]

## Evidence gaps

- Evidence gap: No canonical upstream checkpoint revision hash, release tag, or immutable identifier for lerobot/smolvla_libero was identified in the examined primary artifacts (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: Serialized tokenizer artifact files (vocab, merges, tokenizer.json) and serialized vision feature-extractor/processor artifacts were not identified in the examined primary artifacts (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: The examined primary artifacts do not include an explicit LICENSE file or an explicit license declaration for model weights and/or code (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: The config.json references pretrained_path="lerobot/smolvla_base" but the canonical upstream pretrained checkpoint repository was not inspected as part of these primary-artifact checks; upstream-checkpoint evidence for lerobot/smolvla_base must be opened separately to verify transfer or weight-sharing claims (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: The examined primary artifacts do not publish a complete, execution-safe action decoder mapping (coordinate frames, units, joint vs end-effector mapping, per-action rate limits); checked locators: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json.
- Evidence gap: No canonical per-action calibration, confidence-score semantics, or probabilistic calibration metadata for action outputs were found in the examined primary artifacts (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: No numeric benchmark tables or exact metric values for this exact checkpoint were present in the examined primary artifacts (checked: README and config at https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: Head-to-head, protocol-matched numeric benchmark comparisons between lerobot/smolvla_libero and alternate candidates are not present in the examined primary artifacts (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).
- Evidence gap: The examined primary artifacts do not include end-to-end JSON payload examples, prompt templates, or canonical inference request/response samples (checked: https://huggingface.co/lerobot/smolvla_libero and https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 17 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1] uses unapproved repository owner 'ralfroemer' for this exact model scope: $.sources[1] uses unapproved repository owner 'ralfroemer' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses unapproved repository owner 'huggingfacevla' for this exact model scope: $.sources[4] uses unapproved repository owner 'huggingfacevla' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[11] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[12] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[14] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'rail-berkeley' for this exact model scope: $.sources[18] uses unapproved repository owner 'rail-berkeley' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24] uses forbidden secondary URL https: $.sources[24] uses forbidden secondary URL https://labellerr.com/blog/molmoact2-open-robot-ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24].primary must be true: $.sources[24].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[27].primary must be true: $.sources[27].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[28].primary must be true: $.sources[28].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[29].primary must be true: $.sources[29].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[31] uses unapproved repository owner 'allenai' for this exact model scope: $.sources[31] uses unapproved repository owner 'allenai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
