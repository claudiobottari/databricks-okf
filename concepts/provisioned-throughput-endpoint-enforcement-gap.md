---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73f63336942ec27e22bb3215bf357ff2db6ab56558405ecee584f3637330d15b
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-endpoint-enforcement-gap
    - PTEEG
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Provisioned Throughput Endpoint Enforcement Gap
description: A limitation where provisioned throughput endpoints do not automatically enforce foundation model Unity Catalog permissions and must be manually deleted by admins, unlike pay-per-token and batch inference endpoints which enforce automatically.
tags:
  - databricks
  - provisioned-throughput
  - limitations
timestamp: "2026-06-19T18:55:24.878Z"
---

# Provisioned Throughput Endpoint Enforcement Gap

The **Provisioned Throughput Endpoint Enforcement Gap** refers to the difference in how Unity Catalog permissions are enforced across different types of Databricks-hosted foundation model endpoints. When account admins restrict model access using foundation model Unity Catalog permissions, pay-per-token and batch inference (AI Functions) endpoints automatically stop serving disallowed models, but provisioned throughput endpoints do not—they continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How the Gap Arises

Foundation model Unity Catalog permissions rely on removing the `EXECUTE` permission from the `system.ai` schema and selectively granting it on approved models. After this change:

- **Pay-per-token endpoints** stop serving disallowed models immediately.
- **Batch inference (AI Functions)** calls stop immediately.
- **Provisioned throughput endpoints** continue serving the disallowed models because they do not automatically enforce schema-level permission changes. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

This creates a window (or permanent state, if not addressed) where users can still invoke a provisioned throughput endpoint that serves a model that has been blocked at the schema level.

## Required Manual Step

To close the gap, admins must **manually delete** any existing provisioned throughput endpoints that serve a disallowed model. The source documentation states:

> Delete all provisioned throughput endpoints that serve a disallowed model. Active endpoints continue serving until removed.

^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

No automated enforcement is available for provisioned throughput endpoints. Admins should review all active provisioned throughput endpoints after changing permissions and remove those associated with restricted models.

## Implications

- **Security/compliance risk**: A disallowed model may remain accessible via a provisioned throughput endpoint even after the admin has blocked it via Unity Catalog permissions.
- **Operational burden**: Admins must track which endpoints exist and manually clean them up as part of the permission change workflow.
- **Consistency gap**: Unlike pay-per-token and batch inference, provisioned throughput endpoints are not covered by the automated enforcement model.

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) – The feature that controls which models users can invoke.
- [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md) – A dedicated endpoint type that does not automatically enforce schema-level permissions.
- [Pay-per-token Endpoint](/concepts/pay-per-token-endpoints.md) – An endpoint type that automatically enforces schema-level permissions.
- [Batch Inference (AI Functions)](/concepts/ai-functions-and-batch-inference.md) – Another workload type that automatically enforces permissions.
- [Model Governance](/concepts/ai-governance.md) – Broader policies for restricting model access.

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
