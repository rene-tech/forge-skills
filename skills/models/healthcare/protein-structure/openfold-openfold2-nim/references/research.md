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

- Research key: `build-nvidia-com-openfold-openfold2-b5f4d4f07f`
- Independent audit: `revised`
- Researched: `2026-07-23T22:22:57.494770+00:00`

Canonical NVIDIA and upstream OpenFold sources in the provided findings show that the OpenFold2 NIM (Forge product family build-nvidia-com-openfold-openfold2-b5f4d4f07f) implements the monomer AlphaFold2-style protein structure prediction pipeline. The NIM is distributed as an NGC container and exposes predict, health, metadata, manifest, license and metrics endpoints; template-processing and confidence outputs (per-residue pLDDT and predicted aligned error matrix) are documented in versioned NIM docs. Primary evidence in the findings documents template input formats (mmCIF/mmcif.gz), MSA format (a3m), multiple versioned performance benchmark rows (per-sequence pipeline times reported on NVIDIA performance pages), and API request endpoints/example-requests that list response fields introduced in v2.5.0 (plddt, predicted_aligned_error, max_predicted_aligned_error, aligned_confidence_probs). The primary evidence set does not provide immutable mappings from NIM-served weights to upstream checkpoint commit hashes or artifact digests, does not report a definitive parameter count for the checkpoint files bundled with the NIM, and does not present per-checkpoint accuracy tables mapping specific checkpoint filenames to published accuracy metrics; these are recorded as evidence gaps below.

## Identity

- Upstream name: OpenFold2
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: PyTorch re-implementation of DeepMind's AlphaFold2 (monomer use-case)
- License: Apache-2.0; MIT; NVIDIA product/container terms (as listed in NGC catalog and Forge modelcard)
- Evidence: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2, https://github.com/aqlaboratory/openfold, https://arxiv.org/html/2503.00089v2

## Selection

### Recommended

- **Monomer protein 3D structure prediction from an amino-acid sequence for research purposes (academic and pharmaceutical research, computer-aided drug design).** — The NVIDIA Forge modelcard and NVIDIA NIM overview document the NIM's purpose as predicting 3D protein structure from a query amino-acid sequence with optional MSAs and templates; the NIM exposes a predict endpoint in the API reference.
  Scope: OpenFold2 NIM (NVIDIA-served monomer structure prediction service, versioned docs: v2.5.0 and latest)
  Evidence: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/api-reference.html

### Conditional

- **Structure prediction using externally-supplied templates (mmCIF) when template processing is enabled.** — Set use_templates=true and provide explicit_templates containing mmCIF (or mmcif.gz) text strings; ensure templates meet the documented minimum sequence-identity threshold for the targeted NIM version (see versioned template-processing docs).
  Scope: OpenFold2 NIM template-processing (NVIDIA-served; behavior versioned across v1.2.0, v2.0.0, v2.5.0)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/2.0.0/template-processing.html
- **Using user-supplied mmCIF templates when running NIM versions that document direct template processing support.** — Confirm the NIM runtime/version supports explicit_templates (documented as added/available in 1.2.0 and refined in later versions) before relying on this capability.
  Scope: OpenFold2 NIM (version-scoped template processing support; consult v1.2.0 and later docs)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/performance.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/release-notes.html

### Avoid

- **Multimer / complex (multi-chain) structure prediction** — The provided NVIDIA primary sources document the NIM as implementing the monomer use-case and do not document multimer/multi-chain prediction support for the NIM in the supplied findings.
  Scope: OpenFold2 NIM (monomer)
  Evidence: https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html, https://build.nvidia.com/openfold/openfold2/modelcard
- **Unsupervised clinical decision support or diagnostic use without expert review** — Primary NVIDIA documents and the Forge modelcard describe research use (academic and pharmaceutical research) and do not claim regulatory approval or suitability for clinical/diagnostic decision-making in the provided findings.
  Scope: OpenFold2 NIM (NVIDIA-served monomer service)
  Evidence: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html

## Input preparation

### Semantic inputs

- Required input: a plain amino-acid sequence string representing a single protein chain (monomer). Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html
- Optional inputs: externally-supplied multiple-sequence alignments (MSAs, a3m format) and structural templates (mmCIF or mmcif.gz) may be accepted when provided and when template processing is enabled. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/template-processing.html

### Accepted formats

- Sequence: plain amino-acid sequence string. Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/example-requests.html
- MSA: a3m formatted MSA strings are accepted for MSA inputs. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/template-processing.html
- Templates: mmCIF text strings (mmcif or compressed mmcif.gz) are accepted for explicit_templates in versions >= 2.0.0; older versions include HHR-based template processing modes (versions ≤ 1.2.0). Sources: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/2.0.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/template-processing.html
- The NIM’s predict request payload fields include sequence and (optionally) selected_models and explicit_templates per example-requests and API reference. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/api-reference.html

### Preprocessing

- Evidence gap: The provided findings do not include canonical NVIDIA or upstream documentation describing input chunking behavior, chunk-size tuning, or how chunking is configured/disabled in the NIM runtime; searched NIM docs and upstream repo but no authoritative chunking configuration doc was found. Sources: https://github.com/aqlaboratory/openfold, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/api-reference.html
- Evidence gap: The provided findings do not include an immutable mapping (git commit hash, model artifact digest, or container image digest) that maps NIM-served model parameter files to upstream checkpoint revisions; the NGC container listing references model weights but no digest-to-upstream-commit mapping was provided in the supplied findings. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2, https://github.com/aqlaboratory/openfold

### Pre-submit validation

- The Forge deploy documentation and Forge modelcard state an input sequence length limit of up to 1000 residues in example usage and deploy guidance. Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://build.nvidia.com/openfold/openfold2/deploy
- Ambiguity/conflict: NVIDIA performance pages document supported sequence lengths on a single GPU ranging from 4 to 2048 residues (with specific GPU recommendations for sequences longer than ≈1800 residues), which differs from the sequence ≤1000 statement found in deploy/modelcard; both locators are primary in the findings and should be reconciled by confirming the target NIM version/runtime. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/performance.html, https://build.nvidia.com/openfold/openfold2/modelcard
- Evidence gap: The provided findings do not include a single canonical authoritative statement resolving the conflicting sequence-length bounds across the deploy/modelcard and performance pages; verify against the deployed NIM versioned docs before enforcing any single numeric bound. Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/performance.html

### Task-specific formatting

- The NIM exposes a POST predict endpoint at biology/openfold/openfold2/predict-structure-from-msa-and-template (documented in example-requests and API reference); requests may include fields such as sequence, selected_models, use_templates, and explicit_templates. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/api-reference.html, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html
- To enable direct template processing, set use_templates=true and provide explicit_templates containing mmCIF (or mmcif.gz) text strings as described in the template-processing docs. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/template-processing.html

## Output interpretation

### Outputs

- Predicted 3D protein structure(s) in PDB format are produced as the primary structural output. Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/openfold/-
- Confidence outputs documented include per-residue pLDDT (range 0–100) and a predicted aligned error (PAE) matrix (NxN), plus related fields introduced in v2.5.0 such as max_predicted_aligned_error and aligned_confidence_probs. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/release-notes.html
- Optional embeddings and per-residue/ pairwise tensors (shapes reported as num_res × emb_dims or num_res × num_res × emb_dims in the provided findings) may be emitted by the NIM/upstream tooling as documented in the NGC/clara model listing. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/openfold/-, https://build.nvidia.com/openfold/openfold2/modelcard

### Interpretation

- Interpret per-residue pLDDT and PAE as model-derived confidence metrics; the provided findings do not tie these confidence outputs to per-checkpoint accuracy tables for specific checkpoint filenames served by the NIM. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/release-notes.html, https://build.nvidia.com/openfold/openfold2/modelcard

### Post-inference validation

- Response fields introduced in v2.5.0 are documented in the example-requests page and include plddt (per-residue predicted LDDT scores, range 0–100) and predicted_aligned_error (NxN matrix); use those API docs to validate field names in runtime responses. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html
- Evidence gap: The provided findings do not include an explicit per-checkpoint mapping of output calibration (per-checkpoint accuracy tables tying specific checkpoint filenames to benchmarked quality metrics) for NIM-served checkpoint filenames; no per-checkpoint accuracy table was found in the supplied primary sources. Sources: https://github.com/aqlaboratory/openfold, https://arxiv.org/html/2503.00089v2, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2

## Public benchmarks

### Inference latency (pipeline time) for single-sequence monomer predictions

- Dataset/split: Four test proteins (sequence lengths: 98, 304, 562, 914 residues) used in NVIDIA performance pages / not reported
- Metric/value: pipeline_time (seconds) including parameter loading, feature computation, and forward pass / Version 2.0.0 benchmark times (H100 80 GB) without templates: 4.60 s, 20.03 s, 42.66 s, 97.04 s for sequences 98, 304, 562, 914 respectively; Version 1.0.0 reported 5.31 s, 10.2 s, 19.6 s, 41.2 s for the same-length set under its reported settings. (`lower-is-better`)
- Model scope: OpenFold2 NIM (version-scoped benchmarks as published on NVIDIA NIM performance pages: v2.0.0 and v1.0.0)
- Conditions: Benchmarks reported on NVIDIA performance pages; v2.0.0 times reported on H100 80 GB HBM3 with and without templates; v1.0.0 reported settings include use_templates=false, selected_models [1..5], relax_prediction=false, DeepSpeed Evoformer kernel active, precision bf16 for Evoformer and fp32 elsewhere.
- Source: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/performance.html
- Locator: performance page: 'Benchmark times on H100 80 GB for the four test proteins' section (v2.0.0 data) and performance page v1.0.0 'Version 1.0.0 benchmark on H100 80 GB HBM3' section
- Caveat: Benchmarks are reported per-NVIDIA performance pages for specific NIM versions and hardware; mapping to a running NIM instance requires confirming the NIM version and hardware match the reported conditions.
- Caveat: Reported benchmark values are version-scoped (v1.0.0 vs v2.0.0) and should not be assumed to apply to other NIM versions unless the docs state so.

### Accuracy/quality metrics reported by NVIDIA performance pages

- Dataset/split: Four test proteins (as used in performance pages) / internal benchmark set / not reported
- Metric/value: Accuracy metrics (CADS, LDDT, STRIDE, MP) as reported on performance pages / For version 2.0.0 vs 1.0.0 on H100: CADS 0.740 vs 0.744, LDDT 0.860 vs 0.861, STRIDE 4.24 unchanged, MP 0.878 vs 0.882. (`higher-is-better`)
- Model scope: OpenFold2 NIM (version 2.0.0 vs 1.0.0 per NVIDIA performance page)
- Conditions: Reported on NVIDIA performance page describing H100 80 GB HBM3 comparisons between versions; protocol details for dataset/split not provided in the supplied findings.
- Source: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/performance.html
- Locator: performance page: 'Accuracy metrics on H100 for version 2.0.0 vs 1.0.0' section
- Caveat: The performance page presents internal accuracy comparisons between NIM versions but does not provide full protocol/dataset/split specifications in the supplied findings; do not assume comparability to external benchmarks without further provenance.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Head-to-head quality or latency comparison with external MSA-generation services or other NIMs under identical protocol/hardware
- Criteria: Identical hardware, identical NIM versions, identical end-to-end measurement protocol required but not present in the supplied primary findings.
- Rationale: NVIDIA performance and release docs provide version-scoped internal benchmarks but do not present head-to-head tables that match other NIMs or external MSA-generation services under identical, fully-documented protocols in the supplied findings.
- Comparison conditions: No identical-protocol primary evidence for end-to-end comparisons found in the supplied NIM docs; would require matching NIM version, hardware, and measurement protocol.
- Evidence: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/performance.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/release-notes.html

## Limitations and safety

### Limitations

- OpenFold2 NIM implements the monomer use-case; multimer/multi-chain prediction is not documented in the provided NVIDIA primary sources for the NIM. Sources: https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html, https://build.nvidia.com/openfold/openfold2/modelcard
- Evidence gap: The provided findings do not present immutable upstream checkpoint identifiers (git commit hash, model artifact digest, or container image digest) that map the NIM-served parameter files to upstream checkpoint revisions; NGC container listings reference model weights but no digest-to-upstream-commit mapping was found in the supplied primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2, https://github.com/aqlaboratory/openfold
- Evidence gap: The total parameter count for the OpenFold2 checkpoint files bundled with the NIM is not reported in the provided NVIDIA NIM documentation or the upstream OpenFold materials included in the supplied findings. Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://github.com/aqlaboratory/openfold, https://arxiv.org/html/2503.00089v2
- Evidence gap: The provided findings do not include per-checkpoint published accuracy tables that map specific checkpoint filenames distributed with the NIM (e.g., params_model_*.npz) to benchmarked quality metrics; no such mapping was found in the supplied primary sources. Sources: https://github.com/aqlaboratory/openfold, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2
- Ambiguity/conflict in sequence-length guidance across primary docs: deploy/modelcard example(s) state sequence ≤1000 residues while performance pages document supported sequence ranges on a single GPU of 4–2048 residues (version- and hardware-dependent); reconcile against the target NIM version/runtime before enforcing numeric bounds. Sources: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/performance.html

### Safety

- Use of the OpenFold2 NIM is governed by NVIDIA product/container terms as documented in the NGC container listing; users must follow the container and product licensing terms when deploying the NIM. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2
- Evidence gap: The provided findings do not include explicit PHI- or clinical-data-handling guidance specific to the OpenFold2 NIM; do not assume clinical suitability or PHI-safe deployment without institutional and legal review.

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's OpenFold2 skill documents sequence/MSA/template preparation, selected-model and relaxation controls, mmCIF/confidence validation, and hosted/local operation for the named NIM. Use Forge's declared route and deployed source image for execution.
- [openfold2-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/openfold2-nim)
- [cuEquivariance](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/cuEquivariance)

## Primary sources

### OpenFold2 modelcard (build.nvidia.com)

- URL: https://build.nvidia.com/openfold/openfold2/modelcard
- Publisher: NVIDIA (Forge modelcard)
- Type: `model-card`
- Primary because: Forge modelcard providing accepted input/output formats, overview, and usage guidance for the OpenFold2 NIM.
- Scope: OpenFold2 NIM (Forge modelcard)
- Supports: OpenFold2 predicts the 3D structure of a protein from a sequence, MSAs, and templates.
- Supports: OpenFold2 is available for commercial use and intended for academic and pharmaceutical research labs and computer-aided drug design.
- Supports: The OpenFold2 NIM’s input sequence field accepts strings of up to 1000 residues (as shown in deploy/model examples).

### OpenFold2 NIM overview (latest)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Official NIM documentation describing model purpose, inputs, monomer scope, and relation to OpenFold/AlphaFold2.
- Scope: OpenFold2 NIM overview (latest)
- Supports: OpenFold2 implements the monomer use-case and predicts protein structure from an input sequence with optional MSAs and templates.
- Supports: OpenFold2 is a PyTorch re-implementation of DeepMind's AlphaFold2.

### OpenFold2 NIM API reference (v2.5.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/api-reference.html
- Publisher: NVIDIA (NIM API docs)
- Type: `official-documentation`
- Primary because: Versioned API reference documenting predict and health/metadata endpoints for the OpenFold2 NIM.
- Scope: OpenFold2 NIM API (v2.5.0)
- Supports: Documented API endpoints (predict, health, manifest, license, metrics) and notes that NGC_API_KEY is required to pull the container but not for runtime inference requests.

### OpenFold2 template processing documentation (v2.5.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/template-processing.html
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Versioned documentation of template input format, required fields, and identity thresholds.
- Scope: OpenFold2 template-processing (v2.5.0)
- Supports: Direct template processing in OpenFold2 v2.5.0 uses mmCIF format strings supplied via explicit_templates.
- Supports: To enable template processing in OpenFold2 v2.5.0, set use_templates=true.
- Supports: v2.5.0 requires a minimum of 90% sequence identity between query and template for acceptance; the API selects chains with _atom_site.label_asym_id=A during featurization; Kalign is used for sequence alignment.

### OpenFold2 template processing documentation (v1.2.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/template-processing.html
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Historical template-processing documentation describing available template modes for v1.2.0.
- Scope: OpenFold2 template-processing (v1.2.0)
- Supports: v1.2.0 documents three template processing approaches: no template input, database-driven processing using HHR strings, and direct template processing; v1.2.0 adds user-supplied mmCIF template support per performance/release notes.

### OpenFold2 NIM example requests (latest)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Example request/response documentation listing the predict endpoint and the response fields introduced in v2.5.0.
- Scope: OpenFold2 NIM example-requests (latest)
- Supports: The predict endpoint biology/openfold/openfold2/predict-structure-from-msa-and-template is documented with response fields such as plddt, predicted_aligned_error, max_predicted_aligned_error, and aligned_confidence_probs.
- Supports: Confidence metrics include per-residue pLDDT (0–100) and a predicted aligned error matrix (NxN).

### OpenFold2 NIM example requests (v1.2.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/example-requests.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Versioned example-requests page documenting the predict endpoint and payload fields for older NIM versions.
- Scope: OpenFold2 NIM example-requests (v1.2.0)
- Supports: The predict endpoint biology/openfold/openfold2/predict-structure-from-msa-and-template is present in v1.2.0 example-requests.

### OpenFold2 NIM performance page (v2.5.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/performance.html
- Publisher: NVIDIA (NIM performance docs)
- Type: `official-documentation`
- Primary because: Versioned performance page documenting supported GPUs, sequence-length guidance, and version-scoped benchmark rows.
- Scope: OpenFold2 NIM performance (v2.5.0 / v2.0.0 data present on this page)
- Supports: Supported GPUs list and sequence-length guidance (supported on a single GPU from 4 to 2048 residues, with GPU recommendations for very long sequences).
- Supports: Performance benchmark times for test proteins (per-sequence pipeline times) and accuracy comparisons between versions (v2.0.0 vs v1.0.0) are reported.

### OpenFold2 NIM performance page (v1.2.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/performance.html
- Publisher: NVIDIA (NIM performance docs)
- Type: `official-documentation`
- Primary because: Versioned performance page with notes about feature additions and internal benchmarks for v1.2.0.
- Scope: OpenFold2 NIM performance (v1.2.0)
- Supports: v1.2.0 adds support for user-supplied mmCIF templates and reports internal benchmarks on H100 80 GB HBM3 with latency/accuracy comparable to earlier versions.

### OpenFold2 NIM performance page (v1.0.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/1.0.0/performance.html
- Publisher: NVIDIA (NIM performance docs)
- Type: `official-documentation`
- Primary because: Historical performance page documenting v1.0.0 benchmark times and inference settings.
- Scope: OpenFold2 NIM performance (v1.0.0)
- Supports: v1.0.0 benchmark pipeline times on H100 80 GB HBM3 for four test proteins and inference setting details including precision and kernel usage.

### OpenFold2 NIM release notes (latest)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/latest/release-notes.html
- Publisher: NVIDIA (NIM release notes)
- Type: `official-documentation`
- Primary because: Versioned release notes documenting added features and changes across NIM versions.
- Scope: OpenFold2 NIM release notes (latest / v1.2.0 referenced)
- Supports: Release notes document added features (e.g., confidence outputs introduced in earlier releases and GPU support added in 2.5.0) and other runtime changes.

### OpenFold2 NGC container listing (teams/openfold)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2
- Publisher: NVIDIA NGC (container catalog)
- Type: `official-documentation`
- Primary because: NGC container listing describing NIM contents, model weights, and distribution metadata.
- Scope: OpenFold2 NIM container and packaging
- Supports: The NGC container listing references model weights and container distribution metadata; it documents container packaging and license notes in the supplied findings.

### NGC container details for OpenFold2 (alternate NGC catalog path)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/openfold/containers/openfold2/-
- Publisher: NVIDIA NGC (container catalog)
- Type: `official-documentation`
- Primary because: NGC container metadata entry (alternate path) present in the supplied findings.
- Scope: OpenFold2 NGC container metadata
- Supports: Container tag/versioning and update timestamp metadata as provided in the NGC catalog entry in the supplied findings.

### OpenFold (upstream) GitHub repository (aqlaboratory/openfold)

- URL: https://github.com/aqlaboratory/openfold
- Publisher: AlQuraishi Laboratory / OpenFold project (GitHub)
- Type: `repository`
- Primary because: Upstream open-source implementation repository used for upstream-checkpoint and code-level evidence.
- Scope: Upstream OpenFold codebase
- Supports: The repository contains code, examples, and release notes relevant to OpenFold and its development history.

### OpenFold2 preprint (arXiv)

- URL: https://arxiv.org/html/2503.00089v2
- Publisher: arXiv / OpenFold authors
- Type: `paper`
- Primary because: Upstream preprint describing OpenFold2 experimental methods and datasets.
- Scope: Upstream OpenFold2 experimental results and methods
- Supports: Preprint describes training datasets drawn from PDB and mentions held-out test sets such as CAMEO and CASP (as reported in the supplied findings).

### NVIDIA BioNeMo framework OpenFold model docs

- URL: https://docs.nvidia.com/bionemo-framework/1.10/models/openfold.html
- Publisher: NVIDIA (BioNeMo framework docs)
- Type: `official-documentation`
- Primary because: NVIDIA BioNeMo docs referencing OpenFold model inputs/outputs and confidence metrics.
- Scope: NVIDIA BioNeMo OpenFold model docs
- Supports: OpenFold outputs include PDB and confidence metrics (per-residue pLDDT and PAE matrix) as described in the supplied findings.

### OpenFold (Clara) NGC model listing (alternate OpenFold model page)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/openfold/-
- Publisher: NVIDIA NGC (Clara catalog)
- Type: `official-documentation`
- Primary because: NGC Clara model listing included in the supplied findings that documents output formats and optional embeddings.
- Scope: OpenFold NGC Clara model listing
- Supports: Response outputs include protein structures in PDB format and optionally confidence metrics (pLDDT and PAE) and embeddings (num_res × emb_dims or num_res × num_res × emb_dims).

### NVIDIA NIM API reference (alternate reference path)

- URL: https://docs.api.nvidia.com/nim/reference/openfold-openfold2
- Publisher: NVIDIA (NIM API docs)
- Type: `official-documentation`
- Primary because: API reference path included in the supplied findings documenting NIM governance and usage.
- Scope: OpenFold2 NIM API reference (alternate path)
- Supports: Notes on licensing and intended user communities for the OpenFold2 NIM as provided in the supplied findings.

### OpenFold2 template processing docs (v2.0.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/2.0.0/template-processing.html
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Versioned template-processing page included in the supplied findings documenting the removal of HHR-based templates starting v2.0.0.
- Scope: OpenFold2 template-processing (v2.0.0)
- Supports: v2.0.0 removes HHR-based template processing and accepts only mmCIF format strings for templates.

### OpenFold2 performance page (v2.4.0)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/2.4.0/performance.html
- Publisher: NVIDIA (NIM performance docs)
- Type: `official-documentation`
- Primary because: Versioned performance page included in the supplied findings documenting GPU support and scaling behavior.
- Scope: OpenFold2 NIM performance (v2.4.0)
- Supports: Supported GPUs and notes that performance scales with sequence length and MSA size as documented in the supplied findings.

### OpenFold2 support matrix (latest)

- URL: https://docs.nvidia.com/nim/bionemo/openfold2/latest/support-matrix.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Support matrix included in the supplied findings providing recommended disk space and other runtime guidance.
- Scope: OpenFold2 NIM support matrix (latest)
- Supports: At least 80 GB of disk space is recommended for storage of the OpenFold2 NIM (as per the supplied findings).

### NGC catalog user guide (NGC SBOM and digest guidance)

- URL: https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html
- Publisher: NVIDIA (NGC docs)
- Type: `official-documentation`
- Primary because: NGC user guide documents SBOM/digest formats and how to retrieve SBOMs using image digests, included in the supplied findings.
- Scope: NGC catalog and SBOM guidance
- Supports: SBOM artifact tag format and the requirement to use image digests to retrieve SBOMs; informs evidence-gap rationale for immutable mapping searches.

### Cited official first-party source

- URL: https://build.nvidia.com/openfold/openfold2/deploy
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: openfold-openfold2
- Supports: Exact independently audited claim citation

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/openfold/openfold2
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: openfold-openfold2
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Immutable upstream checkpoint revision identifiers (git commit hash, model artifact digest, or container image digest) mapping NIM-served parameter files to upstream OpenFold checkpoint revisions are not present in the supplied primary findings; searched NGC container listing and upstream GitHub but no digest-to-upstream-commit mapping was found (checked URLs: https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2, https://catalog.ngc.nvidia.com/orgs/nim/openfold/containers/openfold2/-, https://github.com/aqlaboratory/openfold).
- Evidence gap: The total parameter count (number of model parameters) for the OpenFold2 checkpoint files bundled with the NIM is not reported in the supplied primary findings; checked upstream repo and NIM docs without finding a parameter-count table (checked URLs: https://github.com/aqlaboratory/openfold, https://build.nvidia.com/openfold/openfold2/modelcard).
- Evidence gap: Per-checkpoint published accuracy tables mapping specific NIM-served checkpoint filenames (e.g., params_model_*.npz) to benchmarked quality metrics (CASP/CAMEO or other held-out sets) are not present in the supplied primary findings; checked upstream paper and repository and NGC/Forge docs (checked URLs: https://arxiv.org/html/2503.00089v2, https://github.com/aqlaboratory/openfold, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2).
- Evidence gap: Canonical API example responses enumerating exact response-field array shapes for all output tensors (explicit array-dimension declarations for plddt, predicted_aligned_error, embeddings, and PDB pose arrays) are not present in a single authoritative locator in the supplied findings; example-requests list fields and ranges but do not provide fully explicit typed array-shape schemas in the supplied findings (checked URLs: https://docs.nvidia.com/nim/bionemo/openfold2/latest/example-requests.html, https://docs.nvidia.com/nim/bionemo/openfold2/1.2.0/example-requests.html).
- Evidence gap: Canonical documentation for input chunking behavior, chunk-size tuning, or disabling chunking in the NIM runtime was not found in the supplied primary findings (checked URLs: https://github.com/aqlaboratory/openfold, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/api-reference.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2).
- Evidence gap: Explicit PHI- or clinical-data-handling guidance specific to the OpenFold2 NIM is not present in the supplied primary NVIDIA docs; no PHI-specific operational guidance was found in the supplied findings (checked URLs: https://build.nvidia.com/openfold/openfold2/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2, https://docs.nvidia.com/nim/bionemo/openfold2/latest/release-notes.html).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/openfold/openfold2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/openfold/openfold2/deploy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/openfold/openfold2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
