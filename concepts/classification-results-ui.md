---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c2a7505ea8cf5173a7e5fd934661c4d8e9464f1caf47433db78ae6d0fa5cf9f
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classification-results-ui
    - CRU
    - View classification results
  citations:
    - file: data-classification-databricks-on-aws.md
title: Classification Results UI
description: The Databricks user interface that displays per-classification detection counts, auto-tagging status, user access patterns, and provides review panels for detected columns and user access details.
tags:
  - data-governance
  - ui
  - unity-catalog
timestamp: "2026-06-19T14:40:31.891Z"
---

# Classification Results UI

The **Classification Results UI** is the graphical interface within Databricks [Unity Catalog](/concepts/unity-catalog.md) that displays the output of [Data Classification](/concepts/data-classification.md) scans. It allows users to review detected sensitive data, manage automatic tagging, view user access patterns, and configure governance controls — all from a single dashboard.^[data-classification-databricks-on-aws.md]

## Accessing the UI

To view classification results for a catalog, click **View results** next to the **Data Classification** setting in the catalog's **Details** tab. This opens the Data Classification results page, which requires a serverless SQL warehouse to load.^[data-classification-databricks-on-aws.md]

You can also view aggregated results across all classified catalogs in the [Metastore](/concepts/metastore.md) by selecting **All catalogs** from the catalog selector drop-down menu at the upper left of the results page.^[data-classification-databricks-on-aws.md]

## Results Table

For each classification type, the UI displays a table with the following columns:^[data-classification-databricks-on-aws.md]

| Column | Description |
|--------|-------------|
| **Detected columns** | The number of columns where the classification was detected. |
| **Auto-tagging** | The tagging status — **Active**, **Inactive**, or (in the [Metastore](/concepts/metastore.md) view) **Partially Active** when tagging is enabled in some but not all catalogs. |
| **User Access (last 7d)** | The number of distinct users who accessed unmasked vs. masked data of that classification over the last 7 days. Use this to assess the exposure of sensitive data. |

## Reviewing Detections

Click **Review** in the rightmost column of the results table to open a panel with two tabs:^[data-classification-databricks-on-aws.md]

### Detected Columns Tab

This tab displays:^[data-classification-databricks-on-aws.md]

- **Detections over time** chart — Click any bar to see the specific detections for that date.
- A list of detected columns, ordered by most recent detection first.
- **Sample values** for each detected column (visible only if you have the required permissions).
- An **Exclude** icon for each column to mark an incorrect detection.

#### Excluding Detections

Excluding a detection (available in Beta):^[data-classification-databricks-on-aws.md]

- Removes any existing classification tag from that column.
- Prevents future scans from reapplying the tag.
- Provides feedback that improves the accuracy of future classification results.

To exclude a detection, click the **Exclude** icon. To re-include it, click the icon again.

### User Access Tab

This tab displays:^[data-classification-databricks-on-aws.md]

- A list of all users who accessed columns with this classification tag, including their email, username, and whether they have masked or unmasked access.
- Any [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies assigned to this classification tag.
- When viewing results for a single catalog, a **New policy** button to create an ABAC policy directly from the panel.

## Enabling Automatic Tagging

From the UI, you can enable automatic tagging for a classification tag at two levels:^[data-classification-databricks-on-aws.md]

- **Metastore level** — Enable or disable across all catalogs at once. Requires [Metastore](/concepts/metastore.md) admin privileges and `ASSIGN` on the tag.
- **Catalog level** — Enable or disable for the current catalog only. Catalog-level settings take precedence over the metastore-level setting. Requires `USE CATALOG`, `APPLY TAG`, and `ASSIGN` on the tag.

At the catalog level, automatic tagging has three states: **Default (inherited)**, **Active**, and **Inactive**. When you disable tagging, no future tags are applied, but existing tags are not removed. Tags are not backfilled immediately upon enabling; they populate in the next scan (typically within 24 hours).^[data-classification-databricks-on-aws.md]

## Configuring Classification

From the results page, click **Configure** to enable data classification for multiple catalogs at once. You can select individual catalogs or select all available catalogs. Enabling all available catalogs does not automatically enable future catalogs — you must return to the **Configure** dialog to enable new catalogs.^[data-classification-databricks-on-aws.md]

Alternatively, you can enable classification for a single catalog with schema-level control from the catalog's **Details** tab. This allows you to select specific schemas to include and set a usage policy.^[data-classification-databricks-on-aws.md]

## Scan Errors

If any errors occur during the scan, an **Errors** button appears at the upper right of the results table. Clicking it displays the tables that failed the scan and associated error messages. By default, failures for individual tables are skipped and retried the following day.^[data-classification-databricks-on-aws.md]

## Related Concepts

- Supported Classification Tags — The full list of tags organized by [Global Tags](/concepts/global-tags.md), [Regional Tags](/concepts/regional-tags.md), and compliance frameworks.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Create governance policies based on classification results.
- [Data Classification System Table](/concepts/data-classification-system-table.md) — The `system.data_classification.results` table that stores all classification results.
- [Data Classification Expenses](/concepts/data-classification-scans.md) — How to view billing and usage for data classification scans.
- GDPR Discovery and Deletion — Using classification results to assist with GDPR compliance.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
