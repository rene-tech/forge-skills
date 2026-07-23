---
name: nebius-registry-and-secrets
description: Prepare digest-pinned Nebius Container Registry images and MysteryBox selectors for Serverless workloads without exposing credentials or secret payloads.
---

# Nebius Registry And Secrets

- Resolve and record immutable source and target image digests.
- When Serverless image labels impose a length limit, copy to a short alias and
  verify source and alias digests match before use.
- Put registry username/password and runtime keys in task-scoped MysteryBox
  secrets; pass selectors, never values.
- Do not print Docker config JSON, tokens, passwords, selectors with sensitive
  names, or signed URLs.
- Delete temporary selectors after dependent workloads are deleted; retain only
  intentionally published aliases and document why.
