---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f85483fcafb263de21466080206b7fd0358aeac7d4123a3c1bcec4d49ace4a85
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
    - what-is-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-to-databricks-sharing
    - Databricks-to-Databricks
    - Databricks-to-Databricks OpenSharing
    - Databricks-to-Databricks Sharing Protocol
    - Read data shared using Databricks-to-Databricks OpenSharing
    - databricks-to-databricks-sharing-model
    - DSM
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
    - file: what-is-opensharing-databricks-on-aws.md
title: Databricks-to-Databricks Sharing
description: A sharing model where the recipient must be a Databricks user with Unity Catalog; the provider uses the recipient's metastore identifier to create a secure connection.
tags:
  - data-sharing
  - unity-catalog
  - databricks
timestamp: "2026-06-19T21:56:03.890Z"
---

---
title: Databricks-to-Databricks Sharing
summary: A sharing mode within the OpenSharing framework where both the data provider and recipient use Unity Catalog-enabled Databricks workspaces, secured via a sharing identifier with DATABRICKS authentication, requiring no token management.
sources:
  - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  - what-is-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - data-sharing
  - databricks
  - unity-catalog
  - opensharing
aliases:
  - databricks-to-databricks-sharing
confidence: 0.98
provenanceState: merged
inferredParagraphs: 0
---

# Databricks-to-Databricks Sharing

**Databricks-to-Databricks sharing** is a sharing model within the [OpenSharing](/concepts/opensharing.md) framework in which both the data provider and the data recipient use a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace. The connection is secured and managed entirely by Databricks using `DATABRICKS` authentication, without requiring token management from either party. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Unlike [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md), which relies on bearer tokens or OIDC federation, Databricks-to-Databricks sharing uses a **sharing identifier** — a string in the format `<cloud>:<region>:<uuid>` that uniquely identifies the recipient's Unity Catalog [Metastore](/concepts/metastore.md). The provider uses this identifier to create a recipient object with `authentication_type = 'DATABRICKS'`. The shared data can only be accessed from workspaces attached to that specific [Metastore](/concepts/metastore.md). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## How It Works

When the provider grants a share to the recipient, the shared data appears in the recipient's Unity Catalog as a read-only foreign catalog. Updates made by the provider are reflected in near real time without manual refreshes. The recipient does not need to handle credentials, and the provider does not need to distribute or rotate tokens — all identity verification and encryption are handled by the Databricks platform. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

A **provider object** is automatically created in the recipient's Unity Catalog [Metastore](/concepts/metastore.md). Recipients can view providers and their shared shares under **OpenSharing** > **Shared with me** in Catalog Explorer. Provider objects for Databricks-to-Databricks sharing have `authentication_type = DATABRICKS` and their credentials rotate automatically, so recipients never need to update them manually. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Setting Up a Recipient

### Requirements

- The recipient must have access to a Databricks workspace that is enabled for Unity Catalog. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- The provider must have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data to be shared is registered. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- If using a notebook, the compute must run Databricks Runtime 11.3 LTS or above and use standard or dedicated access mode. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Step 1: Obtain the Sharing Identifier

The recipient retrieves their [Metastore](/concepts/metastore.md)'s sharing identifier using Catalog Explorer, the Unity Catalog CLI, or the SQL function `CURRENT_METASTORE`. The identifier has the form `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016`. The recipient sends this string to the provider. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Step 2: Create the Recipient Object

The provider creates a recipient with authentication type `Databricks`. This can be done via Catalog Explorer, SQL, or the Databricks CLI. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

**SQL example**:
```sql
CREATE RECIPIENT recipient_name
USING ID '<sharing-identifier>'
COMMENT 'Optional comment';
```

After creation, the recipient object has `authentication_type = 'DATABRICKS'`. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Supported Assets

Databricks-to-Databricks sharing supports a broader set of asset types than open sharing, including:

- Tables (Delta and managed Iceberg)
- Views (including dynamic views)
- Materialized views and streaming tables
- Unity Catalog volumes
- Unity Catalog AI models
- Notebook files (read-only; recipients can clone and modify them)

All shared assets are read-only for the recipient. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md, what-is-opensharing-databricks-on-aws.md]

## Advantages

- **No token management** – Security is handled entirely by Databricks.
- **Cross-account and cross-cloud sharing** – Works across different Databricks accounts on AWS, Azure, and GCP.
- **Built-in governance** – Recipients can use Unity Catalog to grant or deny access to other users in their organization.
- **Auditing and usage tracking** – Both providers and recipients can monitor share activity through system tables and audit logs.
- **Near real-time updates** – Changes to provider data appear without manual refreshes.

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Comparison with Databricks-to-Open Sharing

| Aspect | Databricks-to-Databricks | Databricks-to-Open |
|--------|--------------------------|---------------------|
| Recipient workspace | Must be Unity Catalog-enabled | Any platform |
| Authentication | Sharing identifier (no tokens) | Bearer token or OIDC federation |
| Asset types supported | Tables, views, volumes, models, notebooks | Tables only |
| Governance for recipient | Full Unity Catalog integration | External connectors |
| Credential rotation | Automatic | Manual via API |
| Provider object creation | Automatic | Not applicable |

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Limitations

- Both parties require a Unity Catalog-enabled Databricks workspace. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- Data sharing between workspaces attached to the **same** Unity Catalog [Metastore](/concepts/metastore.md) does not require OpenSharing — standard Unity Catalog permissions are sufficient. ^[what-is-opensharing-databricks-on-aws.md]
- Each recipient object can only represent a single [Metastore](/concepts/metastore.md). To share data from multiple metastores, separate recipients must be created. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md, what-is-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The overarching protocol for secure data sharing.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer enabling Databricks-to-Databricks sharing.
- [Sharing Identifier](/concepts/sharing-identifier.md) – The [Metastore](/concepts/metastore.md) identifier used to establish a secure connection.
- [Recipient](/concepts/data-recipient.md) – The securable object representing a data consumer.
- Provider – The securable object representing a data supplier (auto-created for recipients).
- Share – A read-only collection of assets shared with recipients.
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) – The alternative flow for non-Databricks recipients.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open protocol (openly available as OpenSharing).

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
- what-is-opensharing-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
2. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
3. [what-is-opensharing-databricks-on-aws.md](/references/what-is-opensharing-databricks-on-aws-adff4826.md)
