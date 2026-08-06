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

- Research key: `huggingface-co-abhinand-medembed-large-v0-1-e3fed155f5`
- Independent audit: `revised`
- Researched: `2026-08-06T10:54:29.362713+00:00`

Verified primary upstream evidence: the Hugging Face repository at https://huggingface.co/abhinand/MedEmbed-large-v0.1 is the official model page for the checkpoint named "MedEmbed-large-v0.1" and documents that MedEmbed is a family of embedding models fine-tuned for medical and clinical data, intended to improve information retrieval, question answering, and semantic search in healthcare contexts. The repository indicates training used a synthetic data generation pipeline named "synthetic-datagen-flow". The repository/commit history shows a specific upload/commit for the model files (commit 59c73573dedc2f8ffdb947399e276dd57e73f426) and that tokenizer files were uploaded in a separate commit (ea342da) per the commits listing. The model card or full documentation asserts performance improvements versus general-purpose embedding models but does not provide verified numeric checkpoint-matched benchmark rows or explicit numeric values at an exact table/figure locator within the inspected primary pages. Several checkpoint-specific operational facts (exact parameter count, exact tokenizer name/revision, maximum sequence length, truncation policy, pooling implementation, normalization defaults, output dimensionality and tensor shape, and an explicit model-weight SPDX/license text) are not reported on the inspected primary sources and have been converted into explicit evidence gaps referencing the exact Hugging Face pages and commit pages checked.

## Identity

- Upstream name: abhinand/MedEmbed-large-v0.1
- Checkpoint/version: MedEmbed-large-v0.1
- Immutable revision: 59c73573dedc2f8ffdb947399e276dd57e73f426
- Parameter scale: not reported
- Architecture/head: MedEmbed family embedding model fine-tuned specifically for medical and clinical data
- License: Evidence gap: checkpoint license not reported on https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426

## Selection

### Recommended

- **Medical and clinical information retrieval** — The Hugging Face model page documents that MedEmbed is fine-tuned for medical and clinical data and is intended to enhance information retrieval in healthcare contexts.
  Scope: abhinand/MedEmbed-large-v0.1 upstream checkpoint
  Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- **Semantic search over medical text** — The Hugging Face model page states intended use for semantic search in medical and clinical contexts.
  Scope: abhinand/MedEmbed-large-v0.1 upstream checkpoint
  Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- **Integration into healthcare research tools and literature search systems** — The Hugging Face model page indicates that the model can be integrated into healthcare systems and research tools to improve medical literature search.
  Scope: abhinand/MedEmbed-large-v0.1 upstream checkpoint
  Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1

### Conditional

- **Question answering in medical or clinical contexts (only with downstream validation)** — The model card lists intended use including question answering but does not provide an official callable QA head, prompting format, or evaluation protocol for this specific checkpoint; downstream validation and explicit pipeline definition are required before deployment for QA.
  Scope: abhinand/MedEmbed-large-v0.1 upstream checkpoint used as embeddings in downstream QA pipelines
  Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1

### Avoid

- **Selecting this checkpoint for tasks that require verified checkpoint-specific license terms** — An explicit model-weight or checkpoint SPDX license text is not reported on the inspected Hugging Face model page or commit page; license is therefore not verifiable from primary sources checked.
  Scope: abhinand/MedEmbed-large-v0.1
  Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- **Assuming this checkpoint is a standalone calibrated clinical/pathogenicity classifier** — Primary upstream evidence documents this checkpoint as an embedding model fine-tuned for medical data; no primary-source evidence shows the checkpoint itself emits calibrated clinical probabilities or a downstream classifier head.
  Scope: abhinand/MedEmbed-large-v0.1
  Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1

## Input preparation

### Semantic inputs

- Text is the accepted upstream modality supported by the model. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- The model is intended for medical and clinical natural language inputs (medical notes, literature, serialized variant annotations as text). Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1

### Accepted formats

- Plain text inputs (medical/clinical natural language) are the accepted upstream format described on the model page. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1

### Preprocessing

- The Hugging Face model page documents training used a synthetic data generation pipeline named "synthetic-datagen-flow". Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Tokenizer files were uploaded in a repository commit identified in the commits listing (tokenizer files uploaded in commit ea342da per the commits listing). Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519
- Evidence gap: The inspected primary sources do not specify tokenizer name or tokenizer revision for this checkpoint; inspected locators: Hugging Face model page and commits listing. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519
- Evidence gap: The inspected primary sources do not specify maximum sequence length, truncation policy, pooling procedure, or normalization defaults for this checkpoint; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519

### Pre-submit validation

- Evidence gap: The inspected primary sources do not provide a checkpoint-specific pre-inference validation checklist, input bounds, or explicit invalid-input rules; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426

### Task-specific formatting

- Evidence gap: The inspected primary sources do not provide an official prompt template, paired-input formatting rule, or serialized input schema for this checkpoint; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519

## Output interpretation

### Outputs

- The checkpoint is an embedding model used to produce semantic embeddings for medical and clinical text tasks (embedding vectors as output). Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Evidence gap: The inspected primary sources do not specify output dimensionality, tensor shape, datatype, or named output fields for this exact checkpoint; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426

### Interpretation

- Outputs should be interpreted as embeddings for similarity- or retrieval-oriented downstream use, not as calibrated probabilities. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Evidence gap: The inspected primary sources do not specify a canonical similarity metric or normalization rule for interpreting embedding distances for this checkpoint; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519

### Post-inference validation

- Evidence gap: The inspected primary sources do not provide checkpoint-specific post-inference calibration steps, acceptance thresholds, or QA checks for downstream decision-making; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### general-purpose embedding models — `insufficient-evidence`

- Task: Medical/clinical embedding performance (as claimed by model page)
- Criteria: The model card asserts outperforming general-purpose embedding models across medical NLP benchmarks but does not provide verifiable checkpoint-matched numeric values or exact table/figure locators on the inspected pages.
- Rationale: Primary-source model page claims comparative performance at a family/claim level but lacks numeric side-by-side checkpoint-matched benchmark rows at exact locators in the inspected primary sources.
- Comparison conditions: Inspected locators: Hugging Face model page and repository commits; no exact numeric tables or figures for the checkpoint were verifiable at those locators.
- Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1

## Limitations and safety

### Limitations

- The checkpoint is domain-specific: MedEmbed is described as fine-tuned specifically for medical and clinical data, which limits generalization outside medical contexts. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Evidence gap: The inspected primary sources do not report an exact parameter count for this checkpoint; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519
- Evidence gap: The inspected primary sources do not report tokenizer revision, pooling implementation, normalization behavior, or maximum context length for this checkpoint; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426
- Evidence gap: The inspected primary sources do not verify checkpoint-specific numeric benchmark tables/values with exact table/figure locators for this checkpoint; inspected locator: Hugging Face model page 'full documentation' claim of metrics without checkpoint-level numeric tables at the checked locations. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1

### Safety

- Use in healthcare contexts should be treated conservatively because the model is documented as intended for medical and clinical settings. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Evidence gap: The inspected primary sources do not provide a checkpoint-specific PHI handling policy, bias-mitigation procedure, or clinical safety governance framework; inspected locators: Hugging Face model page and commit pages. Sources: https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MedEmbed-large-v0.1

- URL: https://huggingface.co/abhinand/MedEmbed-large-v0.1
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official upstream model repository and model card for the checkpoint named in the dossier; contains model identity, intended use, training-note claims, and performance-claim summary.
- Scope: abhinand/MedEmbed-large-v0.1
- Supports: identity.upstreamName
- Supports: identity.checkpoint
- Supports: identity.architecture
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs
- Supports: researchSummary
- Supports: limitations (domain-specific)
- Supports: performance-claim (family-level) in full documentation

### MedEmbed-large-v0.1 commit 59c73573dedc2f8ffdb947399e276dd57e73f426

- URL: https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository commit page identifying the specific uploaded model files used as an immutable revision locator supporting identity.revision.
- Scope: abhinand/MedEmbed-large-v0.1 revision 59c73573dedc2f8ffdb947399e276dd57e73f426
- Supports: identity.revision
- Supports: identity.evidenceUrls (revision locator)
- Supports: evidenceGaps referencing inspected commit content

### MedEmbed-large-v0.1 commits listing

- URL: https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository commits listing showing history, including tokenizer file uploads and README updates used to verify what files/commits were present and to identify missing descriptive metadata.
- Scope: abhinand/MedEmbed-large-v0.1 commit history
- Supports: evidence about tokenizer files uploaded in commit ea342da
- Supports: evidence about README updates and commit history
- Supports: evidenceGaps regarding missing tokenizer name/revision and parameter count

## Evidence gaps

- Evidence gap: The inspected primary sources do not specify a model-weight SPDX/license text for abhinand/MedEmbed-large-v0.1; inspected locators: Hugging Face model page (https://huggingface.co/abhinand/MedEmbed-large-v0.1).
- Evidence gap: The inspected primary sources do not report an exact parameter count for abhinand/MedEmbed-large-v0.1; inspected locators: Hugging Face model page and commits listing (https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519).
- Evidence gap: The inspected primary sources do not provide tokenizer name or tokenizer revision for this checkpoint; inspected locators: Hugging Face model page and commits listing (https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commits/925025692000eece3a0824fd6cc4c9016a112519).
- Evidence gap: The inspected primary sources do not document maximum sequence length, truncation policy, pooling implementation, normalization defaults, or canonical similarity metric for abhinand/MedEmbed-large-v0.1; inspected locators: Hugging Face model page and commit pages (https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426).
- Evidence gap: The inspected primary sources do not specify output dimensionality, tensor shape, datatype, or named output fields for this checkpoint; inspected locators: Hugging Face model page and commit pages (https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426).
- Evidence gap: The inspected primary sources do not provide verifiable checkpoint-matched numeric benchmark tables/values with exact table/figure locators for this checkpoint though the model page claims improved performance; inspected locator: Hugging Face model page 'full documentation' (https://huggingface.co/abhinand/MedEmbed-large-v0.1).
- Evidence gap: The inspected primary sources do not provide checkpoint-specific post-inference calibration thresholds or acceptance criteria; inspected locators: Hugging Face model page and commit pages (https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426).
- Evidence gap: The inspected primary sources do not provide a checkpoint-scoped PHI handling policy or clinical governance procedures; inspected locators: Hugging Face model page and commit pages (https://huggingface.co/abhinand/MedEmbed-large-v0.1, https://huggingface.co/abhinand/MedEmbed-large-v0.1/commit/59c73573dedc2f8ffdb947399e276dd57e73f426).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 46 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1]: $.inputPreparation.acceptedFormats[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1]: $.inputPreparation.preprocessing[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1]: $.outputInterpretation.interpretation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'mradermacher' for this exact model scope: $.sources[6] uses unapproved repository owner 'mradermacher' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'aaditya' for this exact model scope: $.sources[9] uses unapproved repository owner 'aaditya' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'collections' for this exact model scope: $.sources[13] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2412.15258 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[9].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[10].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[11].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[11].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[11].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[11].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[12].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[12].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[12].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[12].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[13].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[13].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[13].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[13].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
