---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5ebd62b18683fb8b0dce2de3880749f224810e9abc5c4211c515496fdd57c75
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-requirements
    - GCR
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Genie Code Requirements
description: To use Genie Code for agent observability and evaluation, the workspace needs Partner-powered AI features enabled for both account and workspace, and the workspace must be in a supported region as Genie Code uses Geos for data residency.
tags:
  - databricks
  - requirements
  - genai
  - prerequisites
timestamp: "2026-06-18T12:29:15.632Z"
---

#Genie Code Requirements

**Genie Code** provides a natural language interface for understanding, debugging, and improving GenAI applications within MLflow. It has read access to experiment data—including traces, prompts, datasets, evaluation runs, scorers, and labeling sessions—allowing users to explore observability and evaluation data conversationally instead of writing queries or navigating multiple UI pages.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Requirements

To use Genie Code for agent observability and evaluation, your workspace must meet the following requirements:

### Partner-Powered AI Features

Partner-powered AI features must be enabled for both the account and the workspace. See [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) for enablement instructions.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Supported Region

Your workspace must be in a supported region. Genie Code is a Designated Service that uses Geos to manage data residency. For the list of supported regions, see Geo availability of Genie Code features.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities Summary (Context)

While the requirements above are necessary for access, Genie Code supports a wide range of observability and evaluation tasks once those prerequisites are met. These include trace analysis and debugging, metrics and performance review, quality evaluations, labeling and review, prompt registry browsing, and instrumentation guidance.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [Genie Code](/concepts/genie-code.md) — The overall feature for natural-language observability
- [MLflow Tracing](/concepts/mlflow-tracing.md) — End-to-end observability for GenAI agents
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Setting up evaluation and monitoring
- [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) — Enablement prerequisite
- [Designated Services](/concepts/databricks-designated-service-with-geos.md) — Data residency classification
- Geos — Geographic data management

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
