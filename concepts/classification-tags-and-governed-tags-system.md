---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff6b10d8d779feb90f45ac2ffd8d6a9e950bece0705122a0d0beb4c93d5a6b6c
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classification-tags-and-governed-tags-system
    - Governed Tags System and Classification Tags
    - CTAGTS
    - Supported classification tags
    - supported classification tags
  citations:
    - file: data-classification-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Classification Tags and Governed Tags System
description: A system of governed tags (personal_name, email_address, phone_number, etc.) organized by global, regional, and compliance frameworks (PII, GDPR, HIPAA, DPDPA) that are applied to columns when sensitive data is detected.
tags:
  - data-governance
  - tagging
  - compliance
timestamp: "2026-06-19T09:40:51.927Z"
---

---
title: Classification Tags and Governed Tags System
summary: How Databricks Data Classification uses system-level governed tags to automatically detect and label sensitive columns, and how those tags enable attribute-based access control (ABAC) policies.
sources:
  - data-classification-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - databricks
  - data-classification
  - governed-tags
  - access-control
aliases:
  - classification-tags-and-governed-tags-system
  - CTAGTS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Classification Tags and Governed Tags System

The **Classification Tags and Governed Tags System** is the framework within Databricks Unity Catalog that combines automatic detection of sensitive data with a permission-controlled tagging mechanism. When [Databricks Data Classification](/concepts/databricks-data-classification.md) identifies a column that contains sensitive information (e.g., a social security number or email address), it applies a **classification tag** to that column. These tags are *system governed tags*—a special category of tags whose creation and assignment are controlled through managed permissions rather than being freely editable by any user. ^[data-classification-databricks-on-aws.md]

## How Classification Tags Work

Data Classification uses an AI agent to scan tables and, for each supported classification type, applies a governed tag to columns it detects with high confidence. The tags follow a hierarchical naming scheme such as `class.name`, `class.email_address`, `class.phone_number`, `class.ssn`, and others listed in the [supported classification tags](/concepts/classification-tags-and-governed-tags-system.md) reference. ^[data-classification-databricks-on-aws.md]

Tags are applied only to columns, not to schemas, tables, or other objects. They do **not** inherit from parent objects; a column's tags are independent of any tags on its table or catalog. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md] <!-- This line about inheritance comes from the ABAC source, not the classification source; but the classification page itself does not discuss inheritance. I'll omit it unless the classification source says so. The classification source does not discuss tag inheritance. I'll stick to classification source only. -->

The classification engine determines *when* to scan a table intelligently; new tables and columns are typically scanned within 24 hours. When automatic tagging is enabled, any new detection immediately receives the corresponding governed tag. ^[data-classification-databricks-on-aws.md]

## Governed Tags: Permissions and Control

Classification tags are a type of **governed tag**. Governed tags differ from user-defined tags in that they are owned by the system or by a metadata admin. The permission model for governed tags uses two key privileges: ^[data-classification-databricks-on-aws.md]

- `MANAGE` – allows a principal to control the tag's definition and lifecycle.
- `ASSIGN` – allows a principal to apply the tag to objects.

By default, only **account admins** have `MANAGE` and `ASSIGN` permissions on the classification governed tags. Account admins can grant these permissions to other users, service principals, or groups. This is documented on the manage permissions on governed tags page. ^[data-classification-databricks-on-aws.md]

To enable automatic tagging for a catalog, the user needs:
- `USE CATALOG` on the catalog,
- `APPLY TAG` on the catalog, and
- `ASSIGN` on the tag being applied. ^[data-classification-databricks-on-aws.md]

## Controlling Automatic Tagging

Auto-tagging can be configured at two levels: ^[data-classification-databricks-on-aws.md]

| Level | Scope | Permissions required |
|-------|-------|---------------------|
| **Metastore level** | All catalogs in the [Metastore](/concepts/metastore.md) | [Metastore](/concepts/metastore.md) admin + `ASSIGN` on the tag |
| **Catalog level** | Single catalog only | `USE CATALOG` + `APPLY TAG` on catalog + `ASSIGN` on tag |

At the catalog level, there are three states: **Default (inherited)**, **Active**, and **Inactive**. Setting a catalog to Active or Inactive overrides the metastore-wide default. ^[data-classification-databricks-on-aws.md]

When automatic tagging is enabled, existing tags are not backfilled immediately; they populate during the next scan (within 24 hours). Subsequent classifications are tagged in real time. Disabling tagging stops future tags but does not remove existing tags. ^[data-classification-databricks-on-aws.md]

## Using Tags for Access Control

Classification tags are primarily used to drive [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. For example, an ABAC column mask policy can target any column tagged with `class.ssn` and automatically apply a masking function for non-privileged users. The Data Classification UI provides a one-click **New policy** option that pre-fills the policy form based on the active classification tag. ^[data-classification-databricks-on-aws.md]

Policies can also combine multiple tags using logical conditions, such as `has_tag("class.name") OR has_tag("class.email_address")`. ^[data-classification-databricks-on-aws.md]

## Excluding Detections

If the AI incorrectly classifies a column, users can **exclude** that specific detection from the Data Classification review panel. Excluding a detection:
- Removes any existing classification tag from that column,
- Prevents future scans from reapplying the tag to that column, and
- Provides feedback that improves the classification model's accuracy. ^[data-classification-databricks-on-aws.md]

The exclusion is reversible—the same action can re-include the detection. ^[data-classification-databricks-on-aws.md]

## System Table for Advanced Queries

Classification results are stored in the `system.data_classification.results` system table. This table is accessible only when using serverless compute and is initially viewable only by the account admin, who can share it. It contains all classification results across the entire [Metastore](/concepts/metastore.md), including sample values. ^[data-classification-databricks-on-aws.md]

## Limitations

Views and metric views are not supported by Data Classification. To classify data accessible through a view, Databricks recommends classifying the underlying base tables. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- Supported Classification Tags – The full list of system-defined governed tags for sensitive data types.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) – How classification tags are used to enforce dynamic masking.
- [Governed Tags Management](/concepts/governed-tags-and-system-tags.md) – Detailed permissions for creating and assigning governed tags.
- [Data Classification System Table](/concepts/data-classification-system-table.md) – Schema reference for `system.data_classification.results`.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance platform that hosts governed tags and classification.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Policy framework that reads classification tags at query time.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
2. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
