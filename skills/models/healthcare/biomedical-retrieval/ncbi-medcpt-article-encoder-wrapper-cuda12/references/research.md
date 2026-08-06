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

- Research key: `huggingface-co-ncbi-medcpt-article-encoder-d189d60deb`
- Independent audit: `revised`
- Researched: `2026-08-06T12:56:26.974240+00:00`

Checkpoint-scoped dossier for the Hugging Face checkpoint ncbi/MedCPT-Article-Encoder ("MedCPT-Article-Encoder"). Primary sources show MedCPT provides separate query/article encoders trained with a contrastive pre-training objective on large-scale PubMed search-log query-article pairs and is intended to produce embeddings for dense retrieval of biomedical articles (title+abstract). The upstream paper (arXiv/Bioinformatics) reports numeric retrieval metrics for the MedCPT article encoder (DEnc) in Table 2 (e.g., RELISH primary metric scores for several parameter scales). Tokenizer configuration for the Article Encoder is available in the repository (BertTokenizer, truncation strategy and related fields). The model and repository LICENSE files indicate the work is a United States Government Work placed in the public domain. Several operational and format-level details required for a complete serving contract are not stated in the inspected primary files (see evidenceGaps): embedding dimensionality, explicit pooling/aggregation rules, embedding normalization semantics, explicit max sequence length, and an immutable checkpoint revision identifier are not reported in the inspected primary sources.

## Identity

- Upstream name: MedCPT
- Checkpoint/version: MedCPT-Article-Encoder
- Immutable revision: not reported
- Parameter scale: 330M
- Architecture/head: Dual-encoder Transformer with separate Query Encoder and Article Encoder; trained with a contrastive pre-training objective on large-scale PubMed query‑article pairs.
- License: United States Government Work (public domain)
- Evidence: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589, https://pubmed.ncbi.nlm.nih.gov/37930897, https://github.com/ncbi/MedCPT, https://huggingface.co/ncbi/MedCPT-Article-Encoder/blame/main/LICENSE, https://github.com/ncbi/MedCPT/blob/main/LICENSE

## Selection

### Recommended

- **Dense retrieval / semantic search of biomedical articles (title + abstract) using article embeddings** — The MedCPT Article Encoder is described in the model card/repository as generating embeddings of biomedical texts that can be used for semantic search (dense retrieval) and the Article Encoder expects title and abstract inputs.
  Scope: MedCPT-Article-Encoder
  Evidence: https://huggingface.co/ncbi/MedCPT-Article-Encoder
- **Zero-shot biomedical information retrieval evaluation (as reported for the article encoder variant DEnc)** — The original MedCPT paper reports zero-shot information retrieval evaluations and numeric results for the MedCPT article encoder (DEnc) on retrieval benchmarks (e.g., RELISH) in Table 2.
  Scope: MedCPT article encoder (DEnc) as reported in the paper
  Evidence: https://arxiv.org/pdf/2307.00589, https://pubmed.ncbi.nlm.nih.gov/37930897

### Conditional


### Avoid

- **Direct clinical diagnostic use without professional oversight** — Evidence gap: Primary sources inspected (model card, paper, and repository) do not present evidence that the checkpoint is clinically validated for direct diagnostic decision-making or provide clinical-validation guidance for unsupervised diagnostic use.
  Scope: MedCPT-Article-Encoder
  Evidence: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589, https://pubmed.ncbi.nlm.nih.gov/37930897

## Input preparation

### Semantic inputs

- Title and abstract text of biomedical articles (intended article-side inputs). Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder

### Accepted formats

- Plain text title and plain text abstract fields (text inputs). Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder

### Preprocessing

- Tokenizer class configured as BertTokenizer per tokenizer_config.json. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blob/main/tokenizer_config.json
- Tokenization parameters set in tokenizer_config.json: stride = 0, strip_accents = null, tokenize_chinese_chars = true, truncation_side = 'right', truncation_strategy = 'longest_first', unk_token = '[UNK]'. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blob/main/tokenizer_config.json

### Pre-submit validation

- Evidence gap: The inspected tokenizer_config.json does not specify a max sequence length (max_length) or padding-length policy; primary-source location checked: tokenizer_config.json did not include max_length or explicit padding rules. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blob/main/tokenizer_config.json
- Evidence gap: The repository and model card do not specify explicit trimming/pooling/padding rules for combined title+abstract inputs; these details were not found in the inspected primary sources. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://github.com/ncbi/MedCPT

### Task-specific formatting

- Evidence gap: Primary sources do not provide an explicit prompt template or paired-input ordering specification for model calls beyond stating that article inputs are title+abstract. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://github.com/ncbi/MedCPT

## Output interpretation

### Outputs

- The model emits dense vector embeddings for biomedical text (article representations) intended for semantic search / dense retrieval. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder
- Evidence gap: Primary sources do not state the embedding dimensionality (vector length) produced by the Article Encoder. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589
- Evidence gap: Primary sources do not state whether output embeddings are L2-normalized or otherwise normalized, nor do they explicitly state the intended similarity scoring function (e.g., dot-product vs. cosine). Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://github.com/ncbi/MedCPT

### Interpretation

- Embeddings are intended for use in semantic similarity and dense retrieval tasks (embedding comparison yields relevance signals). Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder
- Evidence gap: No primary-source specification was found that defines the numeric range, calibration, or score-to-probability mapping for similarity scores produced when embeddings are compared. Sources: https://arxiv.org/pdf/2307.00589, https://huggingface.co/ncbi/MedCPT-Article-Encoder

### Post-inference validation

- Evidence gap: The inspected primary sources do not provide post-inference quality-control checks or recommended sanity tests (e.g., embedding-vector magnitude bounds, near-duplicate detection thresholds). Sources: https://github.com/ncbi/MedCPT, https://huggingface.co/ncbi/MedCPT-Article-Encoder

## Public benchmarks

### Article retrieval / relevance (zero-shot evaluation)

- Dataset/split: RELSIH (RELISH) primary metric / not reported
- Metric/value: primary RELISH metric (as reported in Table 2) / 0.709 (`higher-is-better`)
- Model scope: MedCPT article encoder (DEnc), 330M parameters (as reported in paper Table 2)
- Conditions: Reported in Table 2 of the MedCPT paper (arXiv:2307.00589). See Table 2 for evaluation protocol and exact metric definition.
- Source: https://arxiv.org/pdf/2307.00589
- Locator: Table 2
- Caveat: Table 2 reports multiple MedCPT variants (330M, 220M retriever-only, 110M PubMedBERT baseline); ensure the reported parameter scale matches the desired checkpoint variant before comparison.

### Article retrieval / relevance (zero-shot evaluation) - retriever-only variant

- Dataset/split: RELSIH (RELISH) primary metric / not reported
- Metric/value: primary RELISH metric (as reported in Table 2) / 0.697 (`higher-is-better`)
- Model scope: MedCPT retriever-only variant, 220M parameters (as reported in paper Table 2)
- Conditions: Reported in Table 2 of the MedCPT paper (arXiv:2307.00589).
- Source: https://arxiv.org/pdf/2307.00589
- Locator: Table 2
- Caveat: This row refers to a different reported parameter-scale variant (220M) rather than the 330M article encoder checkpoint; confirm checkpoint identity before attributing this numeric result.

### Article retrieval / relevance (ablative baseline)

- Dataset/split: RELSIH (RELISH) primary metric / not reported
- Metric/value: primary RELISH metric (as reported in Table 2) / 0.059 (`higher-is-better`)
- Model scope: PubMedBERT baseline (110M parameters) reported in paper Table 2
- Conditions: Reported in Table 2 of the MedCPT paper (arXiv:2307.00589).
- Source: https://arxiv.org/pdf/2307.00589
- Locator: Table 2
- Caveat: This result is for a baseline (PubMedBERT) and not the MedCPT Article Encoder checkpoint.

## Comparisons

### SPECTER — `prefer-this`

- Task: Article similarity / retrieval (RELISH primary metric)
- Criteria: Reported primary RELISH metric in Table 2 of the MedCPT paper where the MedCPT article encoder (DEnc) score exceeds SPECTER's reported score on the same table/metric.
- Rationale: The MedCPT paper reports that the MedCPT article encoder outperforms SPECTER on the RELISH article similarity task (see Table 2).
- Comparison conditions: Protocol and dataset as used in Table 2 of arXiv:2307.00589. Confirm SPECTER row and exact protocol in Table 2 when comparing.
- Evidence: https://arxiv.org/pdf/2307.00589

### SciNCL — `prefer-this`

- Task: Article similarity / retrieval (RELISH primary metric)
- Criteria: Reported primary RELISH metric in Table 2 of the MedCPT paper where the MedCPT article encoder (DEnc) score exceeds SciNCL's reported score on the same table/metric.
- Rationale: The MedCPT paper reports that the MedCPT article encoder outperforms SciNCL on the RELISH article similarity task (see Table 2).
- Comparison conditions: Protocol and dataset as used in Table 2 of arXiv:2307.00589. Confirm SciNCL row and exact protocol in Table 2 when comparing.
- Evidence: https://arxiv.org/pdf/2307.00589

## Limitations and safety

### Limitations

- Evidence gap: The inspected primary sources (model card, repository, and paper) do not provide a dedicated, explicit list of model limitations (for example, known failure modes, bias analyses, or domain-coverage limits) for the Article Encoder checkpoint. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589, https://github.com/ncbi/MedCPT

### Safety

- The model and repository LICENSE files indicate the work is a United States Government Work and is placed in the public domain; there are no usage restrictions in the LICENSE files for reuse. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blame/main/LICENSE, https://github.com/ncbi/MedCPT/blob/main/LICENSE
- Evidence gap: The inspected primary sources do not provide explicit safety, privacy, human-subjects, clinical-use, or data-handling guidance for deploying the Article Encoder in sensitive or clinical contexts. Sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589, https://github.com/ncbi/MedCPT

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MedCPT-Article-Encoder model card (Hugging Face)

- URL: https://huggingface.co/ncbi/MedCPT-Article-Encoder
- Publisher: Hugging Face (ncbi)
- Type: `model-card`
- Primary because: Official Hugging Face model card for the ncbi/MedCPT-Article-Encoder checkpoint; provides model description, intended use, and links to repository.
- Scope: MedCPT-Article-Encoder model card and assets on Hugging Face
- Supports: MedCPT generates embeddings of biomedical texts that can be used for semantic search (dense retrieval).
- Supports: The repository hosts the MedCPT Article Encoder.
- Supports: The MedCPT Article Encoder expects as input the title and abstract of a biomedical article.
- Supports: The MedCPT model card lists three primary use cases.

### MedCPT paper (arXiv PDF)

- URL: https://arxiv.org/pdf/2307.00589
- Publisher: arXiv
- Type: `paper`
- Primary because: Original MedCPT preprint/paper reporting architecture, training objective, pretraining data scale, and numeric retrieval results referenced for the article encoder (DEnc).
- Scope: MedCPT family; paper-reported article encoder (DEnc) results and descriptions
- Supports: The MedCPT article encoder (DEnc) outperforms SPECTER and SciNCL on the RELISH article similarity task (reported in Table 2).
- Supports: MedCPT (330M parameters) achieved a score of 0.709 on the primary RELISH metric reported in Table 2.
- Supports: MedCPT (retriever-only, 220M parameters) achieved a score of 0.697 on the primary RELISH metric reported in Table 2.
- Supports: MedCPT without contrastive pre‑training (PubMedBERT, 110M parameters) achieved a score of 0.059 on the primary RELISH metric reported in Table 2.
- Supports: The MedCPT article encoder was evaluated on the SciDocs benchmark framework.

### MedCPT published article (PubMed / Bioinformatics)

- URL: https://pubmed.ncbi.nlm.nih.gov/37930897
- Publisher: PubMed / Bioinformatics (publication record)
- Type: `paper`
- Primary because: Canonical bibliographic record for the published MedCPT article (Bioinformatics); links the preprint and provides official publication metadata.
- Scope: Published MedCPT study
- Supports: The article titled 'MedCPT: Contrastive Pre-trained Transformers with large-scale PubMed search logs for zero-shot biomedical information retrieval' was published in Bioinformatics and has PMID/PMCID metadata.

### MedCPT GitHub repository

- URL: https://github.com/ncbi/MedCPT
- Publisher: GitHub (ncbi)
- Type: `repository`
- Primary because: Official code and repository for MedCPT maintained by the authors/NCBI; contains training and evaluation code relevant to the family.
- Scope: MedCPT repository (training and evaluation code, scripts, and LICENSE)
- Supports: The GitHub repository for MedCPT is https://github.com/ncbi/MedCPT.

### MedCPT Article-Encoder tokenizer configuration (tokenizer_config.json)

- URL: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blob/main/tokenizer_config.json
- Publisher: Hugging Face (ncbi)
- Type: `repository`
- Primary because: Tokenizer configuration file in the official Hugging Face model repository for the Article Encoder; provides tokenizer class and tokenization-related fields.
- Scope: MedCPT-Article-Encoder repository files (tokenizer config)
- Supports: The tokenizer configuration uses the class 'BertTokenizer'.
- Supports: The tokenizer configuration sets 'stride' to 0.
- Supports: The tokenizer configuration sets 'strip_accents' to null.
- Supports: The tokenizer configuration sets 'tokenize_chinese_chars' to true.
- Supports: The tokenizer configuration sets 'truncation_side' to 'right'.
- Supports: The tokenizer configuration sets 'truncation_strategy' to 'longest_first'.
- Supports: The tokenizer configuration sets the unknown token (unk_token) to '[UNK]'.

### MedCPT Article-Encoder LICENSE (Hugging Face repository view/blame)

- URL: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blame/main/LICENSE
- Publisher: Hugging Face (ncbi)
- Type: `repository`
- Primary because: LICENSE file as presented in the Hugging Face repository view; states the licensing/rights status for the repository content hosted there.
- Scope: MedCPT-Article-Encoder repository LICENSE file
- Supports: The LICENSE file states the software/database is a United States Government Work and is in the public domain.
- Supports: The National Library of Medicine and the U.S. Government have placed no restriction on the use or reproduction of the software.

### MedCPT GitHub LICENSE (repository)

- URL: https://github.com/ncbi/MedCPT/blob/main/LICENSE
- Publisher: GitHub (ncbi)
- Type: `repository`
- Primary because: LICENSE file in the official GitHub repository for MedCPT; confirms licensing statement for code/repository.
- Scope: MedCPT GitHub repository LICENSE file
- Supports: The LICENSE file states the software/database is a United States Government Work and is in the public domain.

## Evidence gaps

- Embedding dimensionality (vector length) for MedCPT-Article-Encoder: not stated in inspected primary sources (checked Hugging Face model card and arXiv paper). See: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589
- Pooling / aggregation method for token-level outputs -> final embedding (e.g., CLS pooling, mean pooling): not specified in inspected primary sources (checked repository and model card). See: https://github.com/ncbi/MedCPT, https://huggingface.co/ncbi/MedCPT-Article-Encoder
- Embedding normalization semantics and intended similarity scoring function (dot-product vs. cosine) are not specified in inspected primary sources. See: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://github.com/ncbi/MedCPT
- Max sequence length (max_length) and explicit padding policy are not present in tokenizer_config.json or other inspected files. See: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blob/main/tokenizer_config.json
- Immutable checkpoint revision identifier (commit hash or model snapshot id) for the published MedCPT-Article-Encoder checkpoint is not reported in the inspected model card or paper. See: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://arxiv.org/pdf/2307.00589
- Explicit, dedicated safety, privacy, clinical-use, or data-handling guidance for deploying the Article Encoder in sensitive contexts: not found in inspected primary sources. See: https://huggingface.co/ncbi/MedCPT-Article-Encoder, https://github.com/ncbi/MedCPT, https://arxiv.org/pdf/2307.00589

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 36 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property inputPreparation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property reason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: unexpected property conditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2307.00589 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10627406 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/ncbi/MedCPT Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder/blob/main/tokenizer_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder/commits/main/LICENSE Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs is empty without a section-specific evidence gap: $.inputPreparation.semanticInputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
