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

- Research key: `docs-nvidia-com-nim-bionemo-openfold3-latest-fcfde9d30f`
- Independent audit: `revised`
- Researched: `2026-07-23T22:12:16.408591+00:00`

I verified official NVIDIA NIM documentation and upstream OpenFold3 references. The OpenFold3 NIM is an NVIDIA-packaged inference container exposing an OpenFold3-based protein/nucleic-acid/ligand co-folding service with CIF/PDB outputs, confidence scores, and an optimized TensorRT-backed inference backend. Primary NVIDIA docs define input JSON fields, allowed MSA formats, template support introduced in a named NIM release, a diffusion_samples parameter (NIM default 1, upstream default 5), and runtime performance speedups. The NIM documentation does not publish an immutable upstream checkpoint identifier proving bitwise identical weights to an upstream checkpoint; upstream OpenFold3 docs report a default checkpoint name (openfold3_p2_v1) but I cannot verify the NIM serves that identical named checkpoint from the available primary sources. There is no primary-source numeric calibration mapping confidence scores to expected accuracy for the exact NIM-served checkpoint. I list explicit evidence or evidence gaps for every required dossier field.

## Identity

- Upstream name: OpenFold3
- Checkpoint/version: not reported (NIM does not publish an immutable checkpoint identifier; upstream default checkpoint name observed as "openfold3_p2_v1" in upstream inference docs)
- Immutable revision: not reported
- Parameter scale: 3.68×10⁸ parameters
- Architecture/head: AlphaFold3 (Protein Structure Prediction)
- License: Upstream code/model repo: Apache-2.0; Packaged/serving: NVIDIA Open Model License and NVIDIA Software License / NIM product terms
- Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/, https://build.nvidia.com/openfold/openfold3/modelcard, https://github.com/aqlaboratory/openfold-3, https://openfold-3.readthedocs.io/en/stable/inference.html, https://nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3

## Selection

### Recommended

- **Predicting all-atom 3D structures of biomolecular complexes composed of proteins, DNA, RNA, and non-covalent ligands for research and discovery workflows.** — NVIDIA NIM overview and modelcard state the OpenFold3 NIM predicts all-atom 3D structures of complexes including proteins, DNA, RNA, and ligands and provides confidence scores; NVIDIA NIM packaging provides an accelerated inference backend for these tasks.
  Scope: OpenFold3 NIM packaged container / OpenFold3 model (NIM runtime)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3
- **Generating multiple independent structure predictions per request (ensemble-style sampling) via the diffusion_samples parameter.** — NIM documentation documents diffusion_samples as an inference parameter that controls the number of independent structures to generate and example requests use this parameter.
  Scope: OpenFold3 NIM request API (service-level sampling)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- **Accelerated inference on NVIDIA GPUs using the TensorRT-optimized backend within the NIM container for lower latency vs the open-source baseline.** — NVIDIA NIM performance pages report speedups versus the open-source OpenFold3 baseline and catalog/model pages describe an NVIDIA-optimized inference backend.
  Scope: OpenFold3 NIM container with TensorRT engines (runtime/operational evidence)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/performance.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3

### Conditional

- **Using structural templates (CIF-format) to guide protein predictions when templates are available and supported by the NIM release.** — Template inputs are release-dependent; templates were introduced in the NIM lineage starting at release 1.1.0 and NIM example requests and release-notes describe CIF-format constraints. Confirm the exact NIM version in use supports templates before relying on them.
  Scope: OpenFold3 NIM (template support introduced in 1.1.0 per NIM release notes)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/1.1.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html
- **Accepting ligand inputs for non-covalent small-molecule modeling when using the NIM; avoid assuming covalent ligand modeling is supported.** — NIM docs and upstream inference docs state ligands are accepted via SMILES or CCD codes and that covalent ligand modeling is planned/not currently supported; verify capabilities for the exact NIM release before attempting covalent modeling.
  Scope: OpenFold3 inference (upstream) and OpenFold3 NIM (serving runtime)
  Evidence: https://openfold-3.readthedocs.io/en/stable/inference.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html

### Avoid

- **Modeling covalently bound ligands (covalent docking) relying on NIM or current OpenFold3 inference.** — Primary sources indicate ligand inputs are accepted as SMILES or CCD and that covalent ligand support is planned but not currently available in upstream inference and NIM documentation.
  Scope: OpenFold3 NIM / OpenFold3 upstream inference
  Evidence: https://openfold-3.readthedocs.io/en/stable/inference.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html
- **Relying on the NIM to perform automatic online MSA pairing (i.e., assuming the service will fetch and pair MSAs automatically without user-provided MSAs).** — NIM release notes and API docs indicate MSAs are accepted and required for protein/RNA, and that supported MSA types include paired/unpaired inputs; the docs do not claim the NIM will perform automatic online pairing for all use cases—users must provide MSAs or follow the documented MSA modes.
  Scope: OpenFold3 NIM API
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- **Assuming numeric calibration thresholds that map per-structure confidence scores to precise expected positional accuracy for the exact NIM-served checkpoint.** — Primary sources do not publish a numeric confidence-to-accuracy mapping for the exact NIM-served checkpoint.
  Scope: OpenFold3 NIM / upstream inference
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard

## Input preparation

### Semantic inputs

- Accepted top-level biomolecular entity types: protein, dna, rna, and ligand. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- Ligand inputs are specified either as SMILES or CCD codes (mutually exclusive), representing non-covalent ligands per current docs. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- MSA inputs are required for protein and RNA entity types in the NIM; protein MSAs may be paired or unpaired depending on the input. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html

### Accepted formats

- Accepted MSA file formats: a3m and csv (lowercase), provided inside AlignmentFileRecord objects with an 'alignment' string field. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- Structural templates (when supported) must be provided in CIF (mmCIF/CIF) format for protein templates (template support introduced in NIM release 1.1.0). Sources: https://docs.nvidia.com/nim/bionemo/openfold3/1.1.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- Output file formats supported by the NIM: 'cif' (default) and 'pdb'. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html

### Preprocessing

- MSA modes described across upstream and NIM docs include precomputed MSAs and MSA-free inference; upstream inference docs also reference a ColabFold server mode. The NIM accepts user-provided MSAs and documents supported MSA formats and pairing types; NIM example-requests and release-notes document these modes. Sources: https://openfold-3.readthedocs.io/en/stable/inference.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html
- NIM packaging pulls model assets and prepares an optimized inference backend; the NIM container is documented as shipping an NVIDIA-optimized inference backend (TensorRT engines) for faster predictions. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3, https://build.nvidia.com/openfold/openfold3/deploy
- MSA database/count limits and global depth limits are documented in NVIDIA materials: up to three MSA databases per protein and a maximum global MSA depth of 500 sequences are described in NIM preprocessing/msa references. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html

### Pre-submit validation

- Request-level validation rules from NIM example-requests: 'inputs' is required and must contain exactly one input specification; 'molecules' is required and must be a list containing at least one molecule specification. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- Field-specific validation in example requests: 'input_id' is optional, defaults to 'input_id_0', and may be up to 128 characters; 'id' (chain id) is a string or list of chain identifiers each 1–4 alphanumeric characters. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- AlignmentFileRecord validation: 'alignment' (MSA content) is required, 'format' must be either 'a3m' or 'csv' (lowercase), and 'rank' is optional with default –1 indicating ordering rank for concatenation. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- MSA requirement: MSA is required for protein and RNA entity types per NIM release notes; users must supply MSAs per documented formats and pairing options. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html

### Task-specific formatting

- Example request payloads use a top-level 'inputs' array containing objects with fields such as 'input_id', 'molecules' (each with 'type' and 'sequence'), optional 'diffusion_samples', and optional 'output_format'. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- The 'diffusion_samples' inference parameter is documented in NIM release-notes and example-requests as an integer with allowed range 1–5 and a default of 1 in NIM docs; upstream OpenFold3 inference docs state an upstream default of 5, producing an explicit discrepancy between NIM docs and upstream default. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html, https://openfold-3.readthedocs.io/en/stable/inference.html
- Output format field 'output_format' defaults to 'cif' and may be set to 'cif' or 'pdb' per NIM example requests. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html

## Output interpretation

### Outputs

- Supported structure output file types from the NIM: CIF (default) and PDB; examples and release-notes indicate CIF is the default output format. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- The service emits multiple structure predictions per request when diffusion_samples>1; each structure is returned as a separate file (CIF/PDB) and the service provides per-structure confidence scores. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html

### Interpretation

- NIM documentation refers to 'confidence scores' for predicted structures but does not publish a numeric mapping from those scores to expected positional accuracy for the exact NIM-served checkpoint; therefore quantitative calibration is not provided in the NIM primary sources. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard
- Upstream OpenFold3 inference docs specify upstream defaults and sampling behavior (e.g., upstream default diffusion sample count), but the NIM may override defaults; interpret confidence scores cautiously and verify calibration for the exact runtime/checkpoint before using thresholds. Sources: https://openfold-3.readthedocs.io/en/stable/inference.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html

### Post-inference validation

- Post-inference checks recommended by the available docs: validate output file format correctness (CIF/PDB), and confirm that the number of returned structure files matches diffusion_samples. The NIM example responses and API health check behaviors provide structural output examples to validate service functioning. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/getting-started.html
- Evidence gap: The NIM documentation does not publish a numeric, per-checkpoint calibration mapping (confidence→expected RMSD/TM-score) for the exact NIM-served weights; I could not find such calibration in the checked primary sources. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard

## Public benchmarks

### NIM runtime inference speedup vs open-source OpenFold3 baseline

- Dataset/split: NIM internal performance tests (no public benchmark dataset listed) / not reported
- Metric/value: inference speedup (ratio) / 1.15×–1.69× (range reported by NIM performance pages) (`higher-is-better`)
- Model scope: OpenFold3 NIM container performance (runtime operational benchmark)
- Conditions: Reported as NIM container performance tests versus open-source OF3 baseline; template processing overheads and sequence-length scaling described in performance pages.
- Source: https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/performance.html
- Locator: Performance page tables/figures and text describing speedups and template overhead
- Caveat: These are runtime/operational performance claims for the NIM container, not accuracy benchmarks for the served model weights.
- Caveat: Protocol details (hardware, dataset, exact inputs) are described in the performance page but are NIM test conditions and may not match independent academic benchmarks.

## Comparisons

### AlphaFold3 — `insufficient-evidence`

- Task: Task-level comparison (structure prediction quality and calibration) between OpenFold3 NIM-served checkpoint and AlphaFold3
- Criteria: No primary-source, protocol-matched side-by-side accuracy benchmarks tying the exact NIM-served checkpoint to AlphaFold3 under the same dataset/splits and evaluation metrics were found.
- Rationale: NVIDIA docs and upstream OpenFold3 materials describe model lineage and capabilities but do not provide protocol-matched, checkpoint-identical numeric accuracy comparisons against AlphaFold3 for the NIM-served checkpoint.
- Comparison conditions: Would require identical checkpoint identities, datasets/splits, evaluation metrics, and matching inference protocols; these are not present in the checked primary sources.
- Evidence: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard, https://openfold-3.readthedocs.io/en/stable/inference.html

## Limitations and safety

### Limitations

- No immutable NIM-served upstream checkpoint identifier published: the NIM documentation does not publish a verifiable, immutable checkpoint identifier proving bitwise-identical upstream weights; upstream OpenFold3 docs do report a default checkpoint name but do not confirm the NIM serves that exact named checkpoint. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/, https://openfold-3.readthedocs.io/en/stable/inference.html, https://build.nvidia.com/openfold/openfold3/modelcard
- No numeric confidence-to-accuracy calibration published for the exact NIM-served checkpoint: NIM and Nvidia modelcard do not provide a numeric mapping from confidence scores to expected positional accuracy for the served checkpoint. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard
- Release-dependent feature availability (MSA, template, telemetry, diffusion defaults): key capabilities (template support, telemetry defaults, diffusion_samples default) vary by NIM release; confirm the exact NIM version before relying on a feature. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/1.1.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html

### Safety

- Telemetry and minimal anonymous metadata collection are documented for NIM release 1.3.0 and telemetry is disabled by default; telemetry collects hardware type and NIM version and does not collect user input sequences or prediction results per the release-notes. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- Model and container licensing distinctions must be observed: upstream OpenFold3 code is Apache-2.0 licensed, while the packaged NIM container is governed by NVIDIA product and model license terms; users must comply with NVIDIA Open Model License and NIM product-specific terms when distributing or deploying the packaged model. Sources: https://github.com/aqlaboratory/openfold-3, https://nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license, https://build.nvidia.com/openfold/openfold3
- Evidence gap: The NIM documentation does not publish an explicit clinical/medical-use safety or regulated-deployment policy for the OpenFold3 NIM; I could not find primary-source instructions requiring human review, disclaimers for clinical use, or data-protection specifics beyond telemetry descriptions in the checked NVIDIA docs. Sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html, https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's OpenFold3 skill documents multi-entity protein/nucleic-acid/ligand requests, MSA/template controls, output and confidence artifacts, scientific validation, and hosted/local operation. Use Forge's exact request route, source image, support matrix, and deployment contract.
- [openfold3-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/openfold3-nim)
- [cuEquivariance](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/cuEquivariance)

### `related-multi-model-pipeline`

The NVIDIA BioNeMo MSA-to-OpenFold3 meta-skill documents the A3M handoff between MSA Search and structure prediction. Treat its fixed examples as a workflow template; verify database choices, sequence/entity schema, MSA depth, exact Forge routes, and returned artifacts for the selected versions.
- [msa-structure-prediction-pipeline](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/meta-skills/msa-structure-prediction-pipeline)

## Primary sources

### OpenFold3 NIM documentation (latest)

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/latest/
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM documentation root for the OpenFold3 serving variant covered by the dossier.
- Scope: OpenFold3 NIM serving documentation and examples
- Supports: Serving runtime identity, API reference, example requests, and overview claims

### OpenFold3 NIM overview

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: NVIDIA overview page describing supported inputs, outputs, and high-level capabilities of the OpenFold3 NIM.
- Scope: OpenFold3 NIM overview claims
- Supports: Supported biomolecular types, confidence scores, service capabilities

### OpenFold3 NIM example requests

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Concrete API request/response examples and field-level validation rules for the NIM request schema.
- Scope: API request field semantics, defaults, and formats
- Supports: input field constraints, default values (diffusion_samples, output_format, input_id), AlignmentFileRecord format

### OpenFold3 NIM release notes (latest aggregated)

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/latest/release-notes.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Release notes documenting feature introductions, telemetry, and behavioral changes across NIM releases.
- Scope: NIM versioned behaviors (MSA requirement, telemetry, defaults)
- Supports: MSA requirement, template support notes, telemetry description

### OpenFold3 NIM release notes (1.1.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/1.1.0/release-notes.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Release notes for NIM 1.1.0 documenting the introduction of template support.
- Scope: NIM 1.1.0 feature set
- Supports: Template/CIF support introduction

### OpenFold3 NIM release notes (1.3.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Release notes for NIM 1.3.0 documenting telemetry defaults, MSA formats, diffusion_samples default and other behavior.
- Scope: NIM 1.3.0 feature/behavior details
- Supports: Telemetry description, MSA formats/types, diffusion_samples documentation

### OpenFold3 NIM performance (1.3.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/performance.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: NIM performance test page reporting runtime speedups and template overhead details.
- Scope: NIM runtime performance benchmarks
- Supports: Reported runtime speedups (1.15×–1.69×) and template processing overheads

### OpenFold3 NIM performance (1.1.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/1.1.0/performance.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Earlier NIM performance page with consistent statements about runtime speedups and template overheads.
- Scope: NIM runtime performance context
- Supports: Performance scaling and template overhead notes

### OpenFold3 modelcard (NVIDIA build site)

- URL: https://build.nvidia.com/openfold/openfold3/modelcard
- Publisher: build.nvidia.com
- Type: `model-card`
- Primary because: NVIDIA-hosted modelcard reporting model architecture and parameter count.
- Scope: Modelcard identity and parameter scale
- Supports: Architecture listing and parameter count (3.68×10⁸ parameters)

### OpenFold3 packaging/deploy guidance (NVIDIA build)

- URL: https://build.nvidia.com/openfold/openfold3
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: NVIDIA build site pages describing container governance and deployment instructions.
- Scope: Deployment, license governance, container usage
- Supports: NIM container governance, licensing notes

### NGC catalog entry for OpenFold3 NIM container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3
- Publisher: catalog.ngc.nvidia.com
- Type: `official-documentation`
- Primary because: Official NGC catalog entry describing the packaged container and its claimed capabilities.
- Scope: NGC container identity and runtime claims
- Supports: Container description, runtime/backend optimization claims

### Upstream OpenFold3 GitHub repository

- URL: https://github.com/aqlaboratory/openfold-3
- Publisher: github.com
- Type: `repository`
- Primary because: Canonical upstream OpenFold3 repository and license declaration for upstream code.
- Scope: Upstream codebase and upstream license (Apache-2.0)
- Supports: Upstream repository license (Apache-2.0) and upstream project identity

### Upstream OpenFold3 inference documentation (readthedocs) - inference

- URL: https://openfold-3.readthedocs.io/en/stable/inference.html
- Publisher: openfold-3.readthedocs.io
- Type: `official-documentation`
- Primary because: Upstream inference docs showing upstream defaults and inference flags (checkpoint name, upstream diffusion default).
- Scope: Upstream inference defaults and command-line flags
- Supports: Upstream default checkpoint name (openfold3_p2_v1) and upstream default --num-diffusion-samples = 5

### Upstream OpenFold3 configuration reference (readthedocs)

- URL: https://openfold-3.readthedocs.io/en/latest/configuration_reference.html
- Publisher: openfold-3.readthedocs.io
- Type: `official-documentation`
- Primary because: Upstream configuration reference documenting default checkpoint name and other config defaults.
- Scope: Upstream configuration defaults (checkpoint name)
- Supports: Default checkpoint name: openfold3_p2_v1

### NIM OpenFold3 API reference (OpenAPI spec page)

- URL: https://docs.api.nvidia.com/nim/reference/openfold-openfold3
- Publisher: docs.api.nvidia.com
- Type: `official-documentation`
- Primary because: API reference for the NIM OpenFold3 service (reference-level documentation).
- Scope: API reference and request/response schema
- Supports: API reference presence and structured API documentation

### NIM MSA-search API reference

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: MSA search documentation referenced by NIM docs for MSA database/format behavior.
- Scope: MSA formats, database usage and limits referenced by NIM docs
- Supports: MSA database count and depth limits as described in NIM materials

### NVIDIA Open Model License (enterprise agreements page)

- URL: https://nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license
- Publisher: nvidia.com
- Type: `official-documentation`
- Primary because: Official NVIDIA license page describing the NVIDIA Open Model License terms that apply to packaged models.
- Scope: Packaged/serving license terms
- Supports: NVIDIA Open Model License obligations and distribution text

### OpenFold3 NIM getting started

- URL: https://docs.nvidia.com/nim/bionemo/openfold3/latest/getting-started.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Getting-started page documenting prerequisites, health check, and basic deployment notes.
- Scope: Deployment prerequisites and service health checks
- Supports: Prerequisite software, health check response example

### OpenFold3 NIM deploy guidance (build site)

- URL: https://build.nvidia.com/openfold/openfold3/deploy
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: Deployment examples and container run guidance for the NIM container.
- Scope: Container deployment commands and runtime defaults
- Supports: Container run command examples and GPU usage guidance

## Evidence gaps

- Evidence gap: I did not find a primary-source statement in the NVIDIA NIM documentation or NGC/catalog pages that publishes an immutable, verifiable upstream checkpoint identifier (hash or immutable path) proving the exact weights served by the OpenFold3 NIM. I inspected: https://docs.nvidia.com/nim/bionemo/openfold3/latest/ (overview and release-notes sections), https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3, and https://build.nvidia.com/openfold/openfold3/modelcard without finding an immutable checkpoint identifier.
- Evidence gap: No primary-source numeric calibration (confidence → expected RMSD/TM-score) was published for the exact NIM-served checkpoint in the checked NVIDIA docs and modelcard. I inspected: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html and https://build.nvidia.com/openfold/openfold3/modelcard and found descriptive statements about confidence scores but no numeric calibration mapping.
- Evidence gap: Discrepancy between NIM documentation and upstream OpenFold3 inference docs for default diffusion_samples: NIM example-requests and NIM release-notes document diffusion_samples default = 1 (allowed range 1–5), while upstream OpenFold3 inference docs document an upstream default --num-diffusion-samples = 5. I inspected: https://docs.nvidia.com/nim/bionemo/openfold3/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold3/1.3.0/release-notes.html, and https://openfold-3.readthedocs.io/en/stable/inference.html and found conflicting defaults; the exact intended default for the NIM-served checkpoint requires explicit confirmation from NVIDIA.
- Evidence gap: No primary-source accuracy benchmarks (e.g., RMSD, TM-score) tied explicitly to the exact NIM-served checkpoint were found. I inspected NVIDIA NIM docs and modelcard (https://docs.nvidia.com/nim/bionemo/openfold3/latest/, https://build.nvidia.com/openfold/openfold3/modelcard) and upstream repository/papers (https://github.com/aqlaboratory/openfold-3, https://openfold-3.readthedocs.io/en/stable/inference.html) and found no protocol-matched accuracy tables listing metrics for the NIM-served checkpoint.
- Evidence gap: I did not find a primary-source statement in the NIM docs describing whether the NIM pulls a named upstream checkpoint file or uses a container-internal weight bundle or downloadable engine by immutable identifier. I inspected: https://docs.nvidia.com/nim/bionemo/openfold3/latest/, https://build.nvidia.com/openfold/openfold3/deploy, and https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3 for an exact checkout/asset locator and found none.
- Evidence gap: No primary-source, protocol-matched side-by-side comparison (accuracy) between the exact NIM-served checkpoint and alternatives (e.g., AlphaFold3) was located in the checked sources. I inspected: https://docs.nvidia.com/nim/bionemo/openfold3/latest/overview.html, https://build.nvidia.com/openfold/openfold3/modelcard, and upstream docs but found no such comparison tables.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://docs.nvidia.com/nim/bionemo/openfold3/latest/ Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://developer.nvidia.com/blog/how-to-predict-biomolecular-structures-using-the-openfold3-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
