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

- Research key: `huggingface-co-ncbi-medcpt-cross-encoder-d1e8297dde`
- Independent audit: `revised`
- Researched: `2026-08-06T12:59:33.700753+00:00`

Using only canonical upstream repository artifacts, the repository ncbi/MedCPT-Cross-Encoder contains: a model config.json blob that identifies the implementation as BertForSequenceClassification (model_type 'bert') and reports hidden_size=768, num_hidden_layers=12, num_attention_heads=12, intermediate_size=3072, max_position_embeddings=512, vocab_size=30522, id2label/label2id mappings and torch dtype float32 (config.json blob). A tokenizer_config.json blob exists in the repository and contains tokenizer class and special-token fields; however the tokenizer_config.json also contains an internally inconsistent "model_max_length" numeric value (one field reports 512 as maximum length and another field presents an extremely large integer), producing an ambiguity in declared tokenizer maximum length. The repository README shows example usage calls to AutoTokenizer.from_pretrained and AutoModelForSequenceClassification and demonstrates a query string and ranking usage, and the README lists the model license as "public-domain". The canonical repository does not provide an explicit mapping from the Forge/Forge-wrapper version string hf-71caf65-wrapper-cuda12-safe-state-dict to an exact upstream repository checkpoint name or commit id; the repo does contain a commit (75e855e5) adding a safetensors variant of the model file. The upstream artifacts do not contain checkpoint-scoped numeric benchmark tables, an explicit per-checkpoint tokenizer vocab file blob path (other than tokenizer_config.json), an official query+candidate concatenation/truncation template, output-tensor semantics with calibrated probabilities or thresholds, nor explicit PHI/sanitization guidance; these absences are recorded as evidence gaps and the exact repository blobs checked are listed in the sources and evidenceGaps fields.

## Identity

- Upstream name: ncbi/MedCPT-Cross-Encoder
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: BertForSequenceClassification (model_type 'bert'; config fields verified in config.json: hidden_size=768, num_hidden_layers=12, num_attention_heads=12, max_position_embeddings=512, vocab_size=30522; id2label and label2id mappings present)
- License: public-domain (as listed in README.md; weights-vs-code distinction not reported)
- Evidence: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

## Selection

### Recommended

- **Biomedical query + candidate-article reranking (second-stage re-ranker)** — The repository README demonstrates loading the tokenizer and AutoModelForSequenceClassification and shows example usage for ranking articles for a given query; the config.json identifies a sequence-classification (cross-encoder) head consistent with reranking use.
  Scope: ncbi/MedCPT-Cross-Encoder (upstream repository artifacts: model config.json and README examples)
  Evidence: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

### Conditional

- **Research evaluation of reranking/IR pipelines using this cross-encoder as a second-stage scorer** — Requires downstream evaluation to validate ranking quality for the target dataset and to confirm input formatting (query+candidate concatenation/truncation) since no official checkpoint-scoped numeric benchmarks or an explicit concatenation/truncation template are present in the repository artifacts.
  Scope: ncbi/MedCPT-Cross-Encoder (upstream repository artifacts: config.json and README examples)
  Evidence: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

### Avoid

- **Direct diagnostic decision-making without clinical oversight** — Evidence gap: the upstream repository artifacts do not provide checkpoint-scoped clinical-use guidance, validation, or PHI/data-handling instructions; no upstream primary-source clinical disclaimer was located in the checked blobs, so clinical diagnostic use should be avoided unless separate validated clinical guidance and evaluation are provided.
  Scope: ncbi/MedCPT-Cross-Encoder (upstream repository artifacts checked)
  Evidence: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main

## Input preparation

### Semantic inputs

- A textual user query and candidate article text are the intended paired inputs for ranking; the README demonstrates providing a query string and using the model for ranking candidate articles. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

### Accepted formats

- The model is loadable from the Hugging Face Hub using AutoTokenizer.from_pretrained and AutoModelForSequenceClassification.from_pretrained as shown in the README example. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

### Preprocessing

- Model config.json specifies model_type 'bert' and max_position_embeddings 512, indicating an upper bound of 512 position embeddings declared in config.json. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json
- The repository contains a tokenizer_config.json blob that declares tokenizer class, special tokens, padding and truncation sides, and related tokenizer settings (see tokenizer_config.json blob); however the tokenizer_config.json also contains an inconsistent large integer value for model_max_length, creating ambiguity about the declared tokenizer maximum length. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/tokenizer_config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json

### Pre-submit validation

- Evidence gap: the upstream blobs do not provide a formal input-validation checklist (for example, explicit input-length checks, forbidden-content filters, or PHI-stripping guidance) for use with this checkpoint; repository blobs checked contain no PHI handling instructions. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/tokenizer_config.json

### Task-specific formatting

- Evidence gap: the repository does not present an explicit, canonical paired-input concatenation/prompt template (order, separator tokens, or truncation/cropping policy) for query+candidate pairs in the checked README or config/tokenizer blobs. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main

## Output interpretation

### Outputs

- Evidence gap: the upstream repository blobs do not explicitly document the numeric output tensor semantics (logits vs probabilities) or provide a canonical example output tensor in the checked blobs; the README demonstrates ranking usage but does not define calibrated score semantics. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

### Interpretation

- The model is presented in the README and config as a sequence-classification cross-encoder intended for ranking candidate articles for a query; however, no upstream guidance for interpreting raw numeric outputs (for example, whether outputs are logits or probabilities, or recommended thresholds) is provided in the checked blobs. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

### Post-inference validation

- Evidence gap: no checkpoint-scoped calibration guidance, recommended thresholds, or post-inference validation checks are provided in the upstream repository blobs; downstream validation is required before using numeric scores for decision-making. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: reranking / cross-encoder scoring
- Criteria: Evidence gap: no primary-source comparative benchmark tables or direct comparison rows were found in the checked upstream artifacts for this repository; no repository-local comparison entries to other specific checkpoints were present.
- Rationale: The upstream repository does not contain checkpoint-scoped numeric benchmark tables or explicit comparative evaluations in the checked blobs.
- Comparison conditions: Checked the model page, README.md, config.json, tokenizer_config.json, repository tree, and commit history for benchmark or comparison tables; none were found.
- Evidence: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/tokenizer_config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/commit/75e855e5aaeda1e16da04a894207072d4b0db66a

## Limitations and safety

### Limitations

- The upstream config.json does not report a parameter count for this repository checkpoint (parameter-scale metadata is not present in the checked config blob). Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json
- The model config restricts maximum position embeddings to 512 tokens (max_position_embeddings = 512 in config.json); the repository does not document an explicit long-text handling strategy for inputs exceeding this bound. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json
- Evidence gap: the upstream artifacts do not provide checkpoint-scoped numeric benchmark tables (dataset/split/metric/value) for this repository checkpoint. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main
- Evidence gap: tokenizer vocabulary file blobs (for example, a vocab.txt or tokenizer.json blob) and an explicit canonical special-token or tokenization/truncation ordering for query+candidate concatenation are not present in the checked upstream artifacts beyond tokenizer_config.json. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/tokenizer_config.json, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main

### Safety

- Evidence gap: the upstream repository blobs do not specify PHI/proprietary-data handling, sanitization, or input-filtering guidance for this checkpoint. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder, https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md
- The repository README lists the model license as "public-domain" (README license field); the upstream artifacts do not include a distinct weights-vs-code license separation statement in the checked blobs. Sources: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model page: ncbi/MedCPT-Cross-Encoder

- URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: First-party Hugging Face model repository page for ncbi/MedCPT-Cross-Encoder; serves as the canonical model card and repository entry.
- Scope: ncbi/MedCPT-Cross-Encoder (model repository and model card)
- Supports: Repository landing page and model card entries used to locate README, config, and tokenizer blobs and to confirm repository-level usage framing.

### config.json blob for ncbi/MedCPT-Cross-Encoder

- URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Direct model configuration blob listing architecture type and config fields for the repository's checkpoint artefacts.
- Scope: ncbi/MedCPT-Cross-Encoder (config.json blob)
- Supports: Architecture = BertForSequenceClassification / model_type 'bert'.
- Supports: hidden_size=768, num_hidden_layers=12, num_attention_heads=12, intermediate_size=3072, max_position_embeddings=512, vocab_size=30522, id2label and label2id mappings, torch dtype float32 and other config fields.

### tokenizer_config.json blob for ncbi/MedCPT-Cross-Encoder

- URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/tokenizer_config.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Tokenizer configuration blob for the repository that declares tokenizer class, special tokens, padding/truncation sides, and model_max_length field.
- Scope: ncbi/MedCPT-Cross-Encoder (tokenizer_config.json blob)
- Supports: Declares tokenizer class (BertTokenizer), padding_side and truncation_side (right), separator and special tokens names ([SEP], [UNK], [CLS], [PAD], [MASK]), do_lower_case and tokenize_chinese_chars flags, and includes a model_max_length field (with conflicting numeric values in repository blobs).

### README.md (blame view) for ncbi/MedCPT-Cross-Encoder

- URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md
- Publisher: Hugging Face
- Type: `repository`
- Primary because: First-party README shows example code usage and lists repository-level metadata such as license.
- Scope: ncbi/MedCPT-Cross-Encoder (README.md blob)
- Supports: Example usage loading AutoTokenizer and AutoModelForSequenceClassification from the repository and an example query string; lists the model license as 'public-domain'.

### Repository tree for ncbi/MedCPT-Cross-Encoder (main)

- URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Canonical repository tree view used to confirm presence/absence of blobs (tokenizer_config.json, config.json, model files) and to check for benchmark or documentation files.
- Scope: ncbi/MedCPT-Cross-Encoder (repository tree)
- Supports: Repository-level listing and presence/absence checks for tokenizer and config blobs and other files.

### Commit adding safetensors variant (commit 75e855e5)

- URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/commit/75e855e5aaeda1e16da04a894207072d4b0db66a
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository commit that adds a safetensors variant of the model file; provides an upstream checkpoint artifact addition.
- Scope: ncbi/MedCPT-Cross-Encoder (commit 75e855e5 and associated model file blob)
- Supports: Documents that a safetensors variant of the model was added in this commit and includes file-size and oid metadata in the commit listing.

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric benchmark tables (dataset, split, metric, numeric value) were found in the checked upstream artifacts (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/commit/75e855e5aaeda1e16da04a894207072d4b0db66a).
- Evidence gap: No explicit tokenizer vocabulary file blob (for example vocab.txt or tokenizer.json) or explicit canonical tokenizer model file path beyond tokenizer_config.json was found in the checked upstream artifacts (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/tokenizer_config.json).
- Evidence gap: No official query+candidate concatenation/prompt template (order, separator tokens, or truncation/cropping policy) for paired inputs was found in the checked upstream artifacts (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main).
- Evidence gap: The upstream artifacts do not provide explicit output semantics (logits vs probabilities), calibrated probability guidance, or recommended thresholds for downstream decision-making (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md).
- Evidence gap: The upstream artifacts do not include a checkpoint-scoped parameter count/parameter-scale metadata (checked URL: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json).
- Evidence gap: The upstream artifacts do not provide a separate weights-vs-code license distinction or explicit license text for the model weights file(s) beyond the repository-level license field in README (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main).
- Evidence gap: No explicit PHI/proprietary-data handling, sanitization, or input-filtering guidance for this checkpoint was found in the checked upstream artifacts (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blame/main/README.md ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main).
- Evidence gap: No checkpoint-scoped runtime/precision (for example FP16), latency, or wrapper/runtime-only deployment-performance notes are present in the checked upstream artifacts (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/blob/2bd05345f052f16cb82812fccd6460dff2c17d82/config.json).
- Evidence gap: The mapping between the Forge/Forge-wrapper version string 'hf-71caf65-wrapper-cuda12-safe-state-dict' and an exact upstream repository checkpoint or immutable commit id is not verifiable from the checked upstream artifacts (checked URLs: https://huggingface.co/ncbi/MedCPT-Cross-Encoder ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/tree/main ; https://huggingface.co/ncbi/MedCPT-Cross-Encoder/commit/75e855e5aaeda1e16da04a894207072d4b0db66a).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[0] uses forbidden secondary host ai.azure.com: $.sources[0] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'davidedm26' for this exact model scope: $.sources[9] uses unapproved repository owner 'davidedm26' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'omkaradhali' for this exact model scope: $.sources[10] uses unapproved repository owner 'omkaradhali' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretation_overview: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
