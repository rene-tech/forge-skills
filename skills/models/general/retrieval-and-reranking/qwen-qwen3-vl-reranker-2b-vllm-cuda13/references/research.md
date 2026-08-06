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

- Research key: `huggingface-co-qwen-qwen3-vl-reranker-2b-03d6241fb5`
- Independent audit: `revised`
- Researched: `2026-08-06T09:47:35.818218+00:00`

Upstream primary files for the exact checkpoint Qwen/Qwen3-VL-Reranker-2B (model card README and config.json) show this checkpoint is a Qwen3-VL-family reranker variant with architecture type "Qwen3VLForConditionalGeneration" (per config.json) and that the model series is intended for multimodal retrieval and reranking across text, images, screenshots, videos, and mixed-modality inputs. The embedding README documents the embedding sibling and confirms the reranker role in a two-stage retrieval pipeline; the embedding README also reports the 2B parameter scale and a 32K sequence length for family members. The upstream artifacts checked do not contain an immutable revision identifier, explicit license metadata in the checked files, numeric checkpoint-matched public benchmark tables, nor exact low-level preprocessing, tokenization, output-shape, or score-calibration contracts; those are reported below as evidence gaps with exact checked paths.

## Identity

- Upstream name: Qwen3-VL-Reranker-2B
- Checkpoint/version: Qwen/Qwen3-VL-Reranker-2B
- Immutable revision: Evidence gap: immutable checkpoint revision not reported in the upstream model card or repository; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json
- Parameter scale: 2 billion parameters
- Architecture/head: Model type listed as "Qwen3VLForConditionalGeneration" in config.json; upstream model card and repository describe the Qwen3-VL-Reranker series as a multimodal reranker built on the Qwen3-VL family that refines retrieval results for query-document pairs.
- License: Evidence gap: model-weight and code license not reported in the provided upstream files checked; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json
- Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md

## Selection

### Recommended

- **Multimodal reranking for query-document pairs where fine-grained relevance scoring is required** — Upstream model card and repository describe the Qwen3-VL-Reranker model series as a reranker that refines retrieval results and operates on query-document pairs, intended for multimodal information retrieval and cross-modal understanding.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- **Image–text retrieval reranking (multimodal candidate reranking)** — The upstream model card and repository state the model suite accepts text and images and that the reranker refines retrieval results in a multimodal retrieval pipeline.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- **Video–text matching reranking within a multimodal retrieval workflow** — The upstream model card indicates the suite accepts video as an input modality and positions the reranker as the component to refine retrieval results.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B

### Conditional

- **Text-only reranking (use conditionally with validation)** — Appropriate only when downstream validation confirms task fit because the upstream files document multimodal support but do not provide text-only specialized benchmarks or exact text-only contract for this specific checkpoint.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- **Screenshot retrieval reranking (use conditionally with downstream preprocessing validation)** — Upstream model card lists screenshots as a supported modality but does not specify screenshot-specific preprocessing, formatting, or benchmark conditions for this checkpoint; validate preprocessing and scoring on intended screenshot data before production use.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- **Multilingual reranking (conditional)** — Upstream materials indicate family-level multilingual support in documentation for the model series, but the exact checkpoint-level language coverage, per-language benchmarks, and formatting guidance for this specific 2B reranker checkpoint are not provided in the checked upstream files; perform per-language validation.
  Scope: Qwen/Qwen3-VL-Reranker-2B (family-level multilingual claims exist)
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md

### Avoid

- **Using the reranker checkpoint as an embedding model that outputs vector embeddings for ANN retrieval** — Upstream materials separate the embedding model and the reranker: the embedding model is described as generating high-dimensional vectors while the reranker is described as refining retrieval results with pairwise relevance scoring; this indicates the reranker is not the embedding-producing checkpoint.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- **Relying on reranker outputs as calibrated probabilities or fixed thresholds for automated high-stakes decisions** — Upstream files do not provide score-range semantics, calibration guidance, or thresholding instructions for this checkpoint; no calibration or probability semantics are documented in the checked primary files.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- **Assuming undocumented preprocessing, truncation, batching, or multimodal packing contracts in production-critical pipelines** — Upstream README and config.json do not specify exact tokenization, image/video preprocessing, cropping, resizing, padding, multimodal packing, or batching behavior for this checkpoint; these are gaps that require local validation.
  Scope: Qwen/Qwen3-VL-Reranker-2B
  Evidence: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json

## Input preparation

### Semantic inputs

- The upstream model card and repository state the suite accepts multimodal inputs including text, images, screenshots, videos, and mixtures of these modalities. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- The reranker operates on query-document pair semantics to refine retrieval results in a two-stage pipeline (embedding + reranker) as described in the upstream repository materials. Sources: https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- The model is designed for multimodal information retrieval and cross-modal understanding per the upstream model card. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B

### Accepted formats

- Accepted semantic modalities documented upstream are text, image, screenshot, video, and mixed-modality inputs (model-card stated modalities). Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- Evidence gap: the upstream files do not specify official file/container formats, serialization schema, or exact request object structure for these modalities; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/refs%2Fpr%2F3/README.md

### Preprocessing

- Official usage examples and dependency requirements for the checkpoint are present in the README snapshots (transformers version and qwen-vl-utils usage references appear in the checked README snapshots). Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/refs%2Fpr%2F3/README.md
- Evidence gap: the upstream files do not specify exact tokenization, image preprocessing, video frame sampling, resizing, cropping, padding, truncation, or multimodal packing behavior for this checkpoint; checked README.md and config.json paths.

### Pre-submit validation

- Inputs should be validated to stay within the reported sequence length for family members (the embedding README reports a sequence length of 32K for family models). Sources: https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- Evidence gap: the upstream files do not specify image-count limits, resolution constraints, video duration/frame limits, or explicit invalid-input edge-case rules for this exact checkpoint; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json

### Task-specific formatting

- Official example initialization in the upstream README references model_path "Qwen/Qwen3-VL-Reranker-2B" and provides basic usage pointers in the repository examples. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/refs%2Fpr%2F3/README.md
- Evidence gap: the upstream artifacts do not provide an exact official prompt template, pair-order example, or control-field schema for reranker input formatting for this checkpoint; checked README.md and PR README snapshot.

## Output interpretation

### Outputs

- The reranker model computes fine-grained relevance scores for each query-document pair and is described upstream as the component that refines retrieval results. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- The documented capability of the checkpoint in upstream materials is reranking/refinement of retrieval results (i.e., the supported ability is rerank). Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- Evidence gap: the upstream files do not specify the exact output tensor shape, dtype, score range, or whether returned scores are logits, normalized similarities, or probabilities; checked README.md and config.json.

### Interpretation

- Scores emitted by the reranker should be interpreted as pairwise relevance estimates for relative ordering within a candidate set (the reranker is a pairwise/refinement component in the retrieval pipeline). Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- Evidence gap: the upstream files do not establish that reranker scores are calibrated probabilities or that fixed universal thresholds apply across tasks or datasets; checked README.md and config.json.

### Post-inference validation

- Evidence gap: downstream validation is required before using absolute reranker scores or fixed thresholds for decision-making because no calibration or thresholding guidance is present in the checked upstream files.
- Post-inference sanity checks should focus on ranking behavior and relative ordering for the intended candidate set because the upstream capability is documented as reranking via fine-grained relevance estimation. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### Alibaba-NLP/gte-reranker-modernbert-base — `insufficient-evidence`

- Task: Reranking under multimodal retrieval settings
- Criteria: No primary-source evidence for the alternative checkpoint present in the checked findings; unable to perform a protocol-matched comparison.
- Rationale: The checked upstream files provide evidence for Qwen3-VL-Reranker-2B multimodal reranking capability; the findings do not include a primary model card or repository for the alternative, so a direct checkpoint-scoped comparison is not supportable.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

### BAAI/bge-reranker-v2-m3 — `insufficient-evidence`

- Task: Reranking under multimodal retrieval settings
- Criteria: No primary-source evidence for the alternative checkpoint present in the checked findings; unable to perform a protocol-matched comparison.
- Rationale: Primary evidence exists for Qwen3-VL-Reranker-2B but not for the alternative within the provided findings.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

### NVIDIA Llama 3.2 NV-RerankQA 1B v2 — `insufficient-evidence`

- Task: Direct checkpoint-quality or contract comparison
- Criteria: No primary-source evidence for the alternative checkpoint present in the checked findings.
- Rationale: The reviewed findings do not include a canonical primary source for the alternative checkpoint.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

### NVIDIA Llama Nemotron Rerank 1B v2 — `insufficient-evidence`

- Task: Direct checkpoint-quality or contract comparison
- Criteria: No primary-source evidence for the alternative checkpoint present in the checked findings.
- Rationale: The reviewed findings do not include a canonical primary source for the alternative checkpoint.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

### NVIDIA Llama Nemotron Rerank VL 1B v2 — `insufficient-evidence`

- Task: Direct checkpoint-quality or contract comparison
- Criteria: No primary-source evidence for the alternative checkpoint present in the checked findings.
- Rationale: The reviewed findings do not include a canonical primary source for the alternative checkpoint.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

### Qwen/Qwen3-Reranker-0.6B — `insufficient-evidence`

- Task: Direct checkpoint-quality comparison
- Criteria: No primary-source evidence for the peer checkpoint present in the checked findings.
- Rationale: Although in the broader product line, the reviewed findings do not include the peer’s primary model card or benchmark evidence.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

### Qwen/Qwen3-Reranker-4B — `insufficient-evidence`

- Task: Direct checkpoint-quality comparison
- Criteria: No primary-source evidence for the peer checkpoint present in the checked findings.
- Rationale: The reviewed findings do not include the peer’s primary model card or benchmark evidence.
- Comparison conditions: insufficient primary evidence for the alternative in the reviewed sources.
- Evidence:

## Limitations and safety

### Limitations

- Evidence gap: immutable upstream model revision is not reported in the checked upstream model card or config.json; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json
- Evidence gap: the upstream files do not specify exact preprocessing behavior (tokenization, image resizing/cropping/padding, video frame sampling, truncation, batching, or multimodal packing rules) for this checkpoint; these details were not found in README.md or config.json.
- Evidence gap: the upstream files do not specify exact output tensor shape, score dtype, score range, or whether reranker scores are logits, similarities, or probabilities for this checkpoint; checked README.md and config.json.
- Upstream checked materials do not contain a checkpoint-matched public benchmark table with dataset/split/metric/value for Qwen3-VL-Reranker-2B; family-level performance claims appear in model-card prose but without dataset/split/metric rows in the checked paths. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- The reranker is described upstream as architecturally distinct from the embedding model and intended to refine retrieval results rather than to serve as a vector-embedding generator. Sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B, https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md

### Safety

- Forge policy: because the checked upstream files do not provide privacy, PHI, or proprietary-data handling guidance for this checkpoint, sensitive-data use should require downstream governance, review, and appropriate controls.
- Forge policy: because no calibration or thresholding guidance is reported in upstream materials, high-stakes automated decisions should not rely on absolute reranker scores without task-specific validation and calibration.
- Forge policy: the upstream materials document retrieval and matching uses but do not establish clinical validation or healthcare-specific safety claims for this checkpoint; do not deploy for clinical decision-making without separate validation and approvals.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-VL-Reranker-2B model card

- URL: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B
- Publisher: Qwen
- Type: `model-card`
- Primary because: Official upstream model card and repository page for the exact checkpoint Qwen/Qwen3-VL-Reranker-2B; used to verify checkpoint identity, documented modalities, and high-level capability statements.
- Scope: Qwen/Qwen3-VL-Reranker-2B checkpoint identity and README content
- Supports: identity.checkpoint
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: avoidUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.outputs
- Supports: limitations

### Qwen3-VL-Reranker-2B README (PR snapshot)

- URL: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/refs%2Fpr%2F3/README.md
- Publisher: Qwen
- Type: `repository`
- Primary because: Upstream repository README snapshot used to confirm example usage, dependency/version mentions, and usage initialization patterns for the exact checkpoint.
- Scope: Qwen/Qwen3-VL-Reranker-2B README PR snapshot
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.taskSpecificFormatting
- Supports: researchSummary

### Qwen3-VL-Reranker-2B README (blame/main snapshot)

- URL: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blame/main/README.md
- Publisher: Qwen
- Type: `repository`
- Primary because: Repository blame snapshot used to verify README content variants and confirm documented modality and capability text for the exact checkpoint.
- Scope: Qwen/Qwen3-VL-Reranker-2B README blame snapshot
- Supports: researchSummary
- Supports: inputPreparation.semanticInputs
- Supports: recommendedUseCases

### Qwen3-VL-Embedding-2B README (family-level embedding/reranker framing and parameter-scale statements)

- URL: https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/blob/main/README.md
- Publisher: Qwen
- Type: `repository`
- Primary because: Upstream embedding README for the Qwen3-VL family used to verify family-level parameter scales, sequence length, and the two-stage embedding + reranker framing referenced by the reranker model card.
- Scope: Qwen3-VL-Embedding and family-level documentation (embedding + reranker framing)
- Supports: identity.parameterScale
- Supports: researchSummary
- Supports: avoidUseCases
- Supports: inputPreparation.validation
- Supports: limitations

### Qwen3-VL-Reranker-2B config.json

- URL: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json
- Publisher: Qwen
- Type: `repository`
- Primary because: Upstream config.json for the exact checkpoint used to verify model type, architecture name in-code, dtype entries, token IDs, hidden sizes, and other low-level configuration fields available in the checked file.
- Scope: Qwen/Qwen3-VL-Reranker-2B config.json (exact checkpoint configuration)
- Supports: identity.architecture
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: researchSummary

### Qwen3-VL-Reranker-2B model card — cited revision/file

- URL: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/README.md
- Publisher: Qwen
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: Qwen/Qwen3-VL-Reranker-2B checkpoint identity and README content
- Supports: Exact audited claim citation

## Evidence gaps

- Evidence gap: No immutable checkpoint revision or explicit immutable revision field was found in https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (checked README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json.
- Evidence gap: No checkpoint-matched public benchmark table or numeric row for Qwen/Qwen3-VL-Reranker-2B was found at the checked primary paths: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md root), https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/refs%2Fpr%2F3/README.md, or https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json; these paths were inspected for dataset/split/metric/value entries and none were present for the exact 2B reranker checkpoint.
- Evidence gap: The upstream files checked (README.md root, PR README snapshot, and config.json) do not specify official file/container formats, serialization schema, or exact request object structure for the documented modalities; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/refs%2Fpr%2F3/README.md.
- Evidence gap: The upstream files checked do not specify exact tokenization, image preprocessing, video frame sampling, resizing, cropping, padding, truncation strategies, or multimodal packing rules for the Qwen3-VL-Reranker-2B checkpoint; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/README.md and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json.
- Evidence gap: The upstream files checked do not specify exact output tensor shape, dtype, score units, or whether returned scores are logits, normalized similarities, or probabilities for Qwen/Qwen3-VL-Reranker-2B; checked https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B (README.md) and https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/config.json.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://huggingface.co/papers/2601.04720 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[2] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B/blob/main/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
