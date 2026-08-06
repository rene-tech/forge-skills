---
name: nebius-serverless-endpoints
description: Plan, create, verify, update, and clean up Nebius Serverless endpoints for interactive model inference using an exact model skill and immutable image.
---

# Nebius Serverless Endpoints

Use this skill for interactive containers that remain addressable until
stopped or deleted.

## Plan

1. Load the exact model skill and, for Forge models,
   `$nebius-forge-model-deployment`.
2. Confirm the explicit CLI profile, project, region, subnet, immutable image
   or verified short alias, platform/preset, preemptible/on-demand choice,
   container command/port, public/private networking, auth mode, registry
   selector, runtime secret selectors, health route, and cleanup path.
3. Explain billing and interruption behavior and obtain confirmation before
   creating the paid resource.
4. Check the installed CLI before constructing the command:

   ```bash
   /usr/local/bin/nebius ai endpoint create --help
   ```

## Create and verify

```bash
/usr/local/bin/nebius --profile <PROFILE> ai endpoint create \
  --parent-id '<PROJECT_ID>' \
  --name '<ENDPOINT_NAME>' \
  --image '<DIGEST_OR_VERIFIED_SHORT_ALIAS>' \
  --platform '<PLATFORM>' \
  --preset '<PRESET>' \
  --container-command '<ENTRYPOINT>' \
  --args '<ARGUMENTS>' \
  --container-port '<PORT>' \
  --auth token \
  --token-secret '<TOKEN_SECRET_SELECTOR>' \
  --registry-secret '<REGISTRY_SECRET_SELECTOR>' \
  --subnet-id '<SUBNET_ID>' \
  --public
```

Omit optional flags rather than inserting empty values. Add `--preemptible`
only when interruption is acceptable.

1. Record the endpoint and operation IDs, project/region, platform/preset,
   preemptible choice, image source digest and actual endpoint reference.
2. Poll `nebius ai get <ENDPOINT_ID> --format json` until a terminal state.
3. Read only non-secret logs with
   `nebius ai logs <ENDPOINT_ID> --tail 200 --timestamps`.
4. Verify the health route and one representative synthetic/public request
   using the exact model skill. Record status, response shape, and latency.
5. For an update, first capture the current config and rollback image, then
   repeat readiness, health, and sample-request verification.
6. Delete task-owned temporary endpoints and verify absence; delete temporary
   aliases and selectors only after dependents are gone.

Endpoint creation or `RUNNING` alone is not deployment success. Stop on
authentication, authorization, capacity, or quota failure. Never send PHI,
customer artifacts, unpublished sequences, endpoint tokens, or credentials
without an approved data-use basis.
