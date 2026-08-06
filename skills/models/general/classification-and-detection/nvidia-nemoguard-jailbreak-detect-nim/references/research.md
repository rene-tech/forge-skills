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

- Research key: `build-nvidia-com-nvidia-nemoguard-jailbreak-detect-modelcard-3dbc6e85cc`
- Independent audit: `revised`
- Researched: `2026-07-23T21:46:15.945061+00:00`

NemoGuard JailbreakDetect (checkpoint NemoGuard-JailbreakDetect-v1.0) is a Random Forest classifier published by NVIDIA to detect jailbreak and prompt-injection attempts against LLMs. Primary sources indicate the model was trained to operate on embeddings produced by snowflake-arctic-embed-m-long and was evaluated on the JailbreakHub dataset (Hugging Face model card reports a stratified 20% test subset and lists F1=0.9601, FPR=0.0042, FNR=0.0435). The artifact is available as an NVIDIA container that includes both the classifier and the embedding model. Primary sources disagree on the exact model-weight license string (Hugging Face vs NVIDIA docs); container/runtime code uses NVIDIA-specific container/product licensing per NVIDIA documentation. Primary sources do not provide additional details on calibration semantics, score range, endpoint payload field names, or adversarial/privacy evaluations; those items are recorded as evidence gaps below.

## Identity

- Upstream name: NemoGuard JailbreakDetect
- Checkpoint/version: NemoGuard-JailbreakDetect-v1.0
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Random Forest
- License: Conflicting primary-source entries: Hugging Face lists the model license as 'NVIDIA Open Model License'; NVIDIA documentation lists the model artifact license as 'NVIDIA Community Model License Agreement' and the container artifact license as the 'NVIDIA Software License Agreement'.
- Evidence: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect, https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard

## Selection

### Recommended

- **Detecting jailbreak or prompt-injection attempts in large language model deployments as a guardrail classifier.** — Primary documentation and the published model card describe the model's purpose as a safety classifier to identify jailbreak and prompt-injection activities.
  Scope: NemoGuard-JailbreakDetect-v1.0 (NVIDIA container: nemoguard-jailbreak-detect)
  Evidence: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect
- **Integration into NVIDIA NeMo Guardrails orchestration to gate or block unsafe prompts prior to sending them to an LLM.** — NVIDIA integration documentation and NeMo Guardrails guidance show NemoGuard JailbreakDetect is supported for use within the Guardrails microservice architecture.
  Scope: NemoGuard-JailbreakDetect-v1.0 (NVIDIA Guardrails integration examples)
  Evidence: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/integrate-guardrails.html, https://developer.nvidia.com/nemo-guardrails

### Conditional

- **Use in production environments where false positives/negatives must be tightly controlled (requires downstream validation and calibration).** — Requires downstream validation, threshold calibration, and monitoring; primary sources note evaluation on a stratified 20% subset of JailbreakHub but do not provide calibration or deployment threshold guidance.
  Scope: NemoGuard-JailbreakDetect-v1.0 (evaluation reported on model repository)
  Evidence: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- **Deploying as part of multi-component guardrail stacks that include embedding generation and orchestration.** — Requires ensuring input embeddings are produced by the documented embedding model (snowflake-arctic-embed-m-long) or otherwise validated; primary sources state the container includes both classifier and embedding model but do not certify performance with other embedding sources.
  Scope: NemoGuard-JailbreakDetect-v1.0 (container includes both classifier and embedding model)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html

### Avoid

- **Using the model to make final security or safety-critical decisions without human oversight.** — Primary sources describe the model as a guardrail/safety classifier; they do not claim it is a sole decision-maker for final security decisions.
  Scope: NemoGuard-JailbreakDetect-v1.0
  Evidence: https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html
- **Applying the model to input formats or embedding sources other than the documented snowflake-arctic-embed-m-long without validation.** — Primary sources indicate the classifier uses embeddings produced by snowflake-arctic-embed-m-long and the NGC container bundles the embedding model; primary sources do not certify performance on other embedding sources.
  Scope: NemoGuard-JailbreakDetect-v1.0 (expects embeddings from snowflake-arctic-embed-m-long per primary documentation)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect

## Input preparation

### Semantic inputs

- Input is a text embedding represented as a 768-dimensional vector. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect
- Evidence gap: primary sources state the classifier expects embeddings from snowflake-arctic-embed-m-long (and the container includes that embedding model), but do not provide exhaustive guarantees about other embedding sources or precise preprocessing beyond embedding generation. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html

### Accepted formats

- Accepted format: embedding vector (768 floating-point values) as the model input. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect

### Preprocessing

- Input embeddings are produced by the snowflake-arctic-embed-m-long embedding model (the NVIDIA container bundles the embedding model alongside the classifier). Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html
- Evidence gap: primary sources do not specify additional normalization, tokenization, or numeric ranges beyond supplying the 768-dimensional embedding; exact preprocessing steps before embedding generation are not documented in the primary sources. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect

### Pre-submit validation

- Input vector must be of length 768 (primary sources state input is a 768-dimensional embedding). Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect
- Evidence gap: primary sources do not provide explicit numeric bounds, NaN/Inf handling rules, or additional automated validation checks for embedding values; implementers should validate numerics and vector length before submission. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect

### Task-specific formatting

- Evidence gap: primary sources describe the model as a microservice/classifier that consumes embeddings but do not provide an exact named JSON endpoint path or canonical payload field names in the provided facts; exact API payload schema is not present in the research facts. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/integrate-guardrails.html

## Output interpretation

### Outputs

- Output includes a classification (boolean) and an associated probability/score (floating-point) represented as a one-dimensional value per the model card and API reference. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect

### Interpretation

- The classifier indicates whether an input embedding corresponds to a jailbreak/prompt-injection attempt (primary sources describe the microservice/classifier as classifying jailbreak attempts). Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Evidence gap: primary sources do not supply formal score calibration semantics (exact probability meaning, numeric range, or threshold recommendations) in the provided facts. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect

### Post-inference validation

- Use the reported evaluation metrics (F1, false positive rate, false negative rate) as anchors for threshold selection and monitor operational false positive/negative rates; primary sources provide evaluation metrics but not deployment thresholds. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Implement downstream review and human-in-the-loop processes for flagged inputs; primary sources describe the model as a guardrail classifier and integration examples reference use within NeMo Guardrails. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/integrate-guardrails.html, https://developer.nvidia.com/nemo-guardrails

## Public benchmarks

### Jailbreak and prompt-injection detection

- Dataset/split: JailbreakHub (stratified 20% test subset) / Standard stratified 20% test subset (as reported on model repository)
- Metric/value: F1 score / 0.9601 (`higher-is-better`)
- Model scope: NemoGuard-JailbreakDetect-v1.0 (model repository evaluation)
- Conditions: Evaluation reported on a stratified 20% subset of the aggregate dataset; primary source lists evaluation conditions but does not provide full protocol details beyond the stratified split.
- Source: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Locator: Hugging Face model card > Evaluation section
- Caveat: Benchmark is reported on the Hugging Face model card (upstream model repository) — evaluation depends on embeddings produced by snowflake-arctic-embed-m-long per primary sources.
- Caveat: Primary sources do not provide full evaluation protocol details (e.g., seed, preprocessing pipeline beyond embedding generation) in the provided facts.

### Jailbreak and prompt-injection detection

- Dataset/split: JailbreakHub (stratified 20% test subset) / Standard stratified 20% test subset (as reported on model repository)
- Metric/value: False positive rate / 0.0042 (`lower-is-better`)
- Model scope: NemoGuard-JailbreakDetect-v1.0 (model repository evaluation)
- Conditions: Evaluation reported on a stratified 20% subset of the aggregate dataset; primary source lists evaluation conditions but does not provide full protocol details beyond the stratified split.
- Source: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Locator: Hugging Face model card > Evaluation section
- Caveat: Benchmark is upstream-checkpoint evidence from the Hugging Face model card and depends on embedding generation from snowflake-arctic-embed-m-long as documented in primary sources.
- Caveat: Primary sources do not provide full evaluation protocol details required for strict comparability (e.g., sampling seeds, label schemas).

### Jailbreak and prompt-injection detection

- Dataset/split: JailbreakHub (stratified 20% test subset) / Standard stratified 20% test subset (as reported on model repository)
- Metric/value: False negative rate / 0.0435 (`lower-is-better`)
- Model scope: NemoGuard-JailbreakDetect-v1.0 (model repository evaluation)
- Conditions: Evaluation reported on a stratified 20% subset of the aggregate dataset; primary source lists evaluation conditions but does not provide full protocol details beyond the stratified split.
- Source: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Locator: Hugging Face model card > Evaluation section
- Caveat: Benchmark is upstream-checkpoint evidence from the Hugging Face model card and depends on embedding generation from snowflake-arctic-embed-m-long as documented in primary sources.
- Caveat: Primary sources do not provide full evaluation protocol details required for strict comparability (e.g., sampling seeds, label schemas).

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Jailbreak detection in large language models
- Criteria: No primary-source comparisons to Forge peers are provided in the available facts; protocols, datasets, and metrics for Forge peers are not available in the provided primary facts for direct comparison.
- Rationale: Primary sources for NemoGuard JailbreakDetect document evaluation on JailbreakHub; no primary evidence was found in the provided facts that directly compares this checkpoint to other specific Forge candidates under a shared protocol.
- Comparison conditions: Insufficient primary evidence to match dataset, split, and evaluation protocol between NemoGuard and any named Forge alternative.
- Evidence: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html

## Limitations and safety

### Limitations

- Evidence gap: potential model bias and limited interpretability are not characterized in the provided primary sources; the model architecture is reported as Random Forest but documented bias/robustness analyses are not present in the facts. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Reliance on the quality of input embeddings and limited generalization claims: primary sources indicate the classifier expects embeddings produced by snowflake-arctic-embed-m-long and the NGC container bundles the embedding model; performance with other embedding sources is not certified in the provided facts. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect
- Evaluation scope limitation: primary reported evaluation is on JailbreakHub (stratified 20% test subset) per the model repository; broader real-world performance across diverse deployment scenarios is not documented in the provided facts. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Evidence gap: explicit adversarial robustness evaluations, privacy impact assessments, and dual-use risk analyses are not present in the provided primary facts. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Licensing and deployment constraints: primary NVIDIA documentation distinguishes container/runtime licensing (NVIDIA Software License Agreement and product-specific terms) from the model artifact license (per NVIDIA docs), and Hugging Face lists a model license entry that differs; implementers must consult the cited license documents for deployment restrictions. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Operational integration requirements: primary integration docs show the model is used within NeMo Guardrails and requires following container startup and configuration steps; implementers must follow integration guidance in primary docs. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/integrate-guardrails.html, https://developer.nvidia.com/nemo-guardrails
- Evidence gap: specifics on numeric input validation rules (e.g., acceptable ranges, NaN/Inf handling) and API payload field names are not present in the provided primary facts. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect, https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect
- Evidence gap: no primary-source documentation in the provided facts on clinical, healthcare, or other domain-specific safety validation; application in regulated domains requires domain-specific validation. Sources: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect

### Safety

- The model is intended to function as a guardrail classifier to detect jailbreak/prompt-injection attempts and is documented for integration within NeMo Guardrails; use within guarded orchestration and human review is supported by primary integration documentation. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/integrate-guardrails.html, https://developer.nvidia.com/nemo-guardrails
- Evidence gap: primary sources do not include detailed adversarial mitigation steps, privacy-preserving deployment patterns, or formal human-review thresholds; these areas are not characterized in the provided facts. Sources: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://huggingface.co/nvidia/NemoGuard-JailbreakDetect

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NemoGuard JailbreakDetect on NVIDIA NGC

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect
- Publisher: NVIDIA
- Type: `repository`
- Primary because: Official NVIDIA NGC catalog entry for the NemoGuard JailbreakDetect container; documents container components and bundled models (classifier + embedding model).
- Scope: nemoguard-jailbreak-detect (NGC container)
- Supports: input-spec
- Supports: model-bundle:classifier+embedding
- Supports: deployment:container-availability
- Supports: integration-guidance

### NVIDIA NemoGuard JailbreakDetect documentation (model card/index)

- URL: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA product documentation describing the NemoGuard JailbreakDetect microservice, licensing notes, and relationship to the embedding model.
- Scope: NemoGuard JailbreakDetect (NVIDIA documentation)
- Supports: model-purpose
- Supports: license:container-and-model-artifact-notes
- Supports: input-spec
- Supports: integration-references

### Hugging Face model card for NemoGuard-JailbreakDetect

- URL: https://huggingface.co/nvidia/NemoGuard-JailbreakDetect
- Publisher: NVIDIA (model repository on Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face-hosted model repository maintained by NVIDIA containing the model card, reported evaluation metrics, and input/output descriptions for the checkpoint NemoGuard-JailbreakDetect-v1.0.
- Scope: NemoGuard-JailbreakDetect-v1.0 (model repository)
- Supports: benchmark:F1:0.9601:on JailbreakHub
- Supports: benchmark:False positive rate:0.0042:on JailbreakHub
- Supports: benchmark:False negative rate:0.0435:on JailbreakHub
- Supports: input-spec:768-dim-embedding
- Supports: output-spec:bool+float

### NVIDIA model card on build.nvidia.com for NemoGuard JailbreakDetect

- URL: https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card page (sourceScope provided in the task) describing model readiness for commercial use and listing the model as supported in NeMo Guardrails.
- Scope: NemoGuard JailbreakDetect (build.nvidia.com model card)
- Supports: model-purpose
- Supports: commercial-use-notice
- Supports: integration:NeMo-Guardrails-support

### NVIDIA NIM API reference for NemoGuard JailbreakDetect

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-nemoguard-jailbreak-detect
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA API reference for the NemoGuard JailbreakDetect NIM describing input/output types and model version information as presented in the provided facts.
- Scope: NemoGuard-JailbreakDetect-v1.0 (NIM API reference)
- Supports: input-spec:768-dim-embedding
- Supports: output-spec:classification+probability
- Supports: model-version:NemoGuard-JailbreakDetect-v1.0

### Integrate NemoGuard JailbreakDetect with NeMo Guardrails (NVIDIA docs)

- URL: https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/integrate-guardrails.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official integration documentation showing example Guardrails integration steps and configuration references for using the NemoGuard JailbreakDetect microservice.
- Scope: NemoGuard JailbreakDetect (integration documentation)
- Supports: integration-guidance
- Supports: operational-setup
- Supports: usage-example

### NVIDIA NeMo Guardrails developer page

- URL: https://developer.nvidia.com/nemo-guardrails
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA developer resource describing NeMo Guardrails and its integration points including the JailbreakDetect NIM as referenced in the provided facts.
- Scope: NeMo Guardrails (developer documentation referencing JailbreakDetect integration)
- Supports: integration-guidance
- Supports: guardrails-overview

## Evidence gaps

- Evidence gap: Exact API endpoint path names, JSON payload field names, and canonical request/response examples are not present in the provided primary facts.
- Evidence gap: Formal score calibration semantics, numeric score range, and recommended operational thresholds are not specified in the provided primary facts.
- Evidence gap: Full evaluation protocol details (random seeds, preprocessing pipeline prior to embedding generation, label schema) for the reported JailbreakHub benchmarks are not included in the provided facts.
- Evidence gap: Conflicting primary-source license strings for the model artifact (Hugging Face vs NVIDIA docs) require consulting the canonical license documents for authoritative text.
- Evidence gap: No primary-source adversarial robustness, privacy impact assessment, or dual-use risk analysis is present in the provided facts.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 130 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0]: $.recommendedUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0]: $.recommendedUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1]: $.recommendedUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1]: $.recommendedUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[0]: $.conditionalUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[0]: $.conditionalUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[1]: $.conditionalUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[1]: $.conditionalUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[1]: $.avoidUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[1]: $.avoidUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1]: $.inputPreparation.preprocessing[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1]: $.inputPreparation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[1]: $.inputPreparation.taskSpecificFormatting[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1]: $.outputInterpretation.interpretation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property sourceLocator Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property sourceUrl Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1]: $.benchmarks[1]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1]: $.benchmarks[1]: missing required property sourceLocator Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1]: $.benchmarks[1]: missing required property sourceUrl Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2]: $.benchmarks[2]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2]: $.benchmarks[2]: missing required property sourceLocator Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2]: $.benchmarks[2]: missing required property sourceUrl Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0]: $.limitations[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1]: $.limitations[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2]: $.limitations[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3]: $.limitations[3]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4]: $.limitations[4]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[5]: $.limitations[5]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[6]: $.limitations[6]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[7]: $.limitations[7]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property primary Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must not be empty: $.benchmarks[0].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must not be empty: $.benchmarks[1].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must not be empty: $.benchmarks[2].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0].evidenceUrls must not be empty: $.recommendedUseCases[0].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1].evidenceUrls must not be empty: $.recommendedUseCases[1].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[5] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[5] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[6] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[6] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[7] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[7] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.sources[7]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
