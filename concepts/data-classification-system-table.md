---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f6ca1a830d3ac48548b977fc08d564ca64b04c4dff6c1803be5426884529426
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-system-table
    - DCST
    - Data Classification System Table Reference
    - System tables reference
    - data-classification-results-system-table
    - DCRST
    - systemdata_classificationresults-system-table
    - SST
    - system.data_classification.results|results system table
  citations:
    - file: data-classification-databricks-on-aws.md
title: Data Classification System Table
description: The system.data_classification.results table that stores all classification results across the metastore, including sample values, accessible only via serverless compute.
tags:
  - system-tables
  - monitoring
  - classification
timestamp: "2026-06-19T18:04:06.298Z"
---

# Data Classification System Table

The **Data Classification System Table** is a [Unity Catalog](/concepts/unity-catalog.md) system table named `system.data_classification.results` that stores the output of [Data Classification](/concepts/data-classification.md) scans across the entire [Metastore](/concepts/metastore.md). It is created automatically when data classification is enabled on any catalog. ^[data-classification-databricks-on-aws.md]

## Table Contents

The `system.data_classification.results` table contains all classification results across every catalog in the [Metastore](/concepts/metastore.md), including sample values from the classified columns of each table. This allows administrators to review detections, track tagging status, and audit user access to sensitive data at the [Metastore](/concepts/metastore.md) level. ^[data-classification-databricks-on-aws.md]

## Access Control

By default, only the account admin has access to the `system.data_classification.results` table. The account admin can share the table with other users or groups by granting `SELECT` privilege. The table is only accessible when using [serverless compute](/concepts/serverless-gpu-compute.md) — it cannot be queried from classic or pro compute clusters. ^[data-classification-databricks-on-aws.md]

### Viewing Sample Values in the UI

To see sample values associated with detections on the Data Classification results page, a user must have `SELECT` on this system table in addition to the UI-level permissions (`USE CATALOG` and either `MANAGE` or `SELECT` + `USE SCHEMA` on the catalog). Without `SELECT` on the system table, the results page will display detection counts but not sample values. ^[data-classification-databricks-on-aws.md]

## Security Considerations

The `system.data_classification.results` table contains all classification results across the entire [Metastore](/concepts/metastore.md) and includes sample values from tables in each catalog. Administrators should only share this table with users who are privileged to see metastore‑wide classification results, including sample values. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The feature that generates the classification results stored in this table.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer hosting system tables and classification.
- System Tables – The broader set of system tables in Unity Catalog, including `system.access.audit` and `system.billing.usage`.
- [Governed Tags](/concepts/governed-tags.md) – Tags applied automatically based on classification results.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Policies that can be created from classification results to mask or restrict sensitive data.
- Serverless Compute – The compute environment required to query this table.
- Data Classification Types – The supported classification tags that appear in the results.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
