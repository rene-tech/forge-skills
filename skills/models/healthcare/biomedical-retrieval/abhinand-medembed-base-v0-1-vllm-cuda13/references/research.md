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

- Research key: `huggingface-co-abhinand-medembed-base-v0-1-3b6aaeb88f`
- Independent audit: `revised`
- Researched: `2026-08-06T10:31:33.479820+00:00`

Primary sources inspected: the Hugging Face model page for MedEmbed-base-v0.1, the project README in the canonical GitHub repository, the checkpoint config.json blob, and the canonical preprint(s) reporting benchmarks. The checkpoint config.json documents a BERT-based encoder (BertModel) with hidden_size 768, intermediate_size 3072, 12 hidden layers, 12 attention heads, vocab_size 30522, max_position_embeddings 512, hidden_act gelu; torch_dtype and an immutable revision string are not reported in the primary files inspected. A paper-level label "MedEmbed Base" appears in the canonical arXiv Table 5 reporting retrieval metrics (per-dataset rows and a 16-task aggregate mean), but the table entries do not explicitly map that paper label to the exact Hugging Face checkpoint identifier MedEmbed-base-v0.1; therefore checkpoint-scoped attribution of those table rows is not verified. The checkpoint-level total parameter count is reported as 110 million parameters in a canonical arXiv source. Tokenizer configuration files and explicit tokenizer parameters (tokenizer_config.json, tokenizer class, do_lower_case, model_max_length) were not present in the inspected primary files; pooling/post-processing instructions for producing final embedding vectors are not documented in the checkpoint primary files. No explicit model-weights license statement was found in the inspected primary sources.

## Identity

- Upstream name: MedEmbed-base
- Checkpoint/version: MedEmbed-base-v0.1
- Immutable revision: not reported
- Parameter scale: 110 million parameters
- Architecture/head: BertModel; hidden_size=768; intermediate_size=3072; num_hidden_layers=12; num_attention_heads=12; vocab_size=30522; max_position_embeddings=512; hidden_act=gelu; use_cache=true; torch_dtype=not reported
- License: code: not reported; model-weights: not reported
- Evidence: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md, https://huggingface.co/abhinand/MedEmbed-base-v0.1/blob/101a3f63286f44b661f5caf1491dbe7f3468b064/config.json, https://arxiv.org/html/2412.15258v1

## Selection

### Recommended

- **Biomedical information retrieval and semantic search on medical literature and clinical text (assistive use)** — The Hugging Face model page and repository README describe MedEmbed as an embedding family fine-tuned for medical and clinical data for retrieval/semantic-search tasks; the canonical paper reports retrieval-oriented benchmarking for a paper-labeled MedEmbed Base.
  Scope: MedEmbed-base-v0.1 (Hugging Face checkpoint and repo metadata) and paper-level MedEmbed Base (Table 5)
  Evidence: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md, https://arxiv.org/html/2507.19407v2

### Conditional

- **Clinical decision support (assistive only; requires expert review and downstream validation)** — Requires human expert review and validation prior to any clinical action; model documentation frames MedEmbed as an assistive retrieval/embedding tool rather than a replacement for clinical judgment.
  Scope: MedEmbed-base-v0.1
  Evidence: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md

### Avoid

- **Unvalidated clinical diagnoses or direct clinical decision-making without expert oversight** — Model documentation cautions that the MedEmbed family is an assistive tool and emphasizes ethical considerations; the model card and README do not present the model as a substitute for clinical judgment.
  Scope: MedEmbed-base-v0.1
  Evidence: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md

## Input preparation

### Semantic inputs

- Inputs are plain text strings to be tokenized and consumed as text for embedding generation. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1

### Accepted formats

- Plain text strings (tokenizer input) are the accepted input format; no structured JSON input schema is documented in the inspected primary sources. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1

### Preprocessing

- Model architecture is BERT-based (model_type: bert) as specified in config.json; tokenizer-specific settings (tokenizer class, do_lower_case, model_max_length) are not specified in the primary files inspected. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1/blob/101a3f63286f44b661f5caf1491dbe7f3468b064/config.json, https://huggingface.co/abhinand/MedEmbed-base-v0.1
- Evidence gap: The repository/config files inspected do not contain an explicit tokenizer_config.json or tokenizer class settings that document do_lower_case or model_max_length for this checkpoint. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md

### Pre-submit validation

- No explicit per-checkpoint input validation rules (semantic checks, bounds) are documented beyond the tokenizer/architecture configuration present in the repository files inspected. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1/blob/101a3f63286f44b661f5caf1491dbe7f3468b064/config.json, https://github.com/abhinand5/MedEmbed/blob/main/README.md

### Task-specific formatting

- Evidence gap: No explicit task-formatting templates, paired-input order, or pooling instructions for producing final embedding vectors are documented in the checkpoint model card or repository README inspected for this exact checkpoint. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md

## Output interpretation

### Outputs

- Embedding vectors with dimension 768 (derived from hidden_size in config.json) are the model's core output representation per input. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1/blob/101a3f63286f44b661f5caf1491dbe7f3468b064/config.json

### Interpretation

- Embeddings are intended for similarity and search tasks (semantic retrieval); the inspected primary sources do not document additional official scoring, normalization, or distance semantics for the raw embedding vectors. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://arxiv.org/html/2507.19407v2

### Post-inference validation

- Evidence gap: No documented post-inference pooling, normalization, or validation steps for producing final retrieval scores or normalized embeddings are present in the primary files examined. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md

## Public benchmarks

### Biomedical information retrieval

- Dataset/split: PubMed / not reported
- Metric/value: evaluation score (as reported in Table 5) / 0.89-0.90 (`higher-is-better`)
- Model scope: MedEmbed Base (paper label in Table 5)
- Conditions: As reported in Table 5 of the canonical arXiv preprint; detailed per-dataset splits and evaluation protocol are not provided in the table locator inspected.
- Source: https://arxiv.org/html/2507.19407v2
- Locator: Table 5 (PubMed row)
- Caveat: Evidence gap: The Table 5 entry is for a model labeled "MedEmbed Base" in the paper; the primary source does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locator inspected.
- Caveat: Exact per-dataset splits and full evaluation protocol are not reported in Table 5.

### Biomedical information retrieval

- Dataset/split: BioRxiv / not reported
- Metric/value: evaluation score (as reported in Table 5) / 0.89-0.90 (`higher-is-better`)
- Model scope: MedEmbed Base (paper label in Table 5)
- Conditions: As reported in Table 5 of the canonical arXiv preprint; detailed per-dataset splits and evaluation protocol are not provided in the table locator inspected.
- Source: https://arxiv.org/html/2507.19407v2
- Locator: Table 5 (BioRxiv row)
- Caveat: Evidence gap: The Table 5 entry is for a model labeled "MedEmbed Base" in the paper; the primary source does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locator inspected.
- Caveat: Exact per-dataset splits and full evaluation protocol are not reported in Table 5.

### Biomedical information retrieval

- Dataset/split: MIMIC-IV / not reported
- Metric/value: evaluation score (as reported in Table 5) / 0.61 (`higher-is-better`)
- Model scope: MedEmbed Base (paper label in Table 5)
- Conditions: As reported in Table 5 of the canonical arXiv preprint; detailed per-dataset splits and evaluation protocol are not provided in the table locator inspected.
- Source: https://arxiv.org/html/2507.19407v2
- Locator: Table 5 (MIMIC‑IV row)
- Caveat: Evidence gap: The Table 5 entry is for a model labeled "MedEmbed Base" in the paper; the primary source does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locator inspected.
- Caveat: Exact per-dataset splits and full evaluation protocol are not reported in Table 5.

### Biomedical information retrieval

- Dataset/split: Clinical Trials / not reported
- Metric/value: evaluation score (as reported in Table 5) / 0.81 (`higher-is-better`)
- Model scope: MedEmbed Base (paper label in Table 5)
- Conditions: As reported in Table 5 of the canonical arXiv preprint; detailed per-dataset splits and evaluation protocol are not provided in the table locator inspected.
- Source: https://arxiv.org/html/2507.19407v2
- Locator: Table 5 (Clinical Trials row)
- Caveat: Evidence gap: The Table 5 entry is for a model labeled "MedEmbed Base" in the paper; the primary source does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locator inspected.
- Caveat: Exact per-dataset splits and full evaluation protocol are not reported in Table 5.

### Biomedical information retrieval

- Dataset/split: MedRxiv / not reported
- Metric/value: evaluation score (as reported in Table 5) / 0.74 (`higher-is-better`)
- Model scope: MedEmbed Base (paper label in Table 5)
- Conditions: As reported in Table 5 of the canonical arXiv preprint; detailed per-dataset splits and evaluation protocol are not provided in the table locator inspected.
- Source: https://arxiv.org/html/2507.19407v2
- Locator: Table 5 (MedRxiv row)
- Caveat: Evidence gap: The Table 5 entry is for a model labeled "MedEmbed Base" in the paper; the primary source does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locator inspected.
- Caveat: Exact per-dataset splits and full evaluation protocol are not reported in Table 5.

### Embedding quality (aggregate)

- Dataset/split: Unknown (16-task benchmark aggregate) / not reported
- Metric/value: mean score (across 16 tasks, as reported in Table 5) / 0.578 (`higher-is-better`)
- Model scope: MedEmbed Base (paper label in Table 5)
- Conditions: As reported in Table 5 of the canonical arXiv preprint; the paper reports an aggregate mean across 16 tasks but does not document the per-task splits/protocols in the Table 5 locator inspected.
- Source: https://arxiv.org/html/2507.19407v2
- Locator: Table 5 (Overall mean across 16 tasks)
- Caveat: Evidence gap: The Table 5 aggregate is attributed to a model labeled "MedEmbed Base" in the paper; the primary source does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locator inspected.
- Caveat: Evidence gap: Per-task splits and detailed evaluation protocol for the 16-task aggregate are not reported in the Table 5 locator.

## Comparisons

### other_models_listed_in_paper — `insufficient-evidence`

- Task: Biomedical information retrieval — embedding retrieval comparisons reported in the paper
- Criteria: Protocol-identical, checkpoint-scoped head-to-head embedding retrieval comparison on the same datasets and splits
- Rationale: The canonical arXiv Table 5 reports scores for a model labeled "MedEmbed Base" and for other listed models/encoders, but the table entries do not document explicit mapping from paper labels to the exact Hugging Face checkpoint identifier MedEmbed-base-v0.1 or per-dataset split/protocol details; therefore a protocol-identical, checkpoint-scoped selection cannot be established from the inspected primary sources.
- Comparison conditions: As reported in Table 5 of the canonical arXiv preprint; per-checkpoint identifiers and per-dataset splits are not provided in the table locator inspected.
- Evidence: https://arxiv.org/html/2507.19407v2, https://huggingface.co/abhinand/MedEmbed-base-v0.1

## Limitations and safety

### Limitations

- MedEmbed-base-v0.1 is focused on medical/clinical text and may not generalize to non-medical domains. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md
- Potential dataset-driven biases and ethical considerations are noted in the model documentation; the model is framed as an assistive tool rather than a replacement for human expertise. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md
- Evidence gap: Exact total parameter count per-checkpoint metadata and an immutable repository revision string are not reported in the checkpoint config.json or repository files inspected beyond the paper-level report; parameter-scale reporting in primary files is limited to the canonical arXiv listing. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://arxiv.org/html/2412.15258v1

### Safety

- Model documentation indicates the model should be used as an assistive tool in medical information retrieval and not as a substitute for clinical judgment. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md
- Model authors note potential dataset-driven biases and ethical considerations; deployments should include expert oversight and consider those risks. Sources: https://huggingface.co/abhinand/MedEmbed-base-v0.1, https://github.com/abhinand5/MedEmbed/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MedEmbed-base-v0.1 model page

- URL: https://huggingface.co/abhinand/MedEmbed-base-v0.1
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Canonical Hugging Face model page for the MedEmbed-base-v0.1 checkpoint; provides the model card and links to repository files used in dossier claims.
- Scope: MedEmbed-base-v0.1
- Supports: model card statements about intended use
- Supports: links to repository and model files
- Supports: intended input modality and recommended uses

### MedEmbed repository README

- URL: https://github.com/abhinand5/MedEmbed/blob/main/README.md
- Publisher: GitHub
- Type: `repository`
- Primary because: Canonical project repository README cited for README-level statements about intended use, training artifacts, and links to checkpoint downloads.
- Scope: MedEmbed-base-v0.1
- Supports: intended use statements
- Supports: training/collection notes
- Supports: links to checkpoint downloads

### MedEmbed-base-v0.1 config.json (blob at commit)

- URL: https://huggingface.co/abhinand/MedEmbed-base-v0.1/blob/101a3f63286f44b661f5caf1491dbe7f3468b064/config.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Primary file specifying model architecture fields (hidden_size, num_hidden_layers, num_attention_heads, vocab_size, max_position_embeddings, hidden_act, use_cache when present).
- Scope: MedEmbed-base-v0.1/config.json
- Supports: hidden_size
- Supports: num_hidden_layers
- Supports: num_attention_heads
- Supports: vocab_size
- Supports: max_position_embeddings
- Supports: hidden_act
- Supports: model_type
- Supports: architecture details

### ArXiv preprint (HTML) reporting benchmarks (Table 5)

- URL: https://arxiv.org/html/2507.19407v2
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint used to verify numeric benchmark claims reported in Table 5 for a paper-labeled "MedEmbed Base".
- Scope: MedEmbed Base (paper-level label in Table 5)
- Supports: benchmarks_pubmed
- Supports: benchmarks_biorxiv
- Supports: benchmarks_mimic
- Supports: benchmarks_clinical_trials
- Supports: benchmarks_medrxiv
- Supports: mean_score

### medRxiv preprint (PDF) referenced in findings

- URL: https://medrxiv.org/content/10.1101/2025.08.08.25333318v1.full.pdf
- Publisher: medRxiv
- Type: `paper`
- Primary because: Primary preprint PDF referenced by the research findings; used to corroborate experimental summaries noted in repository/paper-level documentation.
- Scope: MedEmbed experiments reported in medRxiv preprint
- Supports: additional experimental context and claims referenced in the research findings

### ArXiv preprint (parameter-scale reporting)

- URL: https://arxiv.org/html/2412.15258v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv source reporting checkpoint parameter-scale statements (used to verify the reported parameter count for MedEmbed-Base-v0.1).
- Scope: MedEmbed-Base-v0.1 (parameter-scale claim)
- Supports: parameterScale

## Evidence gaps

- Evidence gap: The canonical arXiv Table 5 reports scores for a model labeled "MedEmbed Base" but does not explicitly name the exact checkpoint identifier (e.g., MedEmbed-base-v0.1) in the Table 5 locators inspected; therefore checkpoint-scoped attribution is not fully verified from the paper.
- Evidence gap: Per-dataset splits and full evaluation protocol details for Table 5 benchmark entries (PubMed, BioRxiv, MIMIC-IV, Clinical Trials, MedRxiv and the 16-task aggregate) are not provided in the Table 5 locators inspected in the canonical arXiv HTML source.
- Evidence gap: Exact torch_dtype, an immutable repository revision string, and an explicit tokenizer_config.json/tokenizer class (do_lower_case, model_max_length) for this checkpoint were not found in the inspected primary files; tokenizer-level preprocessing details are therefore not verified.
- Evidence gap: No explicit model-weights license statement was located in the inspected primary sources; code vs weights licensing distinction is not documented in the available primary files.
- Evidence gap: No documented pooling/post-processing strategy (pooling layer, normalization, or explicit pooling instructions) for producing final embedding vectors for this checkpoint is present in the inspected primary files.
- Evidence gap: Direct, protocol-identical, checkpoint-scoped head-to-head comparisons between the exact MedEmbed-base-v0.1 checkpoint and other named alternatives on identical datasets/splits/protocols are not present in the inspected primary sources; comparisons are therefore labeled insufficient-evidence.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 30 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-vllm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
