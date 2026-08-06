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

- Research key: `huggingface-co-instadeepai-nucleotide-transformer-v2-500m-multi-species-d6a0a7b1d7`
- Independent audit: `revised`
- Researched: `2026-07-24T00:02:18.968844+00:00`

Primary upstream sources (Hugging Face model card and files, GitHub repository, and the canonical bioRxiv preprint versions) describe the NT‑v2 multispecies 500M model as an EsmForMaskedLM masked‑language transformer trained on multi‑species and human whole‑genome corpora, using 6‑mer tokenization where available, rotary positional embeddings, and a hidden size of 1024. The Hugging Face config.json for the published checkpoint records num_hidden_layers=29, num_attention_heads=16, intermediate_size=4096, position_embedding_type="rotary", and torch_dtype="float32". The tokenizer_config.json for the checkpoint lists tokenizer_class=EsmTokenizer and model_max_length (model_max_length / max_model_input_size) = 2048, and the vocab.txt contains 6‑mer tokens. The canonical paper and supplements report downstream evaluation results for NT‑Multispecies‑v2 500M (per-task MCCs in Supplementary Table 6 and mean MCC reported in figures), but multiple upstream documents differ in some reported aggregate numbers (see benchmarks) and the examined upstream files do not provide an explicit mapping from the Forge checkpoint id d6a0a7b1d7 to a concrete upstream weights file or immutable revision hash. Important operational details required for deployment or for a Forge I/O contract are not present in the examined upstream sources: an explicit model-weight license declaration (distinct from code/material licenses in the repository), an exact checkpoint-to‑Forge id mapping, explicit pooling/default embedding extraction procedure, formal I/O serialization names/JSON contract and numeric precision for embeddings, documented truncation/stride behavior for inputs exceeding model_max_length, and explicit reverse‑complement / paired‑input / IUPAC handling rules. Where family pages or sibling model cards report differing layer counts or max-length statements, the config.json for the 500M checkpoint is recorded but the discrepancy is documented as an evidence gap.

## Identity

- Upstream name: nucleotide-transformer-v2-500m-multi-species
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 500 million parameters
- Architecture/head: EsmForMaskedLM; config.json fields: hidden_size=1024, intermediate_size=4096, num_hidden_layers=29, num_attention_heads=16, position_embedding_type=rotary
- License: not reported
- Evidence: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/tokenizer_config.json, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/vocab.txt, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://github.com/instadeepai/nucleotide-transformer, https://github.com/instadeepai/nucleotide-transformer/blob/main/LICENSE.md

## Selection

### Recommended

- **Sequence representation extraction for downstream genomics tasks (embedding extraction / probing)** — Upstream README, the example notebook, and the paper describe extracting transformer representations for probing and downstream evaluation; the model is published as EsmForMaskedLM which exposes hidden states suitable for representation extraction.
  Scope: nucleotide-transformer-v2-500m-multi-species (EsmForMaskedLM checkpoint as published on Hugging Face)
  Evidence: https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/nucleotide_transformer_dna_sequence_modelling_with_peft.ipynb, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf
- **Fine‑tuning for regulatory and functional genomics prediction tasks (e.g., chromatin accessibility, promoter/enhancer prediction) using supervised heads** — The canonical paper reports fine‑tuning downstream evaluations across curated genomic prediction tasks and lists these categories as intended downstream applications for the family; authors fine‑tuned pre‑trained NT‑v2 models on task suites and reported MCCs.
  Scope: NT‑Multispecies‑v2 500M as reported in the paper (downstream results require a downstream fine‑tuning head and protocol)
  Evidence: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/nucleotide_transformer_dna_sequence_modelling_with_peft.ipynb

### Conditional

- **Task‑specific fine‑tuning for supervised genomics prediction** — Requires downstream labeled data and application of the paper's fine‑tuning protocol (authors report fine‑tuning on 18 curated tasks); results depend on downstream head architecture and fine‑tuning details.
  Scope: nucleotide-transformer-v2-500m-multi-species (pre‑trained checkpoint; downstream performance requires fine‑tuning as in the paper)
  Evidence: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species
- **Controllable sequence generation or sequence design (experimental)** — Repository-level claims and examples in the family repository indicate controllable generation is possible for the family, but explicit generation protocols, conditioning formats, and checkpoint‑scoped generation examples for the 500M multispecies checkpoint are not documented in the examined checkpoint files; downstream experimental validation is required.
  Scope: nucleotide-transformer family (generation capability described at repository level; not documented for the exact 500M checkpoint files examined)
  Evidence: https://github.com/instadeepai/nucleotide-transformer

### Avoid

- **Clinical diagnostic or direct clinical‑decision use without expert review** — Primary upstream sources (model card, README, and canonical paper) do not state the model is validated or approved for clinical use and provide no clinical certification, PHI handling instructions, or clinical deployment guidance for the checkpoint.
  Scope: nucleotide-transformer-v2-500m-multi-species
  Evidence: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf

## Input preparation

### Semantic inputs

- The model consumes DNA sequence strings (whole‑genome derived sequences) as semantic input. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://github.com/instadeepai/nucleotide-transformer
- Pretraining corpora described upstream include sequences from over 3,200 human genomes and 850 multispecies genomes (multi‑species). Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf

### Accepted formats

- Tokenization vocabulary contains 6‑mer tokens (vocab.txt file lists k‑mer token strings). Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/vocab.txt
- Tokenizer class declared for the checkpoint is EsmTokenizer (tokenizer_config.json). Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/tokenizer_config.json

### Preprocessing

- Upstream tokenizer and family documentation describe non‑overlapping 6‑mer tokenization where possible with fallback to single‑nucleotide tokens. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-250m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-100m-multi-species
- The tokenizer configuration for the 500M checkpoint sets model_max_length / max_model_input_size = 2048 (tokenizer_config.json). Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/tokenizer_config.json
- Pretraining used BERT‑style masking with a [MASK] token as described in the model README/family documentation. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-250m-multi-species

### Pre-submit validation

- Upstream sources do not provide an explicit pre‑submission validation checklist, input character‑set enforcement rules (IUPAC), reverse‑complement handling rules, or documented paired‑input behavior in the examined checkpoint files. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/tokenizer_config.json, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/vocab.txt

### Task-specific formatting

- Family examples document input formatting using a leading <CLS> token followed by tokenized k‑mer tokens; explicit, checkpoint‑scoped task prompt templates or paired‑input formats are not specified for the 500M checkpoint. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-250m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species
- The examined checkpoint files do not document explicit paired‑input ordering, control fields, or special prompt templates for downstream tasks. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://github.com/instadeepai/nucleotide-transformer

## Output interpretation

### Outputs

- Upstream model implementation is EsmForMaskedLM, indicating the model produces per‑token masked‑LM logits and exposes transformer hidden representations (hidden states) per token. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species
- Hidden representation dimensionality is given by hidden_size=1024 (config.json), corresponding to a 1024‑dimensional hidden vector per token layer. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json

### Interpretation

- Authors state that extracted representations can be probed or used after fine‑tuning for downstream evaluation; no official confidence calibration guidance or numeric embedding‑score semantics are provided in the examined upstream checkpoint documentation. Sources: https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/nucleotide_transformer_dna_sequence_modelling_with_peft.ipynb, https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf

### Post-inference validation

- Upstream sources recommend task‑specific fine‑tuning for downstream evaluation but do not provide universal post‑inference sanity checks, embedding normalization rules, default pooling, or an embedding serialization (JSON field name/shape/precision) contract in the examined files. Sources: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/main/README.md

## Public benchmarks

### Downstream genomic prediction (aggregated categories)

- Dataset/split: 18 curated genomic prediction tasks (as reported in paper; exact per‑task dataset names are in the paper/supplementary tables) / not reported
- Metric/value: Mean Matthews Correlation Coefficient (MCC) / 0.778 ± 0.012 (reported for NT‑Multispecies‑v2 500M in paper summary / supplementary references) (`higher-is-better`)
- Model scope: NT‑Multispecies‑v2 (500M) as reported in the paper (mapped to nucleotide-transformer-v2-500m-multi-species family)
- Conditions: Pre‑trained then fine‑tuned on 18 curated genomic prediction tasks; downstream results require fine‑tuning and the downstream head used by authors (see paper/supplements).
- Source: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf
- Locator: Main text and supplementary tables (Supplementary Table 6 referenced for per‑task MCCs)
- Caveat: The examined upstream materials show multiple reported aggregate/mean numbers across document versions (bioRxiv v3/v4) and family pages; exact per‑task rows are in Supplementary Table 6 and mapping to the exact Forge checkpoint id d6a0a7b1d7 is not provided by upstream sources.
- Caveat: Reported mean MCC values depend on downstream fine‑tuning protocol and are not produced by a callable base embedding output alone; authors fine‑tuned models prior to evaluation.

### Downstream genomic prediction (per‑task entries reported in Supplementary Table 6)

- Dataset/split: Supplementary Table 6 (paper/supplementary materials) / not reported
- Metric/value: Matthews Correlation Coefficient (MCC) per downstream task / Per‑task MCC values reported in Supplementary Table 6 for NT‑Multispecies‑v2 (500M) (example entries reported in the upstream supplement). (`higher-is-better`)
- Model scope: NT‑Multispecies‑v2 (500M) per the paper supplement
- Conditions: Fine‑tuning on curated downstream tasks as described in the paper; exact seed/split/hardware details are described in supplementary materials but not reproduced here.
- Source: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf
- Locator: Supplementary Table 6
- Caveat: The Research Findings include per‑task MCC rows in Supplementary Table 6 but mapping from each numerical row to a specific checkpoint revision or to the Forge id d6a0a7b1d7 is not provided in the examined upstream files.
- Caveat: An updated figure in a later upstream document (bioRxiv v4, Figure 5) reports a different reported mean MCC (0.762) for NT‑Multispecies‑v2 (500M), indicating versioned document differences that create ambiguity in aggregate reporting.

## Comparisons

### HuggingFaceBio/Carbon-3B — `insufficient-evidence`

- Task: Downstream genomic prediction (family‑reported tasks)
- Criteria: No direct primary‑source, protocol‑matched benchmark comparisons between the exact NT‑Multispecies‑v2 500M checkpoint and the listed alternative under identical evaluation conditions were found in the examined upstream materials.
- Rationale: The canonical paper and model card report NT family benchmarks but do not present direct task‑and‑protocol matched comparisons to the listed Forge alternatives within the same primary sources.
- Comparison conditions: Direct comparisons would require identical datasets/splits, fine‑tuning protocols, seeds and hardware; these were not jointly reported for the alternatives in the examined upstream sources.
- Evidence: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species

### LongSafari/hyenadna-medium-450k — `insufficient-evidence`

- Task: Downstream genomic prediction (family‑reported tasks)
- Criteria: No primary‑source evidence of protocol‑matched comparisons.
- Rationale: Examined primary sources for NT‑v2 do not include direct, protocol‑matched benchmarking against this alternative.
- Comparison conditions: Missing joint, primary‑source benchmarks under identical protocols.
- Evidence: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species

### zhihan1996/DNABERT-2-117M — `insufficient-evidence`

- Task: Downstream genomic prediction (family‑reported tasks)
- Criteria: No primary‑source evidence of protocol‑matched comparisons.
- Rationale: The NT paper and model card do not present direct comparisons with the listed alternative under identical evaluation conditions in the examined sources.
- Comparison conditions: Direct comparison requires identical dataset/split and fine‑tuning protocols which are not jointly reported.
- Evidence: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species

## Limitations and safety

### Limitations

- Upstream files do not provide an explicit mapping from the Forge checkpoint id d6a0a7b1d7 to a concrete upstream weights file name, immutable revision hash, or exact revision metadata. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json
- An explicit model‑weight license declaration covering the checkpoint weights is not present in the examined upstream model card or checkpoint files; repository-level LICENSE.md lists Apache‑2.0 for code and CC BY‑NC‑SA 4.0 for repository material but does not explicitly state a model‑weights license binding for the published Hugging Face checkpoint. Sources: https://github.com/instadeepai/nucleotide-transformer/blob/main/LICENSE.md, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species
- There is an architectural/metadata inconsistency across upstream materials: the checkpoint config.json for the 500M model lists num_hidden_layers=29 while some family pages and examples reference different layer counts for certain 500M variants; upstream documents do not reconcile this discrepancy. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json, https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/nucleotide_transformer_dna_sequence_modelling_with_peft.ipynb
- Upstream sources do not document a default pooling or embedding‑extraction method (CLS pooling, mean pooling, or specific layer selection) for producing sequence‑level embeddings from per‑token hidden states. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/main/README.md
- Upstream checkpoint files do not specify an I/O serialization contract (JSON field names, embedding array key names, or numeric precision for returned embeddings) usable as a Forge API contract. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json, https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/tokenizer_config.json

### Safety

- Evidence gap: The examined upstream sources do not include an explicit safety policy, clinical‑use disclaimers, PHI‑handling instructions, or dual‑use/biosecurity mitigation guidance for this checkpoint. Sources: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species, https://github.com/instadeepai/nucleotide-transformer, https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: InstaDeepAI/nucleotide-transformer-v2-500m-multi-species

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species
- Publisher: InstaDeep / Hugging Face model card
- Type: `model-card`
- Primary because: Official Hugging Face model card for the checkpoint family; contains README and links to config/tokenizer/vocab files and high‑level statements about pretraining corpora and intended tasks.
- Scope: nucleotide-transformer-v2-500m-multi-species (model card and README)
- Supports: Model family description
- Supports: Training‑corpus statements (multi‑species, number of genomes)
- Supports: High‑level intended uses
- Supports: Links to checkpoint files

### Model config (config.json) for nucleotide-transformer-v2-500m-multi-species

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/config.json
- Publisher: Hugging Face (host of upstream config file)
- Type: `model-card`
- Primary because: Canonical model configuration file for the checkpoint; contains concrete architecture fields observed for the published checkpoint.
- Scope: Exact config of the published checkpoint (config.json)
- Supports: Architecture name (EsmForMaskedLM)
- Supports: hidden_size=1024, intermediate_size=4096, num_hidden_layers=29, num_attention_heads=16
- Supports: position_embedding_type=rotary
- Supports: torch_dtype=float32

### Tokenizer configuration (tokenizer_config.json) for nucleotide-transformer-v2-500m-multi-species

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/f1fd7a1df5b19d31b88f11db1ce87caeb1ea4d2a/tokenizer_config.json
- Publisher: Hugging Face (host of tokenizer config)
- Type: `model-card`
- Primary because: Canonical tokenizer configuration for the checkpoint; reports tokenizer class and model_max_length.
- Scope: Tokenizer config for the 500M checkpoint
- Supports: tokenizer_class=EsmTokenizer
- Supports: model_max_length=2048
- Supports: clean_up_tokenization_spaces=true

### Vocab file (vocab.txt) for nucleotide-transformer-v2-500m-multi-species

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/ac4ca3ca409bec56db5664401f9a7ca701ee7ae7/vocab.txt
- Publisher: Hugging Face (host of vocab file)
- Type: `model-card`
- Primary because: Vocabulary file listing token strings used by the tokenizer; provides direct evidence of k‑mer tokens.
- Scope: Vocab for the 500M checkpoint
- Supports: Presence of 6‑mer tokens in vocabulary

### Model README (README.md) hosted on Hugging Face model page

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/main/README.md
- Publisher: InstaDeep / Hugging Face (model README)
- Type: `model-card`
- Primary because: Model README contains training setup details and high‑level architecture/training claims (training tokens, sequence length used during training, hardware statements).
- Scope: README for nucleotide-transformer-v2-500m-multi-species
- Supports: Training corpus descriptions and training tokens
- Supports: High‑level training/hardware details
- Supports: Intended use descriptions

### GitHub repository: instadeepai/nucleotide-transformer

- URL: https://github.com/instadeepai/nucleotide-transformer
- Publisher: InstaDeep (repository)
- Type: `repository`
- Primary because: Official code and repository maintained by the model authors; contains implementation notes, examples, and LICENSE file.
- Scope: Nucleotide Transformer family repository
- Supports: Repository examples and capability claims
- Supports: LICENSE file for repository material and code

### Repository license file (LICENSE.md) for the nucleotide-transformer repository

- URL: https://github.com/instadeepai/nucleotide-transformer/blob/main/LICENSE.md
- Publisher: InstaDeep (repository)
- Type: `repository`
- Primary because: Repository license file listing code and material licenses present in the repository; used to assess but not to assume an explicit model‑weights license.
- Scope: Repository license declarations
- Supports: Apache License 2.0 declared for code
- Supports: Creative Commons Attribution‑NonCommercial‑ShareAlike 4.0 declared for repository material

### bioRxiv / paper PDF: The Nucleotide Transformer (preprint, v3)

- URL: https://biorxiv.org/content/10.1101/2023.01.11.523679v3.full.pdf
- Publisher: bioRxiv (preprint)
- Type: `paper`
- Primary because: Original research preprint describing Nucleotide Transformer family experiments, datasets, and reported downstream metrics and supplementary tables.
- Scope: NT family experiments and reported metrics (paper text and supplementary materials, v3)
- Supports: Reported downstream evaluation (per‑task MCCs in Supplementary Table 6)
- Supports: Descriptions of pretraining corpora and model variants

### bioRxiv / paper PDF: The Nucleotide Transformer (preprint, v4 / alternate figure reporting)

- URL: https://biorxiv.org/content/10.1101/2023.01.11.523679v4.full.pdf
- Publisher: bioRxiv (preprint)
- Type: `paper`
- Primary because: Alternate/updated preprint PDF containing figures and reported aggregate metrics; used to document versioned differences in reported mean MCCs.
- Scope: NT family experiments and reported metrics (paper text and figures, v4)
- Supports: Figure 5 reported mean MCC values for NT‑Multispecies‑v2 (500M) and other variants

### Hugging Face example Colab notebook referencing Nucleotide Transformer family

- URL: https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/nucleotide_transformer_dna_sequence_modelling_with_peft.ipynb
- Publisher: Hugging Face / example notebook
- Type: `official-documentation`
- Primary because: Official example notebook that demonstrates representation extraction and fine‑tuning usage patterns for the family.
- Scope: Example usage for Nucleotide Transformer family
- Supports: Representation extraction / fine‑tuning examples
- Supports: Usage patterns consistent with model card and paper

### Hugging Face model card: InstaDeepAI/nucleotide-transformer-v2-250m-multi-species (family reference)

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-250m-multi-species
- Publisher: InstaDeep / Hugging Face
- Type: `model-card`
- Primary because: Sibling model card used in the examined materials to corroborate family tokenizer and input formatting claims.
- Scope: nucleotide-transformer-v2 family (250M variant reference)
- Supports: 6‑mer tokenization descriptions and input formatting examples used across v2 family

### Hugging Face model card: InstaDeepAI/nucleotide-transformer-v2-100m-multi-species (family reference)

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-100m-multi-species
- Publisher: InstaDeep / Hugging Face
- Type: `model-card`
- Primary because: Sibling model card documenting family tokenization and training procedure claims.
- Scope: nucleotide-transformer-v2 family (100M variant reference)
- Supports: Family tokenization and training procedure claims

### Hugging Face model card: InstaDeepAI/nucleotide-transformer-v2-50m-3mer-multi-species (family reference)

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-50m-3mer-multi-species
- Publisher: InstaDeep / Hugging Face
- Type: `model-card`
- Primary because: Additional family model card documenting tokenization examples and family practices.
- Scope: nucleotide-transformer-v2 family (50M variant reference)
- Supports: Family tokenization and training procedure claims

### Model file: esm_config.py (model file hosted with the checkpoint)

- URL: https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-500m-multi-species/blob/main/esm_config.py
- Publisher: Hugging Face (host)
- Type: `model-card`
- Primary because: Model configuration helper file bundled with checkpoint files that documents default ESM configuration parameters used by the family.
- Scope: esm_config.py contents for the checkpoint family
- Supports: ESM configuration parameters and default vocab tokens in the checkpoint bundle

## Evidence gaps

- Exact upstream checkpoint identifier mapping: No examined upstream file or model card provides a concrete mapping from the Forge checkpoint id d6a0a7b1d7 to an immutable upstream weights file name or file‑hash; checkpoint/revision is not reported in the examined sources.
- Exact model‑weight license: The repository LICENSE.md lists Apache‑2.0 for code and CC BY‑NC‑SA 4.0 for repository material, but the examined Hugging Face model card and checkpoint files do not explicitly declare a model‑weights license; an explicit model‑weight license statement is not reported.
- I/O serialization contract: The examined upstream files do not specify exact API/JSON field names, embedding array key names, or numeric precision for embedding serialization; this is not reported in the model card, config, tokenizer, or paper.
- Pooling/default embedding extraction: No upstream documentation specifies a default pooling strategy (CLS pooling, mean pooling, specified layer) for producing sequence‑level embeddings from per‑token hidden states for this checkpoint.
- Tokenizer max‑length inconsistency: tokenizer_config.json for the 500M checkpoint lists model_max_length=2048, while some family pages and examples reference other maximum token lengths for family variants; no authoritative file reconciles this inconsistency for the exact 500M checkpoint.
- Truncation / stride behavior for sequences longer than max length: Upstream tokenizer config and README do not document explicit truncation, cropping, or stride behavior for inputs exceeding model_max_length for this checkpoint.
- Reverse‑complement handling and paired‑input support: No explicit rules for reverse‑complement handling, paired‑input formats, or IUPAC ambiguity code handling are documented for the checkpoint files examined.
- Exact numerical benchmark provenance for every reported aggregated metric: While per‑task rows appear in Supplementary Table 6 and aggregated numbers appear in paper figures, mapping of every numeric entry to a specific checkpoint revision or the Forge id d6a0a7b1d7 is not provided; updated preprint versions contain differing reported aggregates, creating an ambiguity.
- Protocol‑matched comparisons to listed Forge alternatives: No primary‑source, protocol‑matched direct comparisons between this exact checkpoint and the listed Forge alternatives were found in the examined upstream materials.
- Runtime / serving contract: Upstream sources do not document a Forge/NIM/runtime API contract (JSON field names, default batching, numeric precision, latency/memory footprints) for this checkpoint; these are not present in the examined model card, config, tokenizer, or paper.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
