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

- Research key: `huggingface-co-nvidia-cosmos-ea-cosmos3-nano-reasoner-4225bbfc6d`
- Independent audit: `revised`
- Researched: `2026-08-06T13:21:04.511871+00:00`

Cosmos3 is a two-tower Mixture-of-Transformers family (Reasoner + Generator) developed by NVIDIA Cosmos Lab. The Reasoner pathway is an autoregressive vision-language model trained on paired vision-language data for multimodal reasoning tasks; the Generator pathway performs iterative denoising generation and can be conditioned on Reasoner outputs. The NVIDIA technical report documents family-level architecture details (layer counts, hidden dimensions, attention heads) and reports family/ checkpoint-referenced ablations (e.g., Table 28 shows replacing Qwen3-VL-8B with Cosmos3‑Nano Reasoner yields measured domain-score improvements on text-to-video understanding domains). The primary authoritative artifacts checked for this dossier were: the NVIDIA Cosmos3 technical report PDF (Table 28 and architecture tables), the NVIDIA Cosmos Lab landing page, the NVIDIA GitHub cookbooks README and inference benchmark docs, the NVIDIA Build model card for cosmos3-nano-reasoner, the NVIDIA NGC catalog entry for the Cosmos3 Reasoner container, and the arXiv preprint record. Where checkpoint-scoped immutable artifacts (exact checkpoint filenames, stable weight download URLs, cryptographic hashes), tokenizer file listings, per-dataset provenance tables, canonical Hugging Face model-card files for the exact Forge catalog slug, or protocol-complete benchmark rows were not present in those primary locations, this dossier records explicit evidence gaps and names the exact primary locations inspected.

## Identity

- Upstream name: Cosmos3-Nano Reasoner
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Mixture-of-Transformers two-tower design (Reasoner: autoregressive transformer; Generator: diffusion transformer). Includes 3D multimodal RoPE (mRoPE). (Family-level architecture reported in the NVIDIA Cosmos3 technical report and Cosmos Lab landing materials.)
- License: OpenMDW-1.1 (stated in the NVIDIA build model card entry)
- Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://research.nvidia.com/labs/cosmos-lab, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune

## Selection

### Recommended

- **Multimodal reasoning (question answering, spatial grounding, temporal reasoning, action understanding) from paired vision-language inputs** — The NVIDIA Cosmos3 technical report describes the Reasoner pathway as trained on paired vision-language data to support question answering, spatial grounding, temporal reasoning, and action understanding.
  Scope: Cosmos3 family / Cosmos3-Nano Reasoner (family-level Reasoner pathway provenance)
  Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- **Autoregressive text generation conditioned on multimodal context (next-token decoding via the Reasoner pathway)** — The technical report describes the Reasoner as an autoregressive tower that generates discrete structured/text outputs (next-token semantics) for downstream conditioning and interpretation.
  Scope: Cosmos3 family / Cosmos3-Nano Reasoner (Reasoner pathway, family-level provenance)
  Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- **Physical-AI world understanding and simulation support (foundational building block for robotics, autonomous vehicles, and smart spaces) when integrated with appropriate domain validation** — The Cosmos Lab landing and technical report describe Cosmos3 as targeted at Physical AI tasks (robotics, AV, smart spaces) and as a world-modeling foundation combining reasoning and generation.
  Scope: Cosmos3 family / Cosmos3-Nano (family-level provenance)
  Evidence: https://research.nvidia.com/labs/cosmos-lab, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Conditional

- **Use of the Generator pathway for multimodal generation (images, video, actions) in production workflows** — The Generator pathway and Generator-serving artifacts are described at family level in NVIDIA materials; confirm the availability, exact image/tag, and serving contract of a published Generator NIM/container (if required) before assuming deployed inference capability or claiming precise runtime behavior.
  Scope: Cosmos3 family Generator pathway (family-level provenance)
  Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md
- **Workstation/accelerated inference deployments of Cosmos3-Nano for efficient inference** — Family-level documentation and the NVIDIA Build model card indicate Nano targets lower inference cost; validate precise runtime/precision/quantization support, exact container image tags, and tested hardware from authoritative NGC or container product pages before deployment.
  Scope: Cosmos3-Nano (family-level/Build model-card provenance)
  Evidence: https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://research.nvidia.com/labs/cosmos-lab

### Avoid

- **Treating Cosmos3-Nano outputs as physically accurate simulation or provably safe/safety-certified decision-making** — Family-level documentation and the model entry note that outputs should not be treated as physically accurate simulation or safety-certified decision making; safety-critical applications require additional validation and guardrails.
  Scope: Cosmos3 family / Cosmos3-Nano Reasoner (family-level provenance)
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

## Input preparation

### Semantic inputs

- Family-level accepted semantic modalities: text, image, video, audio, and action/trajectory sequences. Sources: https://research.nvidia.com/labs/cosmos-lab, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Accepted formats

- The authoritative sources describe accepted modalities (text, image, video, audio, actions) at family level but do not enumerate exact file codecs, MIME types, container formats, resolution/bitrate limits, or exact audio sample-rate constraints in the checked primary artifacts. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://research.nvidia.com/labs/cosmos-lab

### Preprocessing

- Reasoner pathway: text is handled via autoregressive next-token generation semantics; Generator pathway: non-text modalities are synthesized via iterative denoising and the pipeline conditions the Generator on structured JSON from the Reasoner (family-level description). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Architectural preprocessing detail: Cosmos3 uses a 3D multimodal RoPE (mRoPE) positional encoding mechanism for multimodal inputs (family-level architectural description). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Pre-submit validation

- Evidence gap: Immutable checkpoint filenames, exact upstream model-weight download URLs, and cryptographic hashes for Cosmos3-Nano Reasoner are not reported in the checked primary artifacts (technical report, Build model card, NVIDIA GitHub cookbook, NGC catalog, arXiv entry). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner, https://arxiv.org/abs/2606.02800
- Evidence gap: Tokenizer artifact filenames (tokenizer.json, vocab files, merges, tokenizer config) and explicit tokenization/truncation rules (max token counts, special token semantics) are not enumerated in the checked primary artifacts. Sources: https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Evidence gap: The checked primary artifacts do not enumerate precise accepted file-codec/container constraints (permitted video codecs, maximum resolution limits, audio codecs, or exact sample rates) for serving inputs. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune

### Task-specific formatting

- Evidence gap: The checked primary artifacts do not provide canonical prompt templates, paired-input ordering conventions, or explicit inference instruction-format examples for the Cosmos3-Nano Reasoner checkpoint. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md

## Output interpretation

### Outputs

- Text outputs: autoregressively generated discrete token sequences from the Reasoner pathway (next-token decoding semantics described at family level). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Image and video outputs: non-text modalities synthesized by the Generator pathway via iterative denoising, conditioned on Reasoner-produced structured JSON (family-level description). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Action outputs: structured action states/trajectories (JSON-style) are described as an output modality produced by the Reasoner and used to condition the Generator or downstream systems (family-level description). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Interpretation

- Text outputs should be interpreted under standard autoregressive next-token semantics; the primary artifacts do not document calibrated per-token probability export or a standardized confidence-score format. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Evidence gap: The checked primary artifacts do not specify per-token probability export fields, calibrated confidence scores, or a canonical per-output confidence schema. Sources: https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Post-inference validation

- Evidence gap: Post-inference validation checks, recommended downstream sanity tests, or explicit calibration/verification procedures for generated modalities are not specified in the checked primary artifacts. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune

## Public benchmarks

### Text-to-video (family/domain aggregate scores reported)

- Dataset/split: not reported (dataset name/split not specified in the checked Table 28 row) / not reported
- Metric/value: Domain score (aggregate domain-level scores reported in Table 28) / Reported in Table 28: overall T2V domain score improved from 73.7 to 75.7 when replacing Qwen3-VL-8B with Cosmos3‑Nano Reasoner; Robot domain +4.8 (66.5→71.3), Physics +0.5 (88.7→89.2), Autonomous Vehicles +2.3 (52.6→54.9). (`higher-is-better`)
- Model scope: Cosmos3-Nano Reasoner as referenced in Table 28 of the NVIDIA technical report (family/checkpoint-referenced row in the technical report).
- Conditions: Table 28 reports domain-aggregate scores but does not include explicit dataset name(s), exact evaluation split identifiers, prompting or input-shaping protocol, batching/precision details, or full evaluation script/config needed for protocol reproduction in the checked artifact.
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Locator: Table 28 (technical report)
- Caveat: The reported Table 28 row lacks explicit dataset name and split in the checked artifact.
- Caveat: Full protocol details (prompting, input preprocessing, precision, batching) are not present in the checked Table 28 entry necessary for direct reproduction.

## Comparisons

### nvidia-cosmos3-reasoner-super — `insufficient-evidence`

- Task: family-level domain understanding/generation comparisons
- Criteria: No primary-source, protocol-matched head-to-head comparison rows binding both explicit evaluated checkpoint identifiers and full protocol details were found in the checked primary artifacts.
- Rationale: The NVIDIA technical report and Cosmos Lab materials present family-level and some checkpoint-referenced improvements (e.g., Table 28 mentions Cosmos3‑Nano Reasoner replacement effects) but do not provide matched, protocol-complete numeric rows naming both Cosmos3-Nano and the alternative checkpoint with dataset/split/metric and immutable checkpoint artifact identifiers required for direct head-to-head comparability.
- Comparison conditions: Checked primary locations: technical-report Table 28 and surrounding tables; Build model card; NVIDIA GitHub inference_benchmarks.md. These do not contain the full paired protocol rows for the two checkpoints under identical, fully-described evaluation conditions.
- Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://research.nvidia.com/labs/cosmos-lab

## Limitations and safety

### Limitations

- Evidence gap: Immutable checkpoint filenames, exact upstream model-weight download URLs, and cryptographic hashes (e.g., SHA256) for the Cosmos3-Nano Reasoner checkpoint are not present in the checked primary artifacts (technical report, Build model card, NVIDIA GitHub cookbook, NGC catalog, arXiv record). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner, https://arxiv.org/abs/2606.02800
- Evidence gap: Tokenizer artifacts (tokenizer.json, vocab files, merges, tokenizer-config) and explicit tokenization/truncation rules (max tokens, special tokens) for Cosmos3-Nano Reasoner are not enumerated in the checked primary artifacts. Sources: https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Evidence gap: Per-dataset provenance, per-dataset licensing metadata, and explicit per-example filtering rules for pretraining and evaluation corpora are not enumerated in the checked primary artifacts (technical report and arXiv record do not provide per-dataset tables with provenance in the inspected sections). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://arxiv.org/abs/2606.02800
- Evidence gap: Canonical serving/container image tags, compressed image sizes, and exact NGC container artifact metadata (including explicit NGC product terms for any containers) for a published Cosmos3 Generator or Reasoner NIM are not present in the checked primary artifacts; the NGC catalog page describes the Reasoner container product but the checked page does not publish immutable container digests or downloadable checkpoint file hashes. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner, https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune

### Safety

- The Build.NVIDIA model card and NVIDIA materials state the model and NIMs are provided for commercial usage under OpenMDW-1.1 as listed on the Build model card entry; confirm licensing terms from the Build model card and NGC product pages prior to redistribution or embedding in commercial products. Sources: https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner
- Evidence gap: The checked primary artifacts do not enumerate operational data-handling policies (PHI/PII-specific rules), clinical-use restrictions, or explicit mandatory human-review requirements; such operational safety/data-handling policies are not documented in the inspected technical report, Build model card, NGC catalog entry, or GitHub cookbook README. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner
- Evidence gap: Per-dataset filtering rules and explicit statements enumerating exclusion of restricted content at a per-dataset or per-example granularity are not present in the checked primary artifacts (technical report and arXiv record). Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://arxiv.org/abs/2606.02800

## Related upstream agent skills

### `related-model-workflow`

NVIDIA's Cosmos Reason skill gives first-party video-QA data, checkpoint-conversion, evaluation, and SFT guidance. Its packaged default is Cosmos3-Nano; treat the Forge Nano/Super aliases as separate exact checkpoints and verify the selected weight, format, and overrides before applying the workflow, especially for Super.
- [tao-finetune-cosmos-reason](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/tao-finetune-cosmos-reason)

## Primary sources

### Cosmos3 technical report

- URL: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Publisher: NVIDIA (Cosmos Lab)
- Type: `technical-report`
- Primary because: Official NVIDIA technical report documenting family architecture, training description, and benchmark tables (e.g., Table 28).
- Scope: Cosmos3 family technical report (family-level architecture, Reasoner and Generator pathway descriptions, Table 28 benchmarks)
- Supports: architecture
- Supports: Reasoner and Generator pathway design
- Supports: 3D multimodal RoPE (mRoPE)
- Supports: benchmark tables referenced as Table 28

### NVIDIA Cosmos Lab (Cosmos3 family landing)

- URL: https://research.nvidia.com/labs/cosmos-lab
- Publisher: NVIDIA (Cosmos Lab)
- Type: `official-documentation`
- Primary because: Official NVIDIA landing page summarizing Cosmos3 family capabilities and linking to primary artifacts.
- Scope: Cosmos3 family landing and summary
- Supports: family-level capability summary
- Supports: statements about family targets (Physical AI, robotics, smart spaces)

### arXiv: Cosmos 3: Omnimodal World Models for Physical AI

- URL: https://arxiv.org/abs/2606.02800
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint record for the Cosmos3 paper as an authoritative preprint entry; used for paper metadata verification.
- Scope: Canonical arXiv preprint record for Cosmos3 (paper-level metadata)
- Supports: canonical preprint identifier and metadata

### NVIDIA GitHub: Cosmos3 cookbooks README

- URL: https://github.com/NVIDIA/cosmos/blob/main/cookbooks/cosmos3/README.md
- Publisher: NVIDIA (GitHub repository)
- Type: `repository`
- Primary because: Official NVIDIA repository documentation describing NIM images, cookbook usage, and runtime notes (Reasoner and Generator NIM image names referenced here).
- Scope: NVIDIA/cosmos GitHub cookbook for Cosmos3 (cookbook README content, NIM image names, runtime hints)
- Supports: NIM image names and README-level runtime notes
- Supports: cookbook deployment and configuration examples

### NVIDIA GitHub: inference_benchmarks.md (Cosmos)

- URL: https://github.com/NVIDIA/cosmos/blob/main/inference_benchmarks.md
- Publisher: NVIDIA (GitHub repository)
- Type: `repository`
- Primary because: Official NVIDIA repository benchmarking notes describing inference performance experiments for Cosmos3-Nano Reasoner.
- Scope: Inference benchmarks for Cosmos3-Nano Reasoner (vLLM and other engine measurements)
- Supports: inference performance measurements (TTFT, latency, throughput) as reported by NVIDIA

### Build.NVIDIA model card: cosmos3-nano-reasoner

- URL: https://build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune
- Publisher: NVIDIA (Build.NVIDIA)
- Type: `official-documentation`
- Primary because: Official NVIDIA Build model card entry for the cosmos3-nano-reasoner product, providing licensing and release metadata.
- Scope: cosmos3-nano-reasoner Build model card
- Supports: license statement (OpenMDW-1.1) as presented on the Build model card
- Supports: release metadata and product description

### NVIDIA NGC catalog: Cosmos3 Reasoner container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner
- Publisher: NVIDIA (NGC Catalog)
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC catalog product page describing the Cosmos3 Reasoner container offering.
- Scope: NGC catalog entry for Cosmos3 Reasoner container
- Supports: catalog description of the Cosmos3 Reasoner container and its commercial/NGC listing

### Hugging Face model entry: nvidia/Cosmos3-Nano

- URL: https://huggingface.co/nvidia/Cosmos3-Nano
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: Official Hugging Face model repository entry for a Cosmos3 Nano family artifact (used as an available primary Hugging Face-hosted reference in the research findings set).
- Scope: Hugging Face nvidia/Cosmos3-Nano model page (example prompt, usage notes, family-level caution language)
- Supports: usage caution about not treating outputs as physically accurate
- Supports: example prompts and high-level usage notes

### Exact official starting source declared by Forge

- URL: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano-Reasoner
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-cosmos3-reasoner
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The checked primary artifacts do not publish immutable checkpoint filename(s), exact upstream model-weight download URL(s), or cryptographic hash(es) for Cosmos3-Nano Reasoner. Checked locations: research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf (see architecture and tables), build.nvidia.com/nvidia/cosmos3-nano-reasoner/modelcard?modal=fine-tune (model card), github.com/NVIDIA/cosmos cookbooks README and inference_benchmarks.md, catalog.ngc.nvidia.com org/container page, and arXiv record https://arxiv.org/abs/2606.02800.
- Evidence gap: The checked primary artifacts do not list tokenizer artifact filenames (tokenizer.json, vocab files, merges, tokenizer config) or explicit tokenization/truncation rules (max token lengths, special token semantics). Checked locations: Build model card, NVIDIA GitHub cookbooks README, technical report PDF.
- Evidence gap: The checked primary artifacts do not provide per-dataset provenance tables or explicit per-dataset filtering rules enumerating exclusion of restricted content at the per-dataset or per-example level. Checked locations: technical report (checked benchmark/appendix sections including Table 28), arXiv preprint record.
- Evidence gap: Canonical Hugging Face repository/asset listing for the exact Forge-declared slug 'huggingface-co-nvidia-cosmos-ea-cosmos3-nano-reasoner-4225bbfc6d' (immutable model-card files, per-checkpoint asset listing) was not found among the inspected primary artifacts; checked locations: Hugging Face model entry https://huggingface.co/nvidia/Cosmos3-Nano and NVIDIA Build model card and NVIDIA GitHub cookbooks README.
- Evidence gap: Exact serving/container image digests, immutable container artifact digests/tags and compressed image sizes for published NIM/container artifacts are not published in the inspected NGC catalog entry or Build model card; checked locations: NGC catalog page and GitHub README.
- Evidence gap: Protocol-complete, checkpoint-scoped benchmark rows that include dataset name, dataset split, metric definition, numeric value, and an immutable evaluated checkpoint identifier (filename/hash) suitable for direct reproduction were not found in the inspected primary artifacts (see technical report Table 28 for family/checkpoint-referenced deltas but missing dataset/split/protocol binding).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano-Reasoner Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano-Reasoner: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[1]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
