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

- Research key: `huggingface-co-intfloat-multilingual-e5-large-instruct-2111b36652`
- Independent audit: `revised`
- Researched: `2026-08-06T11:43:40.914012+00:00`

Checkpoint-scoped summary: The intfloat/multilingual-e5-large-instruct checkpoint is an instruction-tuned multilingual text embeddings model initialized from xlm-roberta-large. The model configuration lists XLMRobertaModel with hidden_size=1024, 24 transformer layers, 16 attention heads, intermediate_size=4096, activation gelu, and vocab_size=250002 (config.json). The model and README state an embedding size of 1024 and show example usage that produces L2-normalized embeddings (model.encode(..., normalize_embeddings=True)). Tokenizer configuration (tokenizer_config.json) sets model_max_length=512 and the README/model card state long texts are truncated to at most 512 tokens; config.json lists max_position_embeddings=514, creating an ambiguity between tokenizer-declared max length (512) and config max_position_embeddings (514). The model card and README cite the technical report (arXiv:2402.05672) and record first-stage contrastive pre-training on ~1 billion weakly supervised text pairs and subsequent fine-tuning on datasets described in the Multilingual E5 technical report. Repository commit history contains evidence of model weight upload (commit d9f1d8f). Primary-source numeric benchmark tables (e.g., BEIR/MTEB/Mr. TyDi) for this exact instruction-tuned checkpoint are not present in the supplied primary findings; numeric reproduction claims are therefore an evidence gap for checkpoint-scoped benchmark numbers. No canonical license file content was found in the supplied findings.

## Identity

- Upstream name: intfloat/multilingual-e5-large-instruct
- Checkpoint/version: intfloat/multilingual-e5-large-instruct
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: XLMRobertaModel; hidden_size=1024; num_hidden_layers=24; num_attention_heads=16; intermediate_size=4096; hidden_act=gelu; vocab_size=250002
- License: not reported
- Evidence: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/commits/d9f1d8f4923684efb70ce5eaba66c3d3c8703406/.gitattributes, https://arxiv.org/pdf/2402.05672

## Selection

### Recommended

- **Multilingual semantic search / instruction-conditioned retrieval** — Model card and README describe the model as an embeddings model intended for multilingual retrieval and show instruction-conditioned query formatting and instruction-focused examples; embeddings are produced and normalized for retrieval workflows.
  Scope: intfloat/multilingual-e5-large-instruct
  Evidence: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md

### Conditional

- **Deployment on low-resource languages (requires per-language validation)** — Model card and README state performance may degrade for low-resource languages; therefore deployments must validate retrieval quality on the specific low-resource languages of interest before relying on production decisions.
  Scope: intfloat/multilingual-e5-large-instruct
  Evidence: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md
- **Instruction-conditioned query encoding (templates must be validated for task)** — The README mandates each query be prefixed with a one-sentence instruction and shows the instruction format; users must validate that their chosen instruction templates produce acceptable retrieval results for their tasks.
  Scope: intfloat/multilingual-e5-large-instruct
  Evidence: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct

### Avoid

- **Applying the checkpoint without instruction conditioning on the query side (for instruction‑tuned use)** — README explicitly requires each query be prefixed with a one-sentence instruction and the model card notes that omitting instructions degrades performance; therefore using the checkpoint in instruction-tuned mode without query instructions is unsupported by the canonical documentation.
  Scope: intfloat/multilingual-e5-large-instruct
  Evidence: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct

## Input preparation

### Semantic inputs

- Multilingual plain-text inputs intended as queries (instruction-conditioned) or documents/contexts for retrieval; instructions should be added to the query side only. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct
- The model supports languages inherited from xlm-roberta (model card/README state support for ~100 languages) and consumes textual data for embedding generation. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md

### Accepted formats

- Repository examples load the model as a SentenceTransformer using SentenceTransformer('intfloat/multilingual-e5-large-instruct'); tokenizer class is XLMRobertaTokenizer per tokenizer_config.json. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json

### Preprocessing

- Model card and README state that long texts will be truncated to at most 512 tokens and example tokenizer configuration sets model_max_length to 512 (tokenizer_config.json). Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json
- Config.json lists max_position_embeddings = 514; this differs from tokenizer model_max_length=512 and the README/model card truncation note—this is an explicit ambiguity between config.json and tokenizer_config.json/model card statements. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct
- The README shows example encode usage that requests conversion to a tensor and normalization (model.encode(..., convert_to_tensor=True, normalize_embeddings=True)); token-level pooling and masking (average_pool) are provided in the README as an example for producing sequence-level embeddings. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md
- Tokenizer configuration (tokenizer_config.json) declares special tokens and token ids (bos: <s>, pad: <pad>, eos: </s>, unk: <unk>, mask: <mask>) and tokenizer_class XLMRobertaTokenizer. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json

### Pre-submit validation

- Verify presence of a one-sentence instruction prefix on the query side as required by the README; the model card and README warn that omitting instructions degrades performance. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct
- Validate tokenization/truncation behavior in the deployed runtime because tokenizer_config.json model_max_length=512 and config.json max_position_embeddings=514 are inconsistent; ensure actual tokenization truncation aligns with intended max length for application logic. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct

### Task-specific formatting

- The README documents the instruction format used in examples as: 'Instruct: {task_description}\nQuery: {query}' and states that no instruction needs to be added for retrieval documents (only queries require instructions). Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct

## Output interpretation

### Outputs

- The checkpoint produces 1024-dimensional embeddings (model card and README state embedding size 1024; config hidden_size=1024 supports this dimensionality). Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md
- Embeddings are produced and normalized in examples; the README example uses model.encode(..., normalize_embeddings=True) which applies L2 normalization to the output vectors. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct
- Model config records torch dtype = float16 for the model (config.json); an explicit per-embedding output dtype (e.g., tensor dtype returned by the SentenceTransformer wrapper in a given runtime) is not stated in the primary findings. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md

### Interpretation

- Because examples normalize embeddings to unit length (L2 normalization), use cosine similarity or dot-product on normalized vectors for similarity comparisons; the README demonstrates normalized output in code examples. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md
- Do not assume per-embedding dtype or numeric range beyond canonical normalization behavior; the primary sources do not specify per-output tensor dtype guarantees beyond model config declaring float16. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json

### Post-inference validation

- Post-inference checks should confirm embeddings are normalized (unit length) and that tokenization/truncation matched expected max length in the deployed runtime; the README and model card instruct normalization and truncation behavior but the config/tokenizer files show an ambiguity in max length. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json
- The primary findings do not provide recommended numeric thresholds for downstream decisioning or calibration procedures; users must derive and validate thresholds for their specific application. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://arxiv.org/pdf/2402.05672

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Low-resource language degradation: the model card and README warn that performance may degrade for low-resource languages despite broad language support. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md
- Training data and provenance: the model card cites the Multilingual E5 technical report which documents first-stage contrastive pre-training on ~1 billion weakly supervised text pairs and subsequent fine-tuning on datasets described in the paper; details beyond this citation are in the technical report. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://arxiv.org/pdf/2402.05672
- Ambiguity in maximum sequence length: tokenizer_config.json sets model_max_length=512 and the README/model card state truncation to at most 512 tokens, while config.json lists max_position_embeddings=514. This discrepancy between tokenizer_config.json/model card and config.json is an explicit evidence ambiguity in the primary sources. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct
- Checkpoint-scoped benchmark gaps: the primary findings (model card, README, and config) do not contain numeric BEIR/MTEB/Mr. TyDi benchmark tables or per-dataset numeric results for this exact instruction-tuned checkpoint; numeric benchmark values are therefore an evidence gap at checkpoint scope. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://arxiv.org/pdf/2402.05672
- License absence: no canonical license file or explicit license text was present in the supplied primary findings for this repository; license text is an evidence gap in the primary sources provided. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json
- Per-output dtype and per-dimension semantic labels are not specified in the primary findings; the model config lists torch dtype=float16 but the per-embedding output dtype in a given runtime is not documented in the primary sources. Sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md

### Safety

- Evidence gap: The supplied primary findings do not include creator-provided clinical, PHI, or domain-specific data-handling guidance for this checkpoint; no explicit PHI or clinical-use disclaimers were found in the model card, README, or config.
- Evidence gap: The supplied primary findings do not include explicit biosecurity or specialized domain safety mitigations for this checkpoint; users must perform domain-specific validation and conservative safety review where appropriate.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### intfloat/multilingual-e5-large-instruct - Hugging Face

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct
- Publisher: Hugging Face (model card for intfloat/multilingual-e5-large-instruct)
- Type: `model-card`
- Primary because: Official model card and main repository page for this checkpoint; first-party documentation for the checkpoint.
- Scope: intfloat/multilingual-e5-large-instruct (model card, main page)
- Supports: Model cited paper Multilingual E5 technical report (arXiv:2402.05672)
- Supports: Long texts will be truncated to at most 512 tokens (model card statement)
- Supports: Model has 24 transformer layers (model card/README statement)
- Supports: Embedding size 1024 (model card/README statement)
- Supports: Model initialized from xlm-roberta-large (model card/README statement)
- Supports: Supports ~100 languages inherited from xlm-roberta (model card/README statement)
- Supports: Performance may degrade for low-resource languages (model card/README statement)
- Supports: First-stage training contrastive pre-training on ~1 billion weakly supervised text pairs (model card cites paper)
- Supports: Instruction requirement and examples for queries (model card/README)

### intfloat/multilingual-e5-large-instruct/README.md - Hugging Face repository

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md
- Publisher: Hugging Face (repository README for checkpoint)
- Type: `repository`
- Primary because: Repository README is first-party documentation accompanying the checkpoint and contains usage examples, instruction format, and Docker/Infinity example.
- Scope: intfloat/multilingual-e5-large-instruct (README)
- Supports: Each query must be prefixed with a one-sentence instruction (README explicit statement)
- Supports: Instruction format example: 'Instruct: {task_description}\nQuery: {query}' (README example)
- Supports: Example encode usage with convert_to_tensor=True and normalize_embeddings=True (README example)
- Supports: Provides Infinity Docker example including --dtype float16 and --batch-size 32 (README example)
- Supports: States no instruction needed for retrieval documents (README)

### intfloat/multilingual-e5-large-instruct/config.json - Hugging Face repository

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json
- Publisher: Hugging Face (checkpoint config)
- Type: `repository`
- Primary because: Checkpoint configuration file is first-party and records architecture and numeric configuration values for the model.
- Scope: intfloat/multilingual-e5-large-instruct (config.json)
- Supports: architecture = XLMRobertaModel
- Supports: hidden_size = 1024
- Supports: intermediate_size = 4096
- Supports: num_hidden_layers = 24
- Supports: num_attention_heads = 16
- Supports: hidden_act = gelu
- Supports: max_position_embeddings = 514
- Supports: vocab_size = 250002
- Supports: torch dtype = float16

### intfloat/multilingual-e5-large-instruct commit 1a50ec2 - Hugging Face

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct/commit/1a50ec20f8e2fffa5fdc52d5c5c72e2911a66f7a
- Publisher: Hugging Face (repository commits)
- Type: `repository`
- Primary because: Commit history entry is first-party evidence of repository changes (README updates and examples).
- Scope: intfloat/multilingual-e5-large-instruct (commit 1a50ec2)
- Supports: README updated to include Infinity usage and instruction changes (commit metadata/commit message)

### intfloat/multilingual-e5-large-instruct commits listing (README.md) - Hugging Face

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct/commits/refs%2Fpr%2F31/README.md
- Publisher: Hugging Face (repository commits listing)
- Type: `repository`
- Primary because: Commit listing shows commits that updated README, added Sentence Transformers support, added paper link, and other first-party changes.
- Scope: intfloat/multilingual-e5-large-instruct (commits listing for README.md)
- Supports: Commits indicating README changes, addition of Sentence Transformers support, and link to the paper

### intfloat/multilingual-e5-large-instruct commit d9f1d8f .gitattributes (weights upload marker) - Hugging Face

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct/commits/d9f1d8f4923684efb70ce5eaba66c3d3c8703406/.gitattributes
- Publisher: Hugging Face (repository commits)
- Type: `repository`
- Primary because: Commit entry documents an upload of model weights in the repository commit history.
- Scope: intfloat/multilingual-e5-large-instruct (commit d9f1d8f)
- Supports: Commit hash d9f1d8f uploaded model weights (commit metadata)

### intfloat/multilingual-e5-large-instruct/onnx/tokenizer_config.json - Hugging Face repository

- URL: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json
- Publisher: Hugging Face (tokenizer configuration file)
- Type: `repository`
- Primary because: Tokenizer configuration is first-party and records tokenizer_class, special tokens, and model_max_length used with the checkpoint.
- Scope: intfloat/multilingual-e5-large-instruct (tokenizer_config.json blob)
- Supports: tokenizer_class = XLMRobertaTokenizer
- Supports: model_max_length = 512
- Supports: Defines special tokens and their ids (bos, pad, eos, unk, mask)
- Supports: Lists no additional_special_tokens

### Multilingual E5 Text Embeddings: A Technical Report (arXiv:2402.05672)

- URL: https://arxiv.org/pdf/2402.05672
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical technical report cited by the model card and README; first-party preprint describing Multilingual E5 training methodology and variants.
- Scope: Multilingual E5 technical report (paper)
- Supports: Describes multilingual E5 models and training methodology (cited by the model card/README)
- Supports: Documents contrastive pre-training and supervised fine-tuning stages (paper content as cited by model card)

## Evidence gaps

- No canonical license file text for intfloat/multilingual-e5-large-instruct was present in the supplied primary findings; canonical repository license path or file contents were not found in the provided sources (checked model card and config.json). See sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json.
- No checkpoint-scoped numeric BEIR, MTEB, or Mr. TyDi benchmark tables or per-dataset numeric results for the instruction-tuned multilingual-e5-large-instruct checkpoint are present in the supplied primary findings (model card/README/config and cited arXiv do not include numeric tables for this exact checkpoint in the provided findings). See sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://arxiv.org/pdf/2402.05672.
- Tokenizer/config ambiguity: tokenizer_config.json sets model_max_length=512 and the model card/README state truncation to at most 512 tokens, while config.json lists max_position_embeddings = 514; the primary findings do not reconcile whether the effective maximum token length for inference is 512 or 514. See sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/12f5e10ae4575a6c3ef154c80e248ee3f24203c7/onnx/tokenizer_config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct.
- Per-embedding output dtype is not explicitly stated in the primary findings: config.json records model torch dtype = float16 but the README examples do not assert the runtime tensor dtype returned by the SentenceTransformer wrapper; explicit per-output dtype documentation is missing. See sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/config.json, https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md.
- No canonical Hugging Face Text Embeddings Inference (TEI) or Forge runtime HTTP request/response contract examples are present in the supplied primary findings; the README provides an Infinity Docker example but not an official TEI/Forge contract in the primary sources. See sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct/blob/main/README.md, https://huggingface.co/intfloat/multilingual-e5-large-instruct.
- No checkpoint-scoped numeric benchmark comparisons against alternative Forge candidates are present in the supplied primary findings; therefore task- and protocol-matched comparisons cannot be produced from the provided sources. See sources: https://huggingface.co/intfloat/multilingual-e5-large-instruct, https://arxiv.org/pdf/2402.05672.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
