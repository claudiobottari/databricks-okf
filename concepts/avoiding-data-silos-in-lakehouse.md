---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea9ef694d7aca72d07cb7cf82c230c695cab38f92286a23c1b748a8dabce4e1a
  pageDirectory: concepts
  sources:
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - avoiding-data-silos-in-lakehouse
    - ADSIL
    - Data Lakehouse
  citations:
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
title: Avoiding Data Silos in Lakehouse
description: Principles and best practices for preventing data silos by using Unity Catalog views, OpenSharing, single sources of truth, and lineage tracking instead of copying or duplicating datasets across departments.
tags:
  - data-governance
  - data-architecture
  - unity-catalog
timestamp: "2026-06-19T19:55:25.397Z"
---

# Avoiding Data Silos in Lakehouse

**Avoiding Data Silos in Lakehouse** refers to the practices and architectural decisions that prevent isolated, duplicated copies of data from becoming stale, untrustworthy, and out of sync within a Databricks Lakehouse environment. Data silos undermine the single-source-of-truth principle and reduce trust in the data platform.

## Overview

Data movement, copy, and duplication take time and may decrease the quality of the data in the lakehouse, especially when they lead to data silos. These silos soon become out of sync, ultimately leading to a less trustworthy data lake. The goal is to minimize unnecessary duplication while still enabling agility and innovation. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Distinction Between Copy and Silo

A standalone or throwaway copy of data is not harmful on its own and is sometimes necessary to boost agility, experimentation, and innovation. The critical distinction is when such copies become operational—that is, when downstream business data products become dependent on them. At that point, the copy becomes a **data silo**. These operational silos inevitably drift out of sync with the source, eroding trust in the data and creating reconciliation burden. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Best Practices

The following best practices help avoid data silos in a lakehouse architecture:

- **Use Unity Catalog views and OpenSharing instead of copying data.** Virtual views and secure sharing mechanisms provide consumers with live access to the authoritative dataset without creating physical duplicates. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Establish a single source of truth for each dataset.** Every distinct data entity should have one canonical location (typically in the silver or gold layer of the [Medallion Architecture](/concepts/medallion-architecture.md)) from which all consumers read. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Discourage department-level data copies and duplicates.** Encourage teams to use shared datasets rather than creating and maintaining their own copies. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Use Unity Catalog lineage to track data dependencies.** Lineage visibility helps teams understand which datasets are upstream or downstream, making it easier to identify and retire redundant copies. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Retire redundant datasets regularly.** Schedule periodic reviews of the data catalog to identify and remove datasets that are no longer needed or that have been superseded by a canonical source. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Related Concepts

- Data Governance – Overarching framework for data quality, cataloging, and lineage.
- [Unity Catalog](/concepts/unity-catalog.md) – Central governance and metadata layer that enables views, OpenSharing, and lineage.
- [Medallion Architecture](/concepts/medallion-architecture.md) – Bronze, silver, gold layers that provide a structured path from raw data to curated data products, reducing the need for ad‑hoc copies.
- [Data Lineage](/concepts/data-lineage.md) – Tracking data flow from source to consumption to identify dependencies and silos.
- [Open Sharing](/concepts/opensharing.md) – Mechanism for sharing data without copying.

## Sources

- phase-6-design-delta-lake-architecture-databricks-on-aws.md

# Citations

1. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
