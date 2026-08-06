# Biomedical Retrieval model selection

- Category: `healthcare`
- Group: `biomedical-retrieval`
- Independent audit: `revised`
- Researched: `2026-07-23T22:36:52.490991+00:00`

Biomedical-retrieval in this corrected group is limited to checkpoint-scoped tasks directly evidenced in the provided primary findings: biomedical text embedding for retrieval or semantic search; asymmetric query/article dense retrieval when a paired query encoder and article encoder are explicitly documented; cross-encoder article ranking given a query when explicitly documented; biomedical entity representation and synonym-focused entity linking when explicitly documented; and retrieval-plus-generation pipelines only insofar as a listed model is evidenced as a generative biomedical instruction model rather than a native embedding retriever. Outside scope are unsupported claims about exact Forge packaging behavior, protocol-incomparable benchmark rankings across different task families, and any claim that a generative model is itself a native embedding retriever without primary evidence.

## Questions to answer before selecting

- Do you need embedding vectors, pairwise ranking scores, or generated text?
- Is your task symmetric embedding retrieval/semantic search, asymmetric query/article retrieval, cross-encoder reranking, biomedical entity linking/entity similarity, or retrieval-plus-generation?
- If doing retrieval, are queries short biomedical questions/search queries while documents are PubMed-style articles requiring separate encoders?
- Do you need a second-stage reranker that scores a query jointly with a candidate article?
- Are you retrieving biomedical documents or representing biomedical entities/synonyms?
- Do you require a model card that explicitly documents Matryoshka or dynamic embedding dimensions?
- Do you need a checkpoint with direct biomedical retrieval evidence rather than only general semantic embedding intent?
- Is vendor-hosted commercial-use readiness a requirement?
- Can you tolerate unresolved evidence about exact Forge TEI/vLLM/wrapper packaging behavior versus upstream checkpoint behavior?
- Do you need a generation model for answer synthesis after retrieval rather than a retriever itself?

## Comparability rules

- Only compare models within the same task family directly evidenced in source: embedding retrieval/semantic search, asymmetric query/article retrieval, cross-encoder ranking, entity representation/entity linking, or generation for downstream synthesis.
- Do not compare first-stage embedding retrievers with ncbi-medcpt-cross-encoder-wrapper-cuda12 unless the upstream candidate pool and reranking protocol are fixed.
- For MedCPT asymmetric retrieval, preserve the documented pairing of ncbi-medcpt-query-encoder-tei-cuda-1-9 for queries and ncbi-medcpt-article-encoder-wrapper-cuda12 for articles.
- Do not compare cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12 entity-linking evidence directly against document-retrieval evidence from embedding retrievers.
- Only compare benchmark values when the exact dataset name, metric, and conditions are stated in the primary source; otherwise treat the benchmark as unresolved.
- Treat Forge TEI, vLLM, and wrapper variants as packaging around an upstream checkpoint only where the expected scope and sourceUrl identify the upstream checkpoint; do not infer quality differences between packaging variants without primary evidence.
- Do not transfer family-level claims to a different exact checkpoint when the findings only support another variant or repository-wide statement.
- Do not compare Matryoshka operating points unless the source explicitly documents the supported dimensions for that exact upstream checkpoint.
- Do not infer pooling, truncation, normalization, or maximum input length from naming conventions alone; unresolved operational semantics remain evidence gaps.
- Do not treat aaditya-llama3-openbiollm-8b-vllm as a native embedding retriever because the findings only evidence it as a biomedical instruction-tuned language model with benchmark tables, not as an embedding model.

## Conditional routing

### Prefer `ncbi-medcpt-query-encoder-tei-cuda-1-9` when You need asymmetric biomedical first-stage retrieval with separate encoders for short queries and PubMed-style articles.

- Why: The primary findings state that the MedCPT Query Encoder generates embeddings for biomedical queries and was pre-trained on the same 255 million query-article pairs as the article encoder, while the article encoder is documented for dense retrieval over biomedical texts and PubMed search-log pretraining. This is the clearest checkpoint-scoped evidence in the candidate set for an asymmetric query/article retrieval setup.
- Alternative: ncbi-medcpt-article-encoder-wrapper-cuda12
- Alternative: abhinand-medembed-base-v0-1-vllm-cuda13
- Alternative: neuml-pubmedbert-base-embeddings-tei-cuda-1-9
- Evidence: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Article-Encoder

### Prefer `ncbi-medcpt-article-encoder-wrapper-cuda12` when You need the document-side encoder for the documented MedCPT asymmetric retrieval pair over biomedical articles.

- Why: The MedCPT Article Encoder model card is directly evidenced as generating embeddings of biomedical texts for semantic search and dense retrieval, and it is documented as pre-trained on 255 million query-article pairs from PubMed search logs.
- Alternative: ncbi-medcpt-query-encoder-tei-cuda-1-9
- Alternative: abhinand-medembed-large-v0-1-vllm-cuda13
- Alternative: neuml-pubmedbert-base-embeddings-vllm-cuda13
- Evidence: https://huggingface.co/ncbi/MedCPT-Article-Encoder

### Prefer `ncbi-medcpt-cross-encoder-wrapper-cuda12` when You need a native pairwise reranker for ranking articles given a query.

- Why: The MedCPT Cross Encoder primary source states that it is used for ranking articles given a query. That is direct evidence for a cross-encoder reranking role rather than first-stage embedding retrieval.
- Alternative: ncbi-medcpt-query-encoder-tei-cuda-1-9
- Alternative: ncbi-medcpt-article-encoder-wrapper-cuda12
- Alternative: abhinand-medembed-small-v0-1-vllm-cuda13
- Evidence: https://huggingface.co/ncbi/MedCPT-Cross-Encoder

### Prefer `cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12` when You need biomedical entity representation or synonym-focused medical entity linking rather than document retrieval.

- Why: The SapBERT source states that SapBERT self-aligns the representation space of biomedical entities, leverages UMLS, and is designed for medical entity linking tasks, especially modeling synonymy between entities. That evidence is task-specific and should not be widened to general document retrieval superiority.
- Alternative: neuml-pubmedbert-base-embeddings-tei-cuda-1-9
- Alternative: abhinand-medembed-small-v0-1-tei-cuda-1-9
- Alternative: ncbi-medcpt-query-encoder-tei-cuda-1-9
- Evidence: https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext

### Prefer `neuml-pubmedbert-base-embeddings-matryoshka-tei-cuda-1-9` when You require a model card that explicitly documents dynamic Matryoshka embedding dimensions.

- Why: The NeuML Matryoshka model card directly documents dynamic embedding dimensionalities of 64, 128, 256, 384, 512, and 768. This is stronger primary evidence for dimension-flexible embeddings than is available for the other in-scope Matryoshka-labeled candidates.
- Alternative: neuml-pubmedbert-base-embeddings-vllm-cuda13
- Alternative: potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9
- Alternative: potsu-potsu-medembed-small-biomedical-matryoshka-v2-vllm-cuda13
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka

### Prefer `neuml-pubmedbert-base-embeddings-tei-cuda-1-9` when You need a biomedical sentence/paragraph embedding model with direct primary-source evidence for a 768-dimensional dense vector space.

- Why: The NeuML pubmedbert-base-embeddings source states that the model maps sentences and paragraphs to a 768-dimensional dense vector space and reports evaluation on PubMed QA, PubMed Subset, and PubMed Summary with an average score of 95.62. This supports biomedical embedding use, while exact protocol comparability to other retrieval models remains limited.
- Alternative: neuml-pubmedbert-base-embeddings-vllm-cuda13
- Alternative: abhinand-medembed-base-v0-1-vllm-cuda13
- Alternative: abhinand-medembed-large-v0-1-vllm-cuda13
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings

### Prefer `abhinand-medembed-small-v0-1-tei-cuda-1-9` when You want a medical/clinical embedding model from the MedEmbed family at the small checkpoint scale.

- Why: The MedEmbed-small-v0.1 primary source states that it is a specialized embedding model fine-tuned for medical and clinical data for information retrieval, question answering, and semantic search. The evidence supports intended task family, but not exact head-to-head superiority over the rest of the group under a single aligned protocol.
- Alternative: abhinand-medembed-small-v0-1-vllm-cuda13
- Alternative: abhinand-medembed-base-v0-1-vllm-cuda13
- Alternative: potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9
- Evidence: https://huggingface.co/abhinand/MedEmbed-small-v0.1

### Prefer `abhinand-medembed-base-v0-1-vllm-cuda13` when You want a medical/clinical embedding model from the MedEmbed family at the base checkpoint scale.

- Why: The MedEmbed-base-v0.1 primary source states that it is a specialized embedding model fine-tuned for medical and clinical data to improve information retrieval, question answering, and semantic search, and that performance metrics such as nDCG, MAP, Recall, Precision, and MRR are documented in the model's full documentation. The findings, however, do not provide protocol-complete numeric rows here for cross-model routing.
- Alternative: abhinand-medembed-small-v0-1-vllm-cuda13
- Alternative: abhinand-medembed-large-v0-1-vllm-cuda13
- Alternative: nvidia-nv-embedqa-e5-v5
- Evidence: https://huggingface.co/abhinand/MedEmbed-base-v0.1

### Prefer `abhinand-medembed-large-v0-1-vllm-cuda13` when You want a medical/clinical embedding model from the MedEmbed family at the large checkpoint scale.

- Why: The MedEmbed-large-v0.1 primary source states that it is a specialized embedding model fine-tuned for medical and clinical data for information retrieval, question answering, and semantic search. The source supports intended use at the large variant, but the findings do not provide a protocol-aligned basis to declare it globally best among all candidates.
- Alternative: abhinand-medembed-base-v0-1-vllm-cuda13
- Alternative: neuml-pubmedbert-base-embeddings-tei-cuda-1-9
- Alternative: nvidia-nv-embedqa-e5-v5
- Evidence: https://huggingface.co/abhinand/MedEmbed-large-v0.1

### Prefer `nvidia-nv-embedqa-e5-v5` when You need a vendor-served embedding model whose primary source explicitly states commercial-use readiness and gives architecture-level details.

- Why: The NVIDIA source states that the Retrieval QA E5 Embedding Model is ready for commercial use and is a transformer encoder fine-tuned version of E5-Large-Unsupervised with 24 layers and embedding size 1024. The findings support vendor-documented serving identity and intended retrieval use, but do not provide protocol-aligned biomedical head-to-head comparisons against the rest of the group.
- Alternative: abhinand-medembed-base-v0-1-vllm-cuda13
- Alternative: neuml-pubmedbert-base-embeddings-vllm-cuda13
- Alternative: abhinand-medembed-large-v0-1-vllm-cuda13
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5

### Prefer `aaditya-llama3-openbiollm-8b-vllm` when You are building retrieval-plus-generation and need biomedical answer synthesis after retrieval, not a native embedding retriever.

- Why: The primary findings for aaditya/Llama3-OpenBioLLM-8B show benchmark tables on biomedical datasets and describe it as a biomedical instruction-tuned language model. The provided findings do not establish it as an embedding retriever, so it should be routed only to generation roles in a retrieval pipeline.
- Alternative: ncbi-medcpt-cross-encoder-wrapper-cuda12
- Alternative: neuml-pubmedbert-base-embeddings-tei-cuda-1-9
- Alternative: abhinand-medembed-small-v0-1-tei-cuda-1-9
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### Prefer `insufficient-evidence` when You specifically need to choose between the two Forge packaging variants of the same NeuML upstream checkpoint.

- Why: The findings identify TEI and vLLM Forge variants for the same upstream NeuML checkpoint through expected scope, but provide no primary evidence that packaging changes retrieval quality, input handling, or output semantics for this exact checkpoint.
- Alternative: neuml-pubmedbert-base-embeddings-tei-cuda-1-9
- Alternative: neuml-pubmedbert-base-embeddings-vllm-cuda13
- Evidence: https://huggingface.co/NeuML/pubmedbert-base-embeddings

## Benchmark taxonomy

### Bi-encoder dense retrieval over biomedical text

- Datasets: MedicalQARetrieval, NFCorpus, TRECCOVID
- Metrics: nDCG (higher is better), MAP (higher is better), Recall (higher is better), Precision (higher is better), MRR (higher is better)
- Compare only when: Only compare exact checkpoints with benchmark values directly stated in primary sources.
- Compare only when: Do not compare models if the source omits the exact split, ranking depth, or evaluation protocol.
- Compare only when: Do not mix symmetric embedding retrieval with asymmetric query/article retrieval results.
- Compare only when: Treat repository-wide benchmark statements as family evidence unless the exact checkpoint is explicitly named.

### Asymmetric query/article dense retrieval

- Datasets: Zero-shot biomedical information-retrieval datasets (dataset names not specified in the findings)
- Metrics: State-of-the-art retrieval performance claims only where exact metrics are stated by the source, MRR (higher is better), nDCG (higher is better), MAP (higher is better), Recall (higher is better)
- Compare only when: Use ncbi-medcpt-query-encoder-tei-cuda-1-9 on the query side and ncbi-medcpt-article-encoder-wrapper-cuda12 on the article side.
- Compare only when: Restrict comparisons to PubMed-style query/article retrieval when the source evidence is MedCPT-specific.
- Compare only when: Do not compare to symmetric embedding models as if the protocol were identical.
- Compare only when: If exact datasets or metric tables are not given in the findings, keep the benchmark at taxonomy level only.

### Cross-encoder reranking

- Datasets: Query-article ranking tasks (dataset names not specified in the findings)
- Metrics: Ranking score or relevance score for a query-article pair, MRR (higher is better), nDCG (higher is better)
- Compare only when: Fix the candidate generation method and candidate pool before comparing reranking quality.
- Compare only when: Keep exact query-article pair formatting consistent.
- Compare only when: Do not compare cross-encoder results directly to first-stage retrieval results without the same candidate pool.
- Compare only when: Retain only benchmark claims explicitly documented for the cross-encoder; otherwise record an evidence gap.

### Biomedical entity linking or entity similarity

- Datasets: UMLS
- Metrics: Entity linking performance (higher is better), Entity synonym similarity or retrieval quality (higher is better)
- Compare only when: Only compare models explicitly evidenced for entity representation or medical entity linking.
- Compare only when: Do not compare entity-linking evidence directly against document-retrieval benchmark rows.
- Compare only when: Preserve the ontology-backed setup documented for SapBERT.
- Compare only when: If the source does not state the exact evaluation dataset version or protocol, keep claims qualitative.

### Matryoshka dimension-flexible embeddings

- Datasets: MTEB, PubMed QA, PubMed Subset, PubMed Summary
- Metrics: Pearson correlation (higher is better, where reported), Retrieval quality at a documented embedding dimension (higher is better)
- Compare only when: Use only dimensions explicitly documented in the exact model card.
- Compare only when: Do not compare different truncation dimensions as if they were the same operating point.
- Compare only when: Do not infer dimension support for one Matryoshka-labeled checkpoint from another model card.
- Compare only when: Keep MTEB-style semantic evaluations separate from biomedical retrieval benchmarks unless the protocol is the same.

## Primary sources

- [aaditya/Llama3-OpenBioLLM-8B model card](https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B) — Hugging Face repository for aaditya; supports OpenBioLLM-8B is evidenced as a biomedical instruction-tuned language model with benchmark tables., The findings do not evidence this checkpoint as a native embedding retriever.
- [MedEmbed-base-v0.1 model card](https://huggingface.co/abhinand/MedEmbed-base-v0.1) — Hugging Face repository for abhinand; supports MedEmbed-base-v0.1 is a specialized embedding model for medical and clinical data for information retrieval, question answering, and semantic search., The source references metrics such as nDCG, MAP, Recall, Precision, and MRR, but the findings do not supply protocol-complete numeric rows here.
- [MedEmbed-large-v0.1 model card](https://huggingface.co/abhinand/MedEmbed-large-v0.1) — Hugging Face repository for abhinand; supports MedEmbed-large-v0.1 is a specialized embedding model for medical and clinical data for information retrieval, question answering, and semantic search.
- [MedEmbed-small-v0.1 model card](https://huggingface.co/abhinand/MedEmbed-small-v0.1) — Hugging Face repository for abhinand; supports MedEmbed-small-v0.1 is a specialized embedding model for medical and clinical data for information retrieval, question answering, and semantic search.
- [MedEmbed official repository](https://github.com/abhinand5/MedEmbed) — abhinand5 GitHub repository; supports The MedEmbed project includes Small, Base, and Large model variants., The repository names retrieval benchmarks including ArguAna, MedicalQARetrieval, NFCorpus, PublicHealthQA, and TRECCOVID, but repository-wide benchmark statements are not necessarily exact-checkpoint numeric evidence for every Forge candidate.
- [SapBERT-from-PubMedBERT-fulltext model card](https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext) — Hugging Face repository for cambridgeltl; supports SapBERT self-aligns biomedical entity representations., SapBERT leverages UMLS and is designed for medical entity linking, especially synonymy modeling between entities.
- [MedCPT-Article-Encoder model card](https://huggingface.co/ncbi/MedCPT-Article-Encoder) — Hugging Face repository for NCBI; supports The MedCPT Article Encoder generates embeddings of biomedical texts for semantic search and dense retrieval., The source states pretraining on 255 million query-article pairs from PubMed search logs., The source claims state-of-the-art performance on several zero-shot biomedical information-retrieval datasets, but the findings do not enumerate the exact datasets and metrics.
- [MedCPT-Query-Encoder model card](https://huggingface.co/ncbi/MedCPT-Query-Encoder) — Hugging Face repository for NCBI; supports The MedCPT Query Encoder generates embeddings for biomedical queries., It was pre-trained on the same 255 million query-article pairs as the article encoder.
- [MedCPT-Cross-Encoder model card](https://huggingface.co/ncbi/MedCPT-Cross-Encoder) — Hugging Face repository for NCBI; supports The MedCPT Cross Encoder is used for ranking articles given a query.
- [PubMedBERT base embeddings matryoshka model card](https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka) — Hugging Face repository for NeuML; supports The model supports dynamic embedding dimensionalities of 64, 128, 256, 384, 512, and 768., The findings mention MTEB evaluation using Pearson correlation coefficient as the metric.
- [PubMedBERT base embeddings model card](https://huggingface.co/NeuML/pubmedbert-base-embeddings) — Hugging Face repository for NeuML; supports The model maps sentences and paragraphs to a 768-dimensional dense vector space., The findings report evaluation on PubMed QA, PubMed Subset, and PubMed Summary with an average score of 95.62., The source supports biomedical sentence and paragraph embeddings.
- [NVIDIA nv-embedqa-e5-v5 API reference](https://docs.api.nvidia.com/nim/reference/nvidia-nv-embedqa-e5-v5) — NVIDIA documentation; supports The NVIDIA Retrieval QA E5 Embedding Model is ready for commercial use., The source states it is a transformer encoder fine-tuned version of E5-Large-Unsupervised with 24 layers and embedding size 1024.
- [potsu-potsu medembed-small-biomedical-matryoshka-v2 model page](https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2) — Hugging Face repository for potsu-potsu; supports This URL is the official sourceUrl in expected scope for the exact upstream checkpoint identity, but the provided findings contain no factual extraction from it, so checkpoint-scoped claims remain unresolved.

## Evidence gaps

- Evidence gap: The provided findings do not include extracted facts from https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2, so no checkpoint-scoped capability, dimension, or benchmark claims can be verified for potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9 or potsu-potsu-medembed-small-biomedical-matryoshka-v2-vllm-cuda13 beyond source identity.
- Evidence gap: The findings do not provide primary evidence that Forge TEI, vLLM, or wrapper packaging changes model quality or semantics for abhinand-medembed-small-v0-1-tei-cuda-1-9 versus abhinand-medembed-small-v0-1-vllm-cuda13, for neuml-pubmedbert-base-embeddings-tei-cuda-1-9 versus neuml-pubmedbert-base-embeddings-vllm-cuda13, or for other packaging variants in scope.
- Evidence gap: The findings do not specify exact benchmark dataset names, splits, metric values, or tables for MedCPT's claim of state-of-the-art performance on several zero-shot biomedical information-retrieval datasets, so routing cannot rely on exact numeric head-to-head superiority.
- Evidence gap: The findings mention MedEmbed benchmark families and metrics, but do not provide protocol-complete numeric rows for the exact in-scope Small, Base, and Large checkpoints under a shared comparison protocol against the rest of the candidate set.
- Evidence gap: The findings do not specify pooling method, normalization, truncation policy, maximum input length, or output postprocessing for most in-scope embedding checkpoints, so operational comparisons on those dimensions cannot be verified.
- Evidence gap: The findings do not provide exact reranking benchmark datasets, metrics, or candidate-pool conditions for ncbi-medcpt-cross-encoder-wrapper-cuda12; only its use for ranking articles given a query is directly supported.
- Evidence gap: The findings support SapBERT for biomedical entity representation and medical entity linking, but do not provide the exact evaluation protocol, metric table, or ontology version needed for benchmark-level comparison with other candidates.
- Evidence gap: The findings provide NVIDIA serving-page facts for nvidia-nv-embedqa-e5-v5 but do not provide protocol-aligned biomedical head-to-head comparisons against the other exact Forge candidates.
- Evidence gap: The findings provide benchmark tables for aaditya/Llama3-OpenBioLLM-8B, but those are for a biomedical instruction-tuned language model and do not establish native retrieval or embedding behavior for the Forge candidate.
- Evidence gap: The findings cite repository-wide MedEmbed benchmark names including ArguAna and PublicHealthQA, but exact checkpoint-level numeric verification for the in-scope variants under identical conditions is not supplied.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
