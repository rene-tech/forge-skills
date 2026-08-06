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

- Research key: `github-com-allenai-satlas-2d73f9d0db`
- Independent audit: `revised`
- Researched: `2026-07-23T23:20:35.369138+00:00`

Primary SatlasPretrain artifacts (satlaspretrain_models repository, SatlasPretrain.md in the project repo, satlas-pretrain.allen.ai site, PyPI metadata, Hugging Face README, and the canonical arXiv preprint) document a family of pretraining assets for remote‑sensing imagery including Swin and ResNet backbones and a model composition of backbone + FPN + prediction head. The project reports an aggregate family‑level evaluation (Table 3 in the paper) showing a ~6% average improvement over the next best remote‑sensing baseline when fine‑tuned with 50 examples; primary artifacts do not publish an immutable upstream artifact identifier (git SHA, release tag, or file checksum) that maps the Forge serving variant name "usable-highres" to a single canonical file, nor do they report packaged checkpoint parameter counts, low‑level Swin hyperparameters tied to the packaged checkpoint, or an explicit canonical output JSON schema and tile‑assembly/georeference formulas for runtime assembly.

## Identity

- Upstream name: SatlasPretrain
- Checkpoint/version: Aerial_SwinB_SI (reported checkpoint ID pattern); immutable git SHA/release tag/file checksum not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Backbones reported include Swin Transformer (Swin‑Base) and ResNet; model composition described as backbone + Feature Pyramid Network (FPN) + prediction head (multi‑scale feature maps produced by backbone/FPN).
- License: Code / package: Apache Software License (per PyPI satlaspretrain-models and repository metadata). Model checkpoints / dataset: Open Data Commons Attribution License (ODC‑BY) reported for dataset and checkpoints in project model README and satlaspretrain_models statements.
- Evidence: https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md, https://pypi.org/project/satlaspretrain-models, https://huggingface.co/allenai/satlas-pretrain/blame/fb9208489a565e31b35832b272a1af6adc61cab9/README.md, https://arxiv.org/abs/2211.15660, https://satlas-pretrain.allen.ai, https://github.com/allenai/satlaspretrain_models/issues/13

## Selection

### Recommended

- **Representation learning and downstream fine‑tuning for remote‑sensing tasks on high‑resolution aerial imagery (0.5–2.0 m/pixel RGB).** — SatlasPretrain is presented as a large‑scale pretraining dataset and foundation model family intended for representation learning and downstream fine‑tuning; repository/package docs and the ICCV 2023/arXiv paper describe pretrained backbones for aerial imagery and recommend fine‑tuning for downstream tasks.
  Scope: SatlasPretrain foundation models / pretrained aerial backbones (family‑level; checkpoint IDs such as Aerial_SwinB_SI are reported but no immutable artifact identifier is published).
  Evidence: https://arxiv.org/abs/2211.15660, https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md
- **Fine‑tuning a SatlasPretrain backbone with task‑specific prediction heads for supervised downstream tasks (classification/segmentation/detection) on aerial imagery.** — The satlaspretrain_models package and repository document pretrained backbones paired with prediction heads intended for downstream supervised fine‑tuning rather than turnkey inference.
  Scope: Pretrained backbone plus fine‑tuned prediction head workflow (as illustrated by satlaspretrain_models examples and repository docs).
  Evidence: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md

### Conditional

- **Using provided prediction heads for downstream inference only after explicit fine‑tuning on task labels.** — Prediction heads are documented as randomly initialized and provided for fine‑tuning convenience; users must fine‑tune heads on target labels before interpreting outputs as meaningful probabilities or class predictions.
  Scope: satlaspretrain_models prediction heads paired with pretrained backbones (checkpoint IDs such as Aerial_SwinB_SI).
  Evidence: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models
- **Multi‑image temporal stacks (multi‑image mode) for aerial inputs when replicating the reported multi‑image evaluation.** — The multi‑image aerial model is reported trained to accept 4 images (example tensor shape shown as (1, 4, 3, 512, 512)); users altering image count or temporal alignment should validate empirical behavior for their tasks.
  Scope: Satlas multi‑image aerial model variant (e.g., Aerial_SwinB_MI pattern reported in package metadata).
  Evidence: https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlaspretrain_models

### Avoid

- **Using a pretrained checkpoint plus the provided prediction heads as a finalized production classifier/segmenter without fine‑tuning.** — Primary documentation and package metadata state prediction heads are randomly initialized and intended for fine‑tuning; direct use without fine‑tuning is unsupported by the authors.
  Scope: SatlasPretrain pretrained backbones and provided prediction heads (e.g., Aerial_SwinB_SI / packaged heads in satlaspretrain_models).
  Evidence: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models

## Input preparation

### Semantic inputs

- 8‑bit RGB aerial/satellite images at approximately 0.5–2.0 m/pixel are the intended high‑resolution inputs for the aerial SatlasPretrain models; multi‑image time series variants are also reported. Sources: https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlaspretrain_models, https://huggingface.co/allenai/satlas-pretrain/blame/fb9208489a565e31b35832b272a1af6adc61cab9/README.md
- Multi‑image aerial mode is trained to accept four images in examples; single‑image variants also exist (checkpoint ID patterns such as Aerial_SwinB_SI and Aerial_SwinB_MI are reported). Sources: https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlaspretrain_models

### Accepted formats

- 8‑bit (0–255) RGB image arrays suitable for conversion to tensors (examples show shape (1, 4, 3, 512, 512) for multi‑image inference). Sources: https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlaspretrain_models
- Configuration-driven inference invocation expecting a config file path and a weights path for model loading (inference examples reference config files for aerial variants). Sources: https://github.com/allenai/satlas/blob/main/SatlasPretrain.md, https://github.com/allenai/satlaspretrain_models

### Preprocessing

- Input pixel values are expected as 8‑bit integers (0–255) and should be normalized by dividing by 255 to obtain 0–1 floats prior to model input. Sources: https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlaspretrain_models, https://huggingface.co/allenai/satlas-pretrain/blame/fb9208489a565e31b35832b272a1af6adc61cab9/README.md
- Typical inference/training uses 512×512 patches (paper and package examples describe patch‑based training/inference and example tensor shapes matching 512×512 patch windows). Sources: https://arxiv.org/abs/2211.15660, https://pypi.org/project/satlaspretrain-models

### Pre-submit validation

- Users should ensure inputs match expected 8‑bit RGB shape/resolution and normalized value range; no machine‑enforced validation schema is published in the checked primary artifacts. Sources: https://pypi.org/project/satlaspretrain-models, https://github.com/allenai/satlaspretrain_models
- High‑resolution inference is described as tiling large images into 512×512 windows and merging outputs (paper reports tiling for high‑resolution mode), but exact tiling/overlap/assembly formulas are not published in the checked primary artifacts. Sources: https://arxiv.org/abs/2211.15660

### Task-specific formatting

- Repository examples and package usage expect supplying a config file path and a weights/identifier string to load the backbone or backbone+FPN+head for inference or training (config-based invocation pattern). Sources: https://github.com/allenai/satlas/blob/main/SatlasPretrain.md, https://github.com/allenai/satlaspretrain_models
- No canonical zero‑shot prompt, paired‑input text template, or immediate zero‑shot classifier workflow is provided; prediction heads are documented for fine‑tuning workflows. Sources: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models

## Output interpretation

### Outputs

- Model outputs exposed by the package/repository include multi‑scale feature maps from the backbone or FPN; prediction heads (when attached and fine‑tuned) produce task‑specific outputs. Sources: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models
- Checkpoint weight naming patterns and example .get_pretrained_model instantiation demonstrate mapping between checkpoint IDs and model components (e.g., Aerial_SwinB_SI mapped to backbone ± FPN ± head in package examples). Sources: https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlaspretrain_models/issues/13
- Exact runtime output JSON schema (field names, per‑pixel vs per‑box conventions, logits vs probabilities, explicit tensor shapes for served JSON) is not published in the checked primary artifacts. Sources: https://github.com/allenai/satlaspretrain_models, https://huggingface.co/allenai/satlas-pretrain/blame/fb9208489a565e31b35832b272a1af6adc61cab9/README.md

### Interpretation

- Prediction head outputs should not be interpreted as calibrated classification probabilities without downstream fine‑tuning and calibration; heads are documented as randomly initialized and intended for fine‑tuning. Sources: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models
- No canonical calibration guidance (temperature scaling, reliability diagrams, or recommended thresholds) for converting model outputs into calibrated probabilities is provided in the checked primary artifacts. Sources: https://github.com/allenai/satlaspretrain_models, https://arxiv.org/abs/2211.15660

### Post-inference validation

- Post‑inference validation such as recommended thresholding, tile‑assembly numeric rules, coordinate transform formulas, or recommended overlap/postprocessing procedures are not specified in the checked primary artifacts; users must implement downstream assembly and validation. Sources: https://arxiv.org/abs/2211.15660, https://github.com/allenai/satlaspretrain_models

## Public benchmarks

### Aggregate downstream remote‑sensing tasks (average across seven downstream datasets as reported in the SatlasPretrain paper)

- Dataset/split: aggregate of seven downstream datasets (paper‑level aggregate reported in Table 3) / not reported
- Metric/value: average relative performance improvement / 6% average improvement (aggregate family‑level result reported when fine‑tuned with 50 examples) (`higher-is-better`)
- Model scope: SatlasPretrain family‑level pretraining claim (paper‑level aggregate tied to fine‑tuning with 50 examples); not tied to a published immutable checkpoint identifier in the checked primary artifacts.
- Conditions: Result reported when pretrained on SatlasPretrain and then fine‑tuned with 50 labeled examples (see Table 3 in the paper); per‑checkpoint/per‑dataset numeric tables tied to a specific upstream checkpoint are not published in the checked primary artifacts.
- Source: https://arxiv.org/abs/2211.15660
- Locator: Table 3 (Section 5.2) in the SatlasPretrain paper (reports the 18% over ImageNet and 6% over next best baseline when fine‑tuned with 50 examples)
- Caveat: The reported 6% figure is an aggregate family/paper‑level result for fine‑tuning with 50 examples (Table 3) and is not published in the checked primary artifacts as tied to a specific immutable upstream checkpoint file for the Forge serving variant.
- Caveat: Per‑dataset, per‑checkpoint numeric tables and exact evaluation protocols/splits for the aerial Swin checkpoint are not present in the checked primary sources; direct checkpoint‑matched comparisons are therefore not supported by the available primary evidence.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Aggregate downstream remote‑sensing tasks (family‑level evaluation reported in the SatlasPretrain paper)
- Criteria: Protocol‑matched per‑checkpoint and per‑dataset numeric reporting is required to make checkpoint‑level comparisons; such per‑checkpoint tables tied to an immutable checkpoint are not published in the checked primary artifacts.
- Rationale: The paper reports an aggregate improvement (Table 3) for SatlasPretrain pretraining, but the checked primary artifacts do not provide per‑dataset/per‑checkpoint numeric tables or an immutable artifact identifier that would permit protocol‑matched checkpoint comparisons.
- Comparison conditions: Comparison would require a published immutable checkpoint identifier and per‑dataset/per‑checkpoint numeric results under a matching evaluation protocol; these are not present in the checked primary sources.
- Evidence: https://arxiv.org/abs/2211.15660, https://github.com/allenai/satlaspretrain_models

## Limitations and safety

### Limitations

- Primary artifacts do not publish an immutable upstream artifact identifier (git SHA, release tag, or file checksum) that maps a Forge serving variant name (e.g., "usable-highres") to a single canonical upstream checkpoint file. Sources: https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md
- Exact per‑dataset, per‑split, per‑checkpoint numeric benchmark tables and full evaluation protocols for the aerial Swin checkpoint are not present in the checked primary artifacts; only a family/paper‑level aggregate (Table 3) is reported. Sources: https://arxiv.org/abs/2211.15660, https://github.com/allenai/satlaspretrain_models
- Exact parameter counts for the packaged pretrained aerial Swin variant are not reported in the checked primary artifacts. Sources: https://github.com/allenai/satlaspretrain_models, https://pypi.org/project/satlaspretrain-models
- Exact low‑level Swin hyperparameters (patch size, patch‑embed stride/dimension, embedding dimension) tied to the packaged pretrained aerial Swin checkpoint are not documented in the checked primary artifacts. Sources: https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md
- Exact runtime tiling/cropping/stride/tile‑assembly formulas, georeference transform formulas, recommended overlap/postprocessing, and runtime batching/memory/latency guidance are not specified in the checked primary artifacts. Sources: https://arxiv.org/abs/2211.15660, https://github.com/allenai/satlaspretrain_models

### Safety

- Evidence gap: Primary sources do not provide explicit statements about PHI/PII handling, clinical‑use restrictions, or required expert‑in‑the‑loop review for operational deployment. Sources: https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md
- Code/package licensing: repository/package code is licensed under the Apache Software License (per PyPI metadata and repository statements); model checkpoints and dataset are reported as released under ODC‑BY in project README and package statements. Sources: https://pypi.org/project/satlaspretrain-models, https://huggingface.co/allenai/satlas-pretrain/blame/fb9208489a565e31b35832b272a1af6adc61cab9/README.md, https://github.com/allenai/satlaspretrain_models

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### satlaspretrain_models (GitHub repository/package)

- URL: https://github.com/allenai/satlaspretrain_models
- Publisher: allenai
- Type: `repository`
- Primary because: Official project repository/package providing model implementation, checkpoint identifiers, and usage examples maintained by the project authors.
- Scope: satlaspretrain_models implementation, checkpoint ID patterns, prediction head initialization, multi‑image handling, and example instantiation.
- Supports: The satlaspretrain_models repository provides a lightweight library to load pre‑trained SatlasPretrain models for Sentinel‑2, Sentinel‑1, Landsat 8/9, and high‑resolution aerial imagery.
- Supports: The model architecture is described as backbone + Feature Pyramid Network (FPN) + prediction head and the package documents prediction heads are provided for fine‑tuning (randomly initialized).
- Supports: The repository documents multi‑image aerial model behavior and checkpoint ID patterns such as Aerial_SwinB_SI / Aerial_SwinB_MI.

### SatlasPretrain.md (Satlas repository pretraining documentation)

- URL: https://github.com/allenai/satlas/blob/main/SatlasPretrain.md
- Publisher: allenai
- Type: `official-documentation`
- Primary because: Official repository pretraining/inference documentation authored by the Satlas project maintainers.
- Scope: Repository-level pretraining and inference invocation documentation and config examples for aerial Swin variants.
- Supports: Inference and training invocation patterns for SatlasPretrain models (config-driven invocation examples).
- Supports: References to config files and example pretrain/inference configs for aerial variants.

### satlaspretrain-models PyPI package metadata

- URL: https://pypi.org/project/satlaspretrain-models
- Publisher: Satlas @ AI2
- Type: `official-documentation`
- Primary because: Official published package metadata for the satlaspretrain-models package maintained by the project authors.
- Scope: Package metadata, example input expectations, example tensor shapes, and package license declaration.
- Supports: The satlaspretrain-models PyPI package lists the package license as Apache Software License and the author as 'Satlas @ AI2'.
- Supports: Package documentation notes input expectations (8‑bit RGB imagery normalized by dividing by 255) and example tensor shapes for multi‑image inference (e.g., (1, 4, 3, 512, 512)).
- Supports: The package metadata and docs state prediction heads are provided for fine‑tuning.

### Hugging Face README (SatlasPretrain model card - blob view)

- URL: https://huggingface.co/allenai/satlas-pretrain/blame/fb9208489a565e31b35832b272a1af6adc61cab9/README.md
- Publisher: allenai (Hugging Face model repository content)
- Type: `model-card`
- Primary because: Official model README/model‑card content maintained by the Satlas project (hosted on Hugging Face under the project's account).
- Scope: Model card / README content describing dataset licensing and intended imagery resolutions for packaged weights.
- Supports: The README states the SatlasPretrain dataset is released under the Open Data Commons Attribution License (ODC‑BY).
- Supports: The README indicates applicability for 0.5–2.0 m/pixel aerial/satellite RGB imagery and normalization guidance (divide 0–255 by 255).

### satlaspretrain_models issue #13 (example instantiation)

- URL: https://github.com/allenai/satlaspretrain_models/issues/13
- Publisher: allenai
- Type: `repository`
- Primary because: Repository issue demonstrating example code and model instantiation patterns provided by project maintainers; used as primary evidence of example usage.
- Scope: Example instantiation of Aerial_SwinB_SI and mapping between checkpoint IDs and model components in package examples.
- Supports: Issue example demonstrates instantiating a model with identifier 'Aerial_SwinB_SI' using weights_manager.get_pretrained_model and shows example head configuration and upsample layers composition.

### SatlasPretrain paper (arXiv preprint)

- URL: https://arxiv.org/abs/2211.15660
- Publisher: arXiv / authors (ICCV 2023 paper)
- Type: `paper`
- Primary because: Canonical preprint of the SatlasPretrain paper authored by the project authors; contains family‑level benchmark tables and section/table locators for reported aggregate results.
- Scope: Paper‑level description of dataset, pretraining, architecture choices, and aggregate downstream evaluation (Table 3, Section 5.2).
- Supports: The paper reports that pretraining on SatlasPretrain improves average performance on seven downstream datasets by ~6% (Table 3, Section 5.2).
- Supports: The paper documents use of 512×512 patches and high‑resolution tiling for evaluation/processing.

### SatlasPretrain official project site

- URL: https://satlas-pretrain.allen.ai
- Publisher: allenai
- Type: `official-documentation`
- Primary because: Official project landing site maintained by the Satlas authors linking dataset, code, and pre‑trained weights information.
- Scope: Project landing page describing availability of dataset, code, and pretrained model weights.
- Supports: The SatlasPretrain dataset, code, and pre‑trained model weights are publicly available at the project site.

### Exact official starting source declared by Forge

- URL: https://github.com/allenai/satlas
- Publisher: github.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: allenai-satlaspretrain-aerial-swinb
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Exact immutable checkpoint revision identifier (git SHA, release tag, or file checksum) mapping the Forge serving variant name "usable-highres" to a single canonical upstream checkpoint file is not reported in the checked primary sources.
- Exact per‑dataset, per‑split, per‑checkpoint numeric benchmark tables and full evaluation protocols for the aerial Swin checkpoint are not present in the checked primary artifacts; only an aggregate family/paper‑level result (Table 3) is published.
- Exact parameter counts for the packaged pretrained aerial Swin variant are not reported in the checked primary artifacts.
- Exact low‑level Swin hyperparameters (patch size, patch‑embed stride/dimension, embedding dimension) tied to the packaged pretrained aerial Swin checkpoint are not documented in the checked primary artifacts.
- Exact runtime output JSON/schema details (JSON field names, per‑pixel vs per‑box conventions, logits vs probabilities, explicit served tensor shapes) are not published in the checked primary artifacts.
- Exact tiling/cropping/stride/tile‑assembly formulas, georeference transform formulas, recommended overlap/postprocessing, and runtime batching/memory/latency guidance are not specified in the checked primary artifacts.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://github.com/allenai/satlas: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
