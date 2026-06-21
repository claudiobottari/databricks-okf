---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35313654ace55115897a843d2d9bf98c4beef975ea8699acd2dc7953192de2b7
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-enforcement-gap
    - PTEG
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Provisioned Throughput Enforcement Gap
description: A limitation where provisioned throughput endpoints for disallowed models continue serving until manually deleted, unlike pay-per-token and batch inference endpoints which enforce permissions automatically.
tags:
  - databricks
  - provisioned-throughput
  - limitations
timestamp: "2026-06-19T10:39:41.748Z"
---

# Provisioned Throughput Enforcement Gap

The **Provisioned Throughput Enforcement Gap** refers to the difference in how [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) are enforced across different endpoint types. When an account admin restricts model access by revoking `EXECUTE` on the `system.ai` schema and granting it selectively, pay-per-token and batch inference endpoints immediately honor the new permissions. Provisioned throughput endpoints, however, do **not** enforce these restrictions automatically and continue serving the disallowed model until the endpoint is manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How the Gap Manifests

The enforcement gap appears in two scenarios:

1. **After removing `EXECUTE` from the `system.ai` schema**: Pay-per-token and batch inference (AI Functions) calls to all models stop immediately. But provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

2. **After selectively granting `EXECUTE` on approved models**: Only pay-per-token and batch inference endpoints automatically apply the new allow-list. Provisioned throughput endpoints remain unaffected by the permission changes. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

The source documentation explicitly states: "Pay-per-token and batch inference (AI Functions) endpoints automatically enforce the new permissions. Provisioned throughput endpoints do not, so you must manually delete the disallowed endpoints." ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Impact

This gap creates a security blind spot in environments where provisioned throughput endpoints are used to serve restricted models. If an admin revokes access to a model family (e.g., for export control or vendor restrictions), any existing provisioned throughput endpoint for that model remains operational. Users who have access to the endpoint (via workspace permissions) can still make inference calls, bypassing the intended policy. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Mitigation

To close the enforcement gap, account admins must manually delete all provisioned throughput endpoints that serve a disallowed model. The recommended workflow is:

1. Complete the model restriction process (remove `EXECUTE` from `system.ai`, then grant on approved models).
2. Identify all provisioned throughput endpoints that serve models now disallowed.
3. Delete those endpoints through the Databricks UI or API.

Only after deletion is the policy fully enforced. The documentation notes that active endpoints continue serving until removed, so deletion is mandatory. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) – The overall mechanism for restricting model access.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Dedicated endpoints that require manual cleanup.
- [Pay-per-token serving](/concepts/pay-per-token-serving-mode.md) – Endpoint type that enforces permissions automatically.
- [Batch inference (AI Functions)](/concepts/ai-functions-and-batch-inference.md) – Another endpoint type that enforces automatically.
- [system.ai Schema](/concepts/systemai-schema.md) – The Unity Catalog schema where model permissions are managed.

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
