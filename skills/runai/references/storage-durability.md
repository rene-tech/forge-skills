# Storage, checkpoints and artifact delivery

Use the release's shared-storage/workload-assets guides and the storage vendor's
CSI/access-mode documentation. A registered cluster, Bound PVC or successful
mount is only one layer of the durability contract.

## Storage design and inspection

Map project to actual namespace, claim, storage class, volume, filesystem and
mount path. Check access mode, binding mode, reclaim policy, capacity, encryption,
backup and regional failure domain. A local hostPath is tied to a node; a PV's
declared capacity does not enforce a host filesystem quota. Cross-region clusters
do not automatically share the same data or access controls.

Match PV node affinity to nodes with a **verified mounted filesystem**. A label
is useful evidence only when its producer actually mounts that filesystem. Do
not label unmounted CPU/GPU nodes as storage-ready to satisfy scheduling.

Use the image's real UID/GID and least-privilege permissions after the filesystem
is mounted. Preserve existing data; avoid a recursive permission reset over shared
weights/customer output. Keep read-only model assets, mutable caches and result
directories separate. Verify image disk, cache, tmpfs and output headroom; tmpfs
consumes memory, and an `emptyDir` size limit is not a memory reservation.

## Checkpoint and resume

Confirm the application's actual checkpoint format, flush interval, atomicity,
runtime compatibility and restart command. A fresh job must not require a missing
checkpoint; continuation flags belong to a verified existing checkpoint. Record
progress and integrity before interruption, then prove the resumed run advances
from the prior state and produces the complete intended result.

Native preemption or Spot rescheduling is not itself checkpoint recovery.
Determine who detects interruption, stores state, resubmits and verifies results.
If the platform/app has no supported automatic resume contract, report that gap
instead of adding a second controller or silently replaying work from step zero.

## Retrieving completed results

Completed Pods cannot normally support `kubectl exec` or `kubectl cp`. Prefer
the documented storage/download interface. When needed, create a bounded native
Run:ai **CPU** training inspector using an existing standard image, no GPU,
read-only existing output PVC and a finite standard command such as `sleep`.
Use the native API for creation/deletion; keep it in the same authorized project.
Ensure CPU placement is actually storage-compatible before submission.

Copy the real trajectory/checkpoint/log/results, retain sizes and integrity
checks, and parse them using the application's official tools. A nonempty log
does not validate a trajectory; an empty output may indicate failure or legitimate
cadence and must be explained against the requested protocol. Do not replace
scientific validation with a fixture hash or a container exit code.

Delete owned temporary inspectors through the native lifecycle after retrieval.
Confirm physical cleanup separately from history retention. Preserve failed-run
evidence and user data; never delete a PVC/bucket merely because its workload was
cancelled or soft-deleted. Cancellation may leave a supported resume path.
