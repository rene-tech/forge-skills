# Protein Design model selection

- Category: `life-science`
- Group: `protein-design`
- Independent audit: `revised`
- Researched: `2026-07-23T20:29:47.622157+00:00`

Design tasks that produce protein sequences and/or 3D backbone coordinates from structural or motif/contig inputs. In scope: (a) inverse folding / fixed-backbone sequence design (produce amino-acid sequences consistent with a provided backbone PDB), (b) antibody/nanobody antibody-focused inverse folding (CDR-focused or whole-variable-domain sequence design given antibody backbone), (c) Cα-only sequence design (designing sequences from CA-only input), and (d) de novo backbone generation / motif scaffolding / binder design (generate new backbone coordinates conditioned on motif fragments, contigs, or PDB targets). Out of scope: predictive-only structure prediction (no sequence/design objective), non-protein modalities, or any claims about experimental binding affinity beyond what primary sources explicitly report.

## Questions to answer before selecting

- Does the job request require designing only sequences for a fixed backbone (inverse folding) or generating new backbone coordinates (de novo backbone/motif scaffolding)?
- If inverse folding, is the target an antibody (Fab or VHH) requiring CDR-focused optimization and IMGT indexing, or a general (non-antibody) protein?
- Is the input backbone provided as a full-atom PDB, a Cα-only PDB, or as motif+contig specifications (partial PDB + contig map)?
- Are there explicit sampling/control hyperparameters required (e.g., sampling temperature, num sequences per target, random seed, denoiser noise_scale) that must be matched to produce comparable outputs?
- Are there license or deployment constraints (e.g., must use only packages under MIT/BSD vs. NVIDIA NIM terms) that would exclude NIM-packaged models or require specific vendor terms?
- Is postprocessing required (e.g., Rosetta relaxation, AlphaFold refolding) and must that postprocessing be the same for comparisons?
- Are hardware constraints relevant (e.g., availability of NVIDIA GPU and acceptance of NIM packaging) for the requested workflow?

## Comparability rules

- To compare numeric benchmark values across models, the following must match exactly: dataset name and version/tag/split, preprocessing scripts/commands, input-format (PDB full-atom vs CA-only vs motif+contig), model versionKey/checkpoint tag, sampling/postprocessing hyperparameters (sampling_temp, num_seq_per_target, denoiser.noise_scale_* etc.), number of samples per target, and identical metric definitions (see benchmarkTaxonomy entries).
- If any of the above conditions differ (different dataset split, different preprocessing, different postprocessing like Rosetta relaxation/AF2 refolding), numeric results are non-comparable and must be treated as evidence gaps.
- When a NIM-packaged model and an upstream repository checkpoint are claimed to match, a primary-source vendor statement asserting byte-for-byte identical outputs or a repository-to-vendor mapping that documents the exact upstream checkpoint and the vendor package's version must be found before treating them as comparable; absent that primary-source claim, record an explicit evidence gap.

## Conditional routing

### Prefer `oxpig-antifold` when The task is antibody inverse folding (design sequences for an antibody variable domain given an antibody PDB or SAbDab ID with heavy and light chain labels; user prioritizes CDR recovery or low CDR RMSD).

- Why: AntiFold is an antibody-specialized inverse-folding model (fine-tuned for antibody variable domains) and the AntiFold repository, arXiv preprint, OPIG web app, and repository example outputs in the research findings indicate antibody-focused inputs, IMGT-numbering expectations, and example sampled outputs (temperature T=0.20). The primary-source evidence supporting antibody-focused behavior is cited in the evidenceUrls below.
- Alternative: dauparas-proteinmpnn-suite
- Alternative: rfdiffusion-nim
- Evidence: https://github.com/oxpig/AntiFold, https://arxiv.org/abs/2405.03370, https://opig.stats.ox.ac.uk/webapps/antifold, https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta, https://ora.ox.ac.uk/objects/uuid:a68dbce3-e083-4a97-bb00-ecf8931d172b/files/rz316q327z

### Prefer `dauparas-proteinmpnn-suite` when The task is fixed-backbone sequence design for general (non-antibody) proteins given a full-atom PDB backbone or when CA-only inputs are acceptable and the user values sequence recovery / fast runtime.

- Why: ProteinMPNN's repository, run script, examples, and primary paper/supplementary materials in the research findings document model_name defaults (v_48_020 among available identifiers), flags for CA-only and soluble-model operation, example sampling hyperparameters (sampling_temp, num_seq_per_target, seed), and published sequence recovery statistics referenced in the primary preprint/PMC article. These repository and paper artifacts are the primary evidence cited below.
- Alternative: oxpig-antifold
- Alternative: rfdiffusion-nim
- Evidence: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://pmc.ncbi.nlm.nih.gov/articles/PMC9997061, https://github.com/dauparas/ProteinMPNN/blob/main/examples/submit_example_4_non_fixed.sh, https://github.com/dauparas/ProteinMPNN/blob/main/LICENSE, https://docs.nvidia.com/nim/bionemo/proteinmpnn/latest/benchmarking.html

### Prefer `dauparas-proteinmpnn-suite` when The task requires design from Cα-only coordinates (input contains only CA atoms) or the user explicitly requests CA-only modeling.

- Why: The ProteinMPNN repository documents a --ca_only flag and CA-model weight locations (ca_model_weights) and the run script exposes model selection behavior; these repository artifacts in the research findings are the primary evidence for CA-only support.
- Alternative: oxpig-antifold
- Alternative: rfdiffusion-nim
- Evidence: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/README.md

### Prefer `rfdiffusion-nim` when The task requires de novo backbone generation, motif scaffolding around functional-site fragments, or binder design conditioned on target PDBs / contigs / hotspot residues.

- Why: Evidence gap: the research findings provided do not include primary-source RFdiffusion/RosettaCommons or NIM modelcard documents that would verify RFdiffusion's reported inpainting success rates, example contig syntax, or NIM packaging fidelity. The draft dossier lists RFdiffusion-related URLs (RosettaCommons repository, Baker Lab manuscript PDF, and NVIDIA NIM pages) but the research findings available to populate this dossier did not provide their canonical primary-source facts; therefore the claim that RFdiffusion is the preferred candidate for de novo backbone generation is conditioned on locating and verifying those primary sources. See evidenceGaps for precise missing locators.
- Alternative: dauparas-proteinmpnn-suite
- Alternative: oxpig-antifold
- Evidence: https://github.com/RosettaCommons/RFdiffusion, https://bakerlab.org/wp-content/uploads/2022/11/RFdiffusion_Manuscript.pdf, https://build.nvidia.com/ipd/rfdiffusion, https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/overview.html

### Prefer `rfdiffusion-nim` when A production/packaged microservice endpoint and vendor-packaged deployment are required and the user intends to use NVIDIA NIM packaging or an official microservice endpoint.

- Why: Evidence gap: the research findings set used to create this dossier does not contain primary-source vendor documentation that unambiguously proves byte-for-byte output equivalence between a named upstream RFdiffusion checkpoint and an NVIDIA NIM package version. The draft referenced NVIDIA NIM pages for RFdiffusion and for ProteinMPNN; those pages are included in the sources list below (to allow verification), but the research findings did not provide the vendor-to-upstream fidelity statements needed to validate comparability. Until those primary-vendor-to-upstream mappings are located, treat vendor-fidelity claims as gaps.
- Alternative: dauparas-proteinmpnn-suite
- Alternative: oxpig-antifold
- Evidence: https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html, https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html

### Prefer `dauparas-proteinmpnn-suite` when License or commercial-use constraints require permissive open-source licenses (MIT/BSD) and exclude vendor NIM terms or additional vendor-specific model licenses.

- Why: ProteinMPNN repository includes an explicit LICENSE file indicating the MIT License in the research findings; the RFdiffusion vendor-packaged NIM product and its terms require locating primary vendor documentation to confirm differences between upstream code/model licenses and vendor packaging terms (Evidence gap: RFdiffusion/NIM license provenance not present in research findings).
- Alternative: oxpig-antifold
- Alternative: rfdiffusion-nim
- Evidence: https://github.com/dauparas/ProteinMPNN/blob/main/LICENSE, https://github.com/RosettaCommons/RFdiffusion/blob/main/README.md

### Prefer `insufficient-evidence` when The user request is underspecified with respect to objective weighting (e.g., stability vs novelty vs sequence-recovery) or asks for both sequence recovery and novel backbone generation.

- Why: Primary-source evidence in the research findings establishes each candidate's specialization (sequence recovery and CA-only flags for ProteinMPNN; antibody-focused fine-tuning and dataset claims for AntiFold; RFdiffusion described in the draft as a backbone generator). However, no primary-source head-to-head benchmark running all three candidates on one identical protocol and dataset split was found in the provided research findings. Because relative ranking depends on task-weighting and the missing head-to-head primary evidence, prefer cannot be resolved without further canonical primary-source benchmarking. See evidenceGaps for details.
- Alternative: dauparas-proteinmpnn-suite
- Alternative: oxpig-antifold
- Alternative: rfdiffusion-nim
- Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC9997061, https://github.com/oxpig/AntiFold, https://github.com/RosettaCommons/RFdiffusion

## Benchmark taxonomy

### Fixed-backbone sequence design (inverse folding / sequence recovery)

- Datasets: Protein Data Bank (PDB) structures used in ProteinMPNN evaluations (test set: 690 monomer test cases), RosettaCommons ProteinMPNN dataset (as cited by ProteinMPNN paper and toolkit)
- Metrics: sequence recovery (percentage of residues matching native sequence) — as reported in ProteinMPNN primary evaluation, inference/runtime (seconds per redesign) — reported in ProteinMPNN evaluations
- Compare only when: Input must be full-atom PDB backbones or explicitly CA-only PDB; the input format must match the model's expected parser (ProteinMPNN helper scripts documented in repo).
- Compare only when: Model checkpoint/versionKey must match (e.g., ProteinMPNN model v_48_020 or specified soluble/ca checkpoint).
- Compare only when: Sampling hyperparameters must match (sampling_temp, num_seq_per_target, random seed).
- Compare only when: Preprocessing scripts and chain/design region assignment must match (use the same helper scripts/flags as the repository example scripts).
- Compare only when: Postprocessing (e.g., Rosetta relax or AF2 refolding) must be applied identically across evaluations to compare structural-refold metrics.

### Antibody inverse folding / CDR-focused redesign

- Datasets: SAbDab experimental Fab structures (as used in AntiFold fine-tuning/evaluation), Observed Antibody Space (OAS) predicted Fab structures (as used in AntiFold fine-tuning), AntiFold curated evaluation set: 203 Fab structures and 61 VHH structures from SAbDab (resolution <3.5 Å, ≤95% identity)
- Metrics: sequence recovery (per-residue native identity) — reported in AntiFold example outputs, CDR RMSD (Å) — AntiFold reports mean CDR RMSD in the research findings, global_score/score/perplexity as reported by AntiFold in example outputs
- Compare only when: Input must be provided as an antibody PDB or SAbDab ID with explicit heavy/light chain labels and consistent CDR indexing (IMGT or stated numbering); AntiFold expects IMGT-numbered PDBs per repository notes.
- Compare only when: Sampling temperature parameter must be identical (AntiFold example outputs use temperature T=0.20).
- Compare only when: Evaluation on antibody-specific splits (the 203 Fab / 61 VHH split) must be used for comparability.
- Compare only when: Refolding protocol (e.g., AF2 refolding) and metric computation (how CDR RMSD is computed) must match exactly across models.

### De novo backbone generation / motif scaffolding / binder design

- Datasets: Functional-site inpainting benchmark set used in RFdiffusion manuscript (25 inpainting problems), Protein Data Bank (PDB) used for RFdiffusion training as reported
- Metrics: AF2 RMSD (Å) between designed scaffold and target (reporting thresholds such as AF2 RMSD <2 Å), motif RMSD (Å) (reporting thresholds such as motif RMSD <1 Å), predicted alignment error (units as reported; thresholds such as <5), TM-score or other global structure similarity metrics only if reported identically
- Compare only when: Number of designs per problem must match (RFdiffusion reported 100 designs per problem in the draft but this must be verified against a primary source before comparison).
- Compare only when: Denoising/sampling hyperparameters must match (e.g., denoiser.noise_scale_ca, denoiser.noise_scale_frame).
- Compare only when: Input conditioning formats must match (partial PDB input_pdb or input_pdb_asset, contig map syntax as in examples, hotspot residue specifications).
- Compare only when: Postprocessing such as Rosetta energy minimization or AF2-based refolding must be applied identically if used to compute metrics.

## Primary sources

- [ProteinMPNN GitHub repository](https://github.com/dauparas/ProteinMPNN) — GitHub / dauparas; supports ProteinMPNN canonical identity and repository provenance, input modalities (PDB backbone), provided model weights (vanilla, soluble, CA-only), helper scripts, and examples
- [ProteinMPNN run script (protein_mpnn_run.py)](https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py) — GitHub / dauparas; supports CA-only flag (--ca_only), --use_soluble_model flag, model_name options and sampling flags (sampling_temp, seed) as present in the repository run script
- [ProteinMPNN example usage script](https://github.com/dauparas/ProteinMPNN/blob/main/examples/submit_example_4_non_fixed.sh) — GitHub / dauparas; supports Example usage showing sampling_temp, num_seq_per_target, and example non-fixed design script usage as present in repository examples
- [ProteinMPNN LICENSE (MIT)](https://github.com/dauparas/ProteinMPNN/blob/main/LICENSE) — GitHub / dauparas; supports ProteinMPNN license identity (MIT) as declared in the repository LICENSE file
- [ProteinMPNN PMC article / supplementary evaluation](https://pmc.ncbi.nlm.nih.gov/articles/PMC9997061) — PMC / supplementary materials; supports Detailed evaluation numbers reported in ProteinMPNN primary publication: sequence recovery statistics and dataset/test-case descriptions as included in the PMC article
- [ProteinMPNN preprint (bioRxiv)](https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf) — bioRxiv / preprint; supports ProteinMPNN preprint reporting sequence recovery values including 52.4% average recovery on a benchmark as present in the preprint PDF in the research findings
- [ProteinMPNN NVIDIA NIM benchmarking page](https://docs.nvidia.com/nim/bionemo/proteinmpnn/latest/benchmarking.html) — NVIDIA Documentation; supports Reported ProteinMPNN benchmarking number (52.4% sequence recovery) as referenced in the research findings; included here as a cited vendor doc present in the research findings
- [AntiFold GitHub repository](https://github.com/oxpig/AntiFold) — GitHub / oxpig; supports AntiFold repository identity, example outputs, installation instructions, input/output format notes and flags present in the repository
- [AntiFold arXiv preprint](https://arxiv.org/abs/2405.03370) — arXiv; supports AntiFold preprint introduction and claims (arXiv listing present in research findings)
- [AntiFold web app (OPIG)](https://opig.stats.ox.ac.uk/webapps/antifold) — OPIG (University of Oxford); supports AntiFold web app statement of intended input modality (antibody variable domain PDB or SAbDab ID), output formats (CSV/FASTA), and requirement for heavy/light chain labels as presented on the OPIG webapp page in the research findings
- [AntiFold evaluation / methods (ORA record)](https://ora.ox.ac.uk/objects/uuid:a68dbce3-e083-4a97-bb00-ecf8931d172b/files/rz316q327z) — ORA / University of Oxford record; supports AntiFold evaluation / methods claims, dataset composition (203 Fab / 61 VHH) and reported per-region recovery and RMSD statistics as provided in the research findings record
- [AntiFold example FASTA outputs (repository)](https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta) — GitHub / oxpig; supports AntiFold example FASTA outputs (temperature T=0.20), per-sample sequence recovery and scoring fields as present in the repository example file
- [AntiFold repository index.html (license badge)](https://github.com/oxpig/AntiFold/blob/master/index.html) — GitHub / oxpig; supports Repository landing page indicating a 3-Clause license statement in index.html as present in the repository
- [RFdiffusion GitHub repository (RosettaCommons)](https://github.com/RosettaCommons/RFdiffusion) — GitHub / RosettaCommons; supports RFdiffusion upstream repository identity and examples (included here as a candidate upstream repository referenced in the draft; see evidenceGaps for verification status in the provided research findings)
- [RFdiffusion manuscript (Baker Lab PDF)](https://bakerlab.org/wp-content/uploads/2022/11/RFdiffusion_Manuscript.pdf) — Baker Lab / RFdiffusion manuscript; supports RFdiffusion manuscript PDF as cited in the draft (included here to allow verification; research findings did not supply manuscript facts for RFdiffusion, see evidenceGaps)
- [RFdiffusion NIM model card (build.nvidia)](https://build.nvidia.com/ipd/rfdiffusion) — NVIDIA / Build; supports RFdiffusion NIM model card and vendor packaging landing page (included here to allow verification; research findings did not supply vendor-to-upstream fidelity facts for RFdiffusion, see evidenceGaps)
- [RFdiffusion NIM overview (NVIDIA docs)](https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/overview.html) — NVIDIA Documentation; supports RFdiffusion NIM overview and endpoints documentation (included here to allow verification; research findings did not contain the vendor fidelity statements necessary to validate reproducibility claims)
- [RFdiffusion NIM generate endpoint documentation](https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html) — NVIDIA Documentation; supports RFdiffusion NIM endpoints documentation (included here to allow verification)
- [RFdiffusion NIM benchmarking/support matrix (NVIDIA docs)](https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html) — NVIDIA Documentation; supports RFdiffusion NIM benchmarking and support-matrix pages (included here to allow verification; research findings did not include source assertions that NIM outputs exactly match upstream checkpoints)
- [RFdiffusion vendor modelcard (build.nvidia modelcard)](https://build.nvidia.com/ipd/rfdiffusion/modelcard) — NVIDIA / Build; supports RFdiffusion vendor modelcard path (included to allow verification of vendor packaging claims)
- [ProteinMPNN training README (weights and noise levels)](https://github.com/dauparas/ProteinMPNN/blob/main/training/README.md) — GitHub / dauparas; supports ProteinMPNN training README listing model weight identifiers and Gaussian noise training levels
- [ProteinMPNN README](https://github.com/dauparas/ProteinMPNN/blob/main/README.md) — GitHub / dauparas; supports ProteinMPNN README listing available weight files and CA-model weight locations
- [RFdiffusion GitHub repository (RosettaCommons) — cited revision/file](https://github.com/RosettaCommons/RFdiffusion/blob/main/README.md) — GitHub / RosettaCommons; supports Exact audited claim citation

## Evidence gaps

- No primary-source head-to-head benchmark that runs AntiFold, ProteinMPNN, and RFdiffusion on the same dataset split with identical preprocessing, sampling/postprocessing, and metric definitions — prevents direct numeric comparability.
- Evidence gap: the research findings provided did not include authoritative primary-source RFdiffusion upstream repository tables/figures or NVIDIA NIM modelcard statements that verify RFdiffusion claimed metrics (e.g., 23/25 inpainting successes) at an exact checkpoint/version; the RFdiffusion manuscript and vendor pages were listed in the draft but canonical primary assertions needed for verification were not present in the supplied research findings.
- Evidence gap: no primary source found in the supplied research findings asserting that a named NVIDIA NIM RFdiffusion package byte-for-byte reproduces outputs of a specific upstream RFdiffusion checkpoint (precise missing locator: vendor-to-upstream fidelity statement URL for NIM version → upstream checkpoint mapping).
- Evidence gap: the research findings include a ProteinMPNN vendor benchmarking page (NVIDIA docs) reporting 52.4% sequence recovery, but the precise repository checkpoint tag or exact evaluation table cell linking that vendor number to an explicit upstream checkpoint versionKey is not present in the supplied research findings; the exact upstream-checkpoint provenance for that vendor-reported number is therefore unverified in the provided findings.
- Evidence gap: the precise AF2/refolding protocol (exact AF2 version, recycles, model_ensemble, relaxation flags, seeds) used to compute RFdiffusion-reported AF2 RMSD/motif RMSD metrics was not present in the supplied research findings and thus cannot be verified.
- Evidence gap: AntiFold license provenance — while the repository index.html shows a 3-Clause license badge in the research findings, a separate canonical LICENSE file with machine-readable license text was not located in the supplied research findings; confirm repository-level license file to remove this gap if needed.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/proteinmpnn/latest/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/2.3.0/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://github.com/RosettaCommons/RFdiffusion/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://github.com/RosettaCommons/RFdiffusion/blob/main/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
