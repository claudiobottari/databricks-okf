---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 87f78b379fb78e81d5f19121a5573d57b73eb46875ae33e8ff24c3c089255e6f
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admin-databricks
    - MA(
    - Metastore Admin|metastore admins
  citations:
    - file: custom-classifiers-databricks-on-aws.md
      start: 20
      end: 21
    - file: custom-classifiers-databricks-on-aws.md
      start: 22
      end: 23
    - file: custom-classifiers-databricks-on-aws.md#Troubleshooting
title: Metastore Admin (Databricks)
description: Privileged role required to create, edit, or delete custom classifiers in Databricks Unity Catalog data classification.
tags:
  - roles
  - permissions
  - unity-catalog
timestamp: "2026-06-19T18:02:58.481Z"
---

# [Metastore](/concepts/metastore.md) Admin (Databricks)

**Metastore Admin** refers to a Unity Catalog role that grants the highest level of administrative permissions over a [Metastore](/concepts/metastore.md). A [Metastore](/concepts/metastore.md) admin can manage metastore-level configurations, including data classification, governed tags, and custom classifiers.

## Role in Custom Classifiers

Creating, editing, or deleting a [custom classifier](/concepts/custom-classifiers.md) for [Data Classification](/concepts/data-classification.md) in Unity Catalog requires the user to be a [Metastore](/concepts/metastore.md) admin. This requirement is enforced for all write‑level operations on custom classifiers. ^[custom-classifiers-databricks-on-aws.md#L20-L21]

In addition to the [Metastore](/concepts/metastore.md) admin role, creating or editing a custom classifier also requires `ASSIGN` privileges on the [Governed Tag](/concepts/governed-tags.md) used by the classifier. ^[custom-classifiers-databricks-on-aws.md#L22-L23]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) is the top‑level container in Unity Catalog.
- [Data Classification](/concepts/data-classification.md) — The feature that scans tables for sensitive data.
- [Custom Classifiers](/concepts/custom-classifiers.md) — User‑defined detection rules that require [Metastore](/concepts/metastore.md) admin privileges.
- [Governed Tags](/concepts/governed-tags.md) — The tag system used by custom classifiers.

## Troubleshooting

If a user receives a permission denied error when creating or listing custom classifiers, the most common cause is that the user is not a [Metastore](/concepts/metastore.md) admin. ^[custom-classifiers-databricks-on-aws.md#Troubleshooting]

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md:20-21](/references/custom-classifiers-databricks-on-aws-61f050db.md)
2. [custom-classifiers-databricks-on-aws.md:22-23](/references/custom-classifiers-databricks-on-aws-61f050db.md)
3. custom-classifiers-databricks-on-aws.md#Troubleshooting
