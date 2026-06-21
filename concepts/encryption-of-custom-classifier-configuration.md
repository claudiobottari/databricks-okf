---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41484dd5732068af595e22395b35f3fa7fe3dde5c971e5fd9c18db771157df10
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - encryption-of-custom-classifier-configuration
    - EOCCC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Encryption of custom classifier configuration
description: Custom classifier metadata and detection patterns are encrypted at rest, with optional customer-managed key (CMK) support via the system catalog.
tags:
  - security
  - encryption
  - unity-catalog
timestamp: "2026-06-18T14:56:34.798Z"
---

# Encryption of custom classifier configuration

**Encryption of custom classifier configuration** refers to how Databricks protects at rest the metadata and configuration data that is generated when a user creates a custom classifier in Unity Catalog. This includes the classifier’s example columns and any detection metadata that Databricks derives from those examples. ^[custom-classifiers-databricks-on-aws.md]

## At‑rest encryption

Custom classifier configuration and the detection metadata produced from the example columns are encrypted at rest. By default, Databricks manages the encryption key. ^[custom-classifiers-databricks-on-aws.md]

### Customer‑managed keys (CMK)

You can optionally use a customer‑managed key (CMK) on your system catalog to control the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog — not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

The following screenshot shows where to configure a CMK on the system catalog in Catalog Explorer.

![Configure a customer-managed key on the system catalog in Catalog Explorer.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-system-catalog-cmk-3b363fbf9188461e0bc8bf3f9e93f2ce.png) ^[custom-classifiers-databricks-on-aws.md]

## Scope of encryption

- The encryption covers the configuration data (tag selection, example column references) and the detection rules that Databricks generates.
- If a CMK is enabled on the system catalog, it encrypts **all** data in the system catalog, including custom classifier metadata. ^[custom-classifiers-databricks-on-aws.md]

## Related concepts

- Customer-managed key in Unity Catalog – Managing encryption keys for system catalog data.
- [Data Classification](/concepts/data-classification.md) – The parent feature that custom classifiers extend.
- [System catalog](/concepts/system-tables-for-unity-catalog-audit.md) – The storage location for classification metadata.
- [Governed Tags](/concepts/governed-tags.md) – The tags that custom classifiers use to tag detected data.
- Data at rest encryption in Databricks – Broader encryption policies.

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
