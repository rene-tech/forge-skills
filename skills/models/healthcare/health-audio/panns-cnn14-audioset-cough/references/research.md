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

- Research key: `github-com-qiuqiangkong-audioset-tagging-cnn-7d9dedc059`
- Independent audit: `revised`
- Researched: `2026-07-23T23:30:20.275811+00:00`

Using only the provided primary-source findings, the canonical PANNs paper (arXiv:1912.10211) reports the CNN14 audio-tagging system achieving mAP=0.431 under a hop-size experimental configuration (see Table VI / Table IV). The author's panns_inference repository README references a local checkpoint path /root/panns_data/Cnn14_mAP=0.431.pth and shows example class-confidence outputs. The audioset_tagging_cnn repository README lists additional checkpoint filenames (e.g., Cnn14_16k_mAP=0.438.pth and Cnn14_DecisionLevelMax_mAP=0.385.pth) and inference parameter example values (sample_rate=16000, window_size=512, hop_size=160, mel_bins=64, fmin=50, fmax=8000). The repository contains an MIT license file at the documented path. Primary-source materials checked do not provide author-specified per-class decision thresholds, an exact dataset split identifier for the reported mAP, explicit numeric embedding tensor shape tied to the named checkpoint, nor the precise model implementation file locators for spectrogram/log-mel instantiation in the findings; these are recorded as evidence gaps where required.

## Identity

- Upstream name: Cnn14 (PANNs CNN14)
- Checkpoint/version: Cnn14_mAP=0.431.pth
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: CNN14 (14-layer convolutional CNN as reported for PANNs CNN14)
- License: MIT (repository LICENSE.MIT)
- Evidence: https://arxiv.org/pdf/1912.10211, https://github.com/qiuqiangkong/panns_inference/blob/master/README.md, https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/LICENSE.MIT

## Selection

### Recommended

- **Clip-level multi-label audio tagging with AudioSet ontology labels (AudioSet-like classes)** — The PANNs paper evaluates CNN14 on AudioSet and reports clipwise mAP; the author's panns_inference README demonstrates inference examples that output per-class confidences for a Cnn14 checkpoint.
  Scope: Cnn14_mAP=0.431.pth (CNN14 as reported in the PANNs paper and referenced by panns_inference examples)
  Evidence: https://arxiv.org/pdf/1912.10211, https://github.com/qiuqiangkong/panns_inference/blob/master/README.md, https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md
- **Using CNN14 variants as pretrained feature extractors / embedding providers for downstream audio tasks** — The PANNs paper positions PANNs as pretrained models for audio pattern recognition tasks, and the author's inference examples demonstrate extracting per-class confidences from the model checkpoint artifact.
  Scope: Cnn14 variants (checkpoints referenced in author's repositories)
  Evidence: https://arxiv.org/pdf/1912.10211, https://github.com/qiuqiangkong/panns_inference/blob/master/README.md

### Conditional

- **Frame-wise sound event detection using a DecisionLevel-trained checkpoint** — Require explicit confirmation of using a DecisionLevel-trained checkpoint (e.g., Cnn14_DecisionLevelMax_mAP=0.385.pth) from the repository before use; validate frame-wise behavior via the author's provided SED examples or scripts if available.
  Scope: Cnn14_DecisionLevelMax_mAP=0.385.pth (repository-named DecisionLevel checkpoint)
  Evidence: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md

### Avoid

- **Clinical diagnosis, PHI-sensitive decisioning, or healthcare deployment without separate validation** — Primary sources (paper and repository files checked) do not provide clinical validation statements, PHI handling guidance, or healthcare deployment approvals for the checkpoint; repository and paper describe audio tagging on AudioSet but do not include clinical-use validation.
  Scope: Cnn14_mAP=0.431.pth (and other Cnn14 checkpoints)
  Evidence: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://arxiv.org/pdf/1912.10211
- **Any task requiring author-provided per-class calibrated decision thresholds** — Primary sources do not provide recommended per-class thresholds or calibration parameters; only aggregate metrics (mAP) and example raw/confidence outputs are present in the checked locations.
  Scope: Cnn14_mAP=0.431.pth
  Evidence: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://arxiv.org/pdf/1912.10211

## Input preparation

### Semantic inputs

- Monophonic audio waveform intended for clip-level multi-label tagging (examples and paper discuss ~10-second inputs in evaluation context). Sources: https://arxiv.org/pdf/1912.10211, https://github.com/qiuqiangkong/panns_inference/blob/master/README.md

### Accepted formats

- Inference examples and repository example commands use audio sampled at 16000 Hz for the 16 kHz model variant (sample_rate=16000). Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://github.com/qiuqiangkong/panns_inference/blob/master/README.md
- Primary sources do not specify container/codec/bit-depth constraints in the checked files. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md

### Preprocessing

- Repository README example inference parameter values: sample_rate=16000, window_size=512, hop_size=160, mel_bins=64, fmin=50, fmax=8000. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md
- Panns_inference README references the CNN14 checkpoint path used for inference examples (implying the example preprocessing pipeline used by the example). Sources: https://github.com/qiuqiangkong/panns_inference/blob/master/README.md
- Evidence gap: The exact spectrogram/log-mel instantiation parameters (n_fft/window_size relationship, win_length, window type, center, pad_mode, ref/amin/top_db) as implemented in models.py were not present in the provided findings; no models.py file facts were available in the research findings to verify code-level instantiation.

### Pre-submit validation

- Primary sources do not provide explicit min/max input-duration validation bounds, cropping/truncation rules, or batching guidance in the checked README and paper. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://arxiv.org/pdf/1912.10211
- Repository issue evidence indicates checkpoint-to-code compatibility must be validated before loading some checkpoints (see reported pretrained Cnn14 16kHz wrong shape errors). Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/issues/18

### Task-specific formatting

- Multi-label outputs correspond to AudioSet ontology classes; repository README and panns_inference examples reference AudioSet labels and show example class-confidence outputs. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://github.com/qiuqiangkong/panns_inference/blob/master/README.md
- Evidence gap: An explicit mapping file (class index → class name) within the checked repository files was not identified in the provided findings.

## Output interpretation

### Outputs

- Inference examples in the author's panns_inference README present per-class confidence values (example confidences shown) produced by the referenced Cnn14 checkpoint path. Sources: https://github.com/qiuqiangkong/panns_inference/blob/master/README.md
- Evidence gap: The checked findings did not include the exact model implementation file lines or function names that label outputs (e.g., explicit 'clipwise_output' identifier) or a documented numeric embedding tensor shape tied to the Cnn14_mAP=0.431.pth checkpoint.

### Interpretation

- The PANNs paper uses mean average precision (mAP) as the aggregate evaluation metric for clipwise tagging and reports per-model mAP values (e.g., CNN14 mAP=0.431 under a hop-size configuration). Sources: https://arxiv.org/pdf/1912.10211

### Post-inference validation

- Primary sources do not provide author-recommended decision thresholds or per-class calibration guidance; use-case deployment requires downstream validation and calibration. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://arxiv.org/pdf/1912.10211
- Evidence gap: No author-provided per-class decision thresholds or calibration scripts were found in the checked repository README, issues, or paper.

## Public benchmarks

### Audio tagging (clip-level)

- Dataset/split: AudioSet / not reported
- Metric/value: mean average precision (mAP) / 0.431 (`higher-is-better`)
- Model scope: CNN14 system as reported in the PANNs paper (CNN14 hop-size experiment)
- Conditions: Reported by authors in PANNs paper hop-size experiments; hop size 320 configuration reported to yield this mAP.
- Source: https://arxiv.org/pdf/1912.10211
- Locator: PANNs paper, Table VI (hop-size experiments) and Table IV (proposed CNN14 yields mAP=0.431)
- Caveat: The checked primary sources do not provide an explicit dataset split identifier or exact evaluation script path for reproducing the reported mAP in the provided findings.
- Caveat: Reported mAP is tied to a hop-size experimental configuration per the paper; exact runtime/evaluation script details were not present in the provided findings.

### Audio tagging (clip-level) — repository-named checkpoint artifact

- Dataset/split: AudioSet / not reported
- Metric/value: mean average precision (mAP) (as implied by checkpoint filename) / 0.438 (as named in checkpoint filename) (`higher-is-better`)
- Model scope: Cnn14_16k_mAP=0.438.pth (checkpoint filename exposed in audioset_tagging_cnn repository)
- Conditions: Filename indicates a reported mAP value for a 16kHz-trained variant; the repository README states this checkpoint was trained by a later code version and achieves higher mAP than reported in the paper.
- Source: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md
- Locator: audioset_tagging_cnn/README.md paragraph stating 'The checkpoint file Cnn14_16k_mAP=0.438.pth is trained by a later code version and achieves higher mAP than reported in the paper.'
- Caveat: The numeric mAP is embedded in the checkpoint filename; the checked repository files did not include an exact evaluation table or script path in the provided findings to reproduce the reported value.
- Caveat: Split and exact evaluation protocol for the filename-referenced mAP value are not specified in the provided findings.

## Comparisons

### google/hear (candidate alternative supplied) — `insufficient-evidence`

- Task: Audio tagging / health-acoustic embeddings (candidate alternative)
- Criteria: No primary-source, protocol-matched checkpoint-level evaluation artifacts for the alternative were present in the checked evidence; cannot perform like-for-like comparison.
- Rationale: The provided primary findings did not include checkpoint-level evaluation numbers or exact protocol details for the alternative to permit a protocol-matched comparison against PANNs CNN14.
- Comparison conditions: Missing primary-source comparable numbers, dataset split, prompting, preprocessing, and checkpoint identifiers for the candidate alternative in the evidence set used.
- Evidence:

### laion/clap-htsat-fused (candidate alternative supplied) — `insufficient-evidence`

- Task: Zero-shot / audio tagging (candidate alternative)
- Criteria: No primary-source checkpoint-level evaluation artifacts for the alternative were present in the checked evidence.
- Rationale: The provided primary findings did not include comparable primary-source evaluation numbers or checkpoint artifacts for the alternative.
- Comparison conditions: Missing primary-source comparable numbers and protocol details for the alternative in the checked evidence.
- Evidence:

### MIT/ast-finetuned-audioset-10-10-0.4593 (candidate alternative supplied) — `insufficient-evidence`

- Task: Audio tagging fine-tuned on AudioSet (candidate alternative)
- Criteria: No primary-source checkpoint-level evaluation artifacts for the alternative were present in the checked evidence.
- Rationale: The provided primary findings did not include checkpoint-level evidence or protocol-matched numbers for the alternative.
- Comparison conditions: Missing primary-source comparable numbers, dataset split, and checkpoint evidence for the alternative in the checked evidence.
- Evidence:

## Limitations and safety

### Limitations

- Checkpoint-to-code compatibility issues: a repository issue documents size-mismatch errors when loading Cnn14_16k_mAP=0.438.pth with a different code version, indicating compatibility/version sensitivity for checkpoints. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/issues/18
- Training / evaluation data provenance: the PANNs paper evaluates models on AudioSet and the repository references AudioSet labels; the checked findings do not specify the exact dataset split identifier used to compute the reported mAP in the provided materials. Sources: https://arxiv.org/pdf/1912.10211, https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md
- Evidence gap: The provided findings did not include the exact numeric parameter count or multiply-add operations for CNN14; these quantities are not present in the research findings supplied.

### Safety

- License: The audioset_tagging_cnn repository contains an MIT license at the documented path governing the repository (LICENSE.MIT). Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/LICENSE.MIT
- Clinical/PHI guidance not provided: primary sources checked (paper and repository files) do not include clinical validation statements, PHI-handling guidance, or healthcare-specific usage approvals; clinical deployment would require separate validation and expert review. Sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md, https://arxiv.org/pdf/1912.10211
- Evidence gap: The provided findings do not contain author-provided privacy mitigation, dual-use discussion, or health-specific risk-mitigation guidance; none was located in the checked repository README, issues, or paper.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### PANNs paper (arXiv preprint)

- URL: https://arxiv.org/pdf/1912.10211
- Publisher: Qiuqiang Kong et al.
- Type: `paper`
- Primary because: Canonical paper describing PANNs architectures and reporting CNN14 evaluation numbers (mAP) and hop-size experiments used to support benchmark claims.
- Scope: PANNs paper coverage of CNN14 evaluation and hop-size experiments
- Supports: Table VI and Table IV reporting CNN14 mAP=0.431 under hop-size experimental configurations
- Supports: use of AudioSet for evaluation and metrics (mAP, mAUC, d-prime) for audio tagging

### panns_inference README (author's inference examples referencing Cnn14_mAP=0.431.pth)

- URL: https://github.com/qiuqiangkong/panns_inference/blob/master/README.md
- Publisher: Qiuqiang Kong (repository)
- Type: `repository`
- Primary because: Author-maintained inference examples that reference the Cnn14_mAP=0.431.pth checkpoint path and show example outputs/confidences used as upstream-checkpoint evidence.
- Scope: panns_inference examples referencing Cnn14_mAP=0.431.pth and showing sample outputs
- Supports: the checkpoint path /root/panns_data/Cnn14_mAP=0.431.pth used in examples
- Supports: example class-confidence outputs in inference examples
- Supports: citation of the PANNs paper

### audioset_tagging_cnn README (author's repository root README)

- URL: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/README.md
- Publisher: Qiuqiang Kong (repository)
- Type: `repository`
- Primary because: Author's repository README listing checkpoint filenames and example inference parameter values; used to verify presence of repository-named checkpoints and example preprocessing parameters.
- Scope: Repository README statements about checkpoint filenames (e.g., Cnn14_16k_mAP=0.438.pth, Cnn14_DecisionLevelMax_mAP=0.385.pth) and example inference parameters
- Supports: presence and naming of checkpoint Cnn14_16k_mAP=0.438.pth and Cnn14_DecisionLevelMax_mAP=0.385.pth
- Supports: example inference parameters: sample_rate=16000, window_size=512, hop_size=160, mel_bins=64, fmin=50, fmax=8000
- Supports: notation that Cnn14_16k_mAP=0.438.pth was trained by a later code version

### audioset_tagging_cnn LICENSE.MIT

- URL: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/LICENSE.MIT
- Publisher: Qiuqiang Kong (repository)
- Type: `official-documentation`
- Primary because: Author-provided license file governing repository code; used to verify code-license terms.
- Scope: Repository license governing audioset_tagging_cnn
- Supports: MIT license text and copyright statement for the repository

### audioset_tagging_cnn issues index

- URL: https://github.com/qiuqiangkong/audioset_tagging_cnn/issues
- Publisher: Qiuqiang Kong (repository)
- Type: `official-documentation`
- Primary because: Repository issues index used to corroborate presence of checkpoint/compatibility and other operational issues reported by users and the maintainer.
- Scope: Repository issue tracking for audioset_tagging_cnn
- Supports: existence of multiple issues referencing checkpoints, SED, dataset sharing, and access to pretrained model links

### panns_inference issues index

- URL: https://github.com/qiuqiangkong/panns_inference/issues
- Publisher: Qiuqiang Kong (repository)
- Type: `official-documentation`
- Primary because: Repository issues index for panns_inference used to corroborate reported loading/state_dict and inference behavior remarks relevant to checkpoint usage.
- Scope: Repository issue tracking for panns_inference
- Supports: issues reporting errors loading Cnn14 state_dict and other inference-related observations

### audioset_tagging_cnn issue #18 (Pretrained Cnn14 16kHz wrong shape errors)

- URL: https://github.com/qiuqiangkong/audioset_tagging_cnn/issues/18
- Publisher: Qiuqiang Kong (repository issue)
- Type: `official-documentation`
- Primary because: Specific repository issue documenting checkpoint vs. code size-mismatch errors when loading a named checkpoint into a different code version.
- Scope: Issue describing pretrained Cnn14 16kHz wrong shape errors
- Supports: report of size-mismatch errors for spectrogram_extractor and logmel_extractor weights when loading Cnn14_16k_mAP=0.438.pth into a different code version

### Exact official starting source declared by Forge

- URL: https://github.com/qiuqiangkong/audioset_tagging_cnn
- Publisher: github.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: panns-cnn14-audioset
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The provided research findings do not include the exact spectrogram/log-mel instantiation lines or function names from pytorch/models.py; models.py facts were not present in the findings, so spectrogram parameters from code-level implementation cannot be verified from the supplied sources.
- Evidence gap: The provided findings do not include an explicit repository file or paper locator that states the exact numeric embedding tensor shape for the Cnn14_mAP=0.431.pth checkpoint; embedding shape is not reported in the supplied findings.
- Evidence gap: No author-provided per-class decision thresholds, per-class calibration parameters, or deployment threshold recommendations were found in the checked primary sources (README, issues, or paper) in the provided findings.
- Evidence gap: The provided findings do not include an exact dataset split identifier or path used to compute the reported mAP=0.431; the paper reports mAP in tables and the repository references AudioSet but the precise split provenance was not present in the supplied findings.
- Evidence gap: The provided findings do not contain an explicit commit hash, release tag, or exact repository revision mapping to the Cnn14_mAP=0.431.pth checkpoint; no such mapping was present in the supplied findings.
- Evidence gap: The provided findings did not include author-provided privacy mitigation, dual-use discussion, or health-specific risk-mitigation guidance in repository README, issues, or paper.
- Evidence gap: The provided findings did not include any explicit mapping file (class index → class name) within the audioset_tagging_cnn repository files checked in the findings.
- Evidence gap: The provided findings do not include numeric parameter counts or multiply-add operation counts for CNN14; these were not present in the supplied findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'bakhtos' for this exact model scope: $.sources[7] uses unapproved repository owner 'bakhtos' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'litert-community' for this exact model scope: $.sources[9] uses unapproved repository owner 'litert-community' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/LICENSE.MIT Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/qiuqiangkong/audioset_tagging_cnn/blob/master/LICENSE.MIT Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://github.com/qiuqiangkong/audioset_tagging_cnn: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
