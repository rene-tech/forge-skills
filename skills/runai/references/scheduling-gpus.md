# Scheduling, pools, quotas and GPU resources

Start with versioned scheduler/resource-optimization guides in [sources.md](sources.md)
and the matching [KAI documentation/examples](https://github.com/kai-scheduler/KAI-Scheduler).
The full platform manages projects/policies and maps workload intent to scheduler
resources; standalone KAI queues are not a replacement identity/account system.

## Explain a Pending workload with evidence

Evaluate scope/policy first, then per-pool quotas and current borrowing, priority/
preemptibility, gang demand, node allocatable resources, selectors/taints, storage
affinity, actual GPU resources and cloud capacity. Distinguish scheduler fit from
node-autoscaler ability to create a matching VM. Raising quotas cannot create
cloud capacity, and adding nodes cannot fix a forbidden policy.

Guaranteed/deserved quota, maximum limit and over-quota borrowing differ. Fair
share/reclaim behavior depends on queue hierarchy, weights, priority and supported
preemption rules. Demonstrate it with two authorized tenants, finite workloads
and measured allocations. Do not describe quota as permanent dedicated capacity
or idle borrowing as an isolation breach. Check CPU/RAM as well as GPU quotas.

Gang scheduling admits a coordinated group only when its required resources can
fit. Include all ranks/roles and pool placement; inspect PodGroup/queue status
and native events. Do not defeat a gang by launching partial manual Pods.

## Node pools and compatibility

Keep Run:ai node pools, cloud node groups, Kubernetes node labels and GPU classes
distinct. Map them explicitly, with selectors that do not overlap accidentally.
Separate incompatible runtime/driver or sharing modes when required by their
supported configuration; do not impose permanent isolation merely from one test.

Inventory exact GPU SKU, count, compute capability, VRAM, NUMA/topology, driver,
CUDA, Operator/device-plugin/DRA versions and actual allocatable resources.
Compare with the selected executable's native targets and vendor support matrix.
PTX forward compatibility can fail for architecture-specific assumptions; missing
a native target alone is not causal proof. A CUDA compute-kernel error does not
mean the Linux kernel is unsupported. Qualify actual runtime variants rather than
declaring an entire product family unusable.

## Sharing mechanisms are different

| Mechanism | Contract to verify |
| --- | --- |
| Whole GPU | Native allocation/count, exclusive ownership where claimed, full memory available to the workload |
| Run:ai GPU fractions | Exact release's CUDA/fractioning engine, enforced memory/compute behavior, supported GPU and process model |
| Dynamic fractions | Request versus upper memory limit, borrowing/reclaim rules and updated annotation format |
| NVIDIA MIG | Supported hardware/profile, partition ownership, device-plugin strategy, native profile selection and reconfiguration disruption |
| NVIDIA time slicing/MPS | Their own sharing/isolation semantics; neither automatically provides MIG or Run:ai hard memory isolation |

The checked [v3.0 migration guide](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/installation-and-configuration/upgrade/plan-the-upgrade)
requires CUDA-based fractions prerequisites, including r615-or-newer driver,
CUDA13.4 and GPU Operator26.7.1, with the NRI plugin disabled. It also disables
legacy GPU swap/node-level scheduling. This is a **v3.0 migration statement**:
recheck the target support matrix instead of applying these versions universally
or downgrading a working driver based on older guides.

Assign one owner to drivers, toolkit, device plugin, MIG Manager and DRA. Do not
run a second installer over preinstalled cloud drivers without a documented
ownership plan. MIG reconfiguration may require draining and workload disruption;
obtain appropriate authorization and preserve checkpoints.

Sharing acceptance needs real allocation pressure, a bounded denial beyond the
advertised memory cap, concurrent peer correctness and unchanged ownership. A
resource annotation or `nvidia-smi` memory observation alone is not enforcement.
Keep incompatible, unavailable and untested matrix entries distinct.
