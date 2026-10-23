# Multi-cluster fleets, Nebius Applications and Spot

Use the matching Run:ai guided same-/multi-cluster installation and networking
requirements in [sources.md](sources.md). One control plane can coordinate worker
clusters; this does not combine their Kubernetes API, storage, quota, networking
or cloud failure domains into one cluster.

## Regional fleet recipe

1. Resolve independent cluster IDs/contexts, cloud projects/regions, control-plane
   trust, ingress/TLS, route domains, image registries and storage boundaries.
2. Register each worker through the documented bootstrap flow, protecting token
   lifetime and credentials. Verify Connected and operand health per cluster.
3. Map projects, namespace ownership, policies, grants, quotas and pools explicitly
   per cluster. Never reuse identifiers because display names match.
4. Mirror exact images and assets into every eligible region; verify registry
   access from actual nodes and the cache's true upstream. Nearby cache alone is
   not proof of local regional availability.
5. Define intentional submission/routing/failover and data-replication behavior.
   Use native capabilities actually available in the edition; do not invent a
   global scheduler or automatic cross-region checkpoint migration.
6. Qualify a real workload and authorized endpoint in each advertised region,
   including local storage and failure behavior. Report measured/unknown gaps.

## Nebius-specific discovery

[Nebius Applications](https://docs.nebius.com/applications) deploys software onto
Managed Kubernetes. The [October13 OSS Run:ai announcement](https://nebius.com/blog/posts/nvidia-run-ai-open-source-nebius-applications)
confirms availability. Discover the application card or authorized catalog/API
entry's exact package/version, parameters, GPU Operator ownership, supported
existing clusters, HA, updates and worker-registration controls before selecting
it. Public product availability does not reveal every package setting.

The older [Nebius integration tutorial](https://docs.nebius.com/3p-integrations/run-ai)
contains version-specific licensed-era and older prerequisite instructions. Use
it as a dated example, not proof OSS Run:ai is unavailable or that every current
cluster needs public worker IPs/old Knative versions. Compare the current
application's supported architecture and managed-Kubernetes networking guidance.

Use the installed Nebius CLI help/API schema to discover supported application
commands; do not invent a catalog command because application releases exist.
Keep the authorized profile/project/region explicit. Lack of public package detail
is an unanswered discovery question, not authorization to install a replacement.

## Interruptible GPU capacity

Spot price/capacity and VM lifecycle are cloud concerns, separate from Run:ai
priority/preemptibility. Distinguish cloud preemption, operator stop, OOM eviction,
node maintenance and scheduler reclaim using actual event/audit timestamps.
A VM stopped near a502 does not establish who stopped it or why.

Set bounded capacity waits and a documented compatible fallback within existing
authorization. Do not silently raise quotas, increase pool size, switch to costly
capacity or restart scientific work. Verify checkpoint availability and the native
resume contract before claiming recovery. A one-replica service on Spot has an
availability limit even with `minReplicas:1`; healthy idle retention is not
guaranteed VM survival. Account for real VM/GPU time, startup and idle cost using
an explicit current price basis; a reserved resource's configured zero price is
not proof of zero economic cost.
