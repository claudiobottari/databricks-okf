---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f79a896f2395ab9c746e854c2bedf5201f07b6199a7fb90893ac54dd644fa1c
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-producers
    - FTP
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Producers
description: Notebooks and jobs that write to a feature table, visible in the Producers table on the feature table detail page.
tags:
  - feature-store
  - pipeline
  - provenance
timestamp: "2026-06-19T18:45:36.160Z"
---

# Feature Table Producers

**Feature Table Producers** is a UI component within the Databricks Workspace Feature Store that lists all notebooks and jobs that write data to a given feature table. It appears on the feature table detail page and is used to track the data pipeline responsible for populating and refreshing the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Overview

The Producers table provides a centralized view of every notebook and job that writes to a specific feature table. Its primary purpose is to let you quickly confirm the status of scheduled jobs and assess the **freshness** of the feature table — i.e., how recently the data was last updated. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

By reviewing the Producers table, you can identify:

- Which notebooks or jobs are responsible for writing to the feature table.
- Whether those jobs are running as scheduled or have failed.
- The last time a write operation occurred, giving you an indication of data freshness.

This makes the Producers table an essential tool for monitoring [Feature Lineage](/concepts/feature-lineage-tracking.md) and operational health of feature pipelines.

## Usage

To access the Producers table:

1. Open the Databricks Workspace Feature Store UI by clicking **Features** under **AI/ML** in the sidebar.
2. Click the name of any feature table to display its detail page.
3. On the feature table page, locate the **Producers** section. It lists all writing notebooks and jobs with relevant metadata.

The table is read-only and does not allow editing or adding new producers directly. It serves as an audit and monitoring interface.

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Feature Table](/concepts/feature-table.md)
- [Feature Lineage](/concepts/feature-lineage-tracking.md)
- [Workspace Feature Store UI](/concepts/workspace-feature-store-ui.md)
- [Data Freshness](/concepts/data-freshness.md)

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
