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

- Research key: `huggingface-co-neuml-pubmedbert-base-embeddings-matryoshka-751cba225c`
- Independent audit: `revised`
- Researched: `2026-07-24T00:09:40.570777+00:00`

The NeuML/pubmedbert-base-embeddings-matryoshka checkpoint is an official Hugging Face model-card/ repository release that exposes Matryoshka-style multi-resolution embeddings for biomedical text. The model card reports evaluated embedding dimensionalities 64, 128, 256, 384, 512, and 768 with per-dimension performance numbers on PubMed QA, PubMed Subset, and PubMed Summary (per-dimension numeric scores are published on the model card). Repository files include a SentenceTransformers configuration (sentence_transformers v2.4.0, transformers v4.36.2) and a pooling configuration that specifies word_embedding_dimension = 768 and pooling_mode_mean_tokens = true with include_prompt = true. The model page also documents Sentence-Transformers loadability and a txtai usage example. Primary upstream artifacts in the evidence set do not report a checkpoint-level revision identifier, explicit model-weight parameter count, tokenizer metadata (full tokenizer.json contents or explicit tokenizer name), or an explicit license string for the checkpoint; these are recorded as evidence gaps below.

## Identity

- Upstream name: NeuML/pubmedbert-base-embeddings-matryoshka
- Checkpoint/version: NeuML/pubmedbert-base-embeddings-matryoshka
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blame/main/config_sentence_transformers.json

## Selection

### Recommended

- **Sentence / paragraph embedding extraction for biomedical text (PubMed-style titles/abstracts)** — The model card reports per-dimension embedding evaluation results on PubMed QA, PubMed Subset, and PubMed Summary and the repository includes a SentenceTransformers configuration and pooling layer indicating intended use for sentence/paragraph embeddings.
  Scope: NeuML/pubmedbert-base-embeddings-matryoshka
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blame/main/config_sentence_transformers.json

### Conditional

- **Semantic retrieval, clustering, or retrieval-augmented generation (RAG) using lower-dimensional Matryoshka prefixes** — Validate retrieval/semantic-similarity performance on held-out task data for the chosen embedding dimensionality (the model card provides per-dimension numeric results for PubMed QA/Subset/Summary that should be re-measured for each target retrieval/indexing topology and dataset).
  Scope: NeuML/pubmedbert-base-embeddings-matryoshka (supported dims: 64,128,256,384,512,768 as reported on the model card)
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

### Avoid

- **Clinical decision-making or any clinical deployment that will directly influence patient care** — Primary upstream artifacts do not establish clinical validation, regulatory clearance, or clinical-grade performance for this exact checkpoint; the model card and repository files do not provide PHI handling guidance or clinical risk controls for this checkpoint.
  Scope: NeuML/pubmedbert-base-embeddings-matryoshka
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- **Embedding-based processing of protected health information (PHI) without institutional review and appropriate data-handling controls** — No explicit upstream guidance for PHI or operational data-handling for this checkpoint is present in the provided primary artifacts; treat PHI processing as requiring institutional policy and expert oversight.
  Scope: NeuML/pubmedbert-base-embeddings-matryoshka
  Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

## Input preparation

### Semantic inputs

- The model consumes text inputs intended as sentences or paragraphs to be embedded. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

### Accepted formats

- The checkpoint can be loaded with the sentence-transformers library and is presented in examples/usage as an embedding model; the model card and repository indicate use via SentenceTransformers and via txtai example usage. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Evidence gap: The provided primary artifacts do not explicitly document the exact accepted input data types/formats (e.g., single string vs list-of-strings API contract) required by the official loadable object; downstream code should validate expected input shape before bulk inference.

### Preprocessing

- Pooling and embedding post-processing are configured in the repository pooling file: mean-token pooling is enabled and the pooling layer reports word_embedding_dimension = 768 and include_prompt = true. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json
- Evidence gap: The primary artifacts in the evidence set do not disclose tokenizer identity details (tokenizer name) or full tokenizer.json contents beyond a repository commit listing; exact tokenization normalization rules, special-token strings, vocab size, pad_token_id, and max_position_embeddings are not reported in the provided facts.

### Pre-submit validation

- The model card does not provide an explicit upstream input-validation checklist (allowed character sets, explicit pre-tokenization sanitization rules, or disallowed content lists) for this exact checkpoint; implementers should perform input sanitization and sanity checks before embedding production inputs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Evidence gap: Exact tokenizer metadata and preprocessing parameter values required to guarantee tokenization compatibility are not available in the provided primary artifacts.

### Task-specific formatting

- The SentenceTransformers-related configuration file in the repository lists sentence_transformers v2.4.0 and contains an empty prompts object with default_prompt_name null; no prompt templates are defined in the provided configuration. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blame/main/config_sentence_transformers.json
- The model card reports and evaluates specific embedding dimensionalities (64,128,256,384,512,768); Matryoshka usage expects a dimensionality selection to choose the returned prefix length. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

## Output interpretation

### Outputs

- The checkpoint emits dense floating-point embedding vectors; the pooling layer reports word_embedding_dimension = 768 and the model card reports supported embedding prefixes/dimensionalities 64, 128, 256, 384, 512, and 768. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json
- Evidence gap: The primary artifacts do not explicitly state an enforced output normalization (e.g., cosine/L2 normalization) or the numeric output dtype in the provided facts; downstream pipelines should verify normalization and dtype when loading embeddings.

### Interpretation

- Embeddings represent semantic vector encodings of input text suitable for similarity comparisons and retrieval; the model card reports per-dimension empirical performance on PubMed QA/Subset/Summary to guide dimensionality tradeoffs. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Do not assume outputs are calibrated for decision thresholds or clinical use; no upstream guidance on mapping embedding distances to semantic labels or thresholds is provided in the evidence set. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

### Post-inference validation

- Post-inference validation should include: (a) verifying tokenization compatibility with the checkpoint's tokenizer, (b) verifying returned vector shape matches selected dimensionality, and (c) validating retrieval/similarity metrics on held-out task data prior to production use. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json
- Evidence gap: The primary artifacts do not provide recommended numeric thresholds, calibration procedures, or confidence scores for downstream decision-making with this checkpoint.

## Public benchmarks

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed QA / not reported
- Metric/value: score / Dimension 64: 92.16 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=64)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 64
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Subset / not reported
- Metric/value: score / Dimension 64: 96.14 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=64)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 64
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Summary / not reported
- Metric/value: score / Dimension 64: 95.67 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=64)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 64
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: Average (aggregated reported average per-dimension) / not reported
- Metric/value: score / Dimension 64 average: 94.66 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=64)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 64
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed QA / not reported
- Metric/value: score / Dimension 128: 92.80 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=128)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 128
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Subset / not reported
- Metric/value: score / Dimension 128: 96.58 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=128)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 128
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Summary / not reported
- Metric/value: score / Dimension 128: 96.22 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=128)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 128
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: Average (aggregated reported average per-dimension) / not reported
- Metric/value: score / Dimension 128 average: 95.20 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=128)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 128
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed QA / not reported
- Metric/value: score / Dimension 256: 93.11 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=256)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 256
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Subset / not reported
- Metric/value: score / Dimension 256: 96.82 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=256)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 256
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Summary / not reported
- Metric/value: score / Dimension 256: 96.53 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=256)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 256
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: Average (aggregated reported average per-dimension) / not reported
- Metric/value: score / Dimension 256 average: 95.49 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=256)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 256
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed QA / not reported
- Metric/value: score / Dimension 384: 93.42 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=384)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 384
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Subset / not reported
- Metric/value: score / Dimension 384: 97.00 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=384)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 384
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Summary / not reported
- Metric/value: score / Dimension 384: 96.61 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=384)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 384
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: Average (aggregated reported average per-dimension) / not reported
- Metric/value: score / Dimension 384 average: 95.68 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=384)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 384
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed QA / not reported
- Metric/value: score / Dimension 512: 93.37 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=512)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 512
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Subset / not reported
- Metric/value: score / Dimension 512: 97.07 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=512)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 512
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Summary / not reported
- Metric/value: score / Dimension 512: 96.61 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=512)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 512
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: Average (aggregated reported average per-dimension) / not reported
- Metric/value: score / Dimension 512 average: 95.68 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=512)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 512
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed QA / not reported
- Metric/value: score / Dimension 768: 93.53 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=768)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 768
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Subset / not reported
- Metric/value: score / Dimension 768: 97.13 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=768)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 768
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: PubMed Summary / not reported
- Metric/value: score / Dimension 768: 96.70 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=768)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 768
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

### Embedding evaluation (per-dimension averages reported on model card)

- Dataset/split: Average (aggregated reported average per-dimension) / not reported
- Metric/value: score / Dimension 768 average: 95.79 (`higher-is-better`)
- Model scope: NeuML/pubmedbert-base-embeddings-matryoshka (dimension=768)
- Conditions: Reported on the model card evaluation table for the matryoshka checkpoint.
- Source: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Locator: model card evaluation table for dimension 768
- Caveat: Protocol details (exact dataset splits, preprocessing, or metric definitions) are not specified in the provided facts.

## Comparisons

### NeuML/pubmedbert-base-embeddings — `tradeoff`

- Task: Sentence/paragraph embedding for biomedical text (PubMed benchmarks)
- Criteria: Matryoshka provides selectable output dimensionalities (64–768) with per-dimension results reported on the matryoshka model card; the non-matryoshka PubMedBERT embedding scores are reported alongside in the same model card context, indicating a tradeoff between fixed 768-dim published baseline scores and matryoshka's multi-resolution flexibility.
- Rationale: The matryoshka model card lists per-dimension numeric scores and explicitly reports the non-matryoshka pubmedbert-base-embeddings scores for comparison; selection should be guided by dimensionality/performance tradeoffs on target tasks.
- Comparison conditions: Both sets of numbers are reported on the NeuML model card repository; protocol detail differences are not specified in the provided facts.
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

### aaditya/Llama3-OpenBioLLM-8B — `insufficient-evidence`

- Task: biomedical-retrieval / embedding generation
- Criteria: No primary-source, task-matched benchmark artifacts for the peer are present in the provided findings to enable a grounded comparison with the matryoshka checkpoint.
- Rationale: The research findings do not include the peer's model-card or benchmark artifacts required for a protocol-matched comparison.
- Comparison conditions: No matching primary evidence for the peer in the provided findings.
- Evidence:

### abhinand/MedEmbed-base-v0.1 — `insufficient-evidence`

- Task: biomedical-retrieval / embedding generation
- Criteria: Peer primary-source evidence not present in the provided findings.
- Rationale: No primary-source model card or benchmark artifacts for the peer were included in the findings.
- Comparison conditions: No matching primary evidence for the peer in the provided findings.
- Evidence:

### abhinand/MedEmbed-large-v0.1 — `insufficient-evidence`

- Task: biomedical-retrieval / embedding generation
- Criteria: Peer primary-source evidence not present in the provided findings.
- Rationale: No primary-source model card or benchmark artifacts for the peer were included in the findings.
- Comparison conditions: No matching primary evidence for the peer in the provided findings.
- Evidence:

### abhinand/MedEmbed-small-v0.1 — `insufficient-evidence`

- Task: biomedical-retrieval / embedding generation
- Criteria: Peer primary-source evidence not present in the provided findings.
- Rationale: No primary-source model card or benchmark artifacts for the peer were included in the findings.
- Comparison conditions: No matching primary evidence for the peer in the provided findings.
- Evidence:

### cambridgeltl/SapBERT-from-PubMedBERT-fulltext — `insufficient-evidence`

- Task: entity embedding / biomedical entity similarity
- Criteria: No directly comparable primary-source evaluation between SapBERT and matryoshka embeddings present in the provided findings.
- Rationale: The findings do not include the peer's model-card or benchmark artifacts needed for a grounded, protocol-matched comparison.
- Comparison conditions: No matching primary evidence for the peer in the provided findings.
- Evidence:

### ncbi/MedCPT-Article-Encoder — `insufficient-evidence`

- Task: article-level embedding for biomedical retrieval
- Criteria: Peer primary-source benchmark evidence not present in the provided findings.
- Rationale: No primary-source model-card or benchmark artifacts for the peer were included in the findings.
- Comparison conditions: No matching primary evidence for the peer in the provided findings.
- Evidence:

## Limitations and safety

### Limitations

- Evidence gap: The provided primary artifacts do not disclose a checkpoint-level parameter count or immutable revision identifier for NeuML/pubmedbert-base-embeddings-matryoshka; implementers cannot verify exact model scale from the provided facts. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Evidence gap: No explicit license string for this exact matryoshka checkpoint was reported in the provided primary artifacts; upstream license for model weights and repository code is not specified in the facts. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Evidence gap: Tokenizer identity and full tokenizer.json content (special tokens, vocab size, pad_token_id, max_position_embeddings) are not available in the provided primary facts; exact tokenization behavior cannot be verified.
- The pooling configuration in repository reports word_embedding_dimension = 768 and mean-token pooling enabled; matryoshka prefixes are evaluated at 64–768 but empirical tradeoffs beyond the reported PubMed benchmark rows are not exhaustively characterized in the provided facts. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json, https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

### Safety

- Forge policy: Treat this checkpoint as research-only for healthcare and clinical contexts until institutional review and domain-expert validation are completed; the provided primary artifacts do not document PHI handling, clinical validation, or regulatory clearance for this checkpoint. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Evidence gap: The primary artifacts do not describe model-specific biosecurity, dual-use, or deployment mitigations for this checkpoint. Sources: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NeuML/pubmedbert-base-embeddings-matryoshka — model card

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka
- Publisher: NeuML / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card and repository page for the matryoshka checkpoint; contains the per-dimension evaluation table and usage notes used as principal upstream evidence.
- Scope: NeuML/pubmedbert-base-embeddings-matryoshka (model card and repo)
- Supports: per-dimension evaluation scores (dimensions 64,128,256,384,512,768)
- Supports: SentenceTransformers loadability and txtai usage example
- Supports: general model description and comparative statements vs original model

### NeuML/pubmedbert-base-embeddings-matryoshka — pooling configuration (1_Pooling/config.json)

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blob/main/1_Pooling/config.json
- Publisher: NeuML / Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository pooling configuration file specifying pooling_mode_mean_tokens, include_prompt, and word_embedding_dimension used to verify pooling behavior and output dimensionality basis.
- Scope: NeuML/pubmedbert-base-embeddings-matryoshka (pooling layer configuration)
- Supports: word_embedding_dimension = 768
- Supports: pooling_mode_mean_tokens = true
- Supports: pooling_mode_cls_token = false
- Supports: include_prompt = true

### NeuML/pubmedbert-base-embeddings-matryoshka — SentenceTransformers configuration (config_sentence_transformers.json)

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka/blame/main/config_sentence_transformers.json
- Publisher: NeuML / Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository file indicating SentenceTransformers and transformers versions and showing that no prompt templates are defined (empty prompts object).
- Scope: NeuML/pubmedbert-base-embeddings-matryoshka (sentence-transformers configuration)
- Supports: sentence_transformers version = 2.4.0
- Supports: transformers version = 4.36.2
- Supports: pytorch version = 2.1.1+cu121
- Supports: empty prompts object; default_prompt_name = null

### NeuML/pubmedbert-base-embeddings — commits (family-level repository commit history)

- URL: https://huggingface.co/NeuML/pubmedbert-base-embeddings/commits/64beaa086f375ef266deabe426fa420a3e7e1cd3
- Publisher: NeuML / Hugging Face
- Type: `repository`
- Primary because: Official Hugging Face repository commits page for the related non-matryoshka pubmedbert-base-embeddings checkpoint; used only for family-level provenance and commit-history verification where present in the provided facts.
- Scope: NeuML/pubmedbert-base-embeddings (non-matryoshka family repository commits)
- Supports: commit history entries for the NeuML/pubmedbert-base-embeddings repository (family-level provenance)

## Evidence gaps

- Evidence gap: No checkpoint-level immutable revision identifier (commit SHA) for NeuML/pubmedbert-base-embeddings-matryoshka is reported in the provided primary artifacts; a precise revision locator is required to fully verify the exact weights and files.
- Evidence gap: No explicit license declaration for the NeuML/pubmedbert-base-embeddings-matryoshka checkpoint (model weights vs repository code) was present in the provided primary artifacts; an upstream license file or model-card license field is required to close this gap.
- Evidence gap: Tokenizer identity and full tokenizer.json contents (tokenizer name, special-token strings, vocab_size, pad_token_id, max_position_embeddings) are not available in the provided facts; the exact tokenizer metadata is required to guarantee tokenization compatibility.
- Evidence gap: The provided primary artifacts do not disclose an exact model parameter count for this checkpoint; a reported parameter scale is required to verify model scale.
- Evidence gap: Protocol-level details for the reported benchmark rows (dataset splits, preprocessing, metric definitions) are not specified in the provided facts; these details are required to reliably compare published scores to other models under matched protocols.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 21 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'hasankursun' for this exact model scope: $.sources[7] uses unapproved repository owner 'hasankursun' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'raivnlab' for this exact model scope: $.sources[8] uses unapproved repository owner 'raivnlab' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'microsoft' for this exact model scope: $.sources[9] uses unapproved repository owner 'microsoft' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary host ai.azure.com: $.sources[10] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'zhigroup' for this exact model scope: $.sources[12] uses unapproved repository owner 'zhigroup' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses unapproved repository owner 'ncbi-nlp' for this exact model scope: $.sources[15] uses unapproved repository owner 'ncbi-nlp' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19] uses forbidden secondary host docs.vllm.ai: $.sources[19] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
