# Measurement and comparison contract

## Preserve the run

Retain the redacted config, AIPerf version, exact NIM image/profile/model,
hardware/replicas, client resources/location, dataset/tokenizer revisions,
timestamps, warmup, stopping conditions and original errors. Keep the AIPerf
summary JSON/CSV, per-request JSONL and logs. Preserve actual outputs privately
when they contain request data; inspect artifacts for secrets before sharing.

In the checked release, common artifacts include `profile_export_aiperf.json`,
`profile_export_aiperf.csv` and `profile_export.jsonl`. Read the actual schema:
metric values carry units and unavailable fields need not exist. Do not infer
zero error, zero queue time or zero GPU usage from missing/stale telemetry.

## Report comparable quantities

| Quantity | Required interpretation |
|---|---|
| TTFT | Client-observed time to first output; includes the measured network, queue and service path. Streaming required. |
| Inter-token latency | Use AIPerf's exact metric definition. Stream chunks need not be individual tokens; report tokenization/chunking assumptions. |
| Request latency | End-to-end client request duration, distinct from server-only compute. |
| Output tokens/s | Aggregate generated-token throughput over the tool's measurement window, distinct from per-user decode rate. |
| Requests/s | Completed requests per window; report failed/cancelled counts separately. |
| Goodput | Requests/s meeting all declared SLO thresholds; include the thresholds and attainment fraction/denominator. |
| ISL/OSL | Observed distributions, including template/token-count policy; never just requested means. |
| Cost | Measured billed/allocated resource time and sourced price, separated from inference-only time; missing prices stay unknown. |

Include successful and failed counts, actual duration, p50/p95/p99 when supported
by enough observations, variability and the first failed/untested load. A smoke
sample cannot support a strong tail-latency or sustainable-capacity claim. Do not
average percentiles across runs; retain per-run values or recompute from suitable
raw records with an explicit method. Repeat only when required by the requested
confidence or when unresolved variance/failures justify it.

For a latency SLO, select the highest *measured* load satisfying latency,
attainment and error requirements. Separate a measured operating point from a
production recommendation with headroom. Saturation, overload recovery,
multi-tenant isolation, cancellations and autoscaling/draining need separate
evidence if claiming shared-service capacity.

## Comparison boundaries

Hold workload, protocol, image/model/tokenizer, precision, profile, hardware,
parallelism, cache policy, replicas and client path fixed when attributing a
change. Otherwise label all changed factors and avoid a causal speedup claim.
Reasoning tokens, EOS behavior, generated lengths and prefix sharing can change
the useful work even when the model name matches.

Keep model load/startup and warmup separate from steady-state results. Public
gateway timing is not automatically backend timing. High CPU or low GPU activity
is a lead, not proof of a bottleneck; corroborate with traces/telemetry from the
same run. A profiler may affect the workload and needs its own comparison scope.

Performance does not measure output quality. MLPerf compliance requires the
corresponding MLCommons rules, harness, accuracy and submission requirements;
an AIPerf run alone must never be labelled an MLPerf result.

## Minimal result summary

State endpoint/version/workload scope; actual requests/errors and token lengths;
latency distributions with units; throughput/goodput with SLOs; measured load and
client/server limits; artifact locations; and what remains untested. Separate
observation, interpretation and recommendation. Never invent benchmark numbers
to illustrate an actual result.

Sources: [AIPerf metrics](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/metrics-reference.md),
[export schema](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/reference/json-export-schema.md),
[reproducibility](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/reproducibility.md),
[NIM metrics](https://docs.nvidia.com/nim/benchmarking/llm/metrics).
