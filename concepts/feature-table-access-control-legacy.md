---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bcd2811232e172f434771527b06277e0efac4da82aeec35ceda096c8606d25c9
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-access-control-legacy
    - FTAC(
    - Table Access Control (Legacy)
    - Table access control (legacy)
    - table access control (legacy)
    - Access Control (Legacy)
    - Access control (legacy)
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Access Control (Legacy)
description: Mechanisms to control user access to feature tables within the Databricks Workspace Feature Store, documented in a separate dedicated page.
tags:
  - feature-store
  - security
  - access-control
timestamp: "2026-06-18T12:15:47.807Z"
---

# Feature Table Access Control (Legacy)

**Feature Table Access Control (Legacy)** refers to the ability to restrict which users or groups can view, modify, or delete feature tables in the Databricks Workspace Feature Store. This feature is part of the legacy Workspace Feature Store and is accessible through the dedicated UI. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Overview

The legacy Workspace Feature Store provides a centralized interface for managing feature tables used in [MLflow](/concepts/mlflow.md) and [machine learning](/concepts/cicd-for-machine-learning.md) workflows. Access control allows administrators to enforce data governance by granting or denying permissions on individual feature tables. This ensures that only authorized users can view, update, or use the features in production pipelines. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Accessing the Feature Store UI

To manage feature table access, navigate to the **AI/ML** section in the sidebar and click **Features**. The UI displays all available feature tables along with metadata such as creator, data sources, online store publications, scheduled jobs, and last write time. From this interface, you can control access to each feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Controlling Access

For detailed instructions on setting up and managing permissions for feature tables, see the separate documentation on [Access control (legacy)](/concepts/feature-table-access-control-legacy.md). The access control page covers how to assign permissions to users and groups, and explains the available privilege levels. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Feature Store (Legacy)](/concepts/databricks-workspace-feature-store-legacy.md) — The overall feature store platform
- [Access control (legacy)](/concepts/feature-table-access-control-legacy.md) — The detailed guide for configuring permissions
- Feature Table Lineage — Tracking how features are created and used
- Feature Freshness — Monitoring the timeliness of feature values

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
