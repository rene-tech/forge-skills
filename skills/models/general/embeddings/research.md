# Embeddings model selection

- Category: `general`
- Group: `embeddings`
- Independent audit: `revised`
- Researched: `2026-07-23T21:39:35.294188+00:00`

Selection dossier for dense text (and limited multimodal) embedding models in the Forge category general--embeddings. Task: given the canonical set of exact Forge embedding candidate slugs in scope, map use-case predicates (language coverage, input length, retrieval objective, cost/footprint constraints, instruction conditioning, and license/safety boundaries) to a preferred exact Forge slug or to insufficient-evidence when authoritative primary sources in the supplied research findings do not support a clear preference. Scope: selection among the canonical Forge slugs enumerated in the research brief; only claims that can be tied to the supplied primary research findings are asserted. Out of scope: runtime latency/throughput targets beyond what is stated in the supplied findings, and any numeric benchmark or model property not present in the supplied research findings (these are documented as Evidence gap: entries).

## Questions to answer before selecting

- Which languages must be supported (single language vs multilingual; which specific languages are required)?
- What is the maximum input length required (short passages, up to 256–512 tokens, long documents up to multiple thousands of tokens, or very long contexts up to 32K)?
- Which retrieval objective is primary (semantic search, RAG/document retrieval, sentence similarity/STS, clustering, code retrieval, reranking, or QA retrieval)?
- What is the acceptable model footprint (parameter scale or cost sensitivity) and is a small‑model solution required?
- Is instruction‑conditioned embedding behavior required (explicit canonical prompts) or are generic embeddings acceptable?
- What license and safety constraints apply (permissive MIT/Apache vs vendor-specific licenses; HCLS/PHI constraints)?
- Is support for mixture-of-experts (MoE) or Matryoshka/flexible embedding dimensions required?
- Which vector dimensionality, pooling/normalization conventions, and dtype (float32/float16) must be guaranteed for compatibility with downstream indexing?

## Comparability rules

- Compare results only when dataset name and split are identical and when tokenization, text normalization, chunking, pooling, and embedding normalization are matched across candidates (protocol parity required).
- Do not transfer or assume equivalence across different serving wrappers (TEI vs vLLM vs NIM) unless a supplied primary source in the research findings explicitly documents identical embedding behavior for those wrappers; otherwise treat wrapper differences as evidence gaps.
- When a benchmark result requires a downstream head, service, or additional fine‑tuning, record that dependency and do not attribute the downstream result to the plain embedding output unless the supplied primary research sources explicitly document an embedding-only evaluation.
- If a candidate lacks explicit primary documentation for an attribute required for comparison (embedding dimension, pooling, canonical prompt, or max sequence length), mark that attribute as an evidence gap and do not use that attribute to declare a winner.

## Conditional routing

### Prefer `ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9` when Use-case: short/low-cost English semantic search or sentence similarity where compact vectors and a small-model footprint are priorities.

- Why: The IBM Hugging Face model card reports this checkpoint as a 47 million‑parameter dense biencoder producing 384‑dimensional vectors and supporting context up to 8192 tokens in the supplied primary source.
- Alternative: sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9
- Alternative: baai-bge-small-en-v1-5-tei-cuda-1-9
- Alternative: mixedbread-ai-mxbai-embed-large-v1-tei-cuda-1-9
- Alternative: snowflake-arctic-embed-m-v2-0-tei-cuda-1-9
- Evidence: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2

### Prefer `intfloat-multilingual-e5-large-instruct-tei-cuda-1-9` when Use-case: multilingual instruction‑conditioned retrieval where an instruction‑tuned variant is preferred.

- Why: The intfloat multilingual-e5-large-instruct Hugging Face model card in the supplied findings states the model was evaluated on MTEB, is initialized from xlm-roberta-large, and that long texts are truncated to at most 512 tokens per the supplied primary source.
- Alternative: nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9
- Alternative: baai-bge-m3-tei-cuda-1-9
- Alternative: qwen-qwen3-embedding-4b-tei-cuda-1-9
- Alternative: qwen-qwen3-embedding-8b-tei-cuda-1-9
- Evidence: https://huggingface.co/intfloat/multilingual-e5-large-instruct

### Prefer `mixedbread-ai-mxbai-embed-large-v1-tei-cuda-1-9` when Use-case: general-purpose high‑quality retrieval and clustering where documented MTEB-style performance and higher embedding dimension are desired and model footprint is less constrained.

- Why: The mixedbread-ai mxbai-embed-large-v1 Hugging Face primary page in the supplied findings reports the model and documents feature-extraction pipeline behavior and an MTEB-style performance claim in the supplied primary source facts.
- Alternative: baai-bge-base-en-v1-5-tei-cuda-1-9
- Alternative: nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9
- Alternative: snowflake-arctic-embed-l-v2-0-tei-cuda-1-9
- Evidence: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Prefer `nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9` when Use-case: prefer mixture‑of‑experts (MoE) architectures for specialization or routing benefits in retrieval.

- Why: The nomic‑embed‑text‑v2‑moe Hugging Face primary page in the supplied findings describes the model as a multilingual Mixture‑of‑Experts text embedding model and supplies parameter/embedding-dimension and benchmark facts in the supplied primary source.
- Alternative: baai-bge-m3-tei-cuda-1-9
- Alternative: mixedbread-ai-mxbai-embed-large-v1-tei-cuda-1-9
- Alternative: intfloat-multilingual-e5-large-instruct-tei-cuda-1-9
- Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe

### Prefer `insufficient-evidence` when Use-case: candidates provided as NVIDIA NIM-wrapped artifacts where wrapper-level equivalence to an unchanged upstream checkpoint must be proven before preferring a specific NIM variant.

- Why: The supplied primary NIM reference pages document capabilities and configuration for the NVIDIA-wrapped models but do not, across all listed NIM slugs in scope, provide uniform documented proof of unchanged upstream‑checkpoint identity or wrapper‑level pooling/normalization equivalence in the supplied findings; therefore the dossier cannot prefer a specific NIM variant without that wrapper‑to‑upstream identity evidence.
- Alternative: nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim
- Alternative: nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim
- Alternative: nvidia-llama-3-2-nv-embedqa-1b-v2-nim
- Alternative: nvidia-llama-nemotron-embed-1b-v2-nim
- Alternative: nvidia-nvclip-nim
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip

### Prefer `insufficient-evidence` when Use-case: when exact TEI vs vLLM wrapper behavior (pooling, normalization, dtype) needs to be known for a particular slug served under a vLLM wrapper but the supplied primary sources do not document wrapper-specific equivalence.

- Why: The Hugging Face primary pages for the upstream checkpoints are present in the supplied findings but the supplied primary findings do not provide wrapper-specific TEI vs vLLM pooling/normalization/dtype equivalence statements for the vLLM wrapper variants listed in scope.
- Alternative: alibaba-nlp-gte-modernbert-base-tei-cuda-1-9
- Alternative: alibaba-nlp-gte-modernbert-base-vllm-cuda13
- Alternative: baai-bge-base-en-v1-5-vllm-cuda13
- Alternative: baai-bge-small-en-v1-5-vllm-cuda13
- Alternative: qwen-qwen3-embedding-4b-vllm-cuda13
- Alternative: qwen-qwen3-embedding-8b-vllm-cuda13
- Alternative: qwen-qwen3-embedding-0-6b-vllm-cuda13
- Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5, https://huggingface.co/BAAI/bge-small-en-v1.5, https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Alibaba-NLP/gte-modernbert-base

### Prefer `qwen-qwen3-embedding-4b-tei-cuda-1-9` when Use-case: very long-context retrieval or document‑level retrieval requiring large maximum sequence lengths.

- Why: The Qwen3 Embedding 4B Hugging Face primary page in the supplied findings documents support for 32K token sequences in the supplied primary source.
- Alternative: qwen-qwen3-embedding-8b-tei-cuda-1-9
- Alternative: ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9
- Alternative: baai-bge-large-en-v1-5-tei-cuda-1-9
- Alternative: nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim
- Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B

### Prefer `alibaba-nlp-gte-modernbert-base-tei-cuda-1-9` when Use-case: general short-to-mid context English retrieval where a documented mid-sized parameter / mid-dimension embedding model is preferred for balanced capacity and throughput.

- Why: The Alibaba gte-modernbert-base Hugging Face primary page in the supplied findings reports parameter scale, embedding dimension, TEI deployment examples, and reports pooling set to "cls" and normalization true in a TEI example in the supplied primary source facts.
- Alternative: qwen-qwen3-embedding-0-6b-tei-cuda-1-9
- Alternative: sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base

### Prefer `sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9` when Use-case: extremely compact sentence-level embeddings where 384-dim vectors are required for dense retrieval and similarity.

- Why: The sentence-transformers/all-MiniLM-L6-v2 Hugging Face model card in the supplied findings states the model maps sentences and paragraphs to 384‑dimensional dense vectors and notes default truncation behavior in the supplied primary source facts.
- Alternative: qwen-qwen3-embedding-0-6b-tei-cuda-1-9
- Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### Prefer `baai-bge-base-en-v1-5-tei-cuda-1-9` when Use-case: select a BGE variant for English-heavy workloads where base/large dimension and aggregated MTEB-style scores are a decision factor.

- Why: The BAAI bge-base-en-v1.5 Hugging Face primary page in the supplied findings reports embedding dimension 768, a maximum sequence length of 512 tokens, and aggregated MTEB scores in the supplied primary source facts.
- Alternative: baai-bge-large-en-v1-5-tei-cuda-1-9
- Alternative: baai-bge-small-en-v1-5-tei-cuda-1-9
- Alternative: mixedbread-ai-mxbai-embed-large-v1-tei-cuda-1-9
- Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5, https://huggingface.co/BAAI/bge-large-en-v1.5

## Benchmark taxonomy

### Semantic search / passage retrieval

- Datasets: BEIR, MTEB
- Metrics: Recall@k, MRR@k, nDCG@k
- Compare only when: Identical dataset name and split
- Compare only when: Matched tokenization and text normalization
- Compare only when: Matched chunking and document boundary definitions
- Compare only when: Matched pooling and embedding normalization

### Sentence similarity / STS

- Datasets: STS-B, MTEB
- Metrics: Pearson correlation, Spearman correlation, Cosine similarity (with/without L2 normalization)
- Compare only when: Identical sentence pair inputs and splits
- Compare only when: Matched tokenization and truncation rules
- Compare only when: Matched pooling and normalization

### Multilingual retrieval

- Datasets: MIRACL, MTEB multilingual subsets
- Metrics: MRR@k, Recall@k, Average MTEB subtask scores
- Compare only when: Same language coverage and dataset splits
- Compare only when: Document-level pooling and normalization matched

## Primary sources

- [IBM granite-embedding-small-english-r2 (Hugging Face)](https://huggingface.co/ibm-granite/granite-embedding-small-english-r2) — IBM; supports ibm-granite/granite-embedding-small-english-r2 is a 47 million‑parameter dense biencoder embedding model., granite-embedding-small-english-r2 produces embedding vectors of size 384., granite-embedding-small-english-r2 supports a context length of up to 8192 tokens., In MTEB evaluation, granite-embedding-small-english-r2 achieved an average score of 55.6.
- [Intfloat multilingual-e5-large-instruct (Hugging Face)](https://huggingface.co/intfloat/multilingual-e5-large-instruct) — Intfloat; supports The intfloat/multilingual-e5-large-instruct model supports 100 languages from xlm-roberta per the supplied primary source facts., The intfloat/multilingual-e5-large-instruct model was evaluated on the MTEB benchmark per the supplied primary source facts., Long texts are truncated to at most 512 tokens when using intfloat/multilingual-e5-large-instruct per the supplied primary source facts.
- [mixedbread-ai mxbai-embed-large-v1 (Hugging Face)](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) — Mixedbread AI; supports mixedbread-ai/mxbai-embed-large-v1 provides a feature‑extraction pipeline via Transformers.js with dtype options fp32, fp16, and q8., The mxbai-embed-large-v1 model can generate sentence embeddings for arbitrary input sentences per the supplied primary source facts.
- [nomic-embed-text-v2-moe (Hugging Face)](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) — Nomic AI; supports nomic-ai/nomic-embed-text-v2-moe is a multilingual Mixture‑of‑Experts text embedding model per the supplied primary source facts., The nomic‑embed‑text‑v2‑moe model is described in the paper "Training Sparse Mixture Of Experts Text Embedding Models" per the supplied primary source facts.
- [NVIDIA NeMo Retriever Embedding 300M v1 (NIM reference)](https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1) — NVIDIA; supports The NVIDIA Llama 3.2 NeMo Retriever Embedding 300M v1 model is optimized for multilingual and cross‑lingual QA retrieval per the supplied primary source facts., The Llama 3.2 NeMo Retriever Embedding 300M v1 model supports documents up to 8192 tokens per the supplied primary source facts., The Llama 3.2 NeMo Retriever Embedding 300M v1 model has 9 transformer layers and an embedding size of 2048 per the supplied primary source facts.
- [NVIDIA NeMo Retriever Embedding 300M v2 (NIM reference)](https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2) — NVIDIA; supports The Llama 3.2 NeMo Retriever Embedding 300M v2 model supports up to 8192 tokens and the same 26 languages as v1 per the supplied primary source facts., The Llama 3.2 NeMo Retriever Embedding 300M v2 model allows configurable embedding dimensions of 384, 512, 768, 1024, or 2048 per the supplied primary source facts.
- [NVIDIA nv-embedqa-1b-v2 (NIM reference)](https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v2) — NVIDIA; supports The NVIDIA Llama 3.2‑nv‑embedqa‑1b‑v2 model is optimized for multilingual QA retrieval with support for up to 8192 tokens and dynamic Matryoshka embedding sizes per the supplied primary source facts., The Llama 3.2‑nv‑embedqa‑1b‑v2 model has a maximum embedding dimension of 2048, configurable via Matryoshka representation per the supplied primary source facts.
- [NVIDIA Llama Nemotron Embed 1b v2 (NIM reference)](https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2) — NVIDIA; supports The NVIDIA Llama Nemotron‑Embed‑1b‑v2 model is optimized for multilingual QA retrieval with up to 8192 token context length and dynamic Matryoshka embeddings per the supplied primary source facts., The Llama Nemotron‑Embed‑1b‑v2 model has a transformer architecture fine‑tuned from Llama 3.2 per the supplied primary source facts.
- [NV‑CLIP container listing (NGC)](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip) — NVIDIA (NGC catalog); supports NV‑CLIP is a multimodal embeddings model per the supplied primary source facts., NV‑CLIP outputs embeddings of size 1024 for the ViT‑H variant per the supplied primary source facts.
- [Qwen3 Embedding 4B (Hugging Face)](https://huggingface.co/Qwen/Qwen3-Embedding-4B) — Qwen; supports Qwen3-Embedding-4B provides text embedding functionality and documents a context length of 32K tokens per the supplied primary source facts.
- [Alibaba gte-modernbert-base (Hugging Face)](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) — Alibaba-NLP; supports Alibaba-NLP/gte-modernbert-base is built upon modernBERT encoder-only foundation models per the supplied primary source facts., When deployed with TEI, the model is accessible via an OpenAI‑compatible /v1/embeddings endpoint and the supplied TEI example shows pooling set to "cls" and normalization set to true per the supplied primary source facts.
- [all-MiniLM-L6-v2 (Hugging Face)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — sentence-transformers; supports The all-MiniLM-L6-v2 model maps sentences and paragraphs to 384‑dimensional dense vectors per the supplied primary source facts., When using all-MiniLM-L6-v2, input text longer than 256 word pieces is truncated by default per the supplied primary source facts.
- [BAAI bge-base-en-v1.5 (Hugging Face)](https://huggingface.co/BAAI/bge-base-en-v1.5) — BAAI; supports BAAI/bge-base-en-v1.5 has an embedding dimension of 768 per the supplied primary source facts., BAAI/bge-base-en-v1.5 supports a maximum sequence length of 512 tokens per the supplied primary source facts., BAAI/bge-base-en-v1.5 reports aggregated MTEB-style scores in the supplied primary source facts.
- [BAAI bge-large-en-v1.5 (Hugging Face)](https://huggingface.co/BAAI/bge-large-en-v1.5) — BAAI; supports BAAI/bge-large-en-v1.5 has an embedding dimension of 1024 per the supplied primary source facts., BAAI/bge-large-en-v1.5 supports a maximum sequence length of 512 tokens per the supplied primary source facts.
- [BAAI bge-small-en-v1.5 (Hugging Face)](https://huggingface.co/BAAI/bge-small-en-v1.5) — BAAI; supports BAAI/bge-small-en-v1.5 has an embedding dimension of 384 per the supplied primary source facts., BAAI/bge-small-en-v1.5 supports a maximum sequence length of 512 tokens per the supplied primary source facts.
- [BAAI bge-m3 (Hugging Face)](https://huggingface.co/BAAI/bge-m3) — BAAI; supports The BGE M3 paper and model are present in the supplied primary findings per the supplied primary source facts.
- [Qwen3 Embedding 0.6B (Hugging Face)](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) — Qwen; supports Qwen3‑Embedding series includes 0.6 B, 4 B, and 8 B parameter versions per the supplied primary source facts., Qwen3‑Embedding supports 119 languages per the supplied primary source facts.
- [Qwen3 Embedding 8B (Hugging Face)](https://huggingface.co/Qwen/Qwen3-Embedding-8B) — Qwen; supports Qwen3-Embedding-8B has 8 B parameters and supports 32K token sequences per the supplied primary source facts.
- [Snowflake arctic-embed-l-v2.0 (Hugging Face)](https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0) — Snowflake; supports Snowflake arctic-embed-l-v2.0 is released under the Apache 2.0 license per the supplied primary source facts., Snowflake arctic-embed-l-v2.0 claims multilingual retrieval performance and reports MTEB/BEIR/MIRACL-style results in the supplied primary source facts.
- [Snowflake arctic-embed-m-v2.0 (Hugging Face)](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0) — Snowflake; supports Snowflake arctic-embed-m-v2.0 has embedding-dimension facts and reports BEIR/MIRACL-style results in the supplied primary source facts.
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/nvclip) — build.nvidia.com; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Canonical primary dataset pages for BEIR, MTEB, STS-B, and MIRACL (dataset‑split level canonical tables or checkpoint‑row level entries) were not supplied in the research findings; the dossier cannot verify dataset‑split‑level benchmark rows from canonical dataset pages.
- Evidence gap: The supplied primary findings do not consistently document wrapper-specific pooling methods (CLS vs mean vs other) or default L2-normalization and dtype for TEI vs vLLM wrapper variants; wrapper-level pooling/normalization/dtype statements are missing for many vLLM/TEI variants in the supplied findings.
- Evidence gap: For NVIDIA NIM wrapper slugs, while NIM reference pages are present in the supplied findings, the supplied findings do not consistently prove identity between the NIM-wrapped serving artifact and a named unchanged upstream checkpoint for all NIM slugs; upstream-checkpoint equivalence evidence is incomplete for some NIM variants.
- Evidence gap: The supplied primary findings do not provide canonical prompt template text for instruction-conditioned variants (for example, multilingual-e5-large-instruct) beyond statements that instructions are used; no explicit canonical prompt templates are present in the supplied primary sources.
- Evidence gap: The supplied primary findings do not consistently state the default embedding output dtype (float32 vs float16) for specific wrapper variants (TEI/vLLM/NIM); dtype for wrapper variants is therefore unknown from the supplied findings.
- Evidence gap: Where benchmark rows were asserted in draft material, the supplied primary findings do not include canonical dataset‑split‑level tables or explicit checkpoint‑scoped benchmark rows for every asserted value; those specific benchmark rows could not be verified and are therefore omitted.
- Evidence gap: Safety, HCLS/PHI restrictions, or license-provenance details for some NIM-wrapped or mirrored checkpoints are not fully documented in the supplied primary findings; license and safety provenance for certain wrapped artifacts is therefore incomplete.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-large-en-v1-5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/llama-nemotron-embed-vl-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/qwen/qwen3-embedding-0-6b-tei-cuda-1-9 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-small-en-v1.5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-3_2-nv-embedqa-1b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/nvclip: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
