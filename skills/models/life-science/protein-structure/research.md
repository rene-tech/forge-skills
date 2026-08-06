# Protein Structure model selection

- Category: `life-science`
- Group: `protein-structure`
- Independent audit: `revised`
- Researched: `2026-07-23T20:35:31.869654+00:00`

Protein-structure prediction from amino-acid sequences for the exact Forge candidates deepmind-alphafold2-nim, facebook-esmfold-v1, and openfold3-nim. Scope includes single-sequence monomer prediction and, where primary sources document support, multimer/complex prediction, nucleotide-containing complexes, and ligand-bound prediction. Inputs are amino-acid sequences (string), optional MSAs and structural templates where accepted by the named checkpoint/wrapper, and model-specific auxiliary inputs (e.g., ligand descriptors) when explicitly supported by the named NIM or upstream repository. Outputs are predicted 3D atomic structures and model-specific confidence outputs exposed by the named checkpoint/wrapper. All capability, input, output, limit, and license statements below are drawn only from the primary sources listed in the top-level sources array; where primary sources do not provide required details, an evidence gap is recorded in evidenceGaps.

## Questions to answer before selecting

- Is the task a single-sequence monomer prediction without MSA?
- Does the task require modeling multimers or complexes including DNA/RNA or small-molecule ligands?
- Must the runtime produce CIF-format templates or mmCIF output (vs PDB-only)?
- Are strict license constraints (prefer MIT or require Apache-2.0/CC-BY-4.0/NVIDIA NIM terms) a deciding factor?

## Comparability rules

- MSA database set must be identical across models when comparing MSA-dependent methods. Primary-source default/available MSA DBs for AlphaFold2 NIM: uniref90, mgnify, small_bfd (docs.nvidia.com/nim/bionemo/alphafold2 and docs.api.nvidia.com). If unavailable for a compared model, record as a protocol mismatch (evidence gap).
- MSA search algorithm must be matched when possible (jackhmmer vs mmseqs2). AlphaFold2 NIM documents both jackhmmer and mmseqs2 selection (docs.nvidia.com/nim/bionemo/alphafold2/endpoints.html). If a model does not accept MSA inputs (e.g., ESMFold per Hugging Face), comparisons requiring MSAs are infeasible and must be flagged.
- Template-usage policy must be identical: enable/disable template search and provide identical template files (CIF/mmCIF) where supported. OpenFold3 NIM documents CIF-format template acceptance (docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, release-notes). If template guidance is unavailable for a model, treat as protocol mismatch.
- Sequence-length bounds must be matched or identical inputs chosen. AlphaFold2 NIM and associated MSA-search API document maximum input lengths (MSA-search seq length 1–4096) and AlphaFold2 NIM sequence limits (docs.nvidia.com/nim/bionemo/msa-search and build.nvidia.com/deepmind/alphafold2/modelcard). When models have different maximum sequence lengths, comparisons should be restricted to sequences within the minimum common supported length.
- For timing/throughput comparisons, ensure identical hardware and NIM/container configuration; NVIDIA docs show performance depends strongly on GPU model and system config (docs.nvidia.com/nim/bionemo/* performance pages). If identical hardware is not available or not documented, record as evidence gap.
- Random-seed, number of recycles (if applicable), number of MSA sequences used for prediction, and structural-relaxation settings must be matched. Primary sources document some MSA and prediction controls for AlphaFold2 NIM (docs.api.nvidia.com and docs.nvidia.com pages) but do not fully document exact default recycle counts or seed behaviors for all served variants — record evidence gaps for undocumented items.

## Conditional routing

### Prefer `facebook-esmfold-v1` when Monomer single-sequence inference where no MSA lookup is desired and low-latency inference is prioritized

- Why: Primary sources state ESMFold is an end-to-end single-sequence predictor that does not require MSA/database lookups and is significantly faster than alignment-based methods (Hugging Face ESMFold model card and NVIDIA NIM ESMFold modelcard).
- Alternative: deepmind-alphafold2-nim
- Alternative: openfold3-nim
- Evidence: https://huggingface.co/facebook/esmfold_v1, https://build.nvidia.com/meta/esmfold/modelcard

### Prefer `openfold3-nim` when Prediction of multimers or biomolecular complexes that include proteins plus DNA, RNA, or small-molecule ligands

- Why: OpenFold3 NIM documentation explicitly states support for biomolecular complexes composed of proteins, DNA, RNA, and ligands and documents molecule-type fields, paired MSA inputs, and CIF template support (OpenFold3 NIM overview, release notes, and example-requests).
- Alternative: deepmind-alphafold2-nim
- Alternative: facebook-esmfold-v1
- Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html

### Prefer `insufficient-evidence` when Requirement for canonical AlphaFold-style confidence metrics and structured JSON fields (ptm/ipTM/PAE) alongside PDB/mmCIF outputs for downstream automated analysis

- Why: Primary sources show AlphaFold/AlphaFold3 and OpenFold3 expose JSON confidence fields (AlphaFold JSON fields documented by EBI and AlphaFold3 docs; OpenFold3 outputs plddt/pae and a confidences JSON per OpenFold3/readthedocs), but the exact served Forge checkpoints/wrappers differ in documented output schemas and the NIM wrapper-level exposure of identical fields is inconsistently documented across the sources. Because per-field parity and canonical interpretation ranges are not fully documented for every Forge-served variant, there is insufficient primary evidence to prefer one served slug purely on 'rich confidence metadata' without further verification.
- Alternative: deepmind-alphafold2-nim
- Alternative: openfold3-nim
- Evidence: https://ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/alphafold-server-your-gateway-to-alphafold-3/interpreting-results-from-alphafold-server, https://openfold-3.readthedocs.io/en/stable/inference.html

### Prefer `facebook-esmfold-v1` when License-constrained selection favoring minimally restrictive code licensing (prefer MIT for code) or when explicit model-weights license is decisive

- Why: The ESM (ESMFold) source code in the Facebook/ESM repository is licensed under the MIT license per the repository; AlphaFold code is Apache-2.0 and AlphaFold parameters are released under CC BY 4.0 (google-deepmind/alphafold), while OpenFold3 NIM is governed by NVIDIA license(s) plus Apache-2.0 for the model per NGC/catalog entries. Exact model-weights licensing for ESMFold as served by the Forge slug is not fully documented in the primary sources used here (evidence gap).
- Alternative: deepmind-alphafold2-nim
- Alternative: openfold3-nim
- Evidence: https://github.com/facebookresearch/ESM/blob/main/esm/esmfold/v1/esmfold.py, https://github.com/google-deepmind/alphafold, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3

## Benchmark taxonomy

### monomer_structure_prediction

- Datasets: CASP
- Metrics: pLDDT (per-residue confidence; presence documented by OpenFold3 docs and AlphaFold-related JSON docs; numeric scale not specified in these primary sources), ptm/ipTM (predicted TM-score and interface predicted TM-score; existence documented in AlphaFold JSON docs), PAE/pae (predicted aligned error; existence documented by OpenFold3/AlphaFold docs)
- Compare only when: Identical MSA databases and search parameters (e.g., uniref90, mgnify, small_bfd when used) as documented for AlphaFold2 NIM; if a model does not accept MSA input (ESMFold), MSAs must be omitted for parity (protocol mismatch documented).
- Compare only when: Identical template usage (on/off and identical template files) where templates are permitted by the compared models.
- Compare only when: Identical sequence-length restrictions and selection of sequences within the common supported length envelope.
- Compare only when: Identical hardware/runtime and NIM/container configuration when comparing throughput/performance.

## Primary sources

- [AlphaFold2 NIM overview](https://docs.nvidia.com/nim/bionemo/alphafold2/latest/overview.html) — NVIDIA; supports AlphaFold2 NIM provides protein structure prediction from amino acid sequence, AlphaFold2 NIM overview and NIM-level capability statements
- [AlphaFold2 model card (NVIDIA Build)](https://build.nvidia.com/deepmind/alphafold2/modelcard) — NVIDIA / Build; supports AlphaFold2 model is available as a NIM-served variant on NVIDIA Build, Model code under Apache-2.0 and parameters under CC BY 4.0 as noted on NGC/catalog
- [AlphaFold2 (root) Forge candidate page](https://build.nvidia.com/deepmind/alphafold2) — NVIDIA / Build; supports Forge candidate canonical sourceUrl for deepmind-alphafold2-nim, High-level AlphaFold2 NIM trial service and license note
- [AlphaFold2 NIM endpoints and MSA/template inference documentation](https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html) — NVIDIA; supports Endpoints: predict-structure-from-sequence, predict-MSA-from-sequence, MSA endpoint supports uniref90 and allows jackhmmer or mmseqs2 selection
- [AlphaFold2 NIM API reference (inference)](https://docs.api.nvidia.com/nim/reference/deepmind-alphafold2-infer) — NVIDIA; supports Default MSA databases for AlphaFold2 NIM: uniref90, mgnify, small_bfd, AlphaFold2 NIM input validation (IUPAC amino-acid symbols) and MSA/prediction controls
- [AlphaFold GitHub repository (canonical)](https://github.com/google-deepmind/alphafold) — DeepMind / GitHub; supports AlphaFold code license Apache-2.0 and model parameters CC BY 4.0 (as stated in repository), Canonical upstream AlphaFold implementation
- [Hugging Face model card: facebook/esmfold_v1](https://huggingface.co/facebook/esmfold_v1) — Hugging Face / Facebook; supports ESMFold is an end-to-end single-sequence predictor that does not require MSAs, ESMFold Hugging Face canonical model card (Forge candidate canonical sourceUrl for facebook-esmfold-v1)
- [NVIDIA NIM model card: ESMFold](https://build.nvidia.com/meta/esmfold/modelcard) — NVIDIA / Build; supports NVIDIA NIM for ESMFold accepts a protein sequence up to 1024 characters and outputs PDB text, NVIDIA NIM statement that ESMFold does not require MSAs and is faster than alignment-based methods
- [Facebook/ESM GitHub (ESMFold code file, license)](https://github.com/facebookresearch/ESM/blob/main/esm/esmfold/v1/esmfold.py) — Facebook Research / GitHub; supports ESMFold source code is licensed under the MIT license
- [OpenFold3 NIM overview](https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html) — NVIDIA; supports OpenFold3 NIM can predict all-atom 3D structures of biomolecular complexes composed of proteins, DNA, RNA, and ligands, OpenFold3 NIM accepts protein and RNA MSA inputs and template CIF support (documented)
- [OpenFold3 NIM example requests (input schema and allowed fields)](https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html) — NVIDIA; supports OpenFold3 request schema including molecules list, molecule types (protein/dna/rna/ligand), sequence length bounds, msa/pai red_msa requirements, and output_format option (cif or pdb)
- [OpenFold3 NGC catalog / container entry](https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3) — NVIDIA NGC; supports OpenFold3 NIM container release and licensing notes (NVIDIA licenses and Apache-2.0 for model), Statement that OpenFold3 predicts 3D structures from amino-acid, DNA, RNA, and ligand specifiers
- [OpenFold3 release notes (selected)](https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html) — NVIDIA; supports OpenFold3 release history and features: template support added, support for protein/DNA/RNA/ligand entity types
- [OpenFold-3 readthedocs: inference outputs and confidence files](https://openfold-3.readthedocs.io/en/stable/inference.html) — OpenFold / ReadTheDocs; supports OpenFold3 inference outputs include plddt, pae, pde and a _confidences.json file; predicted structure filenames and B-factor storage for per-atom pLDDT
- [MSA-search API reference (NVIDIA MSA-search)](https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html) — NVIDIA; supports MSA-search input constraints: sequence length 1–4096, allowed amino-acid characters list, output formats a3m and fasta, defaults for max_msa_sequences and iterations
- [AlphaFold2 NIM performance and deployment notes (examples of hardware/time guidance)](https://docs.nvidia.com/nim/bionemo/alphafold2/1.2.0/performance.html) — NVIDIA; supports AlphaFold2 NIM hardware guidance and example sequence-length performance considerations
- [AlphaFold JSON interpretation (EBI AlphaFold Server training material)](https://ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/alphafold-server-your-gateway-to-alphafold-3/interpreting-results-from-alphafold-server) — EMBL-EBI; supports AlphaFold JSON includes fields ptm, iptm, ranking_score and other confidence-related fields
- [Build NGC ESMFold collection (NVIDIA catalog entry)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nim/collections/bionemo-esmfold) — NVIDIA NGC; supports NVIDIA NIM for ESMFold predicts 3D structure directly from single amino-acid sequence
- [Exact official starting source declared by Forge](https://docs.nvidia.com/nim/bionemo/openfold3/latest) — docs.nvidia.com; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Exact upstream checkpoint identifier(s) (e.g., specific checkpoint file hashes or canonical model artifact names) for the Forge-served deepmind-alphafold2-nim variant are not documented in the provided primary sources. The NGC/Build pages note model availability and that parameters are downloaded on startup but do not publish a specific upstream checkpoint identifier (see build.nvidia.com/deepmind/alphafold2 and docs.nvidia.com/nim/bionemo/alphafold2).
- Evidence gap: Exact upstream checkpoint identifier(s) for the Forge-served openfold3-nim variant are not documented in the provided primary sources. The NGC/catalog entry and docs describe the container and included weights but do not list a specific upstream checkpoint name or hash (see catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3 and https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html).
- Evidence gap: Model-weights license for facebook-esmfold-v1 as served by the Forge slug is not explicitly stated in the provided primary sources. The ESM source code file indicates an MIT license for code (github.com/facebookresearch/ESM/...), but Hugging Face model card and NVIDIA NIM pages in the provided findings do not state the weights license for the served artifact.
- Evidence gap: Exact numeric benchmarks (accuracy metrics such as GDT_TS, RMSD, per-target values) published for the exact Forge-served checkpoints/versions deepmind-alphafold2-nim, facebook-esmfold-v1 (as served by Forge), and openfold3-nim are not present in the provided primary sources. Papers and model cards document general performance claims and training datasets, but the findings do not contain per-checkpoint numeric benchmark tables tied to the exact Forge-served variants (e.g., the NIM-wrapped checkpoint + NIM version).
- Evidence gap: Exact default random-seed behavior, per-run deterministic guarantees, and explicit documented default recycle counts for the Forge-served AlphaFold2 NIM and OpenFold3 NIM variants are not fully specified in the provided primary sources. The AlphaFold2 NIM API reference mentions a parameter controlling network trunk runs with different MSA cluster centers but does not fully document default seed/recycle values in the provided findings.
- Evidence gap: Exact interpretation ranges/scales and authoritative recommended thresholds for pLDDT, ptm/ipTM, and PAE as exposed by each Forge-served variant are not fully specified across the provided primary sources. While fields are present (OpenFold3 and AlphaFold JSON docs), numeric-scale grounding and recommended thresholds (e.g., numeric cutoffs) are not present in the findings used here.
- Evidence gap: For ESMFold served by the Forge slug, the provided primary sources do not document the presence or format of per-residue confidence metrics (e.g., pLDDT) in the NIM-served output. NVIDIA ESMFold NIM documentation documents PDB output and single-sequence operation but does not detail confidence JSON outputs in the provided findings.
- Evidence gap: Exact MSA search default parameters (complete list of defaults, full command-line or API-body examples for production runs) and the full list of databases used by OpenFold3 NIM for MSA search are not comprehensively documented in the provided findings. AlphaFold2 NIM MSA defaults (uniref90, mgnify, small_bfd) are documented, but OpenFold3 explicit MSA database naming is not completely enumerated in the findings.
- Evidence gap: End-to-end, directly comparable accuracy benchmarks run under identical protocol (identical MSA DBs, identical template files, identical seed/recycle settings) across the three exact Forge-served slugs are not available in the provided primary sources; therefore head-to-head accuracy routing based on numerical superiority is not supported by the evidence here.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarkTaxonomy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparabilityRules Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property decisionRules Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property Are complex inputs present (multimers, nucleic acids, ligands) that require OpenFold3-NIM’s or another model’s special capabilities? Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property Do you require outputs in PDB, mmCIF, or both formats, and do you need accompanying json confidence data?], Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property Is template usage required, optional, or disallowed for your task? Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property completeness and reproducibility constraint: Will you require identical preprocessing steps (MSA search settings, templates, recycles, seeds) across models for benchmarking? Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://docs.nvidia.com/nim/bionemo/openfold3/latest: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
