---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24f3f49535bd477e34c6bad523869ba9b791d05b86f8a1687bc794286b90fba3
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-lifecycle-and-limits
    - Limits and Custom Classifier Lifecycle
    - CCLAL
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Lifecycle and Limits
description: Rules governing custom classifier creation, editing, deletion, and enforcement — including the 50-classifier metastore limit, 1-10 example column requirement, immutability of governed tag after creation, and metastore-wide scope.
tags:
  - data-governance
  - unity-catalog
  - limits
timestamp: "2026-06-19T14:39:19.755Z"
---

# Custom Classifier Lifecycle and Limits

**Custom classifiers** extend Databricks Data Classification so you can detect sensitive data that is specific to your organization, such as internal employee IDs, proprietary product codes, or partner account numbers. They are defined by selecting a [governed tag](/concepts/governed-tags.md) and providing example columns that contain representative values for the class.^[custom-classifiers-databricks-on-aws.md]

## Lifecycle

### Prerequisites

To work with custom classifiers you must meet these requirements:
- Data Classification must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- Serverless compute must be available in the workspace (enabled by default in workspaces with Unity Catalog).
- To create, edit, or delete a custom classifier, you must be a [Metastore](/concepts/metastore.md) admin.
- To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag it uses.
- To select a column for the classifier, you must have `SELECT` on the table that contains it.
^[custom-classifiers-databricks-on-aws.md]

### Creating a Custom Classifier

1. Navigate to the Data Classification results page and click **Manage custom classifiers**.
2. In the side panel, click **Create custom classifier**.
3. Select a governed tag (existing or create new inline) and, if the tag has allowed values, choose the specific value to detect.
4. Select 1–10 example columns that contain representative values for the class. Broader and more varied examples produce more accurate detection rules.
5. Click **Create**.

Detections typically appear on the results page within a few hours after the next Data Classification scan. A custom classifier applies to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled; per-catalog or per-schema scoping is not supported.^[custom-classifiers-databricks-on-aws.md]

### Editing a Custom Classifier

You can update the example columns of an existing classifier, but you **cannot change** the governed tag or tag value after creation. To switch to a different tag, delete the custom classifier and create a new one. Editing steps:
1. Open the **Manage custom classifiers** side panel and select the classifier.
2. Click **Edit** next to the example columns list.
3. Add or remove columns, staying within the 1–10 column limit.
4. Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place.^[custom-classifiers-databricks-on-aws.md]

### Deleting a Custom Classifier

1. In the **Manage custom classifiers** side panel, select the classifier.
2. Click **Delete** and confirm.

When deleted:
- No new detections are produced.
- Existing detections are removed from the Data Classification results page.
- Tags that were already auto-applied to columns are **not** removed automatically.
^[custom-classifiers-databricks-on-aws.md]

### Suspension

If rule generation or validation fails, Databricks suspends the custom classifier. A warning appears on the Data Classification results page and the suspended classifier produces no new detections.^[custom-classifiers-databricks-on-aws.md]

Common causes of suspension:
- Example column tables have been deleted or renamed.
- Example columns are not representative enough.
- The governed tag or tag value is no longer valid.

To resolve:
- If due to inaccessible or unrepresentative columns: edit the classifier with a different set of example columns.
- If due to an invalid tag: delete the classifier and create a new one with a valid tag.
^[custom-classifiers-databricks-on-aws.md]

## Limits

| Limit | Value |
|-------|-------|
| Maximum custom classifiers per [Metastore](/concepts/metastore.md) | 50 |
| Example columns per custom classifier | 1–10 |
| Scoping support | All catalogs only (no per-catalog or per-schema) |
| Governed tag modification after creation | Not allowed |
| Encryption at rest | Custom classifier configuration and detection metadata are encrypted; can be managed with a customer-managed key (CMK) on the system catalog |

All limitations that apply to built-in Data Classification also apply to custom classifiers (e.g., supported table types).^[custom-classifiers-databricks-on-aws.md]

## Troubleshooting

### Permission denied when creating or listing custom classifiers

You must be a [Metastore](/concepts/metastore.md) admin. Creating or editing additionally requires `ASSIGN` on the governed tag. See the prerequisites above.^[custom-classifiers-databricks-on-aws.md]

### Cannot select an example column

You must have `SELECT` on the table. Ask the table owner to grant it, or choose a different example column.^[custom-classifiers-databricks-on-aws.md]

### Custom classifier is suspended

See the suspension section above; resolve by editing or recreating the classifier.^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- Customer-managed key (CMK) for Unity Catalog
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
