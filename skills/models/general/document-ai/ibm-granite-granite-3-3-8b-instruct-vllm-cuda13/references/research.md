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

- Research key: `huggingface-co-ibm-granite-granite-3-3-8b-instruct-d64a1ab489`
- Independent audit: `revised`
- Researched: `2026-08-06T12:33:53.845016+00:00`

Checkpoint ibm-granite/granite-3.3-8b-instruct is documented in the Hugging Face model page and repository tree as an instruct-tuned variant of the Granite 3.3 family. Primary repository blobs for this checkpoint include tokenizer_config.json and vocab.json (at a specific commit) and a generation_config.json blob in the repository. The instruct checkpoint is reported in primary artifacts as an 8B decoder-only transformer and is distributed under Apache-2.0. Primary family-level IBM documentation and the base-model page provide context-window values that conflict numerically (base model page references a 128,000 token claim while IBM documentation and base-model config.json entries reference 131,072 tokens); this numeric discrepancy is not resolved by the checkpoint-scoped blobs inspected. No checkpoint-scoped numeric benchmark tables (dataset/split/metric rows) were found in the inspected checkpoint-scoped primary artifacts. No explicit Forge-serving manifest mapping or calibrated-probability output contract for this exact instruct checkpoint was found in the inspected checkpoint-scoped primary artifacts; those are recorded as evidence gaps below.

## Identity

- Upstream name: ibm-granite/granite-3.3-8b-instruct
- Checkpoint/version: ibm-granite/granite-3.3-8b-instruct
- Immutable revision: 3efd179a48ad7cb28ccf46568985af8cf38cbba9
- Parameter scale: 8 billion
- Architecture/head: decoder-only transformer
- License: Apache-2.0
- Evidence: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/commit/3efd179a48ad7cb28ccf46568985af8cf38cbba9, https://github.com/ibm-granite/granite-3.3-language-models, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/tokenizer_config.json, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/vocab.json

## Selection

### Recommended

- **Instruction following and conversational instruction-tuned text generation** — The Hugging Face model card for ibm-granite/granite-3.3-8b-instruct describes this checkpoint as an instruct-tuned variant intended for instruction following and improved instruction-tuned generation.
  Scope: ibm-granite/granite-3.3-8b-instruct
  Evidence: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- **Multi-step structured reasoning using prompt-delimited intermediate reasoning and final-answer tags** — The Hugging Face model card and repository examples for the instruct checkpoint document use of structured reasoning tags and instruct-tuning improvements for reasoning tasks.
  Scope: ibm-granite/granite-3.3-8b-instruct
  Evidence: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main
- **Code generation and fill-in-the-middle (FIM) style code completion (subject to downstream validation)** — Family-level repository documentation for Granite 3.3 describes FIM support and code-oriented training improvements; the instruct checkpoint is part of that family and the checkpoint repository contains tokenizer entries related to FIM tokens.
  Scope: ibm-granite/granite-3.3-8b-instruct (family-level FIM support; per-deployment validation required)
  Evidence: https://github.com/ibm-granite/granite-3.3-language-models, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/tokenizer_config.json
- **Long-context document summarization and retrieval-augmented generation (RAG) workflows (conditional on end-to-end validation)** — Checkpoint-scoped artifacts and family-level documentation advertise long-context capabilities for the Granite 3.3 family; end-to-end retrieval stacks and quality-validation are required before production use given absence of checkpoint-scoped validation artifacts.
  Scope: ibm-granite/granite-3.3-8b-instruct (requires validated retrieval stacks and per-deployment checks)
  Evidence: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models

### Conditional

- **Retrieval-augmented generation (RAG) using published adapters/LoRA** — Only when adapters/LoRAs are published as explicit checkpoint-scoped primary artifacts and after end-to-end validation of retrieval correctness; verify adapter identity and loading procedures in the official Granite family repository or GGUF conversion repository before deployment.
  Scope: ibm-granite/granite-3.3-8b-instruct (requires explicit adapter/LoRA artifact)
  Evidence: https://github.com/ibm-granite/granite-3.3-language-models, https://github.com/ibm-granite/gguf
- **Multilingual production deployments** — Validate per-language quality for production use; family-level documentation lists supported languages but does not provide exhaustive checkpoint-scoped per-language benchmark tables.
  Scope: ibm-granite/granite-3.3-8b-instruct
  Evidence: https://github.com/ibm-granite/granite-3.3-language-models, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct

### Avoid

- **Non-text modalities (image, audio, video) processing or native multimodal tasks** — Checkpoint-scoped primary artifacts for the instruct checkpoint document text-oriented instruction-following capabilities; no checkpoint-scoped primary artifact documents native multimodal input processing for this checkpoint.
  Scope: ibm-granite/granite-3.3-8b-instruct
  Evidence: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models
- **Clinical decision-making or PHI-handling regulated deployments without external certification** — Inspected checkpoint-scoped and family-level primary artifacts do not document checkpoint-scoped clinical certifications or PHI-handling approvals; external certification and domain-specific validation are required before regulated clinical use.
  Scope: ibm-granite/granite-3.3-8b-instruct
  Evidence: https://github.com/ibm-granite/granite-3.3-language-models, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation

## Input preparation

### Semantic inputs

- Plain-text prompts and structured chat-style messages (text-only inputs). Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- Structured reasoning/control tags (literal text markers such as '<think></think>' and '<response></response>') are used in model-card examples to separate intermediate reasoning from final answers. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- Token-level vocabulary entries and special tokens (including FIM-related tokens) are present in the checkpoint tokenizer blobs and should be used by downstream tokenizers to reproduce canonical tokenization. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/vocab.json, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/tokenizer_config.json

### Accepted formats

- Text/plain prompt payloads and structured textual chat messages (text-only). Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct

### Preprocessing

- Respect generation configuration metadata (bos_token_id, eos_token_id, pad_token_id) present in generation_config.json when performing tokenization and generation. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/main/generation_config.json
- Use the repository tokenizer_config.json and vocab.json blobs associated with the instruct checkpoint to reproduce canonical tokenization (special tokens, padding side, vocab size). Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/tokenizer_config.json, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/vocab.json

### Pre-submit validation

- Validate that inputs are text-only and avoid non-text MIME types because checkpoint-scoped primary artifacts document text-focused instruction tasks. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models
- When using structured tags or tool fields, validate message ordering and field names against the repository's chat-template commits and examples to prevent malformed control messages. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/commit/3efd179a48ad7cb28ccf46568985af8cf38cbba9

### Task-specific formatting

- Use literal structured reasoning tags '<think></think>' and '<response></response>' in prompts as shown in the Hugging Face model-card examples to delineate intermediate reasoning from final answers. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- Inspect repository chat-template examples and committed files in the instruct repository tree to confirm exact message ordering and any 'tools'/'available_tools' fields before deploying tool-calling integrations. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/commit/3efd179a48ad7cb28ccf46568985af8cf38cbba9
- Evidence gap: No single canonical prompt-template artifact enumerating every field, ordering, and tooling metadata for this exact instruct checkpoint was found in the inspected checkpoint-scoped repository and model-card artifacts. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main

## Output interpretation

### Outputs

- Primary outputs are generated textual token sequences forming natural-language responses. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- Structured outputs may be produced by surrounding the final answer with '<response></response>' tags, per model-card examples; '<think></think>' is documented as an intermediate reasoning marker in the model-card examples. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct

### Interpretation

- Treat content inside '<think></think>' as intermediate reasoning markers and '<response></response>' as the intended final answer when used consistently, as demonstrated in the model-card examples. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- Evidence gap: The inspected checkpoint-scoped primary artifacts do not document returned calibrated confidence scores or explicit numeric probability fields for model outputs for this exact instruct checkpoint. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models

### Post-inference validation

- Post-inference validation should include human review for high-risk outputs and verification of retrieved facts when used with retrieval; family-level documentation recommends governance and validation procedures. Sources: https://github.com/ibm-granite/granite-3.3-language-models, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation
- Apply sanity checks for truncation and hallucination, especially for long-context tasks, because checkpoint-scoped primary artifacts advertise long-context capabilities but provide no upstream postprocessing guarantees. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Task- and protocol-specific comparisons vs. peers
- Criteria: No checkpoint-scoped peer primary benchmark artifacts (matching dataset, split, metric, and protocol) were available in the reviewed canonical sources to enable a protocol-matched comparison for this exact checkpoint.
- Rationale: Checkpoint-scoped primary artifacts (Hugging Face model card and repository, Granite family repository, IBM watsonx documentation) do not publish numeric benchmark tables or the protocol details required for direct, protocol-matched comparisons.
- Comparison conditions: Checked checkpoint-scoped model card, repository tree, and family-level documentation for numeric benchmark tables and protocol details; none provided checkpoint-scoped numeric results or matching peer artifacts.
- Evidence: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation

## Limitations and safety

### Limitations

- Primary family-level sources describe governance and training-data review but do not publish a complete provenance listing for all training data used for this exact instruct checkpoint. Sources: https://github.com/ibm-granite/granite-3.3-language-models, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- The exact maximum context length is inconsistent across primary artifacts inspected: the Hugging Face base model page references a 128,000 token claim while IBM watsonx family documentation and the base-model config.json reference 131,072 tokens; the checkpoint-scoped artifacts do not resolve this numeric discrepancy. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-base, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/config.json
- Evidence gap: Canonical checkpoint-scoped artifacts inspected do not publish numeric benchmark tables (per-dataset numeric rows and protocols) for common evaluation suites; secondary aggregator results were not treated as primary and are not used here. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models
- Primary checkpoint-scoped artifacts do not document returned calibrated confidence scores or explicit numeric probability fields for this exact checkpoint; downstream calibration is required for use cases needing calibrated confidence estimates. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models

### Safety

- Family- and repository-level ethical considerations, governance, and GRC evaluation notes are documented in the Granite family repository; follow IBM's documented governance and validation steps when deploying this checkpoint. Sources: https://github.com/ibm-granite/granite-3.3-language-models
- The inspected primary artifacts do not provide checkpoint-scoped clinical certifications or PHI-handling approvals; avoid using this checkpoint for clinical decision-making without external certification and domain-specific validation. Sources: https://github.com/ibm-granite/granite-3.3-language-models, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation
- When using adapters, LoRAs, or GGUF-quantized distributions, validate conversion and adapter provenance from the official Granite family repository and the GGUF conversion repository and review security/provenance implications before deployment. Sources: https://github.com/ibm-granite/granite-3.3-language-models, https://github.com/ibm-granite/gguf

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: ibm-granite/granite-3.3-8b-instruct

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct
- Publisher: ibm-granite (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model page for the exact instruct checkpoint; contains model description, instruct examples, and links to repository blobs for this checkpoint.
- Scope: ibm-granite/granite-3.3-8b-instruct
- Supports: instruction-tuned claims and structured-reasoning tag examples
- Supports: model identifier is ibm-granite/granite-3.3-8b-instruct
- Supports: links to repository artifacts for the instruct checkpoint

### Hugging Face repository tree for granite-3.3-8b-instruct

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main
- Publisher: ibm-granite (Hugging Face)
- Type: `repository`
- Primary because: Repository tree for the exact instruct checkpoint containing example templates and references to checkpoint-scoped blobs.
- Scope: ibm-granite/granite-3.3-8b-instruct (repository artifacts)
- Supports: example prompts and README content
- Supports: locators for generation_config.json and tokenizer/vocab blobs

### Hugging Face commit (weights/config/tokenizer upload) for granite-3.3-8b-instruct

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/commit/3efd179a48ad7cb28ccf46568985af8cf38cbba9
- Publisher: ibm-granite (Hugging Face)
- Type: `repository`
- Primary because: Commit page documenting a repository commit that updates tokenizer/config blobs associated with the instruct checkpoint; used as a revision locator.
- Scope: ibm-granite/granite-3.3-8b-instruct (commit/revision)
- Supports: commit hash for uploaded model/config/tokenizer artifacts for the instruct checkpoint

### tokenizer_config.json (instruct checkpoint blob)

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/tokenizer_config.json
- Publisher: ibm-granite (Hugging Face)
- Type: `repository`
- Primary because: Repository-hosted tokenizer configuration blob associated with the instruct checkpoint containing special tokens and tokenizer settings.
- Scope: ibm-granite/granite-3.3-8b-instruct (tokenizer blob at specific commit)
- Supports: tokenizer configuration and special-token entries for the instruct checkpoint

### vocab.json (instruct checkpoint blob)

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/vocab.json
- Publisher: ibm-granite (Hugging Face)
- Type: `repository`
- Primary because: Repository-hosted tokenizer vocabulary blob associated with the instruct checkpoint.
- Scope: ibm-granite/granite-3.3-8b-instruct (vocab blob at specific commit)
- Supports: tokenizer vocabulary for the instruct checkpoint

### generation_config.json for granite-3.3-8b-instruct (repository blob)

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/main/generation_config.json
- Publisher: ibm-granite (Hugging Face)
- Type: `repository`
- Primary because: Repository-hosted generation configuration file documenting token ids and generation defaults for the instruct checkpoint.
- Scope: ibm-granite/granite-3.3-8b-instruct (generation_config.json)
- Supports: generation_config.json metadata (bos_token_id, eos_token_id, pad_token_id) for the checkpoint

### config.json (instruct checkpoint config blob)

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/config.json
- Publisher: ibm-granite (Hugging Face)
- Type: `repository`
- Primary because: Repository-hosted model configuration blob associated with the instruct checkpoint (architecture and max_position_embeddings entries referenced).
- Scope: ibm-granite/granite-3.3-8b-instruct (config blob at specific commit)
- Supports: architecture entries and max_position_embeddings referenced for the family/base config

### Hugging Face model card: granite-3.3-8b-base (context-length and architecture reference)

- URL: https://huggingface.co/ibm-granite/granite-3.3-8b-base
- Publisher: ibm-granite (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face page for the base model used as a base-level reference for architecture and an advertised 128K context-length claim.
- Scope: granite-3.3-8b-base (base-model reference)
- Supports: advertised 128,000 token context length for the base model
- Supports: architecture and parameter-scale statements for the base model

### IBM watsonx documentation: foundation models (Granite family reference)

- URL: https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation
- Publisher: IBM
- Type: `official-documentation`
- Primary because: Official IBM watsonx documentation listing Granite family entries and family-level attributes such as architecture, parameter counts, supported languages, and an advertised context-window entry.
- Scope: Granite Instruct 3.3 family (family-level documentation)
- Supports: family-level architecture (decoder), parameter count for 8B instruct variant, and an advertised context-window entry (131,072 tokens listed)

### IBM Granite 3.3 language models GitHub repository (family-level)

- URL: https://github.com/ibm-granite/granite-3.3-language-models
- Publisher: ibm-granite (GitHub)
- Type: `repository`
- Primary because: Official Granite 3.3 family GitHub repository containing family-level release artifacts, governance notes, and references to capabilities and tooling.
- Scope: Granite 3.3 family (repository-level documentation)
- Supports: family-level release artifacts, governance and training-data evaluation claims, and FIM/structured-reasoning family-level documentation

### IBM GGUF repository (GGUF conversion and quantization workflows)

- URL: https://github.com/ibm-granite/gguf
- Publisher: ibm-granite (GitHub)
- Type: `repository`
- Primary because: Official GGUF conversion repository associated with Granite family conversion workflows and quantization references; used only where explicit checkpoint-scoped conversion artifacts are published.
- Scope: GGUF conversion workflows relevant to Granite family
- Supports: GGUF conversion workflows and references to source repositories including Granite

## Evidence gaps

- Evidence gap: Checkpoint-scoped numeric benchmark values and detailed evaluation protocols (per-dataset numeric rows for suites such as AlpacaEval-2.0, Arena-Hard, AIME24, MATH-500) are not published in the inspected checkpoint-scoped primary artifacts (Hugging Face model card and repository, Granite family repository, IBM watsonx documentation). Searched locations: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main, https://github.com/ibm-granite/granite-3.3-language-models, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation.
- Evidence gap: The exact maximum context length is inconsistent across primary artifacts inspected: the Hugging Face base model page cites a 128,000 token claim while IBM watsonx documentation and the base-model config.json reference 131,072 tokens. The checkpoint-scoped instruct artifacts inspected do not resolve this numeric discrepancy. Sources: https://huggingface.co/ibm-granite/granite-3.3-8b-base, https://ibm.com/docs/en/watsonx/w-and-w/2.3.x?topic=models-foundation, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/197882a006a895d35b9d807e77536ed10f65f4db/config.json.
- Evidence gap: No primary artifact inspected contains an explicit Forge-serving manifest that maps the Forge-serving slug 'ibm-granite-granite-3-3-8b-instruct-vllm-cuda13' (or any Forge slug) to this exact upstream checkpoint; checked checkpoint-scoped locations: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://github.com/ibm-granite/granite-3.3-language-models, https://github.com/ibm-granite/gguf.
- Evidence gap: The inspected checkpoint-scoped primary artifacts do not document returned calibrated confidence scores or explicit numeric probability fields for model outputs for this exact instruct checkpoint; checked blobs and model card: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct, https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/blob/main/generation_config.json.
- Evidence gap: No single canonical prompt-template file enumerating every field, ordering, and tooling metadata for this exact instruct checkpoint was found in the inspected checkpoint-scoped repository and model-card artifacts; searched: https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/tree/main and the model card at https://huggingface.co/ibm-granite/granite-3.3-8b-instruct.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 14 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://firexcore.com/blog/ibm-granite-3-3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'mungert' for this exact model scope: $.sources[8] uses unapproved repository owner 'mungert' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary host ollama.com: $.sources[9] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary host aws.amazon.com: $.sources[13] uses forbidden secondary host aws.amazon.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary URL https: $.sources[17] uses forbidden secondary URL https://huggingface.co/ibm-granite/granite-3.3-8b-instruct/discussions/1/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.inputPreparation_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
