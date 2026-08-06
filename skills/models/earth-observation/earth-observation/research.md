# Earth Observation model selection

- Category: `earth-observation`
- Group: `earth-observation`
- Independent audit: `revised`
- Researched: `2026-07-23T19:55:51.906265+00:00`

I need a precise, checkpoint-scoped mapping of input→output expectations for the allenai-satlaspretrain-aerial-swinb family. Based on the authoritative repository files and model-library listing found in the primary sources, the documented family-level behavior is: input: an image tensor keyed as "image" where per-channel pixel values are normalized to the 0–1 range (explicit normalization to 0–1 is documented in ModelArchitecture.md and related files). The model can accept multiple aligned images per inference window (ModelArchitecture.md documents retrieval of multiple aligned images, either 3 or 4), each image passed through a Swin-v2-Base backbone to extract four feature maps at 1/4, 1/8, 1/16, and 1/32 of the input resolution; features across time are combined via temporal max‑pooling on each feature map before task‑specific heads make predictions (ModelArchitecture.md and satlas.allen.ai/ai). The satlaspretrain_models repository lists aerial high-resolution pretrained backbones including Aerial_SwinB_SI (single-image) and Aerial_SwinB_MI (multi-image) as the aerial Swin‑B pretrained variants. The repository exposes task categories and label lists for segmentation, point, polygon, classification, and regression tasks (satlas/model/dataset.py). I need explicit checkpoint-to-versionKey mappings, evaluation configs, JSON output schema and CRS conventions, and the exact evaluation scripts/commits that produced DataValidationReport numbers to make any checkpoint-scoped claims; those items are not fully published in the primary sources enumerated below and are listed as evidence gaps.

## Questions to answer before selecting

- What precise EO task is required (one of: land_cover segmentation, crop_type segmentation, point detection, polygon instance detection, wildfire/smoke/snow classification, dem regression)?
- Is the input imagery supplied as single-image or multiple aligned images per inference window (NumImages)?
- Are input pixel values pre-normalized to the 0–1 range (yes/no)?
- Is the input imagery 8-bit RGB and within the aerial high-resolution applicability range documented by the authors (evidence in the repo and model listing indicates aerial high-resolution applicability; see sources)?
- Is an explicit named checkpoint file and commit SHA required to reproduce reported numbers and the Forge versionKey mapping (yes/no)?
- Are polygon-instance outputs (task="polygon") required with a machine-readable JSON schema and CRS metadata (yes/no)?
- Are non‑RGB spectral bands required (e.g., Sentinel multispectral or SAR)?

## Comparability rules

- Input normalization must match: the repository documents normalizing image values to the 0–1 range (ModelArchitecture.md).
- Number of aligned input images (NumImages) and temporal aggregation must match: the repository documents retrieval of multiple aligned images (3 or 4) and applying temporal max‑pooling across feature maps (ModelArchitecture.md; satlas.allen.ai/ai).
- Backbone family must match: the aerial pretrained variants use a Swin‑v2‑Base backbone (satlaspretrain_models listing and ModelArchitecture.md).
- Task-head regime must match: the satlas development site and repository documentation indicate backbones are used with task-specific heads that are fine‑tuned for downstream tasks (satlas.allen.ai/ai); any comparison must match whether heads were randomly initialized and fine‑tuned or whether evaluation used a pretrained prediction head.
- Exact checkpoint identity must match: primary sources do not publish an authoritative mapping from the Forge versionKey 'usable-highres' to a specific checkpoint filename/commit; therefore any cross-report comparison that assumes such a mapping is unsupported without the authors providing the mapping. Evidence gap: mapping of Forge versionKey 'usable-highres' to exact checkpoint filename/commit (see evidenceGaps).
- Reported numeric metrics are only comparable when the identical dataset split, postprocessing, and metric computation code/commit are matched; DataValidationReport provides continent-wise precision and recall tables but does not publish the evaluation commit/config that produced them (DataValidationReport.md).

## Conditional routing

### Prefer `insufficient-evidence` when I require a pretrained aerial high-resolution model for 8‑bit RGB aerial imagery where the workflow can supply multiple aligned images and the evaluation relies on precision/recall as reported in the repository.

- Why: The satlaspretrain_models listing documents aerial Swin‑B single-image and multi-image pretrained backbones (Aerial_SwinB_SI and Aerial_SwinB_MI), and ModelArchitecture.md documents input normalization to 0–1, multiple aligned images (3 or 4), Swin‑v2‑Base backbone, and temporal max‑pooling. However, the repository does not publish a canonical mapping from the Forge versionKey 'usable-highres' to an exact checkpoint filename and commit; therefore I cannot deterministically assert that a particular public checkpoint file corresponds to the Forge slug without additional author confirmation.
- Alternative: allenai-satlaspretrain-aerial-swinb
- Evidence: https://github.com/allenai/satlas/blob/main/ModelArchitecture.md, https://github.com/allenai/satlaspretrain_models, https://github.com/allenai/satlas/blob/main/CustomInference.md

### Prefer `insufficient-evidence` when I require a model for multi-image / multi-temporal inference (multiple aligned images per prediction) and want a pretrained model that applies temporal aggregation at the feature level.

- Why: ModelArchitecture.md documents retrieval of multiple aligned images (either 3 or 4) per inference window and describes applying max pooling on the temporal dimension across feature maps, and satlaspretrain_models lists Aerial_SwinB_MI as a multi-image aerial pretrained variant. The primary sources do not publish a canonical evaluation config tying a named checkpoint to the precise NumImages used to produce reported evaluation numbers; this prevents a fully checkpoint-scoped recommendation.
- Alternative: allenai-satlaspretrain-aerial-swinb
- Evidence: https://github.com/allenai/satlas/blob/main/ModelArchitecture.md, https://github.com/allenai/satlaspretrain_models

### Prefer `insufficient-evidence` when I require confirmed numeric evaluation values (per-class precision/recall or continent-wise tables) that are reproducible from an available public checkpoint and a referenced evaluation commit.

- Why: The DataValidationReport.md presents continent-wise precision and recall definitions and tables, but the repository does not attach an explicit evaluation script/config/commit that produces those tables; therefore I cannot verify which exact checkpoint or commit produced the reported numbers without the authors publishing the evaluation artifacts.
- Alternative: allenai-satlaspretrain-aerial-swinb
- Evidence: https://github.com/allenai/satlas/blob/main/DataValidationReport.md

### Prefer `insufficient-evidence` when I require license statements for code and models to be authoritative for reuse decisions.

- Why: The Satlas repository includes an Apache License Version 2.0 LICENSE file at the repository root; the satlaspretrain_models listing indicates model releases under ODC-BY in the model listing facts in the research findings. Because code and model-data licenses differ, I require authors to explicitly state checkpoint artifact license information tied to each distributed artifact to use the checkpoint under known terms.
- Alternative: allenai-satlaspretrain-aerial-swinb
- Evidence: https://github.com/allenai/satlas/blob/main/LICENSE, https://github.com/allenai/satlaspretrain_models

### Prefer `insufficient-evidence` when I require a machine-readable JSON output schema and CRS/polygon coordinate convention for downstream integration.

- Why: Primary repository files and the Satlas project site document that models produce predictions and that polygon-instance inference is supported, but the repository does not publish an explicit machine-readable JSON output schema or explicit CRS/coordinate-order conventions tied to the inference outputs; therefore I cannot certify the exact JSON schema or coordinate conventions for the Forge slug without authors publishing a sample output/schema.
- Alternative: allenai-satlaspretrain-aerial-swinb
- Evidence: https://github.com/allenai/satlas, https://github.com/allenai/satlas/blob/main/satlas/model/dataset.py, https://github.com/allenai/satlas/blob/main/SatlasPretrain.md

## Benchmark taxonomy

### land_cover segmentation (semantic segmentation)

- Datasets: SatlasPretrain — pretraining collection referenced in repository
- Metrics: precision (as defined in DataValidationReport.md: percentage of objects in geospatial data products that are correct), recall (as defined in DataValidationReport.md: percentage of actual objects in the world that are covered in the geospatial data products)
- Compare only when: identical input normalization to 0–1 (ModelArchitecture.md)
- Compare only when: identical NumImages and temporal aggregation strategy (ModelArchitecture.md documents retrieval of 3 or 4 aligned images and max temporal pooling across feature maps)
- Compare only when: identical backbone family (Swin‑v2‑Base) and matching pretrained variant (single-image vs multi-image) as listed in satlaspretrain_models
- Compare only when: identical metric computation code/commit and dataset split definitions (Evidence gap: the repository does not publish the exact evaluation commit/config that produced DataValidationReport)

### polygon instance detection (instance polygons: e.g., solar_farm, power_plant)

- Datasets: Satlas DataValidationReport internal evaluation set — continent-wise evaluation as used in DataValidationReport.md
- Metrics: precision (DataValidationReport.md continent-wise definitions), recall (DataValidationReport.md continent-wise definitions)
- Compare only when: identical input normalization to 0–1 (ModelArchitecture.md)
- Compare only when: identical NumImages and temporal aggregation (if multi-image variant used) (ModelArchitecture.md)
- Compare only when: identical backbone family and exact checkpoint path (Evidence gap: mapping of Forge versionKey 'usable-highres' to exact checkpoint filename/commit is not published)

### point detection (e.g., wind_turbine, airplane)

- Datasets: Satlas DataValidationReport internal evaluation set — continent-wise evaluation as used in DataValidationReport.md
- Metrics: precision (DataValidationReport.md), recall (DataValidationReport.md)
- Compare only when: identical input normalization to 0–1 (ModelArchitecture.md)
- Compare only when: identical NumImages/temporal aggregation and backbone variant (ModelArchitecture.md; satlaspretrain_models)
- Compare only when: identical matching criteria for point localization (Evidence gap: DataValidationReport does not publish the exact matching radii or IoU thresholds used to compute precision/recall)

### classification and regression (wildfire/smoke/snow classification, dem regression)

- Datasets: Satlas internal task label sets as enumerated in satlas/model/dataset.py
- Metrics: standard classification/regression metrics to be reported by experimenters (e.g., balanced accuracy, F1, RMSE) — not specifically enumerated in primary DataValidationReport for these tasks
- Compare only when: identical input normalization to 0–1 (ModelArchitecture.md)
- Compare only when: identical backbone variant (Swin‑v2‑Base) and exact checkpoint path (Evidence gap: exact checkpoint path mapping to versionKey 'usable-highres' is not published)
- Compare only when: identical downstream fine‑tuning procedure and hyperparameters (Evidence gap: repository does not publish full fine‑tuning hyperparameter tables tied to reported evaluations)

## Primary sources

- [Satlas GitHub repository (root)](https://github.com/allenai/satlas) — AllenAI / Satlas (GitHub); supports High-level project documentation and presence of repository-level LICENSE file; general repository contents (README and top-level documents).
- [Satlas: ModelArchitecture.md](https://github.com/allenai/satlas/blob/main/ModelArchitecture.md) — AllenAI / Satlas (GitHub); supports Documentation that input images are normalized to 0–1, retrieval of multiple aligned images (3 or 4), Swin‑v2‑Base backbone producing feature maps at 1/4, 1/8, 1/16, and 1/32 of input resolution, and max pooling applied on the temporal dimension across images.
- [Satlas: DataValidationReport.md](https://github.com/allenai/satlas/blob/main/DataValidationReport.md) — AllenAI / Satlas (GitHub); supports Continent-wise precision and recall definitions and tables used by the Satlas project; definitions of precision and recall as used in the report.
- [Satlas: CustomInference.md](https://github.com/allenai/satlas/blob/main/CustomInference.md) — AllenAI / Satlas (GitHub); supports Examples of applying Satlas models on custom images and references to high-resolution / Sentinel-2 inference examples and representation extraction examples.
- [Satlas: dataset definitions (satlas/model/dataset.py)](https://github.com/allenai/satlas/blob/main/satlas/model/dataset.py) — AllenAI / Satlas (GitHub); supports Enumerated task names and exact class/category lists for polyline_bin_segment, bin_segment (crop categories), and point task categories such as wind_turbine and offshore_wind_turbine.
- [satlaspretrain_models repository (model listing)](https://github.com/allenai/satlaspretrain_models) — AllenAI (GitHub); supports Listing of pretrained model variants for Sentinel‑1, Landsat 8/9, and aerial high-resolution imagery; aerial pretrained model names include Aerial_SwinB_SI and Aerial_SwinB_MI; indicates model backbone family (Swin‑v2‑Base) for aerial variants.
- [Satlas repository LICENSE](https://github.com/allenai/satlas/blob/main/LICENSE) — AllenAI / Satlas (GitHub); supports Repository-level code license: Apache License Version 2.0 as included in the Satlas repository.
- [SatlasPretrain paper (arXiv record)](https://arxiv.org/abs/2211.15660) — arXiv / Bastani et al.; supports Canonical preprint record for the SatlasPretrain paper (title and arXiv identifier).
- [Satlas project site: Satlas AI model description](https://satlas.allen.ai/ai) — AllenAI / Satlas (project site); supports Documentation that Satlas AI models input a sequence of the three most recent satellite images per location, apply Swin Transformer backbones per image, combine features via max temporal pooling, and fine‑tune task-specific heads on labeled datasets.
- [Satlas GitHub repository (root) — cited revision/file](https://github.com/allenai/satlas/blob/main/SatlasPretrain.md) — AllenAI / Satlas (GitHub); supports Exact audited claim citation

## Evidence gaps

- Evidence gap: mapping of Forge versionKey 'usable-highres' to an exact checkpoint filename and commit SHA — the primary repositories do not publish an authoritative mapping from the versionKey to a named checkpoint file and commit.
- Evidence gap: exact evaluation script/config/commit used to generate the DataValidationReport.md tables — DataValidationReport.md presents continent-wise precision/recall tables but does not publish the specific evaluation commit or config that produced those tables.
- Evidence gap: explicit machine-readable JSON output schema and CRS/polygon coordinate conventions (pixel vs geographic, coordinate order) — the repository documents polygon-instance inference but does not publish a JSON schema or explicit CRS conventions tied to inference outputs.
- Evidence gap: canonical evaluation tile size, tiling/overlap strategy, and TrainMaxTiles usage for downstream segmentation/detection metrics — the repository references TrainMaxTiles/config examples but does not publish canonical evaluation tile sizes or tiling strategy.
- Evidence gap: exact fine-tuning hyperparameters and downstream training recipes tied to reported evaluation numbers — primary sources do not publish full hyperparameter tables linked to reported downstream results.
- Evidence gap: operational constraints (GPU VRAM requirements, latency, memory profiles) for inference with the aerial Swin‑B variants — the repository includes inference examples but no quantitative resource/latency profiles.
- Evidence gap: canonical public dataset split names/URIs for the internal evaluation sets used in DataValidationReport.md — the repository does not publish named public test/train/val split URIs for those reported evaluations.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 24 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property evaluation_conditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property fine_tune_regime Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property input_preproc Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property reproducibility_checklist Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0].datasets[0]: $.benchmarkTaxonomy[0].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property evaluation_conditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property fine_tune_regime Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property input_preproc Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property reproducibility_checklist Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1].datasets[0]: $.benchmarkTaxonomy[1].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property evaluation_conditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property fine_tune_regime Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property input_preproc Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property reproducibility_checklist Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2].datasets[0]: $.benchmarkTaxonomy[2].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: unexpected property evaluation_conditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: unexpected property fine_tune_regime Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: unexpected property input_preproc Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: unexpected property reproducibility_checklist Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3].datasets[0]: $.benchmarkTaxonomy[3].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://github.com/allenai/satlas/blob/main/SatlasPretrain.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
