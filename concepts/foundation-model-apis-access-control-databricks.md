---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e44ad679f48d725dbfb76a676e5247aa2a08ef4330a2617d03d53d192d93e318
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-access-control-databricks
    - FMAAC(
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Foundation Model APIs Access Control (Databricks)
description: Workspace-level access controls for Foundation Model API endpoints, including admin-only governance modifications, IP allowlists, PrivateLink support, and outbound network policy configuration.
tags:
  - databricks
  - security
  - access-control
timestamp: "2026-06-18T12:24:40.293Z"
---

# Foundation Model APIs Access Control (Databricks)

**Foundation Model APIs Access Control** refers to the set of mechanisms available in [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) to govern which users, workspaces, and networks can invoke Databricks-hosted foundation models. Access control spans workspace-level permissions, [Unity Catalog](/concepts/unity-catalog.md) privilege management, and networking restrictions such as IP allowlists and PrivateLink.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Overview

Foundation Model API endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings for these endpoints. The endpoints also respect any networking-related ingress rules configured on the workspace, including IP allowlists and PrivateLink configurations.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

In addition, you can restrict outbound network access from Model Serving endpoints by configuring network policies. See Manage network policies for details.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Unity Catalog Permissions

To restrict which Databricks-hosted foundation models your organization can invoke, use [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md)(model-uc-permissions). This mechanism allows administrators to grant or deny `EXECUTE` on specific models in the `system.ai` schema to users or groups.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Networking Security

| Control Area | Details |
|--------------|---------|
| **Ingress** | Endpoints respect IP allowlists and PrivateLink configurations configured on the workspace. |
| **Egress** | Outbound network access from Model Serving endpoints can be restricted via network policy configuration. |

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Security Best Practices

- **Admin-only governance**: Only workspace admins should modify endpoint governance settings.
- **Network perimeter**: Use IP allowlists and PrivateLink to limit inbound access to endpoints.
- **Model-level restrictions**: Apply Unity Catalog permissions to control which foundation models each user or group can call.
- **Outbound controls**: If your environment requires strict egress rules, configure network policies for Model Serving.

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Overview of Databricks’ hosted model service
- Foundation Model APIs Compliance and Security — Compliance standards and security profile support
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance layer that powers model permissioning
- Model Serving Limits and Regions — Regional availability and rate limits
- PrivateLink — Network security for workspace endpoints
- Manage Network Policies — Serverless network security

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
