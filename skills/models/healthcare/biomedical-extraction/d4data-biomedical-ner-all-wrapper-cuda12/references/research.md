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

- Research key: `huggingface-co-d4data-biomedical-ner-all-f38c6d2cfe`
- Independent audit: `revised`
- Researched: `2026-08-06T11:07:00.468816+00:00`

d4data/biomedical-ner-all is a DistilBertForTokenClassification checkpoint built on distilbert-base-uncased. The repository config.json documents a DistilBERT token-classification model with 6 transformer layers, 12 attention heads, hidden_dim 3072, embedding dim 768, vocabulary size 30,522, and max_position_embeddings 512. The model card and README provide Hugging Face Transformers example usage (AutoTokenizer.from_pretrained and AutoModelForTokenClassification.from_pretrained and a pipeline("ner", ..., aggregation_strategy="simple") example). There is a conflict in upstream statements about label-count: the README/blame view claims training on the Maccrobat dataset to recognize 107 biomedical entities, while the committed config.json id2label mapping enumerates 84 entries (keys 0 through 83). Primary sources do not report a model license, a parameter count, an explicit immutable revision to pin a wrapper to, nor public numeric benchmark tables or evaluation protocol details for named datasets/splits.

## Identity

- Upstream name: d4data/biomedical-ner-all
- Checkpoint/version: d4data/biomedical-ner-all
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: DistilBertForTokenClassification (base _name_or_path: distilbert-base-uncased); config.json reports model_type distilbert, n_layers=6, n_heads=12, hidden_dim=3072, dim=768, vocab_size=30522, max_position_embeddings=512, transformers_version=4.20.1, torch dtype=float32, attention_dropout=0.1, dropout=0.1, qa_dropout=0.1, seq_classif_dropout=0.2, initializer_range=0.02
- License: not reported
- Evidence: https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json, https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/7aa74de711ded74f1e4dd7af873d5ec4c5c608f9/config.json

## Selection

### Recommended

- **English biomedical named-entity recognition (token-level BIO tagging) using the checkpoint's id2label mapping.** — The model config (config.json) is a token-classification model with an id2label and label2id mapping enumerating BIO-tagged entity labels; the model card and README provide NER pipeline usage examples.
  Scope: d4data/biomedical-ner-all (upstream checkpoint)
  Evidence: https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md, https://huggingface.co/d4data/biomedical-ner-all

### Conditional

- **Running local inference via Hugging Face Transformers pipeline for NER with aggregation_strategy='simple' and optional GPU (device=0).** — Follow the repository README example: load tokenizer and model with AutoTokenizer.from_pretrained and AutoModelForTokenClassification.from_pretrained and construct pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple").
  Scope: d4data/biomedical-ner-all (upstream checkpoint)
  Evidence: https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md, https://huggingface.co/d4data/biomedical-ner-all
- **Accessing the model via the Hugging Face Inference API (as an alternative to local loading).** — Model page and README reference the Hugging Face Inference API; follow provider API docs for request/response shapes (provider docs are outside these primary sources and do not establish a Forge wrapper contract).
  Scope: d4data/biomedical-ner-all (upstream checkpoint)
  Evidence: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

### Avoid

- **Clinical decision making or diagnostic deployment without additional validation and expert oversight.** — Primary sources (model card and README) present the checkpoint as a research artifact and do not provide clinical validation, certifications, or deployment guidance for clinical use.
  Scope: d4data/biomedical-ner-all (upstream checkpoint)
  Evidence: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

## Input preparation

### Semantic inputs

- Plain English text strings (biomedical narrative, case-report style text) for token-level named-entity recognition. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

### Accepted formats

- Hugging Face Transformers usage: load tokenizer with AutoTokenizer.from_pretrained('d4data/biomedical-ner-all') and model with AutoModelForTokenClassification.from_pretrained('d4data/biomedical-ner-all'); example demonstrates pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy='simple'). Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md, https://huggingface.co/d4data/biomedical-ner-all

### Preprocessing

- Tokenizer class is DistilBertTokenizer; tokenizer_config.json sets do_lower_case = true and model_max_length = 512; special tokens defined include [CLS], [SEP], [PAD], [MASK], [UNK]; tokenize_chinese_chars is set to true in tokenizer_config.json. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/tokenizer_config.json, https://huggingface.co/d4data/biomedical-ner-all/blame/7aa74de711ded74f1e4dd7af873d5ec4c5c608f9/tokenizer_config.json
- Model and tokenizer maximum length are set to 512 tokens (tokenizer model_max_length = 512; config.json max_position_embeddings = 512). Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/tokenizer_config.json, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- Repository contains a vocab.txt file at blob/main/vocab.txt documenting the vocabulary; config.json records vocab_size = 30522 but the tokenizer vocabulary contents should be taken from the vocab.txt file in the repository. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/vocab.txt, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json

### Pre-submit validation

- Inputs exceeding the tokenizer/model maximum length (512 tokens) must be truncated or otherwise handled prior to inference; the configs report a 512-token limit but specific truncation details (truncation side or policy) are not specified in primary sources. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/tokenizer_config.json, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- No explicit input sanitation, PHI handling guidance, or other input-validation rules are provided in the model card or README. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

### Task-specific formatting

- The model uses a BIO tagging scheme for token classification; config.json contains id2label and label2id mappings with labels prefixed by B- and I- and an O label. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json, https://huggingface.co/d4data/biomedical-ner-all/commit/9c888473bf52f4c8cfdd99dcfb75c725d04c4b45
- Repository README shows pipeline usage with aggregation_strategy='simple' as an example; README also demonstrates passing device=0 for GPU execution in the example. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

## Output interpretation

### Outputs

- The checkpoint is for token classification; config.json provides id2label and label2id mappings that map integer label ids to BIO-tagged entity labels (config.json id2label contains keys 0..83 = 84 entries). Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json

### Interpretation

- Outputs should be interpreted as BIO token-classification labels per the id2label mapping in config.json. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- Primary sources do not specify how to map subword pieces to full-token labels (e.g., align-first-subword vs. aggregate) nor do they specify the exact runtime pipeline output JSON/object shape (fields, coordinate conventions, or whether logits/probabilities are returned). Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json

### Post-inference validation

- No post-inference calibration guidance, confidence thresholds, or recommended downstream validation procedures are provided in the model card or README; downstream validation is required by integrators. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- No license information is provided on the model card or repository pages checked; the model's legal/license status is unspecified in primary sources. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- No parameter count or explicit model size is reported in the primary sources. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- No public benchmark results, dataset-level evaluations, or numeric task performance metrics for named datasets/splits are published in the model card or repository files checked. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- Tokenizer/model truncation behavior (truncation side, token vs. character policy) and exact output object shapes (logits/probabilities and coordinate conventions) are not specified in the checked primary sources. Sources: https://huggingface.co/d4data/biomedical-ner-all/blob/main/tokenizer_config.json, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md
- Repository records training metadata (CO₂ emissions, training time, GPU used) but does not include formal evaluation/benchmark tables in the checked blobs. Sources: https://huggingface.co/d4data/biomedical-ner-all/blame/main/README.md
- Ambiguity between README claim of 107 entity types and config.json id2label enumerating 84 entries: the README/blame states 107 entity types while config.json lists 84 id2label entries (keys 0..83). Sources: https://huggingface.co/d4data/biomedical-ner-all/blame/main/README.md, https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json

### Safety

- Evidence gap: model card and README do not provide PHI/proprietary-data handling guidance or clinical validation instructions; integrators must apply institutional PHI handling policies and clinical validation independently. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md
- The model is documented as a research artifact in the checked sources (research topic attribution present); it is not documented with clinical-use approvals in primary sources. Sources: https://huggingface.co/d4data/biomedical-ner-all, https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### d4data/biomedical-ner-all (Hugging Face model page)

- URL: https://huggingface.co/d4data/biomedical-ner-all
- Publisher: Hugging Face / model maintainer d4data
- Type: `model-card`
- Primary because: Official Hugging Face model card/repository page for the checkpoint d4data/biomedical-ner-all.
- Scope: d4data/biomedical-ner-all
- Supports: Model identifier d4data/biomedical-ner-all
- Supports: Example usage with AutoTokenizer.from_pretrained and AutoModelForTokenClassification.from_pretrained
- Supports: Note that model can be accessed via Hugging Face Inference API
- Supports: Model described as part of research topic 'AI in Biomedical field'
- Supports: Repository provides no license metadata in the model card

### README.md (model repository blob)

- URL: https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Repository README in the official model repository providing usage examples and dataset/training notes.
- Scope: d4data/biomedical-ner-all
- Supports: Training on Maccrobat dataset claim (README/blame)
- Supports: Example Transformers pipeline usage with aggregation_strategy='simple' and device=0
- Supports: Research-topic attribution

### config.json (model configuration blob)

- URL: https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Model configuration file in the official repository containing architecture and id2label/label2id mappings and model hyperparameters.
- Scope: d4data/biomedical-ner-all (DistilBertForTokenClassification config)
- Supports: Architecture: DistilBertForTokenClassification built on distilbert-base-uncased
- Supports: Vocabulary size 30522 and max_position_embeddings 512
- Supports: BIO tagging scheme and id2label mapping enumerating entity labels (84 entries, keys 0..83)
- Supports: Transformer hyperparameters (n_layers=6, n_heads=12, hidden_dim=3072, dim=768, dropout and dtype fields)

### tokenizer_config.json (tokenizer configuration blob)

- URL: https://huggingface.co/d4data/biomedical-ner-all/blob/main/tokenizer_config.json
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Tokenizer configuration in the official repository declaring tokenizer class, special tokens, casing, and model_max_length.
- Scope: d4data/biomedical-ner-all (DistilBertTokenizer config)
- Supports: Tokenizer class DistilBertTokenizer
- Supports: Special tokens: [CLS], [SEP], [PAD], [MASK], [UNK]
- Supports: do_lower_case = true and model_max_length = 512
- Supports: tokenize_chinese_chars = true field present in config

### README.md blame entry with training metadata

- URL: https://huggingface.co/d4data/biomedical-ner-all/blame/main/README.md
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Blame view of README.md shows training metadata recorded in the repository.
- Scope: d4data/biomedical-ner-all
- Supports: Claim that model was trained on the Maccrobat dataset to recognize 107 biomedical entities
- Supports: Training emitted 0.0279399890043426 kilograms of CO₂
- Supports: Training time 30.16527 minutes
- Supports: Training GPU: 1 × GeForce RTX 3060 Laptop GPU

### config.json commit (label change evidence)

- URL: https://huggingface.co/d4data/biomedical-ner-all/commit/9c888473bf52f4c8cfdd99dcfb75c725d04c4b45
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Repository commit showing changes to config.json and label mappings.
- Scope: d4data/biomedical-ner-all (config.json history)
- Supports: Commit shows label replacement/removal in id2label/label2id mappings (example: removal of 'I-Nonbiological_location')

### config.json commit history listing

- URL: https://huggingface.co/d4data/biomedical-ner-all/commits/main/config.json
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Repository commit history showing updates to config.json with multiple commit hashes.
- Scope: d4data/biomedical-ner-all (config.json history)
- Supports: Commit history entries for config.json including multiple commit hashes

### config.json at specific commit (7aa74de) blob

- URL: https://huggingface.co/d4data/biomedical-ner-all/blob/7aa74de711ded74f1e4dd7af873d5ec4c5c608f9/config.json
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: A specific committed snapshot of config.json present in the repository.
- Scope: d4data/biomedical-ner-all (config.json snapshot)
- Supports: Configuration snapshot showing vocabulary size, n_heads, n_layers, hidden_dim, dropout parameters, dtype float32

### tokenizer_config.json blame at commit 7aa74de

- URL: https://huggingface.co/d4data/biomedical-ner-all/blame/7aa74de711ded74f1e4dd7af873d5ec4c5c608f9/tokenizer_config.json
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Blame view for tokenizer_config.json at a specific commit showing tokenizer fields and history.
- Scope: d4data/biomedical-ner-all (tokenizer_config.json history)
- Supports: Tokenization fields (do_lower_case, model_max_length, special tokens) and history at specific commit

### vocab.txt (tokenizer vocabulary blob)

- URL: https://huggingface.co/d4data/biomedical-ner-all/blob/main/vocab.txt
- Publisher: Hugging Face / model maintainer d4data
- Type: `repository`
- Primary because: Tokenizer vocabulary file present in the official repository.
- Scope: d4data/biomedical-ner-all (tokenizer vocabulary)
- Supports: Presence of a vocab.txt file for the checkpoint tokenizer (vocabulary contents available in repository blob)

## Evidence gaps

- No explicit model license information was found in the model card, README, or repository files checked (checked sources: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md; https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json).
- No parameter count (number of parameters) or model-size statement was present in the checked primary sources (checked: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json).
- No public benchmark results, dataset/split/metric numeric values, or evaluation tables for named datasets were found for this checkpoint in the checked primary sources (checked: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md; https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json).
- Exact tokenizer vocabulary contents are present in vocab.txt but a documented mapping from config.json vocab_size to the vocabulary file's canonical path is not explicitly stated beyond the presence of blob/main/vocab.txt (checked: https://huggingface.co/d4data/biomedical-ner-all/blob/main/vocab.txt; https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json).
- Precise runtime I/O contract details were not specified in the model card or README: the exact output JSON/object shape returned by the packaged pipeline, whether logits/probabilities/confidence fields are included, and the coordinate/index convention (token indices vs. character-span offsets) were not documented in the checked sources (checked: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md; https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json).
- Truncation/cropping specifics (truncation side, token vs. character truncation policy) are not stated in the tokenizer or model configs; only model_max_length and max_position_embeddings = 512 were found (checked: https://huggingface.co/d4data/biomedical-ner-all/blob/main/tokenizer_config.json; https://huggingface.co/d4data/biomedical-ner-all/blob/main/config.json).
- No explicit guidance on PHI/proprietary-data handling or clinical validation and deployment was found in the checked primary sources (checked: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md).
- No explicit statement in the checked repository files ties a Forge wrapper slug/version to an immutable upstream checkpoint tag or published revision; the repository contains commits but does not present a declared immutable release identifier to bind a wrapper (checked: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/commits/main/config.json).
- No direct comparison data versus alternative Forge candidates were found in the checked primary sources for d4data/biomedical-ner-all (no cross-model benchmark tables or comparative statements were present in the checked blobs).
- No evaluation protocol details (prompting, fine-tuning, ensembling, dataset split names) were found in the model card or README; therefore no numeric benchmark claims could be recorded (checked: https://huggingface.co/d4data/biomedical-ner-all; https://huggingface.co/d4data/biomedical-ner-all/blob/main/README.md).
- Ambiguity: README/blame claims the model recognizes 107 biomedical entity types (Maccrobat) while config.json id2label enumerates 84 entries (keys 0..83); the primary sources disagree on entity-count and no reconciliation is provided in the checked blobs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[8] uses unapproved repository owner 'risspecct' for this exact model scope: $.sources[8] uses unapproved repository owner 'risspecct' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/d4data/biomedical-ner-all/blame/7aa74de711ded74f1e4dd7af873d5ec4c5c608f9/tokenizer_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.inputPreparation.preprocessingEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
