---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1344ee65a9b417ddd6300d6d41d962cc3a1a1cbec131223a0c888ad8b30faf85
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-databricks
    - GT(
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Governed Tags (Databricks)
description: Tags managed under a governance policy that can be assigned to data assets; custom classifiers use governed tags to label detected sensitive data columns in Unity Catalog.
tags:
  - data-governance
  - unity-catalog
  - tagging
timestamp: "2026-06-19T14:39:19.527Z"
---

---

Created: 2026-06-18T12:26:53.977Z
Updated: 2026-06-18T12:26:53.977Z

---

# Governed Tags (Databricks)

**Governed tags** are a Databricks metadata and governance construct used to organize, classify, and apply access control policies to data assets. Governed tags are the foundational mechanism by which [Custom Classifiers](/concepts/custom-classifiers.md) for [Data Classification](/concepts/data-classification.md) and [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies are defined.

In the context of Data Classification, a custom classifier selects a governed tag and a tag value. The governed tag defines the *type* of sensitive data to detect (for example, "Employee ID"), and the system applies that tag to columns whose data matches the classifier's rules. ^[custom-classifiers-databricks-on-aws.md]

## Purpose

Governed tags serve as the bridge between data classification and access control:

- **Data Classification:** Governed tags are the target of custom classifiers. When a classifier detects data matching a pattern, it auto-tags the column with the specified governed tag. ^[custom-classifiers-databricks-on-aws.md]
- **Access Control:** Tags can be used to define ABAC policies. For instance, a policy can deny access to columns tagged with "Employee ID" unless a user has a specific role or clearance. ^[custom-classifiers-databricks-on-aws.md]

## Managing Governed Tags

### Creating a Governed Tag in a Custom Classifier

When creating a custom classifier, you can either select an existing governed tag or click **Create new tag** to define one inline. If the tag has allowed values, you must choose the specific value you want to detect. ^[custom-classifiers-databricks-on-aws.md]

### Permissions

To create or edit a custom classifier that uses a governed tag, you must have `ASSIGN` privileges on that tag. Without these privileges, you cannot create or modify the classifier. ^[custom-classifiers-databricks-on-aws.md]

## Behavior

- **Auto-tagging:** When a custom classifier detects data matching its criteria, it automatically applies the governed tag to the affected column. ^[custom-classifiers-databricks-on-aws.md]
- **Immutability:** The governed tag used by a custom classifier *cannot be changed* after creation. To use a different tag, you must delete the custom classifier and create a new one with a different tag. ^[custom-classifiers-databricks-on-aws.md]
- **Naming Rules:** Governed tag naming is subject to Tag Policy rules. ^[custom-classifiers-databricks-on-aws.md]

## Relationship with ABAC

Governed tags are a key component of [ABAC](/concepts/abac-attribute-based-access-control.md) in Unity Catalog. ABAC policies can reference governed tags to control access at the column level, enabling fine-grained governance that respects the data's classification. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md) — Detect organization-specific data types using governed tags.
- [Data Classification](/concepts/data-classification.md) — The system that scans data and auto-applies tags.
- Tag Policy rules — Constraints on governed tag naming.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Access control policies that can reference governed tags.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) where governed tags reside.
- [Data Classification System Table](/concepts/data-classification-system-table.md) — A system table that logs classification activity.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
