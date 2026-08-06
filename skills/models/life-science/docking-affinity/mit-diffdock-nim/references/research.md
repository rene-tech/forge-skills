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

- Research key: `build-nvidia-com-mit-diffdock-7ae8526856`
- Independent audit: `revised`
- Researched: `2026-07-23T21:04:35.348946+00:00`

Primary NVIDIA NIM documentation (model card, deployment examples, API reference, release notes) and the canonical upstream DiffDock materials (author repository and arXiv preprint) were inspected. The NIM-packaged artifact identified as DiffDock v2.2.0 is documented on the NVIDIA model card; NVIDIA NIM documentation and deployment examples document API request/response field names and that the service generates ranked docked poses and per-pose confidence scores. Upstream DiffDock papers and repository describe the underlying algorithmic approach (reverse diffusion over molecular pose/orientation/torsion and a learned confidence model). Primary sources do not report an immutable checkpoint checksum or revision identifier for the NIM-served weights (revision not reported). Primary sources also do not publish numeric calibration mapping of reported confidence values to RMSD or success probability, nor do they publish benchmark tables explicitly tied to the exact NIM-served checkpoint; these remain evidence gaps and are enumerated below with the exact primary locators checked.

## Identity

- Upstream name: DiffDock
- Checkpoint/version: v2.2.0
- Immutable revision: not reported
- Parameter scale: 20 million parameters
- Architecture/head: Score‑Based Diffusion Model (3D equivariant graph neural network / graph convolution neural network)
- License: NVIDIA Open Model License; MIT (upstream)
- Evidence: https://build.nvidia.com/mit/diffdock/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/mit/containers/diffdock/-, https://github.com/gcorso/DiffDock

## Selection

### Recommended

- **Generate blind docking poses of small‑molecule ligands against a provided protein structure for downstream validation workflows (pose sampling and ranking).** — NVIDIA's DiffDock model card documents the model's purpose as predicting 3D protein–ligand binding poses and states that the model outputs sampled poses ranked by a Confidence model; the NIM API and deployment examples expose a pose-generation endpoint and example response fields for ranked poses and confidence scores. Upstream DiffDock paper and canonical repository describe the score-and-confidence architecture that underlies pose sampling and ranking.
  Scope: mit-diffdock-nim (NIM-packaged DiffDock v2.2.0) with upstream algorithmic evidence from the canonical DiffDock repository and paper.
  Evidence: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html, https://arxiv.org/abs/2210.01776

### Conditional

- **Throughput-oriented batch docking (submitting multiple ligands for docking against one receptor in a single workflow request).** — Primary NIM release notes and versioned documentation indicate support for multi-line SMILES and adaptive batch sampling added in earlier releases; callers must validate per-request batch limits, timeout behavior, and any deployment-specific request-size constraints because numeric limits (maximum molecules per request, max characters, per-field bounds) are not published in the inspected primary API docs.
  Scope: mit-diffdock-nim (NIM packaging and runtime behavior documented across NIM release-notes and versioned advanced-usage pages); batch-support description is from NIM release notes (1.2.0) and advanced-usage doc variants rather than an immutable upstream checkpoint claim.
  Evidence: https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/diffdock/1.2.0/configure-nim.html, https://build.nvidia.com/mit/diffdock/deploy

### Avoid

- **Use as the sole evidence source for clinical decision-making or safety‑critical drug development without orthogonal experimental validation and expert review.** — NVIDIA model card and NIM documentation describe pose generation and confidence ranking but do not provide clinical‑grade guarantees, numeric calibration of confidence scores to experimental success metrics, or immutable checkpoint checksums tying a published benchmark to the exact NIM-served artifact.
  Scope: mit-diffdock-nim (NIM-packaged DiffDock v2.2.0)
  Evidence: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html

## Input preparation

### Semantic inputs

- Protein input: 3D protein structure in PDB format (text) is accepted as the receptor input for docking. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://build.nvidia.com/mit/diffdock/deploy
- Ligand input: ligand molecules may be provided as SDF-formatted payloads and ligand-file-type metadata is used to indicate format; multiple-ligand input support is documented in NIM release notes and deployment examples. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://build.nvidia.com/mit/diffdock/deploy, https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html

### Accepted formats

- Accepted ligand file types and payload indicators include SDF (explicit example in deployment JSON) and ligand_file_type metadata is present in example deploy payloads; multi-line SMILES batch support was added in NIM release history. Sources: https://build.nvidia.com/mit/diffdock/deploy, https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html
- Protein structures are accepted in PDB text form as the receptor input. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://build.nvidia.com/mit/diffdock/deploy

### Preprocessing

- Upstream DiffDock preprocessing constructs a protein–ligand graph from 3D coordinates and performs reverse diffusion over molecular position, orientation, and torsion; this is described in the canonical DiffDock paper and repository as upstream algorithmic behavior. Sources: https://arxiv.org/abs/2210.01776, https://github.com/gcorso/DiffDock
- NIM deployment examples document the request payload fields used by the service (e.g., ligand, ligand_file_type, protein, num_poses, time_divisions, steps, save_trajectory, is_staged) and example response field names, indicating server-side handling of those fields; exact server-side conformer-generation implementation details (tooling, versions, parameters) are not specified in the inspected docs. Sources: https://build.nvidia.com/mit/diffdock/deploy, https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html

### Pre-submit validation

- NIM deployment examples and API reference document required inference request fields (ligand, ligand_file_type, protein) and the pose-generation endpoint; clients should validate that required fields are present and conform to expected formats before submission. Sources: https://build.nvidia.com/mit/diffdock/deploy, https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html
- Evidence gap: The inspected primary API and deployment documentation do not publish explicit numeric bounds, maximum batch sizes, per-field character/byte limits, or definitive per-request maxima; callers must treat these limits as unspecified and verify them against their deployed NIM instance. Sources: https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html, https://build.nvidia.com/mit/diffdock/deploy, https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html

### Task-specific formatting

- Official example request JSON payload fields demonstrated in NIM deployment examples include `ligand`, `ligand_file_type`, `protein`, `num_poses`, `time_divisions`, `steps`, `save_trajectory`, and `is_staged`; the API exposes a POST generation endpoint for pose generation (`/molecular-docking/diffdock/generate`). Sources: https://build.nvidia.com/mit/diffdock/deploy, https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html

## Output interpretation

### Outputs

- NIM outputs include ranked ligand poses returned as SDF-format pose strings and lists of per-pose numeric confidence values; the model card and deployment examples list output types including ligand 3D positions (SDF), protein PDB text, and a 1‑D array of confidence scores. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://build.nvidia.com/mit/diffdock/deploy
- Example response field names shown in deployment examples include `ligand_positions` and `position_confidence` as payload elements representing pose SDF strings and per-pose confidence arrays respectively. Sources: https://build.nvidia.com/mit/diffdock/deploy

### Interpretation

- DiffDock provides per-pose confidence scores that are used to rank sampled poses; upstream DiffDock materials describe a learned confidence model for pose ranking but do not publish a formal numeric calibration linking the reported confidence value to experimental RMSD or success probability for the NIM-served artifact. Sources: https://arxiv.org/abs/2210.01776, https://build.nvidia.com/mit/diffdock/modelcard
- Evidence gap: No inspected primary source specifies a numeric mapping or recommended threshold (e.g., a `position_confidence` cutoff corresponding to an RMSD or probability) for decision-making for the exact NIM-served checkpoint. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html, https://arxiv.org/abs/2210.01776

### Post-inference validation

- Post-inference validation should verify that returned pose payloads are syntactically valid SDF strings and that the number of returned poses matches the `num_poses` requested in the request payload, per the structure shown in deployment examples. Sources: https://build.nvidia.com/mit/diffdock/deploy
- Evidence gap: The inspected primary sources do not publish formal calibration procedures, numeric quality thresholds, or statistical validation protocols tied to the exact NIM-served checkpoint; downstream validation with experiments or orthogonal computational methods is required for high-stakes uses. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- DiffDock is designed for blind docking of single small‑molecule ligands and operates on static protein structures; performance may degrade for multi‑ligand competition, dynamic ensemble effects, or solvent‑mediated multi‑ligand interactions. Sources: https://build.nvidia.com/mit/diffdock/modelcard
- Evidence gap: No primary-source numeric benchmark tables or performance metrics explicitly tied to the exact NIM-served checkpoint (v2.2.0) were found in the inspected primary materials; see evidenceGaps for exact locators checked. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html, https://arxiv.org/abs/2210.01776

### Safety

- Evidence gap: The inspected primary NVIDIA model card and NIM documentation do not provide a model-specific mandatory human‑in‑the‑loop safety policy or prescriptive clinical‑use restrictions; users must apply domain expert review and experimental validation before using outputs in safety‑critical contexts. Sources: https://build.nvidia.com/mit/diffdock/modelcard, https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's DiffDock NIM skill documents receptor ATOM-record preparation, SMILES/SDF ligand handling, hosted/local path differences, ranked pose artifacts, confidence interpretation, validation, and failure modes. The exact Forge route and deployed NIM version still come from Forge.
- [diffdock-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/diffdock-nim)

### `related-multi-model-pipeline`

The NVIDIA BioNeMo drug-discovery meta-skill composes GenMol, DiffDock, and Boltz2. Use it as a workflow template only after independently selecting exact Forge versions, reconciling SAFE/SMILES and structure artifacts at every boundary, and validating each intermediate result; it is not a head-to-head quality benchmark.
- [drug-discovery-pipeline](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/meta-skills/drug-discovery-pipeline)

### `related-cheminformatics-validation`

NVIDIA BioNeMo's nvMolKit skill is related GPU-batched cheminformatics guidance for fingerprints, similarity, conformers, force-field optimization, clustering, and substructure checks. Use it for large-batch ligand or generated-molecule validation when installed; it does not establish any model's request schema, quality, or Forge runtime behavior, and plain RDKit is generally more appropriate for one-off molecules.
- [nvmolkit-usage](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/nvMolKit)

## Primary sources

### NVIDIA DiffDock model card (Forge/NIM listing)

- URL: https://build.nvidia.com/mit/diffdock/modelcard
- Publisher: NVIDIA / Forge build
- Type: `model-card`
- Primary because: NVIDIA-provided model card describing the NIM-packaged DiffDock, reported released model version, output types, parameter count, and license information used to verify NIM-level identity and usage claims.
- Scope: mit-diffdock-nim (NIM model card)
- Supports: Released model version v2.2.0
- Supports: Output types (SDF poses, PDB protein text, per-pose confidence arrays)
- Supports: Parameter count (Score model ~20 million parameters)
- Supports: License statement (NVIDIA Open Model License; MIT upstream)

### NGC catalog entry for MIT DiffDock (tags)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/mit/containers/diffdock/-
- Publisher: NVIDIA NGC
- Type: `repository`
- Primary because: NGC container metadata and catalog entry used to corroborate NIM container naming patterns and NIM packaging claims in NVIDIA documentation.
- Scope: mit-diffdock-nim (NGC catalog / container metadata)
- Supports: NIM container image tag pattern and NIM packaging metadata
- Supports: Statements about NIM container deployment and global availability

### NVIDIA NIM DiffDock overview (latest)

- URL: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html
- Publisher: NVIDIA documentation
- Type: `official-documentation`
- Primary because: Official NIM overview describing the NIM-packaged DiffDock behavior and accepted modalities; used to corroborate NIM-level functionality and high-level inputs/outputs.
- Scope: mit-diffdock-nim (NIM overview / latest)
- Supports: High-level description of DiffDock as blind docking model
- Supports: Statement that DiffDock does not require a predefined binding pocket
- Supports: General statements about inference and confidence estimates

### NVIDIA NIM DiffDock API reference (v2.0.1)

- URL: https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html
- Publisher: NVIDIA documentation
- Type: `official-documentation`
- Primary because: Versioned API reference documenting the pose-generation endpoint and used to corroborate the POST generation endpoint and API contract structure.
- Scope: mit-diffdock-nim (API reference v2.0.1)
- Supports: POST /molecular-docking/diffdock/generate endpoint for pose generation

### NVIDIA NIM DiffDock release notes (v2.1.0)

- URL: https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html
- Publisher: NVIDIA documentation
- Type: `official-documentation`
- Primary because: Versioned release notes used to verify feature additions across versions (e.g., batch SMILES support, adaptive batch sampling) and runtime dependency changes.
- Scope: mit-diffdock-nim (release notes v2.1.0 and referenced v1.2.0/2.0.1 history)
- Supports: Release 2.1.0 notes (improved reporting on failed docking requests, TritonServer removal)
- Supports: Release history noting that 1.2.0 added multi-line SMILES batch docking support and adaptive batch-sampling

### NVIDIA NIM configure and runtime guidance (latest)

- URL: https://docs.nvidia.com/nim/bionemo/diffdock/latest/configure-nim.html
- Publisher: NVIDIA documentation
- Type: `official-documentation`
- Primary because: Deployment/runtime guidance used to corroborate NIM container runtime flags and environment variables relevant to NIM deployment.
- Scope: mit-diffdock-nim (configure/runtime guidance latest)
- Supports: NIM container runtime flags and environment-variable configuration guidance

### NVIDIA NIM DiffDock configure (v1.2.0)

- URL: https://docs.nvidia.com/nim/bionemo/diffdock/1.2.0/configure-nim.html
- Publisher: NVIDIA documentation
- Type: `official-documentation`
- Primary because: Versioned configure documentation used to corroborate historical NIM runtime and API behavior (used to verify the introduction of features such as multi-line SMILES handling).
- Scope: mit-diffdock-nim (configure v1.2.0)
- Supports: Documentation indexing and runtime configuration for NIM v1.2.0
- Supports: Historical evidence of multi-line SMILES batch-docking support

### Canonical DiffDock repository (author-maintained)

- URL: https://github.com/gcorso/DiffDock
- Publisher: GitHub
- Type: `repository`
- Primary because: Canonical upstream DiffDock codebase used to verify upstream preprocessing and algorithmic descriptions (graph construction, diffusion over pose/orientation/torsion) and repository provenance.
- Scope: upstream DiffDock (canonical repository)
- Supports: Upstream code and CLI repository for DiffDock
- Supports: Algorithmic and preprocessing details for the upstream checkpoint

### DiffDock paper (ICLR 2023 preprint)

- URL: https://arxiv.org/abs/2210.01776
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical DiffDock research paper describing the score-and-confidence architecture, reverse diffusion over pose/orientation/torsion, and the learned confidence model used as upstream algorithmic evidence.
- Scope: upstream DiffDock (paper / algorithmic description)
- Supports: Diffusion-based pose-generation algorithm and learned confidence model
- Supports: Upstream description of preprocessing and pose-sampling approach

### NVIDIA DiffDock deployment and example payloads

- URL: https://build.nvidia.com/mit/diffdock/deploy
- Publisher: NVIDIA / Forge build
- Type: `official-documentation`
- Primary because: Deployment example JSON requests and example response field names used to verify API request/response field names and example payload structure.
- Scope: mit-diffdock-nim (deployment examples)
- Supports: Example inference JSON request fields (ligand, ligand_file_type, protein, num_poses, time_divisions, steps, save_trajectory, is_staged)
- Supports: Example response field names (e.g., ligand_positions, position_confidence)

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/mit/diffdock
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: mit-diffdock
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Immutable checkpoint checksum or revision identifier for the NIM-served weights is not reported in inspected primary sources; checked: https://build.nvidia.com/mit/diffdock/modelcard (model card: release/version metadata), https://catalog.ngc.nvidia.com/orgs/nim/mit/containers/diffdock/- (NGC catalog), and https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html (release notes) and found no published checksum or immutable revision locator.
- Evidence gap: No primary-source numeric calibration mapping `position_confidence` to RMSD or explicit success probability for the exact NIM-served checkpoint; checked: https://build.nvidia.com/mit/diffdock/modelcard (model card output/confidence description), https://arxiv.org/abs/2210.01776 (upstream paper describing learned confidence model), and https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html (release notes) and found no numeric calibration.
- Evidence gap: No primary-source publication of benchmark tables or numeric performance metrics explicitly tied to the exact NIM-served checkpoint (v2.2.0); checked: https://build.nvidia.com/mit/diffdock/modelcard (model card headings and content), https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html (release notes and history), and https://arxiv.org/abs/2210.01776 (upstream paper) and found no benchmark table that names the exact NIM checkpoint or provides protocol-matching numeric results for the NIM-served artifact.
- Evidence gap: No primary-source numeric limits for per-request batch sizes, maximum molecules per request, or per-field character/byte bounds are published in the inspected API and deployment documentation; checked: https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html (API reference), https://build.nvidia.com/mit/diffdock/deploy (deployment examples), and https://docs.nvidia.com/nim/bionemo/diffdock/1.2.0/configure-nim.html (versioned docs) and found no numeric maxima.
- Evidence gap: No protocol-matching, primary-source comparisons between this exact NIM-served checkpoint and other Forge candidates were found; checked: https://build.nvidia.com/mit/diffdock/modelcard (model card), https://docs.nvidia.com/nim/bionemo/diffdock/2.1.0/release-notes.html (release notes), and https://arxiv.org/abs/2210.01776 (upstream paper) and did not find side-by-side comparisons tied to the exact NIM artifact.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 59 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property acceptedFormats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property preprocessing Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property taskSpecificFormatting Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property validation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property acceptedFormats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property preprocessing Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property taskSpecificFormatting Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: missing required property validation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA: $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/mit/diffdock Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/mit/diffdock/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/mit-diffdock Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/mit/containers/diffdock/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara/models/diffdock_score Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://zenodo.org/records/7778651 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://cap.csail.mit.edu/sites/default/files/research-pdfs/DiffDock-%20Diffusion%20Steps,%20Twists,%20andTurns%20for%20Molecular%20Docking.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/configure-nim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/mit/diffdock/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/mit/containers/diffdock/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/mit-diffdock Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/UFResearchComputing/DiffDock-NIM Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/1.2.0/advanced-usage.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/1.2.0/advanced-usage.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://cap.csail.mit.edu/sites/default/files/research-pdfs/DiffDock-%20Diffusion%20Steps,%20Twists,%20andTurns%20for%20Molecular%20Docking.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/overview.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/advanced-usage.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/2.0.1/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/diffdock/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/UFResearchComputing/DiffDock-NIM Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/mit/diffdock: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
