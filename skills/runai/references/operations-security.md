# Operations, security, observability and incident diagnosis

Use versioned Run:ai observability/security/maintenance guides from [sources.md](sources.md).
Observe control-plane, Kubernetes, node, application and cloud layers together.
Allocation, GPU utilization, scientific throughput, uptime and billed VM time are
different metrics; preserve their units, timestamps and sources.

## Minimal read-only incident collection

Select the exact context/namespace/workload. Standard commands below are
inspection examples; choose actual owned objects and avoid broad secret dumps.

```sh
kubectl --context "$CONTEXT" -n "$NAMESPACE" get pods -o wide
kubectl --context "$CONTEXT" -n "$NAMESPACE" describe pod "$POD"
kubectl --context "$CONTEXT" -n "$NAMESPACE" logs "$POD" -c "$CONTAINER" \
  --timestamps --since=15m --tail=200
kubectl --context "$CONTEXT" -n "$NAMESPACE" get events \
  --sort-by=.metadata.creationTimestamp
kubectl --context "$CONTEXT" -n "$NAMESPACE" get endpointslices
```

Read selected status/condition fields and previous-container logs when relevant.
Capture UTC, native identity, Pod/Job/controller UID, node/provider identity,
image digest, request status and event times. Protect sensitive logs and redact
private/customer data. Preserve original failures; a successful retry does not
erase them. Avoid global log streaming, unbounded polling and broad load tests.

## Fault-isolation checklist

| Symptom | First evidence |
| --- | --- |
| API401/403 | Token issuer/expiry, action and scope, exact client grant; distinguish control API from serving endpoint |
| Project namespace absent | Native/external namespace mode, controller reconciliation, admission logs and owners |
| Helm pending | Current release/hook status, hook deletion/finalizers, prerequisite readiness, credential lifetime |
| Pending GPU job | Policy/quota/borrowing, gang, placement/taints/storage, allocatable resources, cloud capacity |
| ImagePullBackOff | Exact registry/digest/platform, node pull IAM/Secret, CA/network; not GPU compatibility |
| CUDA/kernel failure | Exact executable targets, GPU SKU/CC, driver/runtime, vendor error; do not patch libraries first |
| Serving502/503 | Connection versus application response, full Knative hierarchy, Pod lifetime, backend reachability |
| OOM/restart | Termination reason, limits, process/GPU usage, tmpfs, node pressure and queue-proxy resources |
| Lost results | Volume/mount identity, output budget/cadence, upload status, authoritative artifact inventory and retention |
| Cloud VM stop | Provider/audit reason and initiator; correlate scheduler/node events without inferring Spot |

## Security and availability design

Use scoped service accounts, least-privilege API roles and endpoint grants, TLS
validation, supported network policies, non-root identities and writable paths
matching UID/GID. Keep control-plane administration separate from app callers.
Test denied cross-project access and accepted authorized calls without customer
credentials. Do not disable TLS/auth/admission to diagnose a routing problem.

Record configuration ownership and credential-safe observability. Terraform state,
plans, Helm values, curl traces and provider debug logs can expose secrets. A
write-only field's state behavior does not guarantee provider logs are safe;
inspect the exact provider/version before using real credentials with debug logs.

Collect platform metrics plus vendor GPU/DCGM signals, actual CPU/RAM, driver/Xid,
disk/filesystem capacity, startup phases, queue/rejection rates and request latency.
Set alerts from advertised service objectives and measured baselines. Include
black-box authorized requests after idle, not just process probes. Avoid exposing
internal GPU topology or credentials in product flows unless it helps the user.

## Close an incident or release

State confirmed cause, correlated evidence and remaining hypotheses separately.
Implement the smallest documented correction through its owner, then rerun only
the meaningful affected checks. Validate one real batch result, sustained serving,
negative authorization, scoped cleanup and required recovery on the exact build.
For capacity/performance claims, report workload, duration/repetitions, GPU/runtime,
science/protocol and cost basis. Do not call an entire platform production-ready
from a schema check, Ready Pod, tiny request or a successful controller rollout.
