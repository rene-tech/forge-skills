# Docking Affinity model selection

- Category: `life-science`
- Group: `docking-affinity`
- Independent audit: `revised`
- Researched: `2026-07-23T20:22:26.519866+00:00`

Select between two Forge-served NIM candidates (boltz2-nim, versionKey 1-7-0; mit-diffdock-nim, versionKey nim-2-2-0-regional-mirror-onboarding) for (A) blind small-molecule docking (pose sampling and ranking) and/or (B) per-complex binding-affinity regression/ranking. Scope: decisions and claims are limited to what is documented in the official NIM model cards, NIM API/reference pages, NGC catalog entries, canonical upstream papers/preprints, and the official upstream GitHub repositories listed in the top-level sources. Outside scope: protein-only structure prediction without ligand, de-novo ligand generation, and any capability not explicitly present in the cited primary sources. Upstream-checkpoint evidence (original paper/repository) is preserved and labeled where applicable; container-level/runtime claims are restricted to statements present in NIM/NGC/container documentation or marked as evidence gaps when container-level documentation is absent or conflicting.

## Questions to answer before selecting

- Do you require blind docking (no binding‑pocket input) or docking constrained to a specified pocket?
- Do you require numeric per‑complex binding‑affinity predictions (regression to ΔG/pIC50 or comparable values) from the deployed NIM container, or only ranked poses/confidence scores for downstream evaluation?
- Must the affinity prediction be produced by the deployed Boltz‑2 NIM container (versionKey 1-7-0) rather than by upstream artifacts (paper/repository) or separate code?
- Which canonical benchmark/dataset and exact split (name/DOI/URL/accession) will you use for evaluation?
- Which evaluation metrics and thresholds do you require (e.g., Top‑1 RMSD <2Å; Pearson correlation target)?
- Which ligand input formats are required (SMILES, SDF, MOL2) and which receptor input formats are required (PDB text, chain selection, experimental vs modeled structures)?
- What maximum ligand size, maximum polymer/residue count, or token/atom limits must the model accept?
- Is retention of waters, cofactors, or metal ions required for evaluation or production predictions?
- Do you require explicit restraints (residue‑pair contacts, pocket constraints, bond constraints) or JSON prompt schemas to constrain docking/structure outputs?
- What computational constraints (minimum GPU memory, allowed GPU families) and throughput targets do you have (requests/sec; poses per ligand)?

## Comparability rules

- Results may be compared only when reported on the same canonical dataset name and the exact canonical test split/fold/accession/DOI; if the canonical split is not documented in a primary source, treat the split as unspecified and record an evidence gap.
- For docking pose‑accuracy comparisons, the pose‑sampling regimen must match exactly: identical number of sampled poses per ligand, identical receptor preparation (experimental PDB vs modeled receptor, chain selection), and identical retention/removal of waters/cofactors/ions.
- Pose success‑rate comparisons must use the same RMSD threshold (e.g., RMSD < 2 Å) and the same pose count used to compute Top‑k metrics (Top‑1, Top‑5, etc.).
- For affinity/regression comparisons, metrics (Pearson/Spearman/MSE) must be computed on identical test sets and splits; if a time‑split or multi‑split protocol (e.g., Boltz‑2 19 time splits reported upstream) is used, comparisons must replicate that exact split strategy.
- Input preprocessing must match exactly: protonation/tautomer canonicalization, atom typing, ligand stereochemistry handling, treatment of alternate PDB conformations, and retention/removal of waters/cofactors/metal ions; absent explicit preprocessing documentation in a primary source, treat preprocessing as an evidence gap.
- Input format and limits must match: receptor format (sequence vs PDB coordinates), ligand formats (SMILES/SDF/MOL2), and NIM-declared limits such as maximum polymers and ligands per request; only compare containers that share the same NIM versionKey and publicly documented API parameters.
- When a reported metric depends on a downstream head or service that is not demonstrably exposed by the Forge-served container, preserve the upstream-checkpoint provenance and do not attribute the benchmark to the container unless the NIM/NGC documentation explicitly documents the same endpoint/behavior.
- When a model reports per‑pose confidence scores, comparisons that treat those confidences as calibrated probabilities require a documented calibration mapping in a primary source; if no calibration mapping is documented, treat confidence as an uncalibrated score (evidence gap for calibration).

## Conditional routing

### Prefer `mit-diffdock-nim` when Use case: blind small‑molecule docking to propose multiple sampled poses and a ranked list when no pocket information is provided

- Why: DiffDock is explicitly described in the DiffDock NIM and model card as a generative diffusion model for blind molecular docking that outputs many sampled poses and ranks them via a confidence model; upstream DiffDock paper and NIM documentation state it does not require binding‑pocket information and was trained on PLINDER+SAIR.
- Alternative: boltz2-nim
- Evidence: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html, https://arxiv.org/abs/2210.01776

### Prefer `insufficient-evidence` when Use case: I require numeric per‑complex binding‑affinity predictions produced by the deployed Boltz‑2 NIM container (boltz2-nim versionKey 1-7-0) for lead‑optimization

- Why: Upstream Boltz‑2 paper and the Boltz‑2 model card describe an affinity module and report affinity benchmarks; however the Boltz‑2 NGC container entry documents that "Binding affinity prediction is not yet available in the Boltz‑2 NIM but will be added soon," producing a container‑level / deployment conflict. Container‑level availability of an affinity endpoint for versionKey 1-7-0 is not corroborated by the cited NIM/NGC documentation.
- Alternative: boltz2-nim
- Alternative: mit-diffdock-nim
- Evidence: https://build.nvidia.com/mit/boltz2/modelcard, https://biorxiv.org/content/10.1101/2025.06.14.659707v1.full.pdf, https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2

### Prefer `boltz2-nim` when Use case: end‑to‑end atomic structure prediction of protein–ligand complexes (full‑atom coordinates) where obtaining a complete complex structure is the primary objective and affinity ranking is secondary

- Why: The Boltz‑2 model card and upstream Boltz‑2 preprint describe a model that jointly models complex structures and binding affinities and enumerate model components (trunk, denoising module with steering, confidence module, affinity module); the Boltz‑2 NIM API documents a structure prediction endpoint and polymer/ligand input parameters.
- Alternative: mit-diffdock-nim
- Evidence: https://build.nvidia.com/mit/boltz2/modelcard, https://biorxiv.org/content/10.1101/2025.06.14.659707v1.full.pdf, https://docs.nvidia.com/nim/bionemo/boltz2/1.0.0/api-reference.html

### Prefer `insufficient-evidence` when Use case: pose refinement or re‑ranking where a known pocket and a small set of poses are provided and re‑scoring/refinement (not blind sampling) is the primary task

- Why: Primary sources document DiffDock's blind‑docking sampling behavior and Boltz‑2's joint modeling capabilities, but the supplied primary evidence does not include a head‑to‑head evaluation on the same pocket‑constrained benchmark using identical preprocessing and pose‑sampling regimens; therefore there is insufficient primary evidence to prefer one Forge candidate for pocket‑constrained re‑scoring.
- Alternative: boltz2-nim
- Alternative: mit-diffdock-nim
- Evidence: https://build.nvidia.com/mit/diffdock/modelcard, https://build.nvidia.com/mit/boltz2/modelcard

### Prefer `mit-diffdock-nim` when Use case: high‑throughput virtual screening where throughput and GPU‑optimized inference are priorities and per‑pose Top‑k ranking quality (k≤5) is the primary requirement

- Why: DiffDock NIM documentation and the DiffDock NIM performance page document GPU‑optimized deployment, training on PLINDER+SAIR for v2.2, and NIM packaging/runtime guidance used in performance measurements; DiffDock is described as providing sampled poses and ranked outputs suitable for virtual screening workflows.
- Alternative: boltz2-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/diffdock/latest/performance.html, https://docs.nvidia.com/nim/bionemo/diffdock/latest/getting-started.html, https://build.nvidia.com/mit/diffdock/modelcard

### Prefer `insufficient-evidence` when Constraint: you require a documented calibration mapping from the model's reported confidence scores to empirical error rates (a confidence→error calibration) from the NIM‑deployed container

- Why: Primary sources for both Boltz‑2 and DiffDock describe confidence modules/scores, but the supplied NIM model cards, API references, and upstream papers do not provide a per‑container documented calibration mapping that converts reported confidence scores into empirical error probabilities; no container‑level calibration mapping is present in the cited primary sources.
- Alternative: boltz2-nim
- Alternative: mit-diffdock-nim
- Evidence: https://build.nvidia.com/mit/boltz2/modelcard, https://biorxiv.org/content/10.1101/2025.06.14.659707v1.full.pdf, https://build.nvidia.com/mit/diffdock/modelcard

## Benchmark taxonomy

### Blind docking (pose sampling and ranking)

- Datasets: PLINDER, SAIR
- Metrics: Top‑k pose success rate at RMSD < 2Å (direction: higher is better), e.g., Top‑1 and Top‑5 success rates computed on the test split used by the benchmark., Per‑pose confidence score ranking performance (direction: higher is better); comparisons require documented calibration to empirical error rates to treat as probabilities.
- Compare only when: Same canonical dataset name and exact test split/accession/DOI.
- Compare only when: Identical number of sampled poses per ligand (e.g., 10 poses vs 40 poses matters for Top‑k).
- Compare only when: Same receptor preparation (experimental PDB vs modeled receptor), identical chain selection, and identical retention/removal of waters/cofactors/ions.

### Binding‑affinity regression / ranking

- Datasets: FEP+ (OpenFE), CASP16 affinity challenge, MF‑PCBA
- Metrics: Pearson correlation between predicted and experimental affinities (direction: higher is better)., Mean squared error (MSE) or centered MAE where reported (direction: lower is better)., Retrospective hit‑discovery metrics (e.g., average precision, enrichment factor) where reported (direction: higher is better).
- Compare only when: Same canonical dataset and exact test split/accession/DOI for regression/ranking comparison.
- Compare only when: Identical preprocessing for affinity values (unit conversions, assay curation) and identical compound standardization rules.
- Compare only when: If benchmarks report multiple time splits (e.g., Boltz‑2 upstream reports 19 time splits in fine‑tuning), comparisons must reproduce the same split scheme.

### Protein–ligand complex structure prediction (full‑atom complex coordinates)

- Datasets: Datasets used in upstream/training/evaluation as reported in the primary sources (e.g., PDB‑derived co‑crystal sets referenced by PLINDER/PoseBusters/other canonical benchmarks).
- Metrics: Structure confidence scores reported by the model (direction: higher indicates greater internal model confidence) — treat as uncalibrated unless a calibration mapping is provided in a primary source., Ligand heavy‑atom RMSD to experimental ligand (direction: lower is better) computed with the same atom selection and alignment rules.
- Compare only when: Identical input limits and NIM API parameter values (polymers count, sampling_steps, diffusion_samples) as documented in the container API reference.
- Compare only when: Same receptor modeling/chain selection and identical treatment of waters/cofactors/ions.

## Primary sources

- [Boltz-2 NIM model card (build.nvidia.com)](https://build.nvidia.com/mit/boltz2/modelcard) — NVIDIA / build.nvidia.com; supports Boltz‑2 NIM model card and high‑level statements about joint structure and affinity modeling., Container/model release information and model card claims used for provenance of boltz2-nim.
- [Boltz‑2 NIM candidate homepage (build.nvidia.com)](https://build.nvidia.com/mit/boltz2) — NVIDIA / build.nvidia.com (candidate root page); supports Canonical candidate homepage for boltz2-nim (required Forge candidate sourceUrl).
- [Boltz‑2 preprint (bioRxiv)](https://biorxiv.org/content/10.1101/2025.06.14.659707v1.full.pdf) — bioRxiv (Boltz authors); supports Upstream Boltz‑2 preprint: architecture description (trunk, denoising/steering, confidence, affinity modules) and reported affinity/structure benchmarks (upstream‑checkpoint evidence).
- [Boltz upstream GitHub repository (official)](https://github.com/jwohlwend/boltz) — Boltz upstream / GitHub; supports Official Boltz repository (upstream‑checkpoint evidence) including code, license, and artifacts referenced by the Boltz‑2 preprint and model card.
- [Boltz‑2 NIM API reference and inference docs (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/boltz2/1.0.0/api-reference.html) — NVIDIA Docs (NIM); supports Boltz‑2 NIM API reference and inference documentation documenting POST /biology/mit/boltz2/predict, the required 'polymers' input, and documented polymer input count constraints (min/max) in the API/inference docs (container API documentation).
- [Boltz‑2 NIM inference and limits (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/boltz2/latest/inference.html) — NVIDIA Docs (NIM); supports Boltz‑2 NIM inference documentation and runtime details including polymer sequence length limits, health‑check endpoint, and parameter descriptions for inference requests (container API documentation).
- [Boltz‑2 NIM optimization and environment variables (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/boltz2/1.0.0/optimization.html) — NVIDIA Docs (NIM); supports Boltz‑2 NIM optimization and environment variables that control maximum polymers and ligands per request (container runtime/configuration documentation).
- [Boltz‑2 NGC catalog entry (NGC / NVIDIA)](https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2) — NVIDIA NGC Catalog; supports NGC catalog entry documenting the Boltz‑2 container contents and the explicit statement that "Binding affinity prediction is not yet available in the Boltz‑2 NIM but will be added soon." (container‑level statement).
- [DiffDock NIM model card (build.nvidia.com)](https://build.nvidia.com/mit/diffdock/modelcard) — NVIDIA / build.nvidia.com; supports DiffDock model card hosted on build.nvidia.com and model provenance for mit-diffdock-nim (candidate root model card).
- [DiffDock NIM candidate homepage (build.nvidia.com)](https://build.nvidia.com/mit/diffdock) — NVIDIA / build.nvidia.com (candidate root page); supports Canonical candidate homepage for mit-diffdock-nim (required Forge candidate sourceUrl).
- [DiffDock NIM overview (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html) — NVIDIA Docs (NIM); supports DiffDock NIM overview documentation stating DiffDock is a blind docking diffusion model, that it outputs many sampled poses, and that DiffDock NIM v2.2 was trained on PLINDER+SAIR (container/API provenance).
- [DiffDock NIM performance (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/diffdock/latest/performance.html) — NVIDIA Docs (NIM); supports DiffDock NIM performance page documenting training on PLINDER+SAIR and serving/performance notes used in NIM packaging (container performance documentation).
- [DiffDock NIM API reference (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/diffdock/latest/api-reference.html) — NVIDIA Docs (NIM); supports DiffDock NIM API reference listing endpoints including POST /molecular-docking/diffdock/generate and standard health and model listing endpoints (container API documentation).
- [DiffDock NIM getting‑started (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/diffdock/latest/getting-started.html) — NVIDIA Docs (NIM); supports DiffDock NIM getting‑started and runtime/configuration instructions used in NIM packaging and performance measurements (container getting‑started documentation).
- [DiffDock original paper (arXiv / ICLR 2023)](https://arxiv.org/abs/2210.01776) — arXiv / ICLR (DiffDock authors); supports Canonical DiffDock paper (upstream‑checkpoint evidence) describing the diffusion pose generation and confidence model for blind docking (original model paper).
- [DiffDock upstream GitHub repository (official)](https://github.com/gcorso/DiffDock) — DiffDock upstream / GitHub; supports Official DiffDock GitHub repository (upstream‑checkpoint evidence and code provenance).
- [DiffDock NGC catalog entry (NGC / NVIDIA)](https://catalog.ngc.nvidia.com/orgs/nim/mit/containers/diffdock/-) — NVIDIA NGC Catalog; supports NGC catalog listing for the DiffDock container, container tag metadata, and deployment/geography statements (container provenance).
- [PLINDER dataset page (canonical dataset metadata)](https://plinder-org.github.io/plinder/dataset.html) — PLINDER project; supports PLINDER dataset metadata and dataset fields; PLINDER is cited as a PDB‑curated protein‑ligand interaction dataset used in DiffDock training/evaluation.
- [MF‑PCBA canonical description (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10170507) — PMC / NCBI; supports MF‑PCBA dataset and splits metadata (five random splits 80%/10%/10%) and relevant evaluation metrics for retrospective hit‑discovery., Boltz‑2 upstream reporting that includes MF‑PCBA evaluation claims (upstream evidence for Boltz‑2 evaluations).
- [CASP16 challenge format (PredictionCenter)](https://predictioncenter.org/casp16/index.cgi?page=format) — CASP / Prediction Center; supports CASP16 challenge format and target identification metadata relevant to affinity estimation tasks and use in evaluations (canonical CASP16 format documentation).

## Evidence gaps

- Evidence gap: Canonical test split files, exact accession identifiers, or DOIs for PLINDER canonical test splits are not present in the supplied primary sources; PLINDER dataset metadata page is cited but an explicit canonical test split URL/DOI/file for replication was not found in the provided findings.
- Evidence gap: Canonical test split files, exact accession identifiers, or DOIs for SAIR (Structurally‑Augmented IC50 Repository) test splits are not present in the supplied primary sources; the supplied findings reference SAIR training inclusion but no canonical test split URL/DOI was provided.
- Evidence gap: Canonical test split or explicit split DOI/accession for the FEP+ (OpenFE) benchmark as used by Boltz‑2 upstream is not documented in the supplied primary sources; upstream claims reference FEP+/OpenFE performance without an explicit canonical split URL in the cited sources.
- Evidence gap: Exact canonical test split/accession for the CASP16 affinity challenge as used in upstream reporting is not present in the supplied primary sources; CASP16 format pages exist but an explicit canonical test split file/DOI for reproduction was not provided in the findings.
- Evidence gap: No primary‑source documentation was found that confirms the Boltz‑2 NIM container versionKey 1-7-0 exposes a binding‑affinity prediction endpoint; NGC container documentation states that "Binding affinity prediction is not yet available in the Boltz‑2 NIM but will be added soon," creating a container‑level evidence gap for deployed affinity endpoints.
- Evidence gap: No primary‑source calibration mapping (confidence → empirical error probability) for either the Boltz‑2 or DiffDock NIM containers was found in the supplied sources; treat reported confidence values as uncalibrated absent additional published calibration.
- Evidence gap: Exact preprocessing protocols used in reported evaluations (protonation/tautomer enumeration, atom typing, retention/removal of waters/cofactors, handling of alternate PDB conformations) are not fully specified in the supplied primary sources for both Boltz‑2 and DiffDock, preventing exact protocol replication.
- Evidence gap: No head‑to‑head primary‑source evaluation comparing boltz2-nim (container versionKey 1-7-0) and mit-diffdock-nim on the same canonical benchmark with identical preprocessing and pose‑sampling parameters was found in the provided findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
