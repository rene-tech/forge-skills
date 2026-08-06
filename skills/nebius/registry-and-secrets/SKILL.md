---
name: nebius-registry-and-secrets
description: Prepare digest-pinned Nebius Container Registry images and MysteryBox selectors for Serverless workloads without exposing credentials or secret payloads.
---

# Nebius Registry And Secrets

Use this skill whenever a Serverless endpoint or job needs a private container
image or runtime secrets.

## MysteryBox

1. Reuse an approved existing secret only when its project, payload key, and
   ownership match the workflow; otherwise create a task-scoped secret.
2. Pass only the selector/secret ID and payload key through `--env-secret`,
   `--token-secret`, `--registry-secret`, or the corresponding API fields.
3. Record whether the secret is durable user infrastructure or temporary
   verification state. Never read or print its payload during discovery.

## Container image

1. Preserve the canonical source reference and resolve it to an immutable
   digest:

   ```bash
   crane digest '<SOURCE_IMAGE>'
   ```

2. Confirm the destination project can pull the image. Use a registry
   MysteryBox selector when it is private.
3. Nebius Serverless currently rejects image-reference-derived compute-label
   values longer than 64 characters. If the full endpoint image reference
   exceeds that bound, copy the digest-qualified source into a task-owned short
   alias:

   ```bash
   crane copy '<SOURCE_IMAGE>@sha256:<SOURCE_DIGEST>' '<SHORT_TARGET_IMAGE>:<DIGEST_PREFIX>'
   crane digest '<SHORT_TARGET_IMAGE>:<DIGEST_PREFIX>'
   ```

4. Require the target digest to equal the source digest immediately before
   endpoint/job creation. The alias is a transport workaround, not provenance.
5. Scan or inspect images when project policy requires it. Never place registry
   credentials in build arguments, image layers, commands, or documentation.
6. Remove only task-owned temporary aliases/secrets after their dependent
   endpoints/jobs are deleted, and verify absence.

Do not change IAM, registry access policy, or an existing MysteryBox secret
without explicit authorization. Never print Docker config JSON, registry
passwords, secret payloads, signed URLs, or credential-helper output.
