---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d262ec62e4cd2bdc716a4181bfc10180bb4b9cd4ccc0cc77b36b63b3f6faeaf9
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - abac-column-level-mask-unity-catalog
    - ACM(C
    - ABAC Column-Level Masks
    - ABAC column-level masks
    - Column-Level Masking
    - Column‑Level Masking
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: ABAC Column-Level Mask (Unity Catalog)
description: Attribute-based access control policy that can be automatically applied to columns tagged by custom classifiers, enabling dynamic data masking based on user attributes.
tags:
  - security
  - access-control
  - unity-catalog
  - masking
timestamp: "2026-06-19T18:03:20.454Z"
---

Here is the wiki page for "ABAC Column-Level Mask (Unity Catalog)", based solely on the provided source material.

---

## ABAC Column-Level Mask (Unity Catalog)

**ABAC Column-Level Mask (Unity Catalog)** is a policy type within [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) that enables dynamic redaction of sensitive data at the column level based on user attributes. It is a core feature of [Unity Catalog](/concepts/unity-catalog.md)’s fine-grained access control model.

### Overview

ABAC column-level masks are applied to sensitive data detected by [Data Classification](/concepts/data-classification.md) in Unity Catalog. When a classification system—such as a built-in scanner or a [Custom Classifier](/concepts/custom-classifiers.md)—identifies a column as containing sensitive data (e.g., an employee ID, partner code, or internal account number), a governed tag is auto-applied to that column. Administrators can then use that tag to configure an ABAC mask that redacts the column’s contents for users who do not meet the required attribute criteria. ^[custom-classifiers-databricks-on-aws.md]

### Workflow

The typical workflow for applying an ABAC column-level mask is:

1. **Enable Data Classification** on at least one catalog in the [Metastore](/concepts/metastore.md).
2. **Create a Custom Classifier** (or use a built-in classifier) that detects the sensitive data pattern—for example, an internal employee ID format. The classifier selects a governed tag and provides example columns with representative values.
3. **Configure ABAC Mask** using the governed tag that the classifier auto-applies. This mask restricts access to the column based on user attributes.

### Relationship to Custom Classifiers

Custom classifiers are explicitly designed to support ABAC column-level masking. The documentation states that one of the primary benefits of custom classifiers is to “extend governance controls: Apply ABAC column-level masks to sensitive data.” This means that after a custom classifier detects a data pattern and auto-applies a governed tag, that tag can be used to create an ABAC mask that hides the data from unauthorized users. ^[custom-classifiers-databricks-on-aws.md]

### Key Concepts

- **Attribute-Based Access Control (ABAC)**: A model that grants or denies access based on attributes of the user, resource, and environment.
- **Column-Level Mask**: A dynamic redaction that applies only to a specific column; the rest of the table remains visible.
- **Governed Tag**: A tag that is used by Unity Catalog to track and control access to sensitive data. It is assigned by a classifier during data classification.
- **Data Classification**: The process of scanning tables for sensitive data patterns, which can be automated via built-in or custom classifiers.

### Requirements

To use ABAC column-level masks, the following must be in place:

- **Data Classification** must be enabled on at least one catalog in the [Metastore](/concepts/metastore.md).
- **Serverless Compute** must be available (enabled by default in workspaces with Unity Catalog).
- **Metastore admin privileges** to create, edit, or delete custom classifiers.
- **ASSIGN privileges** on the governed tag used by the classifier.
- **SELECT privileges** on the table containing the example column.

### Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md)
- [Data Classification in Unity Catalog](/concepts/data-classification-in-unity-catalog.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- Serverless Compute

### Sources

- [custom-classifiers-databricks-on-aws.md](/concepts/custom-classifier-databricks.md)

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
