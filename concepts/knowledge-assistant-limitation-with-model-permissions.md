---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24109cfef4d6975421fd66c4341842dd963dc9c04d49b0427d4996e4314a2006
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - knowledge-assistant-limitation-with-model-permissions
    - KALWMP
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Knowledge Assistant Limitation with Model Permissions
description: A known limitation where Agent Bricks Knowledge Assistant does not support foundation model Unity Catalog permissions, requiring contact with Databricks account team before enabling the feature if Knowledge Assistant is actively used.
tags:
  - databricks
  - limitations
  - knowledge-assistant
timestamp: "2026-06-19T18:55:28.626Z"
---

# Knowledge Assistant Limitation with Model Permissions

**Knowledge Assistant Limitation with Model Permissions** refers to a known incompatibility between Databricks' [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) and the [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) feature. When account admins restrict access to specific foundation models using Unity Catalog permissions on the `system.ai` schema, Knowledge Assistant does not honor those restrictions. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Overview

Foundation Model Unity Catalog Permissions allow account admins to control which Databricks-hosted foundation models users can access. This is achieved by removing the default `EXECUTE` permission from the `system.ai` schema and selectively granting it on approved individual models. The enforcement applies consistently across pay-per-token endpoints, provisioned throughput endpoints, and batch inference (AI Functions) workloads. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

However, Knowledge Assistant does not support this permission model. This means that even if an admin has restricted access to certain models using Unity Catalog permissions, Knowledge Assistant may still be able to invoke those models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Impact

Organizations that rely on foundation model Unity Catalog permissions for compliance or security reasons must be aware that Knowledge Assistant bypasses these controls. This limitation is particularly relevant for:

- **Export-controlled model families** — Models subject to export regulations may remain accessible through Knowledge Assistant.
- **Vendor-restricted or region-restricted models** — Contractual restrictions on model usage may not be enforced.
- **Corporate policies** — Internal policies prohibiting specific foundation models may be circumvented.

## Recommendation

Databricks advises customers who actively use Knowledge Assistant to contact their Databricks account team before enabling foundation model Unity Catalog permissions. This allows the account team to assess the impact and provide guidance on how to manage the limitation. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) — The feature that Knowledge Assistant does not support.
- [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) — The AI assistant that bypasses model permission restrictions.
- [system.ai Schema](/concepts/systemai-schema.md) — The Unity Catalog schema where model permissions are configured.
- [AI Gateway](/concepts/ai-gateway.md) — An alternative governance tool for rate limits and usage tracking.
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — One of the workload types that properly enforces model permissions.
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Workload type requiring manual deletion of disallowed endpoints.

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
