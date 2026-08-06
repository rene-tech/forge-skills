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

- Research key: `huggingface-co-longsafari-hyenadna-medium-450k-seqlen-hf-22314617db`
- Independent audit: `revised`
- Researched: `2026-08-06T09:34:03.230334+00:00`

Checkpoint-scoped blobs for LongSafari/hyenadna-medium-450k-seqlen-hf (model page, config.json at revision 8ddebc5..., tokenizer blobs, and model.safetensors) establish that this checkpoint uses model_type 'hyenadna' with an implementation mapping to HyenaDNAForCausalLM, a tokenizer declared as HyenaDNATokenizer with model_max_length 450,002, n_layer=8, d_model=256, d_inner=1024, emb_dim=5, vocab_size=12, and pad_token_id=4. The model page and tokenizer blobs document single-character nucleotide tokenization (A,C,G,T plus special tokens and support for 'N' in related README examples). The checkpoint contains a weight file named model.safetensors. The checkpoint-level artifacts do not report an explicit parameter count, do not declare a model-weights license, do not document an embeddings output contract (dimensionality or pooling), and do not specify inference-time input-handling policies (truncate vs sliding-window, default stride, batching semantics). A README for a related checkpoint (hyenadna-medium-160k-seqlen) declares a 'bsd-3-clause' license, but the checkpoint blobs inspected here do not assert a weights or checkpoint-scoped license.

## Identity

- Upstream name: hyenadna-medium-450k-seqlen-hf
- Checkpoint/version: hyenadna-medium-450k-seqlen-hf
- Immutable revision: 8ddebc527c28dca5d142fdacbaa82f519dba4d30
- Parameter scale: not reported
- Architecture/head: HyenaDNAForCausalLM (checkpoint-scoped mapping in config.json; model_type 'hyenadna')
- License: Model-weights license: not reported in checkpoint blobs or model page. Code/license metadata: README for a related checkpoint (hyenadna-medium-160k-seqlen) declares 'bsd-3-clause' (family/checkpoint relation not asserted by the blobs).
- Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/commits/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/model.safetensors, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py, https://huggingface.co/LongSafari/hyenadna-medium-160k-seqlen/blame/main/README.md

## Selection

### Recommended

- **Research experiments in long-range genomic sequence modeling at single-nucleotide resolution (e.g., next-nucleotide prediction / causal LM research and exploratory modeling).** — Checkpoint blobs and model page document a HyenaDNA causal-LM mapping (HyenaDNAForCausalLM), single-nucleotide character tokenization, and a very large tokenizer model_max_length (450,002) supporting long-context sequence modeling experiments.
  Scope: hyenadna-medium-450k-seqlen-hf (checkpoint blobs: config.json, tokenizer_config.json, tokenization_hyena.py)
  Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py

### Conditional

- **Adapting or fine-tuning this checkpoint to downstream genomics prediction tasks (e.g., regulatory-element prediction) conditioned on downstream empirical validation.** — Require downstream empirical validation for this exact checkpoint because checkpoint blobs do not map published family-level benchmark rows or numeric values to this filename and do not declare parameter count, embeddings contract, or inference-time input-handling policies.
  Scope: hyenadna-medium-450k-seqlen-hf (checkpoint blobs)
  Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

### Avoid

- **Assuming the checkpoint is approved or suitable for clinical decision-making without expert review.** — Inspected checkpoint blobs and model page do not provide clinical-use approval, PHI-specific handling guidance, or checkpoint-scoped clinical validation statements; no checkpoint-scoped clinical disclaimers or PHI mitigation procedures are documented in the inspected blobs.
  Scope: hyenadna-medium-450k-seqlen-hf
  Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

## Input preparation

### Semantic inputs

- Raw DNA sequences composed of canonical nucleotide characters at single-nucleotide resolution (characters A, C, G, T) with support for ambiguous base 'N' shown in related README examples. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-160k-seqlen/blame/main/README.md, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py

### Accepted formats

- Tokenizer class declared as 'HyenaDNATokenizer' and model_max_length declared as 450,002 in tokenizer_config.json; tokenizer uses fixed internal character vocabulary and special tokens (no external vocab file referenced in inspected tokenizer blobs). Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py

### Preprocessing

- Tokenization is character-level: the tokenizer implementation returns individual characters as tokens and defines model input names ['input_ids','attention_mask']; tokenizer defines special tokens (BOS '[BOS]', EOS '[SEP]', CLS '[CLS]', MASK '[MASK]', UNK '[UNK]'). Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json

### Pre-submit validation

- Config and tokenizer blobs declare model_max_length / max_seq_len as 450,002 tokens; sequences exceeding this length are outside the declared tokenizer/config maximum. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json
- Evidence gap: The inspected checkpoint blobs and model page do not specify inference-time input-handling policies such as truncate vs sliding-window behavior, default stride, batching semantics, or accepted file header formats. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json

### Task-specific formatting

- Family-level pretraining objective described on the model page is next-token (next-nucleotide) prediction; the inspected checkpoint blobs do not specify any special prompt or wrapper formatting for this checkpoint. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

## Output interpretation

### Outputs

- Family-level official outputs (as described on the model page) are next-token (next-nucleotide) prediction probabilities/scores under a causal LM formulation. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json
- Evidence gap: The inspected checkpoint blobs and model page do not document an embeddings output contract (embedding dimensionality, pooling semantics, or JSON schema) for hyenadna-medium-450k-seqlen-hf. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

### Interpretation

- Next-token outputs from the checkpoint should be interpreted as next-nucleotide prediction probabilities or scores under a causal LM head; do not assume any additional embeddings or downstream-head guarantees absent checkpoint-scoped documentation. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

### Post-inference validation

- Post-inference validation: checkpoint blobs do not include checkpoint-scoped calibration procedures or explicit confidence-interval reporting; users must perform downstream empirical validation for task-specific calibration. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### huggingfacebio-carbon-3b-vllm-cuda13 — `insufficient-evidence`

- Task: no task-specific, protocol-matched comparison available
- Criteria: No primary-source, checkpoint-level head-to-head benchmark or protocol-matched evaluation naming both this checkpoint and the alternative was found in the inspected locators.
- Rationale: Inspected checkpoint-scoped blobs and model page do not contain protocol-matched numeric comparisons to the named alternative.
- Comparison conditions: Checked only the checkpoint blobs and model page for hyenadna-medium-450k-seqlen-hf; no matching comparison rows were present.
- Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

### instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding — `insufficient-evidence`

- Task: no task-specific, protocol-matched comparison available
- Criteria: No primary-source, checkpoint-level protocol-matched evaluation naming both this checkpoint and the alternative was found in the inspected locators.
- Rationale: Inspected checkpoint-scoped blobs and model page do not contain protocol-matched numeric comparisons to the named alternative.
- Comparison conditions: Checked checkpoint blobs and model page for hyenadna-medium-450k-seqlen-hf; no matching comparison rows were present.
- Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

### zhihan1996-dnabert-2-117m-dna-embedding — `insufficient-evidence`

- Task: no task-specific, protocol-matched comparison available
- Criteria: No primary-source, checkpoint-level protocol-matched evaluation naming both this checkpoint and the alternative was found in the inspected locators.
- Rationale: Inspected checkpoint-scoped blobs and model page do not contain protocol-matched numeric comparisons to the named alternative.
- Comparison conditions: Checked checkpoint blobs and model page for hyenadna-medium-450k-seqlen-hf; no matching comparison rows were present.
- Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

## Limitations and safety

### Limitations

- Evidence gap: The inspected checkpoint blobs do not unambiguously map any published family-level numeric benchmark rows or table values to this exact checkpoint filename. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json
- Evidence gap: Exact parameter count for the hyenadna-medium-450k-seqlen-hf checkpoint is not reported in the inspected checkpoint blobs or model page. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf
- Evidence gap: Embedding dimensionality, pooling semantics, and an embeddings output contract (JSON schema) for this checkpoint are not present in the inspected blobs or model page. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json
- Evidence gap: The model-weights license for hyenadna-medium-450k-seqlen-hf is not declared in the inspected checkpoint blobs or model page; a README for a related checkpoint (hyenadna-medium-160k-seqlen) declares 'bsd-3-clause' but that README is for a different named checkpoint. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-160k-seqlen/blame/main/README.md

### Safety

- Training-data provenance (family-level as stated on the model page): HyenaDNA family is described on the model page as pretrained on the human reference genome (HG38) at single-nucleotide resolution; treat human-derived sequence handling with standard privacy and provenance caution. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf
- Evidence gap: The inspected checkpoint blobs and model page do not include explicit PHI-specific handling guidance, clinical-use disclaimers, or upstream safety mitigations for the hyenadna-medium-450k-seqlen-hf checkpoint. Sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### LongSafari / hyenadna-medium-450k-seqlen-hf (Hugging Face model page)

- URL: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf
- Publisher: LongSafari (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model page for the hyenadna-medium-450k-seqlen-hf checkpoint; contains model-card statements and links to checkpoint blobs used in this dossier.
- Scope: hyenadna-medium-450k-seqlen-hf (model page)
- Supports: Listing of hyenadna-medium-450k-seqlen-hf checkpoint under LongSafari
- Supports: Family-level description that HyenaDNA is a long-range genomic foundation model and notes on single-character nucleotide tokenization and next-token pretraining
- Supports: Links to checkpoint blobs (config.json, tokenizer blobs, tokenization implementation, and weight file)

### hyenadna-medium-450k-seqlen-hf/config.json (Hugging Face blob at commit 8ddebc5...)

- URL: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json
- Publisher: LongSafari (Hugging Face model repository)
- Type: `repository`
- Primary because: Checkpoint config.json blob provides checkpoint-scoped model_type, hyperparameters, AutoModel mappings, and max sequence length used throughout the dossier.
- Scope: hyenadna-medium-450k-seqlen-hf (config.json blob)
- Supports: Checkpoint model_type 'hyenadna' and architecture mapping to HyenaDNAForCausalLM
- Supports: Hyperparameters: n_layer=8, d_model=256, d_inner=1024, emb_dim=5, max_seq_len=450002, vocab_size=12, pad_token_id=4
- Supports: AutoModelForCausalLM mapping to modeling_hyena.HyenaDNAForCausalLM

### hyenadna-medium-450k-seqlen-hf/tokenizer_config.json (Hugging Face blob)

- URL: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json
- Publisher: LongSafari (Hugging Face model repository)
- Type: `repository`
- Primary because: Tokenizer configuration blob for the checkpoint that declares tokenizer class, model_max_length, and special-token entries.
- Scope: hyenadna-medium-450k-seqlen-hf (tokenizer_config.json blob)
- Supports: Tokenizer class 'HyenaDNATokenizer' and model_max_length 450,002
- Supports: Declared special tokens including [PAD], [SEP], [UNK] and padding_side 'left'

### hyenadna-medium-450k-seqlen-hf/tokenization_hyena.py (Hugging Face blob)

- URL: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py
- Publisher: LongSafari (Hugging Face model repository)
- Type: `repository`
- Primary because: Tokenizer implementation for the checkpoint containing explicit token-to-id mapping, character token set, and tokenization behavior.
- Scope: hyenadna-medium-450k-seqlen-hf (tokenization_hyena.py blob)
- Supports: Definition of HyenaDNATokenizer class and model input names ['input_ids','attention_mask']
- Supports: Definition of special token strings and tokenizer _tokenize behavior returning individual characters

### hyenadna-medium-160k-seqlen/README.md (blame view) — related checkpoint README

- URL: https://huggingface.co/LongSafari/hyenadna-medium-160k-seqlen/blame/main/README.md
- Publisher: LongSafari (Hugging Face model repository)
- Type: `repository`
- Primary because: README for a related HyenaDNA checkpoint used only for the narrow fact that the README demonstrates character tokenizer examples and declares a license string; included to support provenance claims that appear in the inspected blobs.
- Scope: hyenadna-medium-160k-seqlen (related README, not the hyenadna-medium-450k checkpoint)
- Supports: Example code showing character tokenizer for DNA characters 'A','C','G','T','N'
- Supports: Declaration of license string 'bsd-3-clause' in that README (applies to that README/checkpoint)

### hyenadna-medium-450k-seqlen-hf/model.safetensors (weights file blob)

- URL: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/model.safetensors
- Publisher: LongSafari (Hugging Face model repository)
- Type: `repository`
- Primary because: Checkpoint weight file listed in the model repository file listing; used to verify presence of a weights artifact for this checkpoint (no weights license metadata found in the inspected blobs).
- Scope: hyenadna-medium-450k-seqlen-hf (weights file listed in repository)
- Supports: Presence of a weights file named model.safetensors for this checkpoint

### hyenadna-medium-450k-seqlen-hf config.json commit view (commit 8ddebc5...)

- URL: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/commits/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json
- Publisher: LongSafari (Hugging Face model repository)
- Type: `repository`
- Primary because: Commit view used to identify the specific uploaded config.json revision and associated commit metadata.
- Scope: hyenadna-medium-450k-seqlen-hf (commit view for config.json)
- Supports: Locator for revision hash 8ddebc527c28dca5d142fdacbaa82f519dba4d30 and evidence of the config.json upload

## Evidence gaps

- Evidence gap: Exact numeric benchmark values tied explicitly to the hyenadna-medium-450k-seqlen-hf checkpoint are not present in the inspected primary-source locators. Checked locators: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf and https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json (no tables/rows mapping benchmark numbers to this filename).
- Evidence gap: Exact parameter count for the hyenadna-medium-450k-seqlen-hf checkpoint is not reported in the inspected primary-source artifacts. Checked locators: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json and the model page.
- Evidence gap: The model-weights license for hyenadna-medium-450k-seqlen-hf is not declared in the inspected checkpoint blobs or model page. Checked locators: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf and https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json (related README for a different checkpoint declares 'bsd-3-clause' but does not establish checkpoint-scoped weights license for this checkpoint).
- Evidence gap: Embedding dimensionality, pooling semantics, and explicit embedding JSON schema for hyenadna-medium-450k-seqlen-hf are not present in the inspected blobs or model page. Checked locators: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf and https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json.
- Evidence gap: Inference-time input-handling policies (truncate vs sliding-window, default stride, batching semantics, accepted file header formats) for hyenadna-medium-450k-seqlen-hf are not specified in the inspected checkpoint blobs or model page. Checked locators: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf , https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json , and https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json.
- Evidence gap: Checkpoint-scoped calibration procedures or checkpoint-level confidence-interval reporting for hyenadna-medium-450k-seqlen-hf are not present in the inspected primary-source locators. Checked locators: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf and https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/8ddebc527c28dca5d142fdacbaa82f519dba4d30/config.json.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2] uses unapproved repository owner 'collections' for this exact model scope: $.sources[2] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen/blame/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen/tree/main Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
