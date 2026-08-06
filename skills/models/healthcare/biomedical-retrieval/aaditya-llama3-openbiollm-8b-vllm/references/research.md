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

- Research key: `huggingface-co-aaditya-llama3-openbiollm-8b-d788c593a7`
- Independent audit: `revised`
- Researched: `2026-08-06T11:04:54.156902+00:00`

Canonical repository artifacts for aaditya/Llama3-OpenBioLLM-8B identify the model as an 8B-parameter, instruction-tuned biomedical derivative with architecture LlamaForCausalLM (model_type="llama"). The repository config.json records _name_or_path = "meta-llama/Meta-Llama-3-8B", hidden_size = 4096, intermediate_size = 14336, num_hidden_layers = 32, num_attention_heads = 32, num_key_value_heads = 8, max_position_embeddings = 8192, and vocab_size = 128256. The canonical README and commits assert the model is fine-tuned from meta-llama/Meta-Llama-3-8B and Starling-RM-34B and report aggregate benchmark claims in top-level prose/commit messages; however, no explicit upstream hf-... checkpoint tag or immutable revision mapping the Forge serving slug aaditya-llama3-openbiollm-8b-vllm to a unique upstream artifact is reported in the inspected canonical artifacts. The repository defines special tokens (special_tokens_map.json) but does not publish a canonical tokenizer implementation or explicit tokenization/normalization/padding/truncation policy in the inspected files. Programmatic output contract details (logits shapes, embedding dimensionalities, exposed downstream task heads) are not documented in the inspected repository files. There is conflicting license metadata between README/blame and a commit metadata entry (Meta‑Llama license vs Apache-2.0). Per-dataset, checkpoint-scoped benchmark tables, evaluation scripts, prompt templates, and scoring artifacts required to verify claimed numeric results are not present in the canonical model-card or inspected repository files. Primary sources inspected: Hugging Face model landing page, README (blame view), config.json (blame view), special_tokens_map.json blob, repository commits (c45e06e1, f3f49cbb, 1fb683ea), arXiv preprints and a PMC article referenced in the repository metadata; all claims above are scoped to the exact checkpoint-level evidence found or not found in these canonical URLs.

## Identity

- Upstream name: meta-llama/Meta-Llama-3-8B
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 8 billion parameters
- Architecture/head: LlamaForCausalLM (decoder-only transformer)
- License: Conflicting statements in primary artifacts: README (blame view) asserts Meta‑Llama license while a repository commit (commit c45e06e1) references Apache-2.0; maintainer clarification required to distinguish model-weights license vs repository/code license.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc

## Selection

### Recommended

- **Biomedical question answering and research workflows** — Canonical model landing page and repository README describe the checkpoint as an instruction‑tuned biomedical derivative intended for biomedical question answering and research workflows.
  Scope: aaditya/Llama3-OpenBioLLM-8B (model card and README)
  Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

### Conditional

- **Biomedical research or educational use with human oversight** — Use only with human oversight and explicit downstream verification; canonical repository does not document formal clinical validation, per-dataset evaluation protocols, or regulatory safeguards in the inspected files.
  Scope: aaditya/Llama3-OpenBioLLM-8B (model card and README)
  Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

### Avoid

- **Clinical diagnosis, treatment planning, or any clinical decision-making without expert review** — Repository README and model card explicitly caution outputs should not replace professional medical advice and advise consulting qualified healthcare providers; repository lacks formal clinical validation and regulatory disclaimers beyond general advisories in the inspected files.
  Scope: aaditya/Llama3-OpenBioLLM-8B (model card and README)
  Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

## Input preparation

### Semantic inputs

- Text inputs (natural language prompts/questions) are the accepted modality. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### Accepted formats

- Canonical repository and model card present the checkpoint as a text/LLM (no alternate modalities documented in inspected files). Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### Preprocessing

- Max position embeddings (context length) = 8192 as specified in config.json. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json
- Model architecture config entries: model_type = "llama", hidden_size = 4096, intermediate_size = 14336, num_hidden_layers = 32, num_attention_heads = 32, num_key_value_heads = 8 as specified in config.json. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json
- Vocab size = 128256 and torch_dtype = "bfloat16" recorded in config.json; repository does not publish a canonical tokenizer implementation file in the inspected files to map vocab entries to a tokenizer algorithm. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blob/701cd845975eb1c4f09135bff5fb2757680fc37d/special_tokens_map.json
- Tokenizer algorithm (BPE vs SentencePiece vs other), tokenizer implementation file path, explicit normalization/tokenization rules, padding/truncation policy, and batching limits are not present in the inspected canonical repository files. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blob/701cd845975eb1c4f09135bff5fb2757680fc37d/special_tokens_map.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### Pre-submit validation

- The model card and README do not specify formal input validation rules (e.g., explicit padding/truncation policies beyond max_position_embeddings, forbidden characters, or content filtering rules) in the inspected repository files. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

### Task-specific formatting

- No canonical prompt templates, paired-input ordering, or instruction-format examples are provided in the inspected model card or README; the README references an accompanying paper but does not expose canonical prompt formats in the inspected files. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

## Output interpretation

### Outputs

- The checkpoint is a causal language model (LlamaForCausalLM) and therefore emits autoregressive text outputs; special_tokens_map.json defines BOS/EOS/PAD token strings and token ids in config.json define bos_token_id and eos_token_id. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blob/701cd845975eb1c4f09135bff5fb2757680fc37d/special_tokens_map.json
- Programmatic output contract details (logits/probability output shapes, embedding outputs and dimensionalities, and any exposed task heads) are not documented in the inspected canonical repository files. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### Interpretation

- Authors and the model README advise human oversight and caution for clinical interpretation; no explicit numeric calibration guidance or confidence-score semantics are provided in the inspected model card or README. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

### Post-inference validation

- The model card and README do not provide post-inference validation checks, calibration steps, or recommended downstream verification procedures beyond general human oversight recommendations. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### abhinand/MedEmbed-base-v0.1 — `insufficient-evidence`

- Task: biomedical retrieval / embedding tasks
- Criteria: No checkpoint-scoped, protocol-matched primary-source benchmark data for both models found in the inspected artifacts.
- Rationale: Inspected canonical sources for aaditya/Llama3-OpenBioLLM-8B do not include matched, checkpoint-scoped evaluation artifacts for the alternative to enable a protocol-aligned comparison.
- Comparison conditions: Checked aaditya/Llama3-OpenBioLLM-8B model card and README for per-dataset, per-checkpoint evaluations; alternative's canonical checkpoint-scoped primary artifacts not inspected/available within the checked primary URLs.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### abhinand/MedEmbed-large-v0.1 — `insufficient-evidence`

- Task: biomedical retrieval / embedding tasks
- Criteria: No checkpoint-scoped primary-source evaluations found for the alternative within the inspected evidence set.
- Rationale: Missing canonical, checkpoint-scoped evaluation artifacts for the alternative.
- Comparison conditions: Checked aaditya/Llama3-OpenBioLLM-8B model card and README for per-dataset evaluations; alternative primary artifacts not part of inspected canonical sources.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### abhinand/MedEmbed-small-v0.1 — `insufficient-evidence`

- Task: biomedical retrieval / embedding tasks
- Criteria: No checkpoint-scoped primary-source evaluations found for the alternative within the inspected evidence set.
- Rationale: Missing canonical artifacts for the alternative.
- Comparison conditions: Checked aaditya/Llama3-OpenBioLLM-8B canonical sources; alternative checkpoint evidence not verified.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### cambridgeltl/SapBERT-from-PubMedBERT-fulltext — `insufficient-evidence`

- Task: biomedical entity embedding / retrieval
- Criteria: No shared primary-source checkpoint-scoped benchmark artifacts in the inspected findings for both models.
- Rationale: Inspected primary findings do not include canonical, directly comparable evaluation results for the alternative.
- Comparison conditions: Checked aaditya/Llama3-OpenBioLLM-8B canonical sources and relevant cited arXiv material; alternative's checkpoint-scoped canonical evidence not part of inspected URLs.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://arxiv.org/html/2408.13833v1

### ncbi/MedCPT-Article-Encoder — `insufficient-evidence`

- Task: document/query embedding and retrieval
- Criteria: No directly comparable, checkpoint-scoped primary-source evaluations present in the inspected findings.
- Rationale: Alternative's primary artifacts are not present in the inspected evidence set.
- Comparison conditions: Only aaditya/Llama3-OpenBioLLM-8B canonical sources were inspected for this audit.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### ncbi/MedCPT-Cross-Encoder — `insufficient-evidence`

- Task: cross-encoder ranking for biomedical retrieval
- Criteria: No comparable primary-source evaluations available in the inspected findings.
- Rationale: Missing canonical artifacts for the alternative.
- Comparison conditions: Inspected aaditya/Llama3-OpenBioLLM-8B canonical sources only.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### ncbi/MedCPT-Query-Encoder — `insufficient-evidence`

- Task: query encoding for biomedical retrieval
- Criteria: No comparable checkpoint-scoped primary-source data in the inspected findings.
- Rationale: Missing canonical artifacts for the alternative.
- Comparison conditions: Only aaditya canonical sources inspected.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### NeuML/pubmedbert-base-embeddings — `insufficient-evidence`

- Task: biomedical embeddings / retrieval
- Criteria: No shared canonical, checkpoint-scoped benchmark artifacts in the inspected findings.
- Rationale: Missing canonical artifacts for the alternative.
- Comparison conditions: Checked aaditya canonical sources; alternative evidence not inspected here.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### nvidia NV EmbedQA E5 (original creator/source) — `insufficient-evidence`

- Task: embedding-based retrieval
- Criteria: No canonical primary-source benchmark comparisons between the models present in the inspected findings.
- Rationale: Missing canonical artifacts for the alternative.
- Comparison conditions: Inspected only aaditya canonical sources and cited arXiv material; alternative's primary checkpoint evidence not part of inspected URLs.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

### potsu-potsu/medembed-small-biomedical-matryoshka-v2 — `insufficient-evidence`

- Task: biomedical embeddings / retrieval
- Criteria: No directly comparable canonical primary-source evaluations in the inspected findings.
- Rationale: Missing canonical artifacts for the alternative.
- Comparison conditions: Only aaditya canonical sources were inspected.
- Evidence: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

## Limitations and safety

### Limitations

- Authors note an accompanying paper is referenced but the inspected canonical repository file (README) lists the paper as 'Coming soon' and does not provide a definitive published-paper locator or complete methods and evaluation protocols. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B
- The canonical repository and model card do not include per-dataset, checkpoint-scoped benchmark tables or full evaluation protocol details for claimed numeric results; inspected files do not present per-dataset canonical locators. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B?inference_provider=featherless-ai
- Exact upstream checkpoint tag, hf-... identifier, commit hash, or named revision explicitly tying the Forge serving slug aaditya-llama3-openbiollm-8b-vllm to a unique upstream artifact is not reported in the inspected canonical repository files; checked commit views and repository tree without finding an explicit mapping. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/f3f49cbb5ed58f459c57df16007102243f9f8608
- Tokenizer algorithm name, tokenizer implementation path, normalization rules, and exact tokenization behavior are not present in the inspected canonical repository files. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blob/701cd845975eb1c4f09135bff5fb2757680fc37d/special_tokens_map.json, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B
- Programmatic output contract details (logits/probability return formats, embedding dimensionalities, and any exposed task heads) are not documented in the inspected canonical repository files. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json
- There is conflicting license metadata in the inspected canonical artifacts (README/blame asserts Meta‑Llama license; a repository commit lists Apache-2.0); this ambiguity is a legal/operational evidence gap requiring maintainer clarification. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc

### Safety

- The model card and README include medical disclaimers and advise human oversight; the README explicitly states outputs should not replace professional medical advice and recommends consultation with a qualified healthcare provider. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md
- Evidence gap: No explicit PHI handling guidance, data-handling procedures, or detailed clinical/regulatory disclaimers beyond general medical advisories are documented in the inspected canonical model card or README. Sources: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B, https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### aaditya / Llama3-OpenBioLLM-8B (Hugging Face model card)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B
- Publisher: aaditya (Hugging Face repository)
- Type: `model-card`
- Primary because: Canonical model landing page/model card for the checkpoint under review; contains top-level model description and reported benchmark list.
- Scope: aaditya/Llama3-OpenBioLLM-8B (model card)
- Supports: model described as instruction‑tuned biomedical derivative intended for biomedical question answering and research workflows
- Supports: top-level model description and links to repository files
- Supports: aggregate benchmark claims visible in model card/landing page prose

### aaditya / Llama3-OpenBioLLM-8B README (blame view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md
- Publisher: aaditya (Hugging Face repository file)
- Type: `repository`
- Primary because: Repository README file from the canonical model repository; contains claimed parameter scale, usage advisories, and reference to an accompanying paper.
- Scope: aaditya/Llama3-OpenBioLLM-8B README (blame view)
- Supports: claim of 8 billion parameters
- Supports: medical disclaimers and human-oversight advisories
- Supports: reference to an accompanying paper listed as 'Coming soon'
- Supports: high-level usage guidance and aggregate benchmark claims (prose)

### aaditya / Llama3-OpenBioLLM-8B config.json (blame view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json
- Publisher: aaditya (Hugging Face repository file)
- Type: `repository`
- Primary because: Directly inspected model configuration file providing architecture, model_type, max_position_embeddings, vocabulary size, and other hyperparameters.
- Scope: aaditya/Llama3-OpenBioLLM-8B config.json
- Supports: "_name_or_path" = "meta-llama/Meta-Llama-3-8B"
- Supports: model_type = "llama"
- Supports: max_position_embeddings = 8192
- Supports: vocab_size = 128256
- Supports: num_hidden_layers = 32, num_attention_heads = 32, hidden_size = 4096, intermediate_size = 14336 and other config fields

### aaditya / Llama3-OpenBioLLM-8B special_tokens_map.json (blob view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blob/701cd845975eb1c4f09135bff5fb2757680fc37d/special_tokens_map.json
- Publisher: aaditya (Hugging Face repository file)
- Type: `repository`
- Primary because: Defines BOS/EOS/PAD tokens for the tokenizer mapping.
- Scope: aaditya/Llama3-OpenBioLLM-8B special_tokens_map.json
- Supports: definitions of bos_token/eos_token/pad_token in repository

### aaditya / Llama3-OpenBioLLM-8B commit c45e06e1 (commit view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc
- Publisher: aaditya (Hugging Face repository)
- Type: `repository`
- Primary because: Commit-level metadata referenced in repository used to identify license ambiguity and README edits referencing aggregate benchmark claims.
- Scope: aaditya/Llama3-OpenBioLLM-8B commit c45e06e1
- Supports: commit-level metadata referencing Apache-2.0 and other repository-level claims
- Supports: README edits and aggregate benchmark assertions in commit message/prose

### aaditya / Llama3-OpenBioLLM-8B commit f3f49cbb (commit view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/f3f49cbb5ed58f459c57df16007102243f9f8608
- Publisher: aaditya (Hugging Face repository)
- Type: `repository`
- Primary because: Repository commit documenting README edits relevant to model naming and dataset list.
- Scope: aaditya/Llama3-OpenBioLLM-8B commit f3f49cbb
- Supports: evidence of repository edits to README (example title changed to reference OpenBioLLM-8B)
- Supports: datasets list updated to include berkeley-nest/Nectar (as recorded in commit)

### aaditya / Llama3-OpenBioLLM-8B commit 1fb683ea (initial commit view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/1fb683ea3fd9a59d501b7845af03f8d9736c76a5
- Publisher: aaditya (Hugging Face repository)
- Type: `repository`
- Primary because: Initial commit metadata and repository configuration entries (Git LFS filter entries) from the canonical repository.
- Scope: aaditya/Llama3-OpenBioLLM-8B initial commit
- Supports: initial commit adds Git LFS filter entries for large file types and repository setup information

### ArXiv preprint — Biomedical Large Language Models Seem not to be Superior to Generalist Models on Unseen Medical Data (arXiv 2408.13833v1)

- URL: https://arxiv.org/html/2408.13833v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Primary preprint cited in repository metadata and inspected for per-task metrics and benchmark context.
- Scope: arXiv preprint 2408.13833v1
- Supports: paper-sourced metrics and discussion referenced by the repository metadata (inspected for per-checkpoint tables/locators)

### arXiv 2410.01553v2 (HTML)

- URL: https://arxiv.org/html/2410.01553v2
- Publisher: arXiv
- Type: `paper`
- Primary because: Preprint related to medical adaptation and benchmark discussions referenced in the inspected findings.
- Scope: arXiv 2410.01553v2
- Supports: paper-sourced discussions of medical adaptation and benchmark comparisons referenced in the dossier

### arXiv 2411.04118 (abstract page)

- URL: https://arxiv.org/abs/2411.04118
- Publisher: arXiv
- Type: `paper`
- Primary because: Preprint cited in the inspected findings for related medical adaptation/benchmark context.
- Scope: arXiv 2411.04118
- Supports: citation for medical adaptation and benchmark discussions referenced in the dossier

### PMC article — Biomedicine safety context (PMC)

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12089759
- Publisher: PMC / National Library of Medicine
- Type: `paper`
- Primary because: Canonical publisher article cited for clinical/biomedical safety context referenced in the dossier.
- Scope: PMC article
- Supports: clinical/biomedical safety notes and cautionary context referenced in the dossier

### OpenReview PDF attachment (knowledge-graph evaluation)

- URL: https://openreview.net/notes/edits/attachment?id=6JMmOmQBDP&name=pdf
- Publisher: OpenReview
- Type: `paper`
- Primary because: Primary artifact for reported OpenBioLLM evaluation metrics in an OpenReview attachment as cited in the inspected findings.
- Scope: OpenReview PDF attachment
- Supports: reported evaluation metrics on knowledge-graph evaluation as referenced in the inspected findings

### aaditya / Llama3-OpenBioLLM-8B (inference-provider view)

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B?inference_provider=featherless-ai
- Publisher: aaditya (Hugging Face model landing page with inference provider parameter)
- Type: `model-card`
- Primary because: Model landing page view with inference-provider parameter; used to confirm that per-benchmark scores are visible via the model card/inference-provider view.
- Scope: aaditya/Llama3-OpenBioLLM-8B inference-provider view
- Supports: per-benchmark/aggregate scores visible in model-card inference-provider view (prose/landing page view)

### Cited official first-party source

- URL: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc , https://arxiv.org/html/2408.13833v1
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: aaditya-llama3-openbiollm-8b
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: Exact upstream checkpoint tag, hf-... identifier, commit hash, or named revision explicitly tying the Forge serving slug aaditya-llama3-openbiollm-8b-vllm to a unique upstream artifact is not reported in the inspected canonical repository files. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/f3f49cbb5ed58f459c57df16007102243f9f8608
- Evidence gap: Tokenizer name, tokenizer algorithm (BPE vs SentencePiece vs other), tokenizer implementation file path, explicit normalization/tokenization rules, padding/truncation policy, and batching limits are not present in the inspected canonical files. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blob/701cd845975eb1c4f09135bff5fb2757680fc37d/special_tokens_map.json , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B
- Evidence gap: Tokenizer return shapes, explicit padding/truncation policy, batching limits, and formal input validation rules are not documented in the inspected canonical repository files. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md
- Evidence gap: Programmatic output contract details (logits/probability output shapes, embedding outputs and dimensionalities, and any exposed task heads) are not documented in the inspected canonical repository files. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/2523a77b3ec304ff07272bcee1c663638a3ceff1/config.json , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B
- Evidence gap: Per-dataset, checkpoint-scoped benchmark tables, exact dataset splits used, and the full evaluation protocol (prompt templates, scoring scripts, or downstream head dependencies) for claimed numeric results are not present in the inspected canonical model card or repository files. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B?inference_provider=featherless-ai , https://arxiv.org/html/2408.13833v1
- Evidence gap: Canonical, unambiguous license declaration for the checkpoint (model-weights license vs code/repository license) is not resolvable from the inspected canonical artifacts; README/blame asserts Meta‑Llama license while a commit/model-index metadata references Apache-2.0. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc
- Evidence gap: Direct, checkpoint-scoped primary-source benchmark artifacts or evaluation protocols for each Forge-listed alternative are not present in the inspected findings; therefore task- and protocol-matched comparisons cannot be constructed from the available primary evidence. Checked URLs: https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4] uses forbidden secondary host ollama.com: $.sources[4] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'richarderkhov' for this exact model scope: $.sources[5] uses unapproved repository owner 'richarderkhov' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'momonir' for this exact model scope: $.sources[6] uses unapproved repository owner 'momonir' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'quantfactory' for this exact model scope: $.sources[7] uses unapproved repository owner 'quantfactory' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].value must contain a reported numeric result: $.benchmarks[1].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/blame/b1cdba997fd109ad9e33522ae075d712a82e69b3/README.md , https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B/commit/c45e06e1cc285f4ad10eb4e54876f59b1534b5fc , https://arxiv.org/html/2408.13833v1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
