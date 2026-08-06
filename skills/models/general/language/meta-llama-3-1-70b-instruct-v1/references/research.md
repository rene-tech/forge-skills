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

- Research key: `build-nvidia-com-meta-llama-3-1-70b-instruct-1a2c4f9e26`
- Independent audit: `revised`
- Researched: `2026-07-23T22:37:19.836371+00:00`

Primary evidence from the Meta Llama 3.1 model card (repository model card) and NVIDIA NGC/NIM documentation shows that an instruction‑tuned Llama 3.1 family exists at 8B/70B/405B scales and that the instruction‑tuned variants (including the 70B Instruct checkpoint named meta/llama-3_1-70b-instruct) are optimized for multilingual dialogue and instruction‑following. Meta documents model properties such as 70B parameters, 128k context, GQA, SFT and RLHF tuning, a December 2023 knowledge cutoff, and that the tuned models are text-in/text-out generative models (source: Meta model card). NVIDIA NGC pages and the NIM support matrix demonstrate NVIDIA packages the named 70B Instruct checkpoint in NGC/NIM containers and document deployment guidance, licensing references (NVIDIA Open Model Agreement and the Llama 3.1 Community License Agreement), required GPU capabilities, and recommended system‑level safety guardrails. The provided primary findings did not contain a canonical numeric benchmark table locator for the 70B Instruct checkpoint (the research findings available here do not include the explicit numeric rows in the Meta model card at the specified locator), so numeric upstream-checkpoint benchmark rows could not be independently verified from the provided primary model-card locator; those benchmark rows are recorded as evidence gaps below.

## Identity

- Upstream name: Meta Llama 3.1 70B Instruct
- Checkpoint/version: meta/llama-3_1-70b-instruct
- Immutable revision: not reported
- Parameter scale: 70B
- Architecture/head: Auto-regressive Transformer
- License: Llama 3.1 Community License Agreement
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8, https://docs.nvidia.com/nim/large-language-models/1.3.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/meta-llama-3_1-70b

## Selection

### Recommended

- **Multilingual chatbots and virtual assistants** — Meta's Llama 3.1 model card describes the instruction‑tuned Llama 3.1 models (including the 70B size) as optimized for multilingual dialogue and instruction‑following; NVIDIA NGC packaging documents the 70B Instruct checkpoint as a text-in/text-out generative model suitable for dialogue workloads.
  Scope: meta/llama-3_1-70b-instruct
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8
- **Complex question answering, summarization, and multilingual content generation** — Meta documents the tuned Llama 3.1 instruction variants as optimized for reasoning and instruction‑following across multilingual tasks; NVIDIA packaging describes the model as a text-in/text-out generative checkpoint packaged for deployment.
  Scope: meta/llama-3_1-70b-instruct
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8

### Conditional

- **Large-scale enterprise deployment or redistribution of derivatives** — Subject to the Llama 3.1 Community License Agreement and NVIDIA Open Model Agreement as documented on the NVIDIA NGC container pages; operators must verify license compliance for intended geography and downstream derivative agreements before redistribution.
  Scope: meta/llama-3_1-70b-instruct (packaged in NGC/NIM containers)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8, https://docs.api.nvidia.com/nim/reference/meta-llama-3_1-70b

### Avoid

- **Deploying the model for prohibited or high-risk categories (e.g., weapons, illegal activity, processing sensitive personal data without consent)** — The NVIDIA NIM reference/support documentation for the Llama 3.1 listing specifies prohibited use categories and states that system safeguards and developer responsibility for guardrails are required.
  Scope: meta/llama-3_1-70b-instruct
  Evidence: https://docs.api.nvidia.com/nim/reference/meta-llama-3_1-70b, https://docs.nvidia.com/nim/large-language-models/1.3.0/support-matrix.html

## Input preparation

### Semantic inputs

- Multilingual text input (text-in) is the accepted input modality for the instruction‑tuned Llama 3.1 models including the 70B Instruct checkpoint. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md

### Accepted formats

- The instruction‑tuned Llama 3.1 checked variants are described as text-in/text-out generative models. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8

### Preprocessing

- Evidence gap: Exact preprocessing, normalization, tokenizer type, and tokenizer vocabulary/version for the meta/llama-3_1-70b-instruct checkpoint are not specified in the provided primary findings.

### Pre-submit validation

- Evidence gap: Explicit upstream input-validation rules (bounds, forbidden content filtering at input time) for the 70B Instruct checkpoint are not documented in the provided primary findings.

### Task-specific formatting

- Evidence gap: Canonical per-benchmark prompt templates, paired-input ordering, or official task-formatting templates for benchmarks or downstream tasks are not present in the provided primary findings for the 70B Instruct checkpoint.

## Output interpretation

### Outputs

- The instruction‑tuned Llama 3.1 models (including 70B Instruct) produce text outputs (text-out); no canonical structured output schema or token-level termination contract is specified in the provided primary findings. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8

### Interpretation

- Evidence gap: Calibration guidance, score semantics, or recommended confidence-interpretation procedures for the model outputs are not available in the provided primary findings for the 70B Instruct checkpoint.

### Post-inference validation

- Evidence gap: Post-inference validation checks (sanity checks, automated quality gating, pooling/normalization procedures) are not specified in the available primary findings for the 70B Instruct checkpoint.

## Public benchmarks

### Knowledge and reasoning

- Dataset/split: MMLU / test
- Metric/value: accuracy / 83.6 (`higher-is-better`)
- Model scope: Llama 3.1 70B Instruct
- Conditions: 5-shot evaluation.
- Source: https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md
- Locator: Instruction tuned models benchmark table
- Caveat: Use only for the 70B Instruct checkpoint and reported protocol.

### Code generation

- Dataset/split: HumanEval / test
- Metric/value: pass@1 / 80.5 (`higher-is-better`)
- Model scope: Llama 3.1 70B Instruct
- Conditions: Protocol reported in the Meta model card.
- Source: https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md
- Locator: Instruction tuned models benchmark table
- Caveat: Upstream-checkpoint result; not a Forge runtime benchmark.

### Mathematical reasoning

- Dataset/split: GSM8K / test
- Metric/value: accuracy / 95.1 (`higher-is-better`)
- Model scope: Llama 3.1 70B Instruct
- Conditions: 8-shot chain-of-thought evaluation.
- Source: https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md
- Locator: Instruction tuned models benchmark table
- Caveat: Prompting and scoring must match before comparison.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: General instruction-following / dialogue
- Criteria: No directly comparable peer primary benchmark evidence and aligned protocol was provided in the available findings to support apples-to-apples comparison for this task; protocol alignment and primary benchmark locators for peers are missing.
- Rationale: The available primary findings document properties of the Llama 3.1 70B Instruct checkpoint and NVIDIA packaging but do not include peer primary benchmark tables or canonical scoring/prompt code required to make validated task- and protocol-specific comparisons.
- Comparison conditions: Comparison requires peer primary benchmark artifacts and matching prompt/scoring scripts; these are not present in the provided primary findings.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8

## Limitations and safety

### Limitations

- Evidence gap: Exact tokenizer specification (tokenizer type, vocabulary, tokenizer version) and immutable checkpoint revision/commit SHA for the meta/llama-3_1-70b-instruct checkpoint are not present in the provided primary findings.
- Operational limitation: NVIDIA NIM support documentation cites required GPU compute capability and memory constraints for deploying Llama 3.1 70B Instruct and should be followed for deployment. Sources: https://docs.nvidia.com/nim/large-language-models/1.3.0/support-matrix.html

### Safety

- The NVIDIA NIM reference for the Llama 3.1 listing documents prohibited use categories, recommends system safeguards, and states developers/operators are responsible for additional safety guardrails and safety testing; operators should apply deployment-specific safety reviews and content-moderation tooling. Sources: https://docs.api.nvidia.com/nim/reference/meta-llama-3_1-70b, https://docs.nvidia.com/nim/large-language-models/1.3.0/support-matrix.html
- Evidence gap: Upstream-per-benchmark safety mitigations, per-sample privacy-handling procedures, or canonical human-review thresholds for the 70B Instruct checkpoint are not provided in the available primary findings.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Llama 3.1 model card (Meta repository)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md
- Publisher: Meta
- Type: `model-card`
- Primary because: Canonical upstream model card and repository for Llama 3.1 that documents model-scale properties and tuned-model descriptions.
- Scope: meta/llama-3_1-70b-instruct
- Supports: model-description
- Supports: scale
- Supports: context-window
- Supports: tuning-methods

### NVIDIA NIM LLM support matrix (1.3.0)

- URL: https://docs.nvidia.com/nim/large-language-models/1.3.0/support-matrix.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: NVIDIA NIM support matrix documents supported Llama 3.1 releases, hardware/precision recommendations, and deployment constraints for NIM-packaged checkpoints.
- Scope: meta/llama-3_1-70b-instruct (deployment/compatibility)
- Supports: deployment-requirements
- Supports: hardware-compatibility
- Supports: precision-guidance

### NGC container: llama-3.1-70b-instruct (1.8)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8
- Publisher: NVIDIA NGC
- Type: `repository`
- Primary because: NGC container page documents the NIM/NGC packaging for the Llama 3.1 70B Instruct checkpoint and associated container-level licensing and distribution notes.
- Scope: llama-3.1-70b-instruct (NGC container 1.8)
- Supports: container-distribution
- Supports: licensing
- Supports: model-description

### NGC container layers: llama-3.1-70b-instruct (2.0.4 layers)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/2.0.4/layers
- Publisher: NVIDIA NGC
- Type: `repository`
- Primary because: NGC layers metadata page exposing container layering and signing metadata for a packaged release of the named checkpoint.
- Scope: llama-3.1-70b-instruct (NGC container 2.0.4 layers)
- Supports: container-metadata
- Supports: signing-and-distribution

### NGC container tags: llama-3.1-70b-instruct (1.13.1 tags)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.13.1/tags
- Publisher: NVIDIA NGC
- Type: `repository`
- Primary because: NGC tags/manifest page documenting available container tags and compressed image metadata for packaged releases of the checkpoint.
- Scope: llama-3.1-70b-instruct (NGC container 1.13.1 tags)
- Supports: container-distribution
- Supports: image-metadata

### NVIDIA NIM reference: meta-llama-3_1-70b

- URL: https://docs.api.nvidia.com/nim/reference/meta-llama-3_1-70b
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: NIM reference documentation for the Llama 3.1 70B Instruct listing that documents safety guidance, prohibited categories, and developer responsibilities for deployments.
- Scope: meta/llama-3_1-70b-instruct (NIM reference)
- Supports: safety-guidance
- Supports: prohibited-uses
- Supports: deployment-guidance

### Llama 3.1 model card

- URL: https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md
- Publisher: Meta
- Type: `model-card`
- Primary because: A human reviewer opened this primary source and verified the structured benchmark rows and exact locator recorded in research/manual-review-hints.json.
- Scope: meta-llama-3.1-70b-instruct
- Supports: Manually verified exact-checkpoint benchmark evidence

## Evidence gaps

- Evidence gap: The provided primary Meta model-card locator in the available findings does not include explicit numeric benchmark table rows for the meta/llama-3_1-70b-instruct checkpoint at the specified Instruction tuned models benchmark table locator; therefore the numeric upstream-checkpoint benchmark values (MMLU, MMLU-Pro, HumanEval, GSM8K, MATH) could not be independently verified from the provided primary model-card locator in the available findings.
- Evidence gap: Canonical per-benchmark prompt templates, per-benchmark scoring scripts, and exact evaluation protocol code for the 70B Instruct checkpoint are not present in the provided primary findings.
- Evidence gap: Exact tokenizer specification (tokenizer type, vocabulary, tokenizer version) for the meta/llama-3_1-70b-instruct checkpoint is not present in the provided primary findings.
- Evidence gap: Immutable upstream checkpoint revision or commit SHA for the meta/llama-3_1-70b-instruct checkpoint is not reported in the provided primary findings.
- Evidence gap: Post-inference validation procedures, recommended calibration, and canonical confidence-interpretation procedures for outputs of the 70B Instruct checkpoint are not provided in the available primary findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 33 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0]: $.limitations[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1]: $.limitations[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0]: $.safety[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.1.1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/2.0.6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/2.0.8 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-70b-instruct/1.8.3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].split must say 'not reported' or name the split: $.benchmarks[3].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].split must say 'not reported' or name the split: $.benchmarks[4].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0] without evidence must be labeled as a Forge policy or evidence gap: $.safety[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md#Instruction tuned models benchmark table:accuracy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md#Instruction tuned models benchmark table:pass@1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md#Instruction tuned models benchmark table:accuracy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
