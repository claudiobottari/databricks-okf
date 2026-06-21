---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d987037bf2171aee2876924757c577b3ccfe0fe8b21fd6a5b089d406bb84f66
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-egress-pipeline-notebooks
    - OEPN
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: OpenSharing Egress Pipeline Notebooks
description: Two Databricks Marketplace notebooks (IP Ranges Mapping Pipeline and Egress Cost Analysis Pipeline) that use Lakeflow Spark Declarative Pipelines to monitor egress usage patterns and costs by joining logs with cloud provider IP ranges and OpenSharing system tables.
tags:
  - delta-sharing
  - monitoring
  - notebooks
  - cost-management
timestamp: "2026-06-19T19:45:28.192Z"
---

# OpenSharing Egress Pipeline Notebooks

**OpenSharing Egress Pipeline Notebooks** are two notebooks available in the Databricks Marketplace that help providers monitor and manage cloud vendor egress costs associated with [OpenSharing](/concepts/opensharing.md) data and AI asset sharing. The notebooks are included in the *OpenSharing Egress Pipeline* listing (ID `a6f2e062-3084-4976-9eb0-47b2c8244d43`). ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Notebooks

The listing contains two notebooks that each create and execute a [Lakeflow Spark Declarative Pipeline](/concepts/lakeflow-spark-declarative-pipelines.md):

- **IP Ranges Mapping Pipeline notebook**
- **Egress Cost Analysis Pipeline notebook**

^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## How It Works

When run as a Lakeflow Spark Declarative Pipelines template, the notebooks automatically generate a detailed cost report. They join logs with cloud provider IP range tables and OpenSharing system tables to produce egress bytes transferred, attributed by share and recipient. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

Complete installation requirements and step-by-step instructions are provided in the Marketplace listing. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- Databricks Marketplace
- Egress cost management for OpenSharing
- Replicate data to avoid egress costs
- [Cloudflare R2 storage for egress-free sharing](/concepts/cloudflare-r2-integration-for-zero-egress-sharing.md)

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
