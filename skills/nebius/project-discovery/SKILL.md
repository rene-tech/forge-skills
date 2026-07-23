---
name: nebius-project-discovery
description: Resolve the active Nebius identity, explicit profile, project, region, network, registry, compute platforms, and existing Serverless resources before creating or changing anything.
---

# Nebius Project Discovery

1. Run `nebius profile current` and `nebius iam whoami --format json`.
2. Confirm the user-selected project ID; do not infer tenant-wide visibility.
3. Inspect project, networks/subnets, registries, compute platforms, and
   `nebius ai endpoint list` / `nebius ai job list`.
4. Return exact IDs and identify missing permissions or capacity.

Use an explicit `--profile` and `--parent-id` for every command. This skill is
read-only and does not authorize resource creation.
