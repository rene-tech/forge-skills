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

- Research key: `huggingface-co-qwen-qwen3-1-7b-71ce940ab7`
- Independent audit: `revised`
- Researched: `2026-08-06T09:11:38.461497+00:00`

This dossier covers the upstream checkpoint named Qwen3-1.7B. Primary upstream facts available in canonical sources: the Hugging Face model page is the canonical repository entry for Qwen3-1.7B and includes chat templates and recommended sampling parameters; the repository LICENSE blob shows an Apache‑2.0 license and copyright attribution; the GitHub qwenLM/qwen3 repository and the Qwen3 technical report (arXiv:2505.09388) provide family‑level architecture and design details (Grouped‑Query Attention, SwiGLU, RoPE, RMSNorm); the Hugging Face checkpoint config.json provides checkpoint‑level parameters (28 layers, 16 attention heads, 8 key/value heads, hidden/intermediate sizes, vocab size, and max_position_embeddings = 40,960). Official Qwen ReadTheDocs pages provide tokenization/control‑token conventions and runtime throughput (speed_benchmark) measurements. Where canonical primary sources disagree or do not publish an authoritative single statement required by the dossier (immutable checkpoint revision hash, single authoritative maximum context length, formal logits/probability output contract, and explicit decoding defaults as an upstream contract), those gaps are recorded in evidenceGaps and referenced to the inspected canonical pages.

## Identity

- Upstream name: Qwen3-1.7B
- Checkpoint/version: Qwen3-1.7B
- Immutable revision: not reported
- Parameter scale: 1.7 billion parameters
- Architecture/head: 28 transformer layers; Grouped‑Query Attention (16 query heads, 8 key/value heads); hidden_size 2048; intermediate_size 6144; head_dim 128; RoPE (large theta), SwiGLU activation family, RMSNorm (pre‑norm); causal autoregressive (next‑token) text generation head. (Checkpoint‑level config.json values combined with family technical-report architecture notes.)
- License: Apache License, Version 2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-1.7B, https://huggingface.co/Qwen/Qwen3-1.7B/blob/main/LICENSE, https://github.com/qwenLM/qwen3, https://arxiv.org/abs/2505.09388, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html, https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html, https://huggingface.co/Qwen/Qwen3-1.7B/blame/main/config.json

## Selection

### Recommended

- **Chat and instruction‑style conversational interfaces that follow the Qwen message/chat template** — The Hugging Face model card for Qwen3-1.7B provides a chat template and lists recommended sampling parameters for thinking and non‑thinking modes, indicating the model is intended for chat/instruction-style use.
  Scope: Qwen3-1.7B
  Evidence: https://huggingface.co/Qwen/Qwen3-1.7B

### Conditional

- **High‑throughput or latency‑sensitive deployments using quantized runtimes (validate quantization and runtime conditions before deployment)** — Verify exact quantization method, runtime harness, and single‑GPU conditions in your environment because reported throughput numbers are conditioned on the Qwen official benchmark harness and quantization configuration.
  Scope: Qwen3-1.7B (runtime throughput reported in Qwen speed benchmark)
  Evidence: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- **Using thinking‑mode / chain‑of‑thought style prompts** — Enable and validate thinking‑mode behavior in your serving stack and confirm decoding hyperparameters in your runtime; upstream documentation documents thinking mode and provides recommended sampling parameters but does not provide an immutable runtime contract.
  Scope: Qwen3-1.7B (thinking‑mode support documented in model card and Qwen docs)
  Evidence: https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html

### Avoid

- **Assuming a specific immutable checkpoint revision or commit ID for reproducibility** — Evidence gap: No immutable checkpoint revision hash, exact model file SHA, or commit identifier for the Qwen3-1.7B model file was found in the inspected canonical sources (Hugging Face model page and GitHub repository).
  Scope: Qwen3-1.7B
  Evidence: https://huggingface.co/Qwen/Qwen3-1.7B, https://github.com/qwenLM/qwen3
- **Assuming upstream provides a calibrated logits/probability output contract or confidence scores without instrumentation** — Evidence gap: No primary‑source specification of a logits/probability output contract or calibrated confidence scores was found in the inspected canonical sources.
  Scope: Qwen3-1.7B
  Evidence: https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html, https://github.com/qwenLM/qwen3

## Input preparation

### Semantic inputs

- Single‑modality text inputs (chat‑style message sequences framed with Qwen control tokens or templates). Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html
- Thinking‑mode content delimited by special thinking tokens (`<think>` and `</think>`) when thinking mode is used (dynamic mode switching documented in family technical report and Qwen docs). Sources: https://arxiv.org/abs/2505.09388, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html

### Accepted formats

- Chat/message format using the model card's chat template and control tokens as shown in the upstream model card and documentation. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html

### Preprocessing

- Byte‑pair/byte‑level BPE‑style tokenization (Qwen tokenization as described in Qwen docs) with the documented vocabulary size for the checkpoint. Sources: https://qwen.readthedocs.io/en/latest/getting_started/concepts.html, https://huggingface.co/Qwen/Qwen3-1.7B/blame/main/config.json

### Pre-submit validation

- When using long‑context inputs, validate that the chosen runtime supports the input length used (the official speed benchmark uses large input lengths; confirm runtime memory and tokenization behavior before production deployment). Sources: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html, https://huggingface.co/Qwen/Qwen3-1.7B/blame/main/config.json
- Verify inputs conform to the upstream chat/message framing conventions (control tokens and special tokens) before submission to the model. Sources: https://qwen.readthedocs.io/en/latest/getting_started/concepts.html, https://huggingface.co/Qwen/Qwen3-1.7B

### Task-specific formatting

- Use the chat template provided by the Hugging Face model card (the model card includes a chat template and sampling parameter examples). Sources: https://huggingface.co/Qwen/Qwen3-1.7B

## Output interpretation

### Outputs

- Primary output modality is generated text (assistant responses following chat template and control‑token framing). Sources: https://huggingface.co/Qwen/Qwen3-1.7B

### Interpretation

- Thinking‑mode blocks (when enabled) are delimited by `<think>`/`</think>` and should be interpreted by integrators according to application requirements; upstream documentation documents thinking mode but does not provide an immutable decoding contract. Sources: https://arxiv.org/abs/2505.09388, https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html
- No canonical primary‑source specification of calibrated probabilities or an upstream confidence API was found in the inspected canonical sources; do not assume a calibrated confidence signal is provided by the checkpoint without instrumentation. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html

### Post-inference validation

- Post‑inference validation should include sanity checks (response present within expected token budget, expected thinking markers when enabled) and explicit runtime checks for memory/throughput when using long contexts. Sources: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html, https://huggingface.co/Qwen/Qwen3-1.7B
- If downstream use requires calibrated probabilities, instrument the runtime to export logits and perform separate calibration and evaluation; no upstream calibration procedure was found in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://github.com/qwenLM/qwen3

## Public benchmarks

### Throughput (tokens/sec) - SGLang benchmark

- Dataset/split: SGLang benchmark (runtime throughput tests) / input_length=1 token (single-GPU)
- Metric/value: tokens per second / BF16: 227.80; FP8: 333.90; GPTQ-Int8: 257.40 (`higher-is-better`)
- Model scope: Qwen3-1.7B measured on SGLang benchmark with BF16, FP8, GPTQ-Int8 quantizations (single GPU)
- Conditions: Quantization method specified (BF16/FP8/GPTQ-Int8); single GPU; input_length=1 as used by the official SGLang rows.
- Source: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- Locator: speed_benchmark.html — SGLang throughput table, row input_length=1 (columns BF16 / FP8 / GPTQ-Int8)
- Caveat: This is a runtime throughput benchmark under specified quantizations and input lengths, not an ML quality benchmark.
- Caveat: Results are conditioned on single‑GPU execution and the specific benchmark harness used by Qwen docs.

### Throughput (tokens/sec) - SGLang benchmark

- Dataset/split: SGLang benchmark (runtime throughput tests) / input_length=6144 tokens (single-GPU)
- Metric/value: tokens per second / BF16: 838.28; FP8: 1,198.20; GPTQ-Int8: 945.91 (`higher-is-better`)
- Model scope: Qwen3-1.7B measured on SGLang benchmark with BF16, FP8, GPTQ-Int8 quantizations (single GPU)
- Conditions: Quantization method specified (BF16/FP8/GPTQ-Int8); single GPU; input_length=6144 as used by the official SGLang rows.
- Source: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- Locator: speed_benchmark.html — SGLang throughput table, row input_length=6144 (columns BF16 / FP8 / GPTQ-Int8)
- Caveat: Runtime throughput numbers depend on the benchmark harness and quantization method used by Qwen docs.

### Throughput (tokens/sec) - SGLang benchmark

- Dataset/split: SGLang benchmark (runtime throughput tests) / input_length=14336 tokens (single-GPU)
- Metric/value: tokens per second / BF16: 1,525.71; FP8: 2,095.61; GPTQ-Int8: 1,707.63 (`higher-is-better`)
- Model scope: Qwen3-1.7B measured on SGLang benchmark with BF16, FP8, GPTQ-Int8 quantizations (single GPU)
- Conditions: Quantization method specified; single GPU; input_length=14336 as used by the official SGLang rows.
- Source: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- Locator: speed_benchmark.html — SGLang throughput table, row input_length=14336 (columns BF16 / FP8 / GPTQ-Int8)
- Caveat: Reported throughput scales with input length and quantization; not a measure of model accuracy.

### Throughput (tokens/sec) - SGLang benchmark

- Dataset/split: SGLang benchmark (runtime throughput tests) / input_length=30720 tokens (single-GPU)
- Metric/value: tokens per second / BF16: 2,439.03; FP8: 3,165.32; GPTQ-Int8: 2,706.16 (`higher-is-better`)
- Model scope: Qwen3-1.7B measured on SGLang benchmark with BF16, FP8, GPTQ-Int8 quantizations (single GPU)
- Conditions: Quantization method specified; single GPU; input_length=30720 as used by the official SGLang rows.
- Source: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- Locator: speed_benchmark.html — SGLang throughput table, row input_length=30720 (columns BF16 / FP8 / GPTQ-Int8)
- Caveat: Large‑input throughput numbers show the model's long‑context runtime behavior but not ML task performance.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Ambiguity across primary sources for maximum supported context length and related runtime usages; inspect and validate in your runtime. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://huggingface.co/Qwen/Qwen3-1.7B/blame/main/config.json, https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- No canonical, single immutable checkpoint revision hash or model file SHA was published in the inspected canonical sources; integrators requiring immutable artifacts should obtain and record file digests at download time. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://github.com/qwenLM/qwen3
- Upstream primary sources do not provide a formal logits/probability output contract or calibrated confidence API for this checkpoint; downstream instrumentation is required for calibrated probabilities. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html
- Official decoding hyperparameter recommendations for thinking and non‑thinking modes are provided as examples (model card) but do not constitute an immutable upstream runtime contract; integrators should validate defaults in their serving environment. Sources: https://huggingface.co/Qwen/Qwen3-1.7B

### Safety

- Evidence gap: The inspected canonical primary sources (Hugging Face model card, GitHub repository, Qwen technical report, and Qwen ReadTheDocs) do not publish an explicit, standalone safety policy or domain‑specific handling guidance for sensitive data; treat the model as requiring downstream validation and expert review for safety‑critical or sensitive uses. Sources: https://huggingface.co/Qwen/Qwen3-1.7B, https://github.com/qwenLM/qwen3, https://arxiv.org/abs/2505.09388, https://qwen.readthedocs.io/en/latest/getting_started/concepts.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-1.7B — Hugging Face model card

- URL: https://huggingface.co/Qwen/Qwen3-1.7B
- Publisher: Qwen (Hugging Face repository)
- Type: `model-card`
- Primary because: Official Hugging Face repository and model card for the Qwen3-1.7B checkpoint; contains the checkpoint model card, chat template, and sampling recommendations.
- Scope: Qwen3-1.7B model card / upstream checkpoint page
- Supports: Model card provides chat template and recommended sampling parameters for thinking/non‑thinking modes.
- Supports: Model card is the canonical Hugging Face checkpoint page for Qwen3-1.7B and the starting point for checkpoint artifacts.

### Qwen3-1.7B LICENSE file — Hugging Face

- URL: https://huggingface.co/Qwen/Qwen3-1.7B/blob/main/LICENSE
- Publisher: Qwen (Hugging Face repository)
- Type: `official-documentation`
- Primary because: Official license file published in the Hugging Face model repository for the Qwen3-1.7B checkpoint.
- Scope: Qwen3-1.7B license
- Supports: Qwen3-1.7B is released under the Apache License, Version 2.0, with the LICENSE blob showing the copyright string.

### Qwen3 repository — GitHub

- URL: https://github.com/qwenLM/qwen3
- Publisher: qwenLM (GitHub)
- Type: `repository`
- Primary because: Official Qwen3 project/source repository maintained by the Qwen team; provides family‑level code, links, and references.
- Scope: Qwen3 project repository (general Qwen3 family)
- Supports: Project repository lists Qwen3 family members and links to technical report/family resources.

### Qwen3 Technical Report — arXiv (arXiv:2505.09388)

- URL: https://arxiv.org/abs/2505.09388
- Publisher: Qwen Team (arXiv preprint)
- Type: `paper`
- Primary because: Canonical family‑level technical report describing architecture, grouped‑query attention, thinking mode, and other design elements referenced by the checkpoint.
- Scope: Qwen3 technical report (family-level technical details)
- Supports: Describes family architecture choices (Grouped Query Attention, SwiGLU, RoPE, RMSNorm, QK‑Norm) and thinking/non‑thinking mode framework.

### Qwen docs — Getting started / concepts

- URL: https://qwen.readthedocs.io/en/latest/getting_started/concepts.html
- Publisher: Qwen documentation (ReadTheDocs)
- Type: `official-documentation`
- Primary because: Official Qwen project documentation providing tokenization, control‑token semantics, and thinking‑mode description.
- Scope: Qwen tokenization and control‑token conventions (family-level)
- Supports: Documents Qwen tokenization approach (BPE), control tokens semantics, no unknown token behavior, and thinking mode descriptions.

### Qwen docs — Speed benchmark

- URL: https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html
- Publisher: Qwen documentation (ReadTheDocs)
- Type: `official-documentation`
- Primary because: Official Qwen documentation reporting runtime throughput and memory measurements under specified quantizations and input lengths for Qwen checkpoints.
- Scope: Qwen3-1.7B runtime benchmarks under BF16/FP8/GPTQ‑Int8 quantizations
- Supports: SGLang benchmark throughput numbers for Qwen3-1.7B across quantizations and multiple input lengths (input_length rows used in dossier).

### Qwen3-1.7B config.json (blame view) — Hugging Face

- URL: https://huggingface.co/Qwen/Qwen3-1.7B/blame/main/config.json
- Publisher: Qwen (Hugging Face repository)
- Type: `official-documentation`
- Primary because: Checkpoint config.json in the canonical Hugging Face repository for Qwen3-1.7B providing checkpoint‑level hyperparameters and tokenizer/vocabulary size entries.
- Scope: Qwen3-1.7B checkpoint configuration
- Supports: Specifies 28 hidden layers, 16 attention heads, 8 key/value heads, hidden_size 2048, intermediate_size 6144, head_dim 128, vocab_size 151,936, and max_position_embeddings 40,960 among other checkpoint parameters.

## Evidence gaps

- Evidence gap: No immutable checkpoint revision hash, exact model file SHA, or commit identifier for the Qwen3-1.7B model file was found in the inspected canonical sources (inspected: Hugging Face model page, Hugging Face repository files, GitHub repository).
- Evidence gap: Primary canonical sources inspected provide inconsistent numeric indications related to maximum supported context length: the checkpoint config.json indicates max_position_embeddings = 40,960 (https://huggingface.co/Qwen/Qwen3-1.7B/blame/main/config.json), the Hugging Face model card provides recommended maximum output lengths (https://huggingface.co/Qwen/Qwen3-1.7B) and the ReadTheDocs speed benchmark exercises input lengths up to 30,720 (https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html); a single authoritative maximum context‑length value for Qwen3-1.7B is not published unambiguously in one canonical primary source.
- Evidence gap: No canonical primary‑source specification of truncation/cropping policy (left/right/semantic) or exact overlength handling for inputs was found in the inspected canonical sources (inspected: Hugging Face model card, Qwen ReadTheDocs concepts, Qwen GitHub).
- Evidence gap: No canonical primary‑source publication of a logits/probability output contract, calibrated confidence scores, or a recommended calibration procedure for Qwen3-1.7B was found in the inspected canonical sources (inspected: Hugging Face model card, Qwen ReadTheDocs, Qwen GitHub, Qwen technical report).
- Evidence gap: While the Hugging Face model card provides example sampling parameters for thinking/non‑thinking modes, the inspected canonical sources do not define an immutable set of upstream default decoding hyperparameters as a formal contract for the checkpoint (inspected: Hugging Face model card).
- Evidence gap: Task‑level quality benchmarks (dataset/split/metric/protocol) published by the original creators specifically for the Qwen3-1.7B checkpoint were not located in the inspected canonical primary sources; available primary measurements in canonical sources are runtime throughput/memory benchmarks (inspected: Hugging Face model card, Qwen ReadTheDocs, Qwen GitHub, Qwen technical report).
- Evidence gap: Direct, primary‑source task‑level comparisons between Qwen3-1.7B and other Forge peer checkpoints under a shared protocol were not found in the inspected canonical sources (inspected: Hugging Face model card, Qwen ReadTheDocs, Qwen technical report, Qwen GitHub).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 17 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://qwenlm.github.io/blog/qwen3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary host ollama.com: $.sources[7] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary host ollama.com: $.sources[8] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary host ollama.com: $.sources[13] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.conditionalUseCasesCaveat: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCasesNotes: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisonsNotes: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisonsEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
