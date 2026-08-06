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

- Research key: `huggingface-co-stanford-crfm-biomedlm-e2a609d88c`
- Independent audit: `revised`
- Researched: `2026-08-06T13:39:55.934170+00:00`

This dossier is scoped to the upstream BioMedLM 2.7B checkpoint (stanford-crfm/BioMedLM). Primary-source evidence (Hugging Face model card, the arXiv preprint, Stanford CRFM project page, and the upstream repository artifacts) establishes that BioMedLM is a 2.7B GPT-2–style autoregressive model trained on biomedical text (PubMed abstracts and full-texts from The Pile), uses a tokenizer with vocabulary ≈28,896 and model_max_length 1024, and reports MedQA accuracy = 50.3% in the upstream model card/README. The available primary sources do not report a license for model weights or code, do not publish wrapper-specific benchmarks for any Forge wrapper variant, and do not provide exact MedMCQA or MMLU benchmark locators in the supplied findings. Where wrapper-to-upstream identity is not proven by primary evidence, this dossier retains claims as upstream-checkpoint evidence and records evidence gaps for wrapper identity and for unverified benchmark locators.

## Identity

- Upstream name: BioMedLM
- Checkpoint/version: BioMedLM 2.7B
- Immutable revision: not reported
- Parameter scale: 2.7B
- Architecture/head: GPT-2 style autoregressive transformer (32 layers, 20 attention heads, hidden size 2560; vocabulary size 28,896; context length 1024)
- License: not reported
- Evidence: https://huggingface.co/stanford-crfm/BioMedLM, https://arxiv.org/abs/2403.18421, https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/config.json, https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/tokenizer_config.json, https://crfm.stanford.edu/2022/12/15/biomedlm.html

## Selection

### Recommended

- **Biomedical text generation and biomedical question answering for research and evaluation (non-production).** — Primary sources describe BioMedLM as a 2.7B GPT-style model trained on PubMed abstracts and papers and present evaluation on biomedical QA (MedQA); authors and the model card present the model for research purposes rather than production deployment.
  Scope: BioMedLM 2.7B (upstream checkpoint) — retained as upstream-checkpoint evidence; wrapper identity not established
  Evidence: https://huggingface.co/stanford-crfm/BioMedLM, https://arxiv.org/abs/2403.18421, https://crfm.stanford.edu/2022/12/15/biomedlm.html

### Conditional

- **Use in downstream biomedical QA or research-assisted drafting only with expert review, dataset-specific validation, and documented PHI handling.** — Requires human expert validation, dataset- and prompt-level evaluation on the specific downstream task, and explicit PHI handling processes before any sensitive or clinical use.
  Scope: BioMedLM 2.7B (upstream checkpoint) — retained as upstream-checkpoint evidence; wrapper identity not established
  Evidence: https://huggingface.co/stanford-crfm/BioMedLM, https://crfm.stanford.edu/2022/12/15/biomedlm.html

### Avoid

- **Clinical decision support or high-risk medical decision-making without expert review.** — Primary sources and model card indicate the model and its generation capabilities are intended for research and not suitable for production or clinical deployment without expert oversight.
  Scope: BioMedLM 2.7B (upstream checkpoint)
  Evidence: https://huggingface.co/stanford-crfm/BioMedLM

## Input preparation

### Semantic inputs

- Biomedical text inputs (PubMed abstracts, biomedical papers, clinical language) are the intended domain for the upstream checkpoint. Sources: https://crfm.stanford.edu/2022/12/15/biomedlm.html, https://arxiv.org/abs/2403.18421

### Accepted formats

- Raw text prompts (tokenized by the upstream BioMedLM tokenizer) are the accepted input format for the upstream checkpoint. Sources: https://huggingface.co/stanford-crfm/BioMedLM, https://github.com/stanford-crfm/BioMedLM/blob/main/README.md

### Preprocessing

- Tokenization uses the upstream BioMedLM tokenizer (GPT2Tokenizer class) with model_max_length / context length 1024. Sources: https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/tokenizer_config.json, https://huggingface.co/stanford-crfm/BioMedLM/commit/9ccd482b714e3c9939f61064300100d7a2c11567

### Pre-submit validation

- Inputs should be validated to fit within the model's context length (1024 tokens); the primary sources report model_max_length/context length = 1024. Sources: https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/config.json, https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/tokenizer_config.json

### Task-specific formatting

- No explicit upstream prompt templates or task-formatting templates are documented in the supplied primary sources for the exact checkpoint; prompts used in evaluation are described at a high level but exact formatting for reuse is not provided in the findings. Sources: https://arxiv.org/abs/2403.18421, https://github.com/stanford-crfm/BioMedLM/blob/main/README.md

## Output interpretation

### Outputs

- The upstream checkpoint produces natural-language text generation outputs (autoregressive decoding); logits and generation behavior follow standard Hugging Face Transformers semantics as used by the provided repo and demo. Sources: https://huggingface.co/stanford-crfm/BioMedLM, https://github.com/stanford-crfm/BioMedLM/blob/main/demo.py

### Interpretation

- Higher numeric scores on reported biomedical QA benchmarks indicate relative improvements in the evaluated metrics, but the primary sources do not provide calibration curves or explicit confidence-calibration guidance. Sources: https://arxiv.org/abs/2403.18421, https://huggingface.co/stanford-crfm/BioMedLM

### Post-inference validation

- Primary sources recommend human review for biomedical outputs; specific downstream-calibration procedures are not provided in the supplied findings. Sources: https://huggingface.co/stanford-crfm/BioMedLM, https://arxiv.org/abs/2403.18421

## Public benchmarks

### Biomedical Question Answering

- Dataset/split: MedQA / not reported
- Metric/value: accuracy / 50.3% (`higher-is-better`)
- Model scope: BioMedLM 2.7B (upstream checkpoint)
- Conditions: Reported in upstream model card/README as a standalone evaluation number; evaluation protocol details and split not specified in the supplied findings.
- Source: https://huggingface.co/stanford-crfm/BioMedLM
- Locator: Model card / README 'Evaluation' / results paragraph reporting MedQA accuracy = 50.3%
- Caveat: The supplied findings do not specify dataset split details or an exact table/figure number for this reported value; locator is the model card/README results paragraph rather than a numbered table in the supplied findings.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: General biomedical tasks (protocol alignment required for head-to-head)
- Criteria: No primary-source head-to-head, same-prompt, same-split evaluation data present in the supplied findings to compare BioMedLM 2.7B against specific competitor checkpoints.
- Rationale: The supplied primary findings include only upstream BioMedLM artifacts and do not provide canonical primary sources for competitor checkpoints or shared evaluation protocols; direct comparison is not supported by the available evidence.
- Comparison conditions: Head-to-head comparisons require canonical primary sources for both models with identical prompts, dataset splits, and evaluation protocol; such matching primary evidence is not present in the supplied findings.
- Evidence: https://huggingface.co/stanford-crfm/BioMedLM, https://arxiv.org/abs/2403.18421

## Limitations and safety

### Limitations

- BioMedLM is presented by the authors and model card as intended for research use rather than production or clinical deployment. Sources: https://huggingface.co/stanford-crfm/BioMedLM
- Training data for the upstream checkpoint is reported as PubMed abstracts and full-text biomedical papers drawn from The Pile; the supplied findings do not enumerate any proprietary clinical datasets. Sources: https://github.com/stanford-crfm/BioMedLM/blob/main/README.md, https://arxiv.org/abs/2403.18421
- The supplied findings do not report the model-weights or code license explicitly; license details for weights/code are not reported in the primary sources provided. Sources: https://huggingface.co/stanford-crfm/BioMedLM

### Safety

- Expert human review and documented PHI handling are required before any biomedical deployment; the upstream artifacts frame the model for research use not direct clinical decision-making. Sources: https://huggingface.co/stanford-crfm/BioMedLM, https://crfm.stanford.edu/2022/12/15/biomedlm.html

## Related upstream agent skills

### `agent-integration`

The cookbook maps these exact Forge slugs to BioNeMo-style capability names and Serverless shapes. Use it for routing and tool integration, never as model-quality evidence.
- [BioNeMo capability catalog](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/catalog.py)
- [BioNeMo named tool contracts](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/tools.py)
- [BioNeMo agent routing and safety instructions](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/configs/config.yml)

## Primary sources

### BioMedLM (model card / Hugging Face)

- URL: https://huggingface.co/stanford-crfm/BioMedLM
- Publisher: Stanford CRFM
- Type: `model-card`
- Primary because: Canonical upstream model card and hosting location for the BioMedLM checkpoint; contains evaluation summary, intended-use statements, and hosting instructions.
- Scope: BioMedLM
- Supports: intended-use statement (research, not production)
- Supports: MedQA reported accuracy = 50.3% (model card / README results paragraph)
- Supports: hosting location and usage instructions
- Supports: high-level description of model capabilities and training domain

### BioMedLM README (upstream repository)

- URL: https://github.com/stanford-crfm/BioMedLM/blob/main/README.md
- Publisher: Stanford CRFM
- Type: `repository`
- Primary because: Upstream repository README with training-data description, evaluation summary, and usage/demo instructions.
- Scope: BioMedLM repository
- Supports: training data described as PubMed abstracts and full-texts from The Pile
- Supports: statement of MedQA accuracy = 50.3% in repository README
- Supports: notes on prior name (PubMedGPT) and rename

### BioMedLM: arXiv preprint (canonical)

- URL: https://arxiv.org/abs/2403.18421
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing model architecture, training, compute, and evaluation.
- Scope: BioMedLM 2.7B
- Supports: architecture and model parameter scale (2.7B)
- Supports: training-domain statement (biomedical text)
- Supports: high-level evaluation descriptions
- Supports: authors and bibliographic metadata

### BioMedLM tokenizer configuration (Hugging Face repository blob: tokenizer_config.json)

- URL: https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/tokenizer_config.json
- Publisher: Stanford CRFM
- Type: `repository`
- Primary because: Upstream tokenizer configuration file specifying tokenizer class and model_max_length used by the checkpoint.
- Scope: BioMedLM tokenizer
- Supports: tokenizer class (GPT2Tokenizer) and model_max_length = 1024
- Supports: tokenization semantics and special tokens

### BioMedLM config.json (Hugging Face repository blob)

- URL: https://huggingface.co/stanford-crfm/BioMedLM/blob/6d1e633491cf0c7ab5cec86366a818e58f36b50d/config.json
- Publisher: Stanford CRFM
- Type: `repository`
- Primary because: Upstream model configuration file with architecture hyperparameters and context length.
- Scope: BioMedLM 2.7B (config)
- Supports: model architecture parameters (n_layer=32, n_head=20, n_embd=2560, n_positions=1024)
- Supports: vocabulary size (28896) and context length (1024)
- Supports: model type = gpt2 and other config hyperparameters

### Hugging Face model repo commit showing tokenizer configuration

- URL: https://huggingface.co/stanford-crfm/BioMedLM/commit/9ccd482b714e3c9939f61064300100d7a2c11567
- Publisher: Stanford CRFM
- Type: `repository`
- Primary because: Commit-level record demonstrating tokenizer settings and commit provenance for tokenizer artifacts.
- Scope: BioMedLM tokenizer commit
- Supports: tokenizer configuration details (GPT2Tokenizer class, add_prefix_space=false, model_max_length=1024)
- Supports: commit provenance for tokenizer files

### arXiv HTML (v1) for BioMedLM preprint

- URL: https://arxiv.org/html/2403.18421v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Paper HTML view providing implementation and training detail paragraphs (training infrastructure and compute descriptions).
- Scope: BioMedLM 2.7B (paper v1)
- Supports: training infrastructure and compute details (128 A100 GPUs, Flash Attention, Composer/FSDP)
- Supports: statements about evaluation behavior and multi-sentence answer generation

### BioMedLM demo script (upstream repository)

- URL: https://github.com/stanford-crfm/BioMedLM/blob/main/demo.py
- Publisher: Stanford CRFM
- Type: `repository`
- Primary because: Upstream demo script demonstrating how to load the tokenizer and model identifiers used by the project.
- Scope: BioMedLM demo
- Supports: example loading of tokenizer and model identifiers for runtime use
- Supports: practical usage example referencing tokenizer/model names

### Stanford CRFM project page for BioMedLM

- URL: https://crfm.stanford.edu/2022/12/15/biomedlm.html
- Publisher: Stanford CRFM
- Type: `official-documentation`
- Primary because: Official project page describing authorship, high-level project goals, and context within Stanford CRFM.
- Scope: BioMedLM project
- Supports: authorship and project description
- Supports: high-level intended-use framing and affiliation to Stanford CRFM

### BioMedLM upstream repository root (code and artifacts)

- URL: https://github.com/stanford-crfm/BioMedLM
- Publisher: Stanford CRFM
- Type: `repository`
- Primary because: Canonical upstream code repository for training/fine-tuning scripts and artifacts referenced by the paper and model card.
- Scope: BioMedLM codebase
- Supports: availability of training and demo code
- Supports: links to README and demo artifacts

## Evidence gaps

- No primary-source benchmark locators (exact table/figure/appendix/section) were present in the supplied findings for MedMCQA; the primary sources supplied do not provide a verifiable sourceLocator for a MedMCQA numeric result.
- No primary-source benchmark locators (exact table/figure/appendix/section) were present in the supplied findings for MMLU Medical Genetics; the primary sources supplied do not provide a verifiable sourceLocator for an MMLU numeric result.
- No primary evidence in the supplied findings establishes the identity or provenance linking any Forge wrapper variant (e.g., hf-3e1a0ab-wrapper-20260426-fix2) to the upstream BioMedLM checkpoint; wrapper-to-upstream identity proof is missing from the supplied findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 20 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[0]: $.sources[0]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.evidenceGaps[0]: $.evidenceGaps[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.evidenceGaps[1]: $.evidenceGaps[1]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://huggingface.co/papers/2403.18421 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'biomistral' for this exact model scope: $.sources[6] uses unapproved repository owner 'biomistral' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ar5iv.labs.arxiv.org/html/2403.18421 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
