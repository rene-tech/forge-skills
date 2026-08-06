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

- Research key: `huggingface-co-qwen-qwen3-vl-4b-instruct-2c30792aed`
- Independent audit: `revised`
- Researched: `2026-08-06T09:42:23.287087+00:00`

Primary-source artifacts inspected for the exact checkpoint named Qwen3-VL-4B-Instruct show: (1) repository config.json lists architecture as "Qwen3VLForConditionalGeneration", model_type "qwen3_vl", text vocabulary size 151936, vision-related token ids and vision/patch parameters (see config.json file keys), and tokenizer_config.json lists tokenizer class and special tokens; (2) the Hugging Face model card asserts multimodal (image+text) inputs and text outputs and documents generation hyperparameters and capability claims; (3) a separate arXiv technical-report URL is present among sources but the Hugging Face page and the arXiv URL present differing identifiers (see ambiguity below). Verified numeric/tokenization facts are taken from the checkpoint config and tokenizer file. Primary sources do not publish checkpoint-specific numeric benchmark tables or standard prompt templates for this exact checkpoint. Note: there is an ambiguity between the Hugging Face model-card's cited Qwen3 technical-report identifier (2505.09388 referenced in the model-card facts) and a separate arXiv listing found at 2511.21631; both were checked and are listed in sources below.

## Identity

- Upstream name: Qwen3-VL-4B-Instruct
- Checkpoint/version: Qwen3-VL-4B-Instruct
- Immutable revision: not reported
- Parameter scale: 4B
- Architecture/head: Qwen3VLForConditionalGeneration
- License: Apache-2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://arxiv.org/abs/2511.21631, https://featherless.ai/models/Qwen/Qwen3-VL-4B-Instruct

## Selection

### Recommended

- **OCR and visual document understanding** — The Hugging Face model card describes expanded OCR and long-document structure parsing and the repository README describes enhanced visual perception and document-related capabilities; config and tokenizer show explicit vision configuration enabling image tokens.
  Scope: Qwen3-VL-4B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json
- **Visual question answering (VQA) and multimodal reasoning** — The Hugging Face model card and repository README describe multimodal capabilities, visual reasoning, and enhanced multimodal reasoning; vision+text configuration entries in config.json support image token integration into generation.
  Scope: Qwen3-VL-4B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json
- **Lightweight multimodal/visual-context assistance (e.g., UI description, visual coding hints)** — The README describes enhanced agent interaction capabilities and deeper visual perception applicable to visual-context tasks; the model card documents multimodal chat-style interaction and vision configuration.
  Scope: Qwen3-VL-4B-Instruct
  Evidence: https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json

### Conditional

- **Multimodal reasoning with constrained/prompted flows (image+text)** — Primary sources do not provide canonical prompt templates, formal evaluation protocols, or verified downstream validation for this exact checkpoint; any production deployment requires downstream validation and prompt engineering specific to the use-case.
  Scope: Qwen3-VL-4B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md
- **Image-based content moderation or sensitive-visual-content filtering** — Primary sources do not document safety controls, validated moderation thresholds, or certified usage for safety-critical filtering. Treat as unvalidated for safety-critical filtering until third-party validation and policy controls are added.
  Scope: Qwen3-VL-4B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md

### Avoid

- **High-stakes medical, pharmacological, legal, or PHI-sensitive tasks** — Primary sources (model card, repository README, config/tokenizer files, and technical-report listing) do not document validated safe-use claims, clinical validation, or PHI-safe guarantees for this checkpoint.
  Scope: Qwen3-VL-4B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://arxiv.org/abs/2511.21631

## Input preparation

### Semantic inputs

- Multimodal prompts accepting interleaved image and text inputs (image + text contexts) are described in the model card and repository README. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md

### Accepted formats

- Evidence gap: primary sources do not specify accepted image transport formats (URL, Base64, local file) nor size/byte limits or per-transport constraints for this checkpoint. The Hugging Face model card and repository files were checked and do not document these transport/size contracts. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json

### Preprocessing

- Tokenizer vocabulary size (text) is 151936 as recorded in config.json (text configuration key indicating vocabulary_size = 151936). Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json
- Vision/patch configuration: patch_size = 16 and spatial_merge_size = 2 and temporal_patch_size = 2 as recorded in the vision configuration section of config.json. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json
- Image/vision token identifier values present in config.json: vision_start_token_id = 151652, vision_end_token_id = 151653, and an image token ID value listed as 151655 in the config.json. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json
- Tokenizer configuration: tokenizer class 'Qwen2Tokenizer', model_max_length = 262144, and additional special tokens such as '<|im_start|>' and '<|im_end|>' are present in tokenizer_config.json (refs/pr/22 path). Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/refs%2Fpr%2F22/tokenizer_config.json

### Pre-submit validation

- Evidence gap: primary sources do not provide explicit input validation checks (e.g., required image dimensions, allowed file types, or bounds on image token counts) for this checkpoint; no such validation rules were found in the inspected model card, config.json, tokenizer_config.json, or repository README. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md

### Task-specific formatting

- Tokenizer special tokens intended for multimodal/chat formatting are present (e.g., '<|im_start|>' and '<|im_end|>' listed in tokenizer_config.json), but no canonical prompt templates or pair-input ordering are published for this exact checkpoint in the primary sources. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/refs%2Fpr%2F22/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md

## Output interpretation

### Outputs

- Primary output modality is text (text-sequence generation) driven by the conditional-generation head; the model card describes image+text inputs producing text-based outputs and the model's generation hyperparameters are listed on the model card. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct
- Generation-related hyperparameters and out-sequence length are documented on the model card (VL generation and Text generation hyperparameters, including out_seq_length values of 16384 and 32768 respectively, as presented on the model card). Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct

### Interpretation

- Evidence gap: primary sources do not provide calibration guidance, confidence-score semantics, or recommended post-processing interpretation rules for outputs from this checkpoint; the model card and repository README do not define numeric confidence semantics or calibrated scoring. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md

### Post-inference validation

- Evidence gap: primary sources do not describe post-inference quality checks, calibration procedures, or recommended downstream validation tests for outputs from this specific checkpoint; no such protocols are present in the inspected model card, config.json, tokenizer_config.json, README, or arXiv listing. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://arxiv.org/abs/2511.21631

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Primary sources do not publish checkpoint-specific numeric benchmark tables or per-dataset results for Qwen3-VL-4B-Instruct; therefore dataset-level numeric performance claims for this exact checkpoint are unsupported by the checked primary artifacts. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://arxiv.org/abs/2511.21631, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md
- Primary sources do not document safety certifications or validated usage for clinical, PHI, or other regulated high-stakes domains; absence of upstream safety validation means the checkpoint should not be considered clinically safe without external validation. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://arxiv.org/abs/2511.21631
- Ambiguity/conflict found in cited technical-report identifier: the Hugging Face model-card metadata references a Qwen3 technical-report identifier (2505.09388 as reported on the model-card facts), while an arXiv entry inspected is 2511.21631. Both locations were checked and this identifier mismatch is unresolved by the inspected primary artifacts. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://arxiv.org/abs/2511.21631

### Safety

- Evidence gap: the primary model card, repository README, config.json, and arXiv listing do not provide documented safety controls, PHI handling procedures, or domain-specific validation guidance for medical/clinical/legal use; treat as unvalidated for safety-critical applications until explicit upstream evidence is published. Sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct, https://github.com/QwenLM/Qwen3-VL/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json, https://arxiv.org/abs/2511.21631
- Model/code license: the license for the checkpoint is reported as Apache-2.0 in the inspected source summary (featherless.ai fact); primary repository files checked do not include an explicit LICENSE file in the inspected facts, so further upstream license verification in the canonical repository or model card is advisable. Sources: https://featherless.ai/models/Qwen/Qwen3-VL-4B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: Qwen3-VL-4B-Instruct

- URL: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct
- Publisher: Qwen / Hugging Face model hub
- Type: `model-card`
- Primary because: Official Hugging Face model card for the named checkpoint; contains capability statements, generation hyperparameters, and links cited by other artifacts in the findings.
- Scope: Qwen3-VL-4B-Instruct
- Supports: multimodal (image+text) inputs and text outputs
- Supports: capability claims (OCR expansion, multimodal reasoning, visual perception)
- Supports: generation hyperparameters and out_seq_length values
- Supports: reference to technical-report identifier (as presented on the model card)

### Checkpoint config.json (Hugging Face repository blob)

- URL: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json
- Publisher: Qwen / Hugging Face repository
- Type: `repository`
- Primary because: Canonical checkpoint configuration file listing model_type, architecture name, tokenizer/vocabulary size, vision configuration keys (patch_size, spatial_merge_size, etc.), and vision token id keys.
- Scope: Qwen3-VL-4B-Instruct (config.json)
- Supports: architecture = Qwen3VLForConditionalGeneration (config key)
- Supports: model_type = qwen3_vl (config key)
- Supports: vocabulary_size = 151936 (config key)
- Supports: vision patch_size = 16; spatial_merge_size = 2; temporal_patch_size = 2 (vision config keys)
- Supports: vision_start_token_id = 151652; vision_end_token_id = 151653; image token id listed as 151655 (config keys)

### Tokenizer configuration (refs/pr/22) for Qwen3-VL-4B-Instruct

- URL: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/refs%2Fpr%2F22/tokenizer_config.json
- Publisher: Qwen / Hugging Face repository
- Type: `repository`
- Primary because: Tokenizer configuration file enumerating tokenizer class, model_max_length, and additional special tokens used by the checkpoint.
- Scope: Qwen3-VL-4B-Instruct (tokenizer_config.json)
- Supports: tokenizer class = Qwen2Tokenizer (tokenizer_config key)
- Supports: model_max_length = 262144 (tokenizer_config key)
- Supports: special tokens include '<|im_start|>' and '<|im_end|>' (tokenizer_config key)

### Qwen3-VL repository README

- URL: https://github.com/QwenLM/Qwen3-VL/blob/main/README.md
- Publisher: QwenLM / GitHub
- Type: `repository`
- Primary because: Official repository README describing the Qwen3-VL family and summarizing capability upgrades and intended usage contexts.
- Scope: Qwen3-VL family / Qwen3-VL-4B-Instruct (repository README)
- Supports: descriptions of enhanced visual perception, extended context length, and agent interaction capabilities
- Supports: statements about the Qwen3-VL family design and intended multimodal usage

### ArXiv listing for the Qwen3-VL technical report (checked arXiv record)

- URL: https://arxiv.org/abs/2511.21631
- Publisher: arXiv
- Type: `paper`
- Primary because: ArXiv listing identified in the findings as a technical report relevant to Qwen3-VL; inspected as a primary technical-report artifact.
- Scope: Qwen3-VL technical report (arXiv)
- Supports: presence of an arXiv technical report entry related to Qwen3-VL (identifier 2511.21631 as found in the inspected sources)

### Featherless.ai model summary for Qwen3-VL-4B-Instruct (inspected in findings)

- URL: https://featherless.ai/models/Qwen/Qwen3-VL-4B-Instruct
- Publisher: Featherless.ai
- Type: `official-documentation`
- Primary because: Included in the provided findings and used to verify parameter-scale and license assertions present in the findings set.
- Scope: Qwen3-VL-4B-Instruct (external summary)
- Supports: parameter scale = 4B (fact in findings)
- Supports: license = Apache-2.0 (fact in findings)
- Supports: summary capability claims listed in the findings

## Evidence gaps

- Evidence gap: No checkpoint-specific numeric benchmark tables or per-dataset evaluation results for Qwen3-VL-4B-Instruct were found in the inspected primary sources. Checked locations: Hugging Face model card (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct), repository README (https://github.com/QwenLM/Qwen3-VL/blob/main/README.md), and arXiv listing (https://arxiv.org/abs/2511.21631).
- Evidence gap: Primary sources do not specify accepted image transport formats (URL, Base64, local file) or upload/size limits for this checkpoint. Checked locations: Hugging Face model card, repository README, and config/tokenizer files (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; https://github.com/QwenLM/Qwen3-VL/blob/main/README.md; https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json).
- Evidence gap: No canonical prompt templates, pair-input ordering rules, or exact multimodal formatting examples for this specific checkpoint were found in the inspected primary sources. Checked locations: Hugging Face model card and repository README (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; https://github.com/QwenLM/Qwen3-VL/blob/main/README.md).
- Evidence gap: Primary sources do not publish recommended post-inference calibration, confidence semantics, or validation protocols for outputs produced by Qwen3-VL-4B-Instruct. Checked locations: Hugging Face model card, tokenizer/config files, repository README, and arXiv listing (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json; https://github.com/QwenLM/Qwen3-VL/blob/main/README.md; https://arxiv.org/abs/2511.21631).
- Evidence gap: Conflicting technical-report identifiers were observed between inspected sources: the model card references an identifier listed in the findings as 2505.09388, while an arXiv entry inspected is 2511.21631. Both locations were checked (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; https://arxiv.org/abs/2511.21631) and the mismatch is unresolved by the inspected artifacts.
- Evidence gap: Primary sources do not provide explicit input validation bounds such as required image pixel dimensions, max image token counts, or file-type restrictions for this checkpoint. Checked locations: model card and repository config/tokenizer files (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json; https://github.com/QwenLM/Qwen3-VL/blob/main/README.md).
- Evidence gap: No primary-source, protocol-matched peer-model benchmark comparisons for this exact checkpoint were found. Checked locations: model card, repository README, and arXiv listing (https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; https://github.com/QwenLM/Qwen3-VL/blob/main/README.md; https://arxiv.org/abs/2511.21631).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 52 deterministic draft defect(s) were supplied to the audit.

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
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2505.09388 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/QwenLM/Qwen3-VL/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Fara-7B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/FenomAI/Qwen3-VL-4B-Instruct-AWQ-4bit/blob/f2c4bf0b94ccce2d0cf29c0611e8ddd9a7cba772/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.voxel51.com/model_zoo/models/Qwen_Qwen3_VL_4B_Instruct.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/QwenLM/Qwen3-VL/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2505.09388 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/QwenLM/Qwen3-VL/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://alphaxiv.org/abs/2511.21631 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://aiskyeye.com/wp-content/uploads/2026/05/0402%E7%BB%84%E4%BC%9Aqwen3-vl.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.voxel51.com/model_zoo/models/Qwen_Qwen3_VL_4B_Instruct.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2505.09388 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://alibabacloud.com/help/en/model-studio/vision Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://qwen.readthedocs.io/en/latest/getting_started/concepts.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/b2d05efe1092b10bbdbb2f7447c40a6f7435dda6/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] cites a different cloud provider's hosted API without stating in the same claim that its contract does not establish the NVIDIA NIM or Forge contract: $.inputPreparation.semanticInputs[1] cites a different cloud provider's hosted API without stating in the same claim that its contract does not establish the NVIDIA NIM or Forge contract Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
