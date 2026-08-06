# Biomedical Extraction model selection

- Category: `healthcare`
- Group: `biomedical-extraction`
- Independent audit: `revised`
- Researched: `2026-07-23T20:02:58.627897+00:00`

Token- and span-level biomedical named-entity recognition (NER) over English biomedical/clinical text. Scoped sub-tasks: (A) disease/pathology-centered extraction (e.g., evaluation on BC5CDR‑Disease-style labels when a single DISEASE-type label is used), and (B) broad multi-entity biomedical NER (multi-type token-classification). Input: plain English biomedical text. Output: for token-classification models, per-token BIO-style label sequences or aggregated entity spans with entity type labels; for GLiNER zero-shot models, the model returns zero-shot/label-score outputs that require a documented conversion step to span-level entities prior to span-level scoring. When a model card documents a native entity set, evaluators may use that native set; when no canonical mapping to an evaluation dataset taxonomy is provided by primary sources, an explicit label-mapping step must be applied and published before metric computation.

## Questions to answer before selecting

- Is the target entity set disease/pathology-only (yes/no)?
- Is the task high-risk clinical decision support requiring auditability/regulatory suitability (yes/no/research-prototyping)?
- Do you require zero-shot extraction of arbitrary entity types without fine-tuning (yes/no)?
- Will you fine-tune on an in-domain annotated dataset (yes/no)?
- Is there an upper-bound on input sequence length > 512 tokens (yes/no)?
- Is model license Apache-2.0 acceptable for your operational environment (yes/no/unknown)?
- Are compact/low-latency models preferred over larger models (yes/no)?
- Do you require normalization/mapping of extracted disease mentions to MeSH/OMIM (yes/no)?

## Comparability rules

- Results are comparable only when the following conditions all match: identical dataset name and exact split strings; identical label-space mapping from model labels to dataset canonical labels; identical tokenization and maximum sequence length used at inference; identical evaluation script and span-matching convention (strict exact-span match vs. partial overlap); identical averaging method (micro vs. macro) for aggregated metrics; identical fine-tuning regime and random-seed handling.
- Dataset-level comparability requires that the dataset used is one named in the Benchmark Taxonomy (e.g., "BC5CDR-Disease") and that the dataset version/split referenced in evaluation is the exact same authoritative split referenced by the dataset's official page cited in sources.
- When comparing disease-focused models, if a model outputs multiple entity types, map all disease/pathology-related types to a single DISEASE label prior to scoring if the evaluation dataset expects a single DISEASE label.
- When comparing zero-shot GLiNER outputs to supervised token-classification models, zero-shot outputs must be converted to span-level entities using a documented conversion algorithm; if no canonical conversion algorithm is present in primary sources, the evaluator must publish the conversion code and include it in the experiment artifact to allow comparability.
- If any of the above conditions do not match across experiments, numerical results are not directly comparable and must be reported separately with explicit notes of the mismatched condition(s).

## Conditional routing

### Prefer `openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12` when Use-case: disease/pathology-centered extraction; risk tolerance: research/prototyping; zero-shot not required; fine-tuning or direct evaluation on BC5CDR-Disease intended.

- Why: Primary-source model card for OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M indicates the model was fine-tuned on the BC5CDR dataset and reports evaluation results on the BC5CDR‑Disease test set (precision, recall, F1, and accuracy). This provides direct upstream-checkpoint benchmark evidence for disease/pathology extraction on BC5CDR-Disease.
- Alternative: d4data-biomedical-ner-all-wrapper-cuda12
- Alternative: openmed-pathology-ner-tiny-wrapper-cuda12
- Alternative: openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft
- Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M

### Prefer `d4data-biomedical-ner-all-wrapper-cuda12` when Use-case: broad multi-entity biomedical NER (multi-type token-classification) where a model that supports token-classification usage is preferred.

- Why: The d4data/biomedical-ner-all primary model page documents usage as a Transformers token-classification model and provides token-classification inference examples, indicating suitability for multi-entity biomedical NER tasks at the model-card level.
- Alternative: openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12
- Alternative: openmed-pathology-ner-tiny-wrapper-cuda12
- Evidence: https://huggingface.co/d4data/biomedical-ner-all

### Prefer `openmed-pathology-ner-tiny-wrapper-cuda12` when Use-case: zero-shot extraction of arbitrary entity types with priority on small model footprint and low-latency prototyping (zero-shot GLiNER capability required).

- Why: Primary-source commit for the OpenMed ZeroShot NER Pathology Tiny model documents the GLiNER attribution and shows the model-level commit; the model family is described in primary sources as providing zero-shot entity recognition capabilities (GLiNER-style).
- Alternative: openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft
- Alternative: d4data-biomedical-ner-all-wrapper-cuda12
- Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

### Prefer `openmed-pathology-ner-tiny-wrapper-cuda12` when Operational constraint: license must be explicitly Apache-2.0 in primary source for deployment approval.

- Why: Primary-source commit for the OpenMed ZeroShot NER Pathology Tiny model indicates the model is licensed under the Apache License 2.0; the OpenMed DiseaseDetect BioMed 335M model page also indicates Apache-2.0 at the model page level.
- Alternative: openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12
- Alternative: d4data-biomedical-ner-all-wrapper-cuda12
- Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M

### Prefer `insufficient-evidence` when Constraint: input sequences longer than 512 tokens must be processed by the candidate model at inference without chunking.

- Why: Primary sources reviewed do not provide primary-source evidence that the exact Forge wrapper variants in scope accept sequences >512 tokens without chunking. The OpenMed disease model page provides dataset and evaluation information but does not in the provided findings specify a wrapper-level maximum input length for the exact Forge-served checkpoints; d4data primary page does not specify a maximum input length in the provided findings.
- Alternative: d4data-biomedical-ner-all-wrapper-cuda12
- Alternative: openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12
- Alternative: openmed-pathology-ner-tiny-wrapper-cuda12
- Alternative: openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft
- Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/d4data/biomedical-ner-all

## Benchmark taxonomy

### Disease/pathology named-entity recognition (single DISEASE label)

- Datasets: BC5CDR-Disease (test split)
- Metrics: Precision (span-level, strict exact-span match, micro-averaged), Recall (span-level, strict exact-span match, micro-averaged), F1 (span-level, strict exact-span match, micro-averaged)
- Compare only when: Use identical BC5CDR-Disease official test split (exact split file/version as published on the dataset's authoritative page cited in sources).
- Compare only when: Map each model's output to a single DISEASE label prior to scoring (if model emits multiple disease-related types, collapse to DISEASE).
- Compare only when: Use the same tokenization and maximum sequence length at inference (document clearly if chunking is applied).
- Compare only when: Use span-level strict exact-span matching for positive identification unless a documented alternative partial-match protocol is chosen and applied identically to all models.
- Compare only when: Use micro-averaging across all spans for aggregated precision/recall/F1.

### Broad multi-entity biomedical NER (multi-type token-classification)

- Datasets: Evidence gap: no canonical dataset cited in primary sources for d4data/biomedical-ner-all
- Metrics: Token-level BIO accuracy (where relevant, for debugging), Span-level per-entity-type precision/recall/F1 (strict exact-span match), micro- and macro-averaged as reported, Aggregated micro F1 across all entity types
- Compare only when: Use identical dataset and exact split files.
- Compare only when: Apply explicit mapping from model-declared entity types to the dataset's entity taxonomy; if no mapping is provided by primary sources, the evaluator must publish the mapping.
- Compare only when: Use identical tokenization and maximum sequence length at inference.
- Compare only when: Use the same span-matching code and averaging (micro vs macro) for final metrics.

### Zero-shot pathology/disease extraction (GLiNER outputs converted to spans)

- Datasets: Evidence gap: no canonical GLiNER-to-span conversion algorithm found in primary sources
- Metrics: Span-level precision/recall/F1 (strict exact-span match) after conversion of zero-shot outputs to spans
- Compare only when: Document and publish the zero-shot-to-span conversion algorithm and apply identically across all zero-shot experiments and when comparing to supervised token-classification outputs.
- Compare only when: Use identical evaluation script and exact dataset split for comparison.
- Compare only when: If conversion algorithm is not documented in primary sources, include conversion code in the experiment artifact repository.

## Primary sources

- [OpenMed ZeroShot NER Pathology Tiny - commit showing license and GLiNER attribution](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47) — Hugging Face (OpenMed repository commit); supports The OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M model commit 751c87f2dfa77800e1bead7f9fb40f5734078e47 is available at this commit URL, The OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M model is licensed under the Apache License 2.0, The OpenMed ZeroShot family is attributed to GLiNER-style zero-shot named-entity recognition (zero-shot output modality)
- [d4data/biomedical-ner-all model card](https://huggingface.co/d4data/biomedical-ner-all) — Hugging Face (d4data repository); supports The Hugging Face model ID d4data/biomedical-ner-all is hosted at this URL, The d4data/biomedical-ner-all model can be used with the transformers pipeline "ner" and aggregation_strategy="simple", The model card includes an example inference demonstrating token-classification usage
- [OpenMed NER DiseaseDetect BioMed 335M model card](https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M) — Hugging Face (OpenMed repository); supports The OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M model is hosted at this URL, The model page indicates the model was fine-tuned on the BC5CDR dataset (upstream-checkpoint evidence), The OpenMed-NER-DiseaseDetect-BioMed-335M model page reports evaluation results on the BC5CDR‑Disease test set (precision 0.8887, recall 0.9126, F1 0.9005, accuracy 0.9838 as reported on the model page), The BC5CDR‑Disease corpus description (1,500 PubMed abstracts, 5,818 annotated disease entities) is referenced on the model page in this primary source
- [Exact official starting source declared by Forge](https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No primary-source documentation in the provided findings explicitly ties reported evaluation metrics to the exact Forge wrapper versionKeys for all listed wrapper slugs; upstream-checkpoint metrics are present for OpenMed-NER-DiseaseDetect-BioMed-335M but evidence linking exact Forge wrapper versionKeys (as named in scope) to those exact evaluated checkpoints is not present in the findings.
- Evidence gap: No primary-source canonical GLiNER-to-span conversion algorithm or canonical evaluation script was found in the provided primary sources; evaluators must publish the conversion code to allow reproducibility and comparability.
- Evidence gap: No primary-source canonical mapping from d4data/biomedical-ner-all declared entity types to standard dataset taxonomies (e.g., BC5CDR) was found in the provided findings; evaluators must produce and publish mapping files to allow fair comparison.
- Evidence gap: Exact maximum input length (max sequence length) for the d4data/biomedical-ner-all primary model page is not specified in the provided findings; primary sources do not provide a wrapper-level max input length for the d4data variant in scope.
- Evidence gap: No head-to-head evaluations under matched protocols between the exact Forge wrapper versionKeys listed in scope were present in the provided findings; controlled head-to-head comparisons require running experiments per the Benchmark Taxonomy.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 16 deterministic draft defect(s) were supplied to the audit.

- `medium` $.decisionRules[0]: $.decisionRules[0]: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[1]: $.decisionRules[1]: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[2]: $.decisionRules[2]: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[3]: $.decisionRules[3]: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[4]: $.decisionRules[4]: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[5]: $.decisionRules[5]: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property datasetSources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property metricSources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property datasetSources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property metricSources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property datasetSources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property metricSources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2] uses a community discussion URL: $.sources[2] uses a community discussion URL Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
