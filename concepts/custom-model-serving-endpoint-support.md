---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8eedcd48525d1a47eabe722ebe05f12065494631b48792071964008ab0928d48
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-model-serving-endpoint-support
    - CMSES
    - Custom Model Serving Endpoints
    - Custom model serving endpoint
    - Custom model serving endpoints
    - custom model serving endpoint
    - custom model serving endpoints
    - Create Custom Model Serving Endpoints
    - Create custom model serving endpoints
    - Custom Model Serving
    - custom model serving
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Custom Model Serving Endpoint Support
description: Genie Code for observability currently only supports custom model serving endpoints, not all endpoint types.
tags:
  - model-serving
  - limitations
  - databricks
timestamp: "2026-06-19T19:44:06.593Z"
---

# Custom Model Serving Endpoint Support

**Custom Model Serving Endpoint Support** refers to the ability of [Genie Code](/concepts/genie-code.md) on Databricks to serve as an observability companion specifically for custom model serving endpoints. Genie Code can analyze endpoint health, diagnose deployment failures, investigate latency issues, and provide best practice guidance — all from the Genie Code pane on an endpoint page.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Requirements

To use Genie Code for model serving observability, the workspace must have partner-powered AI features enabled for both the account and the workspace. The workspace must also be in a supported region, as Genie Code is a Designated Service that uses Geos to manage data residency.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Key Characteristics

Genie Code functions as a **read-only advisor** when used on a model serving endpoint page. It can inspect endpoints and provide recommendations, but it cannot modify configurations or deployments. It provides clear, step-by-step instructions and links to documentation so that users can make changes themselves.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Capabilities

### Health Checks and Diagnostics

Genie Code can analyze an endpoint's status and configuration to identify potential issues. This includes checking endpoint health and deployment states, reviewing configuration against best practices, and assessing scaling and resource utilization.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Troubleshooting and Analysis

Genie Code helps resolve issues by diagnosing deployment failures using build logs, events, and endpoint state; investigating high latency or timeout issues using metrics, events, and inference table data; analyzing error patterns from service logs and inference tables; identifying misconfigurations or resource constraints; and comparing current and pending configurations with risk assessment.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Guidance and Best Practices

Genie Code offers recommendations based on endpoint configuration, such as optimal scaling configurations for production and development workloads, explanations of endpoint states and transitions, guidance on monitoring and observability setup, and links to relevant Databricks documentation.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Use Cases

Common prompts that users can try include:

- **Health checks**: “Check the health of this endpoint.”, “Is my endpoint configured correctly?”, “Review my endpoint’s scaling configuration.”
- **Deployment failures**: “/diagnose” or “Why did my deployment fail?”, “Help me fix deployment errors.”, “My endpoint is stuck in a pending state.”
- **Latency debugging**: “Why is my latency so high?”, “Analyze the latency spike from this morning.”, “Show me the performance metrics for the last 24 hours.”
- **Configuration review**: “What changed in my pending configuration?”, “Is my concurrency setting appropriate for production?”, “Show me my inference table configuration.”
- **Request history**: “Show me recent requests to this endpoint.”, “What errors are my users hitting?”, “Analyze error patterns from the last week.”

^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Getting Started

To get started, navigate to a model serving endpoint page, click the Genie Code icon to open the pane, then select **Agent** mode (in the lower-right corner) to toggle on Genie Code’s agent mode. Enter a prompt describing the help needed — for example, “Check the health of this endpoint” or “Why is my latency so high?”.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Related Concepts

- [Genie Code](/concepts/genie-code.md) – General overview of the Genie Code assistant.
- [Model Serving](/concepts/model-serving.md) – Deployment and management of models on Databricks.
- [Inference Table](/concepts/inference-tables.md) – Storage of request/response data used by Genie Code for analysis.
- Monitoring Model Endpoints – Best practices for endpoint observability.

## Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
