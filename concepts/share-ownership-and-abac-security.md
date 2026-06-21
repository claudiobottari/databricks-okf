---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0e4419b865cc226deee32a81c1fcf168dc8e1ec60fc15e55da38ac5c9226e16
  pageDirectory: concepts
  sources:
    - manage-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-ownership-and-abac-security
    - ABAC Security and Share Ownership
    - SOAAS
  citations:
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: Share Ownership and ABAC Security
description: The security implication that transferring share ownership to an over-privileged user may allow recipients over-privileged access when ABAC policies are in effect on underlying tables or schemas.
tags:
  - security
  - abac
  - unity-catalog
  - share-ownership
timestamp: "2026-06-19T19:28:33.339Z"
---

# Share Ownership and ABAC Security

**Share Ownership and ABAC Security** refers to the security implications of transferring ownership of a [Delta Sharing](/concepts/delta-sharing.md) share in [Unity Catalog](/concepts/unity-catalog.md), particularly when [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies are applied to the underlying data assets. The share owner's privileges directly influence the access that recipients receive.

## Overview

A *share* is a securable object in Unity Catalog that bundles data assets—such as tables, views, volumes, notebooks, and AI models—for sharing with one or more recipients. The owner of a share has the authority to manage the share and its contents. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Security Impact of Share Ownership

Who the share owner is affects how authorization and security features, such as ABAC policies, are evaluated. When a table or schema is secured by ABAC policies, transferring share ownership to an over-privileged user allows recipients to gain over-privileged access. This is because ABAC policy evaluation is performed in the context of the share owner, not the recipient. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Best Practices

To maintain proper security boundaries when using [ABAC](/concepts/abac-attribute-based-access-control.md) with shares:

- Carefully consider who is assigned as the share owner
- Avoid transferring ownership to users with elevated privileges unless necessary
- Regularly audit share ownership to ensure least-privilege principles are maintained

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that manages shares
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Security policies that evaluate access based on user attributes
- Manage shares for OpenSharing — Operations for viewing, updating, and deleting shares
- [Data Recipients](/concepts/data-recipient.md) — The users or organizations that receive access to shared data
- ABAC Policies — Attribute-based rules controlling access to data assets

## Sources

- manage-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)
