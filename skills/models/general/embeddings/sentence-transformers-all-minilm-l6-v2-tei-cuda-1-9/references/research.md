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

- Research key: `huggingface-co-sentence-transformers-all-minilm-l6-v2-32e2db27ec`
- Independent audit: `revised`
- Researched: `2026-08-06T13:59:17.099041+00:00`

Upstream primary Hugging Face blobs for sentence-transformers/all-MiniLM-L6-v2 document an embedding checkpoint loadable via SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2') that maps sentences and short paragraphs to 384-dimensional dense vectors intended for semantic search, clustering, and sentence-similarity tasks. The README blobs show the model was fine-tuned from nreimers/MiniLM-L6-H384-uncased and include an example mean-pooling implementation that multiplies token embeddings by an expanded attention mask, sums, and divides by the mask sum; the model card example also shows L2 normalization. The tokenizer_config.json blob for this repository reports tokenizer_class = "BertTokenizer", do_lower_case = true, model_max_length = 512, and standard special tokens. The checked primary Hugging Face blobs do not report a checkpoint-specific immutable revision blob for model weights, do not publish a checkpoint-specific parameter count, and do not contain a checkpoint-scoped numeric benchmark table or head-to-head numeric comparisons for this exact checkpoint. The checked primary blobs also do not provide an explicit repository LICENSE blob within the provided findings.

## Identity

- Upstream name: sentence-transformers/all-MiniLM-L6-v2
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Sentence-transformers embedding checkpoint fine-tuned from nreimers/MiniLM-L6-H384-uncased producing 384-dimensional sentence embeddings (embedding encoder / pooling head); exact layer/hidden-size counts for this checkpoint are not reported in the checked primary blobs.
- License: not reported
- Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/a6ee86b5ffddbfd5bfb2cc7f96f357d8cd094cde/README.md, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json

## Selection

### Recommended

- **Semantic textual similarity for sentences and short paragraphs** — The upstream model card and README document the checkpoint as a sentence/short-paragraph encoder mapping inputs to 384-d vectors and list sentence-similarity as an intended use.
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- **Semantic search / information retrieval over short text** — The upstream model card and README cite information retrieval and semantic search as intended uses for the produced sentence embeddings.
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- **Clustering of short-text embeddings** — The upstream model card and README list clustering as an intended use for the model's sentence embeddings.
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md

### Conditional

- **Fast retriever in RAG or dense-retrieval pipelines (short-text retrieval)** — Use only for short text inputs with downstream validation of retrieval quality; validate segmentation for longer documents because the checked primary blobs show tokenizer_config.json model_max_length = 512 and README examples use truncation=True but do not state an explicit default truncation length in the provided findings (see evidence gap).
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- **Embedding-based downstream classifiers or ranking systems (after supervised calibration)** — Only after downstream task-specific training and held-out validation because upstream blobs document embedding generation but do not provide calibrated supervised classification thresholds.
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### Avoid

- **Token-level prediction tasks (e.g., token classification, token-level tagging) relying on a token-head output** — Upstream README and model card document this checkpoint as a sentence/short-paragraph encoder using mean-pooling to produce sentence embeddings rather than exposing a token-level prediction head.
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- **Encoding long or unsegmented documents with the expectation that the entire document content is always preserved without segmentation** — Tokenizer configuration reports model_max_length = 512 but the README examples call truncation=True without stating an explicit default truncation length in the provided findings; effective runtime truncation behavior for long inputs is not specified in the checked primary blobs.
  Scope: sentence-transformers/all-MiniLM-L6-v2 (upstream checkpoint)
  Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json

## Input preparation

### Semantic inputs

- Plain text sentences or short paragraphs (UTF-8 text strings) are the officially evidenced upstream input form. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### Accepted formats

- Plain text sentences or short paragraphs consumed via the SentenceTransformer API's encode usage example (Python strings). Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### Preprocessing

- Use the upstream checkpoint tokenizer as configured (tokenizer_class = "BertTokenizer"). Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json
- Tokenizer configuration sets do_lower_case = true and standard special tokens ([UNK], [SEP], [PAD], [CLS], [MASK]). Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json
- Tokenizer configuration reports model_max_length = 512 and enables tokenize_chinese_chars / basic tokenization per tokenizer_config blob. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json
- Upstream README documents attention-mask-aware mean pooling: multiply token embeddings by the expanded attention mask, sum over tokens, and divide by the (clamped) sum of the mask to obtain the sentence embedding; README examples also show L2 normalization of the pooled vector. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### Pre-submit validation

- Validate that inputs are sentences or short paragraphs because that is the intended upstream scope. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Evidence gap: The checked primary blobs do not state an explicit default runtime truncation length in the README examples; tokenizer_config.json reports model_max_length = 512 but the README examples only show truncation=True without an explicit numeric default. Confirm effective truncation behavior before submitting longer inputs. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json

### Task-specific formatting

- No special prompt template is reported in the checked upstream files; evidenced upstream usage is direct sentence encoding via the SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2') API example. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

## Output interpretation

### Outputs

- Upstream model card and README report the model maps sentences and paragraphs to a 384-dimensional dense vector. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md

### Interpretation

- Interpret outputs as sentence- or short-paragraph embeddings capturing semantic information; they are not token-level prediction outputs. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md

### Post-inference validation

- Post-inference, verify that each output vector has 384 dimensions to match the upstream model card and README. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### nreimers/MiniLM-L6-H384-uncased — `insufficient-evidence`

- Task: Embedding generation / sentence embedding use (architectural base vs fine-tuned checkpoint)
- Criteria: No checkpoint-specific numeric benchmark or head-to-head evaluation table for sentence-transformers/all-MiniLM-L6-v2 versus the base nreimers/MiniLM-L6-H384-uncased was found in the checked primary blobs.
- Rationale: The README/blame indicates the upstream base model is nreimers/MiniLM-L6-H384-uncased, but no primary-source numeric comparisons or benchmark tables for this exact checkpoint against that base were present in the checked primary sources.
- Comparison conditions: Checked model card and README (blame) for explicit comparisons; none contained checkpoint-scoped numeric comparisons in the provided findings.
- Evidence: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md

## Limitations and safety

### Limitations

- Primary upstream blobs checked do not report a checkpoint-specific parameter count for sentence-transformers/all-MiniLM-L6-v2. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Primary upstream blobs checked do not contain checkpoint-scoped numeric benchmark tables, figures, or named locators for this exact checkpoint. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Evidence gap: The checked primary blobs do not provide an explicit runtime/default truncation numeric value in the README examples; tokenizer_config.json reports model_max_length = 512 while README examples show truncation=True without a stated default length. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- Evidence gap: The checked primary blobs do not document an authoritative mapping proving the Forge serving variant sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9 corresponds to an unchanged upstream checkpoint; confirm with an immutable serving-to-upstream mapping or Forge operator documentation. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2, https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md

### Safety

- Forge policy: Do not treat this embedding model as validated for clinical, diagnostic, or other high-stakes decision-making without domain-specific expert review and downstream validation.
- Forge policy: Review privacy and legal risks before embedding sensitive, proprietary, or regulated text because the checked upstream blobs do not provide checkpoint-specific guidance for such data handling.
- Evidence gap: The checked primary blobs do not include a repository LICENSE blob within the provided findings; the model-weight versus code-license distinction is not reported in the checked primary sources. Sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### all-MiniLM-L6-v2 model card

- URL: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- Publisher: sentence-transformers / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card page for the exact checkpoint named in scope; contains usage text, example code, and high-level claims about embedding dimensionality and intended uses.
- Scope: sentence-transformers/all-MiniLM-L6-v2 upstream model card
- Supports: identity.upstreamName
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.acceptedFormats
- Supports: outputInterpretation.outputs
- Supports: outputInterpretation.interpretation
- Supports: inputPreparation.taskSpecificFormatting
- Supports: inputPreparation.preprocessing

### README.md (blame main)

- URL: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Publisher: sentence-transformers / Hugging Face
- Type: `repository`
- Primary because: Repository README blame view for the exact checkpoint containing pooling documentation, fine-tuning provenance, and example code snippets.
- Scope: sentence-transformers/all-MiniLM-L6-v2 upstream README (blame main)
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation.outputs
- Supports: recommendedUseCases
- Supports: limitations
- Supports: researchSummary
- Supports: avoidUseCases

### README.md (blame a6ee86b5ff...)

- URL: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/a6ee86b5ffddbfd5bfb2cc7f96f357d8cd094cde/README.md
- Publisher: sentence-transformers / Hugging Face
- Type: `repository`
- Primary because: Commit-specific blame view of the README referenced in the checked findings; documents training-data listings and related README details present in the findings.
- Scope: sentence-transformers/all-MiniLM-L6-v2 upstream README (commit-blame)
- Supports: researchSummary
- Supports: limitations
- Supports: recommendedUseCases

### tokenizer_config.json (blob main)

- URL: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json
- Publisher: sentence-transformers / Hugging Face
- Type: `repository`
- Primary because: Commit/branch tokenizer_config.json blob for the exact checkpoint; contains tokenizer_class, do_lower_case, model_max_length, and special-token entries used in the research findings.
- Scope: sentence-transformers/all-MiniLM-L6-v2 upstream tokenizer configuration (blob main)
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: limitations
- Supports: avoidUseCases

## Evidence gaps

- Evidence gap: No checkpoint-specific numeric benchmark table, figure, section, or named locator was found in the checked primary sources; checked locators include the model card and README (blame) but contain no checkpoint-scoped numeric comparisons. Checked URLs: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 ; https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Evidence gap: No checkpoint-specific parameter count was reported in the checked primary findings; checked locators include the model card and README (blame) but no parameter count was present. Checked URLs: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 ; https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Evidence gap: Effective default runtime truncation length is not explicitly stated in the checked README examples (which show truncation=True) while tokenizer_config.json reports model_max_length = 512. The checked primary blobs do not resolve a numeric default truncation value. Checked URLs/paths: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 (README examples) ; https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/tokenizer_config.json (model_max_length)
- Evidence gap: No authoritative mapping in the checked primary findings demonstrates that the Forge serving variant sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9 serves an unchanged upstream checkpoint; confirm with Forge-serving immutable manifest or operator documentation. Checked upstream locators: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 ; https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md
- Evidence gap (comparisons): No verifiable task- and protocol-specific checkpoint-scoped numeric head-to-head comparisons between sentence-transformers/all-MiniLM-L6-v2 and nreimers/MiniLM-L6-H384-uncased were found in the checked primary blobs. Checked URLs: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 ; https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blame/main/README.md

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 44 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[3] uses forbidden secondary URL https: $.sources[3] uses forbidden secondary URL https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/66 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/34 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/145 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/70 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/154/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary host medium.com: $.sources[11] uses forbidden secondary host medium.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'praveenku32k' for this exact model scope: $.sources[13] uses unapproved repository owner 'praveenku32k' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses unapproved repository owner 'embeddings-benchmark' for this exact model scope: $.sources[15] uses unapproved repository owner 'embeddings-benchmark' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses unapproved repository owner 'beir-cellar' for this exact model scope: $.sources[17] uses unapproved repository owner 'beir-cellar' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'zenml' for this exact model scope: $.sources[18] uses unapproved repository owner 'zenml' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20] uses forbidden secondary host ollama.com: $.sources[20] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20].primary must be true: $.sources[20].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://zenml/finetuned-all-MiniLM-L6-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-base-en-v1.5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
