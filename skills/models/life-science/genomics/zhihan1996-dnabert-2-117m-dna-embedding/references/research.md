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

- Research key: `huggingface-co-zhihan1996-dnabert-2-117m-223e616881`
- Independent audit: `revised`
- Researched: `2026-08-06T14:14:17.693921+00:00`

The exact checkpoint zhihan1996/DNABERT-2-117M is hosted on Hugging Face and corresponds to the DNABERT-2 (117M) model family described in the DNABERT-2 paper (arXiv:2306.15006). The repository contains a machine-readable config.json blob that records a BERT-style encoder (BertForMaskedLM) with 12 hidden layers, hidden_size=768, 12 attention heads, intermediate_size=3072, GELU activation, absolute positional embeddings, max_position_embeddings=512, and ALiBi-related field alibi_starting_size=512. The model repository also includes an implementation blob bert_layers.py that defines the BertModel and sequence-classification head code and a model weight artifact (model.safetensors). Tokenizer configuration metadata (tokenizer_config.json) is present in the repository blobs, but explicit tokenizer vocabulary files and full vocab mapping were not found in the inspected primary blobs. The DNABERT-2 paper (arXiv) reports a GUE+ average value (arXiv v1 listing 66.80) for DNABERT-2 (117M) in the paper text/table cited in the findings; however, the inspected primary repository blobs do not contain an explicit in-repo numeric table tying the paper-reported numeric row to a repository path/locator for the exact Hugging Face checkpoint. Where primary blobs do not document a property, the dossier records an explicit evidence gap.

## Identity

- Upstream name: zhihan1996/DNABERT-2-117M
- Checkpoint/version: DNABERT-2-117M
- Immutable revision: not reported
- Parameter scale: 117 million parameters (117M) as reported in the DNABERT-2 paper (arXiv:2306.15006 v1)
- Architecture/head: BERT-style encoder; architectures includes "BertForMaskedLM"; model_type = "bert"; num_hidden_layers = 12; hidden_size = 768; num_attention_heads = 12; intermediate_size = 3072; hidden_act = "gelu"; position_embedding_type = "absolute"; max_position_embeddings = 512; alibi_starting_size = 512; attention_probs_dropout_prob = 0.0; hidden_dropout_prob = 0.1; auto_map entries map AutoConfig -> "configuration_bert.BertConfig" and AutoModel -> "bert_layers.BertModel" (fields recorded in the checkpoint config.json blob).
- License: LICENSE blob present in the repository history at the listed LICENSE blob URL; license text content and explicit weight-vs-code license distinctions were not provided in the inspected findings.
- Evidence: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/model.safetensors, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE, https://arxiv.org/html/2306.15006v1

## Selection

### Recommended

- **DNA sequence representation / embedding for downstream genomics tasks** — The Hugging Face model page demonstrates loading the tokenizer and model, tokenizing DNA strings, producing per-token hidden_states and pooled embeddings; the checkpoint config.json and bert_layers.py record a 768-dimensional hidden size and BERT-style encoder behavior that supports producing sequence embeddings from tokenized DNA input.
  Scope: zhihan1996/DNABERT-2-117M (base checkpoint)
  Evidence: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py

### Conditional

- **Supervised downstream classification after attaching and fine-tuning a task-specific classification head** — The inspected base checkpoint blobs provide encoder hidden states and the repository bert_layers.py implements a BertForSequenceClassification class, but the base model weights do not include a validated downstream classifier head artifact tied to the base checkpoint; downstream classification therefore requires attaching/training a classifier head and performing task-specific fine-tuning and validation.
  Scope: zhihan1996/DNABERT-2-117M (base checkpoint) plus externally attached classifier head or fine-tuned BertForSequenceClassification implementation
  Evidence: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json

### Avoid

- **Clinical deployment or clinical decision support** — Evidence gap: Upstream repository blobs inspected do not provide clinical-grade validation, regulatory authorization, or deployment guidance that would support clinical decision-making for the base checkpoint.
  Scope: zhihan1996/DNABERT-2-117M base checkpoint
  Evidence: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE

## Input preparation

### Semantic inputs

- Intended inputs are raw DNA nucleotide sequences (plain DNA strings). Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M

### Accepted formats

- Model page shows loading via AutoTokenizer.from_pretrained and AutoModel.from_pretrained and demonstrates tokenizing a DNA string to input IDs suitable for the model. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M

### Preprocessing

- The model was pre-trained using a masked language modeling (MLM) style objective on tokenized DNA sequences as described by the model page and the DNABERT-2 paper. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://arxiv.org/html/2306.15006v2
- Configured maximum token length (max_position_embeddings) is 512 as recorded in the checkpoint config.json. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json

### Pre-submit validation

- Config.json records max_position_embeddings=512; sequences longer than 512 tokens exceed the configured maximum according to the checkpoint configuration blob. No explicit runtime truncation/padding contract is present in the inspected blobs. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json, https://huggingface.co/zhihan1996/DNABERT-2-117M
- Evidence gap: Tokenizer vocabulary files (tokenizer.json, vocab.txt, merges.txt, or explicit vocab mapping blobs) were not located in the inspected primary blobs; exact tokenizer vocabulary mapping cannot be verified from the inspected findings. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/tokenizer_config.json

### Task-specific formatting

- No official prompt templates or paired-input wrappers are present in the inspected base checkpoint blobs; downstream task formats must be provided by downstream fine-tuning code or model wrapper implementations. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py

## Output interpretation

### Outputs

- Per-token hidden_states are produced with shape [batch, sequence_length, 768] when tokenized DNA sequences are passed to the model; the Hugging Face model page sample usage demonstrates hidden_states shape [1, sequence_length, 768]. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M
- Pooling (mean or max) over the sequence dimension yields a 768-dimensional sequence embedding; the model page demonstrates pooled embeddings producing dimension 768. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M
- Model weight artifact (model.safetensors) is present in the repository blobs for the checkpoint distribution. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/model.safetensors

### Interpretation

- Encoder hidden states can be interpreted as per-token contextual embeddings; pooled vectors provide fixed-size (768-d) sequence representations for downstream tasks. The inspected primary blobs do not prescribe a specific pooling normalization or classifier design. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py

### Post-inference validation

- Evidence gap: The inspected primary blobs do not document numeric output dtype defaults (e.g., FP32 vs FP16) or an explicit embedding normalization (L2 or other). Downstream code should validate dtype and normalization when using embeddings. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json
- Evidence gap: The inspected repository blobs do not include a served JSON wrapper or a documented served-variant output envelope; no served-format contract is present in the inspected checkpoint blobs. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M

## Public benchmarks

### Genome sequence classification benchmark suite

- Dataset/split: Genome Understanding Evaluation (GUE), 28 datasets / Per-dataset test splits; three random seeds
- Metric/value: Paper-defined average evaluation score / 66.80 (`higher-is-better`)
- Model scope: DNABERT-2 117M base upstream checkpoint without additional GUE masked-language-model pretraining
- Conditions: Table 3 aggregate across the 28 GUE datasets; evaluation uses F1 or MCC by task, the lowest-validation-loss checkpoint, test-set reporting, and an average across three random seeds.
- Source: https://arxiv.org/html/2306.15006v2
- Locator: Table 3
- Caveat: Upstream fine-tuned downstream-task result; it is not a benchmark of raw Forge embeddings or Forge runtime performance.
- Caveat: Do not compare this aggregate directly with GUE+ Table 5 or with the 67.77 row that adds further masked-language-model pretraining on GUE training data.

## Comparisons

### Other DNA foundation models (protocol-matched comparisons not available) — `insufficient-evidence`

- Task: Task- and protocol-matched comparisons on genome sequence classification/embedding benchmarks
- Criteria: Protocol-matched peer-model primary-source benchmark tables with exact checkpoint identifiers and matching dataset/split/metric protocols are required for valid comparisons; such protocol-matched primary artifacts for peers were not present among the inspected primary blobs.
- Rationale: The DNABERT-2 paper reports outperforming some prior DNA language models on GUE+, but the inspected Hugging Face repository blobs and the paper do not supply repository-level, protocol-matched primary-source benchmark artifacts for alternative checkpoints to permit a direct, repository-tied comparison.
- Comparison conditions: Comparability would require peer-model primary-source artifact URLs and explicit table/row locators that were not found in the inspected primary blobs.
- Evidence: https://arxiv.org/html/2306.15006v1, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json

## Limitations and safety

### Limitations

- Evidence gap: No clinical-grade validation, regulatory authorization, or deployment guidance for clinical decision-making is provided in the inspected primary blobs; do not assume clinical suitability without independent validation. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE
- Evidence gap: Tokenizer artifact files containing full vocabulary mappings (e.g., tokenizer.json, vocab.txt, merges.txt) were not present among the inspected primary blobs; exact tokenizer vocabulary and merges cannot be verified from the inspected findings. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/tokenizer_config.json
- Evidence gap: Runtime truncation/padding policy and batching defaults are not documented in the inspected blobs (config.json records max_position_embeddings=512 but no explicit runtime truncation/padding code/contract was located in the inspected implementation blobs). Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py

### Safety

- Evidence gap: The inspected upstream artifacts do not specify PHI handling, biosecurity controls, or clinical deployment safeguards; users should perform independent risk assessment and compliance checks before using this checkpoint in clinical or sensitive contexts. Sources: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### zhihan1996/DNABERT-2-117M – Hugging Face

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model page for the exact checkpoint zhihan1996/DNABERT-2-117M; used to confirm checkpoint identity, sample usage, and model-card statements.
- Scope: zhihan1996/DNABERT-2-117M (model page)
- Supports: Model page presence and sample usage showing tokenization, input_ids, hidden-state shape [1, sequence_length, 768], and pooled embeddings (768-d).
- Supports: Load instructions using AutoTokenizer.from_pretrained and AutoModel.from_pretrained with trust_remote_code=True and example DNA string tokenization.

### DNABERT-2 README.md (blob)

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/README.md
- Publisher: Hugging Face model repository files
- Type: `repository`
- Primary because: Repository README in the model repo describing the model and implementation context.
- Scope: zhihan1996/DNABERT-2-117M README blob
- Supports: Statement that DNABERT-2 is the pre-trained model introduced in the DNABERT-2 paper and that the implementation builds upon MosaicBERT.

### DNABERT-2 model config.json (blob)

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json
- Publisher: Hugging Face model repository files
- Type: `repository`
- Primary because: Machine-readable model configuration blob for the specific DNABERT-2-117M checkpoint; provides architecture and hyperparameter fields.
- Scope: zhihan1996/DNABERT-2-117M config.json
- Supports: architectures includes "BertForMaskedLM"
- Supports: model_type = "bert"
- Supports: num_hidden_layers = 12
- Supports: hidden_size = 768
- Supports: num_attention_heads = 12
- Supports: intermediate_size = 3072
- Supports: hidden_act = "gelu"
- Supports: position_embedding_type = "absolute"
- Supports: max_position_embeddings = 512
- Supports: alibi_starting_size = 512
- Supports: attention_probs_dropout_prob = 0.0
- Supports: hidden_dropout_prob = 0.1
- Supports: auto_map entries mapping AutoConfig and AutoModel to checkpoint-specific classes

### DNABERT-2 tokenizer_config.json (blob)

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/tokenizer_config.json
- Publisher: Hugging Face model repository files
- Type: `repository`
- Primary because: Tokenizer configuration blob present in the model repository that documents tokenizer class and special tokens.
- Scope: zhihan1996/DNABERT-2-117M tokenizer_config.json
- Supports: Defines tokenizer class as "PreTrainedTokenizerFast" and special tokens [UNK],[CLS],[SEP],[PAD],[MASK].

### DNABERT-2 bert_layers.py (blob)

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py
- Publisher: Hugging Face model repository files
- Type: `repository`
- Primary because: Implementation module in the checkpoint repository that documents model forward, encoder and pooling behavior and the available sequence-classification head code.
- Scope: zhihan1996/DNABERT-2-117M implementation blob bert_layers.py
- Supports: Definition of BertModel and BertForSequenceClassification classes and their forward behavior
- Supports: Details about expected input shapes (input_ids shape [batch_size, sequence_length]) and pooling/pooled_output behavior
- Supports: Instantiation of dropout and attention parameter usage consistent with config.json fields

### DNABERT-2 model weight artifact (model.safetensors blob)

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/model.safetensors
- Publisher: Hugging Face model repository files
- Type: `repository`
- Primary because: Model weight blob present in the repository blobs for the checkpoint distribution.
- Scope: zhihan1996/DNABERT-2-117M model weights
- Supports: Presence of model weight artifact (model.safetensors) in the checkpoint blobs

### DNABERT-2 LICENSE blob (repo history)

- URL: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE
- Publisher: Hugging Face model repository files
- Type: `repository`
- Primary because: Repository blob indicating a LICENSE file exists in the repository history for the checkpoint distribution.
- Scope: zhihan1996/DNABERT-2-117M LICENSE blob
- Supports: Presence of a LICENSE file blob in the repository history (license text content not reported in the inspected findings)

### DNABERT-2 paper (arXiv:2306.15006 v1 HTML)

- URL: https://arxiv.org/html/2306.15006v1
- Publisher: arXiv (canonical preprint)
- Type: `paper`
- Primary because: Canonical DNABERT-2 preprint version v1 describing model scale and reported benchmark values referenced in the findings.
- Scope: DNABERT-2 (117M) as reported in the DNABERT-2 paper (arXiv v1)
- Supports: Model scale: 117 million parameters for DNABERT-2 (117M)
- Supports: Reported GUE+ average score value listed in the arXiv v1 HTML as recorded in the inspected findings

### DNABERT-2 paper (arXiv:2306.15006 v2 HTML)

- URL: https://arxiv.org/html/2306.15006v2
- Publisher: arXiv (canonical preprint)
- Type: `paper`
- Primary because: Alternate arXiv preprint revision (v2) of the DNABERT-2 paper referenced in the findings for benchmark and task details.
- Scope: DNABERT-2 (paper v2)
- Supports: Paper-level benchmark tables and reported task results (epigenetic marks prediction scores listed in the inspected findings)

### DNABERT-2 paper (arXiv abstract page)

- URL: https://arxiv.org/abs/2306.15006
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv abstract page for the DNABERT-2 paper referenced in the findings.
- Scope: DNABERT-2 (arXiv abstract)
- Supports: Paper metadata such as recommended citation and subject classifications (as recorded in the inspected findings)

## Evidence gaps

- Evidence gap: Exact tokenizer vocabulary/mapping files (tokenizer.json, vocab.txt, merges.txt or complete vocab mapping) were not located in the inspected primary blobs; checked URLs: https://huggingface.co/zhihan1996/DNABERT-2-117M , https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json , https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/tokenizer_config.json
- Evidence gap: Explicit per-character normalization rules (case handling or IUPAC code handling) are not specified in the inspected primary blobs; checked URLs: https://huggingface.co/zhihan1996/DNABERT-2-117M , https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json
- Evidence gap: Runtime truncation/padding policy, batching defaults, and explicit code-level truncation behavior are not documented in the inspected implementation/config blobs; checked URLs: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json , https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py
- Evidence gap: Exact numeric output dtype defaults (FP32/FP16) and embedding normalization (L2 or other) are not documented in the inspected primary blobs; checked URLs: https://huggingface.co/zhihan1996/DNABERT-2-117M , https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/69993b2cdacd281d1349855af17c500f73528ec0/config.json
- Evidence gap: The inspected repository blobs do not contain an explicit in-repo numeric benchmark table that ties the paper-reported GUE+ numeric rows directly to an exact repository table/locator for the Hugging Face checkpoint; checked URLs: https://arxiv.org/html/2306.15006v1 , https://arxiv.org/html/2306.15006v2 , https://huggingface.co/zhihan1996/DNABERT-2-117M
- Evidence gap: Protocol-matched primary-source benchmark artifacts for peer models required for direct, repository-level comparisons were not present in the inspected primary blobs; checked URLs: https://arxiv.org/html/2306.15006v1 , https://huggingface.co/zhihan1996/DNABERT-2-117M

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 14 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2] uses unapproved repository owner 'multimolecule' for this exact model scope: $.sources[2] uses unapproved repository owner 'multimolecule' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] describes itself as secondary evidence: $.sources[6] describes itself as secondary evidence Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary URL https: $.sources[10] uses forbidden secondary URL https://huggingface.co/zhihan1996/DNABERT-2-117M/discussions/2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2306.15006 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/abs/2509.25274 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2306.15006 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://arxiv.org/html/2306.15006v2#Table 3:Paper-defined average evaluation score: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
