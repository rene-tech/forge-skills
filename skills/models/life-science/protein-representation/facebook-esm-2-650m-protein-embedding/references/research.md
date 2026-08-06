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

- Research key: `huggingface-co-facebook-esm2-t33-650m-ur50d-e087b68cac`
- Independent audit: `revised`
- Researched: `2026-07-23T18:26:41.459698+00:00`

Checkpoint-scoped dossier for the exact upstream checkpoint esm2_t33_650M_UR50D. Primary evidence documents: (a) checkpoint name and files on the Hugging Face model page and repository blame (https://huggingface.co/facebook/esm2_t33_650M_UR50D and its README blame); (b) model configuration and architectural details (33 layers, hidden_size=1280, 20 attention heads, rotary position embeddings, max_position_embeddings=1026, dtype=float32) from the checkpoint config (https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json) and supporting repository code (https://github.com/facebookresearch/esm/blob/main/esm/model/esm2.py); (c) tokenizer class EsmTokenizer from tokenizer_config.json (https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/3241d90544423e7c0aa3d1171f61f7181680ee74/tokenizer_config.json); (d) training-data and benchmark reports in the original ESM-2 paper (https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf); (e) parameter scale and MIT license references from the NVIDIA Hugging Face packaging (https://huggingface.co/nvidia/esm2_t33_650M_UR50D) and Zenodo weights record (https://zenodo.org/records/7566741). Where primary sources do not specify a detail for this exact checkpoint (for example, an explicit pooling method to produce fixed-size sequence embeddings), the dossier records an explicit evidence gap. All evidence URLs are canonical first-party artifacts cited in sources.

## Identity

- Upstream name: Facebook ESM-2
- Checkpoint/version: esm2_t33_650M_UR50D
- Immutable revision: 08e4846e537177426273712802403f7ba8261b6c
- Parameter scale: 650M
- Architecture/head: EsmForMaskedLM (Transformer) — 33 layers, hidden_size=1280, num_attention_heads=20, rotary position embeddings, max_position_embeddings=1026, dtype=float32
- License: MIT
- Evidence: https://huggingface.co/facebook/esm2_t33_650M_UR50D, https://huggingface.co/facebook/esm2_t33_650M_UR50D/blame/08e4846e537177426273712802403f7ba8261b6c/README.md, https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json, https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/3241d90544423e7c0aa3d1171f61f7181680ee74/tokenizer_config.json, https://github.com/facebookresearch/esm/blob/master/esm/pretrained.py, https://huggingface.co/nvidia/esm2_t33_650M_UR50D, https://zenodo.org/records/7566741, https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf

## Selection

### Recommended

- **Produce per-residue and per-sequence protein sequence embeddings for downstream representation learning** — The checkpoint is an ESM-2 embedding model checkpoint producing embeddings for protein sequences as described on the Hugging Face checkpoint page and in the ESM-2 paper; embeddings are appropriate as input features for downstream protein tasks.
  Scope: esm2_t33_650M_UR50D (base embedding checkpoint)
  Evidence: https://huggingface.co/facebook/esm2_t33_650M_UR50D, https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- **Fine-tuning or adapter-based supervised learning using the checkpoint embeddings as input features** — The ESM-2 family and the checkpoint are presented in primary sources as models whose embeddings are usable for downstream tasks and fine-tuning; the checkpoint provides token-level embeddings suitable for downstream predictors.
  Scope: esm2_t33_650M_UR50D (base embedding checkpoint)
  Evidence: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf, https://huggingface.co/facebook/esm2_t33_650M_UR50D

### Conditional


### Avoid

- **Assuming the base embedding checkpoint alone performs structure prediction (end-to-end)** — Structure-prediction results reported in the ESM-2 paper (e.g., CASP/CAMEO TM-scores) depend on a downstream structure prediction pipeline/head (e.g., ESMFold) rather than solely the base embedding outputs; the base embedding checkpoint by itself is not shown in the primary sources to directly produce folded structures.
  Scope: esm2_t33_650M_UR50D (base embedding checkpoint)
  Evidence: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf

## Input preparation

### Semantic inputs

- Input modality is a single protein sequence provided as amino-acid letters (protein_sequence). Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D

### Accepted formats

- Model accepts protein sequences; the Hugging Face model page documents protein-sequence inputs for the checkpoint but does not prescribe a wrapped file format beyond sequence strings. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D

### Preprocessing

- Tokenization for the checkpoint is performed with the EsmTokenizer class as specified in tokenizer_config.json for this checkpoint. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/3241d90544423e7c0aa3d1171f61f7181680ee74/tokenizer_config.json
- Model configuration parameters (hidden_size=1280, num_hidden_layers=33, num_attention_heads=20, rotary position embeddings) are specified in the checkpoint config and repository code; preprocessing (tokenization) must produce token IDs consistent with that tokenizer. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json, https://github.com/facebookresearch/esm/blob/main/esm/model/esm2.py

### Pre-submit validation

- Maximum input length is governed by the model's max_position_embeddings value documented for this checkpoint (1026). Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json

### Task-specific formatting

- No explicit prompt templates or paired-input formats are specified for embedding generation in the checkpoint artifacts; inputs are plain protein-sequence strings. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D

## Output interpretation

### Outputs

- Per-token embeddings with dimensionality equal to the hidden size (1280) are produced for each input residue; dtype indicated as float32 in the checkpoint config. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json, https://huggingface.co/nvidia/esm2_t33_650M_UR50D

### Interpretation

- Embedding vectors are residue-level representations and may be pooled to form sequence-level representations; the checkpoint artifacts do not mandate a specific pooling strategy. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D, https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf

### Post-inference validation

- Outputs are float32 embeddings per the checkpoint config; downstream validation (task-specific calibration or normalization) is required for application-specific use. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json

## Public benchmarks

### Protein language modeling

- Dataset/split: Validation perplexity (Table S1) / validation
- Metric/value: perplexity / 6.95 (`lower-is-better`)
- Model scope: ESM-2 650M (33 layers, hidden_size=1280) as reported in paper Table S1 (upstream checkpoint results)
- Conditions: Reported in Table S1 of the ESM-2 paper (primary source); training on UniRef50 masked language modeling objective is noted in the paper.
- Source: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- Locator: Table S1
- Caveat: Table S1 in the paper reports model-family numeric benchmarks; ensure that any production-serving wrapper uses the identical checkpoint and evaluation protocol to reproduce these numbers.

### Protein structure-related evaluation (requires downstream structure-prediction head)

- Dataset/split: CASP14 / test
- Metric/value: TM-score / 0.51 (`higher-is-better`)
- Model scope: Reported result in paper Table S1 for ESM-2 650M when used in a structure-prediction pipeline (depends on downstream structure head/service)
- Conditions: Reported in Table S1 of the ESM-2 paper; structure outcomes rely on a structure-prediction head/pipeline (e.g., ESMFold) and are not produced solely by the base embedding checkpoint.
- Source: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- Locator: Table S1
- Caveat: Dependency on downstream structure-prediction head: the base embedding checkpoint alone does not directly produce folded structures; reproducing this metric requires the full structure prediction pipeline described in the paper.

### Protein structure-related evaluation (requires downstream structure-prediction head)

- Dataset/split: CAMEO (Apr–Jun 2022 test) / Apr–Jun 2022 test
- Metric/value: TM-score / 0.70 (`higher-is-better`)
- Model scope: Reported result in paper Table S1 for ESM-2 650M when used in a structure-prediction pipeline (depends on downstream structure head/service)
- Conditions: Reported in Table S1 of the ESM-2 paper; structure outcomes rely on a structure-prediction head/pipeline and are not produced solely by the base embedding checkpoint.
- Source: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- Locator: Table S1
- Caveat: Dependency on downstream structure-prediction head: the base embedding checkpoint alone does not directly produce folded structures; reproducing this metric requires the full structure prediction pipeline described in the paper.

## Comparisons

### biohub/ESMC-600M — `insufficient-evidence`

- Task: Protein embeddings / representation learning
- Criteria: Protocol-matched, dataset-matched comparison on the same metric and checkpoint
- Rationale: No primary-source protocol-level, checkpoint-matched comparison between the ESM-2 650M checkpoint and biohub/ESMC-600M is present in the inspected primary sources.
- Comparison conditions: Would require a primary-source evaluation reporting identical dataset, split, metric, and evaluation protocol for both checkpoints.
- Evidence: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf, https://huggingface.co/facebook/esm2_t33_650M_UR50D

### facebook/esm2_t36_3B_UR50D — `insufficient-evidence`

- Task: Protein embeddings / representation learning
- Criteria: Protocol-matched, dataset-matched comparison on the same metric and checkpoint
- Rationale: No primary-source protocol-level, checkpoint-matched comparison between the ESM-2 650M checkpoint and the 3B checkpoint is present in the inspected primary sources.
- Comparison conditions: Would require a primary-source evaluation reporting identical dataset, split, metric, and evaluation protocol for both checkpoints.
- Evidence: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf, https://huggingface.co/facebook/esm2_t33_650M_UR50D

## Limitations and safety

### Limitations

- Training data provenance: ESM-2 family training data is reported as UniRef50 in the primary paper; coverage and license-level details for all training sources are not exhaustively enumerated in the checkpoint artifacts inspected. Sources: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- Model-size transfer: results and benchmarks reported in the paper are for model-family checkpoints and may vary across parameter scales and downstream pipelines; reproducing reported numbers requires using the same checkpoint and evaluation pipeline. Sources: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- Evidence gap: the checkpoint artifacts and primary sources inspected do not specify a mandatory pooling/aggregation scheme for producing fixed-size sequence embeddings from per-token outputs; downstream users must select and validate pooling.
- Evidence gap: protocol-level details (exact dataset name/split) for the 'validation perplexity' row in Table S1 are not explicitly enumerated in the checkpoint artifacts inspected; reproducing the exact numeric comparison requires those details.
- Model input formatting beyond raw protein sequences (for example, explicit FASTA-wrapped API contract) is not specified in the checkpoint artifacts inspected. Sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D
- License distinction: model weights and code are indicated as MIT-licensed in packaging (Hugging Face / NVIDIA pages), while training-data licensing specifics are not exhaustively documented in the inspected checkpoint artifacts. Sources: https://huggingface.co/nvidia/esm2_t33_650M_UR50D, https://zenodo.org/records/7566741

### Safety

- Evidence gap: primary checkpoint artifacts inspected do not provide explicit clinical or PHI-handling guidance for downstream deployments of protein embeddings; expert review recommended for clinical or regulated applications.
- Upstream materials (NVIDIA packaging and build.nvidia modelcard) frame ESM-2 usage as embedding/representation models and note life-science usage considerations. Sources: https://build.nvidia.com/meta/esm2-650m/modelcard, https://docs.nvidia.com/bionemo-framework/1.10/models/esm2-nv.html

## Related upstream agent skills

### `agent-integration`

The cookbook maps these exact Forge slugs to BioNeMo-style capability names and Serverless shapes. Use it for routing and tool integration, never as model-quality evidence.
- [BioNeMo capability catalog](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/catalog.py)
- [BioNeMo named tool contracts](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/tools.py)
- [BioNeMo agent routing and safety instructions](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/configs/config.yml)

## Primary sources

### facebook/esm2_t33_650M_UR50D — Hugging Face model page

- URL: https://huggingface.co/facebook/esm2_t33_650M_UR50D
- Publisher: Facebook / Hugging Face
- Type: `model-card`
- Primary because: Canonical upstream model page for the exact checkpoint and packaging artifacts.
- Scope: esm2_t33_650M_UR50D
- Supports: Checkpoint name and hosting
- Supports: Model usage as a protein-sequence embedding checkpoint

### Hugging Face checkpoint config.json (main)

- URL: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json
- Publisher: Facebook / Hugging Face
- Type: `repository`
- Primary because: Official checkpoint configuration describing architecture, layer count, hidden size, heads, rotary embeddings, max positions, and dtype for this checkpoint.
- Scope: esm2_t33_650M_UR50D
- Supports: architecture class EsmForMaskedLM
- Supports: num_hidden_layers=33
- Supports: hidden_size=1280
- Supports: num_attention_heads=20
- Supports: rotary position embeddings
- Supports: max_position_embeddings=1026
- Supports: dtype=float32

### Hugging Face tokenizer_config.json (tokenizer_class EsmTokenizer) — blob/3241d905...

- URL: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/3241d90544423e7c0aa3d1171f61f7181680ee74/tokenizer_config.json
- Publisher: Facebook / Hugging Face
- Type: `repository`
- Primary because: Tokenizer configuration for this checkpoint indicating tokenizer class EsmTokenizer.
- Scope: esm2_t33_650M_UR50D
- Supports: tokenizer_class EsmTokenizer

### Hugging Face tokenizer_config.json (alternate blob reference)

- URL: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/218058a409fe1a3e95a01fd034790ef8a6622cb5/tokenizer_config.json
- Publisher: Facebook / Hugging Face
- Type: `repository`
- Primary because: Alternate blob path of tokenizer configuration present in checkpoint repository history; supports tokenizer identification for this checkpoint.
- Scope: esm2_t33_650M_UR50D
- Supports: tokenizer_class EsmTokenizer

### facebookresearch/esm — pretrained.py

- URL: https://github.com/facebookresearch/esm/blob/master/esm/pretrained.py
- Publisher: Facebook Research / GitHub
- Type: `repository`
- Primary because: Repository code referencing training data usage and checkpoint utilities for the ESM family.
- Scope: ESM family / checkpoint utilities
- Supports: Notes about training on UniRef50 (repository-level documentation references)

### facebookresearch/esm — esm2.py (model implementation)

- URL: https://github.com/facebookresearch/esm/blob/main/esm/model/esm2.py
- Publisher: Facebook Research / GitHub
- Type: `repository`
- Primary because: Primary repository source defining ESM2 class defaults (num_layers=33, embed_dim=1280, attention_heads=20) used by the family.
- Scope: ESM-2 family / implementation
- Supports: Default architectural parameters: num_layers=33, embed_dim=1280, attention_heads=20
- Supports: Implementation-level details referenced by checkpoint config

### ESM-2 paper (Lin et al., 2022) — bioRxiv

- URL: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf
- Publisher: bioRxiv
- Type: `paper`
- Primary because: Canonical scientific publication describing ESM-2 family training data, objectives, and reported benchmarks (Table S1).
- Scope: ESM-2 family benchmarks and training-data statements
- Supports: Training on UniRef50
- Supports: Table S1 benchmark numeric values (perplexity, TM-scores)
- Supports: Description of downstream structure-prediction pipeline usage for structure benchmarks

### Zenodo record for esm2_t33_650M_UR50D weights

- URL: https://zenodo.org/records/7566741
- Publisher: Zenodo
- Type: `official-documentation`
- Primary because: Canonical archival record for the checkpoint weights associated with this checkpoint packaging.
- Scope: esm2_t33_650M_UR50D
- Supports: Weights artifact and associated metadata

### Hugging Face packaging for NVIDIA esm2_t33_650M_UR50D

- URL: https://huggingface.co/nvidia/esm2_t33_650M_UR50D
- Publisher: NVIDIA / Hugging Face
- Type: `model-card`
- Primary because: Packaged checkpoint config and licensing metadata presented by NVIDIA's Hugging Face packaging for this checkpoint variant.
- Scope: esm2_t33_650M_UR50D (NVIDIA packaging)
- Supports: Parameter count ~650M
- Supports: MIT license statement for the packaged artifact
- Supports: Model hidden size and other config-level metadata consistent with checkpoint config

### NVIDIA BioNeMo ESM-2 documentation

- URL: https://docs.nvidia.com/bionemo-framework/1.10/models/esm2-nv.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA documentation summarizing ESM-2nv variants including the 650M configuration and deployment notes.
- Scope: ESM-2nv 650M packaged variant
- Supports: Statement of 33 layers / 20 attention heads / 650M parameters for the 650M variant
- Supports: Notes on packaging and deployment

### build.nvidia.com ESM2-650m modelcard

- URL: https://build.nvidia.com/meta/esm2-650m/modelcard
- Publisher: NVIDIA / build.nvidia.com
- Type: `official-documentation`
- Primary because: Model card and documentation provided by NVIDIA about ESM2-650m packaging and intended embedding outputs.
- Scope: ESM2-650m packaging and usage notes
- Supports: Description of embedding outputs and life-science usage considerations

### facebook/esm2_t33_650M_UR50D — Hugging Face model page — cited revision/file

- URL: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blame/08e4846e537177426273712802403f7ba8261b6c/README.md
- Publisher: Facebook / Hugging Face
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: esm2_t33_650M_UR50D
- Supports: Exact audited claim citation

## Evidence gaps

- Exact protocol-level dataset naming and split details for the 'validation perplexity' entry in Table S1 are not enumerated in the checkpoint artifacts inspected; the paper's Table S1 lacks a precise dataset-split locator in the inspected sources.
- Precise pooling/aggregation method to produce fixed-size sequence embeddings from per-token outputs is not specified in the checkpoint artifacts inspected.
- Primary-source, protocol-matched comparisons between esm2_t33_650M_UR50D and alternative checkpoints (for example, biohub/ESMC-600M or facebook/esm2_t36_3B_UR50D) are not present in the inspected sources; such comparisons would require identical evaluation datasets, splits, and metrics published for both checkpoints.
- Training-data license-level specifics for UniRef50 usage at scale are not exhaustively documented in the inspected checkpoint artifacts and primary paper.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 17 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/facebookresearch/esm/blob/master/esm/pretrained.py Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/218058a409fe1a3e95a01fd034790ef8a6622cb5/tokenizer_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/218058a409fe1a3e95a01fd034790ef8a6622cb5/tokenizer_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/biohub/ESMC-600M Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/facebookresearch/esm/blob/master/esm/pretrained.py Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/esm2-650m/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/esm2-650m/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/esm2-650m/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://huggingface.co/facebook/esm2_t33_650M_UR50D/blame/08e4846e537177426273712802403f7ba8261b6c/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
