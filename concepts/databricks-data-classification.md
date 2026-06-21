---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6d56535af3dea62bf7b705aea0675c5a1cda1e0a11431d103dbcf9d96e0c588
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-classification
    - DDC
  citations:
    - file: data-classification-databricks-on-aws.md
title: Databricks Data Classification
description: An AI agent in Unity Catalog that automatically classifies and tags sensitive data across tables using large language models and intelligent scanning.
tags:
  - data-governance
  - classification
  - unity-catalog
  - security
timestamp: "2026-06-19T18:04:14.530Z"
---

# Databricks Data Classification

**Databricks Data Classification** is an AI-powered feature in [Unity Catalog](/concepts/unity-catalog.md) that automatically discovers, classifies, and tags sensitive data across tables in a catalog. It uses an agentic LLM-based system to identify sensitive information, helping data teams govern and democratize access to data at scale. ^[data-classification-databricks-on-aws.md]

## Overview

Data catalogs often contain vast amounts of both known and unknown sensitive data. Databricks Data Classification addresses this by using an AI agent to automatically classify and tag tables, enabling organizations to discover sensitive data and apply governance controls using tools such as [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md). ^[data-classification-databricks-on-aws.md]

The feature uses a large language model (LLM) to assist with classification. Classification results are stored using default storage, and users are not billed for storage costs. ^[data-classification-databricks-on-aws.md]

### Key Capabilities

- **Classify data**: The engine uses an agentic AI system to automatically classify and tag any tables in Unity Catalog. ^[data-classification-databricks-on-aws.md]
- **Optimize cost through intelligent scanning**: The system intelligently determines when to scan data by leveraging Unity Catalog and the Data Intelligence Engine. Scanning is incremental and optimized to ensure all new data is classified without manual configuration. ^[data-classification-databricks-on-aws.md]
- **Review and protect sensitive data**: The results display assists in viewing classification results and protecting sensitive data by tagging and creating access control policies for each classification class. ^[data-classification-databricks-on-aws.md]

## Requirements

- The workspace must have Serverless Compute available (enabled by default in workspaces with Unity Catalog). ^[data-classification-databricks-on-aws.md]
- To enable data classification, you must own the catalog or have `USE CATALOG` and `MANAGE` privileges on it. ^[data-classification-databricks-on-aws.md]
- To enable automatic tagging for a catalog, you need `USE CATALOG` on the catalog, `APPLY TAG` on the catalog, and `ASSIGN` on the tag being applied. ^[data-classification-databricks-on-aws.md]
- To view classification results in the UI, you need `USE CATALOG` and either `MANAGE` or (`SELECT` + `USE SCHEMA`) on the catalog. To see sample values associated with detections, you need `SELECT` on the results system table. ^[data-classification-databricks-on-aws.md]

By default, only account admins have `MANAGE` and `ASSIGN` permissions on data classification system governed tags. Account admins can grant these permissions to other users, service principals, or groups. ^[data-classification-databricks-on-aws.md]

## Enabling Data Classification

You can enable data classification for multiple catalogs at once or configure individual catalogs with more granular schema-level control.

### Enable Multiple Catalogs

1. On the Data Classification results page, click **Configure**.
2. Select the catalogs you want to enable, or select all available catalogs in the workspace.
3. Click **Enable**.

Enabling all available catalogs does not automatically enable future catalogs. You must return to the Configure dialog to classify a new catalog. ^[data-classification-databricks-on-aws.md]

### Enable a Single Catalog with Schema Selection

1. Navigate to the catalog and click the **Details** tab.
2. Next to **Data Classification**, click the **Enable** button.
3. In the dialog, select schemas to include from the **Schemas to include** dropdown menu. You can also select a **Usage policy**.
4. Click **Save**.

This creates a background job that incrementally scans all tables in the catalog or selected schemas. New tables and columns are typically scanned within 24 hours of creation. ^[data-classification-databricks-on-aws.md]

## Viewing Classification Results

To view classification results, click **View results** next to the **Data Classification** setting. This opens the Data Classification UI for the catalog. A Serverless SQL Warehouse is required. ^[data-classification-databricks-on-aws.md]

You can view aggregated results across all classified catalogs in the [Metastore](/concepts/metastore.md) by using the catalog selector and choosing **All catalogs**. ^[data-classification-databricks-on-aws.md]

For each classification type, the table displays:
- **Detected columns**: The number of columns where the classification was detected.
- **Auto-tagging**: The tagging status — **Active**, **Inactive**, or (in the [Metastore](/concepts/metastore.md) view) **Partially Active**.
- **User Access (last 7d)**: The number of distinct users who accessed unmasked vs. masked data of that classification over the last 7 days. ^[data-classification-databricks-on-aws.md]

### Reviewing Detections

To review results for a specific classification type, click **Review**. A panel appears with two tabs:

- **Detected Columns**: Displays columns where the classification tag was detected with high confidence, ordered by most recent detection first. Includes a **Detections over time** chart and a list of detected columns with sample values.
- **User Access**: Lists users who accessed columns with this classification tag, showing their email and username along with whether they have masked or unmasked access. Also shows any ABAC policies assigned to this classification tag. ^[data-classification-databricks-on-aws.md]

### Excluding Detections

You can exclude individual column detections from the review panel. Excluding a detection:
- Removes any existing classification tag from that column.
- Prevents future scans from reapplying the tag to that column.
- Provides feedback that improves the accuracy of future classification results. ^[data-classification-databricks-on-aws.md]

To exclude a detection, click the **Exclude** icon for the corresponding column. To re-include the detection, click the icon again. This feature is in Beta. ^[data-classification-databricks-on-aws.md]

## Automatic Tagging

When automatic tagging is enabled, all existing and future detections of a classification are tagged. You can configure tagging at two levels:

- **Metastore level**: Enable or disable across all catalogs. Requires [Metastore](/concepts/metastore.md) admin privileges and `ASSIGN` on the tag.
- **Catalog level**: Enable or disable for the current catalog only. Requires `USE CATALOG`, `APPLY TAG`, and `ASSIGN` on the tag. Catalog-level settings take precedence over the [Metastore](/concepts/metastore.md) level. ^[data-classification-databricks-on-aws.md]

Catalog-level automatic tagging has three states:
- **Default (inherited)**: Inherits the tagging setting from the [Metastore](/concepts/metastore.md) level.
- **Active**: Tagging is explicitly enabled for this catalog.
- **Inactive**: Tagging is explicitly disabled for this catalog. ^[data-classification-databricks-on-aws.md]

When you disable tagging, no future tags are applied, but existing tags are not removed. When enabling tagging, tags are not backfilled immediately — they will be populated in the next scan (typically within 24 hours). ^[data-classification-databricks-on-aws.md]

## Governance Controls

### Mask Sensitive Data Using ABAC

Databricks recommends using [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) to create governance controls based on classification results. From the Data Classification results page, you can create policies pre-filled to mask columns with a specific classification tag. You can also create policies covering multiple classification tags using conditions like `has_tag("class.name") OR has_tag("class.email_address") OR has_tag("class.phone_number")`. ^[data-classification-databricks-on-aws.md]

### GDPR Discovery and Deletion

Data classification can assist with data discovery and deletion for GDPR compliance. See the GDPR discovery and deletion notebook for details. ^[data-classification-databricks-on-aws.md]

## Results System Table

Data classification creates a system table named `system.data_classification.results` to store results. By default, only account admins can access it. The table contains all classification results across the entire [Metastore](/concepts/metastore.md), including sample values from tables in each catalog. It should only be shared with users privileged to see metastore-wide classification results. The table is only accessible using serverless compute. ^[data-classification-databricks-on-aws.md]

Users with `SELECT` access to this table can see sample values associated with detections on the Data Classification results page. ^[data-classification-databricks-on-aws.md]

## Scan Errors

If any errors occur during scanning, an **Errors** button appears at the upper right of the results table. Click it to display tables that failed the scan and associated error messages. By default, failures for individual tables are skipped and retried the following day. ^[data-classification-databricks-on-aws.md]

## Expenses

You can view Data Classification expenses by querying the `system.billing.usage` system table. The billing origin product is `DATA_CLASSIFICATION`. You can break down costs by `created_by` (user who triggered usage) or `catalog_id` (shown in the `system.data_classification.results` table). The initial scan is more costly than subsequent incremental scans on the same catalog. ^[data-classification-databricks-on-aws.md]

You can also view usage from a configured usage dashboard by filtering on the Billing Origin Project labeled "Data Classification." ^[data-classification-databricks-on-aws.md]

## Supported Classification Tags

For a full list of supported tags organized by [Global Tags](/concepts/global-tags.md), [Regional Tags](/concepts/regional-tags.md), and compliance frameworks (PII, GDPR, HIPAA, DPDPA), see Supported Classification Tags. ^[data-classification-databricks-on-aws.md]

## Limitations

- Views and Metric Views are not supported. If a view is based on existing tables, Databricks recommends classifying the underlying tables to check for sensitive data. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- Supported Classification Tags
- [Governed Tags](/concepts/governed-tags.md)
- Serverless Compute
- System Tables
- Data Governance
- [Data Profiling](/concepts/data-profiling.md)

## Sources

- data-classification-databricks-on-aws.md
- secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
- supported-classification-tags-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
