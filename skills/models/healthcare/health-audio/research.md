# Health Audio model selection

- Category: `healthcare`
- Group: `health-audio`
- Independent audit: `revised`
- Researched: `2026-07-23T23:12:00.518782+00:00`

Health-audio task family covering: (a) health-acoustic embedding extraction for downstream research classifiers built on top of frozen embeddings; (b) zero-shot audio classification and text-audio retrieval based on contrastive language-audio pretraining; (c) supervised AudioSet multi-label tagging using AudioSet-fine-tuned classifier checkpoints; and (d) cough-related classification only when primary evidence explicitly documents downstream fine-tuning or evaluation protocols on cough datasets. Out of scope: unsupported clinical diagnostic claims, Forge runtime/serving contract claims derived from upstream docs, and checkpoint-transfer claims not verified for the exact listed candidate checkpoint.

## Questions to answer before selecting

- Do you need a health-acoustic embedding model whose primary evidence directly supports 2-second, 16 kHz inputs and frozen-embedding downstream evaluation?
- Do you need zero-shot audio classification or text-audio retrieval based on a CLAP-style shared latent space rather than a supervised classifier head?
- Do you need an exact AudioSet-fine-tuned supervised classifier checkpoint rather than a general embedding model?
- Is the intended cough task supported directly by the exact upstream checkpoint, or only by downstream fine-tuning workflows described in primary evidence?
- Must the evidence apply to the exact listed checkpoint page rather than to a broader model family or a different checkpoint variant?
- Are benchmark comparisons required to use the same dataset, split, preprocessing, clip duration, and evaluation head?
- Do you need primary evidence for output semantics such as embedding dimensionality or classification-score interpretation rather than inferring behavior from wrappers or third-party integrations?
- Are healthcare-use restrictions, research-only boundaries, or validation requirements from primary sources important for the deployment decision?

## Comparability rules

- Only compare benchmark values when the same task formulation is used: frozen-embedding (linear-probe) evaluation, zero-shot prompting, or supervised fine-tuned classification must not be mixed.
- Only compare results when the same dataset and exact split are used; if the split is not specified in the primary findings, treat the comparison as evidence-limited.
- Input preprocessing must match, including sample rate, channel conversion, fixed clip length or max audio length, and any spectrogram-based preprocessing when documented by the primary source.
- For embedding comparisons, pooling and output representation must be comparable; if embedding dimensionality or extraction protocol is undocumented for one side, treat direct numeric comparison as non-comparable.
- For zero-shot comparisons, prompt templates, tokenization, truncation, and label-mapping rules must match; if the exact checkpoint source does not specify these, treat the comparison as evidence-limited.
- For AudioSet tagging comparisons, exact checkpoint identity and whether the result is checkpoint-level or broader architecture-level must match; family-level AST or PANNs claims should not be treated as exact-checkpoint head-to-head evidence.
- Cough-task comparisons must state whether performance comes from the exact upstream checkpoint directly or from a separate downstream fine-tuning pipeline built on that model.
- Upstream model behavior evidence does not establish Forge runtime contract, wrapper validation, latency, or serving semantics.

## Conditional routing

### Prefer `google-hear-health-acoustic-embeddings` when Need health-acoustic embeddings for downstream research classifiers on short respiratory or biological sounds, and primary evidence must directly support 2-second audio inputs and frozen-embedding evaluation.

- Why: Primary HeAR sources identify HeAR as a health-acoustic representation model evaluated in frozen-embedding downstream settings on multiple health acoustic tasks. The Hugging Face model page and Google Health documentation identify HeAR as an embedding model for health acoustics; an arXiv HTML version of the HeAR paper reports evaluation on health datasets (including FSD50K and FluSense) and frozen-embedding downstream metrics. Note: there is an ambiguity in the primary findings about embedding dimensionality — an arXiv HTML source asserts a 512-dimensional output for 2-second, 16 kHz windows, while an arXiv abstract listing in the findings states the primary paper does not provide explicit numeric embedding-dimension details. Both primary locators are cited below.
- Alternative: laion-clap-htsat-fused-zero-shot-audio
- Alternative: panns-cnn14-audioset-cough
- Evidence: https://huggingface.co/google/hear, https://developers.google.com/health-ai-developer-foundations/hear, https://github.com/Google-Health/hear, https://arxiv.org/html/2403.02522v1, https://arxiv.org/abs/2403.02522, https://colab.research.google.com/github/google-health/hear/blob/master/notebooks/quick_start_with_hugging_face_pytorch.ipynb

### Prefer `laion-clap-htsat-fused-zero-shot-audio` when Need zero-shot audio classification or shared audio-text embeddings for retrieval or text-conditioned matching and the exact laion/clap-htsat-fused Hugging Face checkpoint evidence is acceptable for zero-shot or retrieval use.

- Why: The Hugging Face laion/clap-htsat-fused model page cites the CLAP line of work; the canonical CLAP paper (arXiv 2211.06687) reports zero-shot ESC-50 and related zero-shot classification/retrieval numbers in its Table 4, establishing CLAP-family zero-shot capability. The Hugging Face checkpoint page identifies the checkpoint as providing audio and text embeddings. The primary CLAP paper provides zero-shot ESC-50 numbers although checkpoint-to-checkpoint mapping for every named checkpoint file is not fully enumerated in the Hugging Face model page evidence in the findings.
- Alternative: google-hear-health-acoustic-embeddings
- Alternative: mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12
- Evidence: https://huggingface.co/laion/clap-htsat-fused, https://arxiv.org/html/2211.06687v4

### Prefer `mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12` when Need an explicit supervised AudioSet multi-label classifier checkpoint identified as fine-tuned on AudioSet and exact checkpoint identity matters.

- Why: The MIT/ast-finetuned-audioset-10-10-0.4593 Hugging Face model page in the findings identifies the checkpoint as an AST model fine-tuned on AudioSet, which supports selecting it when a supervised AudioSet checkpoint is required. The primary evidence in the findings supports checkpoint identity but does not provide checkpoint-specific numeric benchmark rows or split-level evaluation details in the collected sources.
- Alternative: google-hear-health-acoustic-embeddings
- Alternative: panns-cnn14-audioset-cough
- Evidence: https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

### Prefer `insufficient-evidence` when Need a model that is proven by primary sources to be an out-of-the-box cough classifier for Coswara or COUGHVID without additional downstream fine-tuning.

- Why: Primary PANNs sources in the findings document that CNN14 is an AudioSet-trained tagging model family with reported AudioSet mAP values and that separate downstream studies fine-tuned pretrained auditory models (including PANN-like backbones) for COVID-19/cough tasks. The findings do not establish that the exact upstream Forge-listed checkpoint is itself a cough-specific classifier without downstream fine-tuning.
- Alternative: panns-cnn14-audioset-cough
- Alternative: google-hear-health-acoustic-embeddings
- Alternative: mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12
- Alternative: laion-clap-htsat-fused-zero-shot-audio
- Evidence: https://github.com/qiuqiangkong/audioset_tagging_cnn, https://arxiv.org/pdf/1912.10211, https://arxiv.org/html/2511.14939v1

## Benchmark taxonomy

### Embedding representation for downstream health or clinical research classifiers

- Datasets: FSD50K, FluSense, CoughVID, Evidence gap: the primary HeAR findings mention 6 datasets and 33 tasks but do not enumerate all dataset names and splits
- Metrics: Mean reciprocal rank (MRR, higher is better), Average precision / mean average precision (AP / mAP, higher is better), Evidence-backed embedding dimensionality and extraction protocol
- Compare only when: Use frozen-embedding downstream evaluation (linear probe) rather than treating embedding model outputs as direct diagnostic classifier outputs.
- Compare only when: Match input duration and sample rate; HeAR primary evidence supports 2-second inputs and a 16 kHz sampling assumption in some primary locators.
- Compare only when: State downstream head explicitly when benchmarks required a linear probe or classifier on top of embeddings.

### Zero-shot audio classification and text-to-audio retrieval

- Datasets: ESC50, US8K, VGGSound, FSD50K
- Metrics: Zero-shot classification accuracy (higher is better), Retrieval metrics reported by the CLAP paper (e.g., recall/accuracy where reported)
- Compare only when: Use the exact CLAP checkpoint and the same zero-shot prompt/template and label-mapping rules; if the exact checkpoint's prompt/label-mapping is undocumented, treat result comparisons as evidence-limited.
- Compare only when: Match audio preprocessing (sample rate, clip length) to the primary CLAP evaluation protocol.

### Supervised AudioSet multi-label tagging

- Datasets: AudioSet
- Metrics: Mean average precision (mAP, higher is better)
- Compare only when: Use the same AudioSet evaluation protocol and checkpoint identity; do not transfer family-level architecture numbers to an exact-checkpoint claim without a matching primary locator.

### Cough detection or cough-related classification

- Datasets: Coswara, COUGHVID, Evidence gap: no canonical common split definition across candidates in primary findings
- Metrics: AUROC / AUC-ROC (higher is better), F1-score (higher is better), Accuracy (higher is better)
- Compare only when: State whether the reported metric is produced by the upstream checkpoint alone or by a downstream fine-tuning pipeline; for cough tasks in the findings, metrics originate from downstream fine-tuning in cited studies.
- Compare only when: Match dataset split, stratification, and preprocessing; when not specified in primary sources, treat comparisons as evidence-limited.

## Primary sources

- [google/hear model page](https://huggingface.co/google/hear) — Hugging Face / Google; supports Exact official starting source for google-hear-health-acoustic-embeddings., HeAR is a health acoustic representation model exposed on Hugging Face as an embedding model., HeAR model page is the canonical Hugging Face locator for the google/hear checkpoint cited in the findings.
- [HeAR developer overview / model card](https://developers.google.com/health-ai-developer-foundations/hear) — Google Health / Developers; supports Official Google Health developer overview and model-card locator for HeAR and its intended research-use framing., HeAR is presented as a health-acoustic embeddings resource in Google developer documentation referenced in the findings.
- [Google-Health/hear repository](https://github.com/Google-Health/hear) — Google Health / GitHub; supports Supporting code repository for HeAR and a canonical upstream code locator for the model and examples., Repository-level statements in the findings that HeAR code is hosted at this GitHub location and that HeAR training used large numbers of two-second clips.
- [HeAR paper (arXiv abstract)](https://arxiv.org/abs/2403.02522) — arXiv; supports Primary HeAR paper locator (arXiv:2403.02522) referenced in the findings., The arXiv abstract locator in the findings is used to support publication identity and high-level claims.
- [HeAR paper (arXiv HTML with benchmark tables)](https://arxiv.org/html/2403.02522v1) — arXiv; supports arXiv HTML locator cited in the findings that contains benchmark tables and claims (e.g., HeAR mAP and AP numbers on FSD50K + FluSense and task-level APs reported in the findings)., This locator is the primary source for the numeric HeAR benchmark rows included in the findings (e.g., combined FSD50K+FluSense mAP 0.658, task APs for breathing and cough).
- [laion/clap-htsat-fused model page](https://huggingface.co/laion/clap-htsat-fused) — Hugging Face / LAION; supports Exact official starting source for laion-clap-htsat-fused-zero-shot-audio., This Hugging Face model page is the canonical locator for the laion/clap-htsat-fused checkpoint referenced in the findings.
- [CLAP paper (arXiv HTML with Table 4)](https://arxiv.org/html/2211.06687v4) — arXiv; supports Primary CLAP paper (arXiv:2211.06687) HTML/Tables locator included in the findings; Table 4 provides CLAP zero-shot ESC-50 and related zero-shot numbers that establish CLAP-family zero-shot performance in the findings., This paper is the canonical primary publication for CLAP-family benchmark claims cited in the findings.
- [MIT/ast-finetuned-audioset-10-10-0.4593 model page](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) — Hugging Face / MIT; supports Exact official starting source for mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12., This Hugging Face page identifies the exact AST checkpoint named in the Forge candidate list as fine-tuned on AudioSet.
- [AudioSet Tagging CNN repository](https://github.com/qiuqiangkong/audioset_tagging_cnn) — Qiuqiang Kong / GitHub; supports Exact official starting source for panns-cnn14-audioset-cough in the findings (AudioSet Tagging CNN repository)., Repository-level evidence in the findings that CNN14 is an AudioSet-trained tagging model family and that AudioSet mAP values are reported by the repository and associated paper.
- [PANNs paper (arXiv PDF)](https://arxiv.org/pdf/1912.10211) — arXiv; supports Primary PANNs paper locator cited in the findings containing reported AudioSet mAP values for CNN14 and sampling-rate comparisons referenced in the findings., Canonical primary publication for PANNs family benchmark claims included in the findings.
- [Fine-tuning Pre-trained Audio Models for COVID-19 (arXiv locator)](https://arxiv.org/html/2511.14939v1) — arXiv; supports A primary study cited in the findings that fine-tuned pretrained audio models (PANN-like backbones) for COVID-19/cough tasks; used in the findings to establish that cough-task metrics cited are downstream fine-tuning results rather than upstream out-of-the-box checkpoint behavior., Source for downstream fine-tuning provenance of cough-task evaluations referenced in the findings.
- [HeAR quick start Colab (example)](https://colab.research.google.com/github/google-health/hear/blob/master/notebooks/quick_start_with_hugging_face_pytorch.ipynb) — HeAR / Colab locator; supports Colab notebook in the findings demonstrating HeAR encoder usage and showing processing of 2-second audio sampled at 16 kHz in an example., Used in the findings to support the 2-second, 16 kHz preprocessing claim for HeAR examples.

## Evidence gaps

- Evidence gap: The HeAR primary abstract locator (arXiv:2403.02522) in the findings includes an ambiguity about embedding dimensionality: an arXiv HTML locator in the findings asserts a 512-dimensional output while an arXiv abstract locator in the findings also states the paper does not provide explicit numeric embedding-dimension details. This dimensionality ambiguity must be resolved by the dossier builder or marked as an unresolved evidence gap.
- Evidence gap: The Hugging Face HeAR model card in the findings lacks explicit preprocessing details such as required mono/stereo channel format, normalization steps, or pooling method; the findings include a Colab example showing 2-second 16 kHz usage but do not provide comprehensive preprocessing contract.
- Evidence gap: The HeAR primary findings report many benchmark results across 33 tasks and 6 datasets but do not enumerate all dataset names and split identifiers in the collected primary locators; exact dataset split names are not fully specified in the primary findings.
- Evidence gap: The CLAP primary paper provides zero-shot numbers in Table 4, but the findings do not fully link every named checkpoint file on external repositories to the exact Hugging Face laion/clap-htsat-fused checkpoint; checkpoint-to-checkpoint numeric mapping is incomplete in the findings.
- Evidence gap: The MIT AST Hugging Face checkpoint is identified as fine-tuned on AudioSet in the findings, but the findings do not provide checkpoint-specific numeric AudioSet mAP rows, split names, or full preprocessing details for strict numeric comparison.
- Evidence gap: The PANNs findings support AudioSet mAP values for CNN14 and cite downstream fine-tuning for cough tasks, but do not show that the exact Forge-listed upstream checkpoint is a cough-specific classifier without additional downstream training; cough metrics are documented as downstream fine-tuning in the findings.
- Evidence gap: No single primary source in the findings provides head-to-head numeric comparisons across all four listed candidates on one shared health-audio protocol with matching splits, preprocessing, and head; a clean cross-model clinical-environment benchmark is absent in the findings.
- Evidence gap: The primary findings do not provide Forge-specific runtime metadata, request schema, wrapper validation behavior, latency, or serving semantics; these remain evidence gaps for Forge integration.
- Evidence gap: The primary findings do not fully specify all dataset splits, averaging conventions, determinism settings, or hyperparameter parity needed for strict numeric comparison across candidates; these protocol-level details are absent in the collected primary locators.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
