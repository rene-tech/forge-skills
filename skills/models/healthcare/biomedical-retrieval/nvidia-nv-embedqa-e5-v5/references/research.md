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

- Research key: `build-nvidia-com-nvidia-nv-embedqa-e5-01c8141b3b`
- Independent audit: `revised`
- Researched: `2026-07-23T20:39:57.925491+00:00`

NV-EmbedQA-E5-v5 (NV-EmbedQA-E5-v5) is an NVIDIA embedding model (transformer encoder fine-tuned from E5-Large-Unsupervised) intended for text question-answering retrieval and dense-retrieval pipelines. Primary NVIDIA documentation reports 24 transformer layers, 1024-dimensional output embeddings, and a parameter scale of 335 million. The model is distributed and invoked via the NeMo Retriever Text Embedding NIM (NVIDIA inference stack) and NVIDIA documentation lists supported hardware microarchitectures and TensorRT as an inference engine. The primary research paper in the provided findings reports runtime microbenchmarks (query latency and passage indexing throughput) for NV-EmbedQA-E5-v5 in Table 1 under an H100 + TensorRT deployment; the same paper and NVIDIA performance documentation describe BEIR QA evaluation datasets were used in benchmark evaluation but the provided findings do not include table-extracted retrieval-quality numeric values for NDCG@10. Official documentation presents a discrepancy on maximum input length (model reference lists 512 tokens; inference reference documents an 8192-token inference limit). Tokenizer name/version/vocabulary/normalization, exact checkpoint revision/hash, and API-level embedding dtype or documented normalization are not specified in the available primary sources and are recorded as evidence gaps.

## Identity

- Upstream name: NVIDIA Retrieval QA E5 Embedding Model
- Checkpoint/version: NV-EmbedQA-E5-v5
- Immutable revision: not reported
- Parameter scale: 335 million
- Architecture/head: Transformer encoder; fine‑tuned from E5‑Large‑Unsupervised; bi-encoder embedding model; 24 transformer layers; embedding dimensionality 1024
- License: Model provided under NVIDIA AI Foundation Models Community License Agreement and MIT (NIM/container governed by NVIDIA Software License Agreement/Product Specific Terms as documented)
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/abs/2409.07691, https://arxiv.org/pdf/2409.07691, https://arxiv.org/html/2409.07691v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/eula.html

## Selection

### Recommended

- **Dense retrieval / semantic search for question-answering over large text corpora** — NVIDIA official model reference describes NV-EmbedQA-E5-v5 as an embedding model optimized for text question-answering retrieval and intended for dense-retrieval pipelines; the NeMo Retriever Text Embedding NIM provides GPU-accelerated inference suitable for high-throughput indexing.
  Scope: NV-EmbedQA-E5-v5 served via NeMo Retriever Text Embedding NIM (NVIDIA inference/runtime)
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html
- **High-throughput document ingestion / passage encoding (indexing) as part of a two-stage retrieval + rerank pipeline** — Primary research paper and NVIDIA performance documentation report deployment-oriented throughput and latency measurements for NV-EmbedQA-E5-v5 and note pairing embedding models with rerankers to improve final QA accuracy; the NIM packaging is oriented to production indexing pipelines.
  Scope: NV-EmbedQA-E5-v5 used as first-stage embedder in GPU-accelerated NeMo Retriever Text Embedding NIM (deployment with TensorRT for throughput/latency gains)
  Evidence: https://arxiv.org/html/2409.07691v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- **Embedding generation for RAG (Retrieval-Augmented Generation) pipelines where 1024-dim vectors are acceptable** — Official reference documents output embedding dimensionality of 1024 and positions the model for use in retrieval/RAG pipelines via NeMo Retriever.
  Scope: NV-EmbedQA-E5-v5 outputs 1024-dimensional embeddings when invoked via the NeMo Retriever Text Embedding NIM
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html

### Conditional

- **Domain tuning or further fine-tuning for specialist domains (e.g., biomedical retrieval)** — Primary sources indicate the model is an embedding model and document training on public datasets, but do not provide checkpoint-scoped biomedical fine-tuning or clinical-validation evidence for NV-EmbedQA-E5-v5; any domain adaptation must be followed by downstream validation, calibration, and expert review.
  Scope: NV-EmbedQA-E5-v5 (requires explicit downstream fine-tuning and validation; not provided in available primary sources)
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/abs/2409.07691
- **Use as part of two-stage retrieval + rerank pipelines to improve final QA accuracy** — Primary research reports pairing embedding and reranker models in two-stage pipelines and reports deployment/runtime improvements; users must reproduce protocol and validate gains on their target datasets.
  Scope: NV-EmbedQA-E5-v5 as first-stage embedder paired with a reranker (reranker required for two-stage metric improvements)
  Evidence: https://arxiv.org/html/2409.07691v1

### Avoid

- **Direct clinical decision-making or unvalidated diagnostic use** — Primary sources do not provide clinical validation, prospective clinical benchmarks, or explicit claims of suitability for clinical decision support; documentation focuses on QA retrieval and enterprise RAG rather than clinical validation.
  Scope: NV-EmbedQA-E5-v5
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/eula.html
- **Assuming specific tokenizer/vocabulary/normalization behavior without verification** — Primary sources do not document tokenizer name/version/vocabulary/normalization rules; tokenization-dependent behaviors cannot be assumed for exact reproducibility.
  Scope: NV-EmbedQA-E5-v5
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer

## Input preparation

### Semantic inputs

- Accepts textual inputs provided as a list of strings representing queries or passages. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5
- Model operates in 'passage' or 'query' modes selectable via input_type parameter; 'passage' intended for indexing and 'query' for querying. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer

### Accepted formats

- Inference API accepts plain text inputs as a list/array of strings for embedding. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### Preprocessing

- Texts longer than the model's maximum context must be chunked or truncated prior to embedding. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5
- Documentation is inconsistent on maximum input length: model reference lists 512 tokens while the inference reference documents up to 8192 tokens for inference; this discrepancy must be resolved by checking the deployed NIM/inference stack. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer
- Exact tokenizer name/version, vocabulary, and normalization are not specified in available primary sources (Evidence gap). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer

### Pre-submit validation

- Validate that inputs are text and provided as a list/array of strings and select the correct input_type ('passage' vs 'query') to avoid large drops in retrieval accuracy. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer
- Confirm and enforce the maximum context length used in deployment because documentation sources conflict (512 vs 8192 tokens). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer

### Task-specific formatting

- No canonical prompt template is provided; inputs are plain text strings and the API exposes an input_type parameter to designate 'passage' or 'query' roles. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer

## Output interpretation

### Outputs

- For each input string the model outputs a 1024-dimensional embedding vector as a list/array of floats. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html
- Primary sources describe outputs as float arrays but do not document API-level dtype (FP32 vs FP16) or explicit L2-normalization at the API level (Evidence gap). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/pdf/2409.07691

### Interpretation

- Embeddings are dense vector representations suitable for measuring semantic similarity and ranking; primary sources do not provide canonical similarity thresholds or calibration guidance. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/abs/2409.07691

### Post-inference validation

- Primary sources do not provide calibration, confidence scores, or canonical threshold values; downstream systems must empirically validate similarity thresholds and reranker behavior for target datasets. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5
- Runtime microbenchmarks reported by the authors (FP16 + TensorRT on H100) require reproducing the same deployment stack to validate latency/throughput claims. Sources: https://arxiv.org/html/2409.07691v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html

## Public benchmarks

### Query embedding latency (runtime performance)

- Dataset/split: runtime microbenchmark (deployment measurement) / not reported
- Metric/value: average query embedding latency (ms) / 5.1 ms (`lower-is-better`)
- Model scope: NV-EmbedQA-E5-v5 converted to FP16 and deployed with TensorRT on a single H100-HBM3-80GB GPU (as reported in the arXiv paper Table 1)
- Conditions: Batch size 1; 20 tokens; FP16; TensorRT; single H100-HBM3-80GB GPU; TensorRT conversion noted by authors
- Source: https://arxiv.org/pdf/2409.07691
- Locator: Table 1
- Caveat: This is a runtime deployment measurement and not a retrieval-quality benchmark on a labeled dataset.
- Caveat: Reproducing this number requires the same hardware and TensorRT FP16 conversion.

### Passage indexing throughput (runtime performance)

- Dataset/split: runtime microbenchmark (deployment measurement) / not reported
- Metric/value: passages indexed per second / 558.4 passages/sec (`higher-is-better`)
- Model scope: NV-EmbedQA-E5-v5 converted to FP16 and deployed with TensorRT on a single H100-HBM3-80GB GPU (as reported in the arXiv paper Table 1)
- Conditions: Batch size 64; passages of 512 tokens; FP16; TensorRT; single H100-HBM3-80GB GPU
- Source: https://arxiv.org/pdf/2409.07691
- Locator: Table 1
- Caveat: Runtime throughput measurement is deployment- and hardware-dependent and not a proxy for retrieval accuracy on public benchmark splits.
- Caveat: Requires identical deployment stack (TensorRT, FP16 conversion, H100) to reproduce.

### Dense retrieval

- Dataset/split: BEIR QA average / BEIR QA evaluation datasets
- Metric/value: NDCG@10 / 0.6083 (`higher-is-better`)
- Model scope: NV-EmbedQA-E5-v5 without reranker
- Conditions: Passages truncated to 512 tokens; top-k 100 retrieval.
- Source: https://arxiv.org/html/2409.07691
- Locator: Table 1
- Caveat: Quality result, not an NVIDIA NIM runtime microbenchmark.

## Comparisons

### aaditya-llama3-openbiollm-8b-vllm — `insufficient-evidence`

- Task: biomedical retrieval / semantic search
- Criteria: No primary-source, checkpoint-scoped model card or benchmark for this Forge candidate is present in the available findings to enable a protocol-matched comparison.
- Rationale: The available primary findings only contain NV-EmbedQA-E5-v5 documentation and the arXiv paper; no official model-card or vendor docs for the candidate were found in the provided evidence set.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/abs/2409.07691

### abhinand-medembed-base-v0-1-vllm-cuda13 — `insufficient-evidence`

- Task: biomedical retrieval / semantic search
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are included in the available evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### abhinand-medembed-large-v0-1-vllm-cuda13 — `insufficient-evidence`

- Task: biomedical retrieval / semantic search
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### abhinand-medembed-small-v0-1-tei-cuda-1-9 — `insufficient-evidence`

- Task: biomedical retrieval / semantic search
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### abhinand-medembed-small-v0-1-vllm-cuda13 — `insufficient-evidence`

- Task: biomedical retrieval / semantic search
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12 — `insufficient-evidence`

- Task: entity / passage embedding for biomedical retrieval
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### ncbi-medcpt-article-encoder-wrapper-cuda12 — `insufficient-evidence`

- Task: article encoding for biomedical retrieval
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### ncbi-medcpt-cross-encoder-wrapper-cuda12 — `insufficient-evidence`

- Task: cross-encoder reranking
- Criteria: Candidate is a different model type (cross-encoder) and no primary-source, protocol-matched benchmarks for the candidate are present in the provided findings.
- Rationale: NV-EmbedQA-E5-v5 is an embedder; the candidate is a cross-encoder reranker and no primary-source checkpoint-scoped comparisons are present in the available evidence.
- Comparison conditions: Different model type and insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/abs/2409.07691

### ncbi-medcpt-query-encoder-tei-cuda-1-9 — `insufficient-evidence`

- Task: query encoding for biomedical retrieval
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### neuml-pubmedbert-base-embeddings-matryoshka-tei-cuda-1-9 — `insufficient-evidence`

- Task: PubMedBERT-based embeddings for biomedical retrieval
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### neuml-pubmedbert-base-embeddings-tei-cuda-1-9 — `insufficient-evidence`

- Task: biomedical embedding generation
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### neuml-pubmedbert-base-embeddings-vllm-cuda13 — `insufficient-evidence`

- Task: biomedical embedding generation
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9 — `insufficient-evidence`

- Task: small biomedical embeddings
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### potsu-potsu-medembed-small-biomedical-matryoshka-v2-vllm-cuda13 — `insufficient-evidence`

- Task: small biomedical embeddings
- Criteria: No official primary-source model card or benchmark for this candidate is present in the provided findings.
- Rationale: No primary-source checkpoint or protocol-matched results for the candidate are available in the provided evidence.
- Comparison conditions: Insufficient primary-source evidence for the candidate within the provided findings.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

## Limitations and safety

### Limitations

- Tokenizer and tokenization specifics (tokenizer name/version, vocabulary, normalization rules) are not reported in the available primary sources (Evidence gap). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer
- Conflicting documentation on maximum input/context length: model reference lists 512 tokens while inference reference lists 8192 tokens; cause of discrepancy is not specified in available primary sources. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer
- Exact checkpoint revision or immutable model-weight hash is not reported in the available primary sources (Evidence gap). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/pdf/2409.07691
- Primary findings do not provide retrieval-quality numeric values (e.g., NDCG@10 per dataset) extracted from Table 1 for NV-EmbedQA-E5-v5; retrieval-quality numbers required by gate must be treated as unverified (Evidence gap). Sources: https://arxiv.org/html/2409.07691v1, https://arxiv.org/pdf/2409.07691
- API-level embedding dtype and any L2-normalization of returned vectors are not documented in the available primary sources (Evidence gap). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://arxiv.org/pdf/2409.07691
- No primary-source guidance on canonical similarity metrics or thresholds for retrieval/reranking is provided in the available findings (Evidence gap). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### Safety

- Primary sources do not specify PHI handling procedures or clinical-use approvals; treat the model as research/engineering infrastructure requiring domain expert review and formal clinical validation before any clinical deployment. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/eula.html
- Users must comply with the model and container licensing terms as documented in the NIM EULA and model references; verify license scope before deployment. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/eula.html, https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

## Related upstream agent skills

### `agent-integration`

The cookbook maps these exact Forge slugs to BioNeMo-style capability names and Serverless shapes. Use it for routing and tool integration, never as model-quality evidence.
- [BioNeMo capability catalog](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/catalog.py)
- [BioNeMo named tool contracts](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/tools.py)
- [BioNeMo agent routing and safety instructions](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/configs/config.yml)

## Primary sources

### NIM reference: nvidia-nv-embedqa-e5-v5

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: First-party NVIDIA technical reference and model-card documentation for NV-EmbedQA-E5-v5 describing model architecture, I/O, and usage.
- Scope: NV-EmbedQA-E5-v5 NIM / model reference
- Supports: model purpose as embedding model for QA retrieval
- Supports: architecture: transformer encoder, fine‑tuned from E5‑Large‑Unsupervised
- Supports: number of transformer layers: 24
- Supports: embedding size: 1024
- Supports: accepted input format: list of strings
- Supports: model-level maximum context length listed as 512 tokens in this reference
- Supports: output described as float arrays

### ArXiv preprint: Enhancing Q&A Text Retrieval with Ranking Models (NV-Retriever)

- URL: https://arxiv.org/abs/2409.07691
- Publisher: arXiv (NVIDIA authors)
- Type: `paper`
- Primary because: Primary research paper reporting benchmark methodology and runtime microbenchmarks referenced in Table 1.
- Scope: Paper-level evaluation including NV-EmbedQA-E5-v5
- Supports: paper identifier and venue information (preprint)
- Supports: description of benchmark study including BEIR QA evaluation datasets

### ArXiv PDF: NV-Retriever paper (runtime and benchmarks)

- URL: https://arxiv.org/pdf/2409.07691
- Publisher: arXiv (NVIDIA authors)
- Type: `paper`
- Primary because: Primary source containing Table 1 runtime microbenchmarks and methodological details referenced by the dossier.
- Scope: Paper Table 1 runtime microbenchmarks and comparative measurements
- Supports: runtime microbenchmark: query embedding latency 5.1 ms (Table 1) for NV-EmbedQA-E5-v5
- Supports: runtime microbenchmark: 558.4 passages/sec passage indexing throughput (Table 1) for NV-EmbedQA-E5-v5
- Supports: statement that BEIR QA datasets (NQ, HotpotQA, FiQA) were used in evaluation (table-level benchmark context)

### ArXiv HTML (v1) of NV-Retriever paper (Table 1 reference)

- URL: https://arxiv.org/html/2409.07691v1
- Publisher: arXiv (NVIDIA authors)
- Type: `paper`
- Primary because: HTML rendering of the arXiv preprint including Table 1 locators referenced for runtime and benchmark descriptions.
- Scope: Paper Table 1 and benchmark descriptions
- Supports: mentions BEIR QA datasets used (NQ, HotpotQA, FiQA) in benchmark evaluation
- Supports: reports runtime microbenchmarks (5.1 ms latency, 558.4 passages/sec throughput) in Table 1

### NeMo Retriever Text Embedding support matrix and model card excerpts

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Official support matrix and model-card information describing supported hardware, embedding dimensionality, and reiterating model card maximum context length.
- Scope: NV-EmbedQA-E5-v5 support matrix / model card excerpts
- Supports: support matrix listing optimized configurations and supported compute capabilities
- Supports: embedding dimension 1024
- Supports: model card for nvidia/nv-embedqa-e5-v5 specifies a maximum context length of 512 tokens

### NIM inference reference: nvidia-nv-embedqa-e5-v5 infer

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5-infer
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Official inference API documentation describing input_type behavior and an inference input token limit that conflicts with the model-card context length.
- Scope: NV-EmbedQA-E5-v5 inference reference (NIM)
- Supports: documented inference input_type parameter (passage vs query)
- Supports: stated inference input token limit up to 8192 tokens
- Supports: warning that incorrect input_type can cause large drops in retrieval accuracy

### NeMo Retriever Text Embedding performance documentation

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Official performance measurements and detailed runtime-oriented tables for NeMo Retriever Text Embedding NIM deployments.
- Scope: NV-EmbedQA-E5-v5 performance measurements (NIM)
- Supports: detailed runtime performance table (latency/throughput) for various batch sizes and token lengths in NIM deployments
- Supports: measurements for passage inputs of 512 tokens at batch sizes and concurrency levels

### NeMo Retriever Text Embedding NIM EULA and licensing

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/eula.html
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Official licensing and EULA document governing NIM containers and model usage.
- Scope: NIM container license and model license governance
- Supports: NIM container governed by NVIDIA Software License Agreement and Product Specific Terms
- Supports: model distributed under NVIDIA AI Foundation Models Community License Agreement and additionally under MIT as stated for the model artifact

### NV-Retriever: Improving text embedding models with effective hard-negative mining

- URL: https://arxiv.org/html/2409.07691
- Publisher: NVIDIA
- Type: `paper`
- Primary because: A human reviewer opened this primary source and verified the structured benchmark rows and exact locator recorded in research/manual-review-hints.json.
- Scope: nvidia-nv-embedqa-e5
- Supports: Manually verified exact-checkpoint benchmark evidence

## Evidence gaps

- Retrieval-quality numeric values (NDCG@10) for NV-EmbedQA-E5-v5 (BEIR QA average 0.6083; NQ 0.6380; HotpotQA 0.7160; FiQA 0.4710) could not be verified in the provided research findings; the available arXiv/html/pdf facts indicate BEIR QA datasets were used but the table-level per-dataset numeric entries required by the brief are not present in the supplied findings.
- Exact checkpoint revision identifier or immutable model-weight hash for NV-EmbedQA-E5-v5 is not reported in the provided primary sources.
- Tokenizer name, tokenizer version, tokenizer vocabulary, and normalization rules are not specified in the available primary sources.
- API-level embedding dtype and any explicit L2-normalization of returned vectors are not documented in the available primary sources.
- Official primary-source model-card or vendor documentation for each Forge peer candidate listed in comparisons is not present in the provided findings; therefore protocol-matched comparisons are not possible from the available evidence.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nv-embedqa-e5-v5-pb6/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nv-embedqa-e5-v5-pb6/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://arxiv.org/html/2409.07691: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://arxiv.org/html/2409.07691#Table 1:NDCG@10: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
