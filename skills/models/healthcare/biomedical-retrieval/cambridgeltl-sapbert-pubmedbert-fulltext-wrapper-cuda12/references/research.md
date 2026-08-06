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

- Research key: `huggingface-co-cambridgeltl-sapbert-from-pubmedbert-fulltext-767ac42e0a`
- Independent audit: `revised`
- Researched: `2026-08-06T11:22:12.430012+00:00`

Primary-source inspection (Hugging Face repository views and the SapBERT arXiv preprint) shows that the repository for cambridgeltl/SapBERT-from-PubMedBERT-fulltext exists at revision d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0 and that the model is presented as a SapBERT-style biomedical entity representation trained with UMLS (README/commit metadata). The repo metadata tags language as English and tags include "biomedical" and "lexical-semantics". The repository manifest (commit history) indicates the presence of config.json, tokenizer_config.json, vocab.txt and related files at the referenced revision, and the README contains a BibTeX citation to the canonical SapBERT paper (arXiv:2010.11784). The primary sources inspected do not report an explicit model-weights license, parameter count, the tokenizer algorithm name, embedding dtype/precision, L2-normalization status, or per-checkpoint benchmark tables tying published paper numbers to this specific revision; those missing items are recorded as evidence gaps with the exact primary URLs checked.

## Identity

- Upstream name: not reported
- Checkpoint/version: cambridgeltl/SapBERT-from-PubMedBERT-fulltext
- Immutable revision: d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main

## Selection

### Recommended

- **Biomedical entity representation / entity-embedding research (embedding tokens/phrases for downstream entity linking or retrieval research)** — The repository README and commit metadata present the checkpoint as implementing SapBERT-style biomedical entity representations trained with UMLS and advise using the [CLS] token as the representation, supporting research use to produce entity embeddings consistent with the SapBERT method.
  Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (revision d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0)
  Evidence: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md

### Conditional

- **Reproducing SapBERT paper-level benchmark evaluations using this checkpoint** — Reproduction requires running the SapBERT evaluation procedures (from the canonical SapBERT paper) against this checkpoint because no per-checkpoint benchmark table or artifact tying published numeric results to this specific revision was found in the repository; users must ensure protocol parity with the SapBERT paper.
  Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (revision d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0)
  Evidence: https://arxiv.org/abs/2010.11784, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main

### Avoid

- **Unreviewed clinical decision-making or direct clinical use without expert oversight** — Evidence gap: The inspected primary repository artifacts and commit metadata do not report any clinical-use approvals, certifications, PHI/data-handling guidance, or deployment safety guarantees for clinical settings.
  Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (revision d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0)
  Evidence: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0

## Input preparation

### Semantic inputs

- English biomedical text (repository metadata tags language as English and tags include 'biomedical' and 'lexical-semantics'; training dataset listed as UMLS in commit metadata). Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0

### Accepted formats

- The repository manifest at the referenced revision indicates the presence of tokenizer and model configuration artifacts (config.json, tokenizer_config.json, vocab.txt) for text input handling, as recorded in the commit history. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main

### Preprocessing

- The README (repository) advises using the [CLS] token as the representation for inputs (i.e., sequence-level representation is provided via [CLS]). Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md
- Evidence gap: The inspected primary repository artifacts do not explicitly state the tokenizer algorithm name (WordPiece, BPE, SentencePiece) or a canonical, ordered preprocessing pipeline (normalization, lowercasing, punctuation handling) in the checked locators. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0

### Pre-submit validation

- Evidence gap: The inspected primary repository artifacts do not provide explicit input-validation rules (allowed character sets, minimum/maximum tokenized lengths beyond the presence of tokenizer/config files in the commit history, or disallowed content checks). Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md

### Task-specific formatting

- Evidence gap: The inspected primary repository artifacts do not document canonical prompt templates, paired-input wrappers, or task-specific control fields in the checked locators. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main

## Output interpretation

### Outputs

- Sequence-level representation is provided via the [CLS] token according to the repository README; the README presents [CLS] as the representation for SapBERT-style embeddings. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md
- Evidence gap: The primary repository artifacts inspected do not state the embedding dtype/precision (fp32/fp16), whether embeddings are L2-normalized, or the runtime output data type/format (Python list, numpy array, tensor) at the checked locators. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md

### Interpretation

- Embeddings produced by this checkpoint are presented in the repository as SapBERT-style biomedical entity representations trained with UMLS; interpretation as entity embeddings for downstream lexical-semantics or entity-linking research is consistent with the repository README and commit metadata. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md

### Post-inference validation

- Evidence gap: The inspected primary repository artifacts do not describe post-inference calibration, recommended normalization, or embedding dtype/precision at the checked locators; downstream validation is required before using embeddings in production or safety-sensitive contexts. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### not reported — `insufficient-evidence`

- Task: model-level comparison (checkpoint-scoped)
- Criteria: Evidence gap: No per-checkpoint benchmark or protocol-matching evaluation artifact was found in the inspected repository to support a task- and protocol-matched comparison for this exact revision.
- Rationale: The repository documents the model artifacts and cites the SapBERT paper but does not contain per-checkpoint benchmark tables or artifacts tying published numeric results to this specific revision; therefore a verified checkpoint-scoped comparison cannot be produced from the checked primary locators.
- Comparison conditions: Checked locators include the repository commit view, commit history, and README; the SapBERT paper (arXiv:2010.11784) provides method-level benchmarks but the repository does not tie those numbers to this exact checkpoint at the inspected locators.
- Evidence: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main, https://arxiv.org/abs/2010.11784

## Limitations and safety

### Limitations

- The repository commit and README present the model as SapBERT-style and trained with UMLS (English only) and indicate the use of microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext as the base model in commit metadata, which constrains the checkpoint to biomedical English-domain entity representations. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0
- Evidence gap: The inspected primary repository artifacts do not disclose an explicit model-weights license or a repository LICENSE file at the checked locators. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main
- Evidence gap: The inspected primary repository artifacts do not provide per-checkpoint benchmark tables or artifacts tying the SapBERT paper's numeric results to this specific revision at the checked locators. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0, https://arxiv.org/abs/2010.11784, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main

### Safety

- The repository metadata and commit message report the model was trained with UMLS (listed as the dataset) and that the model language tag is English; repository tags include 'biomedical' and 'lexical-semantics'. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0
- Evidence gap: The inspected primary repository artifacts do not report clinical-use approvals, certifications, PHI/data-handling guidance, or deployment safety guarantees for clinical settings at the checked locators. Sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md, https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### SapBERT repository tree view at commit d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0

- URL: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0
- Publisher: cambridgeltl / Hugging Face (repository view)
- Type: `repository`
- Primary because: Repository tree view at the exact commit revision verifies the revision exists and files present at that commit.
- Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (tree at commit d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0)
- Supports: Verifies the repository and file tree exist at the referenced revision.

### SapBERT canonical preprint (arXiv:2010.11784)

- URL: https://arxiv.org/abs/2010.11784
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical SapBERT paper preprint used to justify method-level claims cited by the repository.
- Scope: SapBERT method (paper)
- Supports: Method-level description and benchmarks for SapBERT (used for reproducing evaluations and method context).

### SapBERT repository commit d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0 (checkpoint metadata)

- URL: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0
- Publisher: cambridgeltl / Hugging Face (repository commit)
- Type: `repository`
- Primary because: Exact commit/revision referenced by the dossier; contains checkpoint-scoped metadata and tags.
- Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (commit d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0)
- Supports: Commit metadata indicates training with UMLS (2020AA) and base model microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext; repository tags for language and domain are present.

### SapBERT repository commit history (commits/main) indicating presence of config/tokenizer/vocab artifacts

- URL: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main
- Publisher: cambridgeltl / Hugging Face (repository)
- Type: `repository`
- Primary because: Commit history listing the files present at the referenced revision (config.json, tokenizer_config.json, vocab.txt, etc.).
- Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (commits/main view)
- Supports: Shows that config.json, tokenizer_config.json, vocab.txt and model weight files are present in the repository history at the referenced revision.

### SapBERT repository README.md (blame/main view)

- URL: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md
- Publisher: cambridgeltl / Hugging Face (repository file)
- Type: `repository`
- Primary because: Repository README providing usage guidance and a BibTeX citation to the SapBERT paper.
- Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (README blob)
- Supports: README includes a BibTeX citation to the SapBERT paper and advises using the [CLS] token as the representation.

### SapBERT repository vocab.txt (blame/main view)

- URL: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/vocab.txt
- Publisher: cambridgeltl / Hugging Face (repository file)
- Type: `repository`
- Primary because: Tokenizer vocabulary file present in the repository at the referenced revision.
- Scope: cambridgeltl/SapBERT-from-PubMedBERT-fulltext (vocab.txt blob)
- Supports: Presence of vocab.txt (tokenizer vocabulary) at the referenced revision.

### Exact official starting source declared by Forge

- URL: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: cambridgeltl-sapbert-pubmedbert-fulltext
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The inspected primary repository artifacts do not report an explicit model-weights license or a repository LICENSE file at the checked locators. Checked URLs: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0 , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main
- Evidence gap: The inspected primary repository artifacts do not provide a per-checkpoint benchmark table or artifact tying the SapBERT paper's numeric results to this exact revision. Checked URLs: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commit/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0 , https://arxiv.org/abs/2010.11784 , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main
- Evidence gap: The inspected primary repository artifacts do not explicitly state the tokenizer algorithm (WordPiece vs BPE vs SentencePiece) at the checked locators. Checked URLs: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0 , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/vocab.txt
- Evidence gap: The inspected primary repository artifacts do not disclose embedding dtype/precision (fp32/fp16) or whether embeddings are L2-normalized at the checked locators. Checked URLs: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0 , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md
- Evidence gap: The inspected primary repository artifacts do not document a canonical, ordered preprocessing pipeline (normalization, lowercasing, punctuation handling) or explicit input-validation rules at the checked locators. Checked URLs: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/tree/d22b6fba9ffec8283c6cb9d8b9ff04b86eb02cc0
- Evidence gap: The inspected primary repository artifacts do not provide runtime output data type/format (Python list, numpy array, tensor) or a truncation/chunking policy for inputs longer than model position capacity at the checked locators. Checked URLs: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/blame/main/README.md , https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext/commits/main

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
