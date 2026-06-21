---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c04061d6faa5930081a43a5e24b9674c255624cb795125ee50278d3ad88fb31
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifiers-for-databricks-data-classification
    - CCFDDC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom classifiers for Databricks Data Classification
description: User-defined classifiers that extend built-in data classification to detect organization-specific sensitive data by associating governed tags with example columns.
tags:
  - data-governance
  - unity-catalog
  - classification
timestamp: "2026-06-18T14:56:56.344Z"
---

```markdown
# Custom Classifiers for Databricks Data Classification

**Custom classifiers** extend the built-in [[Data Classification]] system in [[Unity Catalog]] so organizations can detect sensitive data that is specific to their domain — such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers. They are configured by selecting a [[Governed Tags|governed tag]] and providing example columns that contain representative values for the class. Data Classification then detects this class during its regular scans. ^[custom-classifiers-databricks-on-aws.md]

Using custom classifiers you can tag organization-specific data and later apply [[ABAC Column-Level Mask (Unity Catalog)|ABAC column-level masks]] to control access to those columns. ^[custom-classifiers-databricks-on-aws.md]

## Requirements

- Data Classification must be enabled on at least one catalog in the [[metastore|Metastore]]. ^[custom-classifiers-databricks-on-aws.md]
- The workspace must have serverless compute available (enabled by default in workspaces with Unity Catalog). ^[custom-classifiers-databricks-on-aws.md]
- To create, edit, or delete a custom classifier you must be a [[metastore|Metastore]] admin. ^[custom-classifiers-databricks-on-aws.md]
- To create or edit a custom classifier you must have `ASSIGN` privileges on the governed tag the classifier uses. ^[custom-classifiers-databricks-on-aws.md]
- To select a column for the classifier you must have `SELECT` on the table that contains it. ^[custom-classifiers-databricks-on-aws.md]

## Create a custom classifier

1. From the Data Classification results page, click **Manage custom classifiers**. ^[custom-classifiers-databricks-on-aws.md]
2. In the side panel, click **Create custom classifier**. ^[custom-classifiers-databricks-on-aws.md]
3. **Select a tag** – choose an existing governed tag or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value you want to detect. ^[custom-classifiers-databricks-on-aws.md]
4. **Select example columns** – browse the catalog tree and select columns that contain representative values for the class. Broader and more varied examples produce more accurate detection rules. You must select between 1 and 10 example columns. ^[custom-classifiers-databricks-on-aws.md]
5. Click **Create**. Detections typically appear on the results page within a few hours. ^[custom-classifiers-databricks-on-aws.md]

A custom classifier applies to **all** catalogs in the [[metastore|Metastore]] that have Data Classification enabled; per-catalog or per-schema scoping is not supported. ^[custom-classifiers-databricks-on-aws.md]

## Manage custom classifiers

The **Manage custom classifiers** side panel lists all custom classifiers configured for the [[metastore|Metastore]]. From this panel you can search by tag name, edit example columns, or delete a classifier. ^[custom-classifiers-databricks-on-aws.md]

### Edit a custom classifier

1. In the side panel, select the classifier you want to edit. ^[custom-classifiers-databricks-on-aws.md]
2. Click **Edit** next to the example columns list. ^[custom-classifiers-databricks-on-aws.md]
3. Add or remove columns (the 1–10 limit applies). ^[custom-classifiers-databricks-on-aws.md]
4. Click **Save**. Updates take effect within a few hours. Existing detections from the previous configuration remain in place. ^[custom-classifiers-databricks-on-aws.md]

The governed tag and tag value cannot be changed after creation. To use a different tag, delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Delete a custom classifier

1. In the side panel, select the classifier and click **Delete**. ^[custom-classifiers-databricks-on-aws.md]
2. Confirm the deletion. ^[custom-classifiers-databricks-on-aws.md]

When you delete a custom classifier:
- No new detections are produced.
- Existing detections are removed from the results page.
- Tags that were already auto-applied to columns are **not** removed automatically. ^[custom-classifiers-databricks-on-aws.md]

### Suspended classifiers

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended classifier produces no new detections. ^[custom-classifiers-databricks-on-aws.md]

Common causes include example columns referencing deleted/renamed tables, unrepresentative columns, or an invalid governed tag or tag value. To resolve, edit the classifier with different example columns or, if the tag is invalid, delete and recreate the classifier. ^[custom-classifiers-databricks-on-aws.md]

## View custom classifier detections

Follow the same steps as for built-in classifications (see [[Data Classification Results Page|Data Classification#view classification results]]). ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Maximum of 50 custom classifiers per [[metastore|Metastore]]. ^[custom-classifiers-databricks-on-aws.md]
- Each classifier must reference between 1 and 10 example columns. ^[custom-classifiers-databricks-on-aws.md]
- Governed tag naming is subject to Tag Policy rules. ^[custom-classifiers-databricks-on-aws.md]
- Custom classifiers apply to all Data Classification–enabled catalogs (no per-catalog/per-schema scoping). ^[custom-classifiers-databricks-on-aws.md]
- The governed tag cannot be changed after creation. ^[custom-classifiers-databricks-on-aws.md]
- New and updated classifiers apply only to **subsequent** scans; existing scan results are not automatically reclassified. ^[custom-classifiers-databricks-on-aws.md]
- All Data Classification limitations (e.g., supported table types) also apply to custom classifiers. ^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

### A custom classifier is suspended
Edit the classifier with a different set of example columns and wait for the next scan. If the suspension is caused by an invalid tag or tag value, delete and recreate the classifier. ^[custom-classifiers-databricks-on-aws.md]

### Permission denied when creating or listing custom classifiers
Must be a [[metastore|Metastore]] admin. Creating/editing additionally requires `ASSIGN` on the governed tag. ^[custom-classifiers-databricks-on-aws.md]

### Cannot select an example column
You must have `SELECT` on the table containing the column. Ask the table owner to grant it or choose a different column. ^[custom-classifiers-databricks-on-aws.md]

## Encryption

Custom classifier configuration and detection metadata that Databricks generates from example columns are encrypted at rest. You can optionally configure a customer-managed key (CMK) on the system catalog to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Related concepts

- [[Data Classification|Built-in classification tags]]
- [[Governed tags]]
- [[ABAC column mask policies]]
- [[Unity Catalog]]
- [[System Tables for Unity Catalog Audit|System catalog]]

## Sources

- custom-classifiers-databricks-on-aws.md
```

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
