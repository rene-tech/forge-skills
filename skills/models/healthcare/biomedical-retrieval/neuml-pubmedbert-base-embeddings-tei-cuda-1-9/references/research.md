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

- Research key: `huggingface-co-neuml-pubmedbert-base-embeddings-537c836d9d`
- Independent audit: `revised`
- Researched: `2026-08-06T08:48:38.370058+00:00`

Checkpoint-scoped summary for NeuML/pubmedbert-base-embeddings at commit b79526d6ef3645e0df4530322e266f24c829f5ef: The repo blobs at the cited commit record a BERT-base architecture (config.json -> "architectures" = ["BertModel"]) with hidden_size = 768, num_hidden_layers = 12, num_attention_heads = 12, max_position_embeddings = 512, vocab_size = 30522, torch_dtype = "float32", and transformers_version = "4.34.0" as captured in the commit-scoped config.json. The tokenizer_config.json at the commit records tokenizer_class = "BertTokenizer", do_lower_case = true, do_basic_tokenize = true, model_max_length (a very large integer value present in the blob), and standard special tokens (cls/sep/pad/mask/unk). The commit page documents an update to README.md at this commit (change in a README line referencing PubMedBERT). The inspected checkpoint-scoped blobs do not provide an explicit parameter count, a LICENSE blob or explicit license statement for the checkpoint, an explicit tokenizer vocab file blob path at this commit, numeric benchmark tables (MTEB or other) in the checked blobs, training-objective/loss details, PHI/data-governance or clinical-use guidance, or reproducibility/determinism guarantees; those items are recorded as evidence gaps with the exact commit-scoped blob URLs checked.

## Identity

- Upstream name: NeuML/pubmedbert-base-embeddings
- Checkpoint/version: commit b79526d6ef3645e0df4530322e266f24c829f5ef
- Immutable revision: b79526d6ef3645e0df4530322e266f24c829f5ef
- Parameter scale: not reported
- Architecture/head: architectures = ["BertModel"]; hidden_size = 768; num_hidden_layers = 12; num_attention_heads = 12; max_position_embeddings = 512; vocab_size = 30522; transformers_version = 4.34.0 (as recorded in config.json at the cited commit)
- License: not reported
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

## Selection

### Recommended

- **Biomedical sentence and paragraph semantic embeddings for clustering and semantic search** — Evidence gap: The inspected checkpoint-scoped blobs (commit page, config.json, tokenizer_config.json at the cited commit) do not contain an explicit upstream recommended-use statement for this exact checkpoint; the model's config and tokenizer blobs record architecture and tokenizer metadata but do not themselves assert recommended downstream use cases.
  Scope: NeuML/pubmedbert-base-embeddings (commit b79526d6ef3645e0df4530322e266f24c829f5ef)
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

### Conditional

- **Biomedical retrieval / embedding-based semantic search with downstream validation** — Condition: Downstream system owners must validate this checkpoint's embeddings on their specific dataset/split and retrieval protocol because no checkpoint-scoped numeric benchmark rows or protocol details are present in the inspected blobs.
  Scope: NeuML/pubmedbert-base-embeddings (commit b79526d6ef3645e0df4530322e266f24c829f5ef)
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- **Any regulated / clinical decision-making use** — Evidence gap: The inspected checkpoint-scoped blobs do not provide PHI/data-governance guidance, clinical-use validation, or regulatory compliance instructions; expert review and formal regulatory validation are required before clinical deployment.
  Scope: NeuML/pubmedbert-base-embeddings (commit b79526d6ef3645e0df4530322e266f24c829f5ef)
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

### Avoid

- **Direct clinical decision-making without expert review and validation** — Evidence gap: The inspected checkpoint-scoped blobs (commit page, config.json, tokenizer_config.json at the cited commit) do not provide checkpoint-scoped clinical-use validation, PHI-handling guidance, or regulatory compliance instructions.
  Scope: NeuML/pubmedbert-base-embeddings (commit b79526d6ef3645e0df4530322e266f24c829f5ef)
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

## Input preparation

### Semantic inputs

- Sentences or paragraphs of biomedical text (semantic input type inferred as text encoder inputs); the inspected blobs document tokenizer and model architecture but do not contain explicit training-data provenance beyond the README change noted on the commit page. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json

### Accepted formats

- Text input for an encoder-based tokenizer/embedding extractor (the repository blobs include tokenizer and model configuration appropriate for text encoder use). Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json

### Preprocessing

- Tokenizer class and tokenization flags for the checkpoint are recorded in tokenizer_config.json at the cited commit: tokenizer_class = "BertTokenizer", do_lower_case = true, do_basic_tokenize = true. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json
- Model maximum position embeddings are recorded in config.json at the cited commit: max_position_embeddings = 512. The inspected blobs do not document serving-wrapper truncation defaults or tokenizer truncation behavior beyond the tokenizer/model config fields. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Special tokens (cls/sep/pad/mask/unk) are defined in tokenizer_config.json at the cited commit; no additional special tokens are listed. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json
- Evidence gap: No explicit tokenizer vocab file blob path (vocab.txt or tokenizer.json) was found in the inspected commit-scoped blobs; the exact repository blob path for the tokenizer vocab at this commit is not reported in the checked blobs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json

### Pre-submit validation

- Evidence gap: The inspected checkpoint-scoped blobs do not enumerate explicit input-validation rules (allowed charsets, PHI-handling instructions, tokenizer failure modes, or explicit truncation policies); no such guidance is present in the checked commit-scoped blobs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

### Task-specific formatting

- Evidence gap: No task-specific prompt tokens or special formatting for producing embeddings are documented in the inspected checkpoint-scoped blobs; tokenizer and model config record standard BERT tokenizer settings only. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json

## Output interpretation

### Outputs

- Produces a single dense embedding vector of dimension 768 as implied by config.json -> "hidden_size" = 768 at the cited commit; the blobs document the model hidden size but do not include an explicit embedding post-processing routine. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Torch dtype for the model is recorded in config.json at the cited commit as "float32" (config.json -> "torch_dtype"). Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json

### Interpretation

- Evidence gap: No upstream-specified post-processing interpretation (e.g., L2 normalization, per-embedding uncertainty, or calibrated scores) is present in the inspected checkpoint-scoped blobs; users should treat output vectors as uncalibrated dense embeddings unless downstream calibration is applied. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef

### Post-inference validation

- Evidence gap: No post-inference quality checks, calibration instructions, or reproducibility/determinism guarantees (seed usage, nondeterministic ops behavior) were found in the inspected checkpoint-scoped blobs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### No primary, checkpoint-scoped alternative with matching protocol found in inspected blobs — `insufficient-evidence`

- Task: embedding-retrieval
- Criteria: No checkpoint-scoped, protocol-matching primary evidence for numeric benchmark comparison was found in the inspected blobs for either this checkpoint or an alternative checkpoint in the same repository; therefore direct numeric comparisons are unsupported.
- Rationale: The inspected commit-scoped blobs (commit page, config.json, tokenizer_config.json) document model configuration and tokenizer metadata but do not contain numeric benchmark rows or a described, reproducible evaluation protocol for a comparable alternative checkpoint.
- Comparison conditions: Evidence gap: No matching checkpoint-scoped benchmark protocol or numeric results found in the checked primary blobs for either side of a comparison; checked URLs are the commit page and the commit-scoped config/tokenizer blobs.
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

## Limitations and safety

### Limitations

- Maximum position embeddings / context length is 512 tokens as recorded in config.json (config.json -> "max_position_embeddings" = 512) at the cited commit. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Tokenizer vocabulary size is recorded in config.json as 30522 (config.json -> "vocab_size" = 30522) at the cited commit; however, the explicit tokenizer vocab file blob path at this commit is not reported. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json
- Evidence gap: No checkpoint-scoped explicit parameter-count statement was found in the inspected commit-scoped blobs; parameter count for this exact commit is not reported in the checked primary blobs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef
- Evidence gap: No LICENSE file blob or explicit license statement for the checkpoint was found in the inspected commit-scoped blobs; checkpoint license is not reported in the checked primary blobs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json

### Safety

- Evidence gap: No upstream, checkpoint-scoped privacy, PHI-handling, clinical safety, or dual-use mitigation guidance was found in the inspected commit-scoped blobs; downstream deployers should apply governance and PHI controls appropriate to clinical or regulated contexts. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Evidence gap: The inspected commit-scoped blobs do not include model-specific recommendations for human-review thresholds, clinical validation procedures, or regulatory compliance pathways for this checkpoint. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef, https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NeuML / pubmedbert-base-embeddings commit b79526d6ef3645e0df4530322e266f24c829f5ef

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef
- Publisher: NeuML (Hugging Face repo)
- Type: `repository`
- Primary because: Exact commit page for the NeuML/pubmedbert-base-embeddings repository on Hugging Face; documents README update at the cited commit and is the canonical commit-scoped locator for other blobs.
- Scope: NeuML/pubmedbert-base-embeddings (commit b79526d6ef3645e0df4530322e266f24c829f5ef)
- Supports: evidence that README was updated at this commit and commit-scoped blob provenance

### NeuML / pubmedbert-base-embeddings config.json (repo blob at cited commit)

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Publisher: NeuML (Hugging Face repo)
- Type: `repository`
- Primary because: Commit-scoped config.json provides definitive model configuration fields for this checkpoint.
- Scope: NeuML/pubmedbert-base-embeddings (config.json at commit b79526d6ef3645e0df4530322e266f24c829f5ef)
- Supports: _name_or_path = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
- Supports: architectures = ["BertModel"]
- Supports: hidden_size = 768
- Supports: num_hidden_layers = 12
- Supports: num_attention_heads = 12
- Supports: max_position_embeddings = 512
- Supports: vocab_size = 30522
- Supports: torch_dtype = "float32"
- Supports: transformers_version = "4.34.0"

### NeuML / pubmedbert-base-embeddings tokenizer_config.json (repo blob at cited commit)

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json
- Publisher: NeuML (Hugging Face repo)
- Type: `repository`
- Primary because: Commit-scoped tokenizer_config.json provides tokenizer_class and tokenization flags for this checkpoint.
- Scope: NeuML/pubmedbert-base-embeddings (tokenizer_config.json at commit b79526d6ef3645e0df4530322e266f24c829f5ef)
- Supports: tokenizer_class = "BertTokenizer"
- Supports: do_lower_case = true
- Supports: do_basic_tokenize = true
- Supports: model_max_length present in the blob
- Supports: special tokens: cls/sep/pad/mask/unk defined
- Supports: additional_special_tokens = []

### Exact official starting source declared by Forge

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: neuml-pubmedbert-base-embeddings
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric MTEB or other benchmark rows (dataset/split/metric/value) were present in the inspected commit-scoped blobs; checked commit page and config/tokenizer blobs at the cited commit: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json
- Evidence gap: No checkpoint-scoped explicit parameter-count statement was found in the inspected commit-scoped blobs; checked: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json , https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef
- Evidence gap: No LICENSE file blob or explicit license statement for this checkpoint was found in the inspected commit-scoped blobs; checked: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Evidence gap: Tokenizer vocab file blob path (explicit repo blob path to vocab.txt or tokenizer.json at this commit) was not present in the inspected commit-scoped blobs; checked: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json , https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef
- Evidence gap: No checkpoint-scoped training-objective (loss) or similarity-function specification (e.g., MultipleNegativesRankingLoss) was found in the inspected commit-scoped blobs; checked: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json
- Evidence gap: No checkpoint-scoped PHI/data-governance or clinical-use guidance or regulatory compliance instructions were found in the inspected commit-scoped blobs; checked: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json
- Evidence gap: No checkpoint-scoped reproducibility/determinism guarantees (seed usage, nondeterministic ops behavior) or post-inference calibration instructions were found in the inspected commit-scoped blobs; checked: https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/config.json , https://huggingface.co/NeuML/pubmedbert-base-embeddings/blob/b79526d6ef3645e0df4530322e266f24c829f5ef/tokenizer_config.json , https://huggingface.co/NeuML/pubmedbert-base-embeddings/commit/b79526d6ef3645e0df4530322e266f24c829f5ef

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 27 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary host ai.azure.com: $.sources[6] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'blog' for this exact model scope: $.sources[7] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://huggingface.co/blog/mteb Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'microsoft' for this exact model scope: $.sources[9] uses unapproved repository owner 'microsoft' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'blog' for this exact model scope: $.sources[12] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/blog/NeuML/biomedbert-small Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary URL https: $.sources[13] uses forbidden secondary URL https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/what%E2%80%99s-trending-on-hugging-face-pubmedbert-base-embeddings-paraphrase-multilingu/4496185 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'ncbi' for this exact model scope: $.sources[14] uses unapproved repository owner 'ncbi' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses unapproved repository owner 'ncbi' for this exact model scope: $.sources[15] uses unapproved repository owner 'ncbi' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/neuml-pubmedbert-base-embeddings-2m Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/NeuML/pubmedbert-base-embeddings: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
