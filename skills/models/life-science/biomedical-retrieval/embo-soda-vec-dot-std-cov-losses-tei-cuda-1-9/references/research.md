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

- Research key: `huggingface-co-embo-soda-vec-dot-std-cov-losses-81dbb7b5f9`
- Independent audit: `revised`
- Researched: `2026-08-06T08:50:44.632447+00:00`

Primary inspected evidence is a Hugging Face dataset commit page (https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5). That source documents a paired PubMed Central (PMC) title-abstract dataset with per-example fields 'anchor' (title), 'positive' (abstract), and 'pmcid' and states the dataset is intended for training sentence-transformer style models with negative sampling; it asserts a CC-BY-4.0 license and tags text-similarity / feature-extraction / biomedical. The dataset-size facts in the provided evidence are conflicting: one statement says the dataset "contains a total of 1,000 examples" while another statement classifies the dataset size as between 10 million and 100 million samples (10M<n<100M). No primary evidence in the supplied findings documents an upstream Hugging Face model card, immutable model-file checksum, tokenizer metadata for a model checkpoint, model identity (checkpoint name/revision/parameter count), numeric benchmarks for a checkpoint, wrapper manifests mapping Forge-serving slugs to an immutable upstream revision, training hyperparameters, pooling/embedding-output dtype, or any clinical/PHI/privacy statements for a model checkpoint. All verifier actions and required dossier fields not supported by the dataset commit page are recorded below as explicit evidence gaps that reference the exact inspected primary URL.

## Identity

- Upstream name: not reported
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

## Selection

### Recommended

- **Training sentence-transformer-style embedding models for text similarity/feature-extraction on PMC title-abstract pairs** — The dataset commit page documents a paired (anchor-positive) format with fields 'anchor' (title) and 'positive' (abstract) and lists task categories 'text-similarity' and 'feature-extraction'.
  Scope: EMBO/soda-vec-data-full_pmc_title_abstract_paired (dataset commit)
  Evidence: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Conditional

- **Contrastive / negative-sampling training (sentence-transformers) using anchor-positive PMC title-abstract pairs** — Use only after verifying the actual dataset scale (conflicting size statements present) and confirming downstream validation on the target corpus; the commit page states the dataset is 'Paired (anchor-positive) for contrastive learning' but contains conflicting size metadata that must be resolved before large-scale training assumptions.
  Scope: EMBO/soda-vec-data-full_pmc_title_abstract_paired (dataset commit)
  Evidence: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Avoid

- **Direct deployment of a model checkpoint for clinical decision-making or production healthcare without further validation** — Evidence gap: The inspected primary source is a dataset commit page and does not provide any model checkpoint clinical validation, safety, or calibration statements for a checkpoint.
  Scope: upstream model checkpoint (not present in provided findings)
  Evidence: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- **Assuming model-checkpoint-specific tokenizer, pooling, or calibrated scores for inference** — Evidence gap: No model checkpoint, tokenizer metadata, pooling rules, or score-interpretation guidance for a checkpoint are present in the inspected primary source.
  Scope: upstream model checkpoint (not present in provided findings)
  Evidence: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

## Input preparation

### Semantic inputs

- Dataset examples contain these fields: 'anchor' (string) representing the article title; 'positive' (string) representing the article abstract; and 'pmcid' (string) representing the PubMed Central ID. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Accepted formats

- Paired (anchor-positive) examples for contrastive learning (anchor = title, positive = abstract). Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- Language: English (en) as stated in the dataset metadata. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Preprocessing

- The dataset is formatted for paired examples; the commit page does not provide tokenizer class name, normalization, lowercasing, or tokenization rules for any model checkpoint. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Pre-submit validation

- Evidence gap: The inspected commit page does not specify input-validation rules, sequence-length limits, truncation/padding policy, or batching strategy for a model checkpoint; verifier must record 'Evidence gap: [URL] -> commit page checked' when filling the dossier fields for tokenizer and preprocessing. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Task-specific formatting

- The dataset is intended for contrastive/paired training; no model-card-level prompt templates, pair-concatenation separators, or inference formatting rules for a checkpoint are present in the inspected source. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

## Output interpretation

### Outputs

- Evidence gap: The inspected primary source is a dataset commit page and does not document any model checkpoint outputs (embedding dimensionality, dtype, pooling method, or normalization). Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Interpretation

- Evidence gap: No recommended post-inference sanity checks, calibration steps, or similarity-function guidance for a model checkpoint are present in the inspected primary source. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Post-inference validation

- Evidence gap: The dataset commit page does not provide post-inference validation checks for a model checkpoint; include exact evidence-gap locator when populating the dossier. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: not reported
- Criteria: No task- and protocol-matched comparisons of a named checkpoint to other checkpoints were present in the inspected primary source.
- Rationale: The inspected commit page documents dataset fields and dataset intent but contains no model-card comparisons or numeric side-by-side evaluations.
- Comparison conditions: Evidence gap: checked dataset commit page for any linked model-card comparisons; none found at this exact locator.
- Evidence: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

## Limitations and safety

### Limitations

- Evidence gap: No upstream model checkpoint identity (model card URL, checkpoint name, model-file checksum, or HF model revision) was present in the provided findings; verifier must record the exact model-card URL if and when it is found. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- Ambiguity in dataset-scale metadata: the inspected evidence contains both 'contains a total of 1,000 examples' and an explicit size-category statement 'between 10 million and 100 million samples (10M<n<100M)'. This conflict must be resolved by checking the canonical dataset page or repository history; both statements were taken from the same commit URL. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- Evidence gap: No tokenizer metadata, embedding dimensionality, pooling rules, output dtype, or inference normalization guidance for any model checkpoint is present in the inspected source. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- Evidence gap: No numeric evaluation metrics or protocol details for checkpoint comparability were found at the inspected locator. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

### Safety

- Evidence gap: The inspected primary source (dataset commit page) does not include clinical validation, PHI-handling guidance, privacy, or data-retention statements relevant to a model checkpoint. Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- Because the available primary evidence documents biomedical literature data, downstream users should conduct task-specific validation and expert review before high-stakes deployment; verifier must record such reviewer guidance as a Forge policy statement only if authoritative upstream documentation is absent (no such documentation was found in the supplied findings). Sources: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### EMBO/soda-vec-data-full_pmc_title_abstract_paired commit 9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5

- URL: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5
- Publisher: EMBO (Hugging Face dataset hosting)
- Type: `repository`
- Primary because: This is the only canonical primary-source URL supplied in the findings. It contains dataset-level claims (per-example fields, intended task categories, dataset license declarations, language and tags) which are the only verified facts available to populate dossier fields.
- Scope: EMBO/soda-vec-data-full_pmc_title_abstract_paired (dataset commit)
- Supports: dataset fields: 'anchor', 'positive', 'pmcid'
- Supports: dataset intended format: Paired (anchor-positive) for contrastive learning
- Supports: dataset task categories: text-similarity, feature-extraction
- Supports: dataset language: English (en)
- Supports: dataset license assertion: CC-BY-4.0 (as reported on the commit page)
- Supports: dataset tags and intended usage guidance for sentence-transformer training
- Supports: conflicting dataset-size metadata (both '1,000 examples' and size-category '10M<n<100M' present in the inspected commit)

### Exact official starting source declared by Forge

- URL: https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: embo-soda-vec-dot-std-cov-losses
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No Hugging Face model card URL for EMBO/soda-vec-dot-std-cov-losses was present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page) -> no model-card or checkpoint identity found.
- Evidence gap: No immutable model artifact identifier (model-file SHA256/MD5 or HF blob id) was present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page) -> no model-file metadata found.
- Evidence gap: Tokenizer class name, tokenizer files, tokenizer_config.json, tokenizer.json, special_tokens_map.json, and full tokenization rules for any model checkpoint are not present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).
- Evidence gap: Embedding output characteristics (dimensionality, pooling method, dtype, inference-time normalization, recommended similarity function) are not present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).
- Evidence gap: No checkpoint-scoped numeric benchmarks (dataset+split+metric+numeric value) were found in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).
- Evidence gap: No wrapper- or Forge-manifest mapping Forge-serving slugs to an immutable upstream checkpoint revision was present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).
- Evidence gap: Training hyperparameters (learning rate, batch size, fp16, scheduler, max steps, eval/save steps) for any model checkpoint are not present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).
- Evidence gap: License applicability distinction between model weights and code for any model checkpoint is not present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).
- Evidence gap: No clinical validation, PHI-handling guidance, privacy, or data-retention statements for a model checkpoint were present in the supplied findings; checked: https://huggingface.co/datasets/EMBO/soda-vec-data-full_pmc_title_abstract_paired/commit/9ea13e99da45b5a499bf6c0d7374e5534fb6dfd5 (commit page).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses unapproved repository owner 'answerdotai' for this exact model scope: $.sources[6] uses unapproved repository owner 'answerdotai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
