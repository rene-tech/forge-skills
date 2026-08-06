# Biomedical Text model selection

- Category: `life-science`
- Group: `biomedical-text`
- Independent audit: `revised`
- Researched: `2026-07-23T20:21:54.683908+00:00`

Biomedical-text in this dossier means text-only use of the exact checkpoint `stanfordcrfm-biomedlm-2-7b` for biomedical text generation and narrowly scoped benchmark reporting that is explicitly supported by primary checkpoint or paper sources. In scope: checkpoint-identified biomedical text generation and checkpoint-identified benchmark claims directly tied to BioMedLM. Out of scope unless directly evidenced for this exact candidate: multimodal use, production-runtime behavior, long-context claims, instruction/chat tuning, adapters, quantized variants, serving wrappers, family-wide transfer claims, and unsupported downstream task claims.

## Questions to answer before selecting

- Is the use case limited to text input and text output?
- Does the user need evidence for the exact checkpoint `stanfordcrfm-biomedlm-2-7b`, rather than family-level wording?
- Is the task biomedical text generation or a benchmark setting explicitly reported for BioMedLM in the primary findings?
- If relying on question-answering evidence, is the user specifically targeting MedQA under a protocol close enough to the reported claim to avoid unsupported transfer?
- Is production suitability required, even though the provided findings do not supply checkpoint-specific production-readiness evidence?
- Does the use case require protocol details such as prompt format, preprocessing, split, decoding, or adaptation regime that are not specified in the verified findings?
- Does the application require long-context support beyond what the verified findings explicitly state?
- Is the user prepared to treat unsupported subtasks as evidence gaps rather than inferring capability from general biomedical pretraining or family naming?
- Does licensing review need more than identity-level checkpoint source evidence from the model card?
- Are safety-sensitive or clinical-use requirements present that would require evidence beyond the sparse checkpoint-specific findings?

## Comparability rules

- Only compare results that are explicitly attributable to the exact candidate `stanfordcrfm-biomedlm-2-7b`; do not transfer unsupported claims from family, variants, adapters, classifiers, serving runtimes, or quantized releases.
- For MedQA comparisons, require the same dataset name, metric, and task formulation; the findings do not specify split, prompt, decoding, preprocessing, or adaptation regime, so unmatched or unspecified protocols are non-comparable.
- Treat classifier-backed or fine-tuned results as distinct from base-checkpoint use unless the source explicitly states the dependency; do not present attached-classifier or fine-tuned results as raw base-model behavior.
- Do not compare operational or deployment properties as model-quality evidence; the provided findings do not establish inference-runtime comparability.
- If a source supports only family identity or renaming, do not use it to imply checkpoint-specific benchmark superiority.
- When protocol details are absent, use insufficient-evidence rather than implying apples-to-apples comparison.
- Do not infer tokenizer behavior, architecture details, context length, or license terms beyond what the verified primary findings explicitly support.

## Conditional routing

### Prefer `stanfordcrfm-biomedlm-2-7b` when A user needs a checkpoint-specific biomedical text model reference and the requirement is limited to text-only biomedical generation or research benchmarking explicitly tied to BioMedLM.

- Why: Primary identity evidence confirms the official model card for BioMedLM and ties the checkpoint naming history to BioMedLM/previously PubMedGPT 2.7B, supporting use of this exact candidate as the only in-scope Forge option. However, the verified findings do not provide complete protocol detail for broad task routing beyond narrow checkpoint attribution.
- Evidence: https://huggingface.co/stanford-crfm/BioMedLM, https://github.com/stanford-crfm/BioMedLM

### Prefer `insufficient-evidence` when A user wants to rely on benchmark evidence for biomedical question answering beyond the narrowly reported MedQA claim, or wants head-to-head routing against other candidates.

- Why: The primary findings include a MedQA 50.3% accuracy claim for BioMedLM, and also report classifier-only and fine-tuned benchmark variants in the paper findings, but the findings do not supply enough protocol detail to support broad comparison or robust routing under matched conditions. There is only one candidate in scope, so no distinct alternative candidate can be preferred.
- Evidence: https://arxiv.org/html/2403.18421v1, https://huggingface.co/stanford-crfm/BioMedLM

### Prefer `insufficient-evidence` when The use case requires production-readiness, explicit serving assurances, instruction-following, chat behavior, or other non-evidenced capabilities for this exact checkpoint.

- Why: The verified findings do not provide checkpoint-specific primary evidence establishing production suitability, runtime guarantees, instruction tuning, or chat optimization for the exact Forge candidate.
- Evidence: https://huggingface.co/stanford-crfm/BioMedLM

## Benchmark taxonomy

### Biomedical question answering

- Datasets: MedQA
- Metrics: Accuracy (higher is better)
- Compare only when: Result must be explicitly attributed to BioMedLM.
- Compare only when: Use MedQA specifically.
- Compare only when: Keep task formulation aligned; the findings do not specify prompt or answer formatting.
- Compare only when: Keep split aligned; the findings do not specify split details for the 50.3% claim in the model-card finding.
- Compare only when: Keep preprocessing, decoding, and normalization aligned; the findings do not specify them.
- Compare only when: Distinguish base checkpoint use from classifier-only or fine-tuned variants when interpreting results.

### Biomedical multiple-choice or exam-style evaluation reported in the paper findings

- Datasets: MedMCQA development set, MMLU Medical Genetics benchmark
- Metrics: Accuracy (higher is better)
- Compare only when: Use the exact named dataset or benchmark.
- Compare only when: Do not compare fine-tuned results to base-model use without preserving the adaptation regime.
- Compare only when: Keep split alignment exact where stated; development and test settings are not interchangeable.
- Compare only when: Treat attached-classifier and fine-tuned results as separate protocols from raw checkpoint use.

### Biomedical text generation / autoregressive language modeling

- Datasets: Evidence gap: The verified findings do not provide a benchmark dataset string for a retained canonical generation benchmark taxonomy entry beyond general checkpoint identity.
- Metrics: Evidence gap: The verified findings do not provide a retained canonical generation metric for exact-checkpoint comparison.
- Compare only when: Text-only input and output only.
- Compare only when: Do not infer benchmark comparability without prompt, preprocessing, decoding, and normalization details.
- Compare only when: Do not transfer serving-runtime observations into model-quality comparisons.

## Primary sources

- [BioMedLM model card](https://huggingface.co/stanford-crfm/BioMedLM) — Stanford CRFM; supports Official Hugging Face model card identity for BioMedLM, Renaming note from PubMedGPT 2.7B to BioMedLM, Checkpoint-scoped source URL for the exact Forge candidate
- [Stanford CRFM BioMedLM repository](https://github.com/stanford-crfm/BioMedLM) — Stanford CRFM; supports Official Stanford CRFM GitHub repository identity for BioMedLM, Renaming note from PubMedGPT 2.7B to BioMedLM
- [BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text](https://arxiv.org/abs/2403.18421) — arXiv; supports Canonical original paper/preprint identity for BioMedLM
- [BioMedLM paper HTML](https://arxiv.org/html/2403.18421v1) — arXiv; supports Reported benchmark values including MedQA 50.3% classifier-only accuracy, Reported MedMCQA development-set accuracy, Reported MMLU Medical Genetics accuracy, Reported fine-tuned benchmark variants, Reported paper-level training-data wording and open-source characterization

## Evidence gaps

- Evidence gap: The verified findings do not provide a primary canonical source in the allowed set that directly confirms architecture details, tokenizer specification, vocabulary size, or context length for the exact checkpoint without relying on forbidden secondary sources from the findings set.
- Evidence gap: The verified findings do not provide checkpoint-specific prompt templates, preprocessing, output normalization, decoding settings, or validation protocol for the reported MedQA claim.
- Evidence gap: The verified findings do not specify whether the model-card-linked MedQA result is zero-shot, few-shot, fine-tuned, or otherwise adapted.
- Evidence gap: The verified findings do not provide a protocol-matched head-to-head comparison basis against any other exact Forge candidate because only one candidate is in scope.
- Evidence gap: The verified findings include benchmark rows in the paper HTML that distinguish classifier-only and fine-tuned conditions, but do not provide enough protocol detail here to route use cases beyond narrow attribution.
- Evidence gap: The verified findings do not provide checkpoint-specific production-readiness, latency, throughput, or operational assurance evidence.
- Evidence gap: The verified findings do not provide checkpoint-specific clinical-use, privacy-handling, expert-review, or healthcare deployment boundary text sufficient to establish stronger safety rules.
- Evidence gap: The verified findings include a canonical paper identity URL, but the supplied findings for that URL do not add benchmark protocol detail beyond paper existence.
- Evidence gap: The findings conflict on training data wording. One primary paper-HTML finding says the model was trained exclusively on PubMed abstracts and full-text articles, while the prompt's draft materials referenced other wording not retained here; this dossier therefore avoids stronger training-corpus normalization claims.
- Evidence gap: The findings mention open-source status in the paper HTML and provide the model-card identity URL, but do not provide a verified primary license statement sufficient to preserve a precise weight-license versus code-license distinction in this corrected dossier.
- Evidence gap: The verified findings do not establish instruction-following, chat behavior, retrieval augmentation, summarization, extraction, classification deployment, or other unsupported biomedical subtasks for the exact checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
