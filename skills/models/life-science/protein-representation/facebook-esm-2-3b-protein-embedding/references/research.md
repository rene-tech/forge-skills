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

- Research key: `huggingface-co-facebook-esm2-t36-3b-ur50d-3487164212`
- Independent audit: `revised`
- Researched: `2026-08-06T12:21:50.080434+00:00`

The provided primary findings identify facebook/esm2_t36_3B_UR50D as an ESM-2 masked-language-model checkpoint for protein sequences with 36 transformer layers and approximately 3 billion parameters. Checkpoint-scoped configuration evidence verifies the exact architecture class and key configuration fields. The verified scope supports protein-sequence input and upstream masked-language-model / representation-learning use, but the findings do not provide exact checkpoint-scoped extraction API details such as canonical pooling defaults, embedding dimensionality as an output contract, normalization guidance, explicit amino-acid OOV policy, or exact checkpoint-matched public benchmark rows for this served embedding scope. Code license is MIT at the repository level, while a distinct model-weights license is not reported in the provided findings.

## Identity

- Upstream name: facebook/esm2_t36_3B_UR50D
- Checkpoint/version: esm2_t36_3B_UR50D
- Immutable revision: Repository tree snapshot revision identifier ef01d4581c13eb61ca735776967e7560e0c6a248 is reported for the checkpoint tree; config.json blob revision e465bb8d75fb881450cacab2f1ccc14585e00ac5 is reported for the configuration file.
- Parameter scale: approximately 3 billion parameters
- Architecture/head: EsmForMaskedLM with model type "esm"; 36 transformer layers are reported for this checkpoint. The config reports hidden size 2560, intermediate size 10240, 40 attention heads per layer, maximum position embeddings 1026, rotary position embeddings, GELU activation, pad token ID 1, mask token ID 32, and is_folding_model false.
- License: Code license: MIT License for the facebookresearch/esm repository. Model-weights license: not reported in the provided primary findings for this exact checkpoint.
- Evidence: https://huggingface.co/facebook/esm2_t36_3B_UR50D, https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/README.md, https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json, https://github.com/facebookresearch/esm/blob/main/LICENSE, https://huggingface.co/facebook/esm2_t36_3B_UR50D/tree/ef01d4581c13eb61ca735776967e7560e0c6a248

## Selection

### Recommended

- **Protein sequence representation learning and embedding-based downstream analysis** — The Hugging Face model page states that ESM-2 is a state-of-the-art protein model trained on a masked language modeling objective, which directly supports use of this checkpoint as a pretrained protein-sequence representation model. The expected Forge scope is an embedding endpoint, and this recommendation is limited to embedding-style use rather than unsupported downstream heads.
  Scope: facebook/esm2_t36_3B_UR50D upstream checkpoint, used as a protein-sequence embedding model within the Forge variants facebook-esm-2-3b and facebook-esm-2-3b-protein-embedding
  Evidence: https://huggingface.co/facebook/esm2_t36_3B_UR50D

### Conditional

- **Downstream supervised classification or regression on protein sequences using checkpoint-derived representations** — Requires downstream task-specific model design, training, and validation. The provided findings verify masked-language-model pretraining and checkpoint architecture, but they do not provide checkpoint-scoped downstream validation protocols or calibrated performance guarantees for a specific supervised task.
  Scope: facebook/esm2_t36_3B_UR50D representations used as features in downstream models outside the base checkpoint
  Evidence: https://huggingface.co/facebook/esm2_t36_3B_UR50D, https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/README.md

### Avoid

- **Use as a validated clinical decision-support system or as a standalone basis for regulated medical decisions** — The provided primary findings identify this checkpoint as a protein masked-language model and do not report any clinical validation, regulatory status, or medical decision-support authorization for this exact checkpoint.
  Scope: facebook/esm2_t36_3B_UR50D and Forge embedding variants derived from this upstream checkpoint
  Evidence: https://huggingface.co/facebook/esm2_t36_3B_UR50D

## Input preparation

### Semantic inputs

- The model consumes protein sequences as input. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D

### Accepted formats

- Accepted upstream format is tokenized input handled by EsmTokenizer; the tokenizer configuration names the tokenizer class as "EsmTokenizer". Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/tokenizer_config.json

### Preprocessing

- Inputs are prepared through the EsmTokenizer tokenizer workflow for this checkpoint family. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/tokenizer_config.json

### Pre-submit validation

- The configuration reports maximum position embeddings of 1026, so sequence preparation must respect that configured positional limit unless an external workflow explicitly handles longer inputs. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json
- Evidence gap: the provided primary findings do not publish an exact checkpoint-scoped official amino-acid alphabet and out-of-vocabulary handling policy for facebook/esm2_t36_3B_UR50D itself.

### Task-specific formatting

- No prompt template is reported in the provided findings; the verified scope is protein-sequence tokenization for an EsmForMaskedLM checkpoint rather than chat or instruction formatting. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json, https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/tokenizer_config.json

## Output interpretation

### Outputs

- The checkpoint architecture is "EsmForMaskedLM", so the directly verified upstream task head is a masked-language-model head rather than a separately documented structure head or classifier head. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json
- Evidence gap: the provided primary findings do not give an exact official output contract for Forge-served embedding objects from this checkpoint, including whether outputs are per-token, pooled, normalized, or which pooling option is default.

### Interpretation

- Interpret outputs conservatively as representations from a pretrained protein masked-language model; the provided findings do not establish that any single embedding directly equals a biological or clinical ground truth without downstream validation. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D

### Post-inference validation

- Post-inference downstream validation is required before relying on representations for a specific biological prediction task, because the provided findings do not report checkpoint-scoped calibration, confidence scores, or task-specific acceptance criteria. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D
- Evidence gap: the provided primary findings do not specify checkpoint-scoped normalization requirements, pooled-embedding defaults, or output dimensionality as an official embedding-output contract for this exact served scope.

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The verified upstream task is masked language modeling on protein sequences; the provided findings do not establish checkpoint-scoped validation for specific downstream scientific or clinical tasks. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D, https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json
- A distinct model-weights license for this exact checkpoint is not reported in the provided primary findings; only the repository code license is verified. Sources: https://github.com/facebookresearch/esm/blob/main/LICENSE, https://huggingface.co/facebook/esm2_t36_3B_UR50D
- The provided primary findings do not supply an exact checkpoint-matched public benchmark row for facebook/esm2_t36_3B_UR50D with dataset, split, metric, and conditions that can be safely attributed to this Forge embedding scope. Sources: https://huggingface.co/facebook/esm2_t36_3B_UR50D, https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text

### Safety

- Forge policy: do not use this checkpoint as a standalone clinical decision tool or as a substitute for expert biological or medical review.
- Forge policy: treat any proprietary, sensitive, or regulated sequence data with separate organizational data-governance controls, because the provided primary findings do not state checkpoint-specific privacy or PHI handling guarantees.
- Evidence gap: the provided primary findings do not report explicit upstream safety, privacy, PHI, or regulated-use guidance for this exact checkpoint.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model page for facebook/esm2_t36_3B_UR50D

- URL: https://huggingface.co/facebook/esm2_t36_3B_UR50D
- Publisher: Hugging Face / Meta FAIR checkpoint page
- Type: `model-card`
- Primary because: Primary checkpoint page for the exact Hugging Face model identifier named in the brief.
- Scope: Exact checkpoint facebook/esm2_t36_3B_UR50D
- Supports: checkpoint identity
- Supports: upstream task description
- Supports: recommended use scope
- Supports: avoid-use boundary
- Supports: interpretation and validation limits

### README.md for facebook/esm2_t36_3B_UR50D

- URL: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/README.md
- Publisher: Hugging Face / Meta FAIR checkpoint repository
- Type: `model-card`
- Primary because: Primary checkpoint repository file reporting exact layer count and parameter scale for this model.
- Scope: Exact checkpoint facebook/esm2_t36_3B_UR50D
- Supports: checkpoint name
- Supports: layer count
- Supports: parameter scale
- Supports: conditional downstream-use scoping

### config.json for facebook/esm2_t36_3B_UR50D at blob revision e465bb8d75fb881450cacab2f1ccc14585e00ac5

- URL: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json
- Publisher: Hugging Face / Meta FAIR checkpoint repository
- Type: `repository`
- Primary because: Primary exact-file configuration source for architecture class and checkpoint configuration fields.
- Scope: Exact checkpoint config for facebook/esm2_t36_3B_UR50D
- Supports: architecture
- Supports: model type
- Supports: hidden size
- Supports: intermediate size
- Supports: attention heads
- Supports: maximum position embeddings
- Supports: rotary position embedding
- Supports: pad and mask token IDs
- Supports: activation
- Supports: dropout
- Supports: is_folding_model
- Supports: config blob revision

### LICENSE for facebookresearch/esm

- URL: https://github.com/facebookresearch/esm/blob/main/LICENSE
- Publisher: facebookresearch / Meta
- Type: `repository`
- Primary because: Primary repository license file establishing the verified code license.
- Scope: facebookresearch/esm repository code
- Supports: code license
- Supports: license distinction limitation

### Repository tree snapshot for facebook/esm2_t36_3B_UR50D at revision ef01d4581c13eb61ca735776967e7560e0c6a248

- URL: https://huggingface.co/facebook/esm2_t36_3B_UR50D/tree/ef01d4581c13eb61ca735776967e7560e0c6a248
- Publisher: Hugging Face / Meta FAIR checkpoint repository
- Type: `repository`
- Primary because: Primary repository tree snapshot giving a reported revision identifier for the exact checkpoint repository state.
- Scope: Exact checkpoint repository snapshot for facebook/esm2_t36_3B_UR50D
- Supports: checkpoint repository revision evidence

### tokenizer_config.json for facebook/esm2_t36_3B_UR50D

- URL: https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/tokenizer_config.json
- Publisher: Hugging Face / Meta FAIR checkpoint repository
- Type: `repository`
- Primary because: Primary tokenizer configuration file for the exact checkpoint repository.
- Scope: Tokenizer configuration for facebook/esm2_t36_3B_UR50D
- Supports: accepted tokenizer class
- Supports: input format
- Supports: preprocessing scope

### bioRxiv full text for ESM-2 study

- URL: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text
- Publisher: bioRxiv / original authors
- Type: `paper`
- Primary because: Primary original paper source for family-level architectural and evaluation context checked for exact-checkpoint benchmark evidence.
- Scope: ESM-2 family paper used only for scoped family context and benchmark-evidence checking
- Supports: family context on rotary position embeddings
- Supports: benchmark evidence-gap check for exact checkpoint attribution

## Evidence gaps

- The provided primary findings do not report a distinct model-weights license for facebook/esm2_t36_3B_UR50D; only the repository code license is verified at https://github.com/facebookresearch/esm/blob/main/LICENSE.
- The provided primary findings do not publish an exact checkpoint-scoped official amino-acid alphabet and explicit OOV policy for facebook/esm2_t36_3B_UR50D.
- The provided primary findings do not specify an exact official Forge embedding output contract for this checkpoint, including pooled-vs-per-token behavior, default pooling choice, normalization, or output dimensionality.
- Benchmark evidence gap: checked https://huggingface.co/facebook/esm2_t36_3B_UR50D (model page), https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/main/README.md (README), and https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text (paper full text, including the findings-reported references to Table 1 and Table S3), but the provided findings do not give an exact verifiable benchmark row for facebook/esm2_t36_3B_UR50D with dataset, split, metric, value, and evaluation conditions attributable to this Forge embedding scope.
- Comparison evidence gap: the provided primary findings do not supply task-matched, protocol-matched primary evidence for this exact checkpoint and a named alternative sufficient to support a non-empty comparisons section without over-transferring family-level claims.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 15 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[2].direction: $.benchmarks[2].direction: 'higher-is-better for accuracy; lower-is-better for RMSE' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19] describes itself as secondary evidence: $.sources[19] describes itself as secondary evidence Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
