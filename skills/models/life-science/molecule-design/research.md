# Molecule Design model selection

- Category: `life-science`
- Group: `molecule-design`
- Independent audit: `revised`
- Researched: `2026-07-23T20:28:44.658553+00:00`

Head-to-head, evidence-grounded comparison of three exact Forge candidates for small-molecule generation (nvidia-genmol-2-0-0-nim, nvidia-genmol-nim, nvidia-molmim-nim). Scope: official NVIDIA NIM/container/serving documentation, official build.nvidia model cards, NGC catalog entries, and bionemo-framework canonical pages for the exact named candidate/service. The dossier reports canonical candidate identity (slug, displayName, versionKey where available in primary sources), documented input modalities and accepted formats (SAFE/SMILES/CSV), documented input preprocessing/validation and explicit numeric limits if present, documented output modalities and the explicit output schema when present, stated use cases and supported generation modes, and license/serving terms as documented. Benchmarks listed are only those verifiable in the cited NVIDIA primary sources for the exact NIM/service or explicitly labeled as upstream-checkpoint evidence. All head-to-head comparisons are permitted only under identical hardware/runtime/prompts/dataset-split/evaluation-pipeline; absent fully matched protocols the dossier reports evidence gaps identifying the missing primary-source data required for comparability.

## Questions to answer before selecting

- Do you require fragment-guided generation using SAFE templates (e.g., motif extension, scaffold decoration, linker design), or SMILES-only generation?
- Is per-molecule scoring/output JSON metadata required in addition to generated molecules (scores, properties)?
- Are production-use licensing constraints a critical factor (NVIDIA Open Model License / NVIDIA AI Foundation Models Community License / Apache / NGC container terms)?
- Is NVIDIA NIM-based deployment (Docker/NGC tooling, GPU runtime flags) a hard constraint for your workflow?
- Do you require explicit CMA-ES-based optimization or other controlled-generation features (latent-space manipulation) in the pipeline?

## Comparability rules

- Head-to-head comparisons are comparable only when the primary sources for each candidate document identical runtime and protocol conditions: same NIM/service version, identical hardware SKU(s) and count, identical prompt/template text, identical dataset split(s), identical generation parameters (temperature, noise, mask_length/min_add_len, num_molecules), identical random seeds and CMA-ES configuration where applicable, and identical evaluation pipeline (SMILES validation, fingerprint settings).
- Only benchmark rows explicitly reported for the exact named candidate/service and version in an NVIDIA primary source may be compared in-place; benchmarks reported for different service versions or upstream checkpoints must be treated as upstream-checkpoint evidence and not conflated with NIM/service measurements.
- Inputs and outputs used in comparisons must adhere to each candidate’s documented modalities, parameter names, and numeric bounds as specified in the cited endpoints or model-card sections; if any input bound or output schema is not documented for a candidate/version, comparisons are not permitted without that missing primary evidence.
- Licensing and deployment terms referenced in comparisons must be taken from each candidate’s primary model card, NGC entry, or official NIM documentation; do not generalize license statements across versions or containers.

## Conditional routing

### Prefer `nvidia-genmol-2-0-0-nim` when Project requires fragment-guided generation from SAFE templates (motif extension, scaffold decoration, one-step linker design) with explicit per-molecule scores returned alongside generated molecules

- Why: GenMol NIM v2.0.0 (NV-GenMol-89M-v2) documents SAFE-string or SMILES template input at the /generate endpoint (parameter name "smiles" accepting SAFE or SMILES, nullable for de novo), and documents Text outputs as an array of SAFE strings plus Number outputs as an array of FP32 scores. GenMol v2.0 NIM endpoints and overview explicitly list de novo generation, motif-extension, scaffold-decoration, and one-step linker design as supported generation modes.
- Alternative: nvidia-genmol-nim
- Alternative: nvidia-molmim-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://build.nvidia.com/nvidia/genmol-generate, https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://docs.nvidia.com/nim/bionemo/genmol/2.0.0/release-notes.html

### Prefer `nvidia-molmim-nim` when Project requires explicit CMA-ES-based latent-space optimization, seed-centered controlled sampling, or direct latent-space perturbation to improve user-defined scoring functions

- Why: MolMIM documentation and model-card describe controlled generation by sampling from a latent space around a seed molecule and optimization in latent space using the CMA-ES algorithm; MolMIM model materials and API reference describe the model as supporting CMA-ES optimization and sampling novel molecules from latent perturbations.
- Alternative: nvidia-genmol-2-0-0-nim
- Alternative: nvidia-genmol-nim
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-molmim, https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html

### Prefer `nvidia-genmol-2-0-0-nim` when Production deployment requires permissive weights/license terms explicitly governed by the NVIDIA Open Model License as stated for the served candidate/version

- Why: The GenMol v2.0 model card and build.nvidia entry document that GenMol v2.0 (NV-GenMol-89M-v2) is governed by the NVIDIA Open Model License for commercial use (as stated on the build.nvidia model-card and service descriptions).
- Alternative: nvidia-genmol-nim
- Alternative: nvidia-molmim-nim
- Evidence: https://build.nvidia.com/nvidia/genmol-generate, https://docs.nvidia.com/nim/bionemo/genmol/2.0.0/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol

### Prefer `nvidia-molmim-nim` when Production deployment requires or is restricted to models governed by the NVIDIA AI Foundation Models Community License / NVIDIA AI Enterprise subscription terms as documented for the service

- Why: MolMIM model-card and NGC entries and selected documentation indicate MolMIM is provided under NVIDIA AI Foundation Models Community License / related NVIDIA service terms and that MolMIM NGC/container access may require NVIDIA AI Enterprise subscription or trial; MolMIM model materials also note licensing distinctions in the framework documentation.
- Alternative: nvidia-genmol-2-0-0-nim
- Alternative: nvidia-genmol-nim
- Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html

### Prefer `insufficient-evidence` when Project requires a single preferred candidate based on an all-candidates, protocol-matched head-to-head benchmark (identical hardware, identical prompts/templates, identical dataset splits, identical seeds and evaluation pipeline) across the three named candidates

- Why: Primary NVIDIA sources provide candidate-specific benchmarks (GenMol NIM v1/v2 SAFE-DRUGS motif-extension and scaffold-decoration results; MolMIM service/framework reconstruction and sampling metrics) but do not provide an NVIDIA primary-source head-to-head table that measures all three exact named candidates under an identical end-to-end protocol; therefore no single preferred candidate can be supported for protocol-matched head-to-head performance.
- Alternative: nvidia-genmol-2-0-0-nim
- Alternative: nvidia-genmol-nim
- Alternative: nvidia-molmim-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html

## Benchmark taxonomy

### GenMol fragment-conditioned small-molecule generation (motif-extension, scaffold-decoration, linker design) as benchmarked in GenMol NIM

- Datasets: SAFE-DRUGS
- Metrics: Validity (fraction of syntactically valid molecules), Uniqueness (fraction unique within generated set), Diversity (internal diversity metric reported by GenMol benchmarks), Novelty (fraction novel relative to reference set), Quality (dataset-specific quality score reported in GenMol benchmarks), Wall-time (per-task inference wall-time on specified GPU SKUs)
- Compare only when: Benchmark parameters must match GenMol benchmark settings: mask_length = 17 (where reported), temperature and noise as specified (e.g., motif-extension: temperature=1.2, noise=1.6; scaffold-decoration: temperature=1.2, noise=2.0) and num_molecules and other endpoint parameters as reported in GenMol /generate endpoint documentation.
- Compare only when: Hardware must match the GenMol benchmark GPU SKU (e.g., H100, A100, A10G, L40S, RTX6000 Ada, RTX6000 Blackwell, H200, B200, B300, GH200, GB200, GB300, DGX Spark GB10) and single-GPU execution semantics used in the GenMol NIM tests.
- Compare only when: Use the SAFE-DRUGS test selection process and the same per-test mask/template construction described in the GenMol benchmarks page.

### MolMIM controlled sampling and latent-space optimization (seed-based sampling and CMA-ES optimization reported by MolMIM materials)

- Datasets: unspecified large-scale SMILES pretraining dataset (pretraining/validation/test split as reported by MolMIM primary sources)
- Metrics: Exact reconstruction (reconstruction accuracy on clustered validation set), Reconstruction without chirality, ECFP4 similarity thresholds (≥0.9, ≥0.8, ≥0.7), Validity (percent valid SMILES), Uniqueness, Novelty, Non-identicality, Effective novelty, Sampling radius parameter (σ) and best-performing radius used in reported metrics
- Compare only when: Comparisons require identical MolMIM service/version and the same sampling radius (σ) settings, same seed selection, identical CMA-ES hyperparameters, and identical validation set (the 250K clustered validation set referenced in MolMIM model-card) to be comparable.
- Compare only when: When comparing MolMIM service metrics to framework-model metrics, require explicit statement in primary sources that sampling/evaluation pipelines are identical or treat the pair as incomparable.

## Primary sources

- [GenMol NIM overview](https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html) — NVIDIA; supports GenMol v2.0 supports de novo generation, linker design, motif extension, scaffold decoration/morphing, hit generation, and lead optimization., GenMol NIM can be deployed as a Docker image and inferences can be made via OpenAPI HTTP(s) requests., One-step linker design in GenMol v2 allows direct generation of a linker connecting two fragments in a single inference pass.
- [GenMol NIM endpoints (parameter and input/output descriptions)](https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html) — NVIDIA; supports The /generate endpoint accepts the parameter "smiles" (string) which can be a SAFE or SMILES template; if null, the model performs de novo generation., The "num_molecules" parameter is an integer between 1 and 1000 with default 30., Temperature, noise, gamma, min_add_len, scoring enum (QED/LogP) and other parameter ranges are documented for GenMol /generate.
- [GenMol NIM benchmarks page](https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html) — NVIDIA; supports GenMol benchmarks include motif-extension and scaffold-decoration tests drawn from the SAFE-DRUGS dataset with reported metric values (validity, uniqueness, diversity, novelty, quality) and per-GPU wall-time measurements., Benchmark parameter settings such as mask_length=17 and specific temperature/noise pairs for motif-extension and scaffold-decoration are reported., Wall-time metrics for multiple GPU SKUs (H100, A100, A10G, L40S, RTX6000 Ada/Blackwell, H200, B200/B300, GH200, GB200/GB300, DGX Spark GB10) are reported.
- [GenMol NIM 2.0.0 release notes](https://docs.nvidia.com/nim/bionemo/genmol/2.0.0/release-notes.html) — NVIDIA; supports GenMol NIM version 2.0.0 upgrades the NIM to the NV-GenMol-89M-v2 checkpoint and documents the v2.0.0 container labeling and validation matrix details.
- [GenMol build.nvidia model card / service entry](https://build.nvidia.com/nvidia/genmol-generate) — NVIDIA; supports GenMol v2.0 (NV-GenMol-89M-v2) is a masked diffusion model trained on SAFE representations for fragment-based molecule generation., Input types accepted include Text (Molecular Sequence), Number, Enumeration (scoring method), and Binary (unique-molecules flag)., Text input is documented as a SAFE string up to 512 tokens; outputs are documented as arrays of SAFE strings and arrays of FP32 scores; license statement references NVIDIA Open Model License for the model.
- [GenMol NGC container entry (NGC catalog)](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol) — NVIDIA; supports GenMol NIM container for v2.0 (NV-GenMol-89M-v2) is distributed via NGC, reports container size and single-GPU execution semantics, and lists supported GPU SKUs in the validation matrix., NGC/container listing documents container licensing under NVIDIA Software License Agreement and product-specific terms for NVIDIA AI products.
- [GenMol getting-started (templating and SAFE syntax)](https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html) — NVIDIA; supports The input template placeholder for masked fragments uses syntax "[{min_len-max_len}]" and providing an empty template triggers de novo generation; a partial SAFE or SMILES template triggers conditioned generation such as motif extension, scaffold decoration, or linker design.
- [GenMol support matrix (hardware and software prerequisites)](https://docs.nvidia.com/nim/bionemo/genmol/2.0.0/support-matrix.html) — NVIDIA; supports GenMol NIM v2.0 requires CUDA compute capability ≥7.0, supported NVIDIA driver versions, and lists recommended minimum local disk space and per-container resource guidance.
- [MolMIM build.nvidia model card / service entry](https://build.nvidia.com/nvidia/molmim-generate) — NVIDIA; supports MolMIM is trained in an unsupervised manner on large-scale SMILES datasets and can sample novel molecules from its latent space., MolMIM model card and service documentation list MolMIM architecture type, controlled generation capabilities, and references supporting CMA-ES usage.
- [MolMIM model card (build.nvidia specific modelcard)](https://build.nvidia.com/nvidia/molmim-generate/modelcard) — NVIDIA; supports MolMIM model-card describes MolMIM as an encoder-decoder (Perceiver encoder + Transformer decoder) with ~65.2M parameters, controlled generation using latent-space perturbations, and CMA-ES optimization for user-defined scoring functions.
- [MolMIM NIM API reference](https://docs.api.nvidia.com/nim/reference/nvidia-molmim) — NVIDIA; supports MolMIM is a latent variable model using transformer architectures and Mutual Information Machine learning; the API reference documents input types (Text/CSV/SMILES) and controlled sampling behavior.
- [MolMIM NIM overview](https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html) — NVIDIA; supports MolMIM NIM documentation states MolMIM can sample valid SMILES from its latent space via perturbations of a seed molecule and can generate molecules with desired properties through controlled latent-space perturbations.
- [MolMIM framework models page (bionemo-framework)](https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html) — NVIDIA; supports MolMIM architecture details (encoder-decoder, Perceiver encoder, 6-layer encoder/decoder, hidden size 512, 8 attention heads, feed-forward dim 2048) and reported sampling/reconstruction metrics for service and framework model variants., The framework page reports measured service metrics such as validity, novelty, uniqueness, non-identicality, and effective novelty for specific service/framework model versions.
- [MolMIM NIM support matrix and deployment notes](https://docs.nvidia.com/nim/bionemo/molmim/latest/support-matrix.html) — NVIDIA; supports MolMIM NIM requires GPUs with at least 3 GB of GPU memory and compute capability > 7.0 and is documented as single-GPU runtime in tested configurations., Tested GPU configurations for MolMIM NIM include L40, A100, and A10 GPUs.
- [MolMIM deploy instructions (build.nvidia)](https://build.nvidia.com/nvidia/molmim-generate/deploy) — NVIDIA; supports MolMIM NIM can be run via Docker with specific runtime flags (runtime=nvidia, NVIDIA_VISIBLE_DEVICES, shm-size, port mapping) and requires environment variables such as NGC_API_KEY and LOCAL_NIM_CACHE when deploying locally.
- [MolMIM NGC model entry (Clara collection)](https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-) — NVIDIA; supports MolMIM model-card entries on NGC list reconstruction/sampling metrics on validation sets and document model privacy/explainability notes and licensing/access conditions.
- [Exact official starting source declared by Forge](https://docs.nvidia.com/nim/bionemo/genmol/latest) — docs.nvidia.com; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Canonical training dataset name(s) used for MolMIM pretraining are not specified in the cited MolMIM primary sources; the dossier requires the exact dataset name (e.g., ZINC-15) and the specific section/figure/table in a primary source to verify dataset provenance for benchmark comparability. (Desired source/section: explicit dataset name and split in build.nvidia MolMIM modelcard or framework page.)
- Evidence gap: Exact JSON output schema for MolMIM NIM (field names, nesting, numeric precisions, and array ordering for returned SMILES and any numerical scores) is not documented in the cited MolMIM primary sources; the /generate output shape and types (e.g., arrays of SMILES plus corresponding numeric score arrays) require an explicit endpoints or model-card section to validate exact schema. (Desired source/section: MolMIM endpoints/specification page showing output JSON schema.)
- Evidence gap: For GenMol and MolMIM, the precise per-request output JSON schema (field names, typing, and per-molecule score alignment rules) beyond the textual descriptions is not available as a single canonical schema document in the cited primary pages; a formal OpenAPI/JSON schema in primary documentation would be required to fully verify exact output shapes.
- Evidence gap: While GenMol NIM benchmarks (SAFE-DRUGS motif-extension and scaffold-decoration) and MolMIM service/framework metrics are reported in primary sources, there is no single NVIDIA primary-source document reporting an end-to-end, identical-protocol head-to-head benchmark across all three exact Forge candidates (nvidia-genmol-2-0-0-nim, nvidia-genmol-nim, nvidia-molmim-nim) with identical hardware, prompts, seeds, and evaluation pipeline; the specific missing artifact would be a unified head-to-head benchmark report or appendix with matched protocol details.
- Evidence gap: Exact post-output validation rules (the official per-candidate recommended SMILES sanitization, canonicalization, and fingerprinting pipeline used to compute reported metrics) are not fully enumerated in the cited benchmark pages; the precise evaluator code or evaluation pipeline reference in a primary source would be required to reproduce reported metric values exactly.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarkTaxonomy_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://docs.nvidia.com/nim/bionemo/genmol/latest: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
