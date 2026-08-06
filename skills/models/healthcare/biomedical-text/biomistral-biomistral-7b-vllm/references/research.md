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

- Research key: `huggingface-co-biomistral-biomistral-7b-63b81ae75b`
- Independent audit: `revised`
- Researched: `2026-07-24T00:06:31.855036+00:00`

BioMistral-7B is a Mistral-derived decoder-only causal language model further pre-trained for medical/biomedical-domain research. The Hugging Face model pages and inspected variant config blobs identify the architecture as MistralForCausalLM and report hyperparameters including hidden_size=4096, 32 hidden layers, 32 attention heads, vocab_size=32000, max_position_embeddings=32768, sliding_window=4096, and torch_dtype bfloat16. The project publishes merged variants (DARE, TIES, SLERP) and quantized builds (e.g., BnB.8). The peer-reviewed preprint (arXiv:2402.10373) provides evaluation tables (including the Prompt 1 QA prompt table) reporting per-domain QA scores for BioMistral-7B and reports reported gains for merged strategies (DARE, TIES, SLERP). The BioMistral BnB.8 model page reports a set of medical benchmark numeric results. The inspected canonical files and model pages do not publish a creator-declared model-weights or code license, do not state an explicit parameter count, and do not publish creator-provided PHI-handling or clinical-deployment certification (evidence gaps listed below).

## Identity

- Upstream name: BioMistral-7B
- Checkpoint/version: BioMistral-7B (base; published merged variants: DARE, TIES, SLERP; quantized build: BnB.8)
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: MistralForCausalLM (decoder-only causal LM; config blobs report hidden_size=4096, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads=8, vocab_size=32000, max_position_embeddings=32768, sliding_window=4096, torch_dtype=bfloat16)
- License: not reported
- Evidence: https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json, https://huggingface.co/BioMistral/BioMistral-7B-DARE/blob/347e1b5e56590ddfc22e4ee15a2f648ea87a20a8/config.json, https://huggingface.co/BioMistral/BioMistral-7B-SLERP/blame/ea6b3ceb95b5e0a8e004c93c75a43fcb3935d882/config.json, https://huggingface.co/BioMistral/BioMistral-7B

## Selection

### Recommended

- **Biomedical question-answering and domain-specific QA evaluation (research/evaluation use only)** — The project model pages and the arXiv preprint present BioMistral-7B and its merged variants as further-pretrained models targeted at medical/biomedical domains and publish SFT/evaluation numeric results for domain QA prompts and medical benchmarks.
  Scope: BioMistral-7B base checkpoint and published merged variants (DARE, TIES, SLERP); quantized build BnB.8 when the reported benchmarks on that variant are cited explicitly.
  Evidence: https://arxiv.org/pdf/2402.10373, https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8, https://huggingface.co/BioMistral/BioMistral-7B-DARE

### Conditional

- **Claiming improved SFT or ensemble performance when using merged checkpoints/ensembles** — Only when using the explicitly published merged checkpoints or ensemble artifacts (DARE, TIES, SLERP) and reproducing the exact evaluation protocol reported in the inspected evaluation tables (e.g., reproduce the Prompt 1 QA prompt as shown in the paper's evaluation table). Improvements reported are tied to the merged-variant artifacts and the paper's evaluation protocol.
  Scope: BioMistral-7B merged variants DARE, TIES, SLERP and BioMistral-7B ensemble artifacts as documented in the project materials and the arXiv preprint.
  Evidence: https://arxiv.org/pdf/2402.10373, https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://huggingface.co/BioMistral/BioMistral-7B-SLERP

### Avoid

- **Direct deployment for clinical care or production medical decision-making** — Evidence gap: the inspected canonical repository/model-page materials and inspected config/tokenizer files do not publish a creator-provided clinical-use certification, PHI-handling guidance, or deployment safety certification; the model is presented and evaluated in a research/evaluation context.
  Scope: BioMistral-7B (base and published variants DARE, TIES, SLERP; BnB.8 quantized build)
  Evidence: https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8

## Input preparation

### Semantic inputs

- Primary accepted input modality is text; model pages and variant descriptions present biomedical/medical textual inputs and QA prompts as the model's evaluation targets. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8

### Accepted formats

- Text prompt strings intended for causal-LM-style prompts and instruction-wrapped chat messages used in the project's evaluation and examples. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://arxiv.org/pdf/2402.10373

### Preprocessing

- Tokenizer configuration for the BnB.8 variant documents special tokens and BOS/EOS handling (add_bos_token true, add_eos_token false) and lists added_tokens_decoder entries; vocabulary size is reported in config blobs. Sources: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/blob/main/tokenizer_config.json, https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json
- The canonical tokenizer/config blobs inspected do not specify the underlying tokenization algorithm (e.g., BPE, SentencePiece, unigram) or provide merges/vocab text files at the inspected locators (Evidence gap). Sources: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/blob/main/tokenizer_config.json, https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json
- The inspected config blobs report vocab_size = 32000 in the checkpoint configuration. Sources: https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json

### Pre-submit validation

- Evidence gap: no explicit upstream input-validation schema (character encodings, JSON field names, maximum input token policy, or runtime truncation contract) was found in the inspected config/tokenizer/repository materials. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/blob/main/tokenizer_config.json

### Task-specific formatting

- The project's model pages and the arXiv preprint present evaluation prompts and instruction-style wrappers in the examples and tables; use the exact prompt format shown in the inspected evaluation materials when reproducing reported results. Sources: https://arxiv.org/pdf/2402.10373, https://huggingface.co/BioMistral/BioMistral-7B-DARE

## Output interpretation

### Outputs

- Checkpoint is a decoder-only causal language model producing textual continuations; config blobs identify the architecture as MistralForCausalLM. Sources: https://huggingface.co/BioMistral/BioMistral-7B-DARE/blob/347e1b5e56590ddfc22e4ee15a2f648ea87a20a8/config.json, https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json

### Interpretation

- Outputs reported in the paper and on model pages are natural-language continuations used to compute SFT/benchmark accuracies in the inspected evaluation tables; no creator-published calibration semantics (logit-to-probability transforms or formal confidence thresholds) were found in the inspected sources. Sources: https://arxiv.org/pdf/2402.10373, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8

### Post-inference validation

- Evidence gap: no creator-provided post-inference calibration guidance, per-token score interpretation semantics, or formal API response schema was found in the inspected repository/model-page files and associated config/tokenizer blobs. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://arxiv.org/pdf/2402.10373

## Public benchmarks

### Biomedical QA (Prompt 1 QA prompt)

- Dataset/split: Prompt 1 (Health, Nutrition, Psychology, Science) / not reported
- Metric/value: score (unspecified metric definition in inspected source) / Health 72.7; Nutrition 68.8; Psychology 31.6; Science 33.3; average 51.6 (`higher-is-better`)
- Model scope: BioMistral-7B (reported in the project's evaluation tables in the arXiv preprint)
- Conditions: Reported under 'Prompt 1 QA prompt' in the arXiv evaluation table; the inspected PDF does not publish additional split or full metric-formula details at that table locator.
- Source: https://arxiv.org/pdf/2402.10373
- Locator: Table 2 (Prompt 1 QA prompt few-shot accuracy table) in the arXiv PDF
- Caveat: The inspected table does not publish explicit dataset split names or the formal metric-definition at the inspected locator; mapping of numeric columns to fully specified benchmark names/splits/metric formulas is not available at the inspected table.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: Clinical KG / not reported
- Metric/value: score (unspecified metric definition in inspected source) / 59.9 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page for the BnB.8 quantized build)
- Conditions: Reported as part of the medical benchmark table on the BnB.8 model page; the inspected model-card table does not publish dataset split or exact metric-definition at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: The inspected model-page entry does not publish dataset split or the formal metric-definition at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: Medical Genetics / not reported
- Metric/value: score (unspecified) / 64.0 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table without further split/metric-definition details at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not available at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: Anatomy / not reported
- Metric/value: score (unspecified) / 56.5 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table without further split/metric-definition details at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not provided at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: Pro Medicine / not reported
- Metric/value: score (unspecified) / 60.4 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table without explicit split/metric-definition details at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not provided at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: College Biology / not reported
- Metric/value: score (unspecified) / 59.0 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table; the inspected locator lacks split/metric-definition metadata.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not published at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: College Medicine / not reported
- Metric/value: score (unspecified) / 54.7 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table without additional split/metric-definition metadata at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not provided at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: MedQA / not reported
- Metric/value: score (unspecified) / 50.6 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table; metric-definition and split not provided at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Metric-definition and split not provided at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: MedQA (5-option) / not reported
- Metric/value: score (unspecified) / 42.8 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table without explicit split/metric-definition metadata at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details not reported at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: PubMedQA / not reported
- Metric/value: score (unspecified) / 77.5 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table without explicit split/metric-definition metadata at the inspected locator.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not published at the inspected locator.

### Medical benchmark suite (per-task scores reported on model page)

- Dataset/split: MedMCQA / not reported
- Metric/value: score (unspecified) / 48.1 (`higher-is-better`)
- Model scope: BioMistral-7B (reported on the BioMistral-7B-BnB.8 model page)
- Conditions: Reported on the model-card benchmark table; the inspected locator lacks split/metric-definition metadata.
- Source: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Locator: Benchmark table on the BioMistral-7B-BnB.8 model card (reported medical benchmarks)
- Caveat: Dataset split and metric-definition details were not provided at the inspected locator.

## Comparisons

### nvidia-llama-3-1-nemotron-nano-8b-healthcare-text2sql — `insufficient-evidence`

- Task: Biomedical-text tasks and medical QA benchmarks
- Criteria: No BioMistral primary-source head-to-head, checkpoint-scoped benchmark evidence against the listed alternative was found in the inspected BioMistral sources; a valid direct comparison would require matched dataset/split/metric and the alternative's primary-source benchmark evidence.
- Rationale: Inspected BioMistral primary files and the arXiv preprint publish per-column SFT/benchmark numeric results for BioMistral-7B and merged variants but do not publish protocol-matched comparisons to the named alternative at the inspected locators.
- Comparison conditions: A protocol-matched comparison requires the alternative's primary-source benchmark with identical dataset/split/metric definitions and the same evaluation prompt; that alternative evidence was not inspected in the BioMistral primary sources.
- Evidence: https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://arxiv.org/pdf/2402.10373

### stanfordcrfm-biomedlm-2-7b-safety-review — `insufficient-evidence`

- Task: Biomedical-text tasks and medical QA benchmarks
- Criteria: No BioMistral primary-source head-to-head, checkpoint-scoped benchmark evidence against the listed alternative was found in the inspected BioMistral sources; a valid direct comparison would require matched dataset/split/metric and the alternative's primary-source benchmark evidence.
- Rationale: Inspected BioMistral primary files and the arXiv preprint publish SFT/benchmark numeric results for BioMistral-7B and merged variants but do not publish protocol-matched comparisons to the named alternative at the inspected locators.
- Comparison conditions: A valid comparison requires the alternative's primary benchmark evidence with identical evaluation protocol; that comparator evidence was not present among the inspected BioMistral primary sources.
- Evidence: https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8

## Limitations and safety

### Limitations

- Context-length reporting is inconsistent across inspected repository artifacts: the BioMistral model page lists sequence length 2048 for presentation notes while canonical config blobs report max_position_embeddings = 32768 and sliding_window = 4096. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-DARE/blob/347e1b5e56590ddfc22e4ee15a2f648ea87a20a8/config.json, https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json
- Evidence gap: the exact model parameter count is not reported in the inspected config.json blobs or variant pages. Sources: https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json, https://huggingface.co/BioMistral/BioMistral-7B-DARE
- Evidence gap: the tokenization algorithm (BPE, SentencePiece, unigram, or other) and detailed tokenizer merges/vocabulary text files are not explicitly documented at the inspected tokenizer/config blobs. Sources: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/blob/main/tokenizer_config.json, https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json
- Evidence gap: no canonical model-weights or code license declaration was published at the inspected primary model pages or config/tokenizer blobs. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Evidence gap: no creator-published PHI-handling guidance, clinical-deployment certification, or clinical-use disclaimers were found at the inspected primary model pages and config/tokenizer blobs. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8

### Safety

- Creators present BioMistral as a suite of Mistral-based further-pretrained open-source models intended for medical/biomedical domains and research use; the repository/variant pages and the arXiv preprint frame the models and evaluation as research-oriented. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-DARE, https://arxiv.org/pdf/2402.10373
- Evidence gap: the inspected canonical repository/model-page files do not publish explicit PHI-handling guidance, clinical-deployment instructions, or clinical-use certification for the BioMistral-7B checkpoint. Sources: https://huggingface.co/BioMistral/BioMistral-7B, https://huggingface.co/BioMistral/BioMistral-7B-BnB.8

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### BioMistral model page (project overview and model card)

- URL: https://huggingface.co/BioMistral/BioMistral-7B
- Publisher: Hugging Face (BioMistral project authors)
- Type: `model-card`
- Primary because: Canonical Hugging Face model page for BioMistral-7B providing project-level statements, presentation notes, and README usage instructions.
- Scope: BioMistral-7B checkpoint and project overview
- Supports: BioMistral is a suite of Mistral-based further-pretrained open source models suited for medical domains
- Supports: Project-level presentation notes list sequence length 2048 for BioMistral-7B variants
- Supports: README files provide usage instructions for Transformers, vLLM, Docker, and SGLang
- Supports: Quantized builds (AWQ 4-bit, BnB.4, BnB.8) are listed with VRAM requirements

### BioMistral-7B base config.json (model architecture metadata)

- URL: https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Canonical config.json blob for the BioMistral-7B checkpoint listing architecture fields and model hyperparameters.
- Scope: BioMistral-7B checkpoint configuration (base)
- Supports: Architecture: model_type "mistral" / MistralForCausalLM
- Supports: hidden_size=4096, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads=8
- Supports: vocab_size=32000, max_position_embeddings=32768, sliding_window=4096
- Supports: torch_dtype = bfloat16

### BioMistral-7B-DARE model page (merged variant description)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-DARE
- Publisher: Hugging Face (BioMistral project authors)
- Type: `model-card`
- Primary because: Model page for the DARE merged variant documenting merged-variant identity, sequence-length presentation notes, and variant-specific metadata.
- Scope: BioMistral-7B-DARE merged variant
- Supports: Declaration of merged variants DARE, TIES, SLERP
- Supports: Presentation notes including sequence length statements for variants
- Supports: README and usage instructions specific to the variant

### BioMistral-7B-TIES model page (merged variant description)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-TIES
- Publisher: Hugging Face (BioMistral project authors)
- Type: `model-card`
- Primary because: Model page for the TIES merged variant documenting merged-variant identity and variant-level metadata.
- Scope: BioMistral-7B-TIES merged variant
- Supports: Declaration of merged variant TIES
- Supports: Variant-level README and usage notes

### BioMistral-7B-SLERP model page (merged variant description)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-SLERP
- Publisher: Hugging Face (BioMistral project authors)
- Type: `model-card`
- Primary because: Model page for the SLERP merged variant documenting merged-variant identity and variant-level metadata.
- Scope: BioMistral-7B-SLERP merged variant
- Supports: Declaration of merged variant SLERP
- Supports: Variant-level README and usage notes

### BioMistral-7B-DARE config.json (variant config blob)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-DARE/blob/347e1b5e56590ddfc22e4ee15a2f648ea87a20a8/config.json
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Inspected config.json blob for the DARE merged variant documenting variant-specific config settings and identical hyperparameters to the base config.
- Scope: BioMistral-7B-DARE configuration blob
- Supports: Architecture: MistralForCausalLM with 32 hidden layers, hidden_size=4096, intermediate_size=14336, 32 attention heads
- Supports: torch_dtype = bfloat16
- Supports: max_position_embeddings = 32768, sliding_window = 4096
- Supports: use_cache = true

### BioMistral-7B-SLERP config blob (blame view)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-SLERP/blame/ea6b3ceb95b5e0a8e004c93c75a43fcb3935d882/config.json
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Inspected SLERP variant config indicating the same architecture and hyperparameters as other variant config blobs.
- Scope: BioMistral-7B-SLERP configuration blob
- Supports: Configuration fields matching DARE variant (MistralForCausalLM and reported hyperparameters)
- Supports: torch_dtype = bfloat16

### BioMistral generation_config.json (generation defaults)

- URL: https://huggingface.co/BioMistral/BioMistral-7B/blob/main/generation_config.json
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Canonical generation_config.json blob documenting generation defaults such as bos_token_id and eos_token_id.
- Scope: BioMistral-7B generation defaults
- Supports: generation_config sets bos_token_id = 1, eos_token_id = 2, transformers_version = "4.35.0"

### BioMistral-7B-BnB.8 model page (quantized build with reported medical benchmarks)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8
- Publisher: Hugging Face (BioMistral project authors)
- Type: `model-card`
- Primary because: Model-page entry reporting quantized-build/variant benchmark numeric results across a set of medical benchmarks for the BnB.8 build.
- Scope: BioMistral-7B BnB.8 quantized build
- Supports: Reported medical benchmark scores for Clinical KG, Medical Genetics, Anatomy, Pro Medicine, College Biology, College Medicine, MedQA, MedQA (5-option), PubMedQA, MedMCQA and an aggregate average value (as presented on the model page)

### BioMistral-7B-BnB.8 tokenizer_config.json (tokenizer metadata for BnB.8)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/blob/main/tokenizer_config.json
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Inspected tokenizer_config.json blob for the BnB.8 variant documenting special tokens and BOS/EOS handling.
- Scope: BioMistral-7B-BnB.8 tokenizer configuration blob
- Supports: Defines special tokens: "<unk>", "<s>", and "</s>"
- Supports: add_bos_token = true, add_eos_token = false
- Supports: bos_token = "<s>", eos_token = "</s>", and added_tokens_decoder entries for token ids 0,1,2

### arXiv preprint (BioMistral: evaluation tables and merging-method results)

- URL: https://arxiv.org/abs/2402.10373
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv record for the BioMistral preprint describing evaluation tables, merging methods (DARE/TIES/SLERP), and reported numeric results.
- Scope: BioMistral evaluation and methods (paper)
- Supports: Presentation of merging strategies DARE, TIES, SLERP and reported gains
- Supports: Evaluation tables including Prompt 1 QA prompt per-domain scores and few-shot/SFT result tables
- Supports: Sections on calibration and truthfulness

### arXiv PDF (BioMistral preprint PDF with evaluation tables)

- URL: https://arxiv.org/pdf/2402.10373
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv PDF containing the evaluation tables (used to verify table values and reported per-domain scores).
- Scope: BioMistral evaluation tables (PDF)
- Supports: Table 2 (Prompt 1 QA prompt few-shot accuracy table) reporting BioMistral-7B per-domain scores (Health 72.7; Nutrition 68.8; Psychology 31.6; Science 33.3; average 51.6)
- Supports: Reported comparative numbers for Mistral-7B-Instruct in the same table

### BioMistral-7B-DARE commit history (example commits)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-DARE/commits/1ca66328d919992302434099f5419ccac57dbd5b
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Commit history view for the DARE variant demonstrating README and file-upload commits used in the project repository.
- Scope: BioMistral-7B-DARE repository commit history
- Supports: Commit history entries show updates to README.md and file uploads for the variant

### BioMistral-7B-BnB.8 commit history (model-card commits)

- URL: https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/commits/main
- Publisher: Hugging Face (BioMistral project authors)
- Type: `repository`
- Primary because: Commit history view for the BnB.8 variant demonstrating README updates and initial README creation.
- Scope: BioMistral-7B-BnB.8 repository commit history
- Supports: Commit history entries show README updates and variant file commits

## Evidence gaps

- Evidence gap: no canonical model-weights or code license declared at https://huggingface.co/BioMistral/BioMistral-7B (inspected model card and linked blobs).
- Evidence gap: exact model parameter count not reported in inspected blobs at https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json or on variant pages (e.g., https://huggingface.co/BioMistral/BioMistral-7B-DARE).
- Evidence gap: tokenization algorithm (BPE, SentencePiece, unigram, or other) and merges/vocabulary text files not specified at https://huggingface.co/BioMistral/BioMistral-7B-BnB.8/blob/main/tokenizer_config.json or https://huggingface.co/BioMistral/BioMistral-7B/blob/main/config.json.
- Evidence gap: authoritative runtime truncation/serving contract (max input tokens, truncation/sliding behavior at runtime) not published at inspected locators https://huggingface.co/BioMistral/BioMistral-7B and https://huggingface.co/BioMistral/BioMistral-7B-DARE/blob/347e1b5e56590ddfc22e4ee15a2f648ea87a20a8/config.json (config reports max_position_embeddings=32768 but presentation notes list sequence length=2048).
- Evidence gap: no creator-published PHI-handling guidance or clinical-deployment certification found at https://huggingface.co/BioMistral/BioMistral-7B or https://huggingface.co/BioMistral/BioMistral-7B-DARE.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses unapproved repository owner 'dizza01' for this exact model scope: $.sources[5] uses unapproved repository owner 'dizza01' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'lonestriker' for this exact model scope: $.sources[10] uses unapproved repository owner 'lonestriker' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'shaikatasif' for this exact model scope: $.sources[11] uses unapproved repository owner 'shaikatasif' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
