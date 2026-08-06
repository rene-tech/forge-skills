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

- Research key: `huggingface-co-qwen-qwen2-5-vl-7b-instruct-557edb1d63`
- Independent audit: `revised`
- Researched: `2026-08-06T09:02:15.618709+00:00`

Primary-source artifacts for the exact checkpoint Qwen2.5-VL-7B-Instruct were inspected. The Hugging Face model page and repository files (config.json, preprocessor_config.json, README.md) identify the model architecture as Qwen2_5_VLForConditionalGeneration, list vision/image/video token IDs and visual-processor parameters (patch_size=14, temporal_patch_size=2, min_pixels/max_pixels), and report multiple multimodal benchmark scores in the model README. The upstream Qwen2.5 technical report (arXiv:2412.15115) documents the Qwen2.5 family training scale and family-level design decisions but does not provide checkpoint-level parameter counts or model-card file contents for this exact checkpoint. Several checkpoint-level numeric benchmark values (MVBench, PerceptionTest, Video-MME, LVBench, LongVideoBench, MMBench-Video, TempCompass, MLVU, Agent sub-scores) are reported on the Hugging Face model page/README; the repository config and preprocessor files supply tokenizer/vision-processor parameter values and special token IDs. Multiple explicit evidence gaps remain for the exact checkpoint: an explicit parameter-count (total parameters) for this checkpoint, an explicit license string exposed in a primary-file on the checkpoint page, and primary evidence that the model emits structured bounding-box or JSON extraction outputs. All cited evidence URLs appear in the dossier sources list.

## Identity

- Upstream name: Qwen2.5-VL-7B-Instruct
- Checkpoint/version: Qwen2.5-VL-7B-Instruct
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Qwen2_5_VLForConditionalGeneration (multimodal vision-language transformer)
- License: not reported
- Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blame/57a7cc3cd9781e958d5ec85a268fe66f515e0612/preprocessor_config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://arxiv.org/pdf/2412.15115

## Selection

### Recommended

- **General multimodal question answering and scene understanding (text+image/video to text)** — The Hugging Face model page and repository README provide an inference example using the processor.apply_chat_template and model.generate code path and report multimodal benchmark scores indicating multimodal QA/video capabilities for the exact Qwen2.5-VL-7B-Instruct checkpoint.
  Scope: Qwen2.5-VL-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md
- **Long-form video/multimodal temporal understanding (research/evaluation)** — The Hugging Face model page/README for Qwen2.5-VL-7B-Instruct reports LongVideoBench and other video-related benchmark scores and the preprocessor/config indicate temporal_patch_size and video token IDs for video inputs, supporting evaluation-oriented long-video understanding use under the reported evaluation conditions.
  Scope: Qwen2.5-VL-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blame/57a7cc3cd9781e958d5ec85a268fe66f515e0612/preprocessor_config.json

### Conditional

- **Structured extraction (bounding-box or JSON extraction) from images/documents** — Evidence gap: primary files inspected (model README, config.json, preprocessor_config.json) do not provide an explicit example or documented output contract that the checkpoint directly emits bounding-box coordinates or structured JSON extraction outputs. Use of this checkpoint for direct structured extraction requires a verified downstream head/service or additional evaluation demonstrating that the checkpoint (as released) produces bounding-box/structured outputs.
  Scope: Qwen2.5-VL-7B-Instruct (requires downstream extraction head or adapter unless explicit structured-head evidence is supplied)
  Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

### Avoid

- **Clinical, medical, or other safety‑critical decision-making** — Evidence gap: no primary evidence in the inspected checkpoint repository files or technical report documents any clinical validation, regulatory evaluation, or explicit clinical‑use safeguards for Qwen2.5-VL-7B-Instruct. The model README and config do not document clinical datasets, certifications, or instructions for safety‑critical deployment.
  Scope: Qwen2.5-VL-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://arxiv.org/pdf/2412.15115

## Input preparation

### Semantic inputs

- The checkpoint accepts multimodal inputs including text, images, and video tokens (video supported per model README and model config token IDs). Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json
- Visual inputs are represented via special vision/image/video token IDs defined in the model config (vision start, vision end, vision token, image token, video token). Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

### Accepted formats

- The model repository and README provide an inference snippet using the processor and model.generate for image (and video) inputs; images/videos are the accepted visual input types for the checkpoint as published. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct

### Preprocessing

- The preprocessor_config.json defines patch_size = 14 and temporal_patch_size = 2 for the visual processor. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blame/57a7cc3cd9781e958d5ec85a268fe66f515e0612/preprocessor_config.json
- The preprocessor_config.json defines min_pixels = 3136 and max_pixels = 12845056 and merge_size = 2 for visual preprocessing; image mean and std normalization are defined. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blame/57a7cc3cd9781e958d5ec85a268fe66f515e0612/preprocessor_config.json
- The model config indicates a sliding window context size and related positional settings (sliding_window_size = 32768 tokens and max_position_embeddings = 128000) relevant to text preprocessing and context-windowing behavior. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

### Pre-submit validation

- Validate that images conform to the preprocessor pixel bounds (min_pixels and max_pixels) specified in preprocessor_config.json before submission. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blame/57a7cc3cd9781e958d5ec85a268fe66f515e0612/preprocessor_config.json
- Validate text context lengths against the model's sliding window size (32768) and max_position_embeddings (128000) as declared in config.json to avoid truncation artifacts. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

### Task-specific formatting

- The repository README demonstrates using processor.apply_chat_template with add_generation_prompt=True followed by model.generate(max_new_tokens=128) as an example prompt/formatting flow for instruction-following multimodal chat. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md

## Output interpretation

### Outputs

- Primary emissions from the checkpoint are autoregressive text outputs produced via model.generate (inference example present in README). Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md
- The model config defines special token IDs for vision and media tokens (vision start/end, vision token, image token, video token) used in multimodal input encoding; these are internal token semantics present in config.json. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

### Interpretation

- Evidence gap: The inspected primary files do not document that the checkpoint directly emits structured bounding-box coordinates or JSON-structured extraction outputs; therefore do not assume structured localization outputs without downstream components or explicit documented output contracts. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

### Post-inference validation

- Post-inference validation should include checking for presence and correct ordering of special vision/media tokens when replaying or verifying multimodal input-output pairs, per token IDs declared in config.json. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json
- Sanity-check generated text length against max_new_tokens usages in example inference (README) and verify that long-context sliding behavior matches the declared sliding_window_size to detect truncation or context-wrapping issues. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json

## Public benchmarks

### MVBench

- Dataset/split: MVBench / not reported
- Metric/value: MVBench score / 69.6 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: As reported in the Hugging Face model README/metrics section for this checkpoint; no separate protocol table or dataset split locator was found in the inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: The README lists the score but does not provide a protocol table or explicit dataset split in the inspected primary files.

### PerceptionTest

- Dataset/split: PerceptionTest / not reported
- Metric/value: PerceptionTest score / 70.5 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: As reported in the Hugging Face model README/metrics section for this checkpoint; no separate protocol table or dataset split locator was found in the inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: The README lists the score but does not provide a protocol table or explicit dataset split in the inspected primary files.

### Video-MME

- Dataset/split: Video-MME / not reported
- Metric/value: Video-MME score / 65.1/71.6 (without subtitles) (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: As reported on the model README; no separate protocol table or exact split locator found in inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: The README reports two numbers (65.1/71.6) with the parenthetical 'without subtitles' but does not include the underlying evaluation table or exact dataset split in the inspected files.

### LVBench

- Dataset/split: LVBench / not reported
- Metric/value: LVBench score / 45.3 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: Reported in README; protocol table or split not present in inspected primary files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: No detailed evaluation table or split locator found in the inspected files.

### LongVideoBench

- Dataset/split: LongVideoBench / not reported
- Metric/value: LongVideoBench score / 54.7 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: Reported in README; no detailed protocol table or split locator found in the inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: The README presents the aggregated score but does not include an explicit evaluation table or split details in the inspected files.

### MMBench-Video

- Dataset/split: MMBench-Video / not reported
- Metric/value: MMBench-Video score / 1.79 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: As reported in the README; no further protocol details found in inspected primary files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: The README provides a scalar but no dataset split or evaluation table in the inspected files.

### TempCompass

- Dataset/split: TempCompass / not reported
- Metric/value: TempCompass score / 71.7 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: Reported on the model README; no separate protocol table or split locator was found in inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: No detailed evaluation protocol or split was present in the inspected primary files.

### MLVU

- Dataset/split: MLVU / not reported
- Metric/value: MLVU score / 70.2 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct
- Conditions: Reported in README; no protocol table or split locator found in the inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Locator: README.md (model metrics section)
- Caveat: The README lists the score but does not include underlying tables or split information in the inspected primary files.

### Agent (ScreenSpot / AITZ_EM / Android Control Low_EM sub-scores)

- Dataset/split: Agent benchmark (subtests ScreenSpot, AITZ_EM, Android Control Low_EM) / not reported
- Metric/value: Agent sub-scores / ScreenSpot 84.7; AITZ_EM 81.9; Android Control Low_EM 93.7 (`context-only`)
- Model scope: Qwen2.5-VL-7B-Instruct (as reported)
- Conditions: Reported in the README; the README provides sub-scores but no detailed protocol tables or splits in inspected files.
- Source: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md
- Locator: README.md (model metrics section)
- Caveat: Inspected repository files do not include the full evaluation tables or split definitions for the Agent benchmark.

## Comparisons

### Qwen2.5-7B-Instruct — `insufficient-evidence`

- Task: Parameter-scale, context-length, and non-visual vs visual variant tradeoffs
- Criteria: Parameter count and exact checkpoint-level parameterization are not both documented for direct comparison; Qwen2.5-7B-Instruct (non-visual) page reports parameter counts but the Qwen2.5-VL-7B-Instruct checkpoint files inspected do not report a total parameter count.
- Rationale: The Hugging Face page for the non-visual Qwen2.5-7B-Instruct reports total and non-embedding parameter counts; the Qwen2.5-VL-7B-Instruct repository/config do not include an explicit total-parameter count. Without an explicit per-checkpoint parameter count for Qwen2.5-VL-7B-Instruct, direct parameter-count comparisons are not supported by inspected primary files.
- Comparison conditions: Compared files: Qwen2.5-VL-7B-Instruct config.json and README (no total parameter count found) versus Qwen2.5-7B-Instruct model card which lists parameter counts.
- Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

## Limitations and safety

### Limitations

- Evidence gap: The exact total parameter count for the Qwen2.5-VL-7B-Instruct checkpoint is not reported in the inspected checkpoint files (config.json, README) and thus cannot be verified from the primary checkpoint artifacts. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Evidence gap: The checkpoint repository files inspected do not surface an explicit license string for the checkpoint weights in the checked files; license attribution for this checkpoint could not be verified from the inspected primary artifacts. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Reported benchmark scores appear in the model README, but the inspected primary files do not include underlying protocol tables, dataset split locators, or evaluation scripts; this limits reproducibility and comparability of the reported numeric results. Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md, https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct

### Safety

- Evidence gap: The inspected checkpoint repository and the Qwen2.5 technical report do not provide documented safety, privacy, or data-handling rules specific to this checkpoint for high-risk domains (clinical, biosecurity, or other regulated contexts). Sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://arxiv.org/pdf/2412.15115

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen2.5-VL-7B-Instruct

- URL: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card / repository for the exact checkpoint Qwen2.5-VL-7B-Instruct; contains README, config, and links to checkpoint files.
- Scope: Qwen2.5-VL-7B-Instruct checkpoint (Hugging Face model page and model card)
- Supports: Reported benchmark scores for the checkpoint (README metrics section)
- Supports: General model usage example (README inference snippet)
- Supports: Checkpoint-level repository presence

### Qwen2.5-VL-7B-Instruct README.md

- URL: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md
- Publisher: Hugging Face (repository README)
- Type: `repository`
- Primary because: Repository README for the checkpoint containing usage examples and the reported checkpoint benchmark scores used in this dossier.
- Scope: Qwen2.5-VL-7B-Instruct README (metrics and inference examples)
- Supports: Inference example using processor.apply_chat_template and model.generate
- Supports: Reported MVBench, PerceptionTest, Video-MME, LVBench, LongVideoBench, MMBench-Video, TempCompass, MLVU, and Agent sub-scores for the checkpoint

### Qwen2.5-VL-7B-Instruct config.json

- URL: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json
- Publisher: Hugging Face (repository file)
- Type: `repository`
- Primary because: Official checkpoint configuration file stored in the Hugging Face repository for this checkpoint; contains architecture identifier, token IDs, vision encoder parameters, sliding window size, and other model-level configuration values.
- Scope: Qwen2.5-VL-7B-Instruct config.json (checkpoint configuration)
- Supports: Architecture identifier Qwen2_5_VLForConditionalGeneration
- Supports: Vision encoder patch_size = 14, vision encoder depth and hidden size, vision token IDs
- Supports: sliding_window_size = 32768 and max_position_embeddings = 128000
- Supports: special token IDs for BOS/EOS and vision/media tokens

### Qwen2.5-VL-7B-Instruct preprocessor_config.json (blame view inspected)

- URL: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blame/57a7cc3cd9781e958d5ec85a268fe66f515e0612/preprocessor_config.json
- Publisher: Hugging Face (repository file)
- Type: `repository`
- Primary because: Official preprocessor configuration file for this checkpoint in the repository; specifies visual preprocessing parameters such as patch size, temporal patch size, pixel bounds, and normalization.
- Scope: Qwen2.5-VL-7B-Instruct preprocessor_config.json
- Supports: patch_size = 14, temporal_patch_size = 2, merge_size = 2
- Supports: min_pixels = 3136, max_pixels = 12845056
- Supports: image_mean and image_std normalization values
- Supports: processor_class and image_processor_type entries

### Qwen2.5-7B-Instruct (non-visual variant model card)

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card for the Qwen2.5-7B-Instruct non-visual variant; used as a primary-source comparison for reported parameter counts and some architecture details for the 7B-family sibling checkpoint.
- Scope: Qwen2.5-7B-Instruct (non-visual sibling model card)
- Supports: Reported parameter counts for the non-visual 7B instruct checkpoint (7.61 billion total parameters and 6.53 billion non-embedding parameters) and context/generation length claims for that checkpoint

### Qwen2.5 technical report (arXiv:2412.15115)

- URL: https://arxiv.org/pdf/2412.15115
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical technical report / preprint describing the Qwen2.5 family and family-level training scale and methods; included as primary family-level documentation.
- Scope: Qwen2.5 family (technical report)
- Supports: Family-level training scale, staged finetuning and reinforcement learning descriptions, and listing of family model sizes

## Evidence gaps

- Evidence gap: Exact total parameter count for Qwen2.5-VL-7B-Instruct checkpoint not found in inspected primary files (checked: config.json, README). See: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json ; https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Evidence gap: Explicit license statement for the checkpoint weights or repository files was not found in the inspected checkpoint files. Check: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Evidence gap: No explicit primary-source documentation in the inspected checkpoint repository that the checkpoint emits structured bounding-box coordinates or JSON extraction outputs. Check: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct ; https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json
- Evidence gap: Reported benchmark scores appear in the model README but the inspected primary files do not include underlying evaluation protocol tables, dataset split locators, or evaluation scripts needed to reproduce or precisely compare the reported numeric results. Checked: README.md and model page: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/README.md ; https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- Evidence gap: No checkpoint-level revision identifier (immutable revision/release tag) was found in the inspected primary repository files for Qwen2.5-VL-7B-Instruct. Checked: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json ; https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 49 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property avoidUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property conditionalUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property inputPreparation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[0]: $.identity.evidenceUrls[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[1]: $.identity.evidenceUrls[1]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[2]: $.identity.evidenceUrls[2]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[3]: $.identity.evidenceUrls[3]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[4]: $.identity.evidenceUrls[4]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[5]: $.identity.evidenceUrls[5]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[6]: $.identity.evidenceUrls[6]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[7]: $.identity.evidenceUrls[7]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity.evidenceUrls[8]: $.identity.evidenceUrls[8]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://arxiv.org/pdf/2502.13923'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://faculty.cc.gatech.edu/~zk15/teaching/AY2025_cs8803vlm_fall/L10_Qwen.pdf'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://huggingface.co/docs/transformers/model_doc/qwen2_5_vl'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/config.json'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/preprocessor_config.json'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/tokenizer_config.json'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/blob/main/generation_config.json'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://arxiv.org/abs/2409.12191'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2502.13923 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://faculty.cc.gatech.edu/~zk15/teaching/AY2025_cs8803vlm_fall/L10_Qwen.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2502.13923 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://faculty.cc.gatech.edu/~zk15/teaching/AY2025_cs8803vlm_fall/L10_Qwen.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://faculty.cc.gatech.edu/~zk15/teaching/AY2025_cs8803vlm_fall/L10_Qwen.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs is empty without a section-specific evidence gap: $.inputPreparation.semanticInputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
