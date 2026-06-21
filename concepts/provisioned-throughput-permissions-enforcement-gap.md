---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2d83f85957c9c61c2b2bb9bedb7e6e52aad10a9573bb9b30d60bd244ad897c4
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-permissions-enforcement-gap
    - PTPEG
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Provisioned Throughput Permissions Enforcement Gap
description: A limitation where provisioned throughput endpoints do not automatically enforce foundation model Unity Catalog permissions and require manual deletion of disallowed endpoints.
tags:
  - limitation
  - permissions
  - provisioned-throughput
timestamp: "2026-06-18T12:26:02.628Z"
---

---
title: Provisioned Throughput Permissions Enforcement Gap
summary: When foundation model Unity Catalog permissions are applied, provisioned throughput endpoints do not automatically enforce the new permission changes; they continue serving until manually deleted, creating an enforcement gap.
sources:
  - foundation-model-unity-catalog-permissions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - permissions
  - unity-catalog
  - foundation-models
aliases:
  - provisioned-throughput-permissions-enforcement-gap
  - PTPEG
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Provisioned Throughput Permissions Enforcement Gap

The **Provisioned Throughput Permissions Enforcement Gap** is a behavior that occurs when an administrator uses [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) to restrict access to Databricks-hosted foundation models. After removing the default `EXECUTE` permission from the `system.ai` schema, pay-per-token and batch inference (AI Functions) calls to all models stop immediately. However, provisioned throughput endpoints do not automatically enforce the new permissions; they continue serving until an administrator manually deletes the disallowed endpoints. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Why the Gap Exists

Provisioned throughput endpoints are pre-allocated compute resources with their own endpoint configurations. Permission changes applied through Unity Catalog on the `system.ai` schema or individual model objects do not propagate to existing provisioned throughput endpoints. As a result, those endpoints remain operational even after the schema-level `EXECUTE` privilege is revoked. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Impact

If an administrator removes `EXECUTE` on the `system.ai` schema (Step 1 of the model restriction workflow), pay-per-token and batch inference workloads are blocked immediately. Any provisioned throughput endpoints serving a now-disallowed model will continue to serve inference requests until they are manually deleted. This creates a period during which the intended access restrictions are not fully enforced. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How to Close the Gap

The documented mitigation is to explicitly delete all provisioned throughput endpoints that serve a disallowed model. This is described as Step 3 in the enforcement process: "Remove disallowed provisioned throughput endpoints." ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

The complete workflow is:

1. Remove `EXECUTE` permission from the `system.ai` schema.
2. Grant `EXECUTE` on individual approved models.
3. **Manually delete** all provisioned throughput endpoints that serve a model not on the allow-list.

Only after Step 3 is complete are provisioned throughput endpoints fully compliant with the new permission policy. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Example Scenario

An organization wants to block all models from model provider X. The admin removes `EXECUTE` on `system.ai`. Pay-per-token calls to model X stop instantly. However, if the team previously created a provisioned throughput endpoint for model X, that endpoint continues to serve requests. The gap persists until the admin deletes that endpoint. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Best Practice

When implementing foundation model Unity Catalog permissions, plan the enforcement rollout to include a manual audit and cleanup of all existing provisioned throughput endpoints before or immediately after revoking the schema-level permission. Use the system.billing table to identify which endpoints are actively consuming provisioned throughput for models that will be restricted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) — The overall feature for restricting model access
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — The endpoint type that requires manual permission enforcement
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Endpoints that automatically enforce permission changes
- [Batch inference (AI Functions)](/concepts/ai-functions-and-batch-inference.md) — Workloads that automatically enforce permission changes
- [AI Gateway](/concepts/ai-gateway.md) — Alternative governance approach for rate limits and usage tracking

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
