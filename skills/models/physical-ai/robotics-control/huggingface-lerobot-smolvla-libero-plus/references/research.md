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

- Research key: `huggingface-co-lerobot-smolvla-libero-plus-2c9c8f8e10`
- Independent audit: `revised`
- Researched: `2026-08-06T12:20:16.459453+00:00`

Primary-source verification for the exact checkpoint libero-plus-7bb70aa-state8-sm103-sdpa-02z of lerobot/smolvla_libero_plus. Evidence confirms model naming, input modalities, action-output shape, tokenizer length, and VLM configuration from model card and config.json. Significant evidence gaps remain for parameter count, explicit license for weights, immutable provenance revision/sha, checkpoint-scoped benchmarks, and explicit safety/calibration guidance for real-world robotic deployment.

## Identity

- Upstream name: lerobot/smolvla_libero_plus
- Checkpoint/version: libero-plus-7bb70aa-state8-sm103-sdpa-02z
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Vision-language-action checkpoint using VLM name 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'; attention mode 'cross_attn'; VLM layers = 16; output action feature shape [7]; images internally resized/padded to 512x512 (see config.json).
- License: not reported
- Evidence: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json, https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json

## Selection

### Recommended

- **Research and prototyping of vision-language-action policies for manipulation tasks (simulation or lab), using the checkpoint's VLM and action head as provided.** — The model card and config.json describe a compact SmolVLA vision-language-action checkpoint, document inputs (text, images, state) and an action output feature, and state the model is intended as a compact/efficient VLA model suitable for consumer-grade hardware and research use.
  Scope: lerobot/smolvla_libero_plus (checkpoint: libero-plus-7bb70aa-state8-sm103-sdpa-02z)
  Evidence: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- **Low-resource local inference for robotics experimentation where a compact VLM is required (research/prototyping only).** — The model card text and model naming describe SmolVLA as compact and deployable on consumer-grade hardware; configuration indicates use_amp=false and device 'cuda' in the repo guidance.
  Scope: lerobot/smolvla_libero_plus (checkpoint: libero-plus-7bb70aa-state8-sm103-sdpa-02z)
  Evidence: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Conditional

- **Simulation-only research context using related derived SmolVLA checkpoints; verify alignment with exact checkpoint and protocol before any definitive claims.** — Intended for simulation-based exploration leveraging derived SmolVLA checkpoints; explicit protocol and exact-checkpoint alignment not established in primary sources for libero-plus-7bb70aa-state8-sm103-sdpa-02z.
  Scope: Derived checkpoints (example: katsukiono/smolvla-libero-spatial-4arm) — not authoritatively verified for libero-plus-7bb70aa
  Evidence:

### Avoid

- **Deployment for safety-critical autonomous robotic operation without human oversight or expert system-level validation.** — Evidence gap: Safety-critical autonomous deployment without human oversight or expert-system validation is not documented in primary sources.
  Scope: lerobot/smolvla_libero_plus (checkpoint: libero-plus-7bb70aa-state8-sm103-sdpa-02z)
  Evidence: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

## Input preparation

### Semantic inputs

- Text instructions or prompts (natural language) are accepted as language input; tokenizer maximum length is 48 tokens as specified in config.json. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Visual inputs: camera images are an expected input modality; the libero_plus config specifies image shape and image resizing behaviour (images are resized with padding to 512x512 and observation.images.empty_camera_1 shape [3,480,640] is present in the config). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Robot state: numeric state vector with maximum configured dimension 32 (max_state_dim = 32). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Accepted formats

- Text: natural-language prompts tokenized with the configured tokenizer (tokenizer max length 48). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Images: RGB camera images that the config indicates will be resized with padding to 512x512 before processing. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Robot state: numeric state vector with maximum configured dimension 32 (max_state_dim = 32). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Preprocessing

- Images are resized with padding to 512x512 as specified in the config.json. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Normalization mappings: VISUAL = IDENTIY; STATE = MEAN_STD; ACTION = MEAN_STD as recorded in the config. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Language inputs use padding mode 'max_length' per config (language_padding = 'max_length'); tokenizer max length set to 48. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Pre-submit validation

- Validate that tokenized text length does not exceed 48 tokens (tokenizer max length = 48 in config). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Validate robot state vectors conform to maximum dimension 32 (max_state_dim = 32 in config). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Validate image inputs are preprocessed to the expected 512x512 padded size and channel ordering expected by the model (config indicates resize_with_padding to 512x512). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Evidence gap: primary sources do not specify full input schema examples, value ranges, or explicit camera calibration requirements — inspected locations: model card page sections and config.json (see sources). Sources: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Task-specific formatting

- Language padding policy is 'max_length' (language_padding = 'max_length' in config) and tokenizer max_length is 48; follow that padding/truncation behavior for text prompts. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Model attention mode is configured as 'cross_attn' and the model uses a VLM named 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct' per config; follow the repo examples for prompt composition if provided in the model card. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Number of action steps (n_action_steps) is 50 in the config; when using the model for multi-step action prediction, align action sequence length accordingly. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

## Output interpretation

### Outputs

- The config declares an output action feature with shape [7] (output_features.action shape = [7]). Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- The model exposes an action sequence length parameter (n_action_steps = 50) and num_steps = 10 inference steps in config; outputs are shaped per the configured action/output_features. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Interpretation

- Interpret the primary action output as a numeric action vector of length 7 as reported in the checkpoint config; mapping from vector indices to robot joints/commands is not documented in the inspected primary sources. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- The precise semantic meaning of each component of the action vector (units, joint mapping, coordinate frames) is not specified in the config.json or model card pages inspected. Sources: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Post-inference validation

- Validate that model outputs match the declared action feature shape ([7]) before downstream execution; reject or require human review if shape or value ranges are unexpected. Sources: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Evidence gap: the precise post-inference calibration, safety checks, or recommended thresholds for executing actions on hardware are not documented in primary sources. Sources: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

###  — `insufficient-evidence`

- Task:
- Criteria:
- Rationale:
- Comparison conditions:
- Evidence:

## Limitations and safety

### Limitations

- Evidence gap: the primary sources inspected (model card and config.json) do not report a parameter count or explicit parameterScale for this checkpoint; checked model card page and config.json for parameter/scale metadata. Sources: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Evidence gap: no checkpoint-specific numeric benchmark results for libero-plus-7bb70aa-state8-sm103-sdpa-02z were found in the model card or config.json; public benchmark tables/figures were not present in these inspected primary sources. Sources: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

### Safety

- Evidence gap: inspected primary sources do not document safety constraints, recommended human-in-the-loop requirements, or validated safety-test procedures for real-world robotic deployment; users should apply expert review and hardware-in-the-loop safety testing before any physical deployment. Sources: https://huggingface.co/lerobot/smolvla_libero_plus, https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### lerobot/smolvla_libero_plus — Hugging Face model card

- URL: https://huggingface.co/lerobot/smolvla_libero_plus
- Publisher: LeRobot / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card and repository page for the checkpoint named in the dossier; provides descriptive text and links to repository files.
- Scope: lerobot/smolvla_libero_plus (checkpoint repository and model card)
- Supports: model naming as smolvla
- Supports: compact/consumer-grade deployment claims
- Supports: general usage documentation and repository pointers

### lerobot/smolvla_libero_plus config.json (repository file)

- URL: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json
- Publisher: LeRobot / Hugging Face
- Type: `repository`
- Primary because: Primary repository configuration file for lerobot/smolvla_libero_plus containing concrete configuration values referenced throughout this dossier (input shapes, normalization, tokenizer settings, VLM name, output shapes).
- Scope: lerobot/smolvla_libero_plus config.json (exact file inspected)
- Supports: image resizing to 512x512
- Supports: output_features.action shape [7]
- Supports: max_state_dim = 32
- Supports: max_action_dim = 32
- Supports: tokenizer max length = 48
- Supports: VLM model name 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'
- Supports: attention mode 'cross_attn'
- Supports: n_action_steps and other training/inference hyperparameters

### lerobot/smolvla_libero — Hugging Face model card

- URL: https://huggingface.co/lerobot/smolvla_libero
- Publisher: LeRobot / Hugging Face
- Type: `model-card`
- Primary because: Related official Hugging Face page describing the SmolVLA family and compact-efficiency design; used to corroborate family-level statements about compactness and deployability.
- Scope: lerobot/smolvla_libero (family-level page)
- Supports: description of SmolVLA as compact and efficient
- Supports: guidance that SmolVLA is intended for consumer-grade deployment/efficiency

### lerobot/smolvla_libero config.json (repository file)

- URL: https://huggingface.co/lerobot/smolvla_libero/blob/main/config.json
- Publisher: LeRobot / Hugging Face
- Type: `repository`
- Primary because: Configuration file for the related smolvla_libero checkpoint used to corroborate common config fields and family conventions (resize, normalization mappings, tokenizer settings).
- Scope: lerobot/smolvla_libero config.json (file inspected)
- Supports: image resizing with padding to 512x512
- Supports: normalization mappings and tokenizer settings
- Supports: training/inference hyperparameter defaults

## Evidence gaps

- Benchmark gap: No checkpoint-scoped numeric benchmark results for libero-plus-7bb70aa-state8-sm103-sdpa-02z were found in the inspected primary sources. Checked: https://huggingface.co/lerobot/smolvla_libero_plus (model card page, all headings and README content) and https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json (config file). No tables or numeric benchmark entries for this exact checkpoint were present.
- Comparison gap: No task- and protocol-matched, checkpoint-scoped comparisons for libero-plus-7bb70aa-state8-sm103-sdpa-02z were found in primary sources. Checked: https://huggingface.co/lerobot/smolvla_libero_plus and https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json for any comparison tables or explicit competitor benchmark rows; none present.
- Parameter-scale gap: The checkpoint config and model card do not report the model parameter count or explicit parameterScale. Checked: https://huggingface.co/lerobot/smolvla_libero_plus and https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json (config.json 'license' is null and no parameter count field present).
- License gap: The checkpoint config.json has license=null and the model card does not provide a distinct model-weights license in the inspected locations. Checked: https://huggingface.co/lerobot/smolvla_libero_plus and https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json.
- Output-semantic gap: The precise semantic mapping from the declared action vector components (output_features.action shape = [7]) to robot joints/actuators, including units and coordinate frames, is not specified in the inspected primary sources. Checked: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json and https://huggingface.co/lerobot/smolvla_libero_plus.
- Input-schema gap: No full robot_state JSON schema examples, explicit camera calibration documentation, or coordinate-frame documentation for the robot_state provided in the inspected primary sources. Checked: https://huggingface.co/lerobot/smolvla_libero_plus and https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json.
- Post-inference safety/calibration gap: The model card and config.json do not specify post-inference calibration, safety checks, or recommended thresholds for physical execution. Checked: https://huggingface.co/lerobot/smolvla_libero_plus and https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json.
- Checkpoint provenance gap: While the config indicates pretrained_path = 'lerobot/smolvla_base' and repository IDs referencing pepijn223 are present in config metadata fields, the inspected primary files do not provide a published revision string or immutable model-weight SHA for libero-plus-7bb70aa-state8-sm103-sdpa-02z. Checked: https://huggingface.co/lerobot/smolvla_libero_plus/blob/main/config.json and https://huggingface.co/lerobot/smolvla_libero_plus.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 47 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property acceptedFormats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property acceptedFormats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property preprocessing Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property taskSpecificFormatting Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property validation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceVLA/smolvla_libero Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2510.13626v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://smolvla.net/paper_en.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceVLA/smolvla_libero Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2510.13626v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://smolvla.net/index_en.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://smolvla.net/paper_en.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openreview.net/pdf/d88b3b83cfa1569a610ef78728ce89d8bfd9d8e5.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2510.13626v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/josefchen/smolvla-libero-obj-t2-lora/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/lerobot/smolvla_libero_plus Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://josefchen/smolvla-libero-obj-t2-lora/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://goelshivam1210/smolvla-libero-lora-r32/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/josefchen/smolvla-libero-obj-t2-lora/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.evidenceGapsNote: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
