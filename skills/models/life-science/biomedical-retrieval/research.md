# Biomedical Retrieval model selection

- Category: `life-science`
- Group: `biomedical-retrieval`
- Independent audit: `revised`
- Researched: `2026-07-23T22:59:59.299716+00:00`

Biomedical literature retrieval with text embedding models for scientific literature. In scope: embedding queries and documents such as titles and abstracts for nearest-neighbor retrieval or ranking. Out of scope: generative text generation, supervised rerankers, token-classification tasks, and any benchmark or service behavior not verified for the exact upstream checkpoint or exact Forge-served variants. Upstream-checkpoint evidence from EMBO/soda-vec-dot-std-cov-losses must be kept separate from serving-wrapper evidence for the tei and vllm Forge variants.

## Questions to answer before selecting

- Do you need evidence that applies to the exact upstream checkpoint EMBO/soda-vec-dot-std-cov-losses, or do you specifically require wrapper-scoped evidence for embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9 or embo-soda-vec-dot-std-cov-losses-vllm-cuda13?
- Do you require verified author-provided evidence for the training objective and high-level training configuration of EMBO/soda-vec-dot-std-cov-losses?
- Do you require verified tokenizer details, tokenizer configuration, pooling behavior, normalization behavior, preprocessing scripts, input limits, embedding shape or dtype, or recommended similarity metric for the exact checkpoint or Forge wrapper?
- Do you require verified biomedical retrieval benchmark numbers tied to the exact checkpoint EMBO/soda-vec-dot-std-cov-losses rather than to other EMBO checkpoints?
- Do you require primary evidence that tei and vllm preserve identical tokenizer, pooling, and embedding semantics for this exact model?

## Comparability rules

- Only compare results when they are tied to the same exact upstream checkpoint; evidence for EMBO/vicreg_exact, EMBO/dot_only, or EMBO/vicreg_our_contrast is not directly comparable to EMBO/soda-vec-dot-std-cov-losses.
- Do not transfer checkpoint-level evidence to Forge wrapper variants as wrapper-specific evidence unless the source explicitly establishes that mapping.
- Tokenizer identity and tokenizer configuration must match exactly before comparing embeddings or retrieval scores; the research findings do not verify these for the exact checkpoint.
- Pooling and normalization behavior must match exactly before comparing embeddings or retrieval scores; the research findings do not verify these for the exact checkpoint or wrappers.
- Dataset name, split, and preprocessing pipeline must match exactly before comparing retrieval metrics; the research findings do not verify benchmark protocol details for the exact checkpoint.
- Metric definition and averaging rules must match exactly before comparing retrieval metrics; the research findings do not verify metric implementations for the exact checkpoint.
- Wrapper/runtime comparability between tei and vllm requires primary evidence that serving does not alter tokenizer, pooling, normalization, or embedding semantics; the available primary findings do not establish this.

## Conditional routing

### Prefer `insufficient-evidence` when You need primary upstream-checkpoint evidence that the model was trained with the named dot/std/cov objective and documented training configuration.

- Why: The primary model page for EMBO/soda-vec-dot-std-cov-losses verifies upstream-checkpoint facts including a custom VICReg configuration named "dot_std_cov", training hyperparameters, more than 26 million PubMed Central title-abstract pairs, and answerdotai/ModernBERT-base as the base model. However, the findings do not provide primary evidence distinguishing embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9 from embo-soda-vec-dot-std-cov-losses-vllm-cuda13 on this criterion.
- Alternative: embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9
- Alternative: embo-soda-vec-dot-std-cov-losses-vllm-cuda13
- Evidence: https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses

### Prefer `insufficient-evidence` when You require verified biomedical retrieval benchmark metrics tied to the exact checkpoint EMBO/soda-vec-dot-std-cov-losses or to either exact Forge variant.

- Why: The research findings do not provide any numeric retrieval benchmark result, dataset split, metric value, or averaging protocol for EMBO/soda-vec-dot-std-cov-losses. Findings about benchmark coverage exist for EMBO/vicreg_exact, but they are for a different checkpoint and cannot be transferred.
- Alternative: embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9
- Alternative: embo-soda-vec-dot-std-cov-losses-vllm-cuda13
- Evidence: https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses, https://huggingface.co/EMBO/vicreg_exact

### Prefer `insufficient-evidence` when You require verified tokenizer configuration, pooling, normalization, preprocessing scripts, input limits, embedding dimensionality or dtype, or similarity-metric guidance for the exact checkpoint or either Forge wrapper.

- Why: The available primary findings for EMBO/soda-vec-dot-std-cov-losses do not specify tokenizer details, pooling, normalization, preprocessing scripts, maximum input length, embedding output shape, embedding dtype, or recommended similarity metric. The TEI and vLLM sources in the findings are general engine documentation and do not establish model-specific invariance for this checkpoint.
- Alternative: embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9
- Alternative: embo-soda-vec-dot-std-cov-losses-vllm-cuda13
- Evidence: https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses

### Prefer `insufficient-evidence` when You need evidence that one Forge wrapper is semantically identical to the other for this exact model.

- Why: The findings include a general TEI documentation page and a general vLLM quickstart page, but they do not verify that embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9 and embo-soda-vec-dot-std-cov-losses-vllm-cuda13 serve unchanged identical tokenizer, pooling, normalization, or embedding semantics for this checkpoint.
- Alternative: embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9
- Alternative: embo-soda-vec-dot-std-cov-losses-vllm-cuda13
- Evidence: https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses

### Prefer `embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9` when You only need a candidate list that explicitly includes both exact Forge slugs while acknowledging no verified primary routing distinction between them.

- Why: No primary finding establishes a quality, semantics, or protocol advantage for either Forge wrapper. This rule does not claim superiority; it only names one exact candidate while keeping the other as an alternative to satisfy exact-slug routing coverage under insufficient evidence.
- Alternative: embo-soda-vec-dot-std-cov-losses-vllm-cuda13
- Evidence: https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses

## Benchmark taxonomy

### Biomedical literature retrieval

- Datasets: Evidence gap: No benchmark dataset or split is numerically evaluated for the exact checkpoint EMBO/soda-vec-dot-std-cov-losses in the available primary findings.
- Metrics: Recall@k (higher is better; exact k and averaging must be specified before comparison), MRR (higher is better; averaging protocol must be specified before comparison), nDCG@k (higher is better; exact k and gain formulation must be specified before comparison), MAP (higher is better; exact averaging protocol must be specified before comparison)
- Compare only when: Same exact checkpoint must be evaluated.
- Compare only when: Same dataset and split must be used.
- Compare only when: Same preprocessing pipeline must be used.
- Compare only when: Same tokenizer and tokenizer configuration must be used.
- Compare only when: Same pooling and normalization behavior must be used.
- Compare only when: Same metric implementation and averaging rules must be used.
- Compare only when: Same serving semantics must be verified if comparing tei and vllm variants.

## Primary sources

- [EMBO/soda-vec-dot-std-cov-losses — Hugging Face model page](https://huggingface.co/EMBO/soda-vec-dot-std-cov-losses) — Hugging Face (EMBO); supports EMBO/soda-vec-dot-std-cov-losses uses a learning rate of 8e-5., EMBO/soda-vec-dot-std-cov-losses uses warmup_steps of 1000., EMBO/soda-vec-dot-std-cov-losses sets max_grad_norm to 2.0., EMBO/soda-vec-dot-std-cov-losses sets weight_decay to 0.01., EMBO/soda-vec-dot-std-cov-losses uses a batch size of 32., EMBO/soda-vec-dot-std-cov-losses uses gradient_accumulation_steps of 1., EMBO/soda-vec-dot-std-cov-losses enables fp16., EMBO/soda-vec-dot-std-cov-losses uses a cosine learning rate scheduler., EMBO/soda-vec-dot-std-cov-losses runs for a maximum of 500000 steps., EMBO/soda-vec-dot-std-cov-losses evaluates every 10000 steps., EMBO/soda-vec-dot-std-cov-losses saves checkpoints every 50000 steps., EMBO/soda-vec-dot-std-cov-losses uses a custom VICReg configuration named "dot_std_cov"., The dot_std_cov configuration includes dot_loss, std_loss, and cov_loss component descriptions., SODA-VEC is described as a sentence transformer model for scientific literature., EMBO/soda-vec-dot-std-cov-losses was trained on more than 26 million title-abstract pairs from PubMed Central., The base model for SODA-VEC is answerdotai/ModernBERT-base.
- [EMBO/vicreg_exact — Hugging Face model page](https://huggingface.co/EMBO/vicreg_exact) — Hugging Face (EMBO); supports EMBO/vicreg_exact is a different EMBO checkpoint with its own training data and benchmark statements., EMBO/vicreg_exact states that detailed evaluation results are in SODA-VEC benchmark notebooks., EMBO/vicreg_exact uses answerdotai/ModernBERT-base as its base model., EMBO/vicreg_exact was trained on EMBO/soda-vec-data-full_pmc_title_abstract_paired., EMBO/vicreg_exact uses exact VICReg objective components and specific coefficients.

## Evidence gaps

- Evidence gap: The available findings verify upstream-checkpoint evidence for EMBO/soda-vec-dot-std-cov-losses but do not provide primary wrapper-specific evidence for embo-soda-vec-dot-std-cov-losses-tei-cuda-1-9 or embo-soda-vec-dot-std-cov-losses-vllm-cuda13.
- Evidence gap: No primary finding verifies tokenizer identity or tokenizer configuration for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No primary finding verifies pooling behavior, whether pooling is in-checkpoint or wrapper-applied, or whether normalization is applied for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No primary finding verifies preprocessing scripts or benchmark preprocessing protocol for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No primary finding verifies maximum input length for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No primary finding verifies embedding dimensionality, output shape, or dtype for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No primary finding verifies a recommended similarity metric for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No numeric biomedical retrieval benchmark tied to the exact checkpoint EMBO/soda-vec-dot-std-cov-losses is present in the available primary findings.
- Evidence gap: Findings about benchmark coverage for EMBO/vicreg_exact cannot be transferred to EMBO/soda-vec-dot-std-cov-losses because they are different checkpoints.
- Evidence gap: No primary finding verifies semantic invariance between the tei and vllm Forge variants for this exact model.
- Evidence gap: No primary finding in the provided evidence states the license for EMBO/soda-vec-dot-std-cov-losses, even though the Forge candidate metadata labels the Forge models as MIT; this dossier does not treat that metadata as primary source evidence.
- Evidence gap: No primary finding provides biomedical safety, privacy, clinical-use, or data-handling guidance for EMBO/soda-vec-dot-std-cov-losses.
- Evidence gap: No primary finding provides exact retrieval task splits, metric definitions, or averaging rules for benchmark comparison of EMBO/soda-vec-dot-std-cov-losses.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
