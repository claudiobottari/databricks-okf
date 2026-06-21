---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e79ea5b17fdf415594bb0945bcae79123126bde7aa6169569756cabe7df84631
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-properties
    - recipient property
    - recipient-properties-opensharing
    - RP(
  citations:
    - file: manage-data-recipients-for-opensharing-databricks-on-aws.md
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: Recipient Properties
description: Custom key-value pairs (metadata) that can be attached to an OpenSharing recipient object for additional configuration or identification.
tags:
  - databricks
  - delta-sharing
  - configuration
timestamp: "2026-06-19T18:01:34.179Z"
---

```markdown
---
title: Recipient Properties
summary: Custom key-value metadata that can be attached to a recipient object during or after creation for management purposes
sources:
  - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  - manage-data-recipients-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:54:45.881Z"
updatedAt: "2026-06-18T14:54:45.881Z"
tags:
  - metadata
  - data-sharing
  - recipient-management
aliases:
  - recipient-properties
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

# Recipient Properties

**Recipient Properties** are key-value pairs attached to an [[OpenSharing]] recipient object in [[Unity Catalog]]. They allow data providers to refine data sharing access, enabling fine-grained control over what data is shared with specific recipients without creating separate shares for each one. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md, create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Predefined Properties

Recipient objects include predefined properties that start with `databricks.` and are automatically populated: ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

| Property | Description | Sharing Mode |
|----------|-------------|--------------|
| `databricks.accountId` | The Databricks account that a data recipient belongs to | Databricks-to-Databricks only |
| `databricks.metastoreId` | The Unity Catalog [[metastore|Metastore]] that a data recipient belongs to | Databricks-to-Databricks only |
| `databricks.name` | The name of the data recipient | All modes |

## Custom Properties

Providers can create custom recipient properties beyond the predefined ones. For example, you might assign a property such as `'country' = 'us'` to a recipient to enable data partitioning or row-level filtering based on geography. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Use Cases

### Partition Filtering

You can share different table partitions with different recipients by using recipient properties in partition filtering logic. For instance, if you attach a `country` property to recipients, you can partition a table by country and share only the US partition with recipients that have `country = 'us'`. This enables you to use the same shares with multiple recipients while maintaining data boundaries between them. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Dynamic Views for Row and Column Filtering

Recipient properties can be used in [[OpenSharing views|dynamic views]] within a share to limit recipient access to table data at the row or column level. For example, a dynamic view can reference `databricks.name` or custom properties to filter rows based on which recipient is querying the data. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Managing Recipient Properties

### Requirements

To manage recipient properties, you must use a SQL warehouse or compute running Databricks Runtime 12.2 or above. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Permissions

Adding or updating recipient properties requires one of the following: ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

- [[metastore|Metastore]] admin, or
- User with the `CREATE RECIPIENT` privilege for the Unity Catalog [[metastore|Metastore]]

You must also be the owner of the recipient object to update its properties. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Adding Properties

Recipient properties can be added when creating a new recipient or updated for an existing recipient using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

In Catalog Explorer, navigate to the recipient details page and click the edit icon next to **Recipient properties**. Enter a property name (key) and value, then click **Save**. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Viewing Properties

To view recipient properties, use Catalog Explorer, the Databricks CLI, or the `DESCRIBE RECIPIENT` SQL command. The output includes both predefined and custom properties. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [[OpenSharing]] — The Delta Sharing framework used by Databricks
- [[Data Recipient|Data Recipients]] — Named objects representing consumers of shared data
- Dynamic Views — Views that can use recipient properties for row and column filtering
- Partition Filtering — Using recipient properties to share different data partitions
- [[Sharing Identifier]] — The [[metastore|Metastore]] identifier used to create Databricks-to-Databricks recipients

## Sources

- manage-data-recipients-for-opensharing-databricks-on-aws.md
- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
```

# Citations

1. [manage-data-recipients-for-opensharing-databricks-on-aws.md](/references/manage-data-recipients-for-opensharing-databricks-on-aws-073afd50.md)
2. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
