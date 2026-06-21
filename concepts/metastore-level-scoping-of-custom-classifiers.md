---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae9f891d5d29aaa38f520c6662752fa12df4a98fcab0e020ad31100cb747df40
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-level-scoping-of-custom-classifiers
    - MSOCC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Metastore-Level Scoping of Custom Classifiers
description: Custom classifiers apply to all catalogs in the metastore that have Data Classification enabled; per-catalog or per-schema scoping is not supported, making this a metastore-wide governance mechanism.
tags:
  - data-governance
  - unity-catalog
  - architecture
timestamp: "2026-06-18T11:25:21.990Z"
---

# Metastore-Level Scoping of Custom Classifiers

**Metastore-Level Scoping of Custom Classifiers** refers to the fact that custom classifiers in [Unity Catalog](/concepts/unity-catalog.md) [Data Classification](/concepts/data-classification.md) apply to **all catalogs** within a [Metastore](/concepts/metastore.md) that have Data Classification enabled. There is no mechanism to restrict a custom classifier to a specific catalog or schema; its detection rules are global across the [Metastore](/concepts/metastore.md). ^[custom-classifiers-databricks-on-aws.md]

## Details

When a [Metastore](/concepts/metastore.md) admin creates a custom classifier, Data Classification scans every catalog in the [Metastore](/concepts/metastore.md) that has Data Classification turned on and applies the classifier's detection logic to all eligible tables in those catalogs. ^[custom-classifiers-databricks-on-aws.md]

This scoping is by design: custom classifiers are intended to detect organization-wide sensitive data – such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers – that should be identified consistently regardless of where it appears. ^[custom-classifiers-databricks-on-aws.md]

The governed tag chosen during classifier creation governs which tag value is auto-applied when the classifier detects matching data. Tags themselves are defined at the [Metastore](/concepts/metastore.md) level and can be used across catalogs, but the classifier's detection logic operates without per-catalog boundaries. ^[custom-classifiers-databricks-on-aws.md]

## Implications

- **No per-catalog or per-schema scoping.** If you need different detection rules for different business units (e.g., one set of employee IDs for HR and another for Finance), you cannot use separate custom classifiers scoped to different catalogs. A single classifier matching a given tag/value pattern will attempt to detect that pattern across all enabled catalogs. ^[custom-classifiers-databricks-on-aws.md]
- **All enabled catalogs are scanned.** Even if you only intend a classifier to apply to one catalog, it will run against every catalog where Data Classification is active. To avoid unwanted detections, carefully choose example columns that are representative of the data you want flagged, and consider disabling Data Classification on catalogs where the classifier should not apply. ^[custom-classifiers-databricks-on-aws.md]
- **Metastore-wide management.** Because custom classifiers are metastore-level objects, only [Metastore Admin|metastore admins](/concepts/metastore-admin-databricks.md) can create, edit, or delete them. Delegating classification to catalog-level stewards is not possible with this feature. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- Maximum of **50 custom classifiers per metastore**. ^[custom-classifiers-databricks-on-aws.md]
- Each classifier must use between **1 and 10 example columns** to provide sufficient training data for the detection engine. ^[custom-classifiers-databricks-on-aws.md]
- The governed tag and tag value **cannot be changed after creation**. To switch tags, delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]
- New and updated classifiers apply only to **subsequent scans**; existing scan results are not automatically reclassified. ^[custom-classifiers-databricks-on-aws.md]
- All Data Classification#Limitations|limitations of the built-in Data Classification system apply to custom classifiers as well, including the set of supported table types. ^[custom-classifiers-databricks-on-aws.md]

## Best Practices

- **Plan your tagging taxonomy** at the [Metastore](/concepts/metastore.md) level before creating classifiers. Use a consistent naming convention for governed tags so that the global scope does not lead to unintended tag applications. ^[custom-classifiers-databricks-on-aws.md]
- **Use narrow, representative example columns** to avoid false positives in catalogs where the data pattern is naturally different. The more varied and typical the examples, the more accurate the detection rule. ^[custom-classifiers-databricks-on-aws.md]
- **Restrict Data Classification enablement** to only those catalogs where you want custom classifiers to run. If a catalog should not be scanned, disable Data Classification on it. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that hosts metastore-level objects
- [Data Classification](/concepts/data-classification.md) — The system that scans tables and applies sensitivity tags
- [Governed Tags](/concepts/governed-tags.md) — The tag infrastructure that custom classifiers use to label detected data
- [ABAC column-level masks](/concepts/abac-column-level-mask-unity-catalog.md) — Downstream access control that can be driven by tags applied by classifiers
- [Metastore Admin](/concepts/metastore-admin-role.md) — The role required to manage custom classifiers
- Data Classification Tags — Reference for supported built-in tags

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
