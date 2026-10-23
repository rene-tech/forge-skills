# Installation, HA, air gap and upgrades

Use the target version's installation/support matrix and [source map](sources.md).
Pin control plane, workers, Kubernetes, ingress, Knative, databases, GPU Operator
and drivers independently; compatibility is not transitive.

## Installation recipe

1. Inventory existing releases/CRDs/namespaces and choose the documented guided
   installer or Helm path. Decide control-plane/worker placement and owners.
2. Resolve DNS, TLS chains, ingress/Gateway support, identity, pod/service CIDRs,
   proxy/egress/CA trust, registry access, node roles, persistent storage, database
   and metrics dependencies. Do not replace existing compatible operators.
3. Prepare exact chart/images and effective values. Render CRDs and hooks; inspect
   immutable fields, namespaced resources, selectors, resource requests and trust.
4. Apply through the authorized configuration owner and observe exact readiness
   blockers. Test native project creation, scoped storage, CPU/GPU work and serving.

Standard Helm inspection, using generic parameters:

```sh
helm show chart "$CHART" --version "$CHART_VERSION"
helm show values "$CHART" --version "$CHART_VERSION"
helm template "$RELEASE" "$CHART" --version "$CHART_VERSION" \
  --namespace "$NAMESPACE" --include-crds -f "$REVIEWED_VALUES"
helm status "$RELEASE" --namespace "$NAMESPACE"
helm history "$RELEASE" --namespace "$NAMESPACE"
```

Rendering can contain credentials. Protect its output; inspect selected fields,
never post full values/Secret manifests. For Terraform/GitOps, retain reviewed
plans and frozen consumed files. Do not edit external inputs during an active
saved-plan apply or let short-lived credentials expire in a long queued plan.

For a stalled release, identify the blocking Deployment/Job/hook, its owners,
deletion timestamp/finalizers and dependent Pods. Read current Helm revision
status before retrying. Do not skip validation or remove finalizers merely to
finish an install. Separate chart rendering, hook waiting, image startup and
controller reconciliation in the time breakdown.

## Availability and disconnected operation

HA includes supported component replication, placement/anti-affinity, disruption
budgets, ingress, database/storage availability and tested restore. Three Pods on
one failure domain are not regional resilience. Size CPU/system pools for real
prerequisites and recovery; an empty GPU pool should not hide blocked CPU hooks.

For air gap, use the matching installer artifacts/templates. Mirror all required
images unchanged, including CRDs' operands, hooks, init/validation Jobs and platform
manifests. Verify digest/platform and registry CA/authentication on target nodes.
Separately localize model weights and supported offline identity/package
dependencies. Mirroring an image does not remove its runtime model-download or
entitlement requirements. Distinguish supported offline NIM/operator/custom-server
modes rather than inventing a proxy.

## Upgrade recipe

Read [upgrade planning](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/installation-and-configuration/upgrade/plan-the-upgrade)
and matching source `docs/installation-and-configuration/upgrade/`. Inventory
running and pending work before any disruption; retain configuration, database,
metrics, credential recovery and required data backups, with restore evidence.
Review release hops, version skew, CRD/database migrations, driver/fractions and
legacy-workload changes. A Helm rollback does not undo every schema migration.

The checked v3.0 guide upgrades the control plane before cluster components and
requires explicit fractions/legacy-workload migrations. Follow the target guide's
actual compatibility and maintenance instructions, not a perpetual hard-coded
version list. Check whether operator prerequisites and fractions are usable
before/after each stage; retain existing independent DRA/driver ownership.

Close out with connected workers, authorization, namespaces, real artifact
delivery, authenticated inference after idle, quota/preemption behavior and
metrics. Preserve failures and mark unavailable features honestly.
