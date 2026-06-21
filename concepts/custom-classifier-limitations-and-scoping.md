---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff8424262a238879d73574d1a5774cf0074de56d26303b4df2b537b6701b8bbe
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-limitations-and-scoping
    - scoping and Custom classifier limitations
    - CCLAS
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom classifier limitations and scoping
description: Operational constraints including 50-classifier metastore limit, 1-10 example column requirement, global metastore-wide application, and tag immutability after creation.
tags:
  - data-governance
  - limitations
  - unity-catalog
timestamp: "2026-06-18T14:56:25.582Z"
---

# Custom classifier limitations and scoping

**Custom classifiers** extend Databricks' built-in [Data Classification](/concepts/data-classification.md) system, enabling organizations to detect sensitive data types unique to their domain, such as internal employee IDs or proprietary product codes. The configuration and behavior of these classifiers are subject to a set of scoping rules and operational limitations, detailed below.

## Scoping

Custom classifiers apply to **all catalogs in the metastore** that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. This means a classifier defined for one set of example columns runs against every eligible catalog in the [Metastore](/concepts/metastore.md), regardless of which catalog the examples were drawn from. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

### Quantity limits

- **Maximum 50 custom classifiers per metastore** – Once this limit is reached, no additional classifiers can be created. ^[custom-classifiers-databricks-on-aws.md]
- **Each classifier must use between 1 and 10 example columns** – Fewer than one or more than ten columns prevents creation of the classifier. ^[custom-classifiers-databricks-on-aws.md]

### Tag constraints

- **Governed tag naming is subject to Tag Policy rules** – See the governed tags documentation for naming and value restrictions. ^[custom-classifiers-databricks-on-aws.md]
- **The governed tag and tag value cannot be changed after creation** – To switch to a different tag, you must delete the custom classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]

### Scan behavior

- **New and updated classifiers apply only to subsequent Data Classification scans** – Existing scan results are not automatically reclassified; detections for previously scanned data appear only after the next scan completes. ^[custom-classifiers-databricks-on-aws.md]

### Inherited Data Classification limitations

All general [Data Classification](/concepts/data-classification.md) limitations apply to custom classifiers as well. These include restrictions on supported table types and other platform-level constraints. ^[custom-classifiers-databricks-on-aws.md]

### Suspended classifiers

If rule generation or validation fails (for example, because example columns reference deleted tables, are not representative enough, or the governed tag becomes invalid), Databricks suspends the custom classifier. A suspended classifier produces **no new detections** and shows a warning on the Data Classification results page. To resolve a suspension, edit the classifier with different example columns or, if the tag is invalid, delete and recreate it. ^[custom-classifiers-databricks-on-aws.md]

### Permission requirements (operational constraints)

Creating, editing, or deleting a custom classifier requires the user to be a **metastore admin**. Additionally:

- `ASSIGN` privilege on the governed tag is required for create and edit operations.
- `SELECT` permission on the table containing the example column is required to select that column.

Lack of any of these permissions results in a "permission denied" error. ^[custom-classifiers-databricks-on-aws.md]

### Encryption note

Custom classifier configuration and detection metadata are encrypted at rest. A customer-managed key (CMK) can be configured on the system catalog to manage the encryption key; this encrypts all data in the system catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

## Related concepts

- [Data Classification](/concepts/data-classification.md) – The built-in system that custom classifiers extend.
- [Governed Tags](/concepts/governed-tags.md) – The tag infrastructure used by custom classifiers.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – A downstream governance control enabled by custom classifier detections.
- Tag Policy – Rules governing tag naming and structure.
- [Metastore Admin](/concepts/metastore-admin-role.md) – Role required to manage custom classifiers.
- [Customer-managed key (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md) – Encryption option for system catalog data.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
