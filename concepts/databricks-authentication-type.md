---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d05fbd22366ee047acc2972bc27986eaabb51b9e4caf9d11c43d74af302de2b5
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-authentication-type
    - DAT
    - Databricks Authentication
    - Databricks Authentication Types
    - Databricks CLI Authentication
    - Databricks CLI authentication
    - Databricks authentication
    - Databricks authentication SDK
    - Databricks authentication profiles
    - Databricks authentication setup
    - Databricks authentication types
    - Authentication types
    - Databricks CLI authentication profiles
    - Databricks authentication types|authentication type
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: DATABRICKS Authentication Type
description: An authentication type for recipient objects that restricts data access to a specific Unity Catalog metastore identified by a sharing identifier, used in Databricks-to-Databricks sharing.
tags:
  - authentication
  - delta-sharing
  - security
timestamp: "2026-06-19T09:38:16.774Z"
---

# DATABRICKS Authentication Type

**DATABRICKS Authentication Type** is a recipient authentication method in [OpenSharing](/concepts/opensharing.md) ([Delta Sharing](/concepts/delta-sharing.md)) that establishes a secure, managed connection between two [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspaces. When a recipient object is created with `authentication_type` of `DATABRICKS`, the shared data can only be accessed on the specific Unity Catalog [Metastore](/concepts/metastore.md) identified by the recipient's sharing identifier. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Overview

Databricks-to-Databricks sharing uses the DATABRICKS authentication type to enable direct sharing between Unity Catalog-enabled workspaces without requiring the provider to manage external tokens or OAuth federation. The recipient is identified by a sharing identifier string in the format `<cloud>:<region>:<uuid>`, which uniquely identifies the recipient's Unity Catalog [Metastore](/concepts/metastore.md). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

This authentication method is one of two sharing modes available in OpenSharing. The alternative is Open Sharing Authentication Type, used for recipients without access to a Unity Catalog-enabled Databricks workspace, which requires the provider to manage token-based authentication (bearer tokens or OIDC Federation). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Creating a Recipient with DATABRICKS Authentication

### Prerequisites

To create a DATABRICKS-type recipient, you must have the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered. The recipient must be created from a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached. If using a notebook, the compute must run Databricks Runtime 11.3 LTS or above with standard or dedicated access mode. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Step 1: Obtain the Recipient's Sharing Identifier

Ask the recipient user to provide the sharing identifier for their Unity Catalog [Metastore](/concepts/metastore.md). The recipient can find this identifier using:

- **Catalog Explorer**: Navigate to Catalog, click the gear icon, select **OpenSharing**, then on the **Shared with me** tab click the organization name and select **Copy sharing identifier**.
- **SQL**: Use the `CURRENT_METASTORE` function in a Databricks notebook or SQL query.
- **CLI**: Use the Databricks Unity Catalog CLI.

The sharing identifier is a string in the format `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016` (cloud, region, and [Metastore](/concepts/metastore.md) UUID). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Step 2: Create the Recipient Object

To create a recipient with DATABRICKS authentication, use one of the following methods:

- **Catalog Explorer**: Click **Catalog** > gear icon > **OpenSharing** > **Shared by me** tab > **New recipient**. Enter the recipient name, select **Databricks** as the recipient type, and paste the sharing identifier.
- **SQL**: Use the `CREATE RECIPIENT` SQL command.
- **CLI**: Use the Databricks Unity Catalog CLI.

The recipient is created with `authentication_type` of `DATABRICKS`. You can optionally add custom recipient properties (key-value pairs) on the recipient's **Overview** tab. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## How It Works

A DATABRICKS-type recipient object represents a data recipient on a specific Unity Catalog [Metastore](/concepts/metastore.md). The sharing identifier in the recipient definition determines which [Metastore](/concepts/metastore.md) can access the shared data. This means:

- Only users on the identified [Metastore](/concepts/metastore.md) can access the shared data.
- The connection is managed by Databricks, eliminating the need for the recipient to manage authentication credentials.
- The provider does not need to distribute tokens or manage OAuth configurations for the recipient. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Comparison with Open Sharing (Token-based) Authentication

| Aspect | DATABRICKS Authentication | Open Sharing Authentication |
|--------|--------------------------|---------------------------|
| Recipient type | Unity Catalog-enabled Databricks workspace | Non-Databricks users or workspaces without Unity Catalog |
| Credential management | Managed by Databricks | Provider-managed (bearer tokens or OAuth federation) |
| Access scope | Specific Unity Catalog [Metastore](/concepts/metastore.md) | Any client with valid credentials |
| Security model | Workspace/[Metastore](/concepts/metastore.md) identity | Token or OIDC-based |

^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) — The framework for sharing data across workspaces and platforms
- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform that enables Databricks-to-Databricks sharing
- Open Sharing Authentication Type — Token-based authentication for non-Databricks recipients
- OIDC Federation — OpenID Connect-based authentication for open sharing recipients
- [Sharing Identifier](/concepts/sharing-identifier.md) — The [Metastore](/concepts/metastore.md) identifier used to create DATABRICKS-type recipients
- Recipient Object — The named object representing a data consumer in Delta Sharing
- [Data Provider vs Data Recipient](/concepts/data-provider-and-data-recipient-roles.md) — Roles in the Delta Sharing model

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
