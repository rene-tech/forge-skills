# Physical Ai model selection

- Category: `physical-ai`
- Group: `physical-ai`
- Independent audit: `revised`
- Researched: `2026-07-23T22:17:23.137086+00:00`

Select among the exact listed Forge packaging variants for four verified Physical-AI families when your primary task is one of: (1) joint video-text embedding retrieval and embedding-based classification (Cosmos-Embed1 upstream checkpoint / NIM), (2) multimodal robot policy prediction/control using Cosmos-Policy ALOHA Predict2 or LIBERO Predict2 upstream checkpoints, (3) multimodal physical-world reasoning using Cosmos Reason1/Reason2 family upstream checkpoints, or (4) early-access Cosmos3 Reasoner variants. Out of scope: (a) asserting equivalence of packaging variants (cuda12/cuda13/b300-optimized/b300-fast-action/fp8) to an upstream checkpoint unless a canonical per-slug NVIDIA serving page documents identical checkpoint identity, (b) numeric benchmark claims that cannot be directly verified at an exact model-card/README/NGC/container page line/table for the exact checkpoint, packaging variant, dataset split, and protocol, and (c) operational latency/throughput claims not present in a primary NVIDIA or official repository source.

## Questions to answer before selecting

- Which primary task family do you need: joint video-text embeddings (Cosmos-Embed1), robot policy prediction/control (ALOHA Predict2 or LIBERO Predict2), multimodal reasoning (Cosmos Reason1/Reason2), or early-access Cosmos3 Reasoner?
- Do you require an embeddings-style API (vectors) or a generative/text output or a policy/action-sequence JSON output?
- Which input modalities will you supply: text, image(s), video, multi-view images, or proprioceptive state?
- Must the chosen candidate be one of the exact listed Forge slugs even if the public primary evidence only documents an upstream checkpoint or a family-level NIM/container?
- Are there license constraints that affect deployment (model-weight license vs container/NIM license vs early-access/evaluation-only terms)?
- Will you compare candidates under a strict benchmark protocol (can you match checkpoint identity, dataset split, preprocessing, prompt/decoding settings, and runtime conditions)?
- Do you require ALOHA-specific action-generation behavior (use Predict2 checkpoint) versus ALOHA planning-model outputs (separate planning-model checkpoint per upstream guidance)?
- Is validated FP8 hardware/precision support required for your deployment (note: the available primary evidence does not document per-slug FP8 validation)?

## Comparability rules

- Compare benchmark values only when the exact evaluated upstream checkpoint identity matches the candidate being discussed or when a primary NVIDIA serving page explicitly documents that a wrapper/container serves the identical upstream checkpoint.
- Do not compare Forge packaging variants (cuda12, cuda13, b300-optimized, b300-fast-action, fp8) on model quality unless a primary source explicitly documents they serve the same checkpoint under a comparable evaluation protocol; treat packaging variants as unresolved wrappers by default.
- For embedding comparisons, match the exact embedding checkpoint, task, and dataset; do not compare embedding retrieval metrics against reasoning or policy outputs.
- For policy-model comparisons, match task family and environment (LIBERO results are not directly comparable to ALOHA results absent a shared benchmark protocol documented in primary sources).
- For reasoning-model comparisons, match modality, prompt/evaluation recipe, and benchmark; do not infer cross-family numeric comparisons when no shared protocol is documented by primary sources.
- Keep runtime/container/NIM evidence (availability, API, license) strictly separate from upstream checkpoint weight and benchmark evidence.
- If a primary source does not specify preprocessing (frame sampling, normalization, pooling), prompt templates, decoding, or split, treat comparisons requiring those controls as insufficiently specified and record an evidence gap.

## Conditional routing

### Prefer `nvidia-cosmos-embed1` when You need joint video-text embeddings for physical-AI retrieval, semantic search, semantic deduplication, zero-shot classification, or k-NN classification and require a text/video embeddings API.

- Why: Primary NVIDIA model-card, NIM documentation, NGC container page, and a Hugging Face model page document Cosmos-Embed1 as a joint video-text embedding model exposed via an embeddings-style HTTP API and list retrieval/semantic-deduplication/zero-shot use cases.
- Alternative: nvidia-cosmos-reason1-7b
- Alternative: nvidia-cosmos-reason2-2b
- Evidence: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1, https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1, https://huggingface.co/nvidia/Cosmos-Embed1-448p

### Prefer `nvidia-cosmos-policy-libero-predict2-cuda12` when You need a robot policy model for LIBERO tasks with documented upstream checkpoint evidence and want to prefer a packaging variant only when wrapper identity is not required to be proven.

- Why: Primary Hugging Face model pages and the cosmos-policy repository provide upstream LIBERO Predict2 2B checkpoint identity, describe input/output modalities (text, multi-view images, proprioceptive state) and link to benchmark/README evidence for LIBERO Predict2; packaging variants lack per-slug canonical primary pages in the retained findings, so the recommendation is conservative and based on upstream-checkpoint evidence.
- Alternative: nvidia-cosmos-policy-libero-predict2-b300-fast-action
- Alternative: nvidia-cosmos-policy-libero-predict2-b300-optimized
- Alternative: nvidia-cosmos-policy-libero-predict2-cuda13
- Alternative: nvidia-cosmos-policy-libero-predict2-fp8
- Evidence: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B, https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blame/4b40eef4f155242348ea24919ea5540dca25a644/README.md, https://github.com/nvlabs/cosmos-policy

### Prefer `nvidia-cosmos-policy-aloha-predict2-cuda12` when You need a robot policy model for ALOHA tasks and action generation (Predict2-style output) rather than only planning-model outputs.

- Why: Primary Hugging Face ALOHA Predict2 model documentation and the cosmos-policy repository state that the Predict2 checkpoint is the intended checkpoint for action-generation outputs; packaging-variant wrappers in Forge are not proven by a primary per-slug sourcing in the retained findings, so wrapper identity remains an evidence gap.
- Alternative: nvidia-cosmos-policy-aloha-predict2-b300-optimized
- Alternative: nvidia-cosmos-policy-aloha-predict2-cuda13
- Evidence: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B, https://github.com/nvlabs/cosmos-policy

### Prefer `nvidia-cosmos-reason2-8b` when You need a stronger-capacity multimodal reasoning VLM among the Reason2 family and prefer an explicitly larger Reason2 checkpoint when documented as providing stronger chain-of-thought reasoning.

- Why: Primary Hugging Face model pages for Reason2 8B and 2B document the Reason2 family and the 8B variant as a higher-parameter reasoning VLM relative to the 2B variant; retained findings indicate a qualitative stronger chain-of-thought claim for the 8B variant but do not provide a strict numeric head-to-head protocol.
- Alternative: nvidia-cosmos-reason2-2b
- Alternative: nvidia-cosmos-reason1-7b
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://huggingface.co/nvidia/Cosmos-Reason2-2B, https://docs.nvidia.com/cosmos/latest/cosmos_nim.html

### Prefer `nvidia-cosmos-reason1-7b` when You prefer the older Reason1 family for deployment compatibility, or need a documented Reason1 NIM/container rather than Reason2 or Cosmos3.

- Why: Primary Hugging Face and NGC container pages identify Cosmos Reason1-7B as a 7B-parameter reasoning VLM for physical AI and the NGC container page documents an associated NIM container and license layering for Reason1-7B.
- Alternative: nvidia-cosmos-reason2-2b
- Alternative: nvidia-cosmos3-reasoner-nano
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason1-7b, https://docs.nvidia.com/cosmos/latest/cosmos_nim.html

### Prefer `nvidia-cosmos3-reasoner-super` when You want a Cosmos3 Reasoner family candidate from the listed set and accept early-access or evidence-limited selection within that family.

- Why: Primary sources document a Cosmos3 Reasoner family and a Cosmos3-Nano Hugging Face page; retained findings confirm Cosmos3 family identity and an NGC cosmos3-reasoner NIM container page but do not provide an explicit public primary per-slug model-card for a 'super' variant, so choosing 'super' is a capacity-oriented routing assumption within the family and remains evidence-limited.
- Alternative: nvidia-cosmos3-reasoner-nano
- Alternative: nvidia-cosmos-reason2-8b
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner, https://huggingface.co/nvidia/Cosmos3-Nano

## Benchmark taxonomy

### Joint video-text embedding retrieval and embedding-based classification

- Datasets: Vad-Reasoning
- Metrics: Use-case-level outcomes documented in primary sources: text-to-video retrieval, inverse video search, semantic deduplication, zero-shot classification, and k-NN classification (primary sources do not provide exact numeric dataset-level benchmark values for the listed Forge slug)., Evidence gap: no exact comparable numeric metrics, split-level values, or evaluation-harness lines for Cosmos-Embed1 on the named datasets were found in the retained primary sources.
- Compare only when: Use the exact Cosmos-Embed1 upstream checkpoint or an explicitly documented identical upstream checkpoint served by the wrapper.
- Compare only when: Match task type: retrieval/classification with embeddings (do not compare against generative reasoning outputs).
- Compare only when: If preprocessing details (frame sampling, normalization, pooling) or split names are not specified by the primary source, comparisons requiring those controls are insufficiently specified.

### LIBERO robot policy prediction/control

- Datasets: LIBERO benchmark, LIBERO-Cosmos-Policy dataset
- Metrics: Suite-level success rate (%) and average success rate (%) as reported by upstream LIBERO Predict2 documentation when explicitly provided by a primary source., Evidence gap: retained primary sources document benchmark/README material for LIBERO Predict2 but do not provide a fully specified per-wrapper numeric head-to-head table for Forge packaging variants.
- Compare only when: Only compare candidates using the same documented upstream LIBERO Predict2 checkpoint identity.
- Compare only when: Do not compare LIBERO results directly against ALOHA results absent a shared, documented benchmark recipe.

### ALOHA policy action generation versus ALOHA planning-model prediction

- Datasets: ALOHA manipulation tasks
- Metrics: Primary-source documented outcomes for ALOHA Predict2 and planning-model checkpoints are descriptive (future-state images, value predictions, and action-generation outputs)., Evidence gap: no exact per-wrapper numeric benchmark table for listed ALOHA packaging variants was found in the retained primary sources.
- Compare only when: For action generation use evidence tied specifically to the ALOHA Predict2 checkpoint; for world-model or value outputs use the separate ALOHA planning-model checkpoint where the primary source instructs so.
- Compare only when: Do not conflate benchmarks of planning-model outputs with Predict2 action-generation benchmarks.

### Multimodal physical-world reasoning with Reason1/Reason2/Cosmos3 Reasoner

- Datasets: Evidence gap: no fully specified primary-source benchmark dataset and protocol comparable across Reason1, Reason2, and Cosmos3 Reasoner was found in the retained findings.
- Metrics: Evidence gap: no retained primary source provides a cross-family benchmark table with exact protocol details for the listed reasoning candidates.
- Compare only when: Compare only within a documented benchmark recipe that specifies modality, prompt/evaluation recipe, split, preprocessing, and decoding settings.
- Compare only when: Do not infer numeric head-to-head superiority across families absent a shared documented protocol.

## Primary sources

- [Cosmos-Embed1 model card (NGC TAO)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1) — NVIDIA NGC Catalog; supports Cosmos-Embed1 is a joint video-text embedder tailored for physical AI, Cosmos-Embed1 use cases: text-to-video retrieval, inverse video search, semantic deduplication, zero-shot classification, k-NN classification, and video curation, A fine-tuned anomaly-detection variant (Vad-Reasoning) is provided
- [Cosmos-Embed1 Hugging Face (Cosmos-Embed1-448p)](https://huggingface.co/nvidia/Cosmos-Embed1-448p) — NVIDIA on Hugging Face; supports Cosmos-Embed1 model developer is NVIDIA, Checkpoint variants are provided at specific fixed resolutions and support non-square resolutions
- [Cosmos-Embed1 NIM introduction (NVIDIA Docs)](https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html) — NVIDIA Documentation; supports Cosmos Embed1 is an NVIDIA Inference Microservice (NIM) that generates joint video-text embeddings for short-form videos, Cosmos Embed1 exposes an HTTP/REST embeddings API compatible with the OpenAI Embeddings API, Cosmos Embed1 NIM lists endpoints and describes deployment as a downloadable container or NVCF function
- [Cosmos-Embed1 NIM container (NGC)](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1) — NVIDIA NGC Catalog; supports Cosmos Embed1 NIM provides access to the Cosmos-Embed1 joint video-text embedding model via an HTTP API, Container composition and license layering (NGC container license distinct from model-use license) are documented
- [Cosmos-Policy ALOHA Predict2 2B (Hugging Face)](https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B) — NVIDIA on Hugging Face; supports ALOHA Predict2 checkpoint provides future-state images and value predictions and is the documented Predict2 checkpoint for action-generation use cases, The HF page documents intended outputs and routing guidance between Predict2 and planning-model checkpoints
- [cosmos-predict2 repository (NVIDIA-Cosmos)](https://github.com/nvidia-cosmos/cosmos-predict2) — NVIDIA-Cosmos (GitHub); supports Repository contains README, license, and Dockerfile artifacts for predict2-related code distribution
- [cosmos-policy repository (NVLabs / NVIDIA)](https://github.com/nvlabs/cosmos-policy) — NVLabs / NVIDIA (GitHub); supports Repository includes example configs referencing upstream checkpoint ckpt_path "nvidia/Cosmos-Policy-LIBERO-Predict2-2B" and inference configs, Repository documentation lists operational VRAM requirements for LIBERO, RoboCasa, and ALOHA simulation tasks
- [Cosmos-Policy LIBERO Predict2 2B README snapshot (Hugging Face blame link)](https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B/blame/4b40eef4f155242348ea24919ea5540dca25a644/README.md) — NVIDIA on Hugging Face; supports Upstream LIBERO Predict2 training/evaluation details and README documentation exist in the model repository
- [Cosmos-Policy LIBERO Predict2 2B model page (Hugging Face)](https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B) — NVIDIA on Hugging Face; supports LIBERO Predict2 checkpoint identity and input/output modality descriptions for the 2B checkpoint
- [Cosmos NIM reference for VLMs (NVIDIA Docs)](https://docs.nvidia.com/cosmos/latest/cosmos_nim.html) — NVIDIA Documentation; supports NIM availability for Cosmos-Reason1 and Cosmos-Reason2 families is documented
- [Cosmos Reason1-7B NIM container (NGC)](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason1-7b) — NVIDIA NGC Catalog; supports Reason1-7B NIM container identity and associated license layering
- [Cosmos-Reason1-7B model page (Hugging Face)](https://huggingface.co/nvidia/Cosmos-Reason1-7B) — NVIDIA on Hugging Face; supports Reason1-7B identity, parameter scale, and high-level reasoning capabilities description
- [Cosmos-Reason2-2B model page (Hugging Face)](https://huggingface.co/nvidia/Cosmos-Reason2-2B) — NVIDIA on Hugging Face; supports Reason2-2B identity and parameter scale and documentation (Cosmos Cookbook reference present in retained facts)
- [Cosmos Reason-2 2B NIM container (NGC)](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-2b) — NVIDIA NGC Catalog; supports Reason2-2B container identity, feature descriptions, and license layering
- [Cosmos-Reason2-8B model page (Hugging Face)](https://huggingface.co/nvidia/Cosmos-Reason2-8B) — NVIDIA on Hugging Face; supports Reason2-8B identity and parameter scale; retained findings indicate it is described as a stronger-capacity variant relative to Reason2-2B
- [Cosmos3-Nano model page (Hugging Face)](https://huggingface.co/nvidia/Cosmos3-Nano) — NVIDIA on Hugging Face; supports Cosmos3-Nano page documents Cosmos3 family and includes OpenMDW 1.1 license indications in retained findings
- [Cosmos3 Reasoner NIM container (NGC)](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos3-reasoner) — NVIDIA NGC Catalog; supports Cosmos3 Reasoner family identity and NIM/container availability are documented
- [Exact official starting source declared by Forge](https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html) — docs.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md) — github.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://github.com/NVlabs/cosmos-policy) — github.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/cosmos-reason1-7b) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/cosmos-reason2-8b) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano-Reasoner) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super-Reasoner) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-aloha-predict2-b300-optimized; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-aloha-predict2-cuda12; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-aloha-predict2-cuda13; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-libero-predict2-b300-fast-action; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-libero-predict2-b300-optimized; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-libero-predict2-cuda12; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-libero-predict2-cuda13; wrapper identity to an upstream checkpoint is unproven in the retained primary sources.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-libero-predict2-fp8; the retained findings do not document an exact FP8 configuration, hardware support statement, or validation protocol for this packaging variant.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-policy-aloha-predict2-b300-optimized; packaging-variant benchmark/latency/precision differences are unproven.
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-reason2-2b that ties a specific Forge wrapper to the upstream checkpoint (the Hugging Face and NGC container pages document the upstream checkpoint; per-slug wrapper identity is unresolved when packaged as a custom Forge container).
- Evidence gap: no canonical public per-slug primary source was found in the retained findings for the Forge slug nvidia-cosmos-reason2-8b that ties a specific Forge wrapper to the upstream checkpoint (the Hugging Face page documents the upstream checkpoint but a per-slug Forge wrapper page is not present in the retained findings).
- Evidence gap: no canonical public per-slug primary source for nvidia-cosmos3-reasoner-super was found in the retained findings; the NGC cosmos3-reasoner container and HF Cosmos3-Nano exist in the retained findings but no explicit public per-slug model-card for a 'super' variant was found.
- Evidence gap: retained primary sources do not provide exact numeric dataset/split-level benchmark tables (values, splits, preprocessing, sampling, pooling) for Cosmos-Embed1 on Vad-Reasoning or any other named dataset that would allow strict numeric comparisons of packaging variants.
- Evidence gap: retained primary sources do not specify preprocessing details required for strict comparison (frame sampling count, frame sampling recipe, per-frame normalization, pooling strategy, embedding dimensionality or preset-specific output shape) for Cosmos-Embed1.
- Evidence gap: retained primary sources do not provide a fully specified, shared benchmark protocol (dataset, splits, preprocessing, prompts, decoding) that allows numeric head-to-head comparisons across Reason1, Reason2, and Cosmos3 families.
- Evidence gap: retained primary sources do not provide per-wrapper JSON schema, exact action-unit definitions, postprocessing, or output-validation schemas for the listed policy Forge slugs; upstream checkpoint pages describe input/output categories but not wrapper-specific JSON schemas.
- Evidence gap: retained primary sources do not provide validated FP8 hardware/precision support statements or a published FP8 validation protocol tied to the listed packaging slug nvidia-cosmos-policy-libero-predict2-fp8.
- Evidence gap: license layering is present in retained findings (model-weight vs container/NIM license) but some specific per-slug license assignments are not documented in the retained findings; do not assume unified license terms across wrapper and upstream weight without checking the per-slug primary page.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 5 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[19] uses forbidden secondary URL https: $.sources[19] uses forbidden secondary URL https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Predict2-2B/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Policy-ALOHA-Planning-Model-Predict2-2B/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://github.com/NVlabs/cosmos-policy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/cosmos-reason1-7b: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/cosmos-reason2-8b: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano-Reasoner: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super-Reasoner: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
