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

- Research key: `huggingface-co-microsoft-fara-7b-4338ec0f1a`
- Independent audit: `revised`
- Researched: `2026-08-06T12:42:48.138635+00:00`

Upstream primary sources (the Hugging Face model card README and the Microsoft Research technical PDF, plus the official GitHub repository and tokenizer metadata) consistently report that Fara-7B is a 7 billion parameter multimodal decoder-only model that accepts screenshots and text context and emits text containing chains-of-thought and tool-call/action blocks. Production baselines leverage Qwen 2.5‑VL (7B). Context-length is asserted as 128k tokens in the README and supported by the tokenizer_config model_max_length = 131072. Reported benchmark scores (WebVoyager 73.5, Online‑Mind2Web 34.1, DeepShop 26.2, WebTailBench 38.4; WebTailBench Process 48.8 and Outcome 24.1 reported elsewhere) appear in the Hugging Face README and repository artifacts; repository webeval docs describe where per-run score files are stored (runs/<benchmark>/<model>/.../scores/...). The canonical primary sources do not publish an immutable checkpoint identifier (exact checkpoint filename, SHA, or checksum) for the Forge-serving runtime label microsoft-fara-7b-vllm-cuda13, nor do they publish explicit low-level preprocessing details (tokenizer binary/release version beyond tokenizer_config entries, image resizing/normalization numeric parameters, or exact input tensor shapes) or a concrete vLLM wrapper runtime prompt template or serialized tool-call schema for the named Forge runtime. Benchmarks in the README/repository are supported as upstream-checkpoint evidence; the repository webeval paths indicate score storage and judge usage but the checked table and repository files do not contain full per-agent protocol metadata in the same table row, yielding protocol-matching caveats documented below.

## Identity

- Upstream name: Qwen 2.5‑VL (7B)
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 7B
- Architecture/head: multimodal decoder-only language model that takes an image (screenshot) plus text context and directly predicts thoughts and actions with grounded arguments
- License: model-weights: MIT; code: not reported
- Evidence: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://github.com/microsoft/fara

## Selection

### Recommended

- **Automated web / computer‑use assistance tasks (searching for information, shopping, booking reservations) when a human supervises or authorizes actions.** — Hugging Face README and the MSR technical PDF describe Fara-7B as designed specifically for computer-use agent tasks, emitting action tokens such as visit_url and web_search and predicting actions with arguments; both sources recommend human oversight for critical operations.
  Scope: Upstream checkpoint: Fara-7B (7B) as described in the Hugging Face README and MSR PDF (upstream-checkpoint evidence).
  Evidence: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf

### Conditional

- **Actionable automation that performs critical operations (e.g., logging in, making purchases) only with explicit human-in-the-loop confirmation.** — Require enforcement of a runtime human-confirmation gating step before executing any action that requires credentials, payments, or irreversible changes; the upstream sources describe Critical Point recognition and recommend human confirmation at such points but do not publish an explicit runtime enforcement API or vLLM wrapper template for the Forge runtime.
  Scope: Upstream checkpoint: Fara-7B (7B) as described in the Hugging Face README and MSR PDF (upstream-checkpoint evidence).
  Evidence: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

### Avoid

- **Unsupervised autonomous actions involving sensitive credentials or financial transactions without human oversight.** — Upstream documentation explicitly recommends human-in-the-loop monitoring and Critical Point halting for operations that involve personal data or consent; sources advise against submitting passwords or sensitive information to the model.
  Scope: Upstream checkpoint: Fara-7B (7B) as described in the MSR PDF and Hugging Face README (upstream-checkpoint evidence).
  Evidence: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

## Input preparation

### Semantic inputs

- Inputs are the user goal (text), current screenshot(s) (image), and the history of previous outputs (thoughts + actions text). Sources: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf
- The model accepts an image (screenshot) and text context as inputs and produces text outputs containing chains-of-thought and tool-call blocks. Sources: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf

### Accepted formats

- Accepted modalities: images (screenshots) and text context; pipeline tag and model-card metadata identify the pipeline as image-text-to-text and vision-enabled. Sources: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://huggingface.co/microsoft/Fara-7B

### Preprocessing

- Context length: 128k tokens is reported in the Hugging Face README; tokenizer_config in the model metadata sets model_max_length = 131072 which corresponds to the reported 128k context claim. Sources: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://huggingface.co/microsoft/Fara-7B/blame/refs%2Fpr%2F8/tokenizer_config.json
- Evidence gap: low-level preprocessing, tokenization special-token semantics beyond the tokenizer_config entries, exact tokenizer software version, image resizing/normalization numeric parameters, and exact input tensor shapes are not specified in the checked primary sources.

### Pre-submit validation

- Inputs that include sensitive credentials or require authentication should not be submitted; upstream sources recommend human oversight and caution about sharing passwords or sensitive information. Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Evidence gap: explicit automated input validation rules (e.g., maximum image size in pixels, accepted image encodings, exact tokenization method beyond tokenizer_config, or numeric bounds) are not present in the checked primary sources.

### Task-specific formatting

- Evidence gap: no explicit prompt template, exact paired-input order examples, or a serialized tool-call schema for a Forge vLLM wrapper (microsoft-fara-7b-vllm-cuda13) were found in the checked primary sources.

## Output interpretation

### Outputs

- Model outputs are generated text containing a chain-of-thought block followed by a tool-call block indicating the action (examples of actions include visit_url, web_search, history_back, pause_and_memorize_fact, wait, terminate, and discrete input/mouse actions). Sources: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md, https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf

### Interpretation

- Outputs should be interpreted as model-generated thoughts plus explicit action/tool-call suggestions; actions are not authoritative and require human verification before execution. Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf

### Post-inference validation

- Post-inference validation must include human review of any proposed action prior to execution; upstream sources recommend keeping a human in the loop and halting actions at critical points if necessary. Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Evidence gap: no formalized output validation checklist (e.g., confidence scores, explicit action-to-API mapping, or a published tool-call schema serialization for the Forge vLLM wrapper) was found in the checked primary sources.

## Public benchmarks

### Web browsing / agentic computer-use evaluation

- Dataset/split: WebVoyager / not reported
- Metric/value: success rate (score aggregated as reported in README table; higher-is-better) / 73.5 (`higher-is-better`)
- Model scope: Fara-7B (7B) as reported in the Hugging Face README benchmark table (upstream-checkpoint evidence)
- Conditions: Benchmark scores reported in the Hugging Face README table and described as averaged over three runs; repository webeval docs show per-run JSON score files under runs/<benchmark>/<model>/.../scores/ but per-agent prompting/evaluation protocol details are not enumerated in the same README table row.
- Source: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Locator: README.md — 'Benchmarks' table (table rows reporting WebVoyager score)
- Caveat: Repository README table reports comparative scores but does not include full per-agent protocol metadata (prompt templates, exact split definitions, or downstream head details) in the same table row; use as upstream-checkpoint evidence only.
- Caveat: Per-run score storage and judge usage are described in webeval/README.md (runs/<benchmark>/<model>/.../scores/gpt_eval.json) which documents judge verdict parsing but not the per-agent prompt templates in the benchmark table row.

### Web browsing / agentic computer-use evaluation

- Dataset/split: Online-Mind2Web / not reported
- Metric/value: success rate (score aggregated as reported in README table; higher-is-better) / 34.1 (`higher-is-better`)
- Model scope: Fara-7B (7B) as reported in the Hugging Face README benchmark table (upstream-checkpoint evidence)
- Conditions: Scores reported in the Hugging Face README table and averaged over three runs per the README; repository webeval docs point to JSON evaluation files for per-run verdicts but the README table lacks full per-agent protocol metadata.
- Source: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Locator: README.md — 'Benchmarks' table (table rows reporting Online-Mind2Web score)
- Caveat: Per-agent prompting/evaluation protocol details required for strict protocol-matched comparisons are not present in the same README table row; repository webeval documentation describes score file locations but not the exact prompt templates in-table.

### WebTailBench v1.5

- Dataset/split: WebTailBench v1.5 / Process
- Metric/value: process success rate (as reported in repository/paper; higher-is-better) / 48.8 (`higher-is-better`)
- Model scope: Fara-7B (7B) as reported in the repository and README (upstream-checkpoint evidence)
- Conditions: WebTailBench v1.5 Process score is reported in the README table and in repository-linked materials; repository webeval/README.md documents per-run score file locations but the README table lacks per-row protocol metadata (prompt templates, judge configuration) needed for exact protocol matching.
- Source: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Locator: README.md — 'Benchmarks' table (table rows reporting WebTailBench v1.5 Process score)
- Caveat: Repository/paper table does not include full per-row protocol metadata for direct comparability (prompt templates, split-definition manifest, or downstream head descriptions) in the same table row.
- Caveat: webeval/README.md documents where per-run scores are stored (runs/<benchmark>/<model>/.../scores/), which supports upstream-checkpoint provenance but does not negate the missing per-agent protocol metadata in the summary table row.

### WebTailBench v1.5

- Dataset/split: WebTailBench v1.5 / Outcome
- Metric/value: outcome success rate (as reported in repository/paper; higher-is-better) / 24.1 (`higher-is-better`)
- Model scope: Fara-7B (7B) as reported in the repository and README (upstream-checkpoint evidence)
- Conditions: Outcome score reported in the README table and associated repository materials; per-run score storage is described in webeval docs but the README table lacks detailed per-agent protocol metadata required for strict protocol-matched comparisons.
- Source: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Locator: README.md — 'Benchmarks' table (table rows reporting WebTailBench v1.5 Outcome score)
- Caveat: Exact per-agent evaluation protocol details (prompt templates, judge prompts, random seeds) are not enumerated in the same README table row; treat the reported numbers as upstream-checkpoint benchmark references only.

## Comparisons

### GPT‑5 — `insufficient-evidence`

- Task: Web browsing / agentic computer-use evaluation (repository benchmark table)
- Criteria: The repository/README table lists comparative scores for multiple agents (including GPT‑5) but does not present per-agent prompting/evaluation protocol metadata (prompt templates, exact split definitions, downstream head descriptions) in the same table row to support a protocol-matched preference.
- Rationale: Primary-source benchmark table provides comparative scores but lacks the per-agent protocol details necessary for a decisive, protocol-matched comparison.
- Comparison conditions: Checked README benchmark table and repository webeval docs; per-run score storage is documented, but per-agent protocol templates and split manifests are not included in the same summary table row.
- Evidence: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

### Gemini 2.5 Computer Use — `insufficient-evidence`

- Task: Web browsing / agentic computer-use evaluation (repository benchmark table)
- Criteria: Same as above: repository table lists scores for Gemini 2.5 Computer Use alongside Fara-7B but lacks per-agent protocol alignment information in-table.
- Rationale: Absence of per-agent prompt templates and split-definition metadata in the primary-source table prevents a protocol-matched selection.
- Comparison conditions: Checked README benchmark table and repository webeval docs; per-agent protocol details are not present in the checklist table row.
- Evidence: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

### OpenAI Operator — `insufficient-evidence`

- Task: Web browsing / agentic computer-use evaluation (repository benchmark table)
- Criteria: Repository table shows comparative scores but lacks per-agent evaluation protocol detail in the same table row.
- Rationale: Primary-source comparative table omits per-agent prompt and judge configuration metadata required for protocol-matched comparison.
- Comparison conditions: Checked README benchmark table and webeval docs; per-agent prompting and split manifests are not present in the README table row.
- Evidence: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

### Yutori Navigator — `insufficient-evidence`

- Task: Web browsing / agentic computer-use evaluation (repository benchmark table)
- Criteria: Repository lists many agents including Yutori Navigator with scores but does not provide per-agent prompting and split metadata in the summary table row.
- Rationale: Missing per-agent protocol specifications in the primary-source table prevent a protocol-matched preference.
- Comparison conditions: Checked README benchmark table and repository webeval documentation; per-agent protocol metadata absent in table row.
- Evidence: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

### GUI‑Owl‑1.5 — `insufficient-evidence`

- Task: Web browsing / agentic computer-use evaluation (repository benchmark table)
- Criteria: Same limitation: lack of per-agent protocol metadata in the README/repository summary table.
- Rationale: Cannot perform protocol-matched selection without per-agent prompt/judge/split details in the primary-source table row.
- Comparison conditions: Checked README benchmark table and webeval docs; per-agent protocol details are not in the summary table row.
- Evidence: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

### Holo2 — `insufficient-evidence`

- Task: Web browsing / agentic computer-use evaluation (repository benchmark table)
- Criteria: Summary table lists Holo2 scores but lacks the necessary per-agent protocol metadata for definitive head-to-head decisions.
- Rationale: Primary-source table does not include prompt templates, split definitions, or downstream head descriptions per agent in the same row.
- Comparison conditions: Checked README benchmark table and repository webeval docs; missing per-agent protocol details.
- Evidence: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md

## Limitations and safety

### Limitations

- Fara‑7B is designed as an agentic small language model for computer use and developing a comprehensive framework for human‑agent collaboration remains an open challenge. Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf
- The MSR PDF and Hugging Face README do not include a formalized Acceptable Use Policy document or a named policy URL in the checked primary sources. Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Evidence gap: precise low-level preprocessing and runtime input encoding details (exact tokenizer software release version, numeric image resize/normalization parameters, and exact input tensor shapes) are not documented in the checked primary sources.

### Safety

- Keep a human in the loop: upstream sources recommend human oversight and that the model should hand over control at Critical Points (e.g., logging in, making purchases). Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Do not share passwords or other sensitive credentials with the model; upstream documentation explicitly advises against submitting such data. Sources: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf, https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Evidence gap: a named Acceptable Use Policy (AUP) URL or formal AUP document is not present in the checked primary sources.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face — microsoft/Fara-7B (model root)

- URL: https://huggingface.co/microsoft/Fara-7B
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model hosting page for Fara-7B (canonical model-card root URL as provided by the project).
- Scope: Fara-7B upstream model hosting page (model-card root)
- Supports: canonical model hosting location for Fara-7B
- Supports: entry point for model README, sample usage and commit history
- Supports: high-level model description and metadata

### Hugging Face — microsoft/Fara-7B README (blob)

- URL: https://huggingface.co/microsoft/Fara-7B/blob/main/README.md
- Publisher: Hugging Face (model card README blob)
- Type: `model-card`
- Primary because: Model README.md on the official Hugging Face model repository contains model metadata (parameter scale, multimodal description, context length, license) used as primary upstream-checkpoint documentation and contains the benchmark table referenced in findings.
- Scope: Upstream Fara-7B README (model-card blob)
- Supports: 7B parameter scale
- Supports: multimodal decoder-only description
- Supports: context length claim (128k)
- Supports: MIT model-weight license claim
- Supports: inputs: user goal, screenshots, history
- Supports: benchmarks table with reported scores (WebVoyager, Online-Mind2Web, DeepShop, WebTailBench)
- Supports: safety guidance and Critical Point recommendations

### MSR publication PDF — Fara‑7B: An Efficient Agentic Model for Computer Use

- URL: https://microsoft.com/en-us/research/wp-content/uploads/2025/11/Fara-7B-An-Efficient-Agentic-Model-for-Computer-Use.pdf
- Publisher: Microsoft Research
- Type: `paper`
- Primary because: Canonical Microsoft Research technical publication PDF describing Fara-7B architecture, experiments, safety guidance, and action types.
- Scope: MSR technical report / paper describing upstream Fara-7B checkpoint and experiments
- Supports: 7B parameter scale
- Supports: multimodal decoder-only model taking image + text
- Supports: Critical Point recognition and safety guidance
- Supports: training resources statement referenced in README
- Supports: list of supported action types and inference history behavior

### Official GitHub repository — microsoft/fara

- URL: https://github.com/microsoft/fara
- Publisher: GitHub / Microsoft
- Type: `repository`
- Primary because: Official project repository containing code, benchmark artifacts, and evaluation framework used by the project authors.
- Scope: Repository root for project artifacts and benchmark orchestration
- Supports: repository artifacts and benchmark table references
- Supports: code, LICENSE, and project files
- Supports: links to evaluation framework and run-level score storage

### Hugging Face tokenizer metadata (blame view) — tokenizer_config.json

- URL: https://huggingface.co/microsoft/Fara-7B/blame/refs%2Fpr%2F8/tokenizer_config.json
- Publisher: Hugging Face (model metadata blob)
- Type: `model-card`
- Primary because: Tokenization/configuration metadata published alongside the model that documents model_max_length and special tokens used by the model.
- Scope: tokenizer_config.json entry in Hugging Face model metadata
- Supports: model_max_length = 131072
- Supports: definitions of eos_token and pad_token and enumerated special tokens
- Supports: tokenizer_class and processor_class entries

### Repository — webeval evaluation README (score storage and judge description)

- URL: https://github.com/microsoft/fara/blob/main/webeval/README.md
- Publisher: GitHub / Microsoft
- Type: `repository`
- Primary because: Repository subpath documenting evaluation framework, per-run directory structure, and score file locations used to store judge verdicts and numeric scores.
- Scope: webeval evaluation framework documentation in repository
- Supports: description of runs/<benchmark>/<model>/.../traj/ directory structure
- Supports: locations and file names for per-run score files (e.g., scores/gpt_eval.json, OnlineMind2Web_eval-3.json)
- Supports: description of judge parsing for converting verdicts to numeric scores

## Evidence gaps

- Evidence gap: No immutable checkpoint identifier (e.g., model file SHA, exact checkpoint file name, or trained-weight checksum) is reported for the Forge variant microsoft-fara-7b-vllm-cuda13 in the checked primary sources.
- Evidence gap: The exact relationship between the Forge-serving runtime label 'microsoft-fara-7b-vllm-cuda13' (vllm-0.21.0-cuda13-vision-chat-probe) and an unchanged upstream checkpoint is not documented in the checked primary sources; no explicit statement proving the vLLM wrapper serves an unchanged upstream checkpoint was found.
- Evidence gap: Low-level preprocessing and input-encoding details (full tokenizer software release/version, special-token semantics beyond the tokenizer_config entries, image resizing/normalization numeric parameters, and exact input tensor shapes) are not present in the checked primary sources.
- Evidence gap: No explicit runtime prompt templates, exact paired-input order examples, or serialized tool-call schema for the Forge vLLM wrapper (microsoft-fara-7b-vllm-cuda13) were found in the checked primary sources.
- Evidence gap: The repository benchmark table and the Hugging Face README summary table do not include full per-agent protocol metadata (prompt templates, judge prompts, split-definition manifests, or downstream head descriptions) in the same table row required for strict protocol-matched external comparisons.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 44 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property avoidUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property conditionalUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property inputPreparation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property recommendedUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/microsoft/Fara-7B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Fara-7B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://microsoft.com/en-us/research/publication/fara-7b-an-efficient-agentic-model-for-computer-use Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://microsoft.com/en-us/research?p=1156495 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/microsoft/fara Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Fara-7B/commit/66dc2c7305da0b86cfee77244d0c40748912efb9 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Fara-7B/discussions/7 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases must contain at least one scoped item: $.recommendedUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs is empty without a section-specific evidence gap: $.inputPreparation.semanticInputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
