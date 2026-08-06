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

- Research key: `huggingface-co-openmed-openmed-ner-diseasedetect-biomed-335m-8e29af3034`
- Independent audit: `revised`
- Researched: `2026-08-06T09:02:15.611174+00:00`

Checkpoint-scoped summary: OpenMed-NER-DiseaseDetect-BioMed-335M is a 335M-parameter fine-tuned transformer (BERT-family) token-classification model for disease named-entity recognition. The Hugging Face model card for this exact checkpoint reports BC5CDR‑Disease aggregate performance values (F1=0.9005, precision=0.8887, recall=0.9126, accuracy=0.9838). An ONNX/Android artifact variant for this checkpoint is published under the OpenMed Hugging Face owner and can run locally on Python CPU, in the browser, and on Android. A separate MLX snapshot published under the OpenMed owner contains a tokenizer.json artifact for a snapshot variant. The canonical OpenMed NER preprint (arXiv:2508.01630) documents family-level methodology (backbone tokenizer usage, BIO label encoding, truncation to 256 word-pieces and 50-token sliding window reported as family methodology, and LoRA fine-tuning) and should be treated as upstream/family evidence rather than automatic checkpoint proof. Primary-source documentation checked does not include a full embedded Apache-2.0 license text at the main model-card URL, explicit BC5CDR split and full evaluation protocol details for the reported metrics, nor a documented token→character-offset mapping algorithm at the main model-card checkout; these are recorded as evidence gaps below.

## Identity

- Upstream name: OpenMed-NER-DiseaseDetect-BioMed-335M
- Checkpoint/version: OpenMed-NER-DiseaseDetect-BioMed-335M
- Immutable revision: not reported
- Parameter scale: 335M
- Architecture/head: Fine-tuned BERT-family transformer backbone with a token-classification head producing token-level BIO labels (B-/I-/O) for DISEASE / O
- License: Apache-2.0
- Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx, https://arxiv.org/abs/2508.01630, https://openmedproject.eu/home, https://openmed.life

## Selection

### Recommended

- **Extracting disease mentions/entities from biomedical and healthcare text for downstream information-extraction pipelines (research or non-clinical analytics).** — The Hugging Face model card for the exact checkpoint describes the model as engineered for disease entity recognition and reports BC5CDR‑Disease performance metrics for this checkpoint.
  Scope: OpenMed-NER-DiseaseDetect-BioMed-335M
  Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- **On-device or local inference for entity extraction in constrained runtimes (research, prototyping, or non-regulated analytics) after downstream validation.** — The checkpoint has an ONNX/Android artifact published by the OpenMed owner that is documented to run locally (Python CPU), in the browser, and on Android; use on-device deployments only after validating span/offset mapping and calibration on target data.
  Scope: OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
  Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android

### Conditional

- **Integrating extracted disease spans into downstream knowledge-graph construction or literature-mining pipelines (non-clinical research) after evaluation on target data.** — Perform target-data evaluation (precision/recall) and calibrate confidence thresholds on representative labeled data; validate tokenizer provenance and token→character-offset alignment before integrating spans downstream.
  Scope: OpenMed-NER-DiseaseDetect-BioMed-335M
  Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx
- **On-device inference (Android) for entity extraction using the ONNX/Android artifacts in low-latency or offline settings.** — Confirm ONNX/Android variant suitability for target hardware, validate quantization variant correctness on-device, and verify token-to-character-offset alignment and confidence calibration for downstream consumers.
  Scope: OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
  Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx

### Avoid

- **Automated clinical diagnosis or clinical decision-making without human oversight.** — Evidence gap: the checked primary sources for this checkpoint and its ONNX/Android artifact do not provide explicit documentation of calibrated thresholds, regulatory validation, or clinical-grade certification required to support automated diagnosis without human oversight.
  Scope: OpenMed-NER-DiseaseDetect-BioMed-335M and OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
  Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android

## Input preparation

### Semantic inputs

- Free-text biomedical or healthcare text (e.g., PubMed abstracts, clinical or research documents) intended for disease-entity extraction. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://openmedproject.eu/home

### Accepted formats

- Lists or batches of text strings supplied as textual inputs for token-classification inference. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- On-device/local inference inputs supported by the published ONNX/Android artifact variant (text inputs for local Python CPU, browser, or Android execution). Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android

### Preprocessing

- Backbone tokenizer usage and BIO label-encoding are described at the OpenMed family level; the canonical OpenMed NER preprint documents use of the backbone tokenizer and BIO encoding as family methodology. Sources: https://arxiv.org/abs/2508.01630
- Family-level preprocessing reported in the preprint includes truncation to 256 word-pieces and a sliding window with 50-token overlap; this is upstream/family methodology in the preprint and is not automatically checkpoint-scoped evidence for the exact published checkpoint unless the model card explicitly states it. Sources: https://arxiv.org/abs/2508.01630
- A tokenizer.json artifact is published for an MLX snapshot of this checkpoint snapshot (tokenizer.json present in the MLX snapshot repository). Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx/blob/bfa6e04cd6d85c256523e662c3204bcae2649428/tokenizer.json

### Pre-submit validation

- Validate tokenizer provenance, tokenization outputs, and token→character-offset alignment on representative target data prior to deployment; confirm the MLX tokenizer.json when using the MLX snapshot. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx
- Evidence gap: the main Hugging Face model-card checkout does not include an explicit token→character-offset mapping algorithm or full tokenizer files; downstream validation is required.

### Task-specific formatting

- Entity labels are encoded using the BIO scheme (B-Disease, I-Disease, O) as described in the OpenMed NER preprint (family-level methodology). Sources: https://arxiv.org/abs/2508.01630

## Output interpretation

### Outputs

- Transformer token-classification outputs BIO labels per token (token-level NER outputs) produced by the model's token-classification head. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://arxiv.org/abs/2508.01630
- Evidence gap: whether the ONNX/Android artifact README for this exact checkpoint documents detected span labels, per-span confidence scores, and character-offset fields is not specified in the checked primary ONNX/Android artifact page for this checkpoint.

### Interpretation

- Treat raw confidence scores as uncalibrated unless downstream calibration on representative labeled data is performed; primary sources for this checkpoint do not provide calibration statistics or recommended numeric thresholds. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
- BIO-tag outputs must be converted to contiguous entity spans and mapped to character offsets using tokenizer/preprocessing alignment; the canonical preprint documents BIO→span semantics at the family level but a token→character-offset algorithm is not present on the main model-card checkout. Sources: https://arxiv.org/abs/2508.01630, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M

### Post-inference validation

- Post-inference validation should include recall/sensitivity checks, threshold calibration for confidence scores, span/offset sanity checks, and human expert review for high-risk uses prior to clinical deployment. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
- Evidence gap: the checked primary sources do not provide standardized calibration procedures, numeric thresholds, or calibration statistics for this checkpoint or its ONNX/Android variant; downstream calibration and benchmarking are required.

## Public benchmarks

### Disease entity recognition (NER)

- Dataset/split: BC5CDR-Disease / not reported
- Metric/value: F1 / 0.9005 (`higher-is-better`)
- Model scope: OpenMed-NER-DiseaseDetect-BioMed-335M
- Conditions: Reported in the Hugging Face model card performance table for this checkpoint; detailed evaluation protocol (exact split identifier, tokenization→offset mapping, IOB/span-matching rules, and random seed) is not specified in the checked primary sources.
- Source: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- Locator: performance table (model card)
- Caveat: Exact dataset split identifier and full evaluation protocol (tokenization→offset mapping, IOB/span-matching rules, random seed) are not reported in the checked model card for this exact checkpoint.

### Disease entity recognition (NER) - precision

- Dataset/split: BC5CDR-Disease / not reported
- Metric/value: Precision / 0.8887 (`higher-is-better`)
- Model scope: OpenMed-NER-DiseaseDetect-BioMed-335M
- Conditions: Reported in the Hugging Face model card performance table for this checkpoint; detailed evaluation protocol not specified.
- Source: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- Locator: performance table (model card)
- Caveat: Exact dataset split identifier and tokenization/matching rules are not reported in the checked model card.

### Disease entity recognition (NER) - recall

- Dataset/split: BC5CDR-Disease / not reported
- Metric/value: Recall / 0.9126 (`higher-is-better`)
- Model scope: OpenMed-NER-DiseaseDetect-BioMed-335M
- Conditions: Reported in the Hugging Face model card performance table for this checkpoint; detailed evaluation protocol not specified.
- Source: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- Locator: performance table (model card)
- Caveat: Exact dataset split identifier and tokenization/matching rules are not reported in the checked model card.

### Disease entity recognition (NER) - accuracy

- Dataset/split: BC5CDR-Disease / not reported
- Metric/value: Accuracy / 0.9838 (`higher-is-better`)
- Model scope: OpenMed-NER-DiseaseDetect-BioMed-335M
- Conditions: Reported in the Hugging Face model card performance table for this checkpoint; detailed evaluation protocol not specified.
- Source: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- Locator: performance table (model card)
- Caveat: Exact dataset split identifier and tokenization/matching rules are not reported in the checked model card.

## Comparisons

### OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M — `insufficient-evidence`

- Task: Disease/entity NER (pathology / disease detection)
- Criteria: Dataset and metric semantics differ between the two primary sources: BioMed-335M reports BC5CDR‑Disease metrics while the Tiny-60M primary model card reports an NCBI_DISEASE result (base F1=0.63) on a different dataset and protocol.
- Rationale: Primary sources show different evaluated datasets and reported metrics; the checked model card sources do not provide matched dataset/split/protocol documentation to support a direct numeric comparison.
- Comparison conditions: Different reported benchmark datasets (BC5CDR-Disease vs NCBI_DISEASE) and differing documented protocols in their respective model cards.
- Evidence: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M

## Limitations and safety

### Limitations

- The Hugging Face model card reports BC5CDR performance numbers for this exact checkpoint but does not provide the complete evaluation protocol (exact dataset split identifier, explicit IOB/span-matching rules, tokenization→character-offset mapping rules, or random seeds), limiting reproducibility of the reported metrics. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://arxiv.org/abs/2508.01630
- Tokenizer vocabulary and explicit token-id mappings for the main Hugging Face model-card checkout are not fully documented on the main model card; a separate MLX snapshot published under the OpenMed owner contains tokenizer.json for a snapshot variant. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx/blob/bfa6e04cd6d85c256523e662c3204bcae2649428/tokenizer.json
- Evidence gap: the checked primary model card page does not embed the full Apache-2.0 license text for the model weights and code at the model-card URL; the model card declares 'Apache-2.0' but a full embedded license text at that exact location was not found in the checked sources. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- Evidence gap: calibration statistics or recommended numeric confidence thresholds for the checkpoint and ONNX/Android artifacts are not provided in the checked primary sources; downstream calibration is required before relying on confidence scores. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
- Evidence gap: standardized runtime latency, memory, and throughput benchmarks for the transformer checkpoint or ONNX/Android variants under a stated protocol and hardware are not provided in the checked primary sources. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android

### Safety

- Evidence gap: Do not use model outputs for automated clinical diagnosis without human expert review and regulatory validation; the checked primary sources do not document clinical-grade certification or calibrated diagnostic thresholds for this checkpoint.
- Evaluate recall, thresholds, and span/offset alignment on governed target data before deployment; validate outputs and thresholds with domain experts for clinical or regulated uses. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android, https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx
- Treat raw confidence scores as uncalibrated unless calibration is performed on representative labeled data; primary sources do not provide calibration statistics. Sources: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- PHI/PII de-identification and regulatory compliance require expert review; project-level documentation indicates de-identification/PII detection capabilities but does not by itself guarantee HIPAA or regulatory suitability without expert validation. Sources: https://openmed.life, https://openmedproject.eu/home

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### OpenMed-NER-DiseaseDetect-BioMed-335M model card (Hugging Face)

- URL: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M
- Publisher: OpenMed (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model card for the exact OpenMed-NER-DiseaseDetect-BioMed-335M checkpoint containing checkpoint-scoped description and reported BC5CDR performance values.
- Scope: OpenMed-NER-DiseaseDetect-BioMed-335M
- Supports: model identity as a fine-tuned transformer for disease NER
- Supports: reported BC5CDR-Disease performance (F1/precision/recall/accuracy) as listed in the model card
- Supports: declared license field (Apache-2.0)

### OpenMed-NER-DiseaseDetect-BioMed-335M ONNX Android artifact (Hugging Face)

- URL: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
- Publisher: OpenMed (Hugging Face artifact)
- Type: `repository`
- Primary because: ONNX/Android artifact page published under the OpenMed Hugging Face owner documenting the on-device artifact variant for this checkpoint and its local/browser/Android execution capabilities.
- Scope: OpenMed-NER-DiseaseDetect-BioMed-335M-v1-onnx-android
- Supports: on-device/local execution modes for this artifact (Python CPU, browser, Android)
- Supports: artifact-level existence of an ONNX/Android packaging for this checkpoint

### OpenMed MLX snapshot tokenizer.json (Hugging Face MLX snapshot)

- URL: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx
- Publisher: OpenMed (Hugging Face MLX snapshot)
- Type: `repository`
- Primary because: MLX snapshot published under the OpenMed owner that contains a tokenizer.json artifact for a snapshot variant of this checkpoint.
- Scope: OpenMed-NER-DiseaseDetect-BioMed-335M-mlx
- Supports: presence of tokenizer.json and snapshot files for a snapshot variant of this checkpoint
- Supports: downloadable MLX snapshot intended for local/offline workflows

### OpenMed NER preprint (arXiv:2508.01630)

- URL: https://arxiv.org/abs/2508.01630
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical OpenMed NER preprint describing family-level methodology including backbone tokenizer usage, BIO label encoding, truncation and sliding-window preprocessing, and LoRA fine-tuning at the family level.
- Scope: OpenMed family / NER methodology
- Supports: tokenization and preprocessing rules at the family level (backbone tokenizer, truncation to 256 word-pieces, 50-token sliding window)
- Supports: BIO label encoding and family-level methodology
- Supports: description of LoRA fine-tuning and training corpus at family scope

### OpenMed project website (official documentation)

- URL: https://openmedproject.eu/home
- Publisher: OpenMed (project website)
- Type: `official-documentation`
- Primary because: Project website providing project-level documentation for OpenMed.
- Scope: OpenMed project and family
- Supports: project-level documentation and description of project capabilities

### OpenMed project site (OpenMed.life)

- URL: https://openmed.life
- Publisher: OpenMed (project website)
- Type: `official-documentation`
- Primary because: Project-level site describing OpenMed capabilities including PII/PHI detection catalog claims and related project information.
- Scope: OpenMed project and family
- Supports: project-level statements about PII/PHI detection capabilities

### OpenMed tokenizer.json file (MLX snapshot path)

- URL: https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M-mlx/blob/bfa6e04cd6d85c256523e662c3204bcae2649428/tokenizer.json
- Publisher: OpenMed (Hugging Face MLX snapshot)
- Type: `repository`
- Primary because: Direct MLX snapshot file path demonstrating the presence of tokenizer.json for the snapshot variant.
- Scope: OpenMed-NER-DiseaseDetect-BioMed-335M-mlx (tokenizer artifact file)
- Supports: presence of tokenizer.json file at the snapshot repository path

### Cited official first-party source

- URL: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: openmed-ner-diseasedetect-biomed-335m
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: The Hugging Face model card for the exact checkpoint does not include the full embedded Apache-2.0 license text at the model-card URL; the model card declares 'Apache-2.0' but a full embedded license text at that exact location was not found in the checked sources.
- Evidence gap: The exact BC5CDR-Disease evaluation protocol details (dataset split identifier, explicit IOB/span-matching rules, tokenization→character-offset mapping rules, and random seeds) for the reported BC5CDR metrics are not specified in the checked primary sources (model card and preprint).
- Evidence gap: Token-to-character-offset mapping provenance and a complete explicit tokenizer token-id mapping for the main Hugging Face model-card checkout are not present on the main model card page; a tokenizer.json exists in an MLX snapshot but the main model card does not embed full tokenizer files or an explicit mapping algorithm.
- Evidence gap: The ONNX/Android artifact README for this exact checkpoint does not, in the checked primary ONNX/Android artifact page, provide a documented token→character-offset mapping algorithm proving how BIO outputs are converted to character offsets; the artifact is documented to run locally but the explicit mapping algorithm was not found in the checked artifact page.
- Evidence gap: Calibration statistics or recommended numeric confidence thresholds for the exact checkpoint and its ONNX/Android artifacts are not provided in the checked primary sources; downstream calibration is required.
- Evidence gap: Standardized runtime latency, memory, and throughput benchmarks for the transformer checkpoint and ONNX/Android variants under a stated protocol and hardware are not provided in the checked primary sources.
- Evidence gap: The checked primary sources do not provide an explicit file-level listing of ONNX artifact filenames (model_int8.onnx, model_fp16.onnx, model.onnx, model.ort) for the exact OpenMed-NER-DiseaseDetect-BioMed-335M ONNX/Android artifact; artifact existence and exact file names at the ONNX/Android artifact page were not confirmed in the checked sources for this exact checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2] uses forbidden secondary URL https: $.sources[2] uses forbidden secondary URL https://huggingface.co/papers/2508.01630 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'onnx-community' for this exact model scope: $.sources[7] uses unapproved repository owner 'onnx-community' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'd4data' for this exact model scope: $.sources[10] uses unapproved repository owner 'd4data' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'maziyarpanahi' for this exact model scope: $.sources[11] uses unapproved repository owner 'maziyarpanahi' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'models' for this exact model scope: $.sources[13] uses unapproved repository owner 'models' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary URL https: $.sources[13] uses forbidden secondary URL https://huggingface.co/models?other=arxiv%3A2508.01630 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
