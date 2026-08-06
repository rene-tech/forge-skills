# Retrieval And Reranking model selection

- Category: `general`
- Group: `retrieval-and-reranking`
- Independent audit: `revised`
- Researched: `2026-07-23T20:17:09.524248+00:00`

Select among these exact Forge reranking candidates for second-stage retrieval and RAG ranking: alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9, baai-bge-reranker-v2-m3-tei-cuda-1-9, nvidia-llama-3-2-nv-rerankqa-1b-v2-nim, nvidia-llama-nemotron-rerank-1b-v2-nim, nvidia-llama-nemotron-rerank-vl-1b-v2-nim, qwen-qwen3-reranker-0-6b-vllm-cuda13, qwen-qwen3-reranker-4b-vllm-cuda13, and qwen-qwen3-vl-reranker-2b-vllm-cuda13. In scope: ranking candidate passages or documents against a query for retrieval, RAG, QA passage reranking, multilingual or cross-lingual text reranking where officially stated, code retrieval where officially stated, and multimodal visual-document or image retrieval reranking for the vision-capable models. Out of scope: first-stage embedding retrieval selection, generation models, non-listed checkpoint variants or sizes, quantized or mirrored reuploads, wrapper-specific latency claims as quality evidence, and performance claims transferred from related but non-identical models.

## Questions to answer before selecting

- Is the retrieval corpus strictly text, or does it include images, screenshots, slides, or visual documents that must be reranked against a text query?
- Do you need a text-only reranker or a multimodal cross-encoder that can score image, text, or mixed image+text documents?
- Is the use case English-only, multilingual, or explicitly cross-lingual?
- Is the workload specifically question-answering passage reranking, or broader generic retrieval reranking?
- Is code retrieval officially required?
- Do you require long input handling, and if so, is an official max input length stated for the candidate you may choose?
- Do you need evidence from BEIR, LoCo, MIRACL, MLQA, MLDR, NQ, HotpotQA, FiQA, TechQA, ViDoRe, or another benchmark family, and are the protocols directly comparable?
- Are you comparing standalone reranker scores, or pipeline-level retrieval results that combine an embedding model and a reranker?
- Do you need commercial-use clarity, and if so, are Apache-2.0 terms preferred over NVIDIA Open Model plus Llama community licensing or NIM/container terms?
- Do you need explicit output semantics such as a logit relevance score or binary-classification-head scoring behavior?
- Do you need instruction-aware ranking behavior, and is this officially documented for the exact candidate?
- For multimodal use, what exact document representation is available at inference time: image only, text extracted from images, or image+text together?
- Is an evidence gap acceptable, or do you need only candidates with directly comparable primary-source evaluations?

## Comparability rules

- Only compare benchmark values when they come from the exact listed candidate, not a related family member, different parameter size, wrapper, quantization, mirror, or sibling checkpoint.
- Dataset and benchmark family must match exactly, including named benchmark collection and any cited sub-benchmark grouping such as BEIR, MIRACL, MLQA, MLDR, LoCo, ViDoRe V1/V2/V3, NQ, HotpotQA, FiQA, or TechQA.
- Exact split or subset must match. If a source gives only a benchmark family average or does not specify splits/subsets, treat comparisons to split-specific numbers as not directly comparable.
- Task formulation must match: generic retrieval reranking, multilingual retrieval reranking, cross-lingual retrieval, QA passage reranking, long-context retrieval, code retrieval, or multimodal visual-document retrieval are different tasks.
- Query/document format must match, such as query/passage, question/passage, text query with text documents, text query with images, or text query with image+text documents.
- Prompt, instruction, or template format must match. If not documented for both sides, treat the comparison as uncertain.
- Input shape and truncation policy must match, including maximum sequence length, document chunking, and any image/text combination strategy. If one model has 8192-token support and another source does not specify context handling, quality comparisons on long-context tasks are not directly controlled.
- Context/window limits must match or be accounted for explicitly. Long-context benchmark results should not be compared against shorter-context or unspecified-context evaluations without noting this mismatch.
- Scoring/output semantics must match: raw logits, binary classification head outputs, mean-pooled relevance scores, or API-specific rerank scores may not be directly comparable numerically across implementations; only ranking-effectiveness metrics should be compared unless scoring calibration is controlled.
- Metric definition must match exactly, including Recall@5, BEIR aggregate score, LoCo aggregate score, macro-F1, or other metric definitions. Do not compare different metrics as if they reflected the same property.
- Evaluation protocol must match, including whether the number is a standalone reranker benchmark, a reranker+embedding pipeline result, an internally curated dataset result, or a benchmark average across multiple datasets.
- Filtering and candidate-generation conditions must match. Pipeline Recall@5 results that depend on a paired embedding model are not directly comparable to standalone reranker aggregate scores.
- Language coverage must match. English-only results should not be used to choose for multilingual or cross-lingual deployment unless no multilingual evidence exists and the gap is stated.
- Fine-tuning regime or training objective must be comparable when inferring transfer: contrastive-learning cross-encoders, binary classification heads, instruction-aware rerankers, or other adaptation regimes may differ materially.
- Whether the result is zero-shot, instruction-tuned, distilled, or otherwise adapted must match if documented. If not documented for both compared results, treat the comparison as incomplete.
- For multimodal models, modality conditions must match exactly: image-only, text-only, or image+text results from the same benchmark are separate settings and should not be merged.
- License or acceptable-use restrictions are not quality metrics, but they are valid selection constraints and must be matched to deployment requirements before preferring a candidate.
- Where a source reports an improvement over an embedding baseline rather than a head-to-head against another listed reranker, treat that as within-model evidence only, not a definitive cross-model ranking.

## Conditional routing

### Prefer `alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9` when You need English-only text retrieval reranking with documented reranker-only benchmark numbers and long-context support.

- Why: The Alibaba-NLP gte-reranker-modernbert-base model card and README in the supplied findings assert this exact reranker identity, parameter count (149M), an 8192-token maximum sequence length, and reported BEIR and LoCo reranker scores for the exact reranker checkpoint.
- Alternative: qwen-qwen3-reranker-0-6b-vllm-cuda13
- Alternative: qwen-qwen3-reranker-4b-vllm-cuda13
- Alternative: nvidia-llama-nemotron-rerank-1b-v2-nim
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/c40156962ee2a34679b0c8399e0d1bb9d68d54ab/README.md, https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2

### Prefer `nvidia-llama-3-2-nv-rerankqa-1b-v2-nim` when You need multilingual or cross-lingual question-answering passage reranking with vendor-stated multilingual evaluation and long-context support.

- Why: NVIDIA NIM documentation and the NVIDIA Build page in the findings describe the Llama 3.2 NV-RerankQA 1B v2 NIM as a fine-tuned reranking model supporting multilingual, cross-lingual QA retrieval, evaluated on 26 languages and with an 8192-token context window; NVIDIA reports pipeline-level Recall@5 style results in supplied findings tied to its retrieval stack.
- Alternative: nvidia-llama-nemotron-rerank-1b-v2-nim
- Alternative: baai-bge-reranker-v2-m3-tei-cuda-1-9
- Alternative: qwen-qwen3-reranker-0-6b-vllm-cuda13
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://bge-model.com/tutorial/5_Reranking/5.2.html, https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

### Prefer `nvidia-llama-nemotron-rerank-1b-v2-nim` when You need a general-purpose multilingual text reranker (non QA-branded) with official model-card claims about contrastive fine-tuning and 26-language evaluation.

- Why: The nvidia/llama-nemotron-rerank-1b-v2 model card and NVIDIA modelcard pages in the findings describe this exact checkpoint as a contrastive-learning fine-tuned cross-encoder for multilingual passage reranking with 8192-token support and intended multilingual evaluation.
- Alternative: nvidia-llama-3-2-nv-rerankqa-1b-v2-nim
- Alternative: baai-bge-reranker-v2-m3-tei-cuda-1-9
- Alternative: qwen-qwen3-reranker-4b-vllm-cuda13
- Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://bge-model.com/tutorial/5_Reranking/5.2.html, https://huggingface.co/Qwen/Qwen3-Reranker-4B

### Prefer `nvidia-llama-nemotron-rerank-vl-1b-v2-nim` when You need multimodal visual-document reranking (image, text, or image+text documents) with primary-source ViDoRe metrics reported for the exact checkpoint.

- Why: The NVIDIA Llama Nemotron Rerank VL 1B v2 model pages in the findings state the exact checkpoint accepts text queries paired with image, text, or combined document inputs, reports ViDoRe V1/V2/V3 Recall@5 results, and provides logit scoring semantics for multimodal document relevance.
- Alternative: qwen-qwen3-vl-reranker-2b-vllm-cuda13
- Alternative: nvidia-llama-nemotron-rerank-1b-v2-nim
- Evidence: https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2/modelcard, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2

### Prefer `qwen-qwen3-vl-reranker-2b-vllm-cuda13` when You need the broadest multimodal input types including video or arbitrary multimodal combinations and prefer primary-source claims of video support.

- Why: The Qwen3-VL-Reranker-2B model card in the supplied findings states this exact checkpoint accepts text, images, screenshots, videos, and arbitrary multimodal combinations and declares multimodal retrieval scope; the supplied findings do not provide exact modality-specific benchmark tables for the exact 2B checkpoint.
- Alternative: nvidia-llama-nemotron-rerank-vl-1b-v2-nim
- Alternative: qwen-qwen3-reranker-4b-vllm-cuda13
- Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2/modelcard, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/Qwen/Qwen3-Reranker-4B

### Prefer `alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9` when You require explicitly Apache-2.0 licensed models for licensing-simplicity and English or multilingual reranking scope.

- Why: The Alibaba-NLP gte-reranker-modernbert-base model card in the findings identifies the exact checkpoint and its license context; Qwen model cards in the findings also assert Apache-2.0 for their reranker checkpoints but lack the same direct reranker-benchmark detail in the supplied findings. NVIDIA candidates in the findings use NVIDIA Open Model License and Llama community license material, which complicates license-simple selection.
- Alternative: qwen-qwen3-reranker-0-6b-vllm-cuda13
- Alternative: qwen-qwen3-reranker-4b-vllm-cuda13
- Alternative: qwen-qwen3-vl-reranker-2b-vllm-cuda13
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base, https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf

### Prefer `qwen-qwen3-reranker-0-6b-vllm-cuda13` when You need an explicit primary-source benchmark for code retrieval on the exact listed candidates.

- Why: The Qwen3-Reranker-0.6B model card in the findings asserts family-level code retrieval applicability for the Qwen3 reranker series and the 0.6B identity is confirmed, while the supplied findings do not contain primary-source code-retrieval benchmark tables for the exact listed candidates.
- Alternative: qwen-qwen3-reranker-4b-vllm-cuda13
- Alternative: nvidia-llama-nemotron-rerank-1b-v2-nim
- Alternative: alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base

### Prefer `insufficient-evidence` when You require a definitive head-to-head winner among the exact listed candidates using a single unified evaluation protocol with matched datasets, language coverage, and truncation settings.

- Why: The supplied findings do not provide a single unified primary-source head-to-head benchmark across the exact listed Forge candidates; multiple supplied sources report model- or pipeline-level results under differing protocols or report family-level identity without exact-checkpoint benchmark tables.
- Alternative: alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9
- Alternative: baai-bge-reranker-v2-m3-tei-cuda-1-9
- Alternative: nvidia-llama-3-2-nv-rerankqa-1b-v2-nim
- Alternative: nvidia-llama-nemotron-rerank-1b-v2-nim
- Alternative: nvidia-llama-nemotron-rerank-vl-1b-v2-nim
- Alternative: qwen-qwen3-reranker-0-6b-vllm-cuda13
- Alternative: qwen-qwen3-reranker-4b-vllm-cuda13
- Alternative: qwen-qwen3-vl-reranker-2b-vllm-cuda13
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base, https://bge-model.com/tutorial/5_Reranking/5.2.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard, https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2/modelcard, https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B

## Benchmark taxonomy

### English text retrieval reranking

- Datasets: BEIR, LoCo
- Metrics: BEIR aggregate score; direction higher is better, LoCo aggregate score; direction higher is better
- Compare only when: Use the exact same English reranker checkpoint.
- Compare only when: Match benchmark family exactly: BEIR versus LoCo are not interchangeable.
- Compare only when: Match the same evaluation aggregation and any benchmark subset composition.
- Compare only when: Use the same query-document or query-passage formulation.
- Compare only when: Use the same prompt/instruction format; if undocumented for one side, comparison is incomplete.
- Compare only when: Match maximum input shape, chunking, and truncation policy; long-context-sensitive results are not comparable when context handling differs.
- Compare only when: Match scoring semantics and rerank API behavior if comparing system outputs rather than published benchmark aggregates.
- Compare only when: Confirm whether the result is standalone reranker evaluation rather than a reranker-plus-embedding pipeline.
- Compare only when: Match language coverage: English-only evaluations should not be generalized to multilingual selection without an evidence-gap note.
- Compare only when: Match training/adaptation regime if claimed as a reason for quality, such as the same reranker head type or instruction-aware setup.

### Multilingual retrieval reranking

- Datasets: MIRACL, MLQA, MLDR, BEIR, TechQA
- Metrics: Recall@5; direction higher is better, Benchmark aggregate scores when explicitly reported; direction higher is better
- Compare only when: Use the same exact listed candidate.
- Compare only when: Match dataset family and named subset; MIRACL, MLQA, and MLDR measure different multilingual properties.
- Compare only when: Match language set and coverage; results over 26 languages are not directly comparable to English-only or unspecified-language evaluations.
- Compare only when: Match whether the number is standalone reranker performance or a pipeline metric requiring a paired embedding model.
- Compare only when: Match task formulation: generic multilingual retrieval versus multilingual QA passage reranking are distinct.
- Compare only when: Match input window limits and truncation behavior.
- Compare only when: Match prompt/template and query-passage formatting.
- Compare only when: Match metric definition and aggregation; Recall@5 is not directly comparable to BEIR or LoCo aggregate scores.
- Compare only when: Match evaluation filtering and candidate generation rules if a pipeline benchmark is used.
- Compare only when: Match adaptation regime, such as contrastive-learning fine-tuning with a binary classification head versus another reranker training setup.

### Cross-lingual retrieval reranking

- Datasets: MIRACL, MLQA, MLDR
- Metrics: Recall@5; direction higher is better, Any officially reported cross-lingual retrieval aggregate if explicitly provided; direction higher is better
- Compare only when: Cross-lingual intent must be explicitly supported by the source for the exact candidate.
- Compare only when: Match source and target language conditions; if the benchmark averages across languages, compare only to results with the same aggregation.
- Compare only when: Match query and passage language configuration where documented.
- Compare only when: Match whether the benchmark is question-answer retrieval or generic document retrieval.
- Compare only when: Match input window and truncation behavior.
- Compare only when: Match paired embedding baseline if the reranker result is reported at pipeline level.
- Compare only when: Match metric definition and candidate-pool construction.
- Compare only when: If a candidate only has multilingual, not explicit cross-lingual, evidence, mark that as a scope gap rather than assuming equivalence.

### QA passage reranking

- Datasets: NQ, HotpotQA, FiQA, TechQA, MLQA
- Metrics: Recall@5; direction higher is better
- Compare only when: The task must be question-to-passage or question-to-document reranking, not generic retrieval.
- Compare only when: Match whether scores are reported for reranker-only evaluation or reranker-plus-embedding pipeline retrieval.
- Compare only when: Match candidate generation, top-k cutoff, and filtering.
- Compare only when: Match question and passage format.
- Compare only when: Match language and cross-lingual setting.
- Compare only when: Match prompt/template if any instruction or query formatting is used.
- Compare only when: Match input limits and truncation policy.
- Compare only when: Match aggregation across datasets when comparing average Recall@5 figures.
- Compare only when: Do not compare pipeline Recall@5 from QA retrieval directly against standalone BEIR or LoCo reranker aggregate scores.

### Long-context retrieval reranking

- Datasets: LoCo, MLDR
- Metrics: LoCo aggregate score; direction higher is better, Recall@5 on MLDR when explicitly reported; direction higher is better
- Compare only when: Match long-context benchmark exactly.
- Compare only when: Match maximum supported context/input length and actual evaluation truncation policy.
- Compare only when: Match document chunking strategy and whether whole long passages or segmented chunks are reranked.
- Compare only when: Match language conditions; MLDR is multilingual evidence while LoCo in the supplied findings is tied to English GTE reporting.
- Compare only when: Match whether the evaluation is standalone reranker or pipeline.
- Compare only when: Match prompt/template and scoring semantics.

### Multimodal visual-document retrieval reranking

- Datasets: ViDoRe V1, ViDoRe V2, ViDoRe V3
- Metrics: Recall@5; direction higher is better
- Compare only when: Use a multimodal reranker capable of the same modality condition being evaluated.
- Compare only when: Match modality exactly: image-only, text-only, and image+text are separate comparison settings.
- Compare only when: Match document representation, e.g., screenshots of document pages or slides versus other image types.
- Compare only when: Match query modality: text query in the supplied NVIDIA evidence.
- Compare only when: Match whether OCR/text extraction is present and whether raw images, extracted text, or combined image+text are passed to the model.
- Compare only when: Match benchmark version: ViDoRe V1, V2, and V3 or an average across them.
- Compare only when: Match candidate generation and Recall@5 protocol.
- Compare only when: Match scoring semantics and any binary-classification-head ranking setup.
- Compare only when: Do not compare multimodal ViDoRe Recall@5 directly to text-only BEIR/LoCo or QA Recall@5 results.

### Text-only chunk retrieval with a multimodal reranker

- Datasets: BEIR, TechQA, MIRACL, MLQA, MLDR
- Metrics: Recall@5; direction higher is better
- Compare only when: The same multimodal model must be evaluated in text-only mode.
- Compare only when: Match benchmark family and any average composition exactly.
- Compare only when: Match whether the reported score is compared to a text-only counterpart or an embedding baseline.
- Compare only when: Match document chunking/truncation policy.
- Compare only when: Match query and text chunk format.
- Compare only when: Match language settings across multilingual benchmarks.
- Compare only when: Match pipeline versus standalone setup.

### Code retrieval reranking

- Datasets:
- Metrics: The research did not find primary-source benchmark metrics for code retrieval for the exact listed candidates.
- Compare only when: Do not infer code-retrieval quality from generic retrieval benchmarks.
- Compare only when: Only compare exact code-retrieval results if an official source reports dataset, split, task format, and metric for the exact candidate.
- Compare only when: If code retrieval is mentioned in candidate description but not backed by benchmark protocol in the supplied primary findings, treat selection as scope-fit only, not quality-ranked.

## Primary sources

- [Alibaba-NLP/gte-reranker-modernbert-base model card](https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base) — Alibaba-NLP on Hugging Face; supports Official identity of alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9 as an English text reranker., 149M parameter size and 8192-token maximum sequence length for the exact GTE reranker., Reported exact-model BEIR and LoCo results used in English reranking selection.
- [Alibaba-NLP gte-reranker-modernbert-base README snapshot](https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/c40156962ee2a34679b0c8399e0d1bb9d68d54ab/README.md) — Alibaba-NLP on Hugging Face; supports Detailed official benchmark numbers for gte-reranker-modernbert-base for BEIR and LoCo reported for the exact reranker., Support for long-context English reranking taxonomy and comparability notes.
- [BGE reranking tutorial](https://bge-model.com/tutorial/5_Reranking/5.2.html) — BAAI/BGE; supports Official family-level description of BAAI/bge-reranker-v2-m3 as a multilingual lightweight cross-encoder with 568M parameters (family-level) and deployment/tutorial guidance., Evidence gap statement that the supplied findings lack exact benchmark protocol details for this exact listed candidate.
- [BAAI/bge-reranker-v2-m3 model page](https://huggingface.co/BAAI/bge-reranker-v2-m3) — BAAI on Hugging Face; supports Official model-card identity for baai-bge-reranker-v2-m3 and family-level claims about multilingual lightweight reranker scope.
- [NVIDIA NIM API reference for Llama-3.2 NV-RerankQA 1B v2](https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2) — NVIDIA; supports Official identity, task scope, 8192-token limit, 26-language evaluation, and NIM-serving documentation for nvidia-llama-3-2-nv-rerankqa-1b-v2., Notes that some reported NVIDIA results are pipeline-level and tied to the retrieval stack.
- [NVIDIA Build page for Llama-3.2 NV-RerankQA 1B v2](https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2) — NVIDIA; supports Official description of multilingual, cross-lingual text QA retrieval and long-context support for the exact NIM-served candidate.
- [NVIDIA Llama Nemotron Rerank 1B v2 model card (Build page)](https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard) — NVIDIA; supports Official model-card facts for nvidia-llama-nemotron-rerank-1b-v2 including training description and intended multilingual reranking scope., Evidence that some NVIDIA reported results are pipeline-level and that the model was trained on auditable, commercially-eligible QA corpora per the model card.
- [nvidia/llama-nemotron-rerank-1b-v2 model card](https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2) — NVIDIA on Hugging Face; supports Official identity, architecture summary (contrastive learning, cross-encoder), 8192-token limit claim, and intended multilingual passage-reranking scope for nvidia-llama-nemotron-rerank-1b-v2.
- [NVIDIA Llama Nemotron Rerank VL 1B v2 model card (Build page)](https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2/modelcard) — NVIDIA; supports Official multimodal identity for nvidia-llama-nemotron-rerank-vl-1b-v2, including image, text, and image+text document processing, and reported ViDoRe V1/V2/V3 Recall@5-style improvements.
- [nvidia/llama-nemotron-rerank-vl-1b-v2 model card](https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2) — NVIDIA on Hugging Face; supports Hugging Face model-card identity for the multimodal NVIDIA reranker and support for screenshots of document pages or slides and image contents including text, tables, charts, and infographics.
- [Qwen/Qwen3-Reranker-0.6B model card](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B) — Qwen on Hugging Face; supports Official identity of qwen-qwen3-reranker-0-6b-vllm-cuda13 as a 0.6B-parameter multilingual reranker in the Qwen3 series., Family-level statements of multilingual and code-retrieval applicability in the supplied findings (but lacking exact checkpoint-level benchmark tables in the supplied findings).
- [Qwen/Qwen3-Reranker-4B model card](https://huggingface.co/Qwen/Qwen3-Reranker-4B) — Qwen on Hugging Face; supports Official identity of qwen-qwen3-reranker-4b-vllm-cuda13 as a 4B-parameter reranker in the Qwen3 family and context-length claims included in the supplied findings.
- [Qwen/Qwen3-VL-Reranker-2B model card](https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B) — Qwen on Hugging Face; supports Official identity of qwen-qwen3-vl-reranker-2b-vllm-cuda13 as a multimodal reranker accepting text, images, screenshots, videos, and mixed-modal inputs (as stated in the supplied findings)., Family-level selection rule for video/broad multimodal requirements; the supplied findings do not include exact modality-specific benchmark tables for this exact checkpoint.
- [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf) — NVIDIA; supports Commercial-use and derivative-rights licensing context for NVIDIA candidates using the NVIDIA Open Model License as cited in the supplied findings.
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2) — build.nvidia.com; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The supplied findings do not include an official exact-model benchmark table (dataset splits, metric definitions, or prompt/template and truncation policy) for baai-bge-reranker-v2-m3 that would allow a verified head-to-head quality comparison against other exact listed candidates.
- Evidence gap: For qwen-qwen3-reranker-0-6b-vllm-cuda13 and qwen-qwen3-reranker-4b-vllm-cuda13 the supplied findings confirm model identity but do not provide exact primary-source benchmark tables, explicit dataset splits, prompt templates, or truncation policies for these exact checkpoints.
- Evidence gap: For qwen-qwen3-vl-reranker-2b-vllm-cuda13 the supplied findings confirm multimodal scope but do not include exact primary-source modality-specific benchmark numbers or dataset/split details for the exact 2B reranker.
- Evidence gap: NVIDIA-reported text-model numbers in the supplied findings are described as pipeline Recall@5 values tied to a paired embedding model or retrieval stack; the supplied findings do not always provide per-checkpoint standalone reranker-only benchmark tables for direct comparison to BEIR/LoCo reranker aggregates.
- Evidence gap: The supplied findings do not specify exact dataset splits/subsets, prompt templates, filtering rules, or candidate-generation methods for most reported benchmark numbers, preventing precise cross-model comparison without additional primary-source protocol details.
- Evidence gap: The supplied findings do not clearly state whether Qwen reranker evaluations (for 0.6B or 4B) are zero-shot, instruction-tuned, distilled, or otherwise adapted for the exact listed checkpoints.
- Evidence gap: The supplied findings do not include primary-source code-retrieval benchmark datasets or metric tables for the exact listed Qwen reranker checkpoints, despite family-level mentions of code retrieval.
- Evidence gap: No supplied primary finding provides a direct official head-to-head comparison among the exact listed text-only candidates under a single unified evaluation protocol with matched datasets, language coverage, and truncation settings.
- Evidence gap: Safety, data-handling, or operational acceptable-use guidance beyond licensing is not present for most candidates in the supplied findings; operational policy selection cannot be fully resolved from these sources alone.
- Evidence gap: For multimodal models, the supplied findings do not provide matched comparisons across identical modality settings between the NVIDIA and Qwen exact candidates (especially for image+text versus video-containing inputs).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.

- `low` https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
