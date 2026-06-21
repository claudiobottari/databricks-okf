---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0845a3db62c94a7f243c7fed19cf7e3c534f84de059ccdad8ca6f54d21c5c9dd
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-with-oidc-federation
    - OWOF
    - OpenSharing OIDC Federation
    - Open ID Connect (OIDC) federation
    - Reading shared data with OIDC federation
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: OpenSharing with OIDC Federation
description: An authentication method for Databricks-to-Open sharing using OpenID Connect (OIDC) token federation, supporting both User-to-Machine (U2M) and Machine-to-Machine (M2M) flows.
tags:
  - data-sharing
  - oidc
  - authentication
  - federation
timestamp: "2026-06-19T21:56:46.541Z"
---

# OpenSharing with OIDC Federation

**OpenSharing with OIDC Federation** is a method for accessing shared data using the OpenSharing protocol where authentication is handled through OpenID Connect (OIDC) federation rather than bearer tokens. This approach is part of the Databricks-to-Open sharing model, enabling recipients to access shared data using any compatible tool, including Tableau and Power BI.

## Overview

OpenSharing with OIDC Federation is one of two authentication mechanisms available in the Databricks-to-Open sharing model. When a data provider configures sharing using OIDC federation, recipients authenticate to the data provider's account using an OIDC token federation flow instead of downloading and managing credential files. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Access persists as long as the provider continues to share the data. Updates to the shared data are available to recipients in near real time. Recipients can read and make copies of the shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Authentication Flows

OIDC Federation for OpenSharing supports two distinct authentication flows depending on the use case:

### User-to-Machine (U2M) Flow

The U2M flow is designed for interactive tools such as Tableau and Power BI, where a human user authenticates to access the shared data. Recipients use the URL sent by the data provider to authenticate. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Machine-to-Machine (M2M) Flow

The M2M flow is designed for automated client applications, such as Python-based applications, where the application itself authenticates programmatically. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Comparison with Bearer Token Authentication

| Feature | OIDC Federation | Bearer Token |
|---------|----------------|--------------|
| Authentication method | OIDC token federation | Credential file with bearer token |
| Token management | Provider-managed | Provider-managed |
| Token rotation | Handled through federation | Provider handles expiration and rotation |
| Token validity | As long as sharing continues | Maximum one year after creation |
| Credential file required | No (uses URL) | Yes (downloadable once) |

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Accessing Shared Data

To access data shared using OIDC Federation:

1. The data provider sends you a portal URL over a secure channel.
2. You use the URL to authenticate to the data provider's account.
3. You can then read the shared data using supported tools.

### For Tableau and Power BI

To learn how to access and read shared data using the OIDC token federation flow in Tableau and Power BI, see the documentation on reading data shared over OIDC federation in a U2M flow. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### For Python Client Applications

To learn how to access and read shared data using the OIDC token federation flow in a Python client app, see the documentation on reading data shared over OIDC federation in an M2M flow. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Data Provider Operations

On the provider side, setting up OIDC Federation involves:

1. Creating a *recipient* in their Databricks account to represent the users who will access the data.
2. Creating a *share*, which represents the tables, volumes, and views to be shared.
3. Sending the recipient an activation URL or portal link over a secure channel.

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — The sharing model for recipients using any tool
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — Sharing between Databricks workspaces with Unity Catalog
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for OpenSharing
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution required for Databricks-to-Databricks sharing
- Audit and monitor data sharing — Tracking data access through audit logs

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
