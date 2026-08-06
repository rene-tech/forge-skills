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

- Research key: `huggingface-co-huggingfacebio-carbon-3b-8f075f26ab`
- Independent audit: `revised`
- Researched: `2026-07-23T23:55:20.295172+00:00`

I audited checkpoint-scoped primary artifacts for HuggingFaceBio/Carbon-3B and report only claims directly supported by those artifacts. The checkpoint is a 3‑billion‑parameter decoder‑only autoregressive genomic foundation model (upstream id: HuggingFaceBio/Carbon-3B). Primary upstream artifacts (Hugging Face model card, Carbon GitHub repository and repo tech‑report, the bioRxiv preprint/PDF, the GGUF artifact page, and the official Hugging Face Space demo) document that Carbon uses a hybrid tokenizer with non‑overlapping 6‑mer DNA tokenization (k=6 exposed by the repository tokenizer implementation), was pretrained on a large DNA/RNA mixture (authors report ~1 trillion 6‑mer tokens ≈6 trillion base pairs and an author‑reported eukaryote‑heavy mixture fraction), used an initial training sequence length of 8,192 tokens, and that the authors report long‑context extension behavior (native context claims reported up to 32,768 6‑mer tokens and extended to 65,536 tokens via YaRN per the primary preprint). The demo Space shows usage patterns including score_sequence for marginal base probabilities and generate for autoregressive DNA generation. The repository includes tokenizer implementation details (HybridDNATokenizer with k=6 and token_mask behavior) and evaluation/fine‑tuning scripts. Several operational and numeric details required by Forge (exact immutable checkpoint revision/hash, full tokenizer id→6‑mer vocabulary mapping, numbered/table locators for some reported numeric task scores) are not present in the inspected primary artifacts and are recorded as evidence gaps below.

## Identity

- Upstream name: HuggingFaceBio/Carbon-3B
- Checkpoint/version: HuggingFaceBio/Carbon-3B
- Immutable revision: not reported
- Parameter scale: 3‑billion‑parameter
- Architecture/head: Decoder‑only autoregressive Transformer (RMSNorm, SwiGLU, RoPE, GQA)
- License: not reported
- Evidence: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon, https://github.com/huggingface/carbon/blob/main/tech-report.pdf

## Selection

### Recommended

- **Research generative DNA sequence modelling and long‑context autoregressive generation (exploratory design and evaluation)** — Primary sources describe Carbon‑3B as a generative DNA foundation model trained on DNA/RNA corpora with non‑overlapping 6‑mer tokenization and autoregressive generation; the demo and repository examples show generate and score_sequence usage for DNA generation and scoring.
  Scope: HuggingFaceBio/Carbon-3B (3B decoder‑only checkpoint, non‑overlapping 6‑mer tokenizer)
  Evidence: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://github.com/huggingface/carbon, https://huggingfacebio-carbon-demo.hf.space
- **Research fine‑tuning for discriminative tasks (variant‑effect prediction, regression heads) using repository fine‑tuning scripts and reported evaluation protocols** — The authors provide fine‑tuning and evaluation scripts in the Carbon repository and report fine‑tuned evaluation results in the preprint/tech‑report; the repository indicates workflows to fine‑tune the base checkpoint with task‑specific heads.
  Scope: HuggingFaceBio/Carbon-3B when fine‑tuned with task heads using repository scripts (fine‑tuned checkpoints are distinct artifacts)
  Evidence: https://github.com/huggingface/carbon, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon/blob/main/tech-report.pdf
- **Sequence recovery and motif/perturbation discrimination in research evaluation suites (training‑free and fine‑tuned benchmarks described by the authors)** — The preprint and repo describe training‑free evaluation suites and fine‑tuned evaluation tasks including sequence recovery and perturbation discrimination where Carbon‑3B is evaluated.
  Scope: HuggingFaceBio/Carbon-3B evaluated under the authors' training‑free and fine‑tuned protocols
  Evidence: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon

### Conditional

- **Very long‑context inference (extended contexts up to author‑reported 65,536 tokens)** — Requires applying the authors' long‑context extension approach (YaRN rope scaling) as described in the primary preprint/tech‑report and may require specific runtime configuration; this is an extension beyond initial pretraining sequence lengths.
  Scope: HuggingFaceBio/Carbon-3B served with YaRN rope scaling or equivalent long‑context extension configured per the authors' description
  Evidence: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon, https://github.com/huggingface/carbon/blob/main/tech-report.pdf
- **Task performance reported for fine‑tuned checkpoints (e.g., regression heads for enhancer activity)** — Requires using the repository fine‑tuning scripts and the specific fine‑tuned checkpoint produced by running those scripts; reported numeric results in the preprint correspond to runs using those fine‑tuned artifacts rather than the untouched base checkpoint.
  Scope: HuggingFaceBio/Carbon-3B when fine‑tuned using the repository scripts to produce task‑specific heads/checkpoints
  Evidence: https://github.com/huggingface/carbon, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text

### Avoid

- **Unreviewed clinical decision‑making or clinical deployment without expert review** — Primary sources do not provide an author declaration of clinical suitability or clinical validation procedures; the materials present research benchmarks and code but not clinical validation.
  Scope: HuggingFaceBio/Carbon-3B
  Evidence: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text
- **Feeding DNA payloads without the expected tokenizer tagging/formatting (risking BPE fallback and degraded DNA modelling quality)** — The repository tokenizer implementation requires DNA regions to be wrapped in <dna>...</dna> tags to be tokenized as non‑overlapping 6‑mers; without tags the tokenizer will treat input as regular BPE text.
  Scope: HuggingFaceBio/Carbon-3B (HybridDNATokenizer behavior)
  Evidence: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B

## Input preparation

### Semantic inputs

- Primary input modality is DNA sequences represented for the hybrid tokenizer as non‑overlapping 6‑mer tokens when wrapped in <dna> tags; the model also accepts natural text handled by the BPE mode of the hybrid tokenizer. Sources: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B
- Training data mixture includes DNA and RNA corpora (authors report ~1 trillion 6‑mer tokens and an eukaryote‑heavy mix including mRNA, splice‑enriched mRNA, and GTDB bacterial genomes). Sources: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon

### Accepted formats

- DNA sequences intended for 6‑mer tokenization should be enclosed in <dna>...</dna> tags to trigger the HybridDNATokenizer's DNA path; natural language text is accepted outside these tags and tokenized with the BPE path. Sources: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B, https://huggingfacebio-carbon-demo.hf.space
- GGUF artifact pages for the checkpoint are provided by the authors and document available quantized artifacts and notes for runtime usage; users should consult the official GGUF page for artifact filenames and basic usage notes. Sources: https://huggingface.co/HuggingFaceBio/Carbon-3B-GGUF

### Preprocessing

- The HybridDNATokenizer implementation in the repository defines k=6 (non‑overlapping 6‑mer chunking) and includes dna_start_id, dna_vocab_size, dna_special_tokens and token_mask semantics for fine‑grained nucleotide supervision. Sources: https://github.com/huggingface/carbon/blob/main/tech-report.pdf, https://huggingface.co/HuggingFaceBio/Carbon-3B/commit/f47e012a66138e22188742060c6f79d8f2db00f3
- Authors report a training prefill/sequence length of 8,192 tokens and report a native context claim (32,768 6‑mer tokens) and author‑reported long‑context extension to 65,536 tokens via YaRN as documented in the preprint/tech‑report. Sources: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon/blob/main/tech-report.pdf, https://huggingface.co/HuggingFaceBio/Carbon-3B

### Pre-submit validation

- Validate that DNA regions intended for 6‑mer tokenization are properly wrapped in <dna>...</dna> tags; the repository notes token_mask semantics and the tokenizer's requirement for tags to select the DNA tokenization path. Sources: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B
- Evidence gap: The repository and model card expose k=6 and tokenizer attributes but do not include the full tokenizer vocabulary mapping (exact token id → 6‑mer string); the exact mapping is not present in the inspected primary artifacts.

### Task-specific formatting

- Wrap DNA payloads in <dna>...</dna> to trigger 6‑mer tokenization and avoid BPE fallback; follow repository/demo examples for calling score_sequence and generate methods. Sources: https://huggingfacebio-carbon-demo.hf.space, https://github.com/huggingface/carbon
- For scoring/evaluation the demo shows a score_sequence method returning mean log‑probability per DNA token; users should consult the demo and repository examples for the exact API usage. Sources: https://huggingfacebio-carbon-demo.hf.space, https://huggingface.co/HuggingFaceBio/Carbon-3B

## Output interpretation

### Outputs

- The demo shows the model supporting marginal base probability outputs and a mean log‑probability per DNA token via score_sequence; these are presented in the demo and repo examples. Sources: https://huggingfacebio-carbon-demo.hf.space, https://github.com/huggingface/carbon

### Interpretation

- Per‑base marginal probabilities and mean log‑probability per DNA token are interpretable as model conditional probabilities under the hybrid 6‑mer tokenizer path; the primary sources present these outputs but do not provide calibration curves or explicit calibration protocols. Sources: https://huggingfacebio-carbon-demo.hf.space, https://huggingface.co/HuggingFaceBio/Carbon-3B
- Evidence gap: Primary artifacts do not include per‑checkpoint calibration curves, logits‑to‑probability calibration procedures, or production confidence thresholds; users must run downstream calibration where needed.

### Post-inference validation

- Post‑inference validation recommended by the authors includes using the repository evaluation scripts for sequence recovery and variant‑effect tasks; reported metrics such as PCC and AUROC are presented in the preprint/repo for fine‑tuned runs. Sources: https://github.com/huggingface/carbon, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text
- Evidence gap: The inspected primary sources do not provide standardized operational thresholds or automatic decision rules for production use; downstream validation and expert review are required for decisioning.

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### InstaDeepAI/nucleotide-transformer-v2-500m-multi-species — `insufficient-evidence`

- Task: General DNA embedding/representation and downstream classification/regression tasks (open task set)
- Criteria: No primary‑source checkpoint‑scoped, head‑to‑head comparison with matching task, dataset/split, and metric is present in the inspected Carbon primary artifacts.
- Rationale: The Carbon preprint and repository present Carbon‑3B benchmarks and protocols but do not include matched primary data for the alternative model to support a validated head‑to‑head comparison.
- Comparison conditions: A valid comparison would require identical dataset/split/metric definitions and protocols for both checkpoints; those matched protocol data for the alternative are not available in the Carbon primary artifacts.
- Evidence: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon

### LongSafari/hyenadna-medium-450k-seqlen-hf — `insufficient-evidence`

- Task: Long‑sequence DNA embedding and throughput/performance for long contexts
- Criteria: No primary‑source matched long‑context benchmark data for both Carbon‑3B and the alternative are present in the inspected Carbon artifacts.
- Rationale: Carbon authors report long‑context behaviors and comparative statements within Carbon family but do not supply matched primary comparison data for the alternative checkpoint in the inspected sources.
- Comparison conditions: Comparability requires matched context lengths, tokenization, and identical evaluation metrics; those matched details for the alternative are absent from the Carbon primary artifacts.
- Evidence: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon

### zhihan1996/DNABERT-2-117M — `insufficient-evidence`

- Task: k‑mer embedding and sequence classification (shorter context tasks)
- Criteria: No primary‑source matched checkpoint comparisons on identical datasets/splits/metrics are present in the Carbon primary artifacts.
- Rationale: The Carbon primary artifacts document Carbon‑3B evaluation protocols but do not include matched primary data for DNABERT‑2 to allow a task‑matched comparison.
- Comparison conditions: A valid head‑to‑head requires identical tokenization, dataset splits, and metrics; these matched protocol data for the alternative are not present in the Carbon sources.
- Evidence: https://github.com/huggingface/carbon, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text

## Limitations and safety

### Limitations

- Pretraining data mixture bias: authors report an eukaryote‑heavy pretraining mixture (authors state ~70% generator‑style eukaryotic genomic DNA), implying potential performance biases toward eukaryotic sequences and underrepresentation of other taxa. Sources: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B
- Tokenization constraints: the HybridDNATokenizer uses non‑overlapping 6‑mer chunking (k=6) for DNA when tags are present; improper formatting or omission of <dna> tags can cause BPE fallback and degraded DNA modelling quality. Sources: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B
- Long‑context extension depends on explicit extension techniques: authors report native pretraining used shorter sequence lengths (8,192 tokens) and describe YaRN rope scaling to extend contexts; therefore long‑context performance depends on extension techniques rather than standard prefill behavior. Sources: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon/blob/main/tech-report.pdf
- Calibration and uncertainty: primary sources document mean log‑prob per token outputs but do not include explicit calibration procedures, uncertainty quantification protocols, or production confidence thresholds. Sources: https://huggingfacebio-carbon-demo.hf.space, https://github.com/huggingface/carbon
- Licensing and reuse: the inspected Hugging Face model card does not report explicit license metadata for the Carbon‑3B checkpoint; license information is not reported in the primary model card artifact. Sources: https://huggingface.co/HuggingFaceBio/Carbon-3B
- Evidence gap: The exact tokenizer vocabulary mapping (token id → 6‑mer string) is not present in the inspected primary artifacts; the repository shows tokenizer attributes and k=6 but not a full id→string vocabulary table.
- Evidence gap: The immutable checkpoint revision/hash for the HuggingFaceBio/Carbon-3B model weights is not reported in the inspected primary artifacts.

### Safety

- Authors do not provide a declaration of clinical suitability in the inspected primary artifacts; treat the model as research‑only and require domain expert review before any clinical application. Sources: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text
- No explicit PHI/data‑handling policy or clinical deployment instructions were found in the inspected primary artifacts; users must apply institutional and legal PHI safeguards for sensitive sequences. Sources: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B
- Dual‑use/biosecurity considerations: primary sources present research benchmarks and model design but do not include a dedicated biosecurity mitigation plan; perform domain expert review for dual‑use risk prior to deployment. Sources: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon

## Related upstream agent skills

### `agent-integration`

The cookbook maps these exact Forge slugs to BioNeMo-style capability names and Serverless shapes. Use it for routing and tool integration, never as model-quality evidence.
- [BioNeMo capability catalog](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/catalog.py)
- [BioNeMo named tool contracts](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/tools.py)
- [BioNeMo agent routing and safety instructions](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/configs/config.yml)

## Primary sources

### HuggingFaceBio/Carbon-3B — Hugging Face model card

- URL: https://huggingface.co/HuggingFaceBio/Carbon-3B
- Publisher: HuggingFaceBio (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model repository and card for the Carbon‑3B checkpoint.
- Scope: HuggingFaceBio/Carbon-3B (3B checkpoint, model card)
- Supports: identity.upstreamName
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: inputPreparation
- Supports: outputInterpretation
- Supports: limitations
- Supports: safety

### Carbon repository — GitHub (model code and evaluation scripts)

- URL: https://github.com/huggingface/carbon
- Publisher: Hugging Face (repository owner)
- Type: `repository`
- Primary because: Official repository containing tokenizer implementation, evaluation/fine‑tuning scripts, and links to the technical report.
- Scope: Repository for Carbon family (scripts and evaluation for Carbon-3B)
- Supports: inputPreparation
- Supports: preprocessing
- Supports: taskSpecificFormatting
- Supports: conditionalUseCases
- Supports: recommendedUseCases
- Supports: outputInterpretation
- Supports: limitations

### Carbon technical report (tech-report.pdf) — GitHub

- URL: https://github.com/huggingface/carbon/blob/main/tech-report.pdf
- Publisher: Hugging Face (technical report hosted in repo)
- Type: `technical-report`
- Primary because: Authors' technical report describing architecture, tokenization, and long‑context behaviour linked from the repository.
- Scope: Carbon family technical report (architecture, tokenization, long‑context claims)
- Supports: identity.architecture
- Supports: inputPreparation
- Supports: preprocessing
- Supports: researchSummary
- Supports: limitations

### Carbon bioRxiv preprint (full text)

- URL: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text
- Publisher: bioRxiv (authors' preprint)
- Type: `paper`
- Primary because: Primary preprint describing Carbon family architecture, training, benchmarks, and long‑context claims.
- Scope: Carbon family preprint (3B and 8B preprint full text)
- Supports: identity.architecture
- Supports: researchSummary
- Supports: conditionalUseCases
- Supports: limitations
- Supports: recommendedUseCases

### Carbon bioRxiv preprint (PDF)

- URL: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full.pdf
- Publisher: bioRxiv (authors' preprint PDF)
- Type: `paper`
- Primary because: PDF variant of the bioRxiv preprint used to corroborate numeric and architecture claims.
- Scope: Carbon family preprint (PDF)
- Supports: researchSummary
- Supports: conditionalUseCases
- Supports: limitations

### HuggingFaceBio/Carbon-3B-GGUF — GGUF artifact page

- URL: https://huggingface.co/HuggingFaceBio/Carbon-3B-GGUF
- Publisher: HuggingFaceBio (Hugging Face)
- Type: `model-card`
- Primary because: Official GGUF artifact page published by the model owners describing provided GGUF artifacts and basic runtime/quantization notes.
- Scope: GGUF variants and runtime/quantization notes for Carbon‑3B
- Supports: inputPreparation
- Supports: preprocessing
- Supports: outputInterpretation
- Supports: limitations

### Hugging Face demo for Carbon‑3B (HF Space)

- URL: https://huggingfacebio-carbon-demo.hf.space
- Publisher: Hugging Face Space (official demo)
- Type: `official-documentation`
- Primary because: Official demo Space showing example code, score_sequence behavior, and generate usage for Carbon‑3B.
- Scope: Demo usage snippets and scoring API examples for Carbon‑3B
- Supports: inputPreparation
- Supports: taskSpecificFormatting
- Supports: outputInterpretation

### Commit showing HybridDNATokenizer attributes and k=6 (Carbon-3B model repo commit)

- URL: https://huggingface.co/HuggingFaceBio/Carbon-3B/commit/f47e012a66138e22188742060c6f79d8f2db00f3
- Publisher: HuggingFaceBio (Hugging Face)
- Type: `repository`
- Primary because: Commit referenced in repository artifacts that documents HybridDNATokenizer implementation details including k=6 and token_mask semantics.
- Scope: Tokenizer implementation note linked from Carbon family artifacts (Carbon-3B commit)
- Supports: inputPreparation
- Supports: preprocessing
- Supports: taskSpecificFormatting

## Evidence gaps

- Exact tokenizer vocabulary listing (full token id → 6‑mer mapping) for the HuggingFaceBio/Carbon-3B checkpoint was not found in the inspected primary artifacts (checked: https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B, https://github.com/huggingface/carbon/blob/main/tech-report.pdf).
- Precise immutable checkpoint revision/hash for the HuggingFaceBio/Carbon-3B model weights is not reported in the inspected primary artifacts (checked: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://github.com/huggingface/carbon).
- Exact numbered table/figure/section locators for some numeric training‑free benchmark values cited in secondary summaries (for example a reported Sequence Recovery value of 61.54) are not present in the inspected primary artifacts; I could not locate a numbered table/figure in the preprint/tech‑report that provides that exact numeric locator (checked: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon/blob/main/tech-report.pdf, https://github.com/huggingface/carbon).
- Per‑checkpoint logits‑to‑probability calibration curves or explicit calibration procedures are not present in the inspected primary artifacts (checked: https://huggingfacebio-carbon-demo.hf.space, https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B).
- Direct, primary‑source head‑to‑head benchmark comparisons between HuggingFaceBio/Carbon-3B and each listed candidate alternative (e.g., InstaDeepAI nucleotide‑transformer, HyenaDNA Medium, DNABERT‑2) on identical dataset/split/metric protocols are not present in the inspected Carbon primary artifacts (checked: https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon).
- Exact runtime/latency/memory measurements for HuggingFaceBio/Carbon-3B in matched hardware/software configurations comparable to external summaries are not provided in the inspected primary artifacts (checked: https://huggingface.co/HuggingFaceBio/Carbon-3B, https://biorxiv.org/content/10.64898/2026.05.22.727119v1.full-text, https://github.com/huggingface/carbon).
- Explicit canonical prompt templates, pair‑input orderings, or few‑shot instruction examples for mixed DNA+text prompts are not provided in the inspected primary artifacts (checked: https://huggingfacebio-carbon-demo.hf.space, https://github.com/huggingface/carbon, https://huggingface.co/HuggingFaceBio/Carbon-3B).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses unapproved repository owner 'pankajpandey-dev' for this exact model scope: $.sources[6] uses unapproved repository owner 'pankajpandey-dev' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary URL https: $.sources[8] uses forbidden secondary URL https://rewire.it/blog/carbon-3b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary host docs.vllm.ai: $.sources[12] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'instadeepai' for this exact model scope: $.sources[13] uses unapproved repository owner 'instadeepai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'longsafari' for this exact model scope: $.sources[14] uses unapproved repository owner 'longsafari' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses unapproved repository owner 'zhihan1996' for this exact model scope: $.sources[15] uses unapproved repository owner 'zhihan1996' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
