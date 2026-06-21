---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d64a32c5014896db1b66f571bf13eda6d69868e343961c801980bfba77bae03
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-producers-table
    - FTPT
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Producers Table
description: A UI component in the feature table page that lists all notebooks and jobs that write to a feature table, enabling freshness and job status verification.
tags:
  - feature-store
  - ui
  - provenance
timestamp: "2026-06-18T12:15:31.939Z"
---

# Feature Table Producers Table

The **Feature Table Producers Table** is a section of the [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) UI that displays information about all notebooks and jobs that write to a specific feature table. It provides visibility into the data pipelines that compute and maintain feature data. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Overview

On the feature table page (reached by clicking any feature table name in the workspace UI), the **Producers** table lists every notebook and job that writes data to that feature table. This enables users to monitor data freshness, confirm that scheduled jobs are running correctly, and understand which pipelines contribute to a given feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![producers table](https://docs.databricks.com/aws/en/assets/images/producers-table-72cf0e89e441f1d0637c6a1b13689051.png)

## Information Displayed

The Producers table contains metadata about each writing operation, including:

- **Notebooks and jobs** — Identifies the specific notebooks and jobs that write to the feature table.
- **Status of scheduled jobs** — Confirms whether scheduled jobs are completing successfully.
- **Feature freshness** — Provides insight into how recently data was written to the feature table.

This information allows you to quickly verify the health of your feature computation pipelines and ensure feature data is up to date. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Features Tables

The feature table page also contains other tables that together provide a complete picture of feature lineage:

- **Features table** — Lists all features in the table and provides links to models, endpoints, jobs, and notebooks that use each feature.
- **Tags table** — Displays key-value tags that can be used for searching and organizing feature tables.

## Use Cases

Common uses of the Producers table include:

- **Monitoring pipeline health** — Checking that scheduled jobs that compute features are running on time and without errors.
- **Identifying stale features** — Detecting feature tables that have not been written to recently.
- **Troubleshooting data issues** — Tracing back to the specific notebook or job that produces a given feature when investigating data quality or consistency problems.

## Related Concepts

- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The feature store platform that hosts the Producers table
- [Feature Tables](/concepts/feature-tables.md) — The organizational unit for feature data
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — The end-to-end tracking of how features are created and consumed
- Feature Freshness — How recently a feature table has been updated

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
