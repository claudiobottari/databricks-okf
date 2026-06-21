---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c714629ad3c18ad50871ed972340f55d0e52376d9631c70153eec6934b10efe
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-limitations
    - CCL
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Limitations
description: Technical constraints include a maximum of 50 classifiers per metastore, 1-10 example columns each, no per-catalog scoping, immutable tag association after creation, and application only to subsequent scans.
tags:
  - limitations
  - constraints
  - boundaries
timestamp: "2026-06-19T09:39:43.988Z"
---

# Custom Classifier Limitations

**Custom Classifier Limitations** are the constraints and restrictions that apply when creating and using custom classifiers for Databricks Data Classification in Unity Catalog. Custom classifiers extend the built-in classification system to detect organization-specific sensitive data, but they are subject to several important limitations.

## [Metastore](/concepts/metastore.md) and Catalog Scope

Custom classifiers apply to **all** catalogs in the [Metastore](/concepts/metastore.md) that have Data Classification enabled. Per-catalog or per-schema scoping is not supported. This means a custom classifier cannot be restricted to a specific catalog or schema — it will scan across the entire [Metastore](/concepts/metastore.md).^[custom-classifiers-databricks-on-aws.md]

## Creation Limits

- **Maximum of 50 custom classifiers per [Metastore](/concepts/metastore.md).** This limit applies across all catalogs and schemas within a single [Metastore](/concepts/metastore.md).^[custom-classifiers-databricks-on-aws.md]
- **Each custom classifier must reference between 1 and 10 example columns.** Providing at least one example column is required, and the maximum of 10 columns ensures sufficient data for classification while preventing excessive resource usage.^[custom-classifiers-databricks-on-aws.md]

## Tag Immutability

The governed tag and tag value used by a custom classifier **cannot be changed after creation**. To switch to a different tag, you must delete the custom classifier and create a new one with the desired tag. This limitation ensures consistency in detection rules across scans.^[custom-classifiers-databricks-on-aws.md]

## Scan Behavior

New and updated custom classifiers apply only to subsequent Data Classification scans. Existing scan results are not automatically reclassified — detections for previously scanned data appear after the next scan completes. Updates to example columns take effect within a few hours, but existing detections from the previous configuration remain in place.^[custom-classifiers-databricks-on-aws.md]

## Permissions Requirements

To create or edit a custom classifier, you must be a [Metastore](/concepts/metastore.md) admin and have `ASSIGN` privileges on the governed tag the classifier uses. To select a column for the classifier, you must have `SELECT` on the table that contains it. Without these permissions, you cannot create, edit, or view custom classifiers.^[custom-classifiers-databricks-on-aws.md]

## Suspension Handling

If rule generation or validation fails, Databricks suspends the custom classifier. A suspended custom classifier produces no new detections. Common causes for suspension include:

- One or more example columns reference tables that have been deleted or renamed since the classifier was created.
- The example columns are not representative enough for the system to learn a stable detection.
- The governed tag is no longer a governed tag, or the tag value is no longer valid.

To resolve a suspension, edit the custom classifier with a different set of example columns. If the suspension is caused by an invalid governed tag or tag value, delete the custom classifier and create a new one.^[custom-classifiers-databricks-on-aws.md]

## Inherited Limitations

All Data Classification limitations apply to custom classifiers as well, including supported table types. Custom classifiers do not introduce broader scanning capabilities beyond what Data Classification already supports.^[custom-classifiers-databricks-on-aws.md]

## Encryption Considerations

Custom classifier configuration and the detection metadata generated from example columns are encrypted at rest. You can use a customer-managed key (CMK) on your system catalog to manage the encryption key, but configuring a CMK on the system catalog encrypts all data in the system catalog — not just custom classifier data.^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The underlying system that custom classifiers extend
- [Governed Tags](/concepts/governed-tags.md) – The tag system used by custom classifiers
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Governance controls that can be applied to classified data
- Data Classification Tags – Supported classification tags for built-in detection
- Policy Evaluation Order – How multiple ABAC policies interact with classified data

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
