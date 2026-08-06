---
name: nebius-project-discovery
description: Resolve the active Nebius identity, explicit profile, project, region, network, registry, compute platforms, and existing Serverless resources before creating or changing anything.
---

# Nebius Project Discovery

Use this skill before planning or changing resources in a Nebius project.

## Read-only workflow

1. Ask which CLI profile and project are in scope. Use both explicitly on every
   command; never infer tenant-wide visibility from one service account.
2. Verify syntax against the installed CLI:

   ```bash
   /usr/local/bin/nebius --help
   /usr/local/bin/nebius ai --help
   /usr/local/bin/nebius ai endpoint create --help
   /usr/local/bin/nebius ai job create --help
   ```

3. Read the selected project and list existing Serverless resources and
   available compute platforms:

   ```bash
   /usr/local/bin/nebius --profile <PROFILE> iam project get <PROJECT_ID> --format json
   /usr/local/bin/nebius --profile <PROFILE> ai list --parent-id <PROJECT_ID> --format json
   /usr/local/bin/nebius --profile <PROFILE> ai endpoint list --parent-id <PROJECT_ID> --format json
   /usr/local/bin/nebius --profile <PROFILE> ai job list --parent-id <PROJECT_ID> --format json
   /usr/local/bin/nebius --profile <PROFILE> compute platform list --parent-id <PROJECT_ID> --all --format json
   ```

4. Resolve the relevant region, subnet, registry, MysteryBox secret metadata
   by ID/name only, platform/preset, and existing endpoint/job IDs.
5. Return a compact inventory and identify missing permissions, capacity, image
   access, network, or secret prerequisites before proposing a change.

## Guardrails

- Discovery is read-only. Do not create, mutate, or delete a resource.
- Never print IAM tokens, secret payloads, kubeconfig material, registry auth,
  endpoint tokens, or signed URLs.
- Stop on authentication or authorization failure. Do not switch credentials,
  profiles, projects, or regions as a workaround.
- Treat live inventory as authoritative and label unavailable scope as unknown.
