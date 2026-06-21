---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74c4a0efe02365594d302ae3a42b550a98306d322a964f61a19c0e95401d1b20
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - intelligent-incremental-scanning
    - IIS
  citations:
    - file: data-classification-databricks-on-aws.md
title: Intelligent Incremental Scanning
description: The classification engine uses an agentic AI system with the Data Intelligence Engine to incrementally scan only new or changed data, optimizing cost and avoiding manual configuration.
tags:
  - scanning
  - optimization
  - data-governance
timestamp: "2026-06-18T14:58:25.635Z"
---

```markdown
---
title: Intelligent Incremental Scanning
summary: An optimized scanning strategy where the classification engine determines when to scan tables, using incremental scans that avoid re-scanning unchanged data and typically complete within 24 hours of new table creation.
sources:
  - data-classification-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:27:06.999Z"
updatedAt: "2026-06-18T11:27:06.999Z"
tags:
  - scanning
  - optimization
  - data-classification
aliases:
  - intelligent-incremental-scanning
  - IIS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Intelligent Incremental Scanning

**Intelligent Incremental Scanning** is a feature of [[Databricks Data Classification]] in [[Unity Catalog]] that determines when to scan tables for sensitive data. It leverages [[Unity Catalog]] metadata and the Data Intelligence Engine to decide whether a table requires reclassification, so that only new or changed data is scanned — without manual configuration. ^[data-classification-databricks-on-aws.md]

## Overview

Data catalogs can contain vast amounts of data, often including known and unknown sensitive information. Intelligent Incremental Scanning addresses the problem of scale by ensuring that the classification engine only scans tables when there is reason to believe new data has appeared. ^[data-classification-databricks-on-aws.md]

The system uses an AI agent to automatically classify and tag tables. When a user enables data classification on a catalog or schema, the engine runs a background job that incrementally scans all tables in scope. New tables and columns that are added to a catalog are typically scanned within **24 hours** of being created. ^[data-classification-databricks-on-aws.md]

## How It Works

Intelligent Incremental Scanning uses two inputs to decide when a table should be re-scanned: ^[data-classification-databricks-on-aws.md]

- [[Unity Catalog]] — The system's metadata layer, which tracks all objects in the [[metastore|Metastore]].
- The Data Intelligence Engine — Databricks' compute and optimization layer.

By combining these, the system can determine which tables and columns are new or have changed without requiring the user to configure a scan schedule or specify which objects to examine. ^[data-classification-databricks-on-aws.md]

## Benefit: Cost Optimization

Because scanning is incremental, subsequent scans on the same catalog are typically **lower cost** than the initial scan. The initial scan generally incurs higher cost because it must classify all existing objects; after that, only deltas are processed. ^[data-classification-databricks-on-aws.md]

You can view Data Classification expenses via the `system.billing.usage` system table or the usage dashboard. The `billing_origin_product` for Data Classification is `'DATA_CLASSIFICATION'`. ^[data-classification-databricks-on-aws.md]

```sql
SELECT
  usage_date,
  identity_metadata.created_by,
  usage_metadata.catalog_id,
  SUM(usage_quantity) AS dbus
FROM system.billing.usage
WHERE
  usage_date >= DATE_SUB(CURRENT_DATE(), 30)
  AND billing_origin_product = 'DATA_CLASSIFICATION'
GROUP BY
  usage_date, created_by, catalog_id
ORDER BY
  usage_date DESC, created_by;
```

## Configuration

### Enable Multiple Catalogs

1. On the Data Classification results page, click **Configure**.
2. Select the catalogs you want to enable.
3. Click **Enable**.

Enabling all available catalogs does not automatically enable future catalogs. To classify a new catalog, return to the **Configure** dialog and enable it. ^[data-classification-databricks-on-aws.md]

### Enable a Single Catalog with Schema Selection

1. Navigate to the catalog and click the **Details** tab.
2. Next to **Data Classification**, click **Enable**.
3. Select schemas to include in the **Schemas to include** dropdown.
4. Optionally select a **Usage policy**.
5. Click **Save**.

This creates a background job that incrementally scans all tables in the selected schemas. ^[data-classification-databricks-on-aws.md]

## Requirements

- The workspace must have [[Serverless GPU Compute|serverless compute]] available (enabled by default in workspaces with Unity Catalog). ^[data-classification-databricks-on-aws.md]
- To enable data classification, you must **own** the catalog or have `USE CATALOG` and `MANAGE` privileges on it. ^[data-classification-databricks-on-aws.md]
- To enable automatic tagging for a catalog, you need `USE CATALOG`, `APPLY TAG`, and `ASSIGN` on the tag being applied. ^[data-classification-databricks-on-aws.md]

## Limitations

- Views and metric views are not supported for data classification. If a view is based on existing tables, Databricks recommends classifying the underlying tables instead. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [[Databricks Data Classification]] — The overall feature for automatic classification and tagging.
- [[Unity Catalog]] — The metadata layer that enables intelligent scanning.
- Data Intelligence Engine — The optimization layer used to decide when to scan.
- Serverless Compute — Required compute for data classification.
- Incremental Scanning — The general pattern of scanning only deltas.
- System Tables — Where billing and classification results are stored.

## Sources

- data-classification-databricks-on-aws.md
```

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
