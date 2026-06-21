---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c78938a7d081e94869af541475a042fe2df92dd88232bf1a5c57b07ae72afe74
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-for-model-serving-observability
    - GCFMSO
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Genie Code for Model Serving Observability
description: An AI-powered read-only advisor that helps diagnose issues, analyze performance, and provide guidance for Databricks model serving endpoints.
tags:
  - model-serving
  - observability
  - ai-assistant
  - databricks
timestamp: "2026-06-19T19:44:12.622Z"
---

# Genie Code for Model Serving Observability

**Genie Code for Model Serving Observability** is a feature that enables interactive diagnosis, performance analysis, and best-practice guidance for [model serving](/concepts/model-serving.md) endpoints directly within the Databricks workspace. When used on a model serving endpoint page, Genie Code acts as a read-only observability companion that can inspect endpoints, analyze logs and metrics, and provide actionable recommendations. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Requirements

To use Genie Code for model serving observability, the workspace must meet the following conditions:

- Partner-powered AI features must be enabled for both the account and the workspace. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- The workspace must be in a supported region, as Genie Code is a Designated Service that uses Geos to manage data residency. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Currently, Genie Code only supports [Custom Model Serving Endpoints|custom model serving endpoints](/concepts/model-serving-endpoint-custom-models.md). ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Capabilities

Genie Code provides three broad categories of capabilities for model serving observability, all delivered through a natural-language interface.

### Health checks and diagnostics

Genie Code can analyze an endpoint’s status and configuration to identify potential issues:

- Check endpoint health and deployment states. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Review configuration against best practices. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Assess scaling and resource utilization. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Troubleshooting and analysis

Genie Code helps resolve issues by using endpoint metadata and telemetry:

- Diagnose deployment failures using build logs, events, and endpoint state. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Investigate high latency or timeout issues using metrics, events, and inference table data. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Analyze error patterns from service logs and inference tables. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Identify misconfigurations or resource constraints. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Compare current and pending configurations with risk assessment. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Guidance and best practices

Genie Code offers recommendations based on an endpoint’s specific configuration:

- Recommend optimal scaling configurations for production and development workloads. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Explain endpoint states and transitions. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Guide on monitoring and observability setup. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- Search Databricks documentation and provide links to relevant articles. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## How to use

To get started with Genie Code on a model serving endpoint page:

1. Navigate to a model serving endpoint page. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
2. Click the sparkle Genie Code icon to open the Genie Code pane. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
3. In the lower-right corner, select **Agent** to toggle on Genie Code’s Agent mode. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
4. Enter a prompt describing what you need help with (e.g., “Check the health of this endpoint”). ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

Genie Code is a read-only advisor in this mode. It can inspect endpoints and provide recommendations, but it cannot modify configurations or deployments. Instead, it provides step-by-step instructions and links to documentation so that users can make changes themselves. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Use cases

The following example prompts illustrate common tasks:

- **Health checks:** “Check the health of this endpoint.” / “Is my endpoint configured correctly?” / “Review my endpoint’s scaling configuration.” ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- **Deployment failures:** “/diagnose” or “Why did my deployment fail?” / “Help me fix deployment errors.” / “My endpoint is stuck in a pending state.” ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- **Latency debugging:** “Why is my latency so high?” / “Analyze the latency spike from this morning.” / “Show me the performance metrics for the last 24 hours.” ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- **Configuration review:** “What changed in my pending configuration?” / “Is my concurrency setting appropriate for production?” / “Show me my inference table configuration.” ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- **Request history:** “Show me recent requests to this endpoint.” / “What errors are my users hitting?” / “Analyze error patterns from the last week.” ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Additional information

For further guidance, refer to the following related documentation:

- [Genie Code](/concepts/genie-code.md) — General overview of the Genie Code feature.
- [Model Serving](/concepts/model-serving.md) — Core model serving concepts on Databricks.
- Model Serving Debugging — Debugging guide for model serving.
- Model Serving Production Optimization — Production optimization guidance.
- Endpoint Monitoring — Monitoring model quality and endpoint health.

## Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
