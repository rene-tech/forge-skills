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

- Research key: `huggingface-co-openai-gpt-oss-20b-4fb7165743`
- Independent audit: `revised`
- Researched: `2026-08-06T13:29:26.840590+00:00`

Primary upstream materials (OpenAI repository and model pages, the canonical arXiv model card, canonical tiktoken files, the Hugging Face distributed model page, and NVIDIA vendor documentation) describe gpt-oss-20b as an open-weight, text-only Mixture-of-Experts (MoE) transformer released under Apache-2.0. The available primary locators list gpt-oss-20b with ~21B total parameters, 32 experts, 4 active experts per token (≈3.6B active parameters per forward pass), and identify Harmony as the response format used for training and agentic flows. Primary sources inspected do not report an immutable distributed checkpoint artifact identifier (e.g., an immutable registry artifact name or a published checkpoint hash) for the gpt-oss-20b weights; primary numeric downstream benchmark tables tied to an immutable checkpoint and protocol-matched across variants were not located in the inspected primary sources. Training-time default sequence-length configuration (4096 tokens) is documented in vendor training/service documentation and appears distinct from the large inference context-length values reported in OpenAI announcements/developer docs; both locators are cited below.

## Identity

- Upstream name: gpt-oss-20b
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 21B total parameters
- Architecture/head: Mixture-of-experts (MoE) transformer; 32 total experts with 4 active experts per token producing ~3.6B active parameters per forward pass (sparse MoE)
- License: Apache-2.0
- Evidence: https://github.com/openai/gpt-oss, https://openai.com/index/introducing-gpt-oss, https://openai.com/index/gpt-oss-model-card, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html, https://huggingface.co/openai/gpt-oss-20b, https://arxiv.org/pdf/2508.10925

## Selection

### Recommended

- **Agentic instruction-following workflows with tool use (function calling, structured outputs, multi-step reasoning)** — OpenAI official model card and repository materials describe the GPT-OSS family as designed for agentic workflows with structured outputs, chain-of-thought style reasoning, and tool-enabled capabilities; the upstream repository provides Harmony-format templates/adapters intended for such flows.
  Scope: gpt-oss-20b upstream checkpoint and repository-provided Harmony templates/adapters as documented by OpenAI
  Evidence: https://openai.com/index/gpt-oss-model-card, https://github.com/openai/gpt-oss, https://huggingface.co/openai/gpt-oss-20b
- **Text-only coding, STEM, and general-knowledge reasoning tasks suitable for a text-only MoE model** — OpenAI model card and vendor documentation characterize gpt-oss-20b as a text-only model with instruction-following and reasoning capabilities applicable to coding and STEM tasks.
  Scope: gpt-oss-20b as characterized by OpenAI model card and NVIDIA vendor model pages
  Evidence: https://openai.com/index/gpt-oss-model-card, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html, https://build.nvidia.com/openai/gpt-oss-20b/modelcard

### Conditional

- **Tool-enabled reasoning that relies on Harmony-format structured outputs or repository adapters/templates** — Requires using the Harmony response format and the upstream repository-provided adapters/templates or correctly applying the Harmony-format chat template; omitting Harmony-format structure or adapters may produce degraded or incorrect agentic behavior.
  Scope: gpt-oss-20b when used in agentic/tool-enabled flows relying on Harmony-format outputs
  Evidence: https://github.com/openai/gpt-oss, https://huggingface.co/openai/gpt-oss-20b, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html

### Avoid

- **Deploying or querying the model in agentic/tool workflows without applying Harmony response-format templates or repository-provided adapters** — Upstream repository and model-card materials indicate the models were trained on the Harmony response format and provide Harmony-format templates/adapters; agentic flows are documented as relying on Harmony-format templates/adapters for correct structured outputs and tool interactions.
  Scope: gpt-oss-20b used in agentic or tool-enabled deployments
  Evidence: https://github.com/openai/gpt-oss, https://openai.com/index/gpt-oss-model-card, https://huggingface.co/openai/gpt-oss-20b

## Input preparation

### Semantic inputs

- Plain-text prompts intended for instruction-following, chain-of-thought reasoning, coding, and tool-use workflows (text-only inputs). Sources: https://openai.com/index/gpt-oss-model-card, https://huggingface.co/openai/gpt-oss-20b
- Agentic or structured-output requests are expected to use the Harmony response format or repository-provided adapters/templates to produce Harmony-format structured responses. Sources: https://github.com/openai/gpt-oss, https://huggingface.co/openai/gpt-oss-20b

### Accepted formats

- Harmony response format (repository-provided Harmony templates/adapters and the Transformers chat template that applies Harmony-format) for agentic and tool-enabled workflows. Sources: https://github.com/openai/gpt-oss, https://huggingface.co/openai/gpt-oss-20b
- Plain text input strings for text-only use cases (model inputs and outputs are text-only). Sources: https://openai.com/index/gpt-oss-model-card, https://build.nvidia.com/openai/gpt-oss-20b/modelcard

### Preprocessing

- Tokenization/encoding mapping for gpt-oss models uses the o200k_harmony encoding defined in canonical tiktoken sources; callers should use the tiktoken-provided o200k_harmony encoding when tokenizing Harmony-format inputs. Sources: https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py, https://github.com/openai/tiktoken/blob/main/tiktoken/model.py

### Pre-submit validation

- Validate that input length plus expected generation length fits within the model's supported context window: OpenAI announcement/model pages and developer docs report very large inference context lengths (examples: 128,000 tokens in the OpenAI announcement/introducing page and 131,072 tokens on the OpenAI developer model docs), while vendor training/service documentation lists a default training maximum sequence length of 4096 tokens (training-time configuration); these locators must be checked by implementers and reconciled for training/finetuning workflows. Sources: https://openai.com/index/introducing-gpt-oss, https://developers.openai.com/api/docs/models/gpt-oss-20b, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html

### Task-specific formatting

- Use upstream-provided Harmony templates/adapters or the repository chat template for agentic flows; the repository README and the Hugging Face model page reference these templates and the requirement to apply Harmony-format structure. Sources: https://github.com/openai/gpt-oss, https://huggingface.co/openai/gpt-oss-20b
- When invoking model.generate or other direct generation interfaces without adapters, apply Harmony-format structure manually consistent with the upstream repository templates and the model-card guidance. Sources: https://huggingface.co/openai/gpt-oss-20b, https://github.com/openai/gpt-oss

## Output interpretation

### Outputs

- Model outputs are plain text; when used with Harmony-enabled adapters/templates the outputs may include structured fields and chain-of-thought style content. Sources: https://openai.com/index/gpt-oss-model-card, https://github.com/openai/gpt-oss

### Interpretation

- Interpret generated text with awareness that Harmony-format runs may produce structured outputs and chain-of-thought; upstream guidance notes implementers should apply moderation and replicate system-level protections when deploying open-weight models. Sources: https://openai.com/index/gpt-oss-model-card, https://github.com/openai/gpt-oss

### Post-inference validation

- Post-inference validation should include safety checks and implementer-applied moderation/safeguard measures as recommended by the upstream model-card materials. Sources: https://openai.com/index/gpt-oss-model-card, https://github.com/openai/gpt-oss

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### gpt-oss-120b — `insufficient-evidence`

- Task: Architecture and reported parameter/active-parameter counts (model-family level)
- Criteria: Protocol- and checkpoint-matched numeric head-to-head superiority for downstream tasks requires protocol-aligned checkpoint-located benchmark tables for both checkpoints; primary sources inspected do not provide a single canonical, protocol-matched numeric benchmark table co-located with immutable checkpoint identifiers for both variants.
- Rationale: Primary OpenAI materials list per-model architecture and parameter/active-parameter counts for both gpt-oss-20b and gpt-oss-120b, but canonical, protocol-aligned, checkpoint-located numeric downstream benchmark tables that would establish head-to-head superiority across downstream tasks under identical protocols were not located in the inspected primary sources.
- Comparison conditions: Insufficient protocol-matched benchmark tables in primary sources for both checkpoints; comparisons would require identical prompts, dataset splits, and evaluation protocols reported alongside immutable checkpoint identifiers.
- Evidence: https://openai.com/index/introducing-gpt-oss, https://openai.com/index/gpt-oss-model-card, https://arxiv.org/pdf/2508.10925

## Limitations and safety

### Limitations

- Immutable checkpoint identifiers (artifact names, immutable registry IDs, or commit hashes for the distributed gpt-oss-20b checkpoint) are not reported in the inspected upstream materials. Sources: https://github.com/openai/gpt-oss, https://openai.com/index/gpt-oss-model-card, https://arxiv.org/pdf/2508.10925, https://huggingface.co/openai/gpt-oss-20b
- Training/inference sequence-length discrepancy: vendor documentation lists a default training maximum sequence length of 4096 tokens and notes sequence-packing is unsupported, while OpenAI announcement/developer pages report very large inference context lengths (locators cited). This is a documented distinction between vendor training config and OpenAI-reported inference context and may affect sequence-packing, fine-tuning, or training parity. Sources: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html, https://openai.com/index/introducing-gpt-oss, https://developers.openai.com/api/docs/models/gpt-oss-20b
- Evidence gap: Canonical, protocol-aligned, checkpoint-located numeric benchmark tables (task, split, metric, exact prompt/protocol) for downstream evaluations of gpt-oss-20b were not found in the inspected primary sources; implementers seeking protocol-matched benchmark claims must consult primary benchmark tables if and when they are published alongside immutable checkpoint identifiers. Sources: https://openai.com/index/introducing-gpt-oss, https://openai.com/index/gpt-oss-model-card, https://arxiv.org/pdf/2508.10925, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html, https://build.nvidia.com/openai/gpt-oss-20b/modelcard
- Evidence gap: Canonical primary-source operational reports of tokenizer/vocabulary mismatches or decoding failures for gpt-oss-20b were not located in the inspected upstream sources; community-reported runtime tokenizer issues (if any) are not documented in the primary locations checked and thus require primary-source confirmation. Sources: https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py, https://github.com/openai/tiktoken/blob/main/tiktoken/model.py, https://github.com/openai/gpt-oss, https://huggingface.co/openai/gpt-oss-20b

### Safety

- Upstream model-card guidance notes implementers must replicate or implement extra safeguards when deploying open-weight models and should apply moderation and safety checks for disallowed content. Sources: https://openai.com/index/gpt-oss-model-card
- Repository-level materials document Harmony-format tooling and usage patterns; deployers should follow repository guidance and apply human review and safeguard workflows appropriate to agentic/tool-enabled deployments. Sources: https://github.com/openai/gpt-oss, https://openai.com/index/gpt-oss-model-card

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### OpenAI GPT-OSS Repository

- URL: https://github.com/openai/gpt-oss
- Publisher: OpenAI
- Type: `repository`
- Primary because: Official upstream repository documenting GPT-OSS training/format requirements, templates, adapters, and reference implementations.
- Scope: gpt-oss-20b (repository-level documentation and templates)
- Supports: Models trained on Harmony response format and repository-provided Harmony templates/adapters
- Supports: Repository guidance on applying Harmony-format templates and chat templates for agentic flows
- Supports: Upstream usage and implementation notes for gpt-oss models

### OpenAI GPT-OSS releases

- URL: https://github.com/openai/gpt-oss/releases
- Publisher: OpenAI
- Type: `repository`
- Primary because: Repository releases page documenting release tags and associated commit metadata for the gpt-oss repository.
- Scope: gpt-oss repository release history (release tags and commit references)
- Supports: Repository release metadata and commit references used to inspect available repository artifacts

### Introducing GPT-OSS (OpenAI announcement)

- URL: https://openai.com/index/introducing-gpt-oss
- Publisher: OpenAI
- Type: `official-documentation`
- Primary because: Official announcement page listing per-model specs, high-level capability descriptions, and safety/format commentary.
- Scope: gpt-oss family (announcement-level capabilities and per-model specs)
- Supports: Announcement-level descriptions of architecture, per-model parameter/active-parameter counts, expert counts, and reported large inference context lengths
- Supports: High-level safety and training-format commentary (Harmony)

### GPT-OSS Model Card (OpenAI)

- URL: https://openai.com/index/gpt-oss-model-card
- Publisher: OpenAI
- Type: `official-documentation`
- Primary because: Official OpenAI model card with capability descriptions, usage guidance, and license statement.
- Scope: gpt-oss-20b (model-card level)
- Supports: Model described as text-only, Apache-2.0 licensed, and compatible with agentic/tool workflows
- Supports: Guidance that implementers should apply safeguards and moderation for open-weight deployments

### arXiv: GPT-OSS model card / preprint (PDF)

- URL: https://arxiv.org/pdf/2508.10925
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint of the GPT-OSS model card and associated technical descriptions.
- Scope: gpt-oss family (paper-level descriptions and sections)
- Supports: Paper-level description of GPT-OSS variants and model-architecture sections (e.g., Section 2.2 for architecture, Section 2.3 for tokenizer, Section 2.5.1 for Harmony chat format)

### tiktoken model-to-encoding mapping (model.py)

- URL: https://github.com/openai/tiktoken/blob/main/tiktoken/model.py
- Publisher: OpenAI
- Type: `repository`
- Primary because: Source file mapping model-name prefixes to canonical encodings, used to verify mapping of the "gpt-oss-" prefix to the o200k_harmony encoding.
- Scope: tiktoken mapping for model name prefixes
- Supports: Mapping of the "gpt-oss-" model name prefix to the o200k_harmony encoding

### tiktoken: o200k_harmony encoding definition (openai_public.py)

- URL: https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py
- Publisher: OpenAI
- Type: `repository`
- Primary because: Source file defining the o200k_harmony encoding and Harmony special tokens.
- Scope: tiktoken encoding constructors and Harmony special tokens
- Supports: Definition of the o200k_harmony encoding and Harmony special tokens used by GPT-OSS models

### GPT-OSS-20B Model Page (Hugging Face)

- URL: https://huggingface.co/openai/gpt-oss-20b
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Canonical Hugging Face model page for the distributed checkpoint with direct links to upstream README and usage notes authored or linked by OpenAI.
- Scope: gpt-oss-20b (Hugging Face distributed checkpoint page and model-card)
- Supports: Statements that the models were trained on the Harmony response format and that the Transformers chat template applies Harmony-format
- Supports: Links to upstream README and usage materials

### gpt-oss-20b config.json (Hugging Face repo blob)

- URL: https://huggingface.co/openai/gpt-oss-20b/blob/main/config.json
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Distributed checkpoint configuration file listing architecture fields relevant to runtime behavior.
- Scope: gpt-oss-20b distributed checkpoint configuration
- Supports: Configuration fields such as architecture class, experts_per_token, and initial_context_length as published with the distributed checkpoint

### NVIDIA NeMo Customizer: GPT-OSS documentation

- URL: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Vendor documentation describing GPT-OSS 20B architecture, active-parameter counts, Harmony requirement, and training default sequence length.
- Scope: gpt-oss-20b (vendor documentation and training/service notes)
- Supports: Statements that GPT-OSS 20B uses MoE architecture with specified active-parameter counts and that the model was trained on the Harmony response format
- Supports: Notes on default training maximum sequence length and lack of sequence-packing support

### NVIDIA Build model card: GPT-OSS-20B

- URL: https://build.nvidia.com/openai/gpt-oss-20b/modelcard
- Publisher: NVIDIA / Build
- Type: `official-documentation`
- Primary because: Vendor model-card summarizing licensing and model characteristics as published by NVIDIA Build.
- Scope: gpt-oss-20b (vendor model-card summary)
- Supports: Vendor confirmation of Apache-2.0 licensing metadata and model characteristics

### NVIDIA NGC catalog entry for GPT-OSS-20B container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/openai/containers/gpt-oss-20b
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NGC catalog entry documenting container metadata and licensing relationships between container and underlying model.
- Scope: gpt-oss-20b (NGC container/catalog entry)
- Supports: NGC container build metadata and licensing notes referencing the underlying Apache-2.0 model weights

### NVIDIA NGC container layers metadata (GPT-OSS-20B 2.0.2 layers)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/openai/containers/gpt-oss-20b/2.0.2/layers
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Container layers metadata showing environment variables and build details for a specific NGC container build.
- Scope: gpt-oss-20b NGC container layers and environment metadata
- Supports: Container environment variables and build metadata used to inspect serving/runtime packaging

### OpenAI Developer model docs: gpt-oss-20b

- URL: https://developers.openai.com/api/docs/models/gpt-oss-20b
- Publisher: OpenAI
- Type: `official-documentation`
- Primary because: Official developer-facing model documentation describing model capabilities and runtime parameters.
- Scope: gpt-oss-20b (developer API/model documentation)
- Supports: Developer-facing runtime claims including supported modalities, context window values reported by OpenAI, and API access notes

## Evidence gaps

- Evidence gap: Immutable checkpoint artifact identifiers or commit-level distributed model artifact names for the gpt-oss-20b weights were not found at the following primary locators inspected: https://github.com/openai/gpt-oss (README and repository contents), https://github.com/openai/gpt-oss/releases (release tags/notes), https://huggingface.co/openai/gpt-oss-20b (distributed model page and model-card), https://openai.com/index/gpt-oss-model-card (model card), https://arxiv.org/pdf/2508.10925 (paper sections and appendices).
- Evidence gap: Canonical, protocol-aligned, checkpoint-located numeric benchmark tables (dataset, split, metric, value, and exact prompt/protocol) for downstream evaluations of gpt-oss-20b were not located in the following primary sources and locators inspected: https://openai.com/index/introducing-gpt-oss (announcement page sections and tables), https://openai.com/index/gpt-oss-model-card (model card sections and appendices), https://arxiv.org/pdf/2508.10925 (paper body and appendices), https://docs.nvidia.com/nemo/microservices/latest/customizer/models/gpt-oss.html (vendor docs and model-card), https://build.nvidia.com/openai/gpt-oss-20b/modelcard (vendor model-card).
- Evidence gap: Canonical primary-source operational reports documenting tokenizer/vocabulary mismatches or decoding failures for gpt-oss-20b were not found at the following primary-source locators inspected: https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py (o200k_harmony encoding definition), https://github.com/openai/tiktoken/blob/main/tiktoken/model.py (model-prefix mapping), https://github.com/openai/gpt-oss (upstream repository README and docs), https://huggingface.co/openai/gpt-oss-20b (distributed model page and config.json). Implementers should treat operational tokenizer mismatch reports as an evidence gap until documented in primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 90 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property think_sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1]: $.inputPreparation.acceptedFormats[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1]: $.inputPreparation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[1]: $.inputPreparation.taskSpecificFormatting[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openai.com/index/introducing-gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openai.com/index/gpt-oss-model-card Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developers.openai.com/api/docs/models/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/tokenizer_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/generation_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/LICENSE Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/abs/2508.10925 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2508.12461v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://benchlm.ai/models/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-gpt-oss-20b.htm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/discussions/151 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://imoz.jp/scraps/202604_harmony.en.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/harmony Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://discuss.huggingface.co/t/what-are-all-the-files-that-are-being-downloaded/173329 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/USAGE_POLICY Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://aws.amazon.com/blogs/machine-learning/deploy-gpt-oss-models-with-amazon-bedrock-custom-model-import Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/gpt-oss-safeguard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/harmony Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openai.com/index/introducing-gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openai.com/index/gpt-oss-model-card Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developers.openai.com/api/docs/models/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openai.com/index/gpt-oss-model-card Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-gpt-oss-20b.htm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://blog.huggingface.co/openai-gpt-oss/ Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://imoz.jp/scraps/202604_harmony.en.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://discuss.huggingface.co/t/what-are-all-the-files-that-are-being-downloaded/173329 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2508.12461v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2508.12461v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://benchlm.ai/models/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2508.12461v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/discussions/151 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developers.openai.com/api/docs/models/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/abs/2508.10925 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://imoz.jp/scraps/202604_harmony.en.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/LICENSE Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/USAGE_POLICY Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b/blob/main/USAGE_POLICY Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/openai/harmony Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://openai.com/index/introducing-gpt-oss Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
