---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f90997f079d1e7d678c93ee0f5bc9ebef03f6de26e1b56b484d0087cae6e759a
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-federation-for-data-sharing
    - OFFDS
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: OIDC Federation for Data Sharing
description: An authentication method using OpenID Connect federation for Databricks-to-Open sharing, supporting both user-to-machine (U2M) and machine-to-machine (M2M) flows, used with tools like Tableau and Power BI.
tags:
  - authentication
  - oidc
  - federation
  - data-sharing
timestamp: "2026-06-19T17:25:01.784Z"
---

# OIDC Federation for Data Sharing

**OIDC (OpenID Connect) federation for data sharing** is an authentication mechanism supported by OpenSharing’s Databricks-to-Open sharing model. It enables data recipients to access shared data using an OIDC token federation flow, replacing the need for a static credential file or bearer token. This approach supports both user‑to‑machine (U2M) and machine‑to‑machine (M2M) authentication patterns. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

In the Databricks-to-Open sharing model, when a data provider configures sharing with OIDC federation, the recipient receives a portal URL instead of an activation link. The recipient uses that URL to authenticate to the provider’s account via the OIDC federation flow. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Key characteristics of OIDC federation for data sharing:

- **No credential file required** – The recipient authenticates through a standard OIDC flow, not by downloading and storing a credential file.
- **Persistent access** – Access continues as long as the provider continues to share the data.
- **Near real‑time updates** – Changes to the shared data are available to the recipient in near real time.
- **Read‑only access** – Recipients can read and copy the shared data but cannot modify the source data.

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Authentication Flows

OIDC federation supports two distinct flows:

### User‑to‑Machine (U2M) Flow

The U2M flow is designed for interactive user scenarios. A person authenticates through a standard OIDC flow, making it suitable for tools like Tableau and Power BI that support OIDC‑based authentication. After successful authentication, users can query and analyze the shared data through those tools. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Machine‑to‑Machine (M2M) Flow

The M2M flow is intended for automated service‑to‑service communication, such as Python client applications that require programmatic access to the shared data. This flow runs without user intervention, enabling automated data pipelines and integrations. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Comparison with Bearer Token Sharing

OIDC federation differs from bearer‑token‑based [OpenSharing](/concepts/opensharing.md) in several important ways:

| Feature | Bearer Token | OIDC Federation |
|---|---|---|
| **Credential delivery** | Activation URL to download a credential file | Portal URL for OIDC authentication |
| **Authentication** | Static bearer token | Dynamic OIDC token federation |
| **Token management** | Provider manages expiration (max 1 year) | Standard OIDC lifecycle |
| **Supported clients** | Databricks, Apache Spark, pandas, Power BI | Tableau, Power BI (U2M), Python apps (M2M) |

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Getting Access

To access data shared via OIDC federation:

1. The data provider creates a recipient and a share in their Databricks account.
2. The provider sends you a portal URL (not an activation link) over a secure channel.
3. You use the URL to authenticate through the OIDC federation flow.
4. Access persists as long as the provider continues sharing the data.
5. You can read and copy the shared data, but you cannot modify the source data.

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Supported Clients

OIDC federation for data sharing supports the following client types:

- **Tableau** – U2M flow for interactive analytics.
- **Power BI** – U2M flow for business intelligence workloads.
- **Python client applications** – M2M flow for automated data access.

Each client type has its own implementation details, documented separately. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The open standard for secure data sharing that supports OIDC federation.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for OpenSharing data exchange.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer for Databricks-to-Databricks sharing.
- [Data Recipients](/concepts/data-recipient.md) – Users or organizations that receive shared data.
- Data Providers – Users or organizations that share data via OpenSharing.

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
