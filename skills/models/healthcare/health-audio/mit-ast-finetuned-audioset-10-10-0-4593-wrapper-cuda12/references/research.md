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

- Research key: `huggingface-co-mit-ast-finetuned-audioset-10-10-0-4593-33830cdbc6`
- Independent audit: `revised`
- Researched: `2026-08-06T08:56:30.661691+00:00`

Primary canonical sources examined: the AST arXiv preprint and HTML (reports of AudioSet experimental results including ensemble and weight‑averaged variants), the upstream YuanGongND/ast GitHub repository (implementation, experiment outputs, and checkpoint filenames), the AST model file that documents a pre-trained checkpoint named audioset_10_10_0.4593.pth, the repository README (experiment summaries and sampling rate), and the Hugging Face model card for MIT/ast-finetuned-audioset-10-10-0.4593 (hosting metadata and license). The AST paper reports ensemble/aggregate AudioSet results up to mAP = 0.485 (reported as Ensemble‑M) and reports other benchmarks (ESC‑50, Speech Commands). The upstream repository reports a weight‑averaged single model mAP = 0.459 (and records a pre-trained checkpoint file audioset_10_10_0.4593.pth described as achieving 0.4593 mAP in src/models/ast_models.py). The repository and code document implementation defaults including 16 kHz sampling for experiments and implementation-level input shapes/examples; explicit checkpoint parameter counts, revision hashes for the hosted HF checkpoint, canonical accepted container formats/bit depths, and inference segmentation policies for inputs longer than the evaluation length are not reported in the supplied primary sources and are recorded as evidence gaps where indicated.

## Identity

- Upstream name: MIT/ast-finetuned-audioset-10-10-0.4593
- Checkpoint/version: MIT/ast-finetuned-audioset-10-10-0.4593
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Audio Spectrogram Transformer (AST): a ViT‑style transformer applied to spectrogram patches with a class token, positional embedding, transformer blocks, and a final MLP/classification head (pure attention, convolution‑free).
- License: BSD-3-Clause
- Evidence: https://arxiv.org/pdf/2104.01778, https://ar5iv.labs.arxiv.org/html/2104.01778, https://github.com/YuanGongND/ast, https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://github.com/YuanGongND/ast/blob/master/README.md, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

## Selection

### Recommended

- **Multi-label audio classification / sound‑event tagging on AudioSet‑style tasks** — AST architecture and multi‑label AudioSet experiments are documented in the AST paper and the upstream repository; the upstream repository provides pretrained/weight‑averaged variants reported on AudioSet and the Hugging Face model card hosts a checkpoint labeled as AST fine‑tuned on AudioSet.
  Scope: AST family models fine‑tuned on AudioSet (family/variant‑level evidence; direct one‑to‑one provenance to the exact HF checkpoint name is not established in the supplied primary sources).
  Evidence: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

### Conditional

- **Domain‑specific supervised fine‑tuning / transfer learning for downstream audio classification** — Requires held‑out labeled domain data, standard fine‑tuning validation, and downstream evaluation; validate performance on domain test sets before deployment and follow repository fine‑tuning procedures.
  Scope: Upstream AST implementation and variants documented in the YuanGongND/ast repository (family/variant‑level evidence; no single canonical locator in the supplied findings proving the named HF checkpoint equals a specific repository variant).
  Evidence: https://github.com/YuanGongND/ast, https://arxiv.org/pdf/2104.01778

### Avoid

- **Clinical‑grade diagnostic decision making based solely on model outputs** — Primary canonical sources document training and evaluation on AudioSet and do not provide primary‑source clinical validation or regulatory clearance for AST checkpoints; the supplied primary sources do not present clinical‑validation evidence tying AST checkpoints to diagnostic use.
  Scope: MIT/ast-finetuned-audioset-10-10-0.4593 (checkpoint as named; no primary clinical‑validation provenance found in the supplied sources)
  Evidence: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593
- **Zero‑shot text‑conditioned / CLAP‑style cross‑modal zero‑shot classification using this checkpoint without additional components** — Upstream AST artifacts and repository document supervised finetuning on AudioSet and do not provide primary‑source evidence of CLAP‑style zero‑shot capability for these AST checkpoints in the supplied findings.
  Scope: MIT/ast-finetuned-audioset-10-10-0.4593
  Evidence: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast

## Input preparation

### Semantic inputs

- Upstream implementation and model experiments operate from spectrogram/feature tensors derived from raw audio; repository examples show input tensors of shape (batch_size, time_frames, frequency_bins), e.g., (12, 1024, 128). Sources: https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://github.com/YuanGongND/ast
- Upstream experiments use 16 kHz audio sampling for training and evaluation as documented in the upstream repository. Sources: https://github.com/YuanGongND/ast, https://github.com/YuanGongND/ast/blob/master/README.md
- The Hugging Face model card identifies the hosted checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 as an AST variant fine‑tuned on AudioSet (model hosting identity). Sources: https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

### Accepted formats

- Primary sources express the input contract at the spectrogram/feature‑tensor level (input_fdim=128, input_tdim examples) rather than enumerating a canonical set of audio container file types and bit depths; explicit accepted container types and bit‑depths are not specified in the supplied findings. Sources: https://github.com/YuanGongND/ast, https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593
- Evidence gap: The supplied primary findings do not provide an explicit, canonical list of accepted audio container/file types (WAV, FLAC, MP3, OGG) or recommended bit‑depth for the named HF checkpoint. Sources: https://github.com/YuanGongND/ast, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

### Preprocessing

- Repository and related upstream code examples document input feature dimensions and patching defaults: input_fdim = 128 and input_tdim = 1024 are used as feature/tensor examples in the implementation; SSAST related repository configuration also lists input_fdim = 128, input_tdim = 1024, fstride = 10, tstride = 10, fshape = 16, tshape = 16 for default configurations. Sources: https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://github.com/YuanGongND/ssast
- Upstream repository and AST paper describe patching/transformer input processing consistent with converting spectrogram patches into embeddings for the ViT‑style transformer pipeline; the repository constructor arguments and defaults implement these conventions. Sources: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast
- Training‑time augmentations referenced in the upstream repository include mixup and spectrogram masking as documented in the repository's experiment descriptions. Sources: https://github.com/YuanGongND/ast
- Evidence gap: The supplied primary findings do not specify window length and hop in milliseconds (e.g., explicit STFT window/hop ms values) for spectrogram computation; this sampling‑to‑frame conversion detail is not verifiable from the supplied findings. Sources: https://github.com/YuanGongND/ast, https://arxiv.org/pdf/2104.01778

### Pre-submit validation

- Validate that input audio is converted to the repository/implementation feature format (input_fdim=128 and expected input_tdim examples) and sampled at 16 kHz to match upstream experiments; ensure spectrogram tensor shape matches model constructor examples before inference. Sources: https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://github.com/YuanGongND/ast
- The upstream repository documents experiment result storage and weight‑averaging outputs: per‑epoch results are saved under ast/egs/audioset/exp/yourexpname/result.csv and a weighted‑averaged model's results are saved in wa_result.csv; use these artifacts to verify reproduced experiment metrics. Sources: https://github.com/YuanGongND/ast
- The upstream repository documents spectrogram normalization guidance (the supplied findings reference a repository normalization formula and guidance). Sources: https://github.com/YuanGongND/ast
- Evidence gap: An explicit canonical inference‑time segmentation/cropping policy for inputs longer than the evaluation length (e.g., >10 s) tied to the named Hugging Face checkpoint is not provided in the supplied primary findings. Sources: https://github.com/YuanGongND/ast, https://arxiv.org/pdf/2104.01778

### Task-specific formatting

- AST checkpoints are applied for multi‑label audio classification: spectrogram tensors are split into patches and fed through the transformer; a final classification head (linear/MLP head) consumes the transformer's pooled / class token output to produce per‑class logits. No prompt or paired‑input templates are defined in the supplied findings. Sources: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

## Output interpretation

### Outputs

- The model's final classification layer is a linear/MLP head producing per‑class raw logits (implementation and paper documentation indicate a classification head on pooled/class token outputs). Sources: https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py, https://arxiv.org/pdf/2104.01778

### Interpretation

- Upstream artifacts document training with binary cross‑entropy loss for multi‑label classification; this supports interpreting raw logits with a per‑class sigmoid for multi‑label outputs. The supplied primary findings do not provide checkpoint‑specific calibrated probability thresholds; downstream calibration is required for decision thresholds. Sources: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py
- Evidence gap: The supplied primary findings do not report recommended calibrated decision thresholds or a checkpoint‑specific post‑processing calibration procedure for the named Hugging Face checkpoint. Sources: https://github.com/YuanGongND/ast, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593

### Post-inference validation

- Post‑inference validation should include downstream calibration and threshold selection on held‑out labeled data; upstream primary sources in the supplied findings do not prescribe specific numeric thresholds tied to the checkpoint. Sources: https://github.com/YuanGongND/ast, https://arxiv.org/pdf/2104.01778
- Evidence gap: Exact numeric mean/std values for any additional inference normalization beyond the repository's spectrogram normalization guidance are not separately enumerated for the named Hugging Face checkpoint in the supplied findings. Sources: https://github.com/YuanGongND/ast

## Public benchmarks

### AudioSet multi‑label classification

- Dataset/split: AudioSet (full evaluation set) / evaluation set
- Metric/value: mean average precision (mAP) / 0.485 (`higher-is-better`)
- Model scope: AST (paper‑reported Ensemble‑M aggregate/ensemble variant as reported in the AST paper)
- Conditions: Paper experimental protocol as reported in the AST paper (ensemble/aggregate evaluation reported by authors); attribution is to the paper's reported Ensemble‑M result, not to a specific Hugging Face checkpoint identifier.
- Source: https://arxiv.org/pdf/2104.01778
- Locator: AST paper — arXiv PDF experimental results reporting Ensemble‑M (multiple‑model ensemble) achieves mAP = 0.485 on AudioSet (as reported in the paper's experimental results section; exact table/figure number not provided in the supplied findings).
- Caveat: The supplied primary findings do not include an exact table/figure number or page locator for the reported 0.485 value; the paper result is treated as a family/variant‑level reported ensemble result in the absence of an explicit mapping to the HF checkpoint name.

### AudioSet multi‑label classification

- Dataset/split: AudioSet (full evaluation set) / evaluation set
- Metric/value: mean average precision (mAP) / 0.459 (`higher-is-better`)
- Model scope: Upstream AST repository weight‑averaged single model variant (repository‑reported single model mAP / pre‑trained checkpoint audioset_10_10_0.4593.pth)
- Conditions: Repository experiment summaries and model artifact naming indicate a weight‑averaging procedure producing a single model reported with mAP ≈ 0.459; attribution is to the upstream repository's reported single‑model variant.
- Source: https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py
- Locator: GitHub — src/models/ast_models.py and README/experiment outputs: pre‑trained checkpoint file named audioset_10_10_0.4593.pth is documented as achieving 0.4593 mAP; repository README and repo experiment output file paths (e.g., ast/egs/audioset/exp/yourexpname/result.csv and wa_result.csv) are used to record experiment metrics.
- Caveat: The supplied findings show the repository reports a weight‑averaged single model mAP = 0.459 and identify a checkpoint filename audioset_10_10_0.4593.pth, but they do not provide a canonical single‑source statement that maps the exact Hugging Face hosted checkpoint name to a unique repository commit/revision; therefore the numeric value is treated as repository‑reported family/variant evidence.

## Comparisons

### google-hear-health-acoustic-embeddings — `insufficient-evidence`

- Task: Health‑audio embeddings / downstream health‑audio tasks
- Criteria: No primary‑source, protocol‑matched head‑to‑head evaluation (same dataset/split, preprocessing, explicit checkpoint identifiers, and metric) between the exact named checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 and the alternative is present in the supplied findings.
- Rationale: AST artifacts document supervised AudioSet training and reported mAPs; the supplied findings do not include a protocol‑matched comparison using explicit checkpoint identifiers for both sides.
- Comparison conditions: Protocol‑matched comparison would require identical preprocessing, identical dataset/split definitions, explicit checkpoint identifiers for both models, and the same metric definitions; these are not present in the supplied findings.
- Evidence: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast

### laion-clap-htsat-fused-zero-shot-audio — `insufficient-evidence`

- Task: Zero‑shot audio classification (CLAP‑style) vs supervised AST
- Criteria: No protocol‑matched, checkpoint‑specific head‑to‑head comparison between MIT/ast-finetuned-audioset-10-10-0.4593 and CLAP/zero‑shot methods on the same dataset/split/metric is present in the supplied findings.
- Rationale: AST artifacts describe supervised task tuning on AudioSet; the supplied findings do not include CLAP‑style zero‑shot evaluations for the AST checkpoint.
- Comparison conditions: Matching would require explicit checkpoint identifiers and zero‑shot protocol details with identical preprocessing and metric; these are not available in the supplied findings.
- Evidence: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast

### panns-cnn14-audioset-cough — `insufficient-evidence`

- Task: Cough / health‑audio detection vs AST‑based classifier
- Criteria: No protocol‑matched, checkpoint‑specific head‑to‑head comparison between MIT/ast-finetuned-audioset-10-10-0.4593 and PANNs CNN14 on the same dataset/split/metric is present in the supplied findings.
- Rationale: Baselines may be referenced in literature, but the supplied primary findings do not provide a protocol‑matched comparison tying the exact HF checkpoint to the named alternatives.
- Comparison conditions: Comparability would require identical preprocessing, dataset/split and explicit checkpoint identifiers for both models; these are not present in the supplied findings.
- Evidence: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast

## Limitations and safety

### Limitations

- The AST model and upstream experiments are trained and evaluated on AudioSet; generalization to out‑of‑distribution audio (including clinical audio) is not established by the supplied primary artifacts. Sources: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast
- Primary sources document differing numeric aggregates across AST variants (paper ensembles vs upstream repository single/weight‑averaged models); the supplied findings do not provide a single canonical locator that unambiguously ties a paper table row or repository variant to the exact Hugging Face checkpoint name, creating ambiguity for checkpoint‑specific benchmark attribution. Sources: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast, https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py
- Evidence gap: The exact parameter count for the named Hugging Face checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 is not reported in the supplied primary findings. Sources: https://github.com/YuanGongND/ast, https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593, https://arxiv.org/pdf/2104.01778

### Safety

- Primary canonical sources document training and evaluation on AudioSet and do not present primary‑source clinical validation or regulatory clearance for AST checkpoints; health/clinical uses require expert review and formal clinical validation before diagnostic use. Sources: https://arxiv.org/pdf/2104.01778, https://github.com/YuanGongND/ast
- Evidence gap: The supplied primary findings do not provide checkpoint‑specific guidance on handling sensitive clinical data (PHI) or institution‑specific data governance for the named Hugging Face checkpoint; apply institutional and regulatory data‑handling controls when using the model with clinical audio.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### AST: Audio Spectrogram Transformer — arXiv PDF

- URL: https://arxiv.org/pdf/2104.01778
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing the AST architecture and reporting AudioSet experimental results (ensemble and single‑model reported mAPs) used in this dossier.
- Scope: AST paper (architectural and experimental claims; reported AudioSet mAP values including Ensemble‑M = 0.485 and weight‑averaged single‑model statements at paper level)
- Supports: Reported AudioSet mAP = 0.485 (Ensemble‑M reported in experimental results)
- Supports: Architecture description of AST as a transformer over spectrogram patches (pure attention)
- Supports: Paper‑level description of AST experimental evaluations on AudioSet, ESC‑50, and Speech Commands

### AST: Audio Spectrogram Transformer — ar5iv HTML

- URL: https://ar5iv.labs.arxiv.org/html/2104.01778
- Publisher: ar5iv (arXiv HTML mirror)
- Type: `paper`
- Primary because: HTML representation of the AST preprint included in the supplied findings set; supports the same paper claims as the arXiv PDF.
- Scope: AST paper HTML mirror (alternate representation of the same preprint content used in supplied findings)
- Supports: Reported AudioSet mAP = 0.485 (Ensemble‑M reported in experimental results)
- Supports: Other experimental metrics reported in the AST paper

### AST upstream repository — YuanGongND (GitHub)

- URL: https://github.com/YuanGongND/ast
- Publisher: YuanGongND (GitHub)
- Type: `repository`
- Primary because: Upstream implementation repository documenting pretrained model variants, default constructor parameters, experiment result storage paths, and reported weight‑averaged single model mAP used in this dossier.
- Scope: AST upstream repository (implementation, defaults, pretrained model filenames, and experiment reporting including weight‑averaged single model mAP ≈ 0.459 and experiment result file locations)
- Supports: Repository reports weight‑averaged single model mAP ≈ 0.459 (experiment/README and code comments)
- Supports: Implementation examples and defaults; experiment result file locations (ast/egs/audioset/exp/yourexpname/result.csv and wa_result.csv)
- Supports: All experiments use 16 kHz sampling as stated in the repository

### AST repository README — YuanGongND (GitHub)

- URL: https://github.com/YuanGongND/ast/blob/master/README.md
- Publisher: YuanGongND (GitHub)
- Type: `repository`
- Primary because: Repository README included in the supplied findings documenting experiment summaries and stated sampling rate and ensemble/single‑model experiment notes.
- Scope: AST upstream repository README (experiment summary and sampling/experiment notes)
- Supports: All experiments in the repository use a 16 kHz audio sampling rate
- Supports: Repository README documents ensemble results and weight‑averaged single model summaries

### AST implementation — src/models/ast_models.py

- URL: https://github.com/YuanGongND/ast/blob/master/src/models/ast_models.py
- Publisher: YuanGongND (GitHub)
- Type: `repository`
- Primary because: Implementation source file in the upstream repository that documents input tensor shapes, architecture components, and references a pre‑trained checkpoint filename and its reported mAP used in the supplied findings.
- Scope: AST implementation file documenting model input shape examples and pre‑trained checkpoint filename audioset_10_10_0.4593.pth
- Supports: ASTModel expects input tensors of shape (batch_size, time_frames, frequency_bins) e.g., (12, 1024, 128)
- Supports: The pre‑trained checkpoint file audioset_10_10_0.4593.pth is documented as achieving 0.4593 mAP on the AudioSet evaluation set
- Supports: Model architecture components (patch embedding, class token, transformer blocks, MLP head) are documented

### SSAST repository — YuanGongND (GitHub)

- URL: https://github.com/YuanGongND/ssast
- Publisher: YuanGongND (GitHub)
- Type: `repository`
- Primary because: SSAST repository supplies configuration defaults (input_fdim, input_tdim, fstride, tstride, fshape, tshape) referenced in the supplied findings and used to corroborate implementation defaults.
- Scope: SSAST repository configuration examples (default config values referenced in supplied findings)
- Supports: SSAST defines input_fdim = 128, input_tdim = 1024, fstride = 10, tstride = 10, fshape = 16, tshape = 16 for default configuration

### Hugging Face model card — MIT/ast-finetuned-audioset-10-10-0.4593

- URL: https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593
- Publisher: Hugging Face
- Type: `official-documentation`
- Primary because: Canonical hosting page for the exact checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 included in the supplied findings; documents model identity and license metadata.
- Scope: Hugging Face model card for the exact checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 (hosting and model identity and license)
- Supports: Presence and hosting of the named checkpoint MIT/ast-finetuned-audioset-10-10-0.4593
- Supports: Model card metadata including license listed as BSD‑3‑Clause and statement that the model is fine‑tuned on AudioSet

### arXiv help — license information

- URL: https://info.arxiv.org/help/license/index.html
- Publisher: arXiv
- Type: `official-documentation`
- Primary because: arXiv help/license page included in the supplied findings set and used as a canonical reference for arXiv distribution/licensing context.
- Scope: arXiv distribution/license help page (used only to indicate possible arXiv distribution/licensing formats in the supplied findings)
- Supports: Reference information about possible distribution licenses for arXiv preprints (contextual/legal guidance)

## Evidence gaps

- Evidence gap: A single canonical mapping in the supplied findings that ties the AST paper's reported ensemble mAP = 0.485 or any specific paper table row directly to the Hugging Face checkpoint name MIT/ast-finetuned-audioset-10-10-0.4593 is not provided in the supplied primary findings.
- Evidence gap: Exact parameter count (number of model parameters) for the specific Hugging Face checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 is not reported in the supplied primary findings.
- Evidence gap: Canonical statement of accepted audio container/file types and recommended bit‑depth (WAV/FLAC/MP3/OGG and bit depth) for the named checkpoint is not provided in the supplied primary findings.
- Evidence gap: Explicit inference‑time segmentation/cropping policy for inputs longer than the evaluation length (e.g., >10 s) tied to the named Hugging Face checkpoint is not provided in the supplied primary findings.
- Evidence gap: Canonical upstream‑specified calibrated probability thresholds or checkpoint‑specific decision rules for binary classification are not provided in the supplied primary findings.
- Evidence gap: Exact canonical repository commit hash or revision identifier tying the pre‑trained checkpoint filename audioset_10_10_0.4593.pth to the Hugging Face hosted checkpoint name is not provided in the supplied primary findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses unapproved repository owner 'audioset' for this exact model scope: $.sources[5] uses unapproved repository owner 'audioset' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'syamaner' for this exact model scope: $.sources[10] uses unapproved repository owner 'syamaner' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'vladimirlv' for this exact model scope: $.sources[11] uses unapproved repository owner 'vladimirlv' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://rocm.blogs.amd.com/artificial-intelligence/speech_models/README.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://rocm.blogs.amd.com/artificial-intelligence/speech_models/README.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/mit-ast-finetuned-audioset-10-10-0.448-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
