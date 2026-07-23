---
name: nebius-serverless-endpoints
description: Plan, create, verify, update, and clean up Nebius Serverless endpoints for interactive model inference using an exact model skill and immutable image.
---

# Nebius Serverless Endpoints

1. Load the exact model skill and live Forge regional deployment contract.
2. Confirm project, region, subnet, image digest, platform/preset, preemptible
   choice, port, auth, registry selector, runtime secrets, and cleanup path.
3. Create only after paid-resource confirmation. Prefer preemptible compute for
   short verification when supported.
4. Wait for `RUNNING`; verify health and one representative non-sensitive
   request matching the exact model skill.
5. Record endpoint/operation/instance IDs, image/digest, request shape, output,
   latency, GPU, region, and failure details.
6. Delete temporary endpoints and task-scoped secrets, then verify absence.

Do not send PHI, customer artifacts, unpublished sequences, or credentials
without an approved data-use basis.
