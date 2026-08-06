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

- Research key: `huggingface-co-baai-bge-large-en-v1-5-cb6f76e0da`
- Independent audit: `revised`
- Researched: `2026-07-23T23:33:32.664719+00:00`

This dossier is scoped to the upstream checkpoint BAAI/bge-large-en-v1.5. Primary-source artifacts in the inspected evidence set (Hugging Face model page, README, config and tokenizer files, commits list, NVIDIA NIM model card, ACL Findings PDF, and arXiv preprint) establish: embedding dimensionality 1024 (README, config.json), maximum position embeddings / sequence length 512 (config.json, README, NVIDIA NIM), model architecture listed as "BertModel" in the checkpoint config (config.json) while NVIDIA NIM describes a fine-tuned XLMRobertaModel (conflict documented), and a reported parameter count of 568 million on the NVIDIA NIM page. The Hugging Face README contains an aggregate benchmark table reporting an average score of 64.23 across a 56-task suite and named subset scores (retrieval 54.29, clustering 46.08, pair classification 87.12, reranking 60.03, STS 83.11, summarization 31.61, classification 75.97). The ACL Findings PDF and the arXiv preprint both report task-level retrieval and task metrics for bge-large-en-v1.5 (including N@10 and per-task numbers) in their papers, but the research findings provided do not include exact table/figure/section locators for these numeric entries; therefore the precise in-paper locators required by the dossier gates are not present in the available findings and are recorded as evidence gaps where required. Important provenance gaps remain: the provided findings do not map the Forge suffix "cb6f76e0da" to any explicit commit, safetensors asset ID, tag, or repository artifact path; tokenizer and vocabulary artifacts exist (tokenizer.json, tokenizer_config.json) and provide tokenizer-class and tokenization parameters, but other runtime contract items (explicit preprocessing pipeline beyond tokenizer settings, explicit batching semantics, embedding normalization policy) are not documented in the provided primary findings. All claims and citations in this report are restricted to the primary-source URLs listed in the top-level sources array.

## Identity

- Upstream name: BAAI/bge-large-en-v1.5
- Checkpoint/version: BAAI/bge-large-en-v1.5
- Immutable revision: not reported
- Parameter scale: 568 million
- Architecture/head: BertModel (config.json) / described as fine-tuned XLMRobertaModel (NVIDIA NIM)
- License: not reported
- Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-large-en-v1.5/commits/main, https://build.nvidia.com/baai/bge-m3/modelcard

## Selection

### Recommended

- **Generate fixed-size (1024-dimensional) embeddings from English text for downstream semantic tasks (semantic search, document retrieval, similarity comparison, clustering).** — README and config.json report the model produces 1024-dimensional embeddings and the model identifier indicates an English embedding variant.
  Scope: BAAI/bge-large-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json
- **Use as an English sentence embedding backbone for retrieval and reranking workflows after downstream validation on target data.** — README reports retrieval and reranking subset scores; ACL and arXiv papers report retrieval/ranking metrics for the checkpoint (task-level reporting present in papers).
  Scope: BAAI/bge-large-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://aclanthology.org/2025.findings-acl.1258.pdf, https://arxiv.org/pdf/2502.07131

### Conditional

- **Information retrieval, reranking, and clustering for English text (use conditionally after downstream validation).** — Primary sources report retrieval subset (54.29), reranking subset (60.03), and clustering subset (46.08) scores in the README; these numeric results require calibration and validation on target datasets before production use.
  Scope: BAAI/bge-large-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- **Pair classification / semantic similarity scoring for English text (conditional).** — High pair classification subset score (87.12) reported in README; users must validate on target distributions.
  Scope: BAAI/bge-large-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md

### Avoid

- **Summarization tasks** — The README reports a low summarization subset score (31.61) for bge-large-en-v1.5 in the documented benchmark table, indicating weak performance on summarization in the reported benchmarks.
  Scope: BAAI/bge-large-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- **Any task requiring documented tokenizer/vocabulary guarantees or per-dimension semantic interpretation of embeddings.** — While tokenizer artifacts exist (tokenizer_config.json, tokenizer.json) and provide class and parameters, the findings do not document a per-dimension semantic meaning for embeddings nor a broader formalized vocabulary guarantee beyond tokenizer files; therefore tasks needing explicit per-dimension semantics should avoid relying on undocumented guarantees.
  Scope: BAAI/bge-large-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/tokenizer.json

## Input preparation

### Semantic inputs

- English text strings (model identifier includes 'en' and README/config indicate English embedding variant). Sources: https://huggingface.co/BAAI/bge-large-en-v1.5, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Input type reported as Text (packaging/runtime metadata documented by NVIDIA NIM). Sources: https://build.nvidia.com/baai/bge-m3/modelcard

### Accepted formats

- Primary sources document typical input as text strings; README and NVIDIA NIM indicate text inputs (no other file-format contract documented). Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://build.nvidia.com/baai/bge-m3/modelcard

### Preprocessing

- Tokenizer class and basic tokenizer parameters are provided by tokenizer_config.json (BertTokenizer, do_lower_case true, do_basic_tokenize true, max length 512, special tokens [CLS],[SEP],[PAD],[MASK],[UNK]). Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/tokenizer.json
- The checkpoint config.json lists model tokenization-related model capacities (max position embeddings 512) and model hidden size (1024); no further explicit normalization or preprocessing pipeline is documented in the provided findings. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md

### Pre-submit validation

- Inputs should be validated to respect maximum sequence length = 512 tokens as reported in config.json and README; no further input-validation bounds (character limits, allowed character set beyond tokenizer config) are documented in the findings. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md

### Task-specific formatting

- No official prompt templates, paired-input order conventions, or embedding-specific prompt formatting are documented in the provided primary sources for embedding use. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-large-en-v1.5

## Output interpretation

### Outputs

- Primary output is a 1024-dimensional embedding vector per input, as reported in the README and implied by hidden_size in config.json. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json
- The checkpoint config.json indicates torch dtype float32 for model tensors; the provided findings do not state whether runtime embeddings are emitted as float32 or cast by specific serving runtimes. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json

### Interpretation

- Do not assume per-dimension semantic interpretation: the provided findings do not assign semantic meaning to individual embedding dimensions. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json
- No normalization/postprocessing (L2-normalization or similar) is documented in the provided primary findings; users should not assume embeddings are normalized by default. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md

### Post-inference validation

- Post-inference checks recommended by dossier authors based on primary findings: verify output dimensionality is 1024 and that inputs respected <=512 token bound; validate downstream retrieval/ranking performance on representative held-out data because subset performance varies in the README and papers. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://aclanthology.org/2025.findings-acl.1258.pdf, https://arxiv.org/pdf/2502.07131
- Evidence gap: batching semantics and exact batched output shape contract are not specified in the provided findings. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md

## Public benchmarks

### Benchmark suite (aggregate)

- Dataset/split: benchmark suite (56 tasks) / not reported
- Metric/value: average score / 64.23 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported aggregate score; dataset composition/splits not enumerated in README
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 64.23 is present in the Hugging Face README table as reported in the research findings.
- Caveat: Evidence gap: README does not enumerate the exact dataset names/splits that compose the 56-task suite in the provided findings.

### Retrieval subset

- Dataset/split: retrieval subset (15 tasks) / not reported
- Metric/value: subset score / 54.29 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported retrieval subset score; dataset composition/splits not specified
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 54.29 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not enumerate constituent dataset names/splits for the retrieval subset in the provided findings.

### Clustering subset

- Dataset/split: clustering subset (11 tasks) / not reported
- Metric/value: subset score / 46.08 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported clustering subset score; dataset composition/splits not specified
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 46.08 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not enumerate constituent dataset names/splits for the clustering subset in the provided findings.

### Pair classification subset

- Dataset/split: pair classification subset (3 tasks) / not reported
- Metric/value: subset score / 87.12 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported pair classification subset score
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 87.12 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not enumerate the exact datasets/splits composing the pair classification subset in the provided findings.

### STS subset

- Dataset/split: STS subset (10 tasks) / not reported
- Metric/value: subset score / 83.11 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported STS subset score
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 83.11 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not enumerate exact STS dataset names/splits in the provided findings.

### Summarization subset

- Dataset/split: summarization subset (1 task) / not reported
- Metric/value: subset score / 31.61 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported summarization subset single-task score
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 31.61 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not provide dataset/split details for the summarization task in the provided findings.

### Classification subset

- Dataset/split: classification subset (12 tasks) / not reported
- Metric/value: subset score / 75.97 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported classification subset score
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 75.97 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not enumerate dataset-level composition/splits for the classification subset in the provided findings.

### Reranking subset

- Dataset/split: reranking subset (4 tasks) / not reported
- Metric/value: subset score / 60.03 (`context-only`)
- Model scope: BAAI/bge-large-en-v1.5
- Conditions: README reported reranking subset score
- Source: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Locator: README.md table (benchmark results)
- Caveat: Verification: numeric value 60.03 is present in the Hugging Face README table per the research findings.
- Caveat: Evidence gap: README does not enumerate exact datasets/splits for the reranking subset in the provided findings.

### Retrieval metrics (ACL findings - first benchmark dataset)

- Dataset/split: first benchmark dataset (as reported in ACL findings paper) / not reported
- Metric/value: N@10 / 25.07 (`context-only`)
- Model scope: bge-large-en-v1.5 (as reported in ACL findings)
- Conditions: Reported in ACL Findings paper
- Source: https://aclanthology.org/2025.findings-acl.1258.pdf
- Locator: Evidence gap: exact table/figure/section/page locator for N@10=25.07 is not specified in the provided findings
- Caveat: Verification: the research findings state the ACL Findings paper reports N@10 = 25.07 for bge-large-en-v1.5 on the first benchmark dataset, but the findings do not provide the precise in-paper locator (table/figure/page/section). Per dossier gates this locator is required; thus the sourceLocator is recorded as an evidence gap.

### Retrieval metrics (ACL findings - multiple reported N@10 values)

- Dataset/split: various evaluation sets (as reported in ACL findings) / not reported
- Metric/value: N@10 (multiple values) / 44.07, 58.20, 60.28, 62.90, 64.35, 66.25 (as reported in findings) (`context-only`)
- Model scope: bge-large-en-v1.5 (ACL findings)
- Conditions: ACL paper reports multiple evaluation sets; mapping to README benchmark suite not provided in findings
- Source: https://aclanthology.org/2025.findings-acl.1258.pdf
- Locator: Evidence gap: exact table/figure/section/page locators for these N@10 values are not specified in the provided findings
- Caveat: Verification: research findings list these numeric values as reported in the ACL Findings paper, but precise locators within the PDF are not included in the provided findings; convert to evidence-gap locators per dossier gates.

## Comparisons

### alibaba-nlp-gte-modernbert-base (Alibaba-NLP/gte-modernbert-base) — `insufficient-evidence`

- Task: embeddings / retrieval / ranking (Forge embeddings task group)
- Criteria: No protocol-matched, checkpoint-exact primary-source comparison exists in the provided findings between BAAI/bge-large-en-v1.5 and the named Alibaba checkpoint.
- Rationale: Inspected primary sources (Hugging Face model card/README/config/commits, NVIDIA NIM, ACL Findings PDF, arXiv preprint) include benchmark numbers for bge-large-en-v1.5 but do not present a protocol-matched, primary-source table comparing the exact Alibaba checkpoint named by the candidate list.
- Comparison conditions: No identical-protocol, checkpoint-exact table found in the provided findings.
- Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://aclanthology.org/2025.findings-acl.1258.pdf, https://arxiv.org/pdf/2502.07131, https://build.nvidia.com/baai/bge-m3/modelcard

### baai-bge-base-en-v1-5 (BAAI/bge-base-en-v1.5) — `insufficient-evidence`

- Task: embeddings / retrieval / ranking
- Criteria: Although related family models are listed, the provided findings do not include protocol-matched, dataset-level tables that compare bge-large-en-v1.5 to bge-base-en-v1.5 under identical conditions for the exact checkpoints.
- Rationale: README and model card list related models and dimensions but no direct, checkpoint-exact head-to-head benchmark table is present in the provided findings.
- Comparison conditions: No identical evaluation protocol and checkpoint pairing found in the provided findings.
- Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-large-en-v1.5/commits/main

### baai-bge-m3 (BAAI/bge-m3 / NVIDIA packaging) — `insufficient-evidence`

- Task: embeddings / long-context multilingual embeddings
- Criteria: NVIDIA NIM references bge-m3 and bge-large-en-v1.5 but does not provide protocol-matched benchmark tables enabling direct head-to-head comparisons for the exact checkpoints in the provided findings.
- Rationale: NVIDIA NIM and the README/config report differing sequence-length/behavior claims across family members (e.g., bge-m3 reported with 8192 sequence length in NVIDIA NIM vs. 512 for bge-large-en-v1.5), preventing a protocol-matched comparison in the provided findings.
- Comparison conditions: No protocol-matched, checkpoint-exact comparison table present in the provided findings.
- Evidence: https://build.nvidia.com/baai/bge-m3/modelcard, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md

### Other listed candidate alternatives (all remaining candidates in the provided list) — `insufficient-evidence`

- Task: embeddings / retrieval / ranking
- Criteria: The provided primary sources do not present protocol-matched comparisons between bge-large-en-v1.5 and each of the other candidate checkpoints named in the candidate list.
- Rationale: Under the research constraints only the provided primary sources were inspected; no matching head-to-head tables were found for the remaining candidates in those sources.
- Comparison conditions: No identical-protocol, checkpoint-exact comparisons in the provided findings.
- Evidence: https://huggingface.co/BAAI/bge-large-en-v1.5, https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-large-en-v1.5/commits/main, https://build.nvidia.com/baai/bge-m3/modelcard, https://aclanthology.org/2025.findings-acl.1258.pdf, https://arxiv.org/pdf/2502.07131

## Limitations and safety

### Limitations

- Ambiguity/conflict between checkpoint config and NVIDIA NIM descriptions: config.json lists architecture as "BertModel" and model hidden_size 1024 while NVIDIA NIM describes the network as a fine-tuned XLMRobertaModel and reports parameter count 568 million; both statements are present in the provided findings and create a provenance/description ambiguity. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json, https://build.nvidia.com/baai/bge-m3/modelcard
- Evidence gap: The provided findings do not map the Forge suffix 'cb6f76e0da' to an explicit commit, safetensors asset, tag, or repository artifact path for BAAI/bge-large-en-v1.5.
- Evidence gap: The README reports aggregate and subset benchmark scores but does not enumerate the exact dataset names/splits composing the 56-task suite in the provided findings, limiting direct cross-source comparability. Sources: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Evidence gap: The provided findings do not document embedding normalization policy (L2-normalization) or per-dimension semantic meanings for embeddings.
- Evidence gap: Batching semantics and exact batched output shape contract are not specified in the provided findings.

### Safety

- Evidence gap: The provided primary findings do not document model-specific safety mitigations, PHI/clinical handling guidance, or dual-use restrictions for this checkpoint.
- License provenance: The provided findings do not include an explicit license statement for BAAI/bge-large-en-v1.5; NVIDIA NIM lists MIT for BGE-M3 but the findings do not provide a direct, explicit license statement for this upstream checkpoint within the inspected artifacts. Sources: https://build.nvidia.com/baai/bge-m3/modelcard

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model page: BAAI/bge-large-en-v1.5

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5
- Publisher: Hugging Face / BAAI model repository
- Type: `model-card`
- Primary because: Official Hugging Face model page for the upstream checkpoint BAAI/bge-large-en-v1.5 (entry point for README and repo files used as primary evidence).
- Scope: BAAI/bge-large-en-v1.5 (Hugging Face model card)
- Supports: Entry page for the BAAI/bge-large-en-v1.5 checkpoint and links to README and repository artifacts used throughout this dossier.

### BAAI/bge-large-en-v1.5 README

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/README.md
- Publisher: BAAI / Hugging Face repository
- Type: `repository`
- Primary because: Repository README accompanying the Hugging Face model card; contains the reported benchmark table and usage recommendations referenced in this dossier.
- Scope: BAAI/bge-large-en-v1.5 (README)
- Supports: Embedding dimension 1024, maximum sequence length 512, aggregate score 64.23 and subset scores: retrieval 54.29, clustering 46.08, pair classification 87.12, reranking 60.03, STS 83.11, summarization 31.61, classification 75.97.

### BAAI/bge-large-en-v1.5 commits list

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5/commits/main
- Publisher: BAAI / Hugging Face repository
- Type: `repository`
- Primary because: Repository commit history for the model artifacts; used to check for safetensors/onnx additions and revision notes (no Forge suffix mapping found).
- Scope: BAAI/bge-large-en-v1.5 (commits)
- Supports: Commit history listing safetensors and ONNX artifact additions; used to inspect artifact provenance within the repository.

### BAAI/bge-large-en-v1.5 config.json

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/config.json
- Publisher: BAAI / Hugging Face repository
- Type: `repository`
- Primary because: Checkpoint configuration file in the Hugging Face repository; provides architecture token/position settings, hidden_size, number of layers, and torch dtype metadata used as primary evidence for model contract attributes.
- Scope: BAAI/bge-large-en-v1.5 (config.json)
- Supports: Architecture listed as "BertModel"; hidden_size 1024; maximum position embeddings 512; torch dtype float32; number of hidden layers and attention head counts; other model configuration parameters.

### BAAI/bge-large-en-v1.5 tokenizer_config.json

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/tokenizer_config.json
- Publisher: BAAI / Hugging Face repository
- Type: `repository`
- Primary because: Tokenizer configuration file in the Hugging Face repository; provides tokenizer class and tokenization parameters used as primary evidence for preprocessing contract.
- Scope: BAAI/bge-large-en-v1.5 (tokenizer_config.json)
- Supports: Tokenizer class: BertTokenizer; tokenizer max model length 512; do_lower_case true; do_basic_tokenize true; special tokens [CLS],[SEP],[PAD],[MASK],[UNK]; tokenize_chinese_chars true.

### BAAI/bge-large-en-v1.5 tokenizer.json

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/tokenizer.json
- Publisher: BAAI / Hugging Face repository
- Type: `repository`
- Primary because: Tokenizer JSON artifact in the Hugging Face repository; confirms presence of tokenizer artifact usable with Transformers / sentence-transformers.
- Scope: BAAI/bge-large-en-v1.5 (tokenizer.json)
- Supports: A tokenizer.json file is provided for the model and can be used with sentence-transformers and Transformers libraries.

### BAAI/bge-large-en-v1.5 model.safetensors

- URL: https://huggingface.co/BAAI/bge-large-en-v1.5/blob/main/model.safetensors
- Publisher: BAAI / Hugging Face repository
- Type: `repository`
- Primary because: Model artifact entry in the Hugging Face repository (safetensors); used to inspect presence of a safetensors asset in commits and repository.
- Scope: BAAI/bge-large-en-v1.5 (model.safetensors artifact page)
- Supports: Presence of a model.safetensors artifact referenced in the repository commit history (safetensors variant added in commits).

### NVIDIA NIM model card (BAAI/BGE listing)

- URL: https://build.nvidia.com/baai/bge-m3/modelcard
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM page that documents packaging/runtime metadata and reports architecture description and parameter count for the family/packaged entries inspected.
- Scope: NVIDIA NIM model card referencing BAAI/BGE family
- Supports: NVIDIA NIM lists BAAI/bge-large-en-v1.5 as having dimension 1024 and maximum sequence length 512, and reports a parameter count of 568 million; describes packaging/runtime input type as text (list of strings) for NVIDIA-served models.

### ACL Findings paper (2025) PDF

- URL: https://aclanthology.org/2025.findings-acl.1258.pdf
- Publisher: ACL Anthology (Findings of ACL 2025)
- Type: `paper`
- Primary because: Peer-reviewed conference Findings PDF reporting retrieval/ranking metrics for bge-large-en-v1.5 used for task-level benchmark evidence in this dossier.
- Scope: bge-large-en-v1.5 evaluated in ACL Findings paper
- Supports: The ACL Findings paper reports retrieval metrics (for example N@10 = 25.07 and other N@10/P@10/R@10 values for bge-large-en-v1.5) as listed in the provided findings.

### arXiv preprint (arXiv:2502.07131) PDF

- URL: https://arxiv.org/pdf/2502.07131
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical arXiv preprint cited by the model documentation that reports per-task metrics for bge-large-en-v1.5.
- Scope: bge-large-en-v1.5 reported in arXiv preprint
- Supports: The arXiv preprint reports task-level metrics for bge-large-en-v1.5 (examples in findings include STS Pearson 0.751, FiQA2018 mAP 0.751, dart V-measure 0.203, and other task metrics).

## Evidence gaps

- Evidence gap: Exact artifact revision identifier mapping from the Forge suffix 'cb6f76e0da' to a named commit, safetensors asset, tag, or repository path for BAAI/bge-large-en-v1.5 is not present in the provided findings.
- Evidence gap: The provided findings do not include explicit in-paper locators (table/figure/section/page) for the ACL Findings paper numeric entries (e.g., N@10 = 25.07); precise locators required by dossier gates are missing in the findings.
- Evidence gap: The provided findings do not include explicit in-paper locators (table/figure/section/page) for the arXiv preprint per-task metrics (e.g., STS Pearson 0.751, FiQA2018 mAP 0.751); precise locators required by dossier gates are missing in the findings.
- Evidence gap: Tokenizer and vocabulary details beyond tokenizer_config.json/tokenizer.json (for example a separate vocabulary.txt file mapping or human-readable vocabulary listing) are not present in the provided findings.
- Evidence gap: Explicit preprocessing/normalization pipeline (normalization rules, punctuation handling beyond basic tokenizer parameters) is not documented in the provided findings.
- Evidence gap: Embedding normalization policy (e.g., whether embeddings are L2-normalized) is not documented in the provided findings.
- Evidence gap: Batching semantics and exact batched output shape contract are not specified in the provided findings.
- Evidence gap: Mapping from Forge serving-variant slugs (for example TEI CUDA serving variants) to an exact upstream artifact name or commit is not present in the provided findings.
- Evidence gap: README reports aggregate and subset benchmark scores but does not enumerate dataset-level composition/splits for the 56-task suite in the provided findings, preventing direct dataset-level cross-source mapping.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[10]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
