---
name: nebius-forge-model-deployment
description: Turn one exact Forge model and live supported region/GPU cell into a user-owned Nebius Serverless endpoint plan with immutable image provenance, verified short aliases, secrets, sample inference, and cleanup.
---

# Forge Model To Nebius Serverless

Load this after an exact Forge model skill is selected and the user wants a
dedicated endpoint in their own Nebius project.

## Live deployment contract

1. Re-fetch the exact model, inference routes, and regional-deployment
   resources from Forge. Repository skills describe reviewed knowledge; these
   live APIs are authoritative for current images, support, regions, GPUs,
   pricing, and required runtime secrets.
2. Select only a currently supported region/GPU cell backed by readiness or
   inference evidence. Do not convert an unsupported, experimental, hidden,
   or entitlement-blocked cell into a deployment claim.
3. Require an immutable regional source image of the form
   `cr.<region>.nebius.cloud/...@sha256:<digest>`. Record model slug,
   `versionKey`, region, GPU, source image, license, stability, required
   secrets, runtime port/health route, request contract, and measured Forge
   evidence separately from public model-quality benchmarks.
4. Prefer the Forge model deployment-plan endpoint when it is available. Treat
   any returned CLI or console URL as a handoff for a user-owned resource, not
   evidence that Forge created or verified the endpoint.

## Image-reference limit

Nebius Serverless currently rejects image-reference-derived compute-label
values longer than 64 characters. When the chosen reference exceeds that
bound:

1. Load `$nebius-registry-and-secrets`.
2. Preserve the canonical digest-qualified source.
3. Copy it to a task-owned target reference no longer than 64 characters.
4. Verify the target resolves to the exact source digest immediately before
   endpoint creation.
5. Use the short target only as transport; keep the canonical source in the
   provenance record and delete a temporary alias only after its endpoint is
   gone.

## Create, test, and clean up

1. Load `$nebius-project-discovery` and `$nebius-serverless-endpoints`.
2. Resolve project, region, subnet, platform/preset, registry selector, runtime
   secret selectors, endpoint auth, preemptible choice, and expected billing.
3. Obtain confirmation before creating the paid endpoint.
4. Wait for a terminal ready state, call the declared health route, and send
   one representative synthetic/public request formatted by the exact model
   skill.
5. Record endpoint/operation IDs, region/GPU, platform/preset, preemptible
   choice, canonical and actual image references, source/resolved digests,
   request shape, output validation, latency, and any failure.
6. Delete task-owned temporary endpoints, aliases, and selectors in dependency
   order and verify absence.

Never print Nebius IAM tokens, endpoint tokens, registry credentials,
MysteryBox payloads, API keys, signed URLs, or private model data. Do not call a
deployment working until readiness, health, and a representative inference all
succeed.
