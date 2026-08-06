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

- Research key: `build-nvidia-com-nvidia-genmol-generate-c1a2135e2c`
- Independent audit: `revised`
- Researched: `2026-07-23T21:51:05.838515+00:00`

NV-GenMol-89M-v2 is documented in NVIDIA primary artifacts as GenMol v2.0: an ~89M-parameter masked-diffusion Transformer (BERT-style) trained on SAFE representations. NVIDIA model card, NIM API reference, NIM release notes, NGC catalog, Hugging Face model card, and the GenMol NIM benchmarks page together report that GenMol NIM v2.0.0 integrates NV-GenMol-89M-v2 and publish NIM-run benchmark tables for motif-extension and scaffold-decoration (SAFE-DRUGS, 10 tests) with hyperparameters and per-GPU wall-times. The arXiv preprint is the upstream paper reporting GenMol experimental results (paper-level experiments). The provided primary sources do not publish an immutable-checkpoint download URL or canonical checksum tying a published immutable hash to NV-GenMol-89M-v2 (evidence gap). The arXiv paper reports upstream experimental metrics but the provided primary NVIDIA serving artifacts do not present an explicit, immutable-checkpoint-mapped numeric table tying the paper's one-step linker numbers to the NV-GenMol-89M-v2 immutable checkpoint (evidence gap).

## Identity

- Upstream name: NV-GenMol-89M-v2
- Checkpoint/version: NV-GenMol-89M-v2
- Immutable revision: Evidence gap: Immutable checkpoint revision/hash not reported in the available primary sources
- Parameter scale: 89 million parameters
- Architecture/head: Masked diffusion model; Transformer / BERT network trained on Sequential Attachment-based Fragment Embedding (SAFE) representations
- License: Model weights: NVIDIA Open Model License; Source code: Apache-2.0 (as reported by primary model-card, API reference, and HF model card)
- Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://docs.api.nvidia.com/nim/reference/nvidia-genmol, https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://arxiv.org/html/2501.06158v1, https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html

## Selection

### Recommended

- **Fragment‑conditioned molecule generation: motif extension and scaffold decoration** — NVIDIA GenMol NIM benchmarks page and the GenMol model card identify motif-extension and scaffold-decoration as supported fragment-completion tasks and provide v2 numeric metrics and hyperparameters for these tasks.
  Scope: NV-GenMol-89M-v2 (NIM/serving benchmark reported on GenMol NIM v2.0.0)
  Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard
- **De novo molecule generation (empty template)** — NIM endpoints documentation and getting-started examples state that passing a null/empty 'smiles' template to the /generate endpoint triggers de novo generation and that outputs are SAFE/SMILES strings.
  Scope: NV-GenMol-89M-v2 served via GenMol NIM endpoints
  Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html
- **Component in hit-generation and lead-optimization pipelines with downstream scoring and filtering** — NVIDIA model card and NIM benchmarks present an integrated workflow expectation (generate then compute properties and apply filters); using GenMol as a generative component combined with downstream property scoring is supported by the provided primary artifacts.
  Scope: NV-GenMol-89M-v2 (upstream model card and NIM-run benchmarks)
  Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html

### Conditional

- **One-step linker generation** — ArXiv paper reports one-step linker experimental results as upstream experiments; NIM release notes state v2 improves linker success but the provided primary sources do not publish an explicit immutable-checkpoint-to-paper mapping tying the paper's numeric values to NV-GenMol-89M-v2. Use only after empirical validation and downstream filtering.
  Scope: ArXiv-reported GenMol experiments (paper-level) and GenMol NIM v2.0.0 serving claims; direct immutable-checkpoint mapping not established in provided primary sources
  Evidence: https://arxiv.org/html/2501.06158v1, https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html
- **Using FP32 property scores as calibrated probabilities in decision-critical clinical pipelines** — Primary NIM benchmarks and model card report FP32 property scores but do not publish a calibration protocol or thresholds; treat FP32 scores as heuristic indicators and validate downstream.
  Scope: NV-GenMol-89M-v2 (NIM benchmarks and model-card evidence)
  Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard

### Avoid

- **One‑step linker design without downstream validation** — Primary sources do not provide a verified immutable-checkpoint-mapped numeric table tying the arXiv paper's one-step linker numbers to NV-GenMol-89M-v2; the paper reports upstream experimental metrics and NIM release notes claim v2 improves linker success but no immutable-checkpoint mapping is published in the provided findings (provenance/evidence gap).
  Scope: Not verifiable for NV-GenMol-89M-v2 (paper-level experimental results are not mapped to an immutable checkpoint in the provided sources)
  Evidence: https://arxiv.org/html/2501.06158v1, https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html
- **Assuming FP32 output property scores are calibrated posterior probabilities for clinical decision-making** — NIM benchmarks and model card present FP32 property scores but do not publish a calibration protocol or threshold semantics in the available primary sources (evidence gap).
  Scope: NV-GenMol-89M-v2 (NIM benchmarks and model-card evidence)
  Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard

## Input preparation

### Semantic inputs

- SAFE molecular sequence templates or SMILES strings representing fragment templates, masked fragment spans, or empty templates to trigger de novo generation. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Numerical control parameters accepted by the endpoint include num_molecules (integer), temperature (float), noise (float), and step_size (sampling/diffusion steps) as documented by the NIM endpoints (note: step_size deprecated in v2.0.0 and ignored). Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Enumeration/selection strings for scoring methods (e.g., QED or LogP) and flags controlling result filtering are accepted per endpoint documentation. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard

### Accepted formats

- The 'smiles' input parameter accepts SAFE or SMILES text with optional masks; passing null triggers de novo generation via the /generate endpoint. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Maximum input length documented as 512 tokens for the upstream Hugging Face model card. Sources: https://huggingface.co/nvidia/NV-GenMol-89M-v2
- num_molecules is an integer parameter with accepted range 1–1000 and default 30 as documented in NIM endpoints; NIM may return fewer molecules due to invalidity filtering. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html

### Preprocessing

- Inputs use SAFE token/format and masked fragment placeholder syntax as shown in the getting-started examples and endpoints documentation. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html

### Pre-submit validation

- Inputs exceeding the documented maximum input length (512 tokens as reported on the HF model card) are outside documented supported sizes. Sources: https://huggingface.co/nvidia/NV-GenMol-89M-v2
- num_molecules accepted range is 1–1000 with default 30; the NIM may return fewer molecules than requested due to invalidity filtering. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Temperature parameter documented range is 0.01–10.0 with default 1.0; noise range documented as 0.0–2.0 with default 1.0 (endpoint documentation). Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html

### Task-specific formatting

- De novo generation: pass a null or empty 'smiles' template to the /generate endpoint to request de novo molecules. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Masked fragment placeholders use the SAFE mask syntax as shown in the getting-started examples. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html

## Output interpretation

### Outputs

- Generated outputs are arrays of SAFE/SMILES strings representing generated molecules (text) as reported by the model card and NIM endpoints. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Accompanying numeric outputs reported by NIM are FP32 property score arrays (property scorers used in benchmarks); the NIM benchmarks present these numeric metrics but do not fully specify calibration semantics in the provided findings. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html

### Interpretation

- The GenMol NIM benchmarks page reports the metrics labeled Validity, Uniqueness, Diversity, Novelty, and Quality for motif-extension and scaffold-decoration tasks, but exact computation details for 'quality' and calibration semantics for FP32 scores are not fully specified in the provided primary sources (evidence gap). Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Evidence gap: The provided primary sources do not document whether FP32 property scores are calibrated probabilities or the thresholds used to compute the 'quality' metric; do not assume calibrated-probability semantics from the available artifacts. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard

### Post-inference validation

- Post-inference validation recommended by the benchmarks page: filter invalid SMILES and deduplicate outputs; compute fingerprint-based diversity/novelty and property scores to apply quality filters as presented in NIM benchmarks (exact thresholds not provided in findings). Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- The NIM endpoint may return fewer molecules than requested due to post-generation invalidity filtering as documented in the endpoints page. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html

## Public benchmarks

### Motif-extension

- Dataset/split: SAFE-DRUGS / not reported
- Metric/value: Validity, Uniqueness, Diversity, Novelty, Quality / validity 0.889; uniqueness 0.670; diversity 0.674; novelty 0.691; quality 0.188 (v2 on H100, NIM benchmark) (`higher-is-better`)
- Model scope: NV-GenMol-89M-v2 (NIM/serving benchmark reported for GenMol NIM v2.0.0 on H100)
- Conditions: NIM benchmarks: mask_length=17, temperature=1.2, noise=1.6; 10 tests per task drawn from SAFE-DRUGS; H100 GPU; v2 vs v1 comparison on benchmarks page.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: GenMol NIM benchmarks page — Motif-extension v2 numeric table/row (motif-extension v2)
- Caveat: Provenance: these are NIM-run benchmark results reported on the GenMol NIM benchmarks page rather than an upstream-only immutable-checkpoint table.
- Caveat: Dataset split names for SAFE-DRUGS are not reported in the provided primary sources (evidence gap).
- Caveat: Downstream scorer thresholds and exact computation details for 'quality' are not specified in the provided primary sources (evidence gap).

### Scaffold-decoration

- Dataset/split: SAFE-DRUGS / not reported
- Metric/value: Validity, Uniqueness, Diversity, Novelty, Quality / validity 0.995; uniqueness 0.756; diversity 0.564; novelty 0.624; quality 0.354 (v2 on H100, NIM benchmark) (`higher-is-better`)
- Model scope: NV-GenMol-89M-v2 (NIM/serving benchmark reported for GenMol NIM v2.0.0 on H100)
- Conditions: NIM benchmarks: mask_length=17, temperature=1.2, noise=2.0; 10 tests per task drawn from SAFE-DRUGS; H100 GPU; v2 vs v1 comparison on benchmarks page.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: GenMol NIM benchmarks page — Scaffold-decoration v2 numeric table/row (scaffold-decoration v2)
- Caveat: Provenance: these are NIM-run benchmark results reported on the GenMol NIM benchmarks page.
- Caveat: Dataset split names for SAFE-DRUGS are not reported in the provided primary sources (evidence gap).
- Caveat: Downstream scorer thresholds and exact computation details for 'quality' are not specified in the provided primary sources (evidence gap).

### Runtime (generation throughput)

- Dataset/split: not applicable / not applicable
- Metric/value: Average wall-time (seconds) to generate 1000 molecules across 10 tests / H100 motif-extension 1.051 s; H100 scaffold-decoration 0.961 s (NIM v2 reported averages) (`lower-is-better`)
- Model scope: NV-GenMol-89M-v2 (NIM/serving runtime benchmark reported on GenMol NIM benchmarks page)
- Conditions: Reported on GenMol NIM benchmarks page as average wall-time on H100 for generating 1000 molecules across 10 tests; hyperparameters match those listed for each task on the benchmarks page.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: GenMol NIM benchmarks page — runtime table (H100 row)
- Caveat: Provenance: runtime values are NIM/serving measurements reported on the benchmarks page.
- Caveat: Per-GPU runtime values are published for multiple SKUs on the benchmarks page, but per-GPU values beyond those enumerated at the benchmarks locator are not present in other provided findings (see evidence gaps).

## Comparisons

### nvidia-genmol-2-0-0-nim — `insufficient-evidence`

- Task: When served via the NIM container for motif-extension, scaffold-decoration, and runtime
- Criteria: NIM release notes, NGC catalog, model card, and NIM benchmarks indicate NIM v2.0.0 integrates NV-GenMol-89M-v2 and report NIM-run numeric metrics; however protocol-matched upstream immutable-checkpoint tables separating upstream-paper experimental runs from NIM-run re-runs are not present in the provided findings, preventing a task-matched direct comparison.
- Rationale: Release notes and NGC catalog indicate NIM v2.0.0 packages NV-GenMol-89M-v2; NIM benchmarks provide numeric values for v2, but the available primary sources do not supply a direct upstream-checkpoint-to-serving matched-protocol numeric table for head-to-head comparability.
- Comparison conditions: NIM v2.0.0 serving conditions as reported on NIM benchmarks and release notes; upstream paper experiments are reported separately in arXiv without explicit immutable-checkpoint mapping in the provided findings.
- Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html

### insufficient-evidence — `insufficient-evidence`

- Task: Protocol-matched comparison to other external generative small-molecule models
- Criteria: No primary-source task-matched benchmark tables for external alternatives are present in the provided findings; therefore a protocol-matched comparison is not supported from the available primary evidence.
- Rationale: The provided findings do not include primary pages or checkpoint identifiers for other candidate models suitable for direct protocol-matched comparison.
- Comparison conditions: N/A — insufficient primary evidence for alternatives in the provided sources.
- Evidence:

## Limitations and safety

### Limitations

- Evidence gap: Immutable checkpoint revision/hash for NV-GenMol-89M-v2 is not reported in the available primary sources; no canonical checksum or immutable download URL was found in the provided findings. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://huggingface.co/nvidia/NV-GenMol-89M-v2
- NIM-run numeric metrics are reported on the benchmarks page; users must consult the exact NIM benchmarks locator for hyperparameter and protocol details because upstream paper and NIM-run tables are not presented as strictly matched-protocol checkpoint-only vs serving re-run tables in the provided findings. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://arxiv.org/html/2501.06158v1, https://build.nvidia.com/nvidia/genmol-generate/modelcard
- Per-GPU runtime wall-time values for some SKUs are reported on the benchmarks page; per-GPU wall-time values for SKUs beyond those enumerated on the benchmarks locator are not present in the provided findings (evidence gap). Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol
- Exact dataset splits and full SAFE-DRUGS provenance (train/test/val) are not enumerated in the provided primary sources (benchmarks page names SAFE-DRUGS but does not report explicit split names). Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html

### Safety

- Model weights and source-code licensing distinctions are published by NVIDIA: model weights governed by the NVIDIA Open Model License and source code under Apache-2.0 as reported on the GenMol model card and the NIM API reference and HF model card. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-genmol, https://huggingface.co/nvidia/NV-GenMol-89M-v2
- Evidence gap: The provided primary sources do not publish an explicit calibration protocol for FP32 property scores nor provide upstream primary guidance on clinical deployment or PHI handling; do not assume calibrated probabilities or clinical readiness from the available artifacts. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard
- Operational use of the GenMol NIM/NGC container is governed by NIM/NGC distribution and product terms as implied by the NGC catalog and release notes; an explicit EULA URL was not present in the provided findings (evidence gap). Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's GenMol NIM skill is first-party operating guidance for SAFE—not ordinary SMILES—input, generation modes, QED/LogP ranking, artifacts, validation, and hosted/local operation. Verify the exact Forge image/version and use Forge's live request contract before invocation.
- [genmol-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/genmol-nim)

### `related-multi-model-pipeline`

The NVIDIA BioNeMo drug-discovery meta-skill composes GenMol, DiffDock, and Boltz2. Use it as a workflow template only after independently selecting exact Forge versions, reconciling SAFE/SMILES and structure artifacts at every boundary, and validating each intermediate result; it is not a head-to-head quality benchmark.
- [drug-discovery-pipeline](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/meta-skills/drug-discovery-pipeline)

### `related-cheminformatics-validation`

NVIDIA BioNeMo's nvMolKit skill is related GPU-batched cheminformatics guidance for fingerprints, similarity, conformers, force-field optimization, clustering, and substructure checks. Use it for large-batch ligand or generated-molecule validation when installed; it does not establish any model's request schema, quality, or Forge runtime behavior, and plain RDKit is generally more appropriate for one-off molecules.
- [nvmolkit-usage](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/nvMolKit)

## Primary sources

### GenMol model card (Build NVIDIA)

- URL: https://build.nvidia.com/nvidia/genmol-generate/modelcard
- Publisher: NVIDIA (build.nvidia.com)
- Type: `model-card`
- Primary because: Official GenMol model card published by NVIDIA describing NV-GenMol-89M-v2 checkpoint, inputs, outputs, and licensing.
- Scope: NV-GenMol-89M-v2 model card and usage notes
- Supports: checkpoint identity (NV-GenMol-89M-v2)
- Supports: architecture summary (masked diffusion, SAFE)
- Supports: license statements for weights and source
- Supports: high-level input/output descriptions

### Hugging Face model card for NV-GenMol-89M-v2

- URL: https://huggingface.co/nvidia/NV-GenMol-89M-v2
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official HF model card entry referencing NV-GenMol-89M-v2 checkpoint and documented maxima (input/output length) and parameter count.
- Scope: NV-GenMol-89M-v2 HF model card
- Supports: checkpoint identity (NV-GenMol-89M-v2)
- Supports: parameter count (~89M)
- Supports: maximum input/output length (512 tokens)

### GenMol NIM release notes (latest)

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html
- Publisher: NVIDIA (docs.nvidia.com)
- Type: `official-documentation`
- Primary because: Official NIM release notes documenting GenMol NIM v2.0.0 upgrade to NV-GenMol-89M-v2 and validated GPU matrix.
- Scope: GenMol NIM v2.0.0 release notes
- Supports: statement that GenMol NIM v2.0.0 upgrades GenMol to NV-GenMol-89M-v2
- Supports: validated GPU matrix listing
- Supports: default noise and temperature defaults for NIM API

### GenMol NIM v2.0.0 release notes (versioned path)

- URL: https://docs.nvidia.com/nim/bionemo/genmol/2.0.0/release-notes.html
- Publisher: NVIDIA (docs.nvidia.com)
- Type: `official-documentation`
- Primary because: Versioned release notes indicating GenMol NIM v2.0.0 upgrade to NV-GenMol-89M-v2 (provided in findings).
- Scope: GenMol NIM v2.0.0 release notes (versioned)
- Supports: Release 2.0.0 upgrades GenMol to the NV-GenMol-89M-v2 checkpoint
- Supports: GenMol NIM version is updated to 2.0.0
- Supports: Validated GPU matrix includes listed SKUs

### GenMol NIM benchmarks (GenMol benchmarks page)

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Publisher: NVIDIA (docs.nvidia.com)
- Type: `official-documentation`
- Primary because: NIM benchmarks page providing numeric quality metrics and runtime wall-times for GenMol v1 and v2 tasks including motif-extension and scaffold-decoration.
- Scope: GenMol NIM benchmarks (v2 reported metrics)
- Supports: motif-extension and scaffold-decoration v2 metrics and hyperparameters (validity, uniqueness, diversity, novelty, quality)
- Supports: runtime wall-time for H100 and other SKUs (generating 1000 molecules across 10 tests)
- Supports: benchmark hyperparameters (mask_length, temperature, noise) as listed for tasks

### GenMol NIM endpoints documentation

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Publisher: NVIDIA (docs.nvidia.com)
- Type: `official-documentation`
- Primary because: Endpoint documentation describing /generate inputs, parameter ranges, defaults, and behavior (including 'smiles' null => de novo).
- Scope: GenMol NIM endpoints
- Supports: endpoint parameter names and defaults (smiles, num_molecules, temperature, noise ranges)
- Supports: behavior when template is null => de novo generation
- Supports: num_molecules accepted range and default

### GenMol NIM getting-started

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html
- Publisher: NVIDIA (docs.nvidia.com)
- Type: `official-documentation`
- Primary because: Getting-started docs documenting SAFE input examples and masked placeholder syntax.
- Scope: GenMol NIM getting-started examples
- Supports: SAFE/SMILES input examples
- Supports: masked fragment placeholder syntax examples

### NGC catalog entry: GenMol NIM container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: NGC catalog entry describing GenMol NIM container packaging and that the container includes GenMol model weights and runtime components.
- Scope: GenMol NIM container (NGC)
- Supports: NIM container distribution and inclusion of model weights and inference code
- Supports: statement of GenMol v2.0 in NGC catalog
- Supports: deployment and release metadata

### NIM API reference: nvidia-genmol

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- Publisher: NVIDIA (docs.api.nvidia.com)
- Type: `official-documentation`
- Primary because: NIM API reference describing API-level parameters and intended usage.
- Scope: NIM API reference for GenMol endpoints
- Supports: API parameter descriptions and intended usage
- Supports: license statement repeated in API reference
- Supports: model description and supported tasks

### GenMol method paper (arXiv 2501.06158 v1 HTML)

- URL: https://arxiv.org/html/2501.06158v1
- Publisher: arXiv
- Type: `paper`
- Primary because: ArXiv preprint describing GenMol methods and reporting upstream experimental metrics (including linker, motif extension, scaffold decoration results).
- Scope: ArXiv GenMol experimental results
- Supports: Upstream experimental metrics for motif extension, scaffold decoration, one-step linker, and other tasks as reported in paper tables
- Supports: method descriptions and benchmark dataset (extracted fragments from ten known drugs)

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/genmol-generate
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-genmol
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Immutable checkpoint revision/hash for NV-GenMol-89M-v2 not reported in the available primary sources (no canonical checksum or immutable download URL identified in findings).
- Evidence gap: Exact QED and SA thresholds or full computation details used to produce the 'quality' metric are not specified in the available primary sources; reproducing 'quality' requires those details.
- Evidence gap: Exact dataset split names (train/test/val) and full SAFE-DRUGS provenance beyond the dataset name are not enumerated in the provided primary sources.
- Evidence gap: Direct, immutable-checkpoint-mapped numeric benchmark table tying the arXiv paper's one-step linker numbers to NV-GenMol-89M-v2 is not present in the provided findings (paper reports upstream experiments; NIM release notes claim v2 improves linker success but do not publish checkpoint-hash mapping).
- Evidence gap: Per-GPU runtime wall-time values for GPU SKUs beyond those listed on the benchmarks page are not enumerated at the benchmarks locator in the provided findings.
- Evidence gap: The provided primary sources do not specify numbered table/figure/section locators in the arXiv HTML for the one-step linker row required to assert a precise cell locator; therefore numeric cells from the paper are treated as paper-level experimental results and not mapped to an immutable checkpoint in this dossier.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].direction: $.benchmarks[0].direction: 'higher-is-better (for validity, uniqueness, diversity, novelty, quality as defined)' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].direction: $.benchmarks[1].direction: 'higher-is-better (for listed metrics)' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses forbidden secondary URL https: $.sources[16] uses forbidden secondary URL https://developer.nvidia.com/blog/evaluating-genmol-as-a-generalist-foundation-model-for-molecular-generation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/getting-started.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/molmim-generate Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/genmol-generate: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[3]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
