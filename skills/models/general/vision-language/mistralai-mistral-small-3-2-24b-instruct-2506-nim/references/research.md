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

- Research key: `docs-nvidia-com-nim-vision-language-models-1-3-1-examples-mistral-small-3-2-api-html-97f486063a`
- Independent audit: `revised`
- Researched: `2026-07-23T22:23:47.345161+00:00`

Primary sources inspected (HuggingFace model card, NVIDIA NGC container entry, NVIDIA NIM API docs and release notes) identify the upstream checkpoint as Mistral-Small-3.2-24B-Instruct-2506 (24B parameters, Apache-2.0 referenced) and the NVIDIA NGC container mistral-small-3.2-24b-instruct-2506 as packaging that checkpoint; primary sources do not publish numeric benchmark tables for this exact checkpoint, and tokenization/preprocessing/tokenizer-vocabulary details are not present in the inspected primary files (generation_config.json present with generation defaults). NVIDIA NIM release notes and the NGC container document multimodal/image inputs, instruction-following improvements, a very large context length, guidance about guardrails, and explicit notes that structured generation is not supported for this model in the NIM release notes; function-calling is documented in NIM API pages as a serving/runtime capability. Where upstream preprocessing, tokenizer config, canonical prompt templates, or numeric benchmark tables are absent in these primary sources, explicit evidence gaps are recorded.

## Identity

- Upstream name: Mistral Small 3.2
- Checkpoint/version: Mistral-Small-3.2-24B-Instruct-2506
- Immutable revision: not reported
- Parameter scale: 24B
- Architecture/head: not reported
- License: Apache-2.0
- Evidence: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html

## Selection

### Recommended

- **Multimodal instruction-following (text+image) with post-processing and user-provided guardrails** — NGC container entry and NVIDIA NIM release notes document multimodal/image support and instruction-following improvements for Mistral-Small-3.2-24B-Instruct-2506; HuggingFace model card describes the checkpoint as an instruct-tuned variant with instruction-following improvements.
  Scope: mistral-small-3.2-24b-instruct-2506 (upstream checkpoint) and the NGC NIM container mistral-small-3.2-24b-instruct-2506 (serving/runtime)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html

### Conditional

- **Structured outputs via function/tool-calling when routed through the NVIDIA NIM function-calling wrapper and with post-processing** — NVIDIA NIM function-calling serving/runtime support must be used and engineers must implement post-processing; upstream checkpoint does not publish native structured-generation outputs and NVIDIA release notes state structured generation is not supported for this model unless handled by wrapper/tooling.
  Scope: serving/runtime dependency: NIM function-calling wrapper (docs.nvidia.com NIM function-calling page) + upstream checkpoint mistral-small-3.2-24b-instruct-2506
  Evidence: https://docs.nvidia.com/nim/vision-language-models/1.3.1/function-calling.html, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506

### Avoid

- **Relying on native structured-generation outputs from the upstream checkpoint without wrapper/tooling** — NVIDIA NIM release notes explicitly state that structured generation is not supported for Mistral Small 3.2 24B Instruct 2506 in the NIM release-notes entry for this model.
  Scope: mistral-small-3.2-24b-instruct-2506 (upstream) and NIM serving/runtime
  Evidence: https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html
- **Accuracy-critical text-only inference when using FP8 profiles on Hopper GPUs** — NVIDIA NIM release notes note that accuracy of text-only requests may be lower on FP8 profiles on Hopper GPUs for this model.
  Scope: mistral-small-3.2-24b-instruct-2506 (serving/runtime conditions)
  Evidence: https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html

## Input preparation

### Semantic inputs

- Text input (instruction and user prompt) is accepted by the upstream instruct-tuned checkpoint and by the NGC-packaged container. Sources: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html
- Image inputs (multimodal requests) are supported by the NGC container and are documented in NVIDIA NIM release notes as supported with up to 5 images per request; upstream model card references multimodal/vision capabilities depending on model config. Sources: https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506

### Accepted formats

- Text input (string/JSON prompt payloads) is an accepted format for requests to the checkpoint/container. Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506
- Image input (image files/URLs embedded in request) is accepted by the NGC container and documented in NIM release notes (up to 5 images per request). Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-

### Preprocessing

- generation_config.json in the upstream HuggingFace model repository records generation defaults (bos_token_id, eos_token_id, transformers_version, default temperature, do_sample) that affect decoding behavior. Sources: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506
- Evidence gap: The inspected primary sources do not publish a canonical upstream tokenizer pipeline, tokenizer vocabulary size, or explicit tokenization normalization rules for this exact checkpoint (no explicit tokenizer/config.json entry located in the inspected model-card landing or generation_config.json). Sources: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json

### Pre-submit validation

- NVIDIA NGC container documentation and release notes require implementers to provide guardrails and safe integration; users must validate inputs and outputs in deployment (serving/runtime responsibility). Sources: https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html
- Evidence gap: No explicit upstream input-validation rules (e.g., bounds checks, forbidden-content filters) are published for the checkpoint on the inspected HuggingFace model card or generation_config.json. Sources: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json

### Task-specific formatting

- NVIDIA NIM documents function-calling usage and example request/response patterns in the serving/runtime docs; function-calling is a serving/runtime feature that can be used to structure prompts and post-process outputs. Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/function-calling.html, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html
- Evidence gap: Canonical upstream prompt templates or task-formatting guidance for this exact checkpoint are not published on the HuggingFace model card landing page inspected. Sources: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506

## Output interpretation

### Outputs

- Upstream checkpoint and NGC container produce text-generation outputs; structured outputs are not provided natively by the upstream checkpoint (structured generation is noted as unsupported in NIM release notes), while the NIM wrapper documents function-calling as a serving/runtime mechanism to produce structured-like outputs when integrated. Sources: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html, https://docs.nvidia.com/nim/vision-language-models/1.3.1/function-calling.html

### Interpretation

- Treat outputs as plain text sequences generated by the upstream checkpoint; do not assume native reliable structured JSON outputs unless the NIM function-calling wrapper or external post-processing is used (structured generation is documented as unsupported in the NIM release-notes). Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html, https://docs.nvidia.com/nim/vision-language-models/1.3.1/function-calling.html, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506

### Post-inference validation

- Post-inference validation and guardrails are required at deployment time per the NGC container and NIM release notes; users must validate and sanitize outputs before downstream use. Sources: https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Evidence gap: Primary sources inspected (NVIDIA NIM API page, NVIDIA NGC container entry, HuggingFace model card, HuggingFace generation_config.json, and NVIDIA NIM release-notes) do not publish numeric benchmark tables or labeled evaluation sections for this exact checkpoint; no canonical numeric benchmark table was found at these URLs/paths. Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html, https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html

### Safety

- NVIDIA NGC container documentation and release notes require implementers to provide guardrails and ensure safe integration; users are responsible for deploying appropriate content filters and validation. Sources: https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Mistral-Small-3.2-24B-Instruct-2506

- URL: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506
- Publisher: Mistral AI / HuggingFace
- Type: `model-card`
- Primary because: Official HuggingFace model card for the exact upstream checkpoint Mistral-Small-3.2-24B-Instruct-2506; contains the model landing page and links to model files (generation_config.json).
- Scope: mistral-small-3.2-24b-instruct-2506
- Supports: Identifies the checkpoint string 'Mistral-Small-3.2-24B-Instruct-2506' on the model-card landing page
- Supports: Provides generation_config.json with generation defaults (bos_token_id, eos_token_id, transformers_version, default temperature, do_sample)

### generation_config.json (model artifact blob)

- URL: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json
- Publisher: Mistral AI / HuggingFace
- Type: `repository`
- Primary because: Primary model artifact containing generation defaults for the exact checkpoint; used to verify decoding defaults.
- Scope: mistral-small-3.2-24b-instruct-2506
- Supports: Shows bos_token_id, eos_token_id, transformers_version, default temperature, and do_sample values that affect decoding behavior

### Mistral Small 3.2 API - NVIDIA NIM

- URL: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM API documentation page for the Mistral Small 3.2 examples and API usage; confirms NIM support and provides example Docker/run commands.
- Scope: mistral-small-3.2-24b-instruct-2506 (NIM API examples and usage)
- Supports: References the model card for the Mistral Small 3.2 24B Instruct model and provides example Docker/launch commands for the NIM container

### Mistral Small 3.2 - Function Calling (NIM docs)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.3.1/function-calling.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM documentation describing function-calling features in the NIM wrapper; evidences serving/runtime structured-output tooling.
- Scope: serving/runtime (NIM function-calling)
- Supports: Documents the NIM function-calling serving/runtime capability and example patterns for integrating tool/function calls with model prompts

### Mistral Small 3.2 24B Instruct-2506 - NVIDIA NGC Container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NGC catalog/container entry for the exact NIM container image packaging Mistral-Small-3.2-24B-Instruct-2506; provides identity, license references, release date, and deployment notes including guardrails.
- Scope: mistral-small-3.2-24b-instruct-2506 (NGC container)
- Supports: Identifies the container and associates it with the checkpoint Mistral-Small-3.2-24B-Instruct-2506
- Supports: Documents release metadata, licensing references (including Apache-2.0), multimodal/vision capabilities, and ethical/guardrail recommendations

### NVIDIA NIM Release Notes (vision-language-models 1.3.1)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM release notes for the 1.3.1 vision-language models bundle; contains model-specific runtime notes for Mistral Small 3.2 24B Instruct 2506 (context length, images per request, structured-generation support, FP8 caveat).
- Scope: mistral-small-3.2-24b-instruct-2506 (NIM release notes)
- Supports: States structured generation is not supported for Mistral Small 3.2 24B Instruct 2506 in NIM release notes
- Supports: Documents default maximum sequence length (131,000 tokens) and that each request supports up to 5 images
- Supports: Notes accuracy caveat for FP8 profiles on Hopper GPUs

## Evidence gaps

- Evidence gap: No numeric benchmark tables or labeled evaluation sections were found for Mistral-Small-3.2-24B-Instruct-2506 on the inspected primary sources. URLs and exact inspected paths: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506 (model-card landing — checked for 'Benchmarks'/'Evaluation' headings), https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json (artifact blob — generation defaults only), https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/- (NGC container main page — checked for benchmark/evaluation tables), https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html (API example page — checked main page for evaluation/benchmarks), https://docs.nvidia.com/nim/vision-language-models/1.3.1/release-notes.html (release notes — checked model-specific notes).
- Evidence gap: No canonical upstream tokenizer configuration, tokenizer vocabulary size, or detailed tokenization/normalization pipeline was found in the inspected primary sources for this exact checkpoint. Exact inspected paths: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506 (model-card landing) and https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506/blob/main/generation_config.json (generation defaults blob).
- Evidence gap: No canonical prompt templates or upstream task-formatting guidance for Mistral-Small-3.2-24B-Instruct-2506 were found on the inspected HuggingFace model-card landing or the NGC/ NIM API example pages. Exact inspected paths: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506, https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/-, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html
- Evidence gap: Benchmarks/comparisons gap: No primary-source task-level comparisons or protocol-matched numeric comparisons for this exact checkpoint were located on the inspected primary sources. Inspected paths: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506 (model-card landing), https://catalog.ngc.nvidia.com/orgs/nim/mistralai/containers/mistral-small-3.2-24b-instruct-2506/- (NGC container page), https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html (NIM API page).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 26 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1]: $.inputPreparation.acceptedFormats[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1]: $.inputPreparation.preprocessing[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1]: $.inputPreparation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.conditionalUseCasesEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.avoidUseCasesEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisonsEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
