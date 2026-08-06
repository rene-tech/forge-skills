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

- Research key: `build-nvidia-com-meta-llama-3-1-8b-instruct-365e0f344a`
- Independent audit: `revised`
- Researched: `2026-07-23T22:43:59.904438+00:00`

This dossier covers the Meta Llama 3.1 instruction-tuned 8B checkpoint (Llama-3.1-8B-Instruct) as documented in upstream primary resources and the NVIDIA NGC catalog pages present in the evidence set. Primary upstream documentation (GitHub MODEL_CARD.md and the Hugging Face model page) identify an instruction-tuned 8B auto-regressive transformer using Grouped-Query Attention (GQA) and report a family-level maximum context length of 128,000 tokens. Upstream evaluation notes (eval_details.md and MODEL_CARD.md) report numeric evaluation entries (e.g., MMLU 5-shot micro-average for the post-trained 8B instruct model reported as 69.4% in MODEL_CARD.md) and provide evaluation-shot counts and some length limits, but the cited primary artifacts do not publish exact prompt templates, random seeds, or complete decoding hyperparameters for reproduced benchmarks. The available primary NGC container metadata documents a served container named for the model and container-layer metadata, but an immutable provenance mapping (artifact checksum or upstream commit SHA proving byte-for-byte identity between served container weights and an upstream checkpoint artifact) is not reported in the examined primary sources. Several operational details required for provenance-sensitive workflows (canonical tokenizer implementation and token-ID mapping, exact revision identifiers for the upstream weights, exposure of raw logits by the callable serving container, and full evaluation prompt/decoding protocol) are not available in the cited primary sources and are recorded as evidence gaps.

## Identity

- Upstream name: meta-llama-3.1-8b-instruct
- Checkpoint/version: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- Immutable revision: not reported
- Parameter scale: 8 billion parameters
- Architecture/head: auto-regressive transformer with Grouped-Query Attention (GQA)
- License: Llama 3.1 Community License — https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/models/llama-3.1-8b-instruct/h200x1-throughput-lora-fp8-uglyei4ocw, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-8b-instruct/1.2.2/layers, https://build.nvidia.com/meta/llama-3.1-8b-instruct

## Selection

### Recommended

- **Instruction-following and conversational dialogue** — Upstream model card and the Hugging Face presentation describe the checkpoint as instruction-tuned and optimized for assistant-like chat and dialogue.
  Scope: meta-llama-3.1-8b-instruct (upstream checkpoint documentation)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- **Code-evaluation and coding assistance experiments (requires downstream validation and calibration)** — Upstream evaluation documentation and MODEL_CARD.md report code-evaluation metrics (HumanEval / MBPP family entries) for the post-trained/instruct variants, indicating the checkpoint was evaluated on code tasks; adopters must validate sampling/decoding and perform task-specific calibration before production use.
  Scope: meta-llama-3.1-8b-instruct (upstream post-trained/instruct checkpoint as reported in upstream evaluation artifacts)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- **Summarization and general multilingual text generation** — Upstream model card and Hugging Face documentation present the tuned models as intended for coherent multilingual text generation and instruction-following tasks.
  Scope: meta-llama-3.1-8b-instruct (upstream checkpoint documentation)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

### Conditional

- **Very-long-context workflows approaching the family-level maximum (document-level retrieval / long-context pipelines)** — Family-level documentation lists a 128,000-token maximum context window; runtime- and container-specific end-to-end validation (position-embedding support, tokenizer behavior, memory/precision tradeoffs, and container/runtime limits) is required to confirm the specific 8B instruct variant and chosen serving container preserve full 128k behavior before relying on it in production.
  Scope: meta-llama-3.1-8b-instruct (family-level context claim; runtime/container validation required for the served 8B instruct variant)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://catalog.ngc.nvidia.com/orgs/nim/meta/models/llama-3.1-8b-instruct/h200x1-throughput-lora-fp8-uglyei4ocw
- **Safety-critical or regulated-domain deployment (medical, legal, financial decisioning)** — Upstream model card and NVIDIA guidance recommend human review and system-level guardrails; deployers must perform domain-specific validation, human oversight, and legal/compliance checks prior to production use.
  Scope: meta-llama-3.1-8b-instruct (upstream checkpoint and any chosen served/container runtime used in deployment)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/models/llama-3.1-8b-instruct/h200x1-throughput-lora-fp8-uglyei4ocw

### Avoid

- **Unreviewed deployment in high-risk domains without expert oversight** — Upstream model card documents limitations including hallucination risk and recommends human review for high-risk applications; do not deploy without domain experts and validation.
  Scope: meta-llama-3.1-8b-instruct (upstream checkpoint)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE

## Input preparation

### Semantic inputs

- Input modality: plain text (string) only. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- Evidence gap: canonical tokenizer implementation description (library/class and canonical special-token ID mapping) for the upstream instruct checkpoint is not enumerated in the upstream model card or Hugging Face model presentation. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

### Accepted formats

- Accepted input: a non-empty text prompt (string) for single-turn or multi-turn instruction-following interactions. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- Evidence gap: the upstream sources do not provide a canonical structured role-based prompt template (system/user/assistant markers) specific to this instruct checkpoint. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

### Preprocessing

- Evidence gap: explicit tokenization and preprocessing steps (tokenizer implementation, BPE/merge details, normalization pipeline) are not documented in the upstream model card or Hugging Face model page for this exact instruct checkpoint. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- Evidence gap: the upstream documentation does not enumerate a default client-side truncation or alignment policy; deployers should validate tokenization and truncation behavior in their runtime. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md

### Pre-submit validation

- Input and context validation: family-level documentation lists a maximum context length of 128,000 tokens; validate runtime and chosen container for effective window behavior before relying on the maximum in production. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://catalog.ngc.nvidia.com/orgs/nim/meta/models/llama-3.1-8b-instruct/h200x1-throughput-lora-fp8-uglyei4ocw
- Evidence gap: the upstream documentation does not provide a canonical list of invalid or ambiguous input cases requiring rejection at the tokenizer level; deployers must implement domain-specific input validation. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md

### Task-specific formatting

- Evidence gap: the upstream model card does not publish official role-markup templates (system/user/assistant) or a canonical tool-calling schema for this instruct checkpoint. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- Evidence gap: no upstream canonical examples documenting special tokens for tool calling or function-call emission for this checkpoint were found in the examined primary sources. Sources: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md

## Output interpretation

### Outputs

- Evidence gap: primary upstream sources do not document that the callable checkpoint exposes raw logits or per-token unnormalized scores to end users; the upstream model card and Hugging Face page do not specify exposed runtime output shapes, and the examined NGC container metadata does not provide that runtime detail. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-8b-instruct/1.2.2/layers

### Interpretation

- Model outputs should be interpreted as text continuations conditioned on the prompt; upstream documentation documents hallucination risk and recommends human review for high-risk outputs. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md

### Post-inference validation

- Post-inference validation: perform human review for high-risk outputs and task-specific validation where correctness matters; the upstream model card recommends human review for high-risk applications. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md

## Public benchmarks

### MMLU (Massive Multitask Language Understanding)

- Dataset/split: MMLU / not reported
- Metric/value: micro-average accuracy / 69.4% (post-trained/instruct 8B, 5-shot) (`higher-is-better`)
- Model scope: meta-llama-3.1-8b-instruct (post-trained/instruct 8B as reported in upstream MODEL_CARD.md)
- Conditions: Reported as 5-shot in MODEL_CARD.md; exact prompt templates, decoding algorithm, sampling temperature, beam/sampling settings, and random seeds are not provided in the cited primary artifacts.
- Source: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md
- Locator: MODEL_CARD.md section reporting MMLU (5-shot macro_avg/acc) scores for Llama 3.1 8B Instruct
- Caveat: Missing exact prompt templates and full decoding hyperparameters (temperature, sampling/beam/greedy, random seeds) in the cited MODEL_CARD.md and eval_details.md.
- Caveat: Split not reported in the cited primary source; reproductions must confirm dataset split and filtering.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: performance benchmark comparisons requiring protocol-matched evidence
- Criteria: Protocol-matched dataset/split/prompt/decoding required for direct comparisons; such matching primary evidence for alternative named candidates was not found in the examined sources.
- Rationale: Primary evidence provides benchmark numbers for Llama-3.1-8B-Instruct in MODEL_CARD.md and evaluation notes in eval_details.md, but protocol-matched primary benchmark entries for named alternatives were not found in the examined primary sources; therefore direct comparisons are not supported.
- Comparison conditions: Benchmarks must match dataset, split, prompt templates, shot conditions, decoding hyperparameters, and seeds for valid comparison.
- Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

## Limitations and safety

### Limitations

- Upstream model card documents typical LLM limitations: hallucination risk, bias, and a knowledge cutoff; human review is recommended for high-risk applications. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md
- Family-level training-data scale: upstream sources report a pretraining token count exceeding 15 trillion tokens for the Llama 3.1 family (family-level statement). Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- License scope limitation: the upstream license requires compliance with applicable laws and an Acceptable Use Policy; the license text does not enumerate exhaustive per-category prohibitions within the license file examined. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE, https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

### Safety

- The license requires compliance with applicable laws, regulations, and the Acceptable Use Policy; deployers must enforce legal and policy compliance in their use of the checkpoint. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE
- Upstream model card and NGC model/container metadata recommend human review for high-risk applications and document known risks (hallucination, bias); human-in-the-loop review and system-level guardrails are advised. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/meta/models/llama-3.1-8b-instruct/h200x1-throughput-lora-fp8-uglyei4ocw

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Meta Llama-3.1 family model card (GitHub repository)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md
- Publisher: Meta
- Type: `model-card`
- Primary because: Primary author-maintained model card documenting family and checkpoint-level design, training notes, limitations, and family-level claims.
- Scope: upstream family and checkpoint documentation for Llama-3.1 series
- Supports: architecture (auto-regressive transformer with GQA)
- Supports: training method notes and instruction-tuning claims
- Supports: recommended human review and documented limitations
- Supports: family-level claims (training scale, supported languages, context length)
- Supports: reported benchmark numbers (e.g., MMLU 5-shot entries for 8B instruct)

### Llama 3.1 Community License file (upstream)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE
- Publisher: Meta
- Type: `official-documentation`
- Primary because: Canonical license text provided with the upstream model distribution.
- Scope: license governing upstream Llama-3.1 materials
- Supports: license name and obligations (distribution under the Llama 3.1 Community License)
- Supports: license terms referenced by upstream distribution

### Hugging Face model page: Meta Llama-3.1-8B-Instruct

- URL: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
- Publisher: Meta (upstream model distribution on Hugging Face)
- Type: `repository`
- Primary because: Canonical upstream model distribution and presentation page for the Llama-3.1-8B-Instruct checkpoint.
- Scope: upstream checkpoint model page and distribution for Llama-3.1-8B-Instruct
- Supports: upstream checkpoint identity and presentation
- Supports: parameter scale (8B stated)
- Supports: family-level context window claim (128,000 tokens)
- Supports: intended uses and out-of-scope guidance

### Upstream evaluation details for Llama-3.1 (eval_details.md)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md
- Publisher: Meta
- Type: `repository`
- Primary because: Primary upstream evaluation notes and reported numeric scores for specific tasks and shot conditions.
- Scope: upstream evaluation details for Llama-3.1 family and 8B checkpoint
- Supports: evaluation methodology context and shot counts for reported benchmarks
- Supports: evaluation notes referenced by MODEL_CARD.md

### NGC model/catalog listing: Llama-3.1-8B-Instruct (model page)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/meta/models/llama-3.1-8b-instruct/h200x1-throughput-lora-fp8-uglyei4ocw
- Publisher: NVIDIA NGC (NIM)
- Type: `official-documentation`
- Primary because: NVIDIA NGC catalog entry describing the served model, its parameter scale, context limit, and serving guidance.
- Scope: NVIDIA-served container/model listing for meta-llama-3.1-8b-instruct
- Supports: serving/runtime presentation and stated model identity
- Supports: presentation of parameter scale and stated context length metadata for the served container
- Supports: serving guidance and license references for the container

### NGC container listing: Llama-3.1-8B-Instruct (container layers / metadata)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/meta/containers/llama-3.1-8b-instruct/1.2.2/layers
- Publisher: NVIDIA NGC (NIM)
- Type: `official-documentation`
- Primary because: NGC container metadata and distribution page documenting container tag, environment variables, and model_manifest location.
- Scope: NGC container metadata and distribution for the served checkpoint
- Supports: container tag and metadata (model_manifest path, MODEL_LICENSE file)
- Supports: environment variables indicating the served model name and NIM version

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/meta/llama-3.1-8b-instruct
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: meta-llama-3-1-8b-instruct
- Supports: Forge-to-upstream exact-version identity and official starting source declared by Forge

## Evidence gaps

- Evidence gap: Exact checkpoint revision identifier (commit SHA, release tag, or artifact checksum) for the named upstream Llama-3.1-8B-Instruct weights is not reported in the examined primary sources.
- Evidence gap: Canonical tokenizer implementation description (library/class name and canonical special-token ID mapping) for the upstream instruct checkpoint is not enumerated in the upstream model card or Hugging Face model page.
- Evidence gap: Full evaluation protocol details required to reproduce retained numeric benchmarks (exact prompt templates, random seeds, complete decoding hyperparameters including temperature and sampling/beam settings) are not present in the cited primary artifacts (MODEL_CARD.md and eval_details.md).
- Evidence gap: The examined primary sources do not document whether the callable NGC/NIM serving container exposes raw logits or per-token unnormalized scores to end users; runtime-specific validation is required.
- Evidence gap: An explicit immutable provenance mapping (artifact checksum, release tag, or upstream commit SHA proving byte-for-byte identity) tying the NGC/NIM-served container image to an unchanged upstream checkpoint artifact (weights + model card revision) is not present in the examined NGC container metadata pages.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 112 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0]: $.recommendedUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0]: $.recommendedUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1]: $.recommendedUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1]: $.recommendedUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[2]: $.recommendedUseCases[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[2]: $.recommendedUseCases[2]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[0]: $.conditionalUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[0]: $.conditionalUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[1]: $.conditionalUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[1]: $.conditionalUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[1]: $.avoidUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[1]: $.avoidUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[2]: $.avoidUseCases[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[2]: $.avoidUseCases[2]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[2]: $.inputPreparation.semanticInputs[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1]: $.inputPreparation.acceptedFormats[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1]: $.inputPreparation.preprocessing[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[2]: $.inputPreparation.preprocessing[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1]: $.inputPreparation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[1]: $.inputPreparation.taskSpecificFormatting[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1]: $.outputInterpretation.outputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1]: $.outputInterpretation.interpretation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[2]: $.outputInterpretation.interpretation[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
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
- `medium` $.benchmarks[3]: $.benchmarks[3]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3]: $.benchmarks[3]: missing required property sourceLocator Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3]: $.benchmarks[3]: missing required property sourceUrl Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11]: $.sources[11]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12]: $.sources[12]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13]: $.sources[13]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14]: $.sources[14]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15]: $.sources[15]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16]: $.sources[16]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17]: $.sources[17]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18]: $.sources[18]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19]: $.sources[19]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20]: $.sources[20]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21]: $.sources[21]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA: $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/meta/llama-3.1-8b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/llama-3_1-8b-instruct-nemo Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3_1-8b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ollama.com/library/llama3.1:8b-instruct-q3_K_M/blobs/f1cd752815fc Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://x.com/natolambert/status/1815768837926842842 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ollama.com/library/llama3.1:8b-instruct-q3_K_M/blobs/f1cd752815fc Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must not be empty: $.benchmarks[0].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must not be empty: $.benchmarks[1].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must not be empty: $.benchmarks[2].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must not be empty: $.benchmarks[3].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0].evidenceUrls must not be empty: $.recommendedUseCases[0].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1].evidenceUrls must not be empty: $.recommendedUseCases[1].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[2].evidenceUrls must not be empty: $.recommendedUseCases[2].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[2] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[2] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[2] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
