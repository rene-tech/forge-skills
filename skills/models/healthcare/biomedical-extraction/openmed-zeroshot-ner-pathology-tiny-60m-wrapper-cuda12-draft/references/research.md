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

- Research key: `huggingface-co-openmed-openmed-zeroshot-ner-pathology-tiny-60m-39d50bbdf4`
- Independent audit: `revised`
- Researched: `2026-08-06T09:17:54.668981+00:00`

Checkpoint-scoped inspection of the Hugging Face model repository and commit blobs for OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M shows the upstream checkpoint is presented as a GLiNER-based zero-shot token-classification model specialized for disease/entity recognition. Official example usage in commit blobs demonstrates loading via GLiNER.from_pretrained with model identifier "OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M", example input text "Early detection of breast cancer improves survival rates.", passing a label list ['DISEASE'], and calling a prediction API with threshold=0.5. The repository contains a gliner_config.json (blob and blame) that documents tokenizer class (T5Tokenizer), vocabulary size (250102), encoder base model (google/mt5-small), maximum input length (max_len = 1024), and other architecture and training hyperparameters. The model card and commit metadata state the license as Apache License 2.0. The checked primary sources do not contain checkpoint-scoped numeric benchmark rows explicitly tied to the Tiny-60M checkpoint (no dataset/split/metric/value row verifiable for this exact checkpoint in the inspected locators), do not expose a formal inference output JSON schema, and do not present explicit creator-authorized PHI handling or clinical-use authorization statements in the inspected locations.

## Identity

- Upstream name: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M
- Checkpoint/version: commit 751c87f2dfa77800e1bead7f9fb40f5734078e47
- Immutable revision: not reported
- Parameter scale: Tiny-60M
- Architecture/head: GLiNER (zero-shot token-classification)
- License: Apache-2.0
- Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blob/main/gliner_config.json, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blame/main/gliner_config.json

## Selection

### Recommended

- **Zero-shot disease/entity extraction from biomedical English text using GLiNER label lists** — The model card and repository commit-level examples present the checkpoint as a GLiNER zero-shot token-classification model specialized for disease/entity recognition and include example usage loading the model via GLiNER.from_pretrained and passing a label list (['DISEASE']).
  Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (repository and commit-level examples)
  Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be

### Conditional

- **Adjusting extraction sensitivity by setting a detection threshold when predicting entities** — Use as demonstrated in repository example invocation which sets threshold=0.5; no additional creator-provided calibration guidance or recommended threshold-tuning workflow is present in the inspected sources.
  Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (repository commit example showing threshold usage)
  Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M

### Avoid

- **Unvalidated use for clinical decision-making or diagnostics without local validation** — Evidence gap: The inspected primary sources do not provide explicit creator-authorized clinical-use validation, deployment guidance, or statements authorizing the model for clinical decision-making.
  Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M
  Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be

## Input preparation

### Semantic inputs

- The model accepts plain biomedical English text as input for zero-shot named-entity prediction. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be

### Accepted formats

- Example usage demonstrates passing free-form text strings to GLiNER APIs (loaded via GLiNER.from_pretrained with the upstream model name). Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

### Preprocessing

- gliner_config.json documents tokenizer class as T5Tokenizer, vocabulary size as 250102, maximum input length (max_len) = 1024 tokens, and encoder base model 'google/mt5-small', which inform preprocessing/tokenization and input-length semantics. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blob/main/gliner_config.json, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blame/main/gliner_config.json
- Evidence gap: The inspected primary-source facts do not include a file-level listing of tokenizer artifact filenames (e.g., tokenizer.json, vocab.txt, merges.txt) in the provided research findings. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

### Pre-submit validation

- Evidence gap: The inspected primary sources do not provide explicit input-validation rules such as production input-length bounds beyond max_len in gliner_config.json, sanitization requirements, or explicit checks to perform before inference. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blob/main/gliner_config.json, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M

### Task-specific formatting

- Example usage in the repository commit demonstrates supplying a label list (e.g., ['DISEASE']) when calling the prediction API, consistent with GLiNER zero-shot label-list usage. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be

## Output interpretation

### Outputs

- The model produces named-entity predictions (zero-shot NER) from input biomedical text. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

### Interpretation

- Repository example shows entity prediction invoked with a detection threshold parameter (example uses threshold=0.5); no calibrated mapping from model scores to calibrated probabilities is present in the inspected sources. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M

### Post-inference validation

- Evidence gap: The inspected primary-source locators do not include a formal inference output JSON schema (field names, span object structure, token-level arrays, or exact score field names). Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Protocol-matched numeric comparison for Tiny-60M
- Criteria: No checkpoint-scoped numeric benchmark entries tied to the Tiny-60M checkpoint were present in the inspected primary-source locators to enable protocol-matched comparison.
- Rationale: The inspected primary-source facts do not contain numeric benchmark rows explicitly tied to this exact Tiny-60M checkpoint; therefore protocol-matched numeric comparisons cannot be supported from the checked locators.
- Comparison conditions: Checked the model card benchmark table and commit blobs for dataset/split/metric/value rows specific to the Tiny-60M checkpoint; found benchmark rows for larger family members in the model card but no verifiable numeric row for the Tiny-60M checkpoint in the inspected locators.
- Evidence: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

## Limitations and safety

### Limitations

- The model is presented as specialized for disease entity recognition and is described as a GLiNER-based zero-shot token-classification model; training/fine-tuning and specialization are claimed in the model card and commits. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be
- Evidence gap: The inspected primary-source facts do not provide checkpoint-scoped numeric benchmark results tied to Tiny-60M (no table/figure/section/commit row with dataset, split, metric, and value was present in the checked primary-source locators). Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blob/main/gliner_config.json
- Evidence gap: Tokenizer artifact file-level contents and explicit tokenizer vocabulary or merges files were not present in the inspected primary-source locators within the provided research findings. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47

### Safety

- Evidence gap: The inspected primary-source facts do not include creator-provided statements about PHI handling, data-retention policy, or explicit clinical-use authorization. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be
- The model card and repository characterize the model as useful for clinical and biomedical NLP and disease entity extraction, which is safety-relevant context for healthcare deployments. Sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (model card)

- URL: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M
- Publisher: OpenMed (hosted on Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model repository page and model card for this checkpoint; contains descriptive claims, benchmark table (family-level), and usage guidance used as primary evidence for checkpoint-scoped claims where explicit.
- Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (Tiny-60M checkpoint as presented on Hugging Face)
- Supports: The model identifier is "OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M".
- Supports: The model is presented as GLiNER-based zero-shot NER specialized for disease/entity recognition.
- Supports: The model is described as useful for clinical and biomedical NLP tasks.
- Supports: The model card contains a benchmark table showing numeric results for larger family members (e.g., XLarge and Large) and lists performance values (the card lists values including 0.63 and 23.4% without clear checkpoint-scoped attribution in the inspected locators).

### Repository commit (example usage and upload) - commit 751c87f2dfa77800e1bead7f9fb40f5734078e47

- URL: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47
- Publisher: OpenMed (hosted on Hugging Face repository)
- Type: `repository`
- Primary because: Commit blob contains installation instructions, example loading of the model via GLiNER.from_pretrained, example input text, and repository metadata including license statements used to verify checkpoint-level identity and usage.
- Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (commit-level metadata and example usage)
- Supports: Installation command for the model's dependencies is documented (pip install -q "gliner[tokenizers]").
- Supports: The model can be loaded with GLiNER.from_pretrained(model_name).
- Supports: The model identifier is 'OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M'.
- Supports: The repository states the license in the repository content (Apache License 2.0).
- Supports: Example input text used in the README is 'Early detection of breast cancer improves survival rates.' (present in commit-level content).

### Repository commit (tags and metadata) - commit 80b8848d04f30c35daacb06f89bc59b8ae0362be

- URL: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be
- Publisher: OpenMed (hosted on Hugging Face repository)
- Type: `repository`
- Primary because: Commit blob contains example usage demonstrating GLiNER.from_pretrained usage, example input text, label-list usage, prediction API call with threshold=0.5, and language/license tags used as primary evidence for example invocation semantics.
- Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (commit-level example usage and metadata)
- Supports: Example usage code sets model_name to 'OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M'.
- Supports: Example input text used in the README is 'Early detection of breast cancer improves survival rates.'
- Supports: The code example shows predicting entities with model.predict_entities(..., threshold=0.5).
- Supports: The example specifies the label list ['DISEASE'] for prediction.
- Supports: The repository tags the model language as English and lists license file as apache-2.0.

### gliner_config.json (blob) - model configuration

- URL: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blob/main/gliner_config.json
- Publisher: OpenMed (hosted on Hugging Face repository)
- Type: `repository`
- Primary because: Configuration file blob documents tokenizer class, vocabulary size, encoder base model, max input length, model_type 'gliner', and many architectural and training hyperparameters used as primary evidence for input preprocessing and architecture-level details.
- Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (gliner_config.json documented configuration)
- Supports: Tokenization/tokenizer class is 'T5Tokenizer'.
- Supports: Vocabulary size is 250102.
- Supports: Model type is 'gliner' and encoder base model is 'google/mt5-small'.
- Supports: Maximum input length (max_len) = 1024.
- Supports: Various encoder/decoder and training hyperparameters (encoder/decoder layers, attention heads, dropout, num_steps, etc.) are documented in the config.

### gliner_config.json (blame view) - configuration provenance

- URL: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/blame/main/gliner_config.json
- Publisher: OpenMed (hosted on Hugging Face repository)
- Type: `repository`
- Primary because: Blame view of gliner_config.json provides provenance and corroborates the configuration fields (tokenizer class, vocab size, model_type, max_len, learning rates, training scheduling) used to verify preprocessing and architecture claims.
- Scope: OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (gliner_config.json blame/provenance)
- Supports: Tokenizer class is 'T5Tokenizer'.
- Supports: Vocab and encoder configuration details (including google/mt5-small as encoder base).
- Supports: Training hyperparameters and model_type = 'gliner' are recorded in the file.

## Evidence gaps

- Evidence gap: No numeric public benchmark results tied specifically to the exact checkpoint OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M were present in the inspected primary-source locators. Checked locators: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M (model card main page, benchmark table and performance fields) and commit blobs (https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47 and https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be).
- Evidence gap: The inspected primary-source locators do not include a formal inference output JSON schema (field names, span object structure, token-level arrays, or exact score field names). Checked locators: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M and the cited commit blobs.
- Evidence gap: Tokenizer artifact file-level contents (explicit filenames such as tokenizer.json, vocab.txt, merges.txt) were not listed in the inspected research findings; checked locators: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M and https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47. Note: gliner_config.json documents tokenizer class and vocabulary size but not explicit artifact filenames in the inspected locators.
- Evidence gap: The inspected primary-source locators do not include creator-provided statements about PHI handling, data-retention policy, or explicit clinical-use authorization. Checked locators: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M, https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/751c87f2dfa77800e1bead7f9fb40f5734078e47, and https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/commit/80b8848d04f30c35daacb06f89bc59b8ae0362be.
- Evidence gap: No authoritative mapping from the supplied Forge wrapper slugs to an unchanged upstream checkpoint was verifiable from the inspected primary-source locators. Checked locators: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M and the cited commit blobs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses unapproved repository owner 'models' for this exact model scope: $.sources[6] uses unapproved repository owner 'models' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://huggingface.co/models?other=zero-shot-ner&p=2&sort=trending Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://huggingface.co/papers/2508.01630 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/OpenMed/OpenMed-ZeroShot-NER-Pathology-Tiny-60M/.gitattributes Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.inputPreparation_summary: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.outputInterpretation_summary: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
