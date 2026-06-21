---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e5d26fa0257d93f87b930d0a1e36e486a0c51810f0ed3c6a57bf97f7bb672fd
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automated-data-classification-with-ai
    - ADCWA
    - Automatic Data Classification
  citations:
    - file: data-classification-databricks-on-aws.md
title: Automated Data Classification with AI
description: Databricks Data Classification uses a large language model (LLM) agent to automatically classify and tag tables in Unity Catalog, identifying sensitive data such as PII, GDPR, HIPAA, and DPDPA-related content.
tags:
  - data-governance
  - AI
  - unity-catalog
timestamp: "2026-06-19T09:40:45.993Z"
---

# Automated Data Classification with AI

**Automated Data Classification with AI** is a Databricks feature that uses an agentic AI system to automatically discover, classify, and tag sensitive data in [Unity Catalog](/concepts/unity-catalog.md) tables. It helps data teams understand what kind of sensitive data exists in each table so they can apply appropriate governance controls and democratize access safely. ^[data-classification-databricks-on-aws.md]

## Overview

Data catalogs can contain vast amounts of data with both known and unknown sensitive content. Databricks Data Classification addresses this by automatically scanning tables, classifying them against a set of supported tags, and optionally applying tags that can be used with [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md). The system leverages a large language model (LLM) to assist with classification. ^[data-classification-databricks-on-aws.md]

Key capabilities include:

- **Classify data**: The engine automatically classifies and tags any tables in Unity Catalog using an agentic AI system. ^[data-classification-databricks-on-aws.md]
- **Optimize cost through intelligent scanning**: Scanning is incremental and optimized; new data is classified without manual configuration by leveraging Unity Catalog and the Data Intelligence Engine. ^[data-classification-databricks-on-aws.md]
- **Review and protect sensitive data**: The results display helps view classification results and protect sensitive data by tagging and creating access control policies for each class. ^[data-classification-databricks-on-aws.md]

Classification results are stored in [default storage](/concepts/workspace-default-storage-path.md) and users are not billed for this storage. ^[data-classification-databricks-on-aws.md]

## Requirements

- The workspace must have [serverless compute](/concepts/serverless-gpu-compute.md) available (enabled by default in workspaces with Unity Catalog). ^[data-classification-databricks-on-aws.md]
- To enable data classification for a catalog, the user must own the catalog or have `USE CATALOG` and `MANAGE` privileges on it. ^[data-classification-databricks-on-aws.md]
- To enable automatic tagging for a catalog, the user must have `USE CATALOG` on the catalog, `APPLY TAG` on the catalog, and `ASSIGN` on the tag being applied. ^[data-classification-databricks-on-aws.md]
- To view classification results in the UI, the user must have `USE CATALOG` and either `MANAGE` or (`SELECT` + `USE SCHEMA`) on the catalog. To see sample values associated with detections, the user must have `SELECT` on the [Data Classification System Table](/concepts/data-classification-system-table.md). ^[data-classification-databricks-on-aws.md]

By default, only account admins have `MANAGE` and `ASSIGN` permissions on data classification system governed tags. Account admins can grant these permissions for individual governed tags to other users, service principals, or groups. ^[data-classification-databricks-on-aws.md]

## Enabling Data Classification

Data classification can be enabled for multiple catalogs at once from the results page, or configured for individual catalogs with schema-level control.

### Enable Multiple Catalogs

1. On the Data Classification results page, click **Configure**.
2. Select the catalogs (or all available catalogs in the workspace).
3. Click **Enable**. Enabling all available catalogs does not automatically enable future catalogs — new catalogs must be added manually. ^[data-classification-databricks-on-aws.md]

### Enable a Single Catalog with Schema Selection

1. Navigate to the catalog and click the **Details** tab.
2. Next to **Data Classification**, click the **Enable** button.
3. In the dialog, optionally select specific schemas to include in the **Schemas to include** dropdown. You can also select a **Usage policy**.
4. Click **Save**.

This creates a background job that incrementally scans all tables in the catalog or selected schemas. New tables and columns are typically scanned within 24 hours of being created. ^[data-classification-databricks-on-aws.md]

## Viewing Classification Results

To view results, click **View results** next to the **Data Classification** setting on the catalog’s details page. This opens the Data Classification UI, which requires a serverless SQL warehouse.

Results can be aggregated across all classified catalogs in the [Metastore](/concepts/metastore.md) by selecting **All catalogs** from the catalog selector at the upper left. ^[data-classification-databricks-on-aws.md]

For each classification type, the table shows:

- **Detected columns**: Number of columns where the classification was detected.
- **Auto-tagging**: Tagging status — **Active**, **Inactive**, or **Partially Active** (at [Metastore](/concepts/metastore.md) view when enabled in some but not all catalogs).
- **User Access (last 7d)**: Number of distinct users who accessed unmasked vs. masked data of that classification over the last 7 days. ^[data-classification-databricks-on-aws.md]

### Review Detections

Click **Review** for a classification type to open a panel with two tabs:

- **Detected Columns**: Lists columns where the classification tag was detected with high confidence, ordered by most recent detection. Includes a **Detections over time** chart and a list of detected columns with sample values (if permissions allow). Click any bar in the chart to see detections for that date.
- **User Access**: Lists all users who accessed columns with this classification tag, showing email, username, and whether they have masked or unmasked access. Also shows any ABAC policies assigned to this classification tag. When viewing results for a single catalog, a **New policy** button is available. ^[data-classification-databricks-on-aws.md]

## Automatic Tagging

When automatic tagging is enabled, all existing and future detections of a classification are tagged. Automatic tagging can be configured at two levels:

- **Metastore level**: Enable or disable across all catalogs. Requires [Metastore](/concepts/metastore.md) admin and `ASSIGN` on the tag.
- **Catalog level**: Enable or disable for the current catalog only. Catalog-level settings take precedence over metastore-level. Requires `USE CATALOG`, `APPLY TAG` on the catalog, and `ASSIGN` on the tag. ^[data-classification-databricks-on-aws.md]

At the catalog level, automatic tagging has three states:

- **Default (inherited)**: Inherits the metastore-level setting.
- **Active**: Explicitly enabled for this catalog.
- **Inactive**: Explicitly disabled for this catalog.

When tagging is disabled, no future tags are applied, but existing tags are not removed. When enabled, tags are not backfilled immediately — they will be populated in the next scan (within 24 hours). Subsequent classifications are tagged immediately. ^[data-classification-databricks-on-aws.md]

## Excluding Detections

In the review panel (Beta feature), individual column detections can be excluded. Excluding a detection:

- Removes any existing classification tag from that column.
- Prevents future scans from reapplying the tag.
- Provides feedback that improves the accuracy of future classification results. ^[data-classification-databricks-on-aws.md]

To exclude, click the **Exclude** icon for the corresponding column. To re-include, click the icon again.

## Governance Controls Based on Results

Databricks recommends using [ABAC in Unity Catalog](/concepts/abac-policies-in-unity-catalog.md) to create governance controls based on data classification results. From the Data Classification results page, click **Review** for a classification tag, open the **User Access** tab, and click **New policy**. The policy form is pre-filled to mask columns with that classification tag. To mask data, specify a masking function registered in Unity Catalog and click **Save**. A policy can cover multiple classification tags by changing **When column** to **meets condition** and providing multiple tags (e.g., `has_tag("class.name") OR has_tag("class.email_address")`). ^[data-classification-databricks-on-aws.md]

The source also provides a notebook example for GDPR discovery and deletion using data classification.

## Scan Errors

If errors occur during a scan, an **Errors** button appears at the upper right of the results table. Clicking it displays the tables that failed and associated error messages. By default, failures for individual tables are skipped and retried the following day. ^[data-classification-databricks-on-aws.md]

## Expenses

Data Classification billing is detailed on the [Databricks pricing page](https://www.databricks.com/product/pricing). The initial scan is more costly than subsequent incremental scans. Expenses can be queried from the `system.billing.usage` table using `billing_origin_product = 'DATA_CLASSIFICATION'`. The `created_by` and `catalog_id` fields can break down costs. To calculate dollar cost, join with `system.billing.list_prices`. Alternatively, a usage dashboard can be configured and filtered by billing origin product **Data Classification**. ^[data-classification-databricks-on-aws.md]

## Limitations

- Views and metric views are not supported. If a view is based on existing tables, Databricks recommends classifying the underlying tables to determine if they contain sensitive data. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Data Classification System Table](/concepts/data-classification-system-table.md)
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- GDPR compliance
- System tables
- [Default storage](/concepts/workspace-default-storage-path.md)

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
