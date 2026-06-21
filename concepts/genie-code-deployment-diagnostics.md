---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7e096b5279e48db04f22c3f4deb2fded40e61904b71d06d79fd9ca75e8414d6
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-deployment-diagnostics
    - GCDD
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Genie Code Deployment Diagnostics
description: Capability to diagnose deployment failures, analyze build logs and endpoint state, and assess pending configuration changes.
tags:
  - deployment
  - diagnostics
  - troubleshooting
  - genie-code
timestamp: "2026-06-19T19:44:09.414Z"
---

# Genie Code Deployment Diagnostics

**Genie Code Deployment Diagnostics** refers to the observability and troubleshooting capabilities that [Genie Code](/concepts/genie-code.md) provides for [Model Serving](/concepts/model-serving.md) endpoints on Databricks. When used on a model serving endpoint page, Genie Code acts as a read-only advisor that can analyze endpoint health, diagnose deployment failures, investigate latency issues, and provide best practice guidance – all from the Genie Code pane. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Requirements

To use Genie Code for model serving observability, the workspace must have **Partner-powered AI features** enabled for both the account and the workspace, and the workspace must be in a supported region. Genie Code is a Designated Service that uses Geos to manage data residency. See [Geo availability of Genie Code features](https://docs.databricks.com/aws/en/genie-code/#geo-availability). ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

Currently, Genie Code only supports **custom model serving endpoints** (not Foundation Model APIs or external models). ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Capabilities

Genie Code can inspect endpoints and provide recommendations, but it cannot modify configurations or deployments. It provides step-by-step instructions and links to documentation so users can make changes themselves. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Health Checks and Diagnostics

- Check endpoint health and deployment states.
- Review configuration against best practices.
- Assess scaling and resource utilization.

### Troubleshooting and Analysis

- Diagnose deployment failures using build logs, events, and endpoint state.
- Investigate high latency or timeout issues using metrics, events, and inference table data.
- Analyze error patterns from service logs and inference tables.
- Identify misconfigurations or resource constraints.
- Compare current and pending configurations with risk assessment.

### Guidance and Best Practices

- Recommend optimal scaling configurations for production and development workloads.
- Explain endpoint states and transitions.
- Guide users on monitoring and observability setup.
- Search Databricks documentation and provide links to relevant articles.

## Common Use Cases

Users can start diagnostics by opening the Genie Code pane on an endpoint page, toggling **Agent** mode, and entering prompts such as:

- **Health checks**: "Check the health of this endpoint." / "Review my endpoint's scaling configuration."
- **Deployment failures**: "/diagnose" or "Why did my deployment fail?" / "My endpoint is stuck in a pending state."
- **Latency debugging**: "Why is my latency so high?" / "Analyze the latency spike from this morning."
- **Configuration review**: "What changed in my pending configuration?" / "Is my concurrency setting appropriate for production?"
- **Request history**: "Show me recent requests to this endpoint." / "What errors are my users hitting?" / "Analyze error patterns from the last week."

^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Related Concepts

- [Genie Code](/concepts/genie-code.md) – The underlying AI assistant framework.
- [Model Serving](/concepts/model-serving.md) – The Databricks service for deploying models.
- Model Serving Endpoint Health – Monitoring endpoint status and performance.
- Model Serving Debugging – General debugging guide for model serving.
- Production Optimization for Model Serving – Best practices for production endpoints.
- Monitor Model Quality and Endpoint Health – Official documentation on monitoring.

## Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
