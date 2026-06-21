---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4eacfd034a061eb1e5820d86766b1bbc64a18e14d5e7b6aa29d73dad36876640
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-intelligent-scanning
    - IIS
  citations:
    - file: data-classification-databricks-on-aws.md
title: Incremental Intelligent Scanning
description: The classification engine intelligently determines when to scan data by leveraging Unity Catalog metadata, performing incremental scans to classify new data without manual configuration, typically scanning new tables and columns within 24 hours.
tags:
  - data-governance
  - optimization
  - unity-catalog
timestamp: "2026-06-19T09:40:44.077Z"
---

# Incremental Intelligent Scanning

**Incremental Intelligent Scanning** is a feature of [Data Classification](/concepts/data-classification.md) in Unity Catalog that automatically and efficiently scans tables to detect and tag sensitive data. Instead of re‑scanning the entire catalog on each cycle, the system uses intelligence from Unity Catalog and the Data Intelligence Engine to scan only new or changed data, minimizing cost and manual overhead. ^[data-classification-databricks-on-aws.md]

## Overview

When you enable Data Classification for a catalog or schema, a background job is created that incrementally scans all tables. The scanning engine determines *when* to scan each table by leveraging metadata in [Unity Catalog](/concepts/unity-catalog.md) and the Data Intelligence Engine. This ensures that all new data is classified without requiring manual configuration. ^[data-classification-databricks-on-aws.md]

New tables and columns in a catalog are typically scanned within 24 hours of being created. If any individual table scan fails, that failure is skipped and automatically retried the following day. ^[data-classification-databricks-on-aws.md]

## Benefits

- **Cost efficiency**: The initial full scan is more costly, but subsequent scans are incremental and typically incur significantly lower costs. This allows organizations to continuously monitor for sensitive data without running full re‑scans. ^[data-classification-databricks-on-aws.md]
- **Automated coverage**: As new tables or columns are added, they are detected and scanned automatically without manual intervention. ^[data-classification-databricks-on-aws.md]
- **Resilience**: Failed scans are retried automatically, ensuring that transient errors do not permanently block classification. ^[data-classification-databricks-on-aws.md]

## How It Works

Incremental Intelligent Scanning uses:

- **Unity Catalog metadata** to identify which tables and columns have changed since the last scan.
- **The Data Intelligence Engine** to decide the optimal time and scope for each scan.
- **Serverless Compute** to execute the classification jobs.

The results of the scan are stored in a system table (`system.data_classification.results`) that is accessible only to account admins by default. ^[data-classification-databricks-on-aws.md]

## Cost Implications

Because scans are incremental, the per‑scan cost drops after the initial full scan. You can view Data Classification expenses by querying the `system.billing.usage` system table, filtering on `billing_origin_product = 'DATA_CLASSIFICATION'`, or by using a usage dashboard. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The overall feature that uses Incremental Intelligent Scanning.
- [Unity Catalog](/concepts/unity-catalog.md) — The metadata layer that enables intelligent scan decisions.
- Data Intelligence Engine — The engine that determines when and what to scan.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Governance controls that can be applied to classification results.
- Serverless Compute — Required for scanning and viewing results.
- System Tables — Includes `system.data_classification.results` and `system.billing.usage`.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
