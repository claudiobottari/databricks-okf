---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8aee487bcd50f4d436d4c338be26398ab3bbb70498fe08f7795ca19b248d6886
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-results-system-table
    - DCRST
  citations:
    - file: data-classification-databricks-on-aws.md
title: Data Classification Results System Table
description: A system table (system.data_classification.results) storing all classification results across the metastore, including sample values, accessible only via serverless compute.
tags:
  - system-table
  - audit
  - classification
timestamp: "2026-06-18T14:58:41.090Z"
---

# Data Classification Results System Table

The **Data Classification Results System Table** (`system.data_classification.results`) is a system table created by Databricks Data Classification to store the outcomes of automated sensitive-data scanning across a [Metastore](/concepts/metastore.md). It enables account admins and privileged users to inspect classification tags, sample values, and associated metadata for all catalogs in a single location. ^[data-classification-databricks-on-aws.md]

## Contents

The table contains all classification results across the entire [Metastore](/concepts/metastore.md), including sample values extracted from columns in each catalog. Each row corresponds to a detection of a [classification tag](/concepts/data-classification.md) on a column, along with the tag name, the column and table identifiers, and the timestamp of detection. The table also includes the `catalog_id` field, which can be used to break down costs when querying the `system.billing.usage` table for Data Classification expenses. ^[data-classification-databricks-on-aws.md]

## Access and Permissions

By default, only **account admins** have access to the results system table. Account admins can grant `SELECT` permission on the table to other users or service principals. ^[data-classification-databricks-on-aws.md]

- The table is only accessible when using [serverless compute](/concepts/serverless-gpu-compute.md). ^[data-classification-databricks-on-aws.md]
- Because the table contains sample values from tables in every catalog, Databricks recommends sharing it only with users who are privileged to see metastore-wide classification results, including sample values. ^[data-classification-databricks-on-aws.md]
- Users who have `SELECT` on this table can also see sample values associated with detections on the Data Classification results page in the UI. ^[data-classification-databricks-on-aws.md]

## Usage

The primary uses of the results system table are:

- **Auditing and discovery**: Review which columns across the [Metastore](/concepts/metastore.md) have been classified, what tags were applied, and when the detection occurred.
- **Cost analysis**: Join with `system.billing.usage` using the `catalog_id` field to break down Data Classification costs by catalog over a given time period. ^[data-classification-databricks-on-aws.md]
- **Governance integration**: Use the classification results to inform the creation of [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) or other access controls.

For the full schema of the table, see the [Data classification system table reference](https://docs.databricks.com/aws/en/admin/system-tables/data-classification). ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The feature that generates the results stored in this table.
- Classification Tags – The governed tags (e.g., `class.email_address`) that are applied to columns.
- Serverless Compute – Required to query the system table.
- System Tables – The broader framework for system-provided tables in Databricks.
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) – Used to create governance policies based on classification results.
- [Cost Monitoring for Data Classification](/concepts/data-classification-billing-and-cost-monitoring.md) – How to use the results table to track expenses.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
