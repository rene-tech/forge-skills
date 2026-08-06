# Protein Representation model selection

- Category: `life-science`
- Group: `protein-representation`
- Independent audit: `revised`
- Researched: `2026-07-23T21:23:49.249650+00:00`

Protein representation in this group means encoding a protein amino-acid sequence into learned features usable for: masked-language-model scoring (per-token or pseudo/perplexity measures), per-residue embeddings, pooled/per-sequence embeddings, retrieval/clustering, remote-homology-style comparison, variant-effect scoring (fitness/regression), or contact/structure-proxy analyses. In scope are the exact Forge candidates biohub-esmc-600m-protein-embedding, facebook-esm-2-3b, facebook-esm-2-3b-protein-embedding, facebook-esm-2-650m, and facebook-esm-2-650m-protein-embedding. Upstream-checkpoint evidence (model card, config, or paper) may be used only when it clearly applies to the named checkpoint; wrapper/runtime behavior for the Forge embedding variants is separate unless directly documented in a primary source. Out of scope are claims that depend on attached structure heads, ESMFold/ESMFold2 pipelines, downstream supervised heads, third-party serving stacks, or unofficial conversions unless explicitly documented in a primary source.

## Questions to answer before selecting

- Do you need checkpoint-scoped upstream evidence only, or exact serving/runtime evidence for the Forge wrapper/versionKey?
- Do you need per-residue (per-token) embeddings or a pooled/per-sequence embedding (for example mean pooling), and is that output explicitly documented for the exact Forge artifact?
- What maximum sequence length must be supported, and does the requirement apply to the upstream checkpoint or the serving wrapper?
- Will you compare models on MLM/perplexity, remote homology, variant-effect prediction, contact/structure proxy, or embedding retrieval, and is there a protocol-matched primary benchmark for the exact artifacts?
- Are you relying on a base masked-language-model checkpoint only, or on an additional predictor/structure/retrieval service that is not exposed by the Forge candidate?
- Must licensing be clearly permissive and consistent across primary sources, or can you tolerate unresolved licensing or clickthrough restrictions for ESMC-related artifacts?
- Do you require documented hidden-size or architecture details (for example 1280-dim versus 2560-dim internal representations) from a primary source for downstream integration?
- Do you require documented masking details, pooling method, normalization, dtype, or output shape, and if so are those semantics available for the exact Forge artifact rather than only an upstream checkpoint or provider conversion?
- Are you comparing results across artifacts that differ in wrapper, precision, output format, or provider documentation, in which case comparability may fail even when upstream checkpoints are related?
- Do you require safety, use-restriction, or commercial-use documentation from primary sources for the exact artifact?

## Comparability rules

- Only compare benchmark values when the exact upstream checkpoint or exact served artifact is the same class of object; do not compare a base checkpoint result with a wrapper/runtime result unless parity is explicitly documented.
- For MLM/perplexity comparisons, masking rate and evaluation procedure must match exactly. The ESM-2 paper reports 15% masking during training; use that exact masking for protocol-matched perplexity comparisons. (ESM-2 preprint)
- For per-sequence embedding comparisons, pooling method must match exactly; some sources report mean embeddings for ESM‑C 600M but that is artifact-specific and must be matched before comparison.
- For per-residue embedding comparisons, output semantics must match exactly: per-token/per-residue versus pooled sequence embedding, returned layer choice if configurable, and whether logits or predictor outputs are included.
- Maximum supported sequence length must be matched at the artifact level; converted-provider docs report fixed training/evaluation lengths for some variants and those must be respected.
- Do not transfer performance from ESMFold/ESMFold2, contact heads, or other attached structures to a base embedding checkpoint unless the dependency is stated explicitly.

## Conditional routing

### Prefer `facebook-esm-2-3b` when You need the strongest primary evidence in this group for exact upstream checkpoint identity and architecture details, and no protocol-matched downstream benchmark across the Forge variants is required.

- Why: Primary upstream-checkpoint evidence exists for the exact facebook/esm2_t36_3B_UR50D checkpoint including a Hugging Face model card that identifies the checkpoint; configuration-level architecture details (36 layers, 40 attention heads, hidden size 2560) are present in the model card/config and NVIDIA BioNeMo documentation documents converted 3B variants. This is upstream-checkpoint evidence suitable when checkpoint identity and architecture are the primary selection criteria.
- Alternative: facebook-esm-2-650m
- Alternative: biohub-esmc-600m-protein-embedding
- Alternative: facebook-esm-2-3b-protein-embedding
- Alternative: facebook-esm-2-650m-protein-embedding
- Evidence: https://huggingface.co/facebook/esm2_t36_3B_UR50D, https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json, https://docs.nvidia.com/bionemo-framework/1.10/models/esm2-nv.html, https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text

### Prefer `facebook-esm-2-650m` when You need the strongest primary evidence in this group for exact upstream checkpoint identity plus explicit config-level architecture details for a smaller ESM-2 checkpoint.

- Why: Primary upstream-checkpoint evidence exists for the exact facebook/esm2_t33_650M_UR50D checkpoint including a Hugging Face model card and an explicit config.json that documents EsmForMaskedLM architecture, 33 layers, hidden size 1280, 20 attention heads, max_position_embeddings 1026, token_dropout true, and torch_dtype float32. NVIDIA documentation also documents converted 650M variants. This evidence supports selecting the 650M checkpoint when smaller architecture and documented config are required.
- Alternative: facebook-esm-2-3b
- Alternative: facebook-esm-2-650m-protein-embedding
- Alternative: biohub-esmc-600m-protein-embedding
- Alternative: facebook-esm-2-3b-protein-embedding
- Evidence: https://huggingface.co/facebook/esm2_t33_650M_UR50D, https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json, https://docs.nvidia.com/bionemo-framework/1.10/models/esm2-nv.html

### Prefer `biohub-esmc-600m-protein-embedding` when You need an ESMC-family artifact with primary-source claims of up to 2048-residue encoding and configurable mean and/or per-token embeddings, and you accept that this evidence is for Biohub-family artifacts rather than verified Forge-wrapper parity.

- Why: Primary Biohub sources (repository and Hugging Face pages) and Biohub documentation describe ESMC family training regimes and released ESMC checkpoints; a Biohub description documents stage training with a longer context length (stage 2 context length 2048) for ESMC, and peer literature reports mean embeddings for ESM‑C 600M as a provider‑described pooling modality. However, this is artifact/family/provider-scoped evidence rather than explicit Forge-wrapper runtime parity evidence.
- Alternative: facebook-esm-2-650m
- Alternative: facebook-esm-2-650m-protein-embedding
- Alternative: facebook-esm-2-3b
- Alternative: facebook-esm-2-3b-protein-embedding
- Evidence: https://github.com/Biohub/esm, https://huggingface.co/biohub/ESMC-600M, https://huggingface.co/biohub/esmc-600m-2024-12/blame/main/README.md, https://nature.com/articles/s41598-025-05674-x

### Prefer `insufficient-evidence` when You require protocol-matched head-to-head benchmark evidence across the exact scoped Forge candidates for remote homology, variant-effect prediction, contact/structure proxy, or embedding retrieval.

- Why: The available primary sources include upstream-checkpoint benchmark fragments (NVIDIA converted-checkpoint benchmarks, PFMBench entries) and per-artifact provider claims, but no primary-source protocol-matched head-to-head evaluation was found that runs the exact Forge candidates under identical datasets, splits, pooling, normalization, and scoring rules. Therefore there is insufficient primary evidence to prefer any one exact Forge candidate for protocol-matched group-wide benchmark superiority.
- Alternative: biohub-esmc-600m-protein-embedding
- Alternative: facebook-esm-2-3b
- Alternative: facebook-esm-2-3b-protein-embedding
- Alternative: facebook-esm-2-650m
- Alternative: facebook-esm-2-650m-protein-embedding
- Evidence: https://docs.nvidia.com/bionemo-framework/1.10/models/model-benchmarks.html, https://arxiv.org/html/2407.07265v1, https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text

### Prefer `facebook-esm-2-650m` when Licensing clarity is a decisive requirement and you cannot proceed with unresolved artifact-family license ambiguity (for example ESMC clickthrough restrictions).

- Why: Primary converted-provider and Hugging Face entries for NVIDIA-converted ESM-2 650M list an MIT license and provider documentation states converted ESM-2 models are ready for commercial use; in contrast, EvolutionaryScale clickthrough/license documents describe clickthrough licensing and usage restrictions for ESMC-class models, producing ambiguity for ESMC-family artifacts. When licensing clarity is decisive and NVIDIA/Hugging Face MIT-licensed converted variants are acceptable, prefer the documented MIT-licensed ESM-2 650M checkpoint.
- Alternative: biohub-esmc-600m-protein-embedding
- Alternative: facebook-esm-2-3b
- Alternative: facebook-esm-2-3b-protein-embedding
- Alternative: facebook-esm-2-650m-protein-embedding
- Evidence: https://huggingface.co/nvidia/esm2_t33_650M_UR50D, https://docs.nvidia.com/bionemo-framework/1.10/models/esm2-nv.html, https://evolutionaryscale.ai/policies/cambrian-inference-clickthrough-license-agreement

## Benchmark taxonomy

### MLM / pretraining fit (perplexity)

- Datasets: UniRef
- Metrics: Perplexity (lower is better) when computed with identical masking rate, held-out-data definition, and aggregation (ESM-2 training used 15% amino-acid masking)
- Compare only when: Masking procedure must match exactly (15% masking as reported for ESM-2 in the ESM-2 preprint).
- Compare only when: Evaluation must use the same held-out data definition and perplexity aggregation method.
- Compare only when: Do not compare provider-specific predictor endpoints with base-checkpoint MLM results unless they expose the same scoring protocol.

### Remote homology / structure-family retrieval

- Datasets: 4HBT family
- Metrics: HMM-based retrieval or family-retrieval metrics only when the exact pipeline is matched (for example positional-probability → hmmbuild as used in the cited remote-homology study), Evidence gap: no canonical retrieval metric across the scoped artifacts verified for group-wide comparison
- Compare only when: Method must match exactly: plain embeddings, positional probabilities, or HMM construction are not interchangeable.
- Compare only when: Family/split definition must match exactly.
- Compare only when: Do not compare a probability-to-HMM pipeline result with a pooled-embedding retrieval result.

### Variant-effect prediction / fitness

- Datasets: ProteinGym v1, GB1
- Metrics: Dataset-matched regression/ranking metrics only (for example mean-squared error for GB1 when the provider/benchmark protocol specifies that aggregation)
- Compare only when: Dataset and assay must match exactly, including whether the task is regression or ranking.
- Compare only when: Scoring method must match exactly: predictor logits, masked-token scoring, or another mutation-scoring pipeline are not interchangeable.
- Compare only when: Do not compare third-party API predictor outputs with base-checkpoint zero-shot scoring unless the scoring procedure is the same and documented.

### Contact / per-residue structure proxy

- Datasets: Unverified: no canonical protocol-matched dataset for group comparison verified
- Metrics: Long-range precision at L (P@L) for unsupervised inter-residue contact precision when the same protocol is used
- Compare only when: Must distinguish base embedding checkpoints from contact-map outputs or attached structure pipelines.
- Compare only when: Returned representation type must match exactly: per-token embeddings, self-attention maps, contact maps, or downstream structure-module outputs are different artifacts.
- Compare only when: Comparison requires the same contact definition and sequence filtering protocol.

### Embedding-quality retrieval / clustering

- Datasets: Unverified: no canonical retrieval/clustering dataset with protocol-matched results across scoped artifacts
- Metrics: Nearest-neighbor retrieval accuracy, clustering purity, or related retrieval metrics only when the exact corpus, labels, normalization, pooling, and distance metric are matched
- Compare only when: Pooling must match exactly for per-sequence comparisons.
- Compare only when: Normalization and distance metric must match exactly.
- Compare only when: If a provider API allows configurable layer choice, the compared layer must also match exactly.

## Primary sources

- [Hugging Face model card for biohub/ESMC-600M](https://huggingface.co/biohub/ESMC-600M) — Biohub on Hugging Face; supports Exact upstream source URL for the Biohub ESMC 600M Forge candidate, Existence of the Biohub ESMC 600M model artifact and recommended Hugging Face-compatible weights
- [Biohub ESM GitHub repository](https://github.com/Biohub/esm) — Biohub GitHub; supports ESMC family primary repository evidence and code (esm package), Repository-level license statements and code distribution for ESM family
- [Hugging Face README for biohub/esmc-600m-2024-12](https://huggingface.co/biohub/esmc-600m-2024-12/blame/main/README.md) — Biohub on Hugging Face; supports Legacy/release README documenting recommended Hugging Face-compatible ESMC weights and packaging format
- [Hugging Face model card for facebook/esm2_t36_3B_UR50D](https://huggingface.co/facebook/esm2_t36_3B_UR50D) — Meta on Hugging Face; supports Exact upstream checkpoint identity for ESM-2 3B, Model card presence for facebook/esm2_t36_3B_UR50D
- [Hugging Face config for facebook/esm2_t36_3B_UR50D](https://huggingface.co/facebook/esm2_t36_3B_UR50D/blob/e465bb8d75fb881450cacab2f1ccc14585e00ac5/config.json) — Meta on Hugging Face; supports Config-level architecture details for ESM-2 3B when available in the model repository
- [Hugging Face model card for facebook/esm2_t33_650M_UR50D](https://huggingface.co/facebook/esm2_t33_650M_UR50D) — Meta on Hugging Face; supports Exact upstream checkpoint identity for ESM-2 650M, Model card presence for facebook/esm2_t33_650M_UR50D
- [Hugging Face config for facebook/esm2_t33_650M_UR50D](https://huggingface.co/facebook/esm2_t33_650M_UR50D/blob/main/config.json) — Meta on Hugging Face; supports Exact config-level architecture details for ESM-2 650M including EsmForMaskedLM, hidden size 1280, 33 layers, 20 attention heads, max_position_embeddings 1026, token_dropout true, and torch_dtype float32
- [NVIDIA BioNeMo ESM-2 documentation](https://docs.nvidia.com/bionemo-framework/1.10/models/esm2-nv.html) — NVIDIA; supports BioNeMo documents converted ESM-2 checkpoints (650M and 3B) and provides converted-checkpoint architecture summaries and provider-specific input/output notes, Provider-specific training/evaluation length and per-amino-acid output statements for converted variants
- [NVIDIA BioNeMo model benchmarks v1.10](https://docs.nvidia.com/bionemo-framework/1.10/models/model-benchmarks.html) — NVIDIA; supports NVIDIA BioNeMo model benchmarks for converted ESM-2 variants (benchmark table fragments for multiple tasks)
- [ESM-2 original bioRxiv preprint full text](https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text) — bioRxiv; supports ESM-2 original preprint describing training on UniRef, the 15% amino-acid masking rate used for ESM-2 training, and family-level claims about learned internal representations including contact-related structure information
- [bioRxiv paper on ESM-2 3B positional probabilities for remote homology study](https://biorxiv.org/content/biorxiv/early/2023/07/29/2023.07.26.550718.full.pdf) — bioRxiv; supports Remote-homology-style evidence that ESM-2 3B positional probabilities were used to build HMMs with hmmbuild for the 4HBT family in a cited remote-homology study
- [EvolutionaryScale Cambrian inference clickthrough license agreement](https://evolutionaryscale.ai/policies/cambrian-inference-clickthrough-license-agreement) — EvolutionaryScale; supports Clickthrough/license evidence describing usage restrictions and commercial/API usage prohibitions for certain ESMC-delivered models, Evidence that EvolutionaryScale lists ESMC models under specific clickthrough or community licensing terms
- [PFMBench (arXiv preprint)](https://arxiv.org/html/2407.07265v1) — arXiv; supports PFMBench entries reporting per-task results for specific checkpoint variants (PDBBind, Stability, etc.) but not as a protocol-matched head-to-head across the exact Forge wrappers
- [Hugging Face model card for nvidia/esm2_t36_3B_UR50D](https://huggingface.co/nvidia/esm2_t36_3B_UR50D) — Hugging Face (NVIDIA repo); supports NVIDIA-converted Hugging Face model page for nvidia/esm2_t36_3B_UR50D documenting MIT license and conversion/optimization status
- [Hugging Face model card for nvidia/esm2_t33_650M_UR50D](https://huggingface.co/nvidia/esm2_t33_650M_UR50D) — Hugging Face (NVIDIA repo); supports NVIDIA-converted Hugging Face model page for nvidia/esm2_t33_650M_UR50D documenting MIT license and conversion/optimization status
- [Scientific article referencing ESM‑C 600M mean embeddings](https://nature.com/articles/s41598-025-05674-x) — Nature Communications / Scientific Reports (publisher noted in findings); supports Analysis and provider-reported conclusions noting that ESM-C 600M mean embeddings offer balance between performance and efficiency; literature-level statements about ESM‑C 600M and mid-size model tradeoffs
- [Hybrid ESM2-UMAP variant-classification preprint](https://biorxiv.org/content/10.1101/2025.07.26.666924v1.full.pdf) — bioRxiv; supports Example application of hybrid ESM2 embeddings for variant classification and reported ROC-AUC results in a later preprint

## Evidence gaps

- Evidence gap: No primary-source, protocol-matched head-to-head benchmark was found for the exact Forge candidates biohub-esmc-600m-protein-embedding, facebook-esm-2-3b, facebook-esm-2-3b-protein-embedding, facebook-esm-2-650m, and facebook-esm-2-650m-protein-embedding under identical datasets, splits, pooling, normalization, and scoring rules. (See NVIDIA BioNeMo benchmarks and PFMBench fragments which are not protocol-matched across the exact Forge wrappers.)
- Evidence gap: The findings do not provide exact wrapper-parity evidence for the Forge embedding variants biohub-esmc-600m-protein-embedding, facebook-esm-2-3b-protein-embedding, or facebook-esm-2-650m-protein-embedding; upstream-checkpoint evidence should not be treated as serving-runtime benchmark evidence without explicit documentation.
- Evidence gap: Pooling method for the exact Forge embedding variants is not fully documented in the available primary sources for every wrapper; while literature and some provider pages document mean embeddings for ESM‑C 600M, wrapper-level pooling semantics remain unverified for the exact Forge embedding artifacts.
- Evidence gap: Output shape, dtype, returned layer, and JSON-field semantics are not fully documented for the exact Forge embedding variants. NVIDIA converted model pages document Float16 1-D embedding outputs for converted artifacts, while upstream checkpoint configs state torch_dtype float32 at the config level; these differences are artifact-scoped and not resolved to wrapper parity.
- Evidence gap: Maximum sequence length evidence is artifact-specific and not uniformly comparable across all scoped artifacts. NVIDIA BioNeMo docs mention fixed training/evaluation lengths (for example 1024) for converted variants, while ESMC family descriptions reference longer context in stage training for ESMC; the exact supported length per Forge wrapper is not fully verified.
- Evidence gap: For ESM-2 MLM/perplexity, the ESM-2 preprint documents 15% masking during training but a full protocol-matched held-out-perplexity benchmark across the exact Forge candidates was not found.
- Evidence gap: The findings do not verify a canonical protocol-matched dataset and metric suite across the scoped artifacts for remote homology, contact prediction, or embedding retrieval/clustering.
- Evidence gap: Variant-effect evidence is incomplete for group-wide comparison: provider-specific or converted-checkpoint fragments exist, but a single verified common evaluation protocol across all scoped artifacts is not present in the primary sources.
- Evidence gap: Some ESMC performance-positioning claims in provider or Biohub pages are family/provider claims rather than exact Forge-artifact benchmark rows; they are insufficient to declare an across-group winner without wrapper parity.
- Evidence gap: Licensing for ESMC-related usage is not cleanly resolved at the group level because EvolutionaryScale clickthrough/license documentation indicates clickthrough/usage restrictions for some ESMC deliveries while other Hugging Face/NVIDIA entries list MIT for converted ESM-2 variants; this creates artifact-family licensing ambiguity that requires per-artifact legal review.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 15 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarkTaxonomy[0].datasets[0]: $.benchmarkTaxonomy[0].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1].datasets[0]: $.benchmarkTaxonomy[1].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1].datasets[1]: $.benchmarkTaxonomy[1].datasets[1]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2].datasets[0]: $.benchmarkTaxonomy[2].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2].datasets[1]: $.benchmarkTaxonomy[2].datasets[1]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2].datasets[2]: $.benchmarkTaxonomy[2].datasets[2]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3].datasets[0]: $.benchmarkTaxonomy[3].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[4].datasets[0]: $.benchmarkTaxonomy[4].datasets[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[4].datasets[1]: $.benchmarkTaxonomy[4].datasets[1]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/esm2_t36_3B_UR50D Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/2.0/models/esm2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/nvidia/esm2_t36_3B_UR50D Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/2.0/models/esm2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://biorxiv.org/content/10.1101/2022.07.20.500902v1.full.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/bionemo-framework/2.0/models/esm2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
