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

- Research key: `build-nvidia-com-nvidia-llama-3-2-nv-embedqa-1b-v2-9adb739da2`
- Independent audit: `revised`
- Researched: `2026-07-23T23:20:13.125726+00:00`

Checkpoint-scoped summary using only verified primary NVIDIA and upstream sources in the dossier: The exact NIM checkpoint nvidia/llama-3.2-nv-embedqa-1b-v2 is documented by NVIDIA as a Llama 3.2 1B transformer embedding/retriever optimized for multilingual question-answer retrieval. NVIDIA primary documentation reports the model as having 1B scale, 16 layers, and an embedding size of 2048. NVIDIA materials state the model is intended to be served as a NIM (NeMo Retriever) embedding microservice and evaluated on multiple QA/retrieval benchmarks. NVIDIA support-matrix and NeMo microservices pages list varying maximum sequence-length values across documents (examples in this dossier show 8192, 4096, and 2048 tokens in different official pages), creating a conflict about a single canonical deployed infer token limit for the checkpoint. Canonical public tokenizer artifact locators (immutable tokenizer files) and an immutable NVIDIA-packaged weight/revision identifier for this exact NIM-served checkpoint were not located in the verified primary NVIDIA sources in the findings and are recorded as evidence gaps. Benchmark numeric claims reported on upstream nemotron modelcard pages are preserved as upstream-checkpoint evidence (not conflated with NIM serving identity) and are annotated with explicit provenance and the GitHub release mapping that links the upstream slug to the NIM slug where present.

## Identity

- Upstream name: nvidia/llama-3.2-nv-embedqa-1b-v2
- Checkpoint/version: nvidia/llama-3.2-nv-embedqa-1b-v2
- Immutable revision: not reported
- Parameter scale: 1B
- Architecture/head: Transformer (fine-tuned Llama 3.2 retriever); reported 16 layers; bi-encoder style embedding head; reported embedding dimension 2048
- License: Model weights: NVIDIA AI Foundation Models Community License (NVIDIA). Upstream Llama materials: Llama 3.2 Community License (Meta). (Distinct obligations for NVIDIA-packaged weights vs upstream Llama materials.)
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html, https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2, https://developer.nvidia.com/downloads/ai-foundation-models-license, https://developer.meta.com/ai/llama3_2/license

## Selection

### Recommended

- **Multilingual dense‑retrieval question answering (query→passage retrieval)** — NVIDIA NIM reference and Build.NVIDIA model landing describe the model as optimized for multilingual and cross‑lingual text QA retrieval and evaluated across multiple QA benchmarks and 26 languages.
  Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (NIM serving identity)
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2, https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html
- **Production embedding microservice deployment via NVIDIA NIM/NGC container (indexing and retrieval) after domain validation** — NGC container catalog and Build.NVIDIA deploy guidance document the model as an NIM microservice / NGC container intended for deployment; these are operational deployment artifacts.
  Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (NGC container / NIM deployment)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.2-nv-embedqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2/deploy

### Conditional

- **Long-document retrieval using dynamic/Matryoshka embeddings** — Only if the deployed NIM runtime/profile supports the larger sequence length profile and Matryoshka/dynamic embeddings as indicated in specific NVIDIA support-matrix or release-note pages; callers must validate the deployed infer endpoint token limit/profile and dynamic-embedding behavior prior to relying on long-context workflows.
  Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (NIM serving identity)
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html

### Avoid

- **Direct replacement of multimodal (image+text) embedding models for vision+text retrieval** — NeMo Retriever embedding microservice documentation and the NIM embedding references identify the embedding microservice and this checkpoint as text embedding models and document text-only embedding request/response behaviors; multimodal image+text support is not documented for this checkpoint in verified primary sources.
  Scope: nvidia/llama-3.2-nv-embedqa-1b-v2
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2

## Input preparation

### Semantic inputs

- Input modality: text (single string or list/array of UTF-8 strings) used as 'query' or 'passage' per the NIM request semantics. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference-grpc.html
- Intended semantic use: query and passage text for dense retrieval (bi-encoder contrastive retrieval). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html

### Accepted formats

- Accepted request formats include JSON REST embeddings requests with required 'model' and 'input' fields and optional 'input_type' and 'modality' fields as documented in the NIM embeddings REST reference; gRPC embedding requests accept a 'text' field (list of UTF‑8 strings) per the NeMo Retriever gRPC reference. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference-grpc.html

### Preprocessing

- Callers must chunk or truncate long documents upstream as needed to respect the deployed infer endpoint's maximum input length/profile; NVIDIA support-matrix and microservices pages document differing maximum sequence-length values for different profiles/configurations. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html, https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html
- Evidence gap: Canonical public tokenizer artifact locators (tokenizer.model, tokenizer.json, tokenizer_config.json) for the exact NIM-served checkpoint were not found in the verified primary NVIDIA documents in the findings.

### Pre-submit validation

- Validate request fields per the NIM REST/gRPC reference: REST embeddings requests require a 'model' field and an 'input' field (string or array of strings); the 'input_type' and 'modality' fields are available and documented in the REST reference. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/reference.html
- Evidence gap: There is no single reconciled canonical statement in the verified primary NVIDIA documents in the findings that defines a single deployed infer token limit for all profiles; multiple official pages list different maximum sequence-length values, so callers must verify the deployed NIM profile's token limit. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html

### Task-specific formatting

- No special prompt templates are documented for producing embeddings; inputs are standard text strings (or arrays) and may be labeled with 'input_type' such as 'query' or 'passage' per the NIM REST/gRPC references. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference-grpc.html

## Output interpretation

### Outputs

- The model outputs dense float embedding vectors per input; NVIDIA support-matrix and the NIM model reference report an embedding dimension of 2048 for this checkpoint. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2

### Interpretation

- Embeddings are intended to be used with vector similarity measures (dot product or cosine) for dense retrieval evaluation; NVIDIA modelcard/benchmark pages report Recall@5 for embed-only and embed+rerank pipelines separately for upstream nemotron modelcards. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2

### Post-inference validation

- No canonical NVIDIA primary document in the verified findings provides an explicit guarantee about default post-inference pooling or L2 normalization for embeddings; callers should validate pooling/normalization behavior on domain holdout data. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html
- Evidence gap: Verified primary NVIDIA sources in the findings do not state a canonical default post-inference pooling or normalization (e.g., L2) applied to embeddings for this exact NIM checkpoint.

## Public benchmarks

### Dense retrieval (BeIR/TextQA: Recall@5 aggregated over NQ, HotpotQA, FiQA, TechQA)

- Dataset/split: NQ, HotpotQA, FiQA, TechQA / aggregated (NQ, HotpotQA, FiQA, TechQA averaged)
- Metric/value: Recall@5 / 68.60% (`higher-is-better`)
- Model scope: llama-nemotron-embed-1b-v2 (upstream-checkpoint evidence; embed-only row on the upstream modelcard)
- Conditions: Embed-only evaluation (embed model used without a reranker); aggregated across the four listed datasets. This is reported on the upstream nemotron modelcard and is preserved as upstream-checkpoint evidence rather than a direct NIM infer endpoint result.
- Source: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard
- Locator: Benchmarks table row reporting embed-only Recall@5 aggregated over NQ, HotpotQA, FiQA, TechQA
- Caveat: This benchmark row is on the upstream nemotron modelcard and is treated as upstream-checkpoint evidence, not as a direct callable NIM infer endpoint result.
- Caveat: If the reported pipeline includes a reranker or downstream step, that dependency is not implied to be callable from the NIM embedding endpoint unless NVIDIA documents the pipeline as exposed by the NIM service (the modelcard separates embed-only and embed+rerank rows).
- Caveat: Mapping between the upstream nemotron slug and the NIM serving slug is documented in an NVIDIA GitHub release mapping and is preserved as provenance; benchmark values remain upstream-checkpoint evidence unless NVIDIA explicitly states equivalence on a single canonical serving page.

## Comparisons

### nvidia-llama-nemotron-embed-1b-v2 — `insufficient-evidence`

- Task: Dense retrieval (BeIR/TextQA: Recall@5 aggregated over NQ, HotpotQA, FiQA, TechQA)
- Criteria: Protocol alignment and exact checkpoint identity
- Rationale: The upstream nemotron modelcard reports matching numeric Recall@5 values, but those rows are upstream-checkpoint evidence; the dossier preserves them as upstream evidence and does not conflate identities without a single canonical NVIDIA serving page that reports the same benchmark as produced by the NIM infer endpoint.
- Comparison conditions: Upstream modelcard vs NIM-serving slug identity mapping considerations; explicit mapping exists in a GitHub release but benchmark provenance remains upstream-checkpoint evidence.
- Evidence: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://github.com/NVIDIA-AI-Blueprints/rag/releases

### nvidia/llama-3_2-nemoretriever-300m-embed-v1 — `insufficient-evidence`

- Task: Dense retrieval (BeIR/TextQA: Recall@5 aggregated over NQ, HotpotQA, FiQA, TechQA)
- Criteria: Benchmark parity; different model scale (300M vs 1B) requires matched-protocol re-evaluation
- Rationale: The verified NIM reference for the 300M NeMo Retriever variant reports a different average Recall@5; because this candidate is a different model scale, direct parity with the 1B nv-embedqa-v2 cannot be assumed without a matched-protocol re-evaluation.
- Comparison conditions: Different model scale (300M vs 1B) and matched-protocol re-evaluation required.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-

### insufficient-evidence — `insufficient-evidence`

- Task: Dense retrieval (BeIR/TextQA aggregate)
- Criteria: No same-protocol primary benchmark in the verified findings for the listed third-party alternatives
- Rationale: The verified primary findings do not contain canonical per-checkpoint BeIR/TextQA aggregated Recall@5 entries for the many third-party alternatives that would allow same-protocol comparisons; therefore protocol-matched comparisons cannot be established from the verified primary sources.
- Comparison conditions: No same-protocol primary benchmark rows available in the verified findings for the alternatives referenced in the draft.
- Evidence:

## Limitations and safety

### Limitations

- Official NVIDIA primary documents in the verified findings list differing maximum sequence-length values for the checkpoint across pages/profiles (examples include 8192, 4096, and 2048 tokens); there is no single reconciled canonical deployed infer token limit present in the verified primary sources in the findings. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html, https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html
- Primary NVIDIA documentation in the verified findings does not deeply enumerate dataset provenance or scientific dataset limitations for this checkpoint; users must perform domain validation and evaluation before deployment. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2
- Evidence gap: Canonical public tokenizer artifact locators and an immutable upstream weight/revision identifier for the exact NIM-served checkpoint were not found in the verified primary NVIDIA documents in the findings; no authoritative public tokenizer file URL or immutable upstream-weight-revision locator is present in the verified findings.

### Safety

- Model weights and use are governed by the NVIDIA AI Foundation Models Community License for NVIDIA-packaged artifacts and by the Llama 3.2 Community License for upstream Llama materials; users must accept and comply with those license texts. Sources: https://developer.nvidia.com/downloads/ai-foundation-models-license, https://developer.meta.com/ai/llama3_2/license
- Users must ensure legal and compliance checks (export controls, acceptable-use policy) per the NVIDIA and upstream Llama license texts and any corporate/region policies that apply. Sources: https://developer.nvidia.com/downloads/ai-foundation-models-license, https://nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license
- Evidence gap: The verified primary NVIDIA documents in the findings do not include checkpoint-specific authoritative guidance for privacy/PII handling, clinical/medical safety, or biosecurity restrictions for this checkpoint; these domains require additional legal and domain-specific review before deployment.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NIM reference: nvidia-llama-3_2-nv-embedqa-1b-v2

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM reference page for the exact checkpoint; contains checkpoint-scoped statements about architecture, embedding size (2048), multilingual intended use, Matryoshka embeddings, and long-context support claims used in this dossier.
- Scope: nvidia/llama-3_2-nv-embedqa-1b-v2
- Supports: Architecture and intended use for multilingual QA retrieval
- Supports: Reported embedding size of 2048
- Supports: Statement of Matryoshka (dynamic) embeddings
- Supports: Claims about long-context support as stated in this reference

### NIM reference: nvidia-llama-nemotron-rerank-1b-v2 (benchmarks / upstream modelcard)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official upstream modelcard / benchmark documentation used as upstream-checkpoint evidence for reported benchmark rows.
- Scope: llama-nemotron-rerank-1b-v2 / llama-nemotron-embed-1b-v2
- Supports: Upstream benchmark rows for embed-only and embed+rerank pipelines (used as upstream-checkpoint evidence)

### Build.NVIDIA model landing: llama-3_2-nv-embedqa-1b-v2

- URL: https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official Build.NVIDIA landing page for the exact Forge-served variant; used to confirm intended use and deployment guidance.
- Scope: nvidia/llama-3_2-nv-embedqa-1b-v2
- Supports: Description of the model as multilingual/cross-lingual text QA retrieval with long context support
- Supports: Deployment guidance and model description used in dossier

### Build.NVIDIA deploy guidance for llama-3_2-nv-embedqa-1b-v2

- URL: https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2/deploy
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official Build.NVIDIA deployment page with NGC/NIM usage examples and a sample API call referencing the model slug.
- Scope: nvidia/llama-3_2-nv-embedqa-1b-v2 (deploy guidance)
- Supports: Docker/NGC deployment example and sample API request showing the model slug and input_type usage

### NGC catalog entry: llama-3.2-nv-embedqa-1b-v2 (container)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.2-nv-embedqa-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NGC container catalog entry for the NIM image used to deploy the model; used as operational/packaging evidence.
- Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (NGC container)
- Supports: NGC container metadata and production packaging for deployment

### NGC catalog entry (alternate): llama-3.2-nv-embedqa-1b-v2 (pb25h2)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.2-nv-embedqa-1b-v2-pb25h2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Alternate/related NGC container catalog entry referenced in the findings as an official NGC packaging instance.
- Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (NGC container variant)
- Supports: NGC container catalog listing and packaging metadata

### NeMo microservices embedding documentation (embedding docs)

- URL: https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NeMo microservices embedding documentation referenced for embedding model behavior and deployment guidance.
- Scope: NeMo Retriever embedding microservice guidance
- Supports: Embedding model description, recommended use, and some sequence-length indications

### NeMo Retriever gRPC reference (text embedding)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference-grpc.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official gRPC documentation for the NIM text embedding service describing request fields and supported request formats.
- Scope: nvidia_llama_3_2_nv_embedqa_1b_v2 (gRPC request mapping)
- Supports: gRPC request shape including 'text' field and optional 'modality' semantics

### NIM text-embedding support matrix (1.10.0)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Support-matrix page listing maximum token length, embedding dimension, parameter counts, and dynamic-embedding support for the checkpoint.
- Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (support-matrix v1.10.0)
- Supports: Lists maximum token length as 8192 tokens (per this support-matrix page)
- Supports: Reports embedding dimension 2048 and parameter counts (973M excluding embeddings; total 1236M)
- Supports: States dynamic embeddings support

### NIM text-embedding support matrix (latest)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Latest support-matrix page listing alternative sequence-length/profile values and non-optimized/optimized configuration notes.
- Scope: nvidia/llama-3.2-nv-embedqa-1b-v2 (support-matrix latest)
- Supports: Lists non-optimized configuration max token length 4096 and default VLM profile 2048 (per this support-matrix page)
- Supports: Reports embedding dimension 2048

### NIM text-embedding REST reference (v2.2.0)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: REST reference documenting required request fields and supported input/modality/embedding_type parameters for NIM embedding endpoints.
- Scope: NIM /v1/embeddings REST reference
- Supports: Documents required 'model' and 'input' fields and optional 'input_type' and 'modality' fields for embedding requests

### NIM text-embedding release notes

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes documenting added support (e.g., Matryoshka dynamic embeddings) and NIM version mappings for the embedding models.
- Scope: NeMo Retriever text-embedding release notes
- Supports: Documented addition of support for Matryoshka/dynamic embeddings and model support changes

### Build.NVIDIA upstream modelcard: llama-nemotron-embed-1b-v2 (benchmarks)

- URL: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Upstream modelcard containing benchmark table rows used as upstream-checkpoint evidence for Recall@5 values.
- Scope: llama-nemotron-embed-1b-v2 (upstream modelcard)
- Supports: Embed-only and embed+rerank Recall@5 benchmark rows for various embedding dimensions and datasets

### GitHub: NVIDIA-AI-Blueprints RAG releases (slug mapping)

- URL: https://github.com/NVIDIA-AI-Blueprints/rag/releases
- Publisher: NVIDIA (GitHub organization)
- Type: `repository`
- Primary because: Release notes that map the NIM serving slug to the upstream nemotron modelcard slug; used as canonical mapping evidence present in the findings.
- Scope: mapping between nvidia/llama-3.2-nv-embedqa-1b-v2 and nvidia/llama-nemotron-embed-1b-v2
- Supports: Mapping statement linking the Forge/NIM serving slug to the upstream nemotron modelcard slug

### Developer page: AI Foundation Models license (NVIDIA)

- URL: https://developer.nvidia.com/downloads/ai-foundation-models-license
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical NVIDIA AI Foundation Models Community License document referenced in the findings.
- Scope: applies to NVIDIA-packaged model weights
- Supports: Governing license text for NVIDIA-packaged model weights

### NVIDIA Community Model License (Enterprise Software page)

- URL: https://nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Enterprise software licensing page referenced in the findings relevant to NVIDIA community model licensing.
- Scope: license/agreements
- Supports: Enterprise license references relevant to community model licensing

### Upstream Llama 3.2 Community License (Meta)

- URL: https://developer.meta.com/ai/llama3_2/license
- Publisher: Meta
- Type: `official-documentation`
- Primary because: Canonical upstream Llama 3.2 Community License text included in the findings and used to distinguish upstream license obligations.
- Scope: Meta Llama 3.2 upstream materials (license)
- Supports: Upstream Llama 3.2 Community License statements cited in the dossier

### Cited official first-party source

- URL: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-
- Publisher: catalog.ngc.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-llama-3-2-nv-embedqa-1b-v2
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Publisher: docs.api.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-llama-3-2-nv-embedqa-1b-v2
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-llama-3-2-nv-embedqa-1b-v2
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: Canonical public tokenizer artifact locators (tokenizer.model, tokenizer.json, tokenizer_config.json) for the exact NIM-served checkpoint were not found in the verified primary NVIDIA documents in the findings.
- Evidence gap: An immutable NVIDIA-packaged weight file path or immutable revision identifier for the exact NIM-served checkpoint was not located in the verified primary NVIDIA sources in the findings.
- Evidence gap: No single reconciled canonical deployed infer token limit/profile is present in the verified primary NVIDIA sources in the findings; official pages list differing maximum sequence-length values (examples include 8192, 4096, and 2048 tokens) across documents and profiles.
- Evidence gap: The verified primary NVIDIA documents in the findings do not state a canonical default post-inference pooling or normalization (e.g., L2) applied to embeddings for this exact NIM checkpoint.
- Evidence gap: The verified primary NVIDIA documents in the findings do not provide checkpoint-specific authoritative guidance for privacy/PII handling, clinical/medical safety, or biosecurity restrictions for this checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 37 deterministic draft defect(s) were supplied to the audit.

- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[2]: $.comparisons[2]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[3]: $.comparisons[3]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[4]: $.comparisons[4]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[5]: $.comparisons[5]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[6]: $.comparisons[6]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[7]: $.comparisons[7]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[8]: $.comparisons[8]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[9]: $.comparisons[9]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[10]: $.comparisons[10]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[11]: $.comparisons[11]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[12]: $.comparisons[12]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[13]: $.comparisons[13]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[14]: $.comparisons[14]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[15]: $.comparisons[15]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[16]: $.comparisons[16]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[17]: $.comparisons[17]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[18]: $.comparisons[18]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[19]: $.comparisons[19]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[20]: $.comparisons[20]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[21]: $.comparisons[21]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1] uses forbidden secondary host ai.azure.com: $.sources[1] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nemo/microservices/25.8.0/fine-tune/models/embedding.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://zilliz.com/ai-models/bge-m3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks[0].evidenceUrls: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
