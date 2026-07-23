# Evidence

- Research status: `reviewed`
- Policy: Forge runtime latency/throughput evidence is operational placement data, not model-quality evidence.

## Reviewed public benchmark claims

### Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction

- Primary source: https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1
- Checked: 2026-07-23
- Model/checkpoint scope: Research Boltz-2 evaluation reported by the authors; the Forge endpoint packages Boltz2 v2.2.1 in NVIDIA NIM 1.7.0.
- Dataset and split: FEP+, CASP16, and MF-PCBA evaluations described in the paper / Paper-defined evaluation protocols
- Metric and value: Affinity accuracy and computational efficiency relative to reported physics-based FEP workflows / Authors report approaching FEP accuracy while being at least 1,000 times more computationally efficient
- Direction: context-only
- Provenance: reported
- Conditions: Cross-protocol summary from the paper abstract and evaluations; no Forge reproduction of the scientific benchmark is claimed.
- Caveat: The comparison is protocol- and hardware-dependent and is not an endpoint latency guarantee.
- Caveat: Performance on a new target, assay, or chemical series may differ materially.

## Sources

- Exact model source/model card: https://build.nvidia.com/mit/boltz2
- Boltz-2 paper: https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1 (paper)
- Boltz repository: https://github.com/jwohlwend/boltz (repository)
- NVIDIA Boltz-2 NIM: https://build.nvidia.com/mit/boltz2 (documentation)

The complete public Forge model and exact-skill snapshots are in `forge-model.json` and `forge-skill.json`.
