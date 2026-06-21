---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a0a6dafcf5332901ae6ae06cb4679086bdfdd4d950110e79cb54552926dca26
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-access-governance-alternatives
    - FMAGA
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Foundation Model Access Governance Alternatives
description: Alternative governance mechanisms for Databricks foundation models including system.billing for cost tracking, AI Gateway for rate limits, Private Link for secure connectivity, and egress controls — to be used for day-to-day governance rather than model-specific restriction.
tags:
  - databricks
  - governance
  - security
  - ai-gateway
timestamp: "2026-06-19T18:55:45.988Z"
---

# Foundation Model Access Governance Alternatives

**Foundation Model Access Governance Alternatives** refers to the various methods available on Databricks for controlling and governing access to foundation models, beyond the specialized [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) feature. While Unity Catalog permissions on the `system.ai` schema provide model-level access control for legally required restrictions, other tools and techniques address day-to-day governance needs such as cost tracking, rate limiting, and network security. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Overview

Day-to-day governance of foundation model usage typically involves monitoring costs, controlling request rates, and securing network connectivity rather than blocking specific models. Databricks provides several complementary approaches for these purposes, each addressing a different governance concern. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Cost Tracking and Attribution

### `system.billing`

The `system.billing` database provides cost tracking and attribution for foundation model usage. This allows organizations to monitor spending, attribute costs to specific teams or projects, and manage budgets without restricting which models are available. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Rate Limiting and Usage Tracking

### AI Gateway

[AI Gateway](/concepts/ai-gateway.md) provides rate limits and request-level usage tracking for foundation model APIs. This allows administrators to control the volume of API calls, prevent abuse, and track individual request metrics. AI Gateway is the recommended tool for operational governance of model usage patterns. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Network Security

### Private Link and Private Networking

Private Link and private networking solutions enable secure connectivity between the Databricks workspace and foundation model endpoints. These technologies ensure that model requests and responses remain within a private network, reducing exposure to the public internet. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Egress and Network Controls

Egress controls and network-level restrictions limit outbound traffic from the workspace. These controls can prevent data exfiltration and ensure that model interactions comply with organization security policies. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Comparison with Foundation Model Unity Catalog Permissions

The [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) feature is designed specifically for legally required access restrictions — such as blocking export-controlled model families, vendor-restricted models, or models prohibited by corporate policy. Unlike the alternatives described here, it operates at the model object level by granting or revoking `EXECUTE` permission on `system.ai` schema objects. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

The enforcement of Unity Catalog permissions is consistent across pay-per-token, provisioned throughput, and batch inference (AI Functions) workloads, with the exception that provisioned throughput endpoints require manual deletion of disallowed endpoints. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Use Case Summary

| Governance Need | Recommended Alternative |
|---|---|
| Cost monitoring and attribution | `system.billing` |
| Rate limiting and usage tracking | AI Gateway |
| Secure network connectivity | Private Link, private networking |
| Restricting outbound traffic | Egress and network controls |
| Legally required model blocking | Foundation Model Unity Catalog Permissions |

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md)
- [AI Gateway](/concepts/ai-gateway.md)
- Private Link
- [Unity Catalog](/concepts/unity-catalog.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The core service for invoking Databricks-hosted foundation models
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Custom endpoints affected by permission changes
- Batch Inference — AI Functions workload that respects Unity Catalog permissions

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
