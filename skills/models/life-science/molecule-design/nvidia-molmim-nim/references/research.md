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

- Research key: `build-nvidia-com-nvidia-molmim-generate-212f025c33`
- Independent audit: `revised`
- Researched: `2026-07-23T23:12:52.061565+00:00`

MolMIM is a latent-variable probabilistic auto-encoder for small-molecule SMILES developed by NVIDIA. The model uses a Perceiver encoder to map variable-length SMILES text to a fixed-length latent code and a Transformer decoder to autoregressively decode SMILES. Primary NVIDIA documentation (build model card, NIM API reference, BioNeMo model page) and the canonical MolMIM preprint (arXiv) report a 65.2M-parameter encoder-decoder architecture with the numeric layer/hidden/head/FF dimensions listed in identity. NVIDIA NIM documentation exposes endpoints for generation/sampling, /embedding, /hidden, and /decode and documents using latent-space perturbation (including CMA-ES examples) to sample candidate molecules. Primary sources do not report an immutable upstream checkpoint SHA or container digest that unequivocally ties published sampling metrics or numeric benchmarks to a specific immutable artifact. Primary documentation contains conflicting token-length claims (see inputPreparation.preprocesssing) and does not publish exhaustive low-level tokenization/token-indexing, SMILES canonicalization, or complete per-field JSON request/response schemas for all NIM endpoints. Primary sources also present conflicting license statements (see identity.license).

## Identity

- Upstream name: MolMIM (NVIDIA)
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 65.2 million parameters
- Architecture/head: Perceiver encoder + Transformer decoder (both encoder and decoder contain 6 layers; hidden size 512; 8 attention heads; feed‑forward dim 2048)
- License: Primary sources present conflicting license statements: catalog.ngc.nvidia.com lists the NVIDIA AI Foundations Model Community License while the BioNeMo framework page lists Apache License (see evidenceUrls).
- Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-molmim, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html, https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-, https://arxiv.org/pdf/2208.09016

## Selection

### Recommended

- **Sampling novel small-molecule SMILES by perturbing latent representations from a seed molecule** — Primary NVIDIA model card, NIM overview, and the MolMIM preprint describe MolMIM as a probabilistic latent-variable auto-encoder that samples valid SMILES by perturbing clustered latent codes derived from a seed molecule.
  Scope: MolMIM upstream model behavior and NIM-serving behavior as described on the NVIDIA model card and NIM overview (upstream-checkpoint evidence for model behavior; NIM-serving evidence for exposed endpoints).
  Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html, https://arxiv.org/pdf/2208.09016
- **Compute fixed-length molecular embeddings from SMILES for downstream machine-learning tasks** — The official NIM endpoints documentation documents an /embedding endpoint that returns fixed-length numerical embeddings for a given input SMILES string.
  Scope: MolMIM /embedding endpoint (NIM runtime as documented).
  Evidence: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html
- **Use MolMIM latent-space representations in optimization workflows (example: CMA-ES guided optimization) for early-stage candidate generation under expert review** — NVIDIA primary documentation and the NGC model page describe latent-space optimization capability and document CMA-ES usage for optimization in examples and notebooks.
  Scope: MolMIM upstream behavior (as described in BioNeMo and model card) and NIM-served examples (notebook and NIM overview).
  Evidence: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-, https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/bionemo-framework/1.10/notebooks/MolMIM_GenerativeAI_local_inference_with_examples.html

### Conditional

- **Using generated molecules as candidates for downstream experimental prioritization** — Generated molecules must undergo domain-expert review, cheminformatics validation, synthesis-feasibility checks, and laboratory safety review before experimental use; primary sources present MolMIM as a research tool and do not document clinical validation or regulatory approval.
  Scope: MolMIM as documented on NVIDIA model card, NIM overview, and BioNeMo framework pages (upstream model behavior; NIM-serving examples).
  Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html

### Avoid

- **Clinical diagnostic use or direct medical decision making** — Primary NVIDIA model-card and NGC explainability pages present MolMIM for molecular design and research and do not document clinical validation, authorization, or regulatory approval for clinical use.
  Scope: MolMIM as documented on NVIDIA build model card and NGC explainability page.
  Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-

## Input preparation

### Semantic inputs

- Molecular sequences expressed as SMILES strings (text) are accepted as model input. Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-molmim

### Accepted formats

- Accepted input formats documented as Comma-Separated Values (CSV) and SMILES strings (text). Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-molmim

### Preprocessing

- MolMIM represents molecules as text sequences (SMILES) and maps variable-length sequences to a fixed-length latent representation via a Perceiver encoder. Sources: https://arxiv.org/pdf/2208.09016, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html, https://build.nvidia.com/nvidia/molmim-generate/modelcard
- Primary sources present conflicting token-length claims: the NVIDIA build model card and docs.api.nvidia.com report a maximum input length of 512 tokens, while the BioNeMo framework model page reports a maximum input length of 128 tokens (including BOS/EOS). Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-molmim, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html
- Low-level tokenization details (tokenizer vocabulary size, token-indexing scheme), SMILES canonicalization and stereochemistry-normalization rules, and featurizer implementation details are not specified in the checked primary documentation. Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html, https://docs.api.nvidia.com/nim/reference/nvidia-molmim

### Pre-submit validation

- Primary NIM and model-card documentation do not provide exhaustive per-field input-validation bounds (e.g., exact token-index ranges, allowed character sets, tokenizer error codes); callers should validate SMILES format prior to submission. Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html, https://build.nvidia.com/nvidia/molmim-generate/modelcard

### Task-specific formatting

- NIM endpoints documented for MolMIM include generation and sampling endpoints (generate), as well as endpoints that return embeddings and hidden/latent states (/embedding, /hidden, /decode); endpoint documentation provides high-level parameter names but does not publish a complete exhaustive per-field JSON schema in the checked pages. Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html, https://docs.nvidia.com/nim/bionemo/molmim/latest/deployment-guide.html

## Output interpretation

### Outputs

- The /embedding endpoint returns fixed-length numerical embeddings (vector representations) for a given input SMILES string. Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html
- The /hidden endpoint returns the model's hidden/latent state representation for a given input SMILES string. Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html
- The /decode endpoint decodes a hidden state representation back into a SMILES string (text molecular sequence). Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html, https://docs.nvidia.com/nim/bionemo/molmim/latest/advanced-usage.html
- The generation/sampling endpoint produces generated SMILES strings as its principal textual output (documentation describes sampling by perturbing latent codes). Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html

### Interpretation

- Generated outputs are SMILES strings representing proposed molecular structures; documentation describes sampling by perturbing clustered latent codes from a seed molecule. Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://arxiv.org/pdf/2208.09016
- Embedding vectors are fixed-length numerical representations intended for downstream machine-learning tasks; primary documentation does not report per-molecule calibrated confidence or likelihood scores. Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html, https://build.nvidia.com/nvidia/molmim-generate/modelcard

### Post-inference validation

- Primary sources do not supply published numeric benchmark tables tied unequivocally to an immutable served NIM/container artifact; BioNeMo reports sampling metrics for named variants but the checked pages do not tie those metrics to an immutable checkpoint identifier or specify dataset/split/protocol at the required granularity. Sources: https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html, https://build.nvidia.com/nvidia/molmim-generate/modelcard

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### nvidia-genmol-2-0-0-nim — `insufficient-evidence`

- Task: various molecule generation tasks
- Criteria: No protocol-matched, head-to-head benchmark evidence (dataset/split/metric/protocol) tying MolMIM to the named alternative was found in the checked primary pages.
- Rationale: Checked NVIDIA model card and NIM overview document MolMIM behavior and endpoints but do not publish matched comparative benchmarks against the named alternative; absence of protocol-matched evidence prevents a comparative verdict.
- Comparison conditions: No protocol details (dataset/split/metric/protocol) documented for both models in the checked primary sources.
- Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html

### nvidia-genmol-nim — `insufficient-evidence`

- Task: various molecule generation tasks
- Criteria: No protocol-matched, head-to-head benchmark evidence (dataset/split/metric/protocol) tying MolMIM to the named alternative was found in the checked primary pages.
- Rationale: Checked NVIDIA model card and NIM overview document MolMIM behavior and endpoints but do not publish matched comparative benchmarks against the named alternative; absence of protocol-matched evidence prevents a comparative verdict.
- Comparison conditions: No protocol details (dataset/split/metric/protocol) documented for both models in the checked primary sources.
- Evidence: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html

## Limitations and safety

### Limitations

- Model intended for molecular drug discovery and design research; not documented as clinically validated or authorized for clinical use. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-, https://build.nvidia.com/nvidia/molmim-generate/modelcard
- MolMIM may not perform well on sequences highly divergent from the ZINC-15 training distribution (documented technical limitation). Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-
- Operational constraints: minimum/tested system hardware and recommended GPU configurations are documented for the NIM, but an immutable container digest or upstream checkpoint identity mapping to those runtime artifacts is not reported in the checked primary pages. Sources: https://docs.nvidia.com/nim/bionemo/molmim/1.0.0/support-matrix.html, https://docs.nvidia.com/nim/bionemo/molmim/latest/deployment-guide.html, https://build.nvidia.com/nvidia/molmim-generate/deploy
- Licensing ambiguity between primary pages: catalog.ngc.nvidia.com lists the NVIDIA AI Foundations Model Community License while the BioNeMo framework page lists Apache License; this conflict is present in primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html
- Evidence gap: Immutable upstream checkpoint revision identifier (artifact checksum, git SHA, or immutable release id) for the exact checkpoint served by the MolMIM NIM/container is not reported in the checked primary sources (deployment guide, model card). Sources: https://docs.nvidia.com/nim/bionemo/molmim/latest/deployment-guide.html, https://build.nvidia.com/nvidia/molmim-generate/modelcard

### Safety

- MolMIM is presented in primary sources for research use in molecular design; primary findings do not report authorization for clinical use or clinical validation. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-, https://build.nvidia.com/nvidia/molmim-generate/modelcard
- Evidence gap: The checked primary pages do not include documented adversarial/failure-mode analyses, hallucination characterizations, dual-use mitigation procedures, or per-molecule calibrated confidence outputs; users should apply domain expert review and responsible-use controls. Sources: https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html, https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's MolMIM skill documents generation, embedding, hidden-state, decoding, sampling, CMA-ES optimization, SMILES/property validation, and the hosted-versus-local endpoint boundary. Use only the routes Forge declares for its deployed NIM and do not invent hosted latent endpoints.
- [molmim-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/molmim-nim)

### `related-cheminformatics-validation`

NVIDIA BioNeMo's nvMolKit skill is related GPU-batched cheminformatics guidance for fingerprints, similarity, conformers, force-field optimization, clustering, and substructure checks. Use it for large-batch ligand or generated-molecule validation when installed; it does not establish any model's request schema, quality, or Forge runtime behavior, and plain RDKit is generally more appropriate for one-off molecules.
- [nvmolkit-usage](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/nvMolKit)

## Primary sources

### MolMIM model card (build.nvidia.com)

- URL: https://build.nvidia.com/nvidia/molmim-generate/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official MolMIM model card on NVIDIA build site describing architecture, parameter count, input formats, and general usage.
- Scope: MolMIM model card (build site)
- Supports: MolMIM is a latent variable model trained over SMILES and can sample novel molecules from latent space.
- Supports: Perceiver encoder + Transformer decoder architecture description and layer/hidden/head/FF dimensions.
- Supports: Parameter count: 65.2 million parameters.
- Supports: Accepted input formats: CSV and SMILES.
- Supports: Maximum input length reported as 512 tokens (per model card).
- Supports: MolMIM performs controlled generation to find molecules with desired properties.

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/molmim-generate
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: Forge-to-upstream starting source
- Supports: Forge-to-upstream exact-version identity

### MolMIM model page in BioNeMo framework (1.10)

- URL: https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html
- Publisher: NVIDIA BioNeMo framework documentation
- Type: `official-documentation`
- Primary because: BioNeMo framework model page reporting model behavior, intended use, and sampling/quality metrics for named variants.
- Scope: BioNeMo MolMIM model page (1.10)
- Supports: Reports that MolMIM uses a Perceiver encoder and Transformer decoder and provides fixed-length latent representations.
- Supports: Reports numeric sampling/quality metrics for named variants (page reports metrics for named service/variant versions).
- Supports: States MolMIM is listed with an Apache License (per BioNeMo page).
- Supports: Documents a differing token-length claim (maximum input length 128 tokens; maximum output length 512 tokens) relative to other primary sources.

### MolMIM NIM overview

- URL: https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: NIM overview describing MolMIM purpose, probabilistic auto-encoder behavior, and latent-space sampling.
- Scope: MolMIM NIM overview
- Supports: MolMIM is a probabilistic auto-encoder providing a fixed-length representation of variable-length SMILES strings.
- Supports: MolMIM can sample valid SMILES strings by perturbing its clustered latent space.

### MolMIM NIM endpoints

- URL: https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM endpoints documentation listing available HTTP endpoints and documented output fields.
- Scope: MolMIM NIM endpoints
- Supports: Available NIM endpoints include generation and sampling endpoints as well as /embedding, /hidden, /decode.
- Supports: The /embedding endpoint returns numerical embeddings; /hidden returns hidden/latent state; /decode decodes hidden state to SMILES.

### MolMIM NIM deployment guide (container info)

- URL: https://docs.nvidia.com/nim/bionemo/molmim/latest/deployment-guide.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Deployment guide indicating Docker commands to obtain and run the MolMIM NIM container image and runtime behavior.
- Scope: MolMIM NIM deployment guide
- Supports: The NVIDIA NIM container for MolMIM uses Docker image tag nvcr.io/nim/nvidia/molmim:1.0.0 (deployment guide).
- Supports: On first startup, the MolMIM NIM container downloads the MolMIM checkpoint from NGC; checkpoint weights can be cached locally.
- Supports: Runtime flags and environment variables for GPU acceleration and authentication are documented.

### NIM API reference: nvidia-molmim

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-molmim
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: API reference summarizing model architecture, token limits, and input/output formats for MolMIM.
- Scope: NIM API reference for MolMIM
- Supports: MolMIM is a latent variable encoder-decoder trained over SMILES.
- Supports: Model architecture and high-level numeric fields are summarized in the API reference.
- Supports: Accepted input formats include SMILES/CSV (as indicated in API reference).
- Supports: Maximum input length reported as 512 tokens in the API reference (conflicts with BioNeMo page for input length).
- Supports: Maximum output length reported differently on API reference (conflicts with BioNeMo page).
- Supports: Model version listed as MolMIM-24.03; training dataset listed as ZINC-15.

### MolMIM NIM support matrix (1.0.0)

- URL: https://docs.nvidia.com/nim/bionemo/molmim/1.0.0/support-matrix.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Versioned NIM support matrix page documenting hardware and runtime requirements for the 1.0.0 NIM.
- Scope: MolMIM NIM support matrix (1.0.0)
- Supports: Minimum and tested GPU/hardware configurations for NIM runtime are documented (minimum GPU memory requirement, single-GPU configuration, and tested GPU models).

### MolMIM NIM advanced usage

- URL: https://docs.nvidia.com/nim/bionemo/molmim/latest/advanced-usage.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Advanced usage notes for MolMIM NIM (endpoints, logging, and decode/reconstruction behavior).
- Scope: MolMIM NIM advanced usage
- Supports: Provides /decode endpoint behavior and /hidden endpoint behavior and engineering notes on logging and validation.
- Supports: Describes reconstruction accuracy measurement and decoding considerations.

### MolMIM explainability (NGC model card safety-and-security)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/molmim/-
- Publisher: NVIDIA NGC
- Type: `model-card`
- Primary because: NGC explainability/safety section documents intended domain and noted technical limitations.
- Scope: NGC MolMIM explainability/safety
- Supports: Intended domain: molecular drug discovery and design; output modality: SMILES text.
- Supports: Technical limitation noted: may not perform well on sequences divergent from ZINC-15.
- Supports: Model presented for research and development use only.
- Supports: MolMIM is provided under the NVIDIA AI Foundations Model Community License (per NGC page).

### MolMIM BioNeMo notebook examples (local inference)

- URL: https://docs.nvidia.com/bionemo-framework/1.10/notebooks/MolMIM_GenerativeAI_local_inference_with_examples.html
- Publisher: NVIDIA BioNeMo framework documentation
- Type: `official-documentation`
- Primary because: Canonical BioNeMo notebook demonstrating downloading pre-trained MolMIM model checkpoints for local inference and example workflows.
- Scope: BioNeMo MolMIM example notebook
- Supports: Demonstrates downloading pre-trained MolMIM checkpoints for local inference and example optimization workflows (CMA-ES).

### MolMIM deployment notes (build site)

- URL: https://build.nvidia.com/nvidia/molmim-generate/deploy
- Publisher: NVIDIA (build site)
- Type: `official-documentation`
- Primary because: Build site deployment notes documenting runtime requirements to deploy the MolMIM NIM container.
- Scope: MolMIM NIM deployment notes (build site)
- Supports: MolMIM NIM container requires Docker runtime with NVIDIA GPU support and specific runtime settings (deployment guidance).

### MolMIM canonical preprint (arXiv:2208.09016)

- URL: https://arxiv.org/pdf/2208.09016
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical preprint introducing MolMIM methodology and reporting architecture and evaluation claims.
- Scope: MolMIM original preprint
- Supports: Describes MolMIM as a probabilistic auto-encoder with a Perceiver encoder and Transformer decoder.
- Supports: Reports that MolMIM clusters chemically similar molecules and can sample unique and novel molecules via latent perturbations.
- Supports: Provides architectural details used by NVIDIA documentation (encoder/decoder layer counts, sizes) and evaluation claims in the original study.

## Evidence gaps

- Evidence gap: Immutable upstream checkpoint revision identifier (artifact checksum, git SHA, or immutable release id) for the exact checkpoint served by the MolMIM NIM/container is not reported on the deployment guide or model card (checked https://docs.nvidia.com/nim/bionemo/molmim/latest/deployment-guide.html and https://build.nvidia.com/nvidia/molmim-generate/modelcard).
- Evidence gap: Low-level tokenizer/tokenization vocabulary size, token-indexing scheme, SMILES canonicalization rules, and stereochemistry-normalization specifics are not specified on the checked primary documentation (checked https://build.nvidia.com/nvidia/molmim-generate/modelcard, https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html, and https://docs.api.nvidia.com/nim/reference/nvidia-molmim).
- Evidence gap: Official exhaustive per-field JSON request/response schemas, default values, and numeric bounds for all MolMIM NIM endpoints are not provided in the checked primary pages (checked https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html and https://docs.nvidia.com/nim/bionemo/molmim/latest/deployment-guide.html).
- Evidence gap: Per-molecule calibrated confidence scores or likelihood outputs are not documented for MolMIM in the checked primary documentation (checked https://docs.nvidia.com/nim/bionemo/molmim/latest/endpoints.html and https://build.nvidia.com/nvidia/molmim-generate/modelcard).
- Evidence gap: Detailed adversarial/failure-mode analyses, hallucination characterizations, and formal dual-use mitigation procedures are not present on the checked primary pages (checked https://build.nvidia.com/nvidia/molmim-generate/modelcard and https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html).
- Evidence gap: Protocol-matched, head-to-head benchmark comparisons between MolMIM (served or upstream variants) and named Forge peers (e.g., nvidia-genmol-2-0-0-nim, nvidia-genmol-nim) are not present in the checked primary pages; checked sources do not publish matched dataset/split/metric/protocol pairs for both sides (checked https://build.nvidia.com/nvidia/molmim-generate/modelcard and https://docs.nvidia.com/nim/bionemo/molmim/latest/overview.html).
- Evidence gap: Exact numeric benchmark values and the precise evaluation protocol (dataset name and split, sampling radius, seeds, and reproduction steps) for sampling/quality metrics reported on the BioNeMo model page are not tied to an immutable checkpoint identifier or table/figure with a verifiable locator; checked https://docs.nvidia.com/bionemo-framework/1.10/models/molmim.html for the sampling metrics section but the page does not provide an explicit immutable artifact locator (table/figure id) to verify checkpoint-scoped benchmark provenance.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/1.10.1/models/molmim.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretation_evidenceOnly: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
