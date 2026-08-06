# Genomics model selection

- Category: `life-science`
- Group: `genomics`
- Independent audit: `revised`
- Researched: `2026-07-23T20:25:19.801130+00:00`

Model-selection for genomic sequence representation and generation within the Forge "genomics" group. Scope: selecting among these four exact Forge slugs (huggingfacebio-carbon-3b-vllm-cuda13; instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding; longsafari-hyenadna-medium-450k-dna-embedding; zhihan1996-dnabert-2-117m-dna-embedding) for tasks including (a) long-context sequence embeddings, (b) dense per-base/position embeddings for classification, (c) generative DNA sequence design, (d) cross-species comparative embeddings, (e) commercial/clinical license compatibility, and (f) variant-effect prediction and fine-tuning on small labeled datasets. Out of scope: any other model checkpoints, quantizations, adapters, wrappers, NIM versions, or different parameter-scale checkpoints; every claim in this dossier is supported only by the primary sources listed in the top-level sources array. The research findings did not provide authoritative, primary-source versionKey commit objects for all slugs named in the user scope; where the exact versionKey/commit provenance is not present in the provided primary sources the dossier records an evidence gap. Recommended use, avoid-use, limitations, and safety/data-handling rule statements for this group are provided below; where the primary sources did not provide a specific statement the dossier records an explicit evidence gap.

Recommended use (sourced): prefer models whose primary sources document the capability required by the user (examples below are tied to primary-source evidence listed in the sources array). Avoid-use boundary (sourced or evidence-gapped): do not assume embedding dimensionality, JSON output schema, license status, or tokenizer stride for any slug unless an explicit primary-source artifact in the sources confirms those fields; otherwise treat as evidence gaps. Limitation (sourced or evidence-gapped): many cross-model comparisons require identical tokenization/k-merization and pooling; the primary sources do not provide an across-slug canonical k→base conversion protocol in the provided findings, which creates an evidence gap for direct k-mer vs single-base comparisons. Safety/data-handling rule (sourced or evidence-gapped): where primary sources do not include explicit biosecurity or misuse-mitigation guidance for a slug, treat absence as an evidence gap for deployment safety guidance.

## Questions to answer before selecting

- Do you require generative DNA sequence output (sampled sequences) or only fixed embeddings for downstream models?
- Is the application long-context (multi-100kb to multi-Mbp) where native single-nucleotide context is required, or is shorter context (≤2048 tokens) acceptable?
- Do you require per-base/dense positional embeddings (one embedding per nucleotide) or chunked/k-mer pooled embeddings?
- Is license compatibility with commercial deployment required (no NC clauses)?
- Is cross-species training-data diversity a priority (models trained on many species vs. human-centric)?
- Will you fine-tune on small labeled datasets (few-shot/freeze+head, linear probe, or full fine-tune)?
- Is a specific reference genome build (e.g., hg38) required for training/validation comparability?
- Do you require an explicit published evaluation on the task/dataset you care about (e.g., Genomic‑NIAH, GUE) for the exact slug and versionKey?
- What maximum input length/context (in bases or tokens) do you need at inference?
- Do you require single‑nucleotide tokenization or is k‑mer tokenization acceptable (and if k‑mer, which k)?

## Comparability rules

- Any reported benchmark comparison between two slugs is comparable only if the primary sources confirm identical dataset and split definitions, identical input preprocessing (including reference genome build and masking), identical tokenization/k-merization (same k and same stride), identical model checkpoint/versionKey, identical context length and tokenization stride/windowing, identical pooling or aggregation used to produce fixed embeddings, identical fine-tuning regime with matching hyperparameters, identical metric definitions and computation, and identical random-seed reporting or variance reporting for stochastic procedures. (This rule reflects the requirement that primary-source protocol items must match before numbers are comparable; the research findings do not provide cross-slug, matched head-to-head primary artifacts for the exact slugs.)
- Do not transfer claims across parameter scales, checkpoint variants, or model families: comparisons must reference the exact slug string and the exact primary-source provenance present in this dossier's sources.
- When models use different tokenization conventions (e.g., 6-mer vs. single-nucleotide), comparisons require an explicit transformation protocol documented in a primary source; if no such primary-source transformation exists in the dossier, declare the comparison not comparable.
- When context lengths differ across slugs, comparisons require either (a) a documented mapping from tokens to bases present in primary sources for both slugs, or (b) an evidence gap for cross-token comparability if no mapping is present in primary sources.

## Conditional routing

### Prefer `longsafari-hyenadna-medium-450k-dna-embedding` when If the user requires long-context sequence embeddings for multi‑hundred‑kb to multi‑Mbp genomic regions (primary priority: native single‑nucleotide context and maximum native context length at inference).

- Why: Primary sources for LongSafari/hyenadna-medium-450k-seqlen-hf document a single-character (single-nucleotide) tokenizer and long-context capabilities up to 450k tokens for the medium checkpoint and up to 1M tokens for larger variants; these primary artifacts establish native single-nucleotide tokenization and long-context design.
- Alternative: huggingfacebio-carbon-3b-vllm-cuda13
- Alternative: zhihan1996-dnabert-2-117m-dna-embedding
- Evidence: https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf, https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py, https://arxiv.org/pdf/2306.15794

### Prefer `zhihan1996-dnabert-2-117m-dna-embedding` when If the user requires dense per-position embeddings aligned to tokens with documented hidden-state output shape (primary priority: explicit per-token hidden-state dimensionality and pooling semantics).

- Why: Primary sources for zhihan1996/DNABERT-2-117M report hidden-state dimensionality 768 and that mean/max pooled embeddings therefore have dimensionality 768; the DNABERT repository and model card provide loading instructions and output shape evidence.
- Alternative: instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding
- Alternative: longsafari-hyenadna-medium-450k-dna-embedding
- Evidence: https://huggingface.co/zhihan1996/DNABERT-2-117M, https://github.com/MAGICS-LAB/DNABERT_2

### Prefer `huggingfacebio-carbon-3b-vllm-cuda13` when If the user requires a generative DNA model to propose synthetic sequences under an autoregressive objective (primary priority: explicit autoregressive/generative training objective and documented generation behavior).

- Why: The HuggingFaceBio/Carbon-3B primary model page documents Carbon-3B as a 3B-parameter decoder-only autoregressive genomic foundation model that uses a 6-mer tokenizer and a next-token generative objective; the Carbon model card in the primary sources also references Genomic‑NIAH benchmark evaluations reported for Carbon.
- Alternative: instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding
- Alternative: longsafari-hyenadna-medium-450k-dna-embedding
- Evidence: https://huggingface.co/HuggingFaceBio/Carbon-3B

### Prefer `instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding` when If the user requires cross-species comparative embeddings and provenance showing multi-species training data (primary priority: documented training-data species diversity in primary sources).

- Why: Primary sources for the Nucleotide Transformer family and the InstaDeepAI/nucleotide-transformer-v2-500m-multi-species model document training on many genomes (figures in the family GitHub and the model card/commit indicate integration of sequences from hundreds of species and thousands of human genomes) and commit-level tokenizer/hyperparameter evidence for k-mer tokenization and embedding dimension.
- Alternative: zhihan1996-dnabert-2-117m-dna-embedding
- Alternative: longsafari-hyenadna-medium-450k-dna-embedding
- Evidence: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://github.com/instadeepai/nucleotide-transformer, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/commit/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a

### Prefer `zhihan1996-dnabert-2-117m-dna-embedding` when If the user requires explicit permissive licensing (e.g., Apache-2.0) for commercial/clinical deployment.

- Why: The zhihan1996/DNABERT-2-117M model repository includes an Apache-2.0 LICENSE file in the primary-source repository evidence; the InstaDeepAI 500M slug and HuggingFaceBio Carbon-3B primary-source artifacts in the provided findings do not include an explicit Apache-2.0 license file for those exact slugs in the provided primary sources, creating license-provenance ambiguity for those slugs in this dossier.
- Alternative: instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding
- Alternative: huggingfacebio-carbon-3b-vllm-cuda13
- Evidence: https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://huggingface.co/HuggingFaceBio/Carbon-3B

### Prefer `huggingfacebio-carbon-3b-vllm-cuda13` when If the user prioritizes starting points for variant-effect prediction and small-dataset fine-tuning informed by primary-source benchmark claims.

- Why: The primary-source model page for Carbon-3B reports Genomic‑NIAH benchmark evaluations and variant-effect/perturbation claims tied to Carbon in the available findings, identifying Carbon as a candidate for generative/variant-effect workflows in the provided primary evidence.
- Alternative: zhihan1996-dnabert-2-117m-dna-embedding
- Alternative: instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding
- Evidence: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://huggingface.co/zhihan1996/DNABERT-2-117M

## Benchmark taxonomy

### Long-range retrieval and long-range regulatory prediction (Genomic‑NIAH style retrieval and planted-value retrieval across context lengths)

- Datasets: Genomic‑NIAH
- Metrics: Retrieval accuracy / success rate at planted-value depths (use the Genomic‑NIAH benchmark script in the primary source to compute exact metric), Where available, area-under-curve metrics reported by the original benchmark; compute area across thresholds only if the primary benchmark defines thresholding
- Compare only when: Same Genomic‑NIAH dataset and split definitions as used by the slug's primary source when that slug reports Genomic‑NIAH results
- Compare only when: Same context lengths measured and converted to base pairs consistently using the tokenizer mapping documented in the primary sources
- Compare only when: Same tokenization mapping protocol when comparing k‑mer token models to single‑base token models: require an explicit primary-source mapping; otherwise mark as not comparable
- Compare only when: Same model checkpoint/versionKey and same inference-time context extension method when reported

### Representation quality via transfer learning (classification/regression on promoter/enhancer/TF binding datasets — GUE style transfers)

- Datasets: Genome Understanding Evaluation (GUE)
- Metrics: AUROC for binary classification tasks, AUPRC for highly imbalanced classification tasks, Accuracy/F1 for balanced classification tasks, Spearman/Pearson correlation for regression tasks
- Compare only when: Use the exact datasets and splits defined in the GUE canonical specification as cited in DNABERT primary sources
- Compare only when: Use identical preprocessing: k-merization setting (same K), masking rules, coordinate conventions, genome build, and species-filtering as documented in the primary-source benchmark artifacts
- Compare only when: When comparing embedding methods, specify pooling (mean, max, CLS) used to convert token-level hidden states to fixed vectors; pooling must match across compared runs

### Variant effect prediction and motif-perturbation discrimination

- Datasets: Variant and motif perturbation sets as used in Carbon Genomic‑NIAH reporting
- Metrics: Task-specific accuracy or ranking metrics used by the primary benchmark (obtain canonical metric computation from the benchmark's primary artifact before comparing), When reported as classification, AUROC/AUPRC as aggregated metrics
- Compare only when: Same variant set and perturbation protocol; same input sequence window around the variant; same reference genome build; same mapping from tokenization to base positions
- Compare only when: Exact model checkpoint/versionKey must be the same as the one reported in the primary benchmark claim

### Embedding retrieval and nearest-neighbor tasks (planted-value retrieval across varying depths and context lengths)

- Datasets: Genomic‑NIAH
- Metrics: Retrieval precision@k, recall@k, success rate per planted depth, mean reciprocal rank (MRR), and top-k recall when cosine similarity is used, Report normalization procedures (L2/unit length) and pooling procedures used to compute embeddings
- Compare only when: Identical embedding extraction protocol: tokenization, pooling, normalization (L2/unit length), sliding window/tiling if used, and exact checkpoint/versionKey
- Compare only when: If models use different tokenizations (k vs. single base), require an explicit documented re-tokenization or mapping protocol in primary sources

### Generative evaluation (sequence sampling quality, constraint satisfaction, constrained design)

- Datasets: Task-specific held-out test sets defined by the primary work (as documented in the slug's primary sources)
- Metrics: Constraint satisfaction fraction (how often generated sequence meets explicit constraints), Perplexity or cross-entropy on held-out sequences when applicable (compute on same tokenization as used in training), Task-specific functional scores where experimental assays exist — report Spearman/Pearson correlation when available
- Compare only when: Same decode settings: sampling method (top-k/top-p), temperature, max generated length, and any post-processing to map tokens back to bases
- Compare only when: Same random seeds and number of sampling replicates for statistical reporting; same evaluation dataset/split and preprocessing

### Operational fine-tuning comparability (transfer settings for small labeled datasets)

- Datasets: User-specified supervised dataset (matches across models for comparability; e.g., GUE splits when applicable)
- Metrics: Task-dependent supervised metrics (AUROC/AUPRC/F1/accuracy/Spearman) with variance across seeds or cross-validation folds, Data efficiency curves (performance vs. labeled sample size) recommended
- Compare only when: Define fine-tuning regime explicitly (linear probe, head-only, or full fine-tune) and match optimizer, learning rate schedule, batch size, #epochs, regularization, early stopping criteria, and random seeds
- Compare only when: Use identical data augmentation, sequence windowing, and tokenization

## Primary sources

- [HuggingFaceBio/Carbon-3B (model card)](https://huggingface.co/HuggingFaceBio/Carbon-3B) — HuggingFaceBio (Hugging Face model card); supports Carbon-3B is a 3‑billion‑parameter decoder-only autoregressive genomic foundation model trained on DNA and RNA sequences with a primary focus on eukaryotes., Carbon-3B has a native context length of 32,768 6‑mer tokens (~197,000 DNA base pairs) and can extend context to 65,536 6‑mer tokens via YaRN per the model card facts in the research findings., Carbon-3B uses a custom DNA tokenizer that requires trust_remote_code and is built on top of a LlamaForCausalLM variant, and the model card reports Genomic‑NIAH benchmark evaluations.
- [InstaDeepAI/nucleotide-transformer-v2-500m-multi-species (Hugging Face model card)](https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species) — InstaDeepAI (Hugging Face model card); supports The nucleotide-transformer-v2-500m-multi-species model has 500 million parameters and was pre-trained on DNA sequences from many species and thousands of human genomes as stated in the model card facts., The model uses k-mer tokenization (6-mers when possible, fallback to single-nucleotide tokens) and has tokenizer configuration evidence for model_max_length=2048 in commit artifacts.
- [InstaDeepAI/nucleotide-transformer v2 500M commit (tokenizer/hyperparameter evidence)](https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/commit/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a) — InstaDeepAI (Hugging Face commit); supports Commit-level evidence documents tokenizer behavior and hyperparameters referenced in the model card for the v2-500M slug (tokenizer tokenization behavior and related config entries).
- [InstaDeepAI/nucleotide-transformer-v2-500m-multi-species README (alternate/commit path)](https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/6dee01f8296ecf6d25214526ecf940007cf5c2c9/README.md) — InstaDeepAI (Hugging Face README); supports An alternate README commit in the model repo reports a different pre-training sequence length in the findings (this reflects a commit-level inconsistency in the provided primary artifacts).
- [Nucleotide Transformer official GitHub repository](https://github.com/instadeepai/nucleotide-transformer) — InstaDeepAI (GitHub repository); supports Family-level statements about training-data composition (integration of many human genomes and many species) and family-level provenance present in the research findings.
- [Nucleotide Transformer v2 500M tokenizer config (commit file)](https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/commits/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/esm_config.py) — InstaDeepAI (Hugging Face commits); supports Commit artifacts in the model repo include tokenizer/model configuration and AutoModel entries referenced in the research findings.
- [HyenaDNA medium 450k model card](https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf) — LongSafari (Hugging Face model card); supports HyenaDNA-medium-450k-seqlen is documented as a long-range genomic foundation model with single-nucleotide character tokenizer support and training on next-nucleotide prediction on HG38 in the research findings., Model card facts document long-context claims (450k tokens for medium checkpoint; larger variants documented up to 1M tokens in the findings).
- [HyenaDNA tokenizer implementation (tokenization_hyena.py)](https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/5087bae36caee220a8f5e26b0f1f4b7571e5cd1a/tokenization_hyena.py) — LongSafari (tokenizer file in model repo); supports Tokenization implementation for HyenaDNA is present in the repository and documents single-nucleotide character-level tokenization and special tokens as noted in the research findings.
- [HyenaDNA tokenizer_config.json (model_max_length evidence)](https://huggingface.co/LongSafari/hyenadna-medium-450k-seqlen-hf/blob/e3c43387c1a5b546ff075d15e27d789fe749874b/tokenizer_config.json) — LongSafari (tokenizer config file); supports Tokenizer configuration sets model_max_length to 450002 and defines special tokens and tokenizer_class as documented in the research findings.
- [HyenaDNA academic PDF / HyenaDNA supplementary (context-length evidence)](https://arxiv.org/pdf/2306.15794) — HyenaDNA authors (academic PDF); supports HyenaDNA context-length capability of 450k–1M tokens is documented in the HyenaDNA academic PDF and supplementary experiment details per the research findings.
- [DNABERT-2 117M model card](https://huggingface.co/zhihan1996/DNABERT-2-117M) — zhihan1996 (Hugging Face model card); supports DNABERT-2-117M provides hidden states of dimension 768; mean-pooled or max-pooled embeddings therefore have shape (768) as reported in the research findings., The model can be loaded via Hugging Face AutoTokenizer/AutoModel with trust_remote_code per the research findings.
- [DNABERT-2 GitHub (training scripts and GUE description)](https://github.com/MAGICS-LAB/DNABERT_2) — MAGICS-LAB (GitHub repository); supports The DNABERT-2 repository includes references to the GUE benchmark and training scripts per the research findings.
- [DNABERT-2 LICENSE (Apache-2.0) in model repo](https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/refs%2Fpr%2F40/LICENSE) — zhihan1996 (Hugging Face repository file); supports The DNABERT-2-117M repository contains an Apache-2.0 LICENSE file as documented in the research findings.
- [Nucleotide Transformer v2 primary preprint / record (biorxiv/nature entries present in findings)](https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full-text) — bioRxiv (preprint); supports NT-v2 documentation in the research findings states context-length capability (12 kbp) for NT-v2 models and per-paper benchmark summaries referenced in the findings.
- [NT-v2 / related Nature record (NT-v2 context-length statement in findings)](https://nature.com/articles/s41592-024-02523-z) — Nature (paper record referenced in findings); supports NT-v2 context-length and benchmark summary statements appear in the Nature record as included in the research findings.
- [DNABERT-2 technical/summary PDF (DNABERT materials)](https://zhihan1996.github.io/data/dnaberts.pdf) — DNABERT authors (official PDF); supports DNABERT-2 is described and experimental settings referenced in DNABERT materials per the research findings.
- [PMCID article referencing DNABERT-S experiments (K=4 usage)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12663285) — PubMed Central (PMCID); supports The PMCID article in the research findings references DNABERT-S experiments and K selection usage as noted in the findings.

## Evidence gaps

- Evidence gap: Carbon‑3B — the provided research findings did not include a primary-source explicit LICENSE file URL for the exact HuggingFaceBio/Carbon-3B slug; the research findings state the model card lacked explicit license text in the reviewed primary sources.
- Evidence gap: Carbon‑3B embedding output schema — the research findings document Carbon primarily as a generative model and did not provide a canonical JSON embedding output shape or embedding dimensionality for Carbon-3B in the provided primary sources.
- Evidence gap: InstaDeep nucleotide-transformer v2 500M — the research findings did not include an explicit LICENSE file for the exact 500M slug; a different family member (v2-250M) had an Apache-2.0 LICENSE in the provided findings, producing license-provenance ambiguity for the 500M slug.
- Evidence gap: InstaDeep nucleotide-transformer v2 500M canonical JSON output schema — the research findings include commit-level embed_dim metadata but do not include a canonical JSON output schema for embeddings for the exact slug.
- Evidence gap: HyenaDNA medium 450k — the research findings did not provide a canonical single numeric embedding dimensionality or a canonical JSON embedding output shape for the exact LongSafari/hyenadna-medium-450k-seqlen-hf slug.
- Evidence gap: HyenaDNA medium 450k license — the research findings did not include an explicit LICENSE file URL for the exact LongSafari/hyenadna-medium-450k-seqlen-hf slug.
- Evidence gap: Exact versionKey/commit provenance for some slugs — the provided research findings include commit-level artifacts for some models but do not provide a complete, canonical mapping of every user-cited versionKey string to a single commit file for all four slugs; where an exact versionKey was cited by the user and not present in the findings, the dossier records an evidence gap.
- Evidence gap: Head-to-head primary-source evaluations among the four exact slugs — the research findings do not contain complete, matching primary-source artifacts that run the exact same protocol (dataset splits, tokenization, pooling, checkpoint/versionKey) across these exact four slugs; therefore direct performance ranking claims between these exact slugs are not supported by the provided primary evidence.
- Evidence gap: Tokenization k→base mapping protocol for cross-tokenization comparisons — although the findings document tokenization types for each slug (6-mer vs. single-nucleotide), the dossier did not find a primary-source canonical re-tokenization or mapping protocol that allows direct 6-mer ↔ single-nucleotide comparisons across the slugs in the provided findings.
- Evidence gap: Generative safety/biosecurity and misuse-mitigation text — for Carbon-3B, HyenaDNA medium 450k, and InstaDeep v2 500M the provided research findings did not include explicit safety or misuse-mitigation policy text tied to the exact slugs; absence of explicit biosecurity guidance in the provided primary sources is an evidence gap.
- Evidence gap: Exact maximal native context lengths for DNABERT-2-117M — the research findings do not provide a canonical maximum sequence length for the exact zhihan1996/DNABERT-2-117M slug beyond general benchmark usage references.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.

- `low` $.benchmarkTaxonomy_evidence: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
