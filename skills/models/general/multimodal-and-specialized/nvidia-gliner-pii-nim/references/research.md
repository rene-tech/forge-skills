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

- Research key: `build-nvidia-com-nvidia-gliner-pii-59057755e4`
- Independent audit: `revised`
- Researched: `2026-07-23T21:24:23.441312+00:00`

Primary-source findings identify a checkpoint named nvidia/gliner-PII. The checkpoint is described in NVIDIA model-card and NIM documentation and hosted on Hugging Face. Primary facts state the model is a non-generative Transformer-based GLiNER span-tagging network that detects and classifies PII/PHI in UTF-8 text and emits span-level entity annotations (text, label, start, end, score) across 55+ categories. The checkpoint parameter count is reported as 5.7 × 10^8. Primary sources report the model was developed based on an upstream GLiNER variant, but upstream-lineage statements conflict across sources (see evidenceGaps). Primary documentation and Guardrails integration docs recommend threshold calibration and human review for high-stakes redaction. The primary sources do not present an explicit, single immutable NVIDIA-hosted checkpoint filename/tag beyond Hugging Face commit references; tokenizer files exist in the Hugging Face repository but the sources do not unambiguously state that those tokenizer files are an immutable artifact of the NVIDIA-served checkpoint. No unambiguous numeric benchmark tables tied to this exact nvidia/gliner-PII checkpoint were found in the checked primary locators.

## Identity

- Upstream name: nvidia/gliner-PII
- Checkpoint/version: nvidia/gliner-PII
- Immutable revision: eb01413053b8084409708759193671f56b429cff
- Parameter scale: 5.7 × 10^8
- Architecture/head: Transformer (GLiNER network design)
- License: NVIDIA Open Model License; Apache-2.0; NVIDIA Software License / Product-Specific Terms (NGC)
- Evidence: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://huggingface.co/nvidia/gliner-PII, https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/gliner-pii/-

## Selection

### Recommended

- **Automated detection and redaction of Personally Identifiable Information (PII) and Protected Health Information (PHI) in structured and unstructured UTF-8 text for enterprise/regulatory workflows** — NVIDIA model-card and NIM documentation state the model is intended to detect and classify PII/PHI and to emit span-level annotations with confidence scores across 55+ categories, making it suitable as a component in redaction workflows.
  Scope: nvidia/gliner-PII
  Evidence: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://huggingface.co/nvidia/gliner-PII
- **Integration as a PII detection/masking guardrail in NeMo Guardrails-based pipelines for input/output monitoring and masking** — NeMo Guardrails documentation references the model identifier and documents request/response fields and default thresholding behavior, supporting integration as a Guardrails component.
  Scope: nvidia/gliner-PII
  Evidence: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog, https://developer.nvidia.com/nemo-guardrails

### Conditional

- **High-stakes regulatory redaction without human review** — Allowed only after domain-specific validation, threshold tuning, and human review; primary NVIDIA documentation explicitly recommends validation and human review because performance varies by domain, format, and confidence threshold.
  Scope: nvidia/gliner-PII
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://build.nvidia.com/nvidia/gliner-pii/modelcard
- **Domain adaptation or deployment to niche industry ontologies** — Requires downstream validation and likely additional fine-tuning or calibration; primary findings report the model was developed based on an upstream GLiNER variant but do not publish in-domain benchmark numbers for the NVIDIA checkpoint.
  Scope: nvidia/gliner-PII
  Evidence: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii

### Avoid

- **Using the model as a generative language model for text synthesis or instruction-following** — Primary-source facts describe GLiNER PII as a non-generative span-tagging model that performs span-level entity annotation rather than text generation.
  Scope: nvidia/gliner-PII
  Evidence: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://huggingface.co/nvidia/gliner-PII
- **Non-text input modalities (audio, image) without upstream conversion to UTF-8 text** — All primary-source facts indicate the checkpoint accepts UTF-8 text strings as input; no primary evidence indicates the checkpoint accepts raw audio or images.
  Scope: nvidia/gliner-PII
  Evidence: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii

## Input preparation

### Semantic inputs

- One-dimensional UTF-8 text strings representing structured or unstructured textual content (plain text). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii
- Inputs can represent structured records or unstructured free text; the model is reported to support both forms of textual content. Sources: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://huggingface.co/nvidia/gliner-PII

### Accepted formats

- UTF-8 text strings are the accepted input format for the model. Sources: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii

### Preprocessing

- Primary sources report the input type as UTF-8 text strings but do not publish a complete, explicit tokenizer provenance statement that unambiguously ties an immutable tokenizer artifact to the NVIDIA-served checkpoint. Sources: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii
- Hugging Face repository for nvidia/gliner-PII includes a tokenizer_config.json listing special tokens and token IDs, but the primary findings do not explicitly state that these tokenizer files are an immutable artifact shipped with the NVIDIA-served checkpoint. Sources: https://huggingface.co/nvidia/gliner-PII/blob/main/tokenizer_config.json, https://huggingface.co/nvidia/gliner-PII
- Training metadata in Hugging Face commit entries reports vocabulary size, backbone, hidden size, number of layers, and training sequence length (commit-level metadata), but the NIM/NVIDIA documentation does not duplicate a single immutable tokenizer file fingerprint for the NVIDIA-served checkpoint. Sources: https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff, https://huggingface.co/nvidia/gliner-PII/commit/b0851dd8139301516282d2c8c4bb326ef043f54b

### Pre-submit validation

- Inputs should be validated as UTF-8 text; NVIDIA documentation recommends validation, threshold tuning, and human review prior to high-stakes deployment because performance varies by domain, format, and confidence threshold. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://build.nvidia.com/nvidia/gliner-pii/modelcard
- NeMo Guardrails integrations referencing this model include optional request fields such as 'labels', 'threshold', 'chunk_length', and 'overlap' for configuring detection behavior and chunking; these are configuration-level controls used in validation and deployment. Sources: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog, https://developer.nvidia.com/nemo-guardrails

### Task-specific formatting

- Guardrails integration documentation shows request/response fields and configuration parameters for the model (e.g., 'model' field set to 'nvidia/gliner-pii', optional 'labels' array, 'threshold' float, and chunking parameters) describing how Guardrails formats requests to the model. Sources: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog
- NVIDIA NIM documentation and NGC catalog describe packaging and usage for the NIM/NGC container, but low-level transport framing or every runtime SDK call signature is not exhaustively specified in the available primary locators. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/gliner-pii/-

## Output interpretation

### Outputs

- The model returns an 'entities' array (list of dictionaries/EntitySpan objects) with keys that include text, label, start, end, and score. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff
- Span-level entity annotations cover 55+ categories as reported in NVIDIA documentation and Hugging Face metadata. Sources: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://huggingface.co/nvidia/gliner-PII

### Interpretation

- The 'score' field is presented as a confidence score; NeMo Guardrails documentation indicates a default confidence threshold of 0.5 and implies a 0.0–1.0 score range for configuration, so scores should be interpreted as probabilities/confidence values within that range when Guardrails is used. Sources: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog
- Start/end offsets are provided to indicate span positions in the input UTF-8 text; interpreting offsets requires mapping them back to the original UTF-8 input. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii

### Post-inference validation

- NVIDIA documentation recommends calibration of confidence thresholds and human review for high-stakes scenarios; downstream validation practices should include threshold tuning on in-domain data and human review of redaction decisions. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://build.nvidia.com/nvidia/gliner-pii/modelcard
- NeMo Guardrails default configuration uses a 0.5 confidence threshold by default for GLiNER integrations; this default can be adjusted as part of postprocessing and deployment configuration. Sources: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### knowledgator/gliner-bi-large-v1.0 — `insufficient-evidence`

- Task: PII/PHI detection (span-level entity recognition)
- Criteria: No primary-source numeric head-to-head metrics tied to the exact nvidia/gliner-PII checkpoint were found to support a comparative verdict.
- Rationale: Primary sources reference an upstream GLiNER variant in lineage statements but do not publish numeric head-to-head benchmarks for the exact NVIDIA checkpoint; therefore direct comparison is unsupported by the checked primary locators.
- Comparison conditions: Checked Build.NVIDIA model card, NIM reference, Hugging Face model page, and Hugging Face commit pages for numeric comparisons; none contain head-to-head numeric tables tied to the exact NVIDIA checkpoint.
- Evidence: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff

## Limitations and safety

### Limitations

- Performance varies by domain, format, and confidence threshold; validation and human review are recommended for high-stakes deployments. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://build.nvidia.com/nvidia/gliner-pii/modelcard
- The primary sources do not publish exhaustive tokenizer/tokenization internals or a single immutable tokenizer fingerprint for the NVIDIA-served checkpoint; Hugging Face repository includes tokenizer_config.json but the NVIDIA documentation does not explicitly declare that file as the immutable tokenizer artifact for the NVIDIA-served checkpoint. Sources: https://huggingface.co/nvidia/gliner-PII/blob/main/tokenizer_config.json, https://build.nvidia.com/nvidia/gliner-pii/modelcard
- Exact immutable revision identifiers (single canonical checkpoint filename with immutable tag or an NVIDIA-hosted checksum) for the nvidia/gliner-PII checkpoint are not consistently reported in the NVIDIA-hosted documentation; commit-level snapshots exist in the Hugging Face repository but an authoritative single immutable NVIDIA-hosted checkpoint filename/tag is not reported in the checked NVIDIA pages. Sources: https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff, https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii
- No unambiguous numeric benchmark tables (dataset, split, metric, numeric value) tied to the exact nvidia/gliner-PII checkpoint were found at the checked primary locators. Sources: https://build.nvidia.com/nvidia/gliner-pii/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://huggingface.co/nvidia/gliner-PII

### Safety

- NVIDIA documentation recommends validation, confidence-threshold tuning, and human review for high-stakes or regulated PII/PHI redaction scenarios. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://build.nvidia.com/nvidia/gliner-pii/modelcard
- NeMo Guardrails provides configuration-level defaults (including a default threshold of 0.5) and flows for PII detection and masking when integrating nvidia/gliner-pii, indicating guardrail-level handling and integration points for logging/retention controls. Sources: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog, https://developer.nvidia.com/nemo-guardrails
- Use of GLiNER PII is reported in the findings to be governed by the NVIDIA Open Model License and additional NVIDIA trial/product license references; licensing differs by distribution (Hugging Face, NIM/NGC) and is documented in the corresponding primary locators. Sources: https://huggingface.co/nvidia/gliner-PII, https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/gliner-pii/-

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### GLiNER PII model card (Build.NVIDIA)

- URL: https://build.nvidia.com/nvidia/gliner-pii/modelcard
- Publisher: not reported
- Type: `model-card`
- Primary because: Official NVIDIA model card page used to support checkpoint-scoped claims about intended purpose, architecture type, categories, and deployment guidance.
- Scope: nvidia/gliner-PII (Build.NVIDIA model card)
- Supports: The GLiNER PII model was released on Build.NVIDIA.com and is described on the model card.
- Supports: The model architecture type is Transformer and network architecture is GLiNER.
- Supports: The model detects PII/PHI and outputs span-level annotations across 55+ categories.
- Supports: The model accepts UTF-8 text inputs and is intended for PII/PHI detection and redaction workflows.
- Supports: Documentation recommends validation, threshold tuning, and human review for high-stakes deployments.

### Hugging Face model page: nvidia/gliner-PII

- URL: https://huggingface.co/nvidia/gliner-PII
- Publisher: not reported
- Type: `repository`
- Primary because: Hugging Face model repository page for the NVIDIA-hosted checkpoint; contains release metadata and links to commit-level artifacts used to corroborate checkpoint-level metadata.
- Scope: nvidia/gliner-PII (Hugging Face repository entry)
- Supports: The model page documents the model name, purpose (PII/PHI detection), reported parameter count, license metadata, and release date.
- Supports: Hugging Face repository metadata includes references to training dataset and model tags.

### Hugging Face commit snapshot (eb01413053b8084409708759193671f56b429cff)

- URL: https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff
- Publisher: not reported
- Type: `repository`
- Primary because: Commit-level repository snapshot containing model metadata and training/configuration facts referenced in the findings.
- Scope: nvidia/gliner-PII (Hugging Face commit eb01413053b8...)
- Supports: Commit-level metadata lists training dataset (nvidia/Nemotron-PII), output schema (entities list with keys text,label,start,end,score), backbone details, and other training configuration fields.

### Hugging Face commit snapshot (b0851dd8139301516282d2c8c4bb326ef043f54b)

- URL: https://huggingface.co/nvidia/gliner-PII/commit/b0851dd8139301516282d2c8c4bb326ef043f54b
- Publisher: not reported
- Type: `repository`
- Primary because: Commit-level repository snapshot containing additional training/configuration metadata referenced in the findings.
- Scope: nvidia/gliner-PII (Hugging Face commit b0851dd8...)
- Supports: Commit-level metadata reports training dataset details, sequence length, span mode, subtoken pooling strategy, backbone (Microsoft/deberta-v3-large) metadata, vocabulary size, hidden size, layer counts, and other training parameters.

### NVIDIA NIM Reference: nvidia-gliner-pii

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii
- Publisher: not reported
- Type: `official-documentation`
- Primary because: Official NIM reference documenting API contract, output schema, licensing references, and deployment guidance for the NVIDIA-served checkpoint.
- Scope: nvidia/gliner-PII (NIM/wrapped checkpoint as described in NVIDIA docs)
- Supports: The NIM reference documents output schema (entities array with keys text,label,start,end,score), that the model is a non-generative span-level entity annotator, parameter count, architecture type, lineage statements, and deployment/license notes.

### Hugging Face: tokenizer_config.json for nvidia/gliner-PII

- URL: https://huggingface.co/nvidia/gliner-PII/blob/main/tokenizer_config.json
- Publisher: not reported
- Type: `repository`
- Primary because: Tokenizer configuration file in the Hugging Face repository referenced in the findings and used to corroborate special tokens and token IDs.
- Scope: nvidia/gliner-PII (tokenizer_config.json in Hugging Face repo)
- Supports: The tokenizer_config.json file defines added token decoders and lists special token IDs and content such as [PAD], [CLS], [SEP], [UNK], [MASK], [FLERT], <<ENT>>, and <<SEP>>.

### NeMo Guardrails catalog (Guardrails GLiNER entry)

- URL: https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog
- Publisher: not reported
- Type: `official-documentation`
- Primary because: NeMo Guardrails catalog entry referencing GLiNER integrations used to corroborate request/response fields, default threshold values, and Guardrails-specific configuration.
- Scope: nvidia/gliner-PII (Guardrails catalog entry)
- Supports: Guardrails catalog documents how to configure GLiNER integrations (request fields like model, labels, threshold, chunking parameters) and notes a default threshold of 0.5 for Guardrails GLiNER integrations.

### NeMo Guardrails developer page

- URL: https://developer.nvidia.com/nemo-guardrails
- Publisher: not reported
- Type: `official-documentation`
- Primary because: Developer documentation for NeMo Guardrails referenced in the findings to support integration and runtime deployment details.
- Scope: nvidia/gliner-PII (NeMo Guardrails developer docs referencing GLiNER)
- Supports: NeMo Guardrails developer docs describe configuration, integration, and runtime deployment patterns used with Guardrails catalog entries.

### NGC catalog entry for GLiNER-PII container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/gliner-pii/-
- Publisher: not reported
- Type: `official-documentation`
- Primary because: NGC catalog entry referenced in the findings providing packaging and deployment metadata for the containerized NIM package.
- Scope: nvidia/gliner-pii NGC container
- Supports: NGC catalog documents container packaging, licensing references for the container, deployment requirements and distribution details.

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/gliner-pii
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-gliner-pii
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No single authoritative NVIDIA-hosted immutable checkpoint filename/tag or checksum was found in the checked NVIDIA primary locators. Checked locators: https://build.nvidia.com/nvidia/gliner-pii/modelcard (model card page), https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii (NIM reference page). Hugging Face commit snapshots exist but a single canonical NVIDIA-hosted immutable artifact was not located at the NVIDIA pages.
- Evidence gap: Tokenizer provenance ambiguity — Hugging Face repository contains tokenizer_config.json (https://huggingface.co/nvidia/gliner-PII/blob/main/tokenizer_config.json) listing special tokens and IDs, but the NVIDIA-hosted documentation does not explicitly state that this tokenizer_config.json is the immutable tokenizer shipped with the NVIDIA-served checkpoint. Checked locators: NVIDIA model card (https://build.nvidia.com/nvidia/gliner-pii/modelcard) and NIM reference (https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii).
- Evidence gap: No unambiguous numeric benchmark tables (dataset + split + metric + numeric value) tied to the exact nvidia/gliner-PII checkpoint were found at checked primary locators. Checked locators: https://build.nvidia.com/nvidia/gliner-pii/modelcard (model card page), https://docs.api.nvidia.com/nim/reference/nvidia-gliner-pii (NIM reference page), https://huggingface.co/nvidia/gliner-PII (model page), https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff (commit-level files).
- Evidence gap: Upstream lineage ambiguity — some primary locators state the model was developed based on knowledgator/gliner-bi-large-v1.0 while other repository metadata references different GLiNER base descriptors; the primary locators checked include https://build.nvidia.com/nvidia/gliner-pii/modelcard and https://huggingface.co/nvidia/gliner-PII/commit/eb01413053b8084409708759193671f56b429cff.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/gliner-pii: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
