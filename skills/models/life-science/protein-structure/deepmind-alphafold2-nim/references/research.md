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

- Research key: `build-nvidia-com-deepmind-alphafold2-312dcaf74a`
- Independent audit: `revised`
- Researched: `2026-07-23T23:11:24.276952+00:00`

Primary-source evidence supports the exact Forge scope as an NVIDIA AlphaFold2 NIM service for predicting 3D protein structure from amino acid sequence through documented sequence-to-structure and sequence-to-MSA endpoints. Upstream evidence supports AlphaFold2 licensing distinctions, confidence cautions, and a non-clinical-use boundary. However, the findings do not verify an exact upstream checkpoint or immutable revision for the NVIDIA-packaged callable variant, and no exact-scope numeric benchmark for the Forge/NIM runtime was retained. Upstream architecture and clinical-boundary evidence should therefore be treated as upstream-checkpoint/family evidence, not as a runtime-quality benchmark of the NVIDIA service artifact.

## Identity

- Upstream name: AlphaFold2
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Protein structure prediction model; upstream architecture evidence describes an input module that generates MSA and pair representations from an amino-acid sequence, an Evoformer module, and a structure module that converts abstract representations to 3D atom coordinates.
- License: Forge source page states use of the AlphaFold2 model is governed by the Apache 2.0 License; upstream repository states code is released under Apache 2.0 and model parameters are licensed under CC BY 4.0; NVIDIA NGC container listing additionally states the container is governed by the NVIDIA Software License Agreement, the Product-Specific Terms for NVIDIA AI Products, and the AI Foundation Models Community License Agreement.
- Evidence: https://build.nvidia.com/deepmind/alphafold2, https://github.com/google-deepmind/alphafold, https://catalog.ngc.nvidia.com/orgs/nim/teams/deepmind/containers/alphafold2, https://nature.com/articles/s41392-023-01381-z

## Selection

### Recommended

- **Predicting 3D protein structure from an amino acid sequence** — The Forge source page states AlphaFold2 predicts the 3D structure of a protein from its amino acid sequence, the NVIDIA model card states the model predicts the 3D structure of a protein from its amino acid sequence, and NVIDIA endpoint documentation exposes a predict-structure-from-sequence endpoint.
  Scope: deepmind-alphafold2-nim at https://build.nvidia.com/deepmind/alphafold2
  Evidence: https://build.nvidia.com/deepmind/alphafold2, https://build.nvidia.com/deepmind/alphafold2/modelcard, https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html
- **Generating multiple sequence alignment and templates for downstream inference within the NVIDIA AlphaFold2 NIM workflow** — NVIDIA endpoint documentation states AlphaFold2 provides an endpoint protein-structure/alphafold2/predict-MSA-from-sequence to generate a multiple sequence alignment and templates for inference.
  Scope: deepmind-alphafold2-nim endpoint protein-structure/alphafold2/predict-MSA-from-sequence
  Evidence: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html

### Conditional

- **Using predictions to support research workflows that generate and assess the structure and function of new proteins and small molecules** — Use only as a research-support tool, not as a sole authority; downstream scientific validation remains necessary because upstream sources state predictions have varying levels of confidence and should be interpreted carefully.
  Scope: NVIDIA AlphaFold2 NIM used with other NIMs in pipeline settings
  Evidence: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/overview.html, https://github.com/google-deepmind/alphafold, https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf

### Avoid

- **Clinical diagnostic decision-making or clinical use as a validated/approved authority** — Upstream repository states AlphaFold 2 and its output are intended for theoretical modeling only and are not validated or approved for clinical use. The retained NVIDIA primary sources do not provide contrary clinical validation or approval language for the packaged NIM.
  Scope: AlphaFold2 guidance applied to the NVIDIA-packaged AlphaFold2 NIM as an upstream-use boundary
  Evidence: https://github.com/google-deepmind/alphafold

## Input preparation

### Semantic inputs

- The model consumes a protein amino acid sequence as input. Sources: https://build.nvidia.com/deepmind/alphafold2, https://build.nvidia.com/deepmind/alphafold2/modelcard, https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html

### Accepted formats

- The exact Forge scope accepts a protein sequence as input for structure prediction. Sources: https://build.nvidia.com/deepmind/alphafold2, https://build.nvidia.com/deepmind/alphafold2/modelcard, https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html

### Preprocessing

- NVIDIA documentation exposes a predict-MSA-from-sequence endpoint that generates a multiple sequence alignment and templates for inference, indicating that MSA/template generation is part of the documented service workflow when that endpoint is used. Sources: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html
- Upstream architecture evidence describes an input module that generates MSA and pair representations from an amino-acid sequence before Evoformer and structure modules operate. Sources: https://nature.com/articles/s41392-023-01381-z

### Pre-submit validation

- Evidence gap: The research findings do not specify exact allowed residue alphabet, sequence-length bounds, invalid-character handling, or request-schema field constraints for the exact Forge callable interface.

### Task-specific formatting

- The documented task format is endpoint-based: protein-structure/alphafold2/predict-structure-from-sequence for sequence-to-structure prediction and protein-structure/alphafold2/predict-MSA-from-sequence for MSA/template generation. Sources: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html

## Output interpretation

### Outputs

- The Forge scope outputs protein structure predictions; the source page and model card describe 3D structure prediction from amino acid sequence. Sources: https://build.nvidia.com/deepmind/alphafold2, https://build.nvidia.com/deepmind/alphafold2/modelcard
- The Forge metadata provided in the brief labels output modalities as structure and json, but the retained primary findings do not define the exact JSON schema or file/object contract. Sources: https://build.nvidia.com/deepmind/alphafold2

### Interpretation

- AlphaFold predictions have varying levels of confidence and should be interpreted carefully. Sources: https://github.com/google-deepmind/alphafold, https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf

### Post-inference validation

- Downstream users should validate scientific conclusions rather than treating outputs as clinically validated results, because upstream documentation states outputs are intended for theoretical modeling only and are not validated or approved for clinical use. Sources: https://github.com/google-deepmind/alphafold
- Evidence gap: The research findings do not specify exact confidence-field names, numeric calibration thresholds, or a post-inference acceptance checklist for the NVIDIA AlphaFold2 NIM output contract.

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### facebook-esmfold-v1 — `insufficient-evidence`

- Task: Protein structure prediction from amino acid sequence
- Criteria: No protocol-matched primary-source benchmark for the exact NVIDIA AlphaFold2 NIM scope and the named alternative was retained in the findings.
- Rationale: The retained primary findings document AlphaFold2 capabilities and qualitative CASP statements but do not provide a directly comparable benchmark against facebook-esmfold-v1 under matched protocol for the exact Forge service scope.
- Comparison conditions: Comparison blocked by missing matched evaluation protocol and missing primary-source benchmark for the alternative within the provided findings.
- Evidence: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/overview.html

### openfold3-nim — `insufficient-evidence`

- Task: Protein structure prediction from amino acid sequence
- Criteria: No protocol-matched primary-source benchmark for the exact NVIDIA AlphaFold2 NIM scope and the named alternative was retained in the findings.
- Rationale: The retained primary findings do not include a direct numeric comparison between the exact callable AlphaFold2 Forge scope and openfold3-nim under matched conditions.
- Comparison conditions: Comparison blocked by missing matched evaluation protocol and missing retained primary-source benchmark for the alternative within the provided findings.
- Evidence: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/overview.html

## Limitations and safety

### Limitations

- The exact upstream checkpoint, model revision, and parameter scale for the NVIDIA-packaged callable Forge variant are not reported in the retained primary findings. Sources: https://build.nvidia.com/deepmind/alphafold2, https://build.nvidia.com/deepmind/alphafold2/modelcard, https://docs.nvidia.com/nim/bionemo/alphafold2/latest/deployment-guide.html
- AlphaFold predictions have varying levels of confidence and should be interpreted carefully. Sources: https://github.com/google-deepmind/alphafold, https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf
- Upstream evidence states AlphaFold's prediction accuracy decreases substantially when median MSA depth is less than about 30 sequences, and increasing MSA depth beyond approximately 100 sequences yields only small additional accuracy gains. Sources: https://nature.com/articles/s41586-021-03819-2
- The Forge source page states use of the AlphaFold2 model is governed by the Apache 2.0 License, while upstream and NVIDIA NGC sources distinguish code under Apache 2.0, model parameters under CC BY 4.0, and additional NVIDIA container/service terms for the packaged NIM; users must reconcile these scope-specific licensing layers. Sources: https://build.nvidia.com/deepmind/alphafold2, https://github.com/google-deepmind/alphafold, https://catalog.ngc.nvidia.com/orgs/nim/teams/deepmind/containers/alphafold2
- Running the packaged service is operationally containerized; NVIDIA deployment documentation identifies Docker image nvcr.io/nim/deepmind/alphafold2 with tag 2.1.0 and GPU visibility configuration via CUDA_VISIBLE_DEVICES. Sources: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/deployment-guide.html

### Safety

- AlphaFold 2 and its output are intended for theoretical modeling only and are not validated or approved for clinical use. Sources: https://github.com/google-deepmind/alphafold
- Users must comply with applicable license and service terms: the Forge source page states the trial service is governed by the NVIDIA API Trial Service Terms of Use, upstream code is under Apache 2.0, model parameters are under CC BY 4.0, and the NVIDIA container listing adds NVIDIA software and AI product terms. Sources: https://build.nvidia.com/deepmind/alphafold2, https://github.com/google-deepmind/alphafold, https://catalog.ngc.nvidia.com/orgs/nim/teams/deepmind/containers/alphafold2
- AlphaFold predictions have varying levels of confidence and should be interpreted carefully. Sources: https://github.com/google-deepmind/alphafold, https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### AlphaFold2 on NVIDIA Build

- URL: https://build.nvidia.com/deepmind/alphafold2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official Forge source page for the exact callable model scope named in the brief.
- Scope: deepmind-alphafold2-nim Forge page
- Supports: identity
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs
- Supports: safety
- Supports: limitations

### NVIDIA AlphaFold2 model card

- URL: https://build.nvidia.com/deepmind/alphafold2/modelcard
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA model card for the exact Forge AlphaFold2 listing.
- Scope: deepmind-alphafold2-nim model card
- Supports: identity
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs
- Supports: limitations

### NVIDIA NIM AlphaFold2 overview

- URL: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA documentation describing AlphaFold2 NIM capabilities and usage framing.
- Scope: NVIDIA AlphaFold2 NIM documentation
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: comparisons

### NVIDIA NIM AlphaFold2 endpoints

- URL: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA endpoint documentation for the AlphaFold2 NIM API.
- Scope: NVIDIA AlphaFold2 NIM API endpoints
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.taskSpecificFormatting

### NVIDIA NIM AlphaFold2 deployment guide

- URL: https://docs.nvidia.com/nim/bionemo/alphafold2/latest/deployment-guide.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA deployment documentation for the AlphaFold2 NIM runtime/container.
- Scope: NVIDIA AlphaFold2 NIM deployment/runtime
- Supports: identity
- Supports: limitations

### DeepMind AlphaFold repository

- URL: https://github.com/google-deepmind/alphafold
- Publisher: Google DeepMind
- Type: `repository`
- Primary because: Canonical upstream repository providing upstream license, confidence, dataset-license, and clinical-boundary statements.
- Scope: Upstream AlphaFold family repository
- Supports: identity
- Supports: researchSummary
- Supports: conditionalUseCases
- Supports: avoidUseCases
- Supports: outputInterpretation.interpretation
- Supports: outputInterpretation.validation
- Supports: limitations
- Supports: safety

### AlphaFold license disclaimer

- URL: https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf
- Publisher: EMBL-EBI / DeepMind
- Type: `official-documentation`
- Primary because: Authoritative license and usage/disclaimer document for AlphaFold data distribution and confidence caution.
- Scope: AlphaFold data/license disclaimer
- Supports: conditionalUseCases
- Supports: outputInterpretation.interpretation
- Supports: limitations
- Supports: safety

### Nature review/source describing AlphaFold2 pipeline

- URL: https://nature.com/articles/s41392-023-01381-z
- Publisher: Nature
- Type: `paper`
- Primary because: Primary research publication used here only for architecture-level description found in the provided research findings.
- Scope: AlphaFold2 architecture description
- Supports: identity
- Supports: inputPreparation.preprocessing

### Nature: Highly accurate protein structure prediction with AlphaFold

- URL: https://nature.com/articles/s41586-021-03819-2
- Publisher: Nature
- Type: `paper`
- Primary because: Canonical AlphaFold methods paper used here only for the specific limitation facts present in the findings.
- Scope: Upstream AlphaFold performance/limitations paper
- Supports: limitations
- Supports: evidenceGaps

### NVIDIA NGC AlphaFold2 container listing

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/deepmind/containers/alphafold2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA container listing documenting additional licensing/terms for the packaged AlphaFold2 NIM.
- Scope: NVIDIA AlphaFold2 NIM container/package terms
- Supports: identity
- Supports: limitations
- Supports: safety

## Evidence gaps

- Evidence gap: No exact-scope numeric benchmark was retained for the callable Forge variant deepmind-alphafold2-nim. Checked primary sources: https://build.nvidia.com/deepmind/alphafold2 (Forge source page), https://build.nvidia.com/deepmind/alphafold2/modelcard (model card), https://docs.nvidia.com/nim/bionemo/alphafold2/latest/overview.html (overview), https://docs.nvidia.com/nim/bionemo/alphafold2/latest/endpoints.html (endpoints), https://docs.nvidia.com/nim/bionemo/alphafold2/latest/deployment-guide.html (deployment guide), and https://nature.com/articles/s41586-021-03819-2 (canonical upstream paper). The provided findings contain no verified table, figure, section, page, or heading with a numeric benchmark explicitly tied to the NVIDIA-packaged Forge/NIM artifact.
- Evidence gap: The retained primary findings do not report the exact upstream checkpoint identifier, immutable revision, or parameter count for the NVIDIA-packaged callable AlphaFold2 Forge variant.
- Evidence gap: The retained primary findings do not specify exact request-schema fields beyond endpoint purpose, nor exact allowed alphabet, sequence-length limit, or invalid-input handling for the Forge callable interface.
- Evidence gap: The retained primary findings do not define the exact output JSON schema, confidence-field names, calibration thresholds, or file/object locations for confidence metrics in the NVIDIA AlphaFold2 NIM outputs.
- Evidence gap: No protocol-matched primary-source comparison benchmark was retained for deepmind-alphafold2-nim versus facebook-esmfold-v1 or openfold3-nim within the provided findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 42 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10690423 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.rcd.clemson.edu/software/applications/protein_prediction/alphafold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10690423 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.rcd.clemson.edu/software/applications/protein_prediction/alphafold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10690423 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC10690423 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.rcd.clemson.edu/software/applications/protein_prediction/alphafold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/deepmind-alphafold2-multimer Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.clore.ai/guides/science-and-research/alphafold2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://uvio.bio/alphafold-architecture Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/deepmind-alphafold2-multimer Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/deepmind/alphafold2/modelcard?signin=true&integrate_nim=true&hosted_api=true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].value must contain a reported numeric result: $.benchmarks[0].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
