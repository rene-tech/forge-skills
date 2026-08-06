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

- Research key: `huggingface-co-qwen-qwen2-5-coder-7b-instruct-1fed2cd4d7`
- Independent audit: `revised`
- Researched: `2026-08-06T09:04:50.158582+00:00`

The verified checkpoint is Qwen/Qwen2.5-Coder-7B-Instruct: an instruction‑tuned 7B member of the Qwen2.5‑Coder series. Primary upstream evidence confirms the Qwen2.5‑Coder family is code-specialized, lists six mainstream model sizes including a 7B scale, and indicates an instruction‑tuned 7B repository exists. The supplied primary sources do not contain checkpoint-scoped numeric benchmark tables, tokenization implementation details, explicit runtime/API contract statements (logits/hidden-state access, sampling defaults, stop-token semantics), quantized artifact releases, or detailed evaluation protocols for code benchmarks; those absences are represented as explicit evidence gaps below.

## Identity

- Upstream name: Qwen/Qwen2.5-Coder-7B-Instruct
- Checkpoint/version: Qwen/Qwen2.5-Coder-7B-Instruct
- Immutable revision: not reported
- Parameter scale: 7B
- Architecture/head: Qwen2.5 architecture (Qwen2.5-Coder series)
- License: not reported
- Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

## Selection

### Recommended

- **Code generation (single-file and multi-file snippets)** — Primary evidence identifies the Qwen2.5‑Coder series as code-specialized and confirms an instruction‑tuned 7B checkpoint exists in the repository; therefore the instruct 7B checkpoint is presented upstream for code-focused instruction use.
  Scope: Qwen/Qwen2.5-Coder-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186
- **Code completion and code repair (with downstream validation)** — Primary sources present the Qwen2.5‑Coder series as code-focused and document the existence of an instruction‑tuned 7B checkpoint intended for instruction-style code tasks; checkpoint-scoped numeric protocol or performance details are not available in the supplied primary evidence and downstream validation is required.
  Scope: Qwen/Qwen2.5-Coder-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186
- **Instruction-following for developer workflows and agentic coding assistants** — The repository-level evidence and the technical report collectively document an instruction-tuned member of the Qwen2.5‑Coder family at the 7B scale, indicating upstream intent for instruction-following in code contexts.
  Scope: Qwen/Qwen2.5-Coder-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Conditional

- **Long-context / very-large-context repository-level reasoning** — Evidence gap: The primary sources inspected do not contain checkpoint-scoped claims or experiments about maximum context length, positional scaling, or recommended long-context serving configurations. Insist on upstream checkpoint-scoped documentation or validation experiments before relying on long-context behavior.
  Scope: Qwen/Qwen2.5-Coder-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186
- **Quantized deployments (GGUF/GPTQ/AWQ) for constrained hardware** — Evidence gap: The primary sources inspected do not report checkpoint-scoped released quantized artifacts or quantization performance numbers for the instruct 7B checkpoint. Any quantized deployment requires independent, task-specific validation against this exact checkpoint.
  Scope: Qwen/Qwen2.5-Coder-7B-Instruct (quantized variants)
  Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Avoid

- **Using an unmodified base 7B model for conversational/dialogue tasks without instruction tuning** — Evidence gap: The supplied primary findings do not contain an explicit upstream statement advising against conversational use of a base (non‑instruction‑tuned) 7B checkpoint, nor a checkpoint-scoped upstream comparison establishing such a caution. Only the instruction‑tuned 7B repository is confirmed upstream in the inspected sources.
  Scope: Qwen/Qwen2.5-Coder-7B (base) vs Qwen/Qwen2.5-Coder-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

## Input preparation

### Semantic inputs

- Accepts textual inputs including code and natural-language instructions (the instruct checkpoint is presented upstream for instruction-style code tasks). Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Accepted formats

- The Qwen2.5‑Coder repository is presented upstream as part of the Hugging Face model ecosystem and the series is described as code-specialized; the sources indicate the code is integrated with the Hugging Face transformers ecosystem. Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Preprocessing

- Evidence gap: The primary sources inspected do not provide checkpoint-scoped tokenizer implementation commands, exact tokenizer class names, vocabulary size, or explicit byte-level vs. other encoding details for Qwen/Qwen2.5-Coder-7B-Instruct. Inspected locations: the Hugging Face model card root page and the Qwen2.5‑Coder technical report (arXiv PDF). Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Pre-submit validation

- Evidence gap: The primary sources inspected do not present a checkpoint-scoped canonical input-validation checklist, JSON prompt key schema, or explicit required/forbidden input patterns for the instruct 7B checkpoint. Inspected locations: the Hugging Face model card root page and the Qwen2.5‑Coder technical report (arXiv PDF). Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Task-specific formatting

- Evidence gap: The primary sources inspected do not contain canonical prompt templates, role schemas (system/user/assistant), or explicit instruction-tuning prompt examples for the instruct 7B checkpoint. Inspected locations: the Hugging Face model card root page and the Qwen2.5‑Coder technical report (arXiv PDF). Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

## Output interpretation

### Outputs

- Primary output produced by the instruction-tuned decoder is generated text (code and natural language) for code-focused instruction tasks as presented upstream. Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Interpretation

- The technical report describes evaluation of the Qwen2.5‑Coder family at a series level and indicates improved general capabilities for code tasks; the inspected primary sources do not provide checkpoint-scoped calibrated confidence scores or recommended likelihood thresholds for outputs of the instruct 7B checkpoint. Sources: https://arxiv.org/pdf/2409.12186, https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct

### Post-inference validation

- Evidence gap: The primary sources inspected do not document token-level API contracts (logits/hidden-state access), sampling defaults, stop-token semantics, truncation/cropping policy, or batching behavior for the instruct 7B checkpoint. Inspected locations: the Hugging Face model card root page and the Qwen2.5‑Coder technical report (arXiv PDF). Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The Qwen2.5‑Coder series includes multiple model scales (0.5B, 1.5B, 3B, 7B, 14B, 32B) and the inspected primary sources confirm a 7B instruction-tuned repository exists; however, the primary sources do not include checkpoint-scoped numeric benchmark tables or extractable evaluation protocol rows for the instruct 7B checkpoint. Sources: https://arxiv.org/pdf/2409.12186, https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct
- Evidence gap: Evaluation protocol details required for comparability (sampling temperature, top-k/top-p, beam settings, random seeds, number-of-samples per prompt, exact prompt templates) are not present in the inspected primary locations for checkpoint-scoped numeric benchmarks. Sources: https://arxiv.org/pdf/2409.12186, https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct
- Evidence gap: Tokenizer implementation details (exact tokenizer class name, tokenizer initialization commands, vocabulary size, byte-level vs. other encoding specifics) for Qwen/Qwen2.5-Coder-7B-Instruct are not present in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186

### Safety

- Evidence gap: The inspected primary sources do not state the model-weight license or code license explicitly for the Qwen/Qwen2.5-Coder-7B-Instruct checkpoint at the checkpoint scope. Locations inspected: Hugging Face model card root page and the Qwen2.5‑Coder technical report (arXiv PDF). Sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct, https://arxiv.org/pdf/2409.12186
- Evidence gap: The inspected primary sources do not include explicit upstream guidance on clinical, biosecurity, or PHI handling for the instruct checkpoint; treat generated code and outputs as requiring downstream review for safety-sensitive or regulated contexts. Locations inspected: Hugging Face model card root page and the Qwen2.5‑Coder technical report (arXiv PDF). Sources: https://arxiv.org/pdf/2409.12186, https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen2.5-Coder-7B-Instruct (Hugging Face model card / README)

- URL: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct
- Publisher: Hugging Face (Qwen)
- Type: `model-card`
- Primary because: Canonical Hugging Face model card/repository root for the instruct checkpoint; establishes repository-level identity and the existence of an instruction-tuned 7B checkpoint.
- Scope: Qwen/Qwen2.5-Coder-7B-Instruct
- Supports: identity
- Supports: recommendedUseCases
- Supports: inputPreparation
- Supports: outputInterpretation
- Supports: limitations

### Qwen2.5-Coder Technical Report (arXiv PDF)

- URL: https://arxiv.org/pdf/2409.12186
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical technical report describing the Qwen2.5-Coder series, model scales, architecture basis, and high-level series capability claims used to ground family- and series-level statements.
- Scope: Qwen2.5-Coder series (includes Qwen2.5-Coder-7B-Instruct)
- Supports: identity
- Supports: researchSummary
- Supports: limitations

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric benchmark rows (dataset/split, metric, numeric value, and exact table/figure/section locator) for HumanEval, MBPP, BigCodeBench, CRUXEval, Aider, PASS@k, code-repair results, or other code benchmarks were found in the inspected primary sources. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: Evaluation protocol details required for comparability (sampling temperature, top-k/top-p, beam settings, random seeds, number-of-samples per prompt, exact prompt templates) are not present at the checkpoint scope in the inspected primary sources. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: Tokenizer implementation details (exact tokenizer class name, tokenizer initialization commands, vocabulary size, byte-level vs. other encoding specifics) for Qwen/Qwen2.5-Coder-7B-Instruct are not present in the inspected primary sources. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: Upstream API contract details (logits/hidden-state access, sampling defaults, stop-token semantics, truncation/cropping policy, batching behavior) for the instruct checkpoint are not present in the inspected primary sources. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: Checkpoint-scoped documentation or experiments for maximum supported context length or positional-scaling behavior for Qwen/Qwen2.5-Coder-7B-Instruct are not present in the inspected primary sources. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: Evidence of upstream-released quantized artifacts (GGUF/GPTQ/AWQ) or checkpoint-scoped quantization performance numbers for Qwen/Qwen2.5-Coder-7B-Instruct are not present in the inspected primary sources. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: The inspected primary sources do not explicitly state the model-weight license and separate code/license metadata at the checkpoint scope for Qwen/Qwen2.5-Coder-7B-Instruct. Inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap: No canonical prompt templates, role schemas, or instruction-format examples for the instruction-tuned 7B checkpoint were found at the inspected primary locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).
- Evidence gap (comparisons): The inspected primary sources do not provide checkpoint-scoped, protocol-matched numeric comparisons between Qwen/Qwen2.5-Coder-7B-Instruct and named alternative checkpoints with exact dataset/split/metric/row locators; inspected locations: Hugging Face model card root page (https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) and Qwen2.5‑Coder technical report (arXiv PDF, https://arxiv.org/pdf/2409.12186).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 23 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4] uses forbidden secondary host emergentmind.com: $.sources[4] uses forbidden secondary host emergentmind.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary host docs.vllm.ai: $.sources[5] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary host ollama.com: $.sources[9] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'unsloth' for this exact model scope: $.sources[10] uses unapproved repository owner 'unsloth' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary host hf-mirror.com: $.sources[11] uses forbidden secondary host hf-mirror.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/papers/2409.12186 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
