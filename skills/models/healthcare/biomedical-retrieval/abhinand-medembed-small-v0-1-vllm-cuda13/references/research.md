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

- Research key: `huggingface-co-abhinand-medembed-small-v0-1-d1bc68419f`
- Independent audit: `revised`
- Researched: `2026-08-06T11:05:25.811790+00:00`

I inspected the primary Hugging Face model card for abhinand/MedEmbed-small-v0.1, the project GitHub repository README, and the canonical preprint PDF. The Hugging Face model card and the repository indicate that MedEmbed is a family of embedding models fine-tuned specifically for medical and clinical data and provide usage/download pointers for the v0.1 family (including MedEmbed-small-v0.1). The project README lists v0.1 download links and names benchmark suites used for evaluation but does not provide checkpoint-scoped numeric retrieval tables in the inspected README content. The preprint provides family-level context about embedding uses and a statement that domain-specific embedding models such as MedEmbed are constrained by a maximum context length of 512 tokens. Multiple checkpoint-scoped artifacts required for a fully detailed dossier (tokenizer config files, explicit pooling implementation/config, parameter count, checkpoint-scoped license declaration on the Hugging Face upload, immutable file checksums tying the HF-hosted artifact to a repository commit, checkpoint-scoped numeric retrieval metric rows, PHI de-identification statements, and runnable notebooks demonstrating a RAG pipeline using the exact HF checkpoint) were not reported in the inspected primary sources and are recorded as evidence gaps below.

## Identity

- Upstream name: not reported
- Checkpoint/version: MedEmbed-small-v0.1
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Embedding model fine-tuned for medical/clinical text (sentence-/sentence-transformer-style embeddings) as described for the MedEmbed family
- License: not reported
- Evidence: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

## Selection

### Recommended

- **Medical and clinical information retrieval (semantic search over medical text)** — The Hugging Face model card and the project README describe MedEmbed as embedding models fine-tuned for medical/clinical data and present usage guidance for embedding extraction, supporting retrieval-oriented use.
  Scope: MedEmbed-small-v0.1
  Evidence: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed
- **Embedding extraction for retrieval-augmented pipelines (retrieval encoder only, requiring downstream validation)** — Project materials and the model card present MedEmbed as embedding models intended for retrieval/semantic-search workflows; they show family-level training and usage orientation toward embedding extraction.
  Scope: MedEmbed-small-v0.1 (embedding-only checkpoint)
  Evidence: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed

### Conditional

- **Use inside research or engineering RAG stacks (retrieval component only) with downstream validation** — Requires an independently validated downstream reader/reranker and system-level evaluation; primary sources present embedding-use framing but do not publish checkpoint-scoped end-to-end clinical validation or a runnable RAG notebook for the exact HF checkpoint.
  Scope: MedEmbed-small-v0.1 as retrieval encoder
  Evidence: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

### Avoid

- **Using MedEmbed-small-v0.1 as a standalone clinical diagnostic or decision-making tool without expert oversight** — The model-family materials and the Hugging Face model card frame MedEmbed as embedding/retrieval aids and explicitly present the model as a tool to assist rather than replace human expertise in medical decision-making.
  Scope: MedEmbed-small-v0.1
  Evidence: https://huggingface.co/abhinand/MedEmbed-small-v0.1

## Input preparation

### Semantic inputs

- Plain text strings (sentences or medical text) intended for feature-extraction/embedding pipelines. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1

### Accepted formats

- Plain text input for embedding extraction calls (typical sentence-transformers-style usage). Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1

### Preprocessing

- Primary usage examples and family-oriented training descriptions indicate embedding extraction flows; exact tokenizer configuration and tokenizer files for the checkpoint were not reported in the inspected sources. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed
- Evidence gap: The inspected primary sources do not report exact tokenizer files/config (tokenizer_class, tokenizer.json, vocab/merges, special_tokens_map, normalization/tokenization rules, or explicit max token length) for the abhinand/MedEmbed-small-v0.1 checkpoint. I checked: https://huggingface.co/abhinand/MedEmbed-small-v0.1 (model card) and https://github.com/abhinand5/MedEmbed (README and repository files) and https://arxiv.org/pdf/2505.13482 (paper). Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

### Pre-submit validation

- Evidence gap: The inspected primary sources do not publish explicit input-validation checks such as exact max tokens, truncation policy, sentence-splitting rules, or numeric bounds for abhinand/MedEmbed-small-v0.1. I inspected the model card, repository README, and the preprint. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

### Task-specific formatting

- No official task-specific prompt templates or paired-input ordering are provided for embedding extraction in the inspected model-card or README; inputs are presented as plain text for embedding extraction. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed

## Output interpretation

### Outputs

- Dense sentence embeddings intended for similarity-based retrieval and nearest-neighbor ranking (embedding encoder output). Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1

### Interpretation

- Similarity scores computed over dense embeddings (dot-product/cosine) are framed as ranking signals for retrieval tasks in the project materials. Sources: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1
- Evidence gap: The inspected primary sources do not provide canonical numeric thresholds or calibration procedures to map similarity scores to binary/decision outcomes for abhinand/MedEmbed-small-v0.1. I inspected the model card, repository README, and the preprint. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

### Post-inference validation

- Evidence gap: Post-inference validation checks, sanity bounds, or application-specific calibration guidelines for abhinand/MedEmbed-small-v0.1 are not reported in the inspected primary sources (model card, README, preprint). Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### abhinand/MedEmbed-base-v0.1 — `insufficient-evidence`

- Task: medical information retrieval — per-variant retrieval metrics
- Criteria: No protocol-matched, checkpoint-scoped head-to-head numeric table or figure was located in the inspected primary sources that attributes comparable numeric rows to both MedEmbed-small-v0.1 and MedEmbed-base-v0.1 under identical dataset/split/metric.
- Rationale: The repository README and model card discuss family-level evaluations and improvements versus base models but do not provide a single explicit numeric locator mapping both checkpoints under identical conditions in the inspected sources.
- Comparison conditions: Inspected README.md and the Hugging Face model card; no checkpoint-scoped numeric rows found for both checkpoints in a single table/figure.
- Evidence: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1

### abhinand/MedEmbed-large-v0.1 — `insufficient-evidence`

- Task: medical information retrieval — per-variant retrieval metrics
- Criteria: No protocol-matched, checkpoint-scoped head-to-head numeric table or figure was located in the inspected primary sources that attributes comparable numeric rows to both MedEmbed-small-v0.1 and MedEmbed-large-v0.1 under identical dataset/split/metric.
- Rationale: The repository README and model card present family-level claims but do not provide a single explicit numeric locator mapping both checkpoints under identical conditions in the inspected sources.
- Comparison conditions: Inspected README.md and the Hugging Face model card; no checkpoint-scoped numeric rows found for both checkpoints in a single table/figure.
- Evidence: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1

## Limitations and safety

### Limitations

- Model family and model card scope: MedEmbed is presented as a family of embedding models fine-tuned specifically for medical and clinical data; applicability outside this domain is not established in the inspected primary sources. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1
- Evidence gap: Exact tokenizer configuration files, tokenizer_class, vocabulary/merges file paths, special_tokens_map, normalization/tokenization rules, and max token lengths for abhinand/MedEmbed-small-v0.1 were not found in the inspected primary sources (model card, repository README, preprint). I inspected: README.md, model card, and the preprint PDF. Sources: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://arxiv.org/pdf/2505.13482
- Evidence gap: No canonical checkpoint-scoped locator for pooling implementation (CLS vs mean vs pooling head), output embedding dimensionality, or dtype (float32/float16) was found in the inspected primary sources (model card, README, preprint). Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482
- Evidence gap: No explicit LICENSE file path or authoritative license text tied to the Hugging Face checkpoint upload for abhinand/MedEmbed-small-v0.1 was located in the inspected Hugging Face model-card view; the repository contains a LICENSE but the model-card did not present a checkpoint-scoped license declaration in the inspected views. Sources: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1
- Evidence gap: No immutable artifact identifier (file-hash, model-file checksum, or git commit SHA explicitly tying the uploaded model file to a repository commit) was present in the inspected model-card or README content for abhinand/MedEmbed-small-v0.1. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed
- Evidence gap: No checkpoint-scoped numeric benchmark tables/figures attributing retrieval metrics (Recall/MRR/nDCG/Precision/MAP) specifically to abhinand/MedEmbed-small-v0.1 were present in the inspected primary sources; the README lists evaluated datasets but does not include numeric rows for the checkpoint. Sources: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1
- Evidence gap: No published PHI de-identification workflow, consent statements, or operational privacy safeguards specific to training data for abhinand/MedEmbed-small-v0.1 were found in the inspected primary sources (model card, repository README, preprint). Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://github.com/abhinand5/MedEmbed, https://arxiv.org/pdf/2505.13482

### Safety

- Model intended use and human oversight: The model-family materials and the MedEmbed-small-v0.1 model card present MedEmbed as embedding models for medical/clinical retrieval and frame the model as a tool to assist, not to replace, human expertise in medical decision-making. Sources: https://huggingface.co/abhinand/MedEmbed-small-v0.1
- Evidence gap: The inspected primary sources do not contain checkpoint-scoped statements describing PHI de-identification workflows, data consent, or other privacy safeguards tied specifically to the MedEmbed-small-v0.1 training data. Sources: https://github.com/abhinand5/MedEmbed, https://huggingface.co/abhinand/MedEmbed-small-v0.1, https://arxiv.org/pdf/2505.13482

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### abhinand/MedEmbed-small-v0.1 model card

- URL: https://huggingface.co/abhinand/MedEmbed-small-v0.1
- Publisher: Hugging Face (model author listing)
- Type: `model-card`
- Primary because: Official Hugging Face model page for the exact checkpoint; used to verify checkpoint name, intended use framing, and example usage references.
- Scope: MedEmbed-small-v0.1 model card
- Supports: MedEmbed is a family of embedding models fine-tuned specifically for medical and clinical data.
- Supports: Model-card intended-use framing that the model is an assistive retrieval/embedding tool and should not replace human expertise.
- Supports: Example usage and embedding-extraction orientation for the family/checkpoint.

### MedEmbed project repository (README.md)

- URL: https://github.com/abhinand5/MedEmbed
- Publisher: GitHub (project repository owner)
- Type: `repository`
- Primary because: Author-maintained project repository containing the README and links that list MedEmbed v0.1 model download entries and benchmark lists; used to verify repository-level training/evaluation claims and the presence of v0.1 download references.
- Scope: MedEmbed project repository and README (family-level artifacts, v0.1 links)
- Supports: Repository README lists model download links for version 0.1 including abhinand/MedEmbed-small-v0.1 and enumerates evaluated benchmark datasets used for the family.
- Supports: Project-level training descriptions and synthetic data generation pipeline assertions (family-level).

### Medembed: Medical-focused embedding models (arXiv preprint PDF)

- URL: https://arxiv.org/pdf/2505.13482
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint PDF referenced by the project; used to verify family-level descriptions and statements about embedding-use context and maximum context-length constraints mentioned for MedEmbed.
- Scope: MedEmbed family described in canonical preprint
- Supports: Paper describing MedEmbed family-level characteristics and use-cases for embeddings in RAG and retrieval.
- Supports: Statement that domain-specific embedding models such as MedEmbed are constrained by a maximum context length of 512 tokens (family-level).

## Evidence gaps

- Evidence gap: No explicit tokenizer files/config (tokenizer_class, tokenizer.json, vocab/merges, special_tokens_map, normalization/tokenization rules, or max token length) for abhinand/MedEmbed-small-v0.1 were reported in the inspected primary sources. I checked: https://huggingface.co/abhinand/MedEmbed-small-v0.1 (model card), https://github.com/abhinand5/MedEmbed (README.md/repository files), and https://arxiv.org/pdf/2505.13482 (preprint PDF).
- Evidence gap: No canonical checkpoint-scoped pooling implementation details (pooling type, pooling config file or code path, embedding dimensionality, or explicit dtype float32/float16) for abhinand/MedEmbed-small-v0.1 were reported in the inspected primary sources. I checked: model card, repository README, and preprint PDF at the URLs in the sources list.
- Evidence gap: No authoritative parameter count (parameter-scale) for abhinand/MedEmbed-small-v0.1 is specified in the inspected primary sources (model card, README, preprint).
- Evidence gap: No explicit LICENSE file path or authoritative license text tied to the Hugging Face checkpoint upload for abhinand/MedEmbed-small-v0.1 was located in the inspected Hugging Face model-card view; I inspected https://huggingface.co/abhinand/MedEmbed-small-v0.1 and https://github.com/abhinand5/MedEmbed (repository-level LICENSE exists but was not presented on the HF model-card in the inspected view).
- Evidence gap: No immutable artifact identifier mapping a file checksum to the uploaded model artifact for abhinand/MedEmbed-small-v0.1 was found in the inspected primary sources; I inspected https://huggingface.co/abhinand/MedEmbed-small-v0.1 (model card) and https://github.com/abhinand5/MedEmbed (repository) and did not find an explicit file-hash or commit-to-artifact checksum pairing.
- Evidence gap: No checkpoint-scoped numeric benchmark tables/figures attributing retrieval metrics (Recall, MRR, nDCG, MAP, Precision) specifically to abhinand/MedEmbed-small-v0.1 were present in the inspected primary sources; I inspected https://github.com/abhinand5/MedEmbed (README.md benchmark list) and https://huggingface.co/abhinand/MedEmbed-small-v0.1 (model card) and did not find numeric rows for the checkpoint.
- Evidence gap: No published PHI de-identification workflow, consent statements, or operational privacy safeguards specific to the training data for abhinand/MedEmbed-small-v0.1 were found in the inspected primary sources; I inspected the model card, repository README, and the preprint PDF.
- Evidence gap: No canonical runnable notebook or repository file path demonstrating a complete RAG/embedding pipeline using the exact abhinand/MedEmbed-small-v0.1 checkpoint was identified in the inspected primary sources (model card, README, preprint).
- Evidence gap: The inspected primary sources do not provide numeric thresholds, truncation policies, token limits, or calibration guidance for mapping similarity scores to decision thresholds for abhinand/MedEmbed-small-v0.1; I inspected the model card, repository README, and preprint PDF.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 23 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1] uses unapproved repository owner 'collections' for this exact model scope: $.sources[1] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'blog' for this exact model scope: $.sources[5] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://huggingface.co/blog/abhinand/medembed-finetuned-embedding-models-for-medical-ir Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'models' for this exact model scope: $.sources[8] uses unapproved repository owner 'models' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://huggingface.co/models?other=medical-embedding Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'aleksanderobuchowski' for this exact model scope: $.sources[12] uses unapproved repository owner 'aleksanderobuchowski' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'chrisolande' for this exact model scope: $.sources[13] uses unapproved repository owner 'chrisolande' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].value must contain a reported numeric result: $.benchmarks[3].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[1]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[2]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[3]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[4]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
