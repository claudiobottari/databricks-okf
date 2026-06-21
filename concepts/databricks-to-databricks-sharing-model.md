---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a23caa7c7b449cdf1e34c4e97527ab0cdc5e42f78ac5b6b0e89f2114c278b8ae
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-databricks-sharing-model
    - DSM
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Databricks-to-Databricks Sharing Model
description: A sharing model where both the data provider and recipient use Databricks workspaces with Unity Catalog, using a metastore sharing identifier to establish a secure connection.
tags:
  - data-sharing
  - unity-catalog
  - databricks
timestamp: "2026-06-19T13:51:30.587Z"
---

# Databricks-to-Databricks Sharing Model

**Databricks-to-Databricks sharing model** is one of two models in [OpenSharing](/concepts/opensharing.md) for sharing data across organizational boundaries. In this model, both the data provider and the data recipient are Databricks users with workspaces enabled for [Unity Catalog](/concepts/unity-catalog.md). Instead of requiring credential files or activation URLs, the data provider creates a secure sharing connection using the recipient's [Metastore](/concepts/metastore.md) sharing identifier, and the shared data becomes automatically discoverable in the recipient's workspace. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## How It Works

In the Databricks-to-Databricks sharing model, the process follows these steps:

1. The data recipient locates a unique identifier for their Unity Catalog [Metastore](/concepts/metastore.md) — the *sharing identifier* — and sends it to the data provider. The sharing identifier uses the format `<cloud>:<region>:<uuid>`, for example `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

2. The data provider creates:
   - A *recipient* in their Databricks account to represent the receiving organization and its users.
   - A *share*, which is a representation of the tables, volumes, and views to be shared. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

3. The shared data becomes automatically discoverable in the recipient's Databricks workspace. No credential file or activation URL is required. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

4. If necessary, the recipient's team can configure granular access control on the shared data for their users, similar to managing permissions on any other securable object in Unity Catalog. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Obtaining the Sharing Identifier

Recipients can obtain their sharing identifier using either Catalog Explorer or a SQL query.

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared with me** tab, select your Databricks sharing organization name in the upper right, and select **Copy sharing identifier**. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Using SQL

Use the default SQL function `CURRENT_METASTORE` in a notebook or Databricks SQL query. If using a notebook, it must run on a standard or dedicated access mode in the workspace you will use to access the shared data: ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

```sql
SELECT CURRENT_METASTORE();
```

## Accessing Shared Data

Because Databricks manages the secure connection in this model, no credential file is required. The shared data is automatically discoverable in your Databricks workspace. To learn how to find, read, and manage that shared data, see Read data shared using Databricks-to-Databricks OpenSharing (for recipients). ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Auditing

If you have access to a Databricks workspace, you can use Databricks audit logs to understand who in your organization is accessing which data using OpenSharing. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Comparison with Databricks-to-Open Sharing

| Feature | Databricks-to-Databricks | Databricks-to-Open |
|---------|--------------------------|---------------------|
| Recipient technology | Must be a Databricks workspace user with Unity Catalog | Can use any tool (including Databricks) |
| Authentication method | [Metastore](/concepts/metastore.md) sharing identifier | Activation URL or portal link for credential download |
| Setup process | Recipient provides sharing identifier to provider | Provider sends activation link or portal URL to recipient |
| Data discovery | Automatic in recipient's workspace | Requires credential file or OIDC federation |
| Access control | Granular permissions configurable in recipient's workspace | Limited to the shared data set |

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Best Practices

- **Use VPC gateway endpoints or interface endpoints for S3** instead of NAT gateways for in-region storage access whenever possible to reduce costs and enhance security. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Ensure notebooks used to retrieve the sharing identifier** run on a standard or dedicated access mode in the workspace that will access the shared data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Configure granular access control** on shared data within your workspace using standard Unity Catalog permissions. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Limitations

- The data provider must be a Databricks user running on Databricks infrastructure — shared data is not provided by Databricks directly. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- Databricks may collect information about data recipients' use of and access to the shared data (including identifying any individual or company who accesses the data) and may share it with the applicable data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing
- [Databricks-to-Open Sharing Model](/concepts/databricks-to-open-sharing-model.md) — The alternative sharing model for non-Databricks recipients
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer required for Databricks-to-Databricks sharing
- Read data shared using Databricks-to-Databricks OpenSharing (for recipients) — Detailed instructions for accessing shared data
- Audit and monitor data sharing — Using audit logs to track data access

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
