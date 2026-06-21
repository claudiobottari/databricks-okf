---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e3b8438a76964d60017a5de6a606b1ec4490452d0ba6a0c682979293043543c
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-latency-and-error-analysis
    - Error Analysis and Genie Code Latency
    - GCLAEA
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Genie Code Latency and Error Analysis
description: Ability to investigate high latency, timeout issues, and error patterns using metrics, events, inference tables, and service logs.
tags:
  - latency
  - error-analysis
  - monitoring
  - genie-code
timestamp: "2026-06-19T19:44:29.089Z"
---

# Genie Code Latency and Error Analysis

**Genie Code Latency and Error Analysis** refers to the diagnostic capabilities of [Genie Code](/concepts/genie-code.md) when used as an observability companion for [Model Serving](/concepts/model-serving.md) endpoints on Databricks. It enables you to investigate high latency, timeouts, error patterns, and deployment failures directly from the endpoint page.

## Overview

Genie Code acts as a read-only advisor for custom model serving endpoints. It can inspect endpoint configurations, review metrics and events, and analyze inference table data to identify the root cause of performance issues. It cannot modify configurations or deployments, but it provides step-by-step guidance and links to documentation so you can make changes yourself. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Requirements

To use Genie Code for latency and error analysis, your workspace must meet the following requirements:

- **Partner-powered AI features** enabled for both the account and the workspace. See [Partner-Powered AI Features](/concepts/partner-powered-ai-features-on-databricks.md).
- Workspace located in a supported region. Genie Code is a Designated Service that uses Geos for data residency. See [Geo availability of Genie Code features](https://docs.databricks.com/aws/en/genie-code/#geo-availability).
- Only **custom model serving endpoints** are currently supported. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Accessing Genie Code

1. Navigate to a model serving endpoint page.
2. Click the sparkle genie code icon to open the Genie Code pane.
3. In the lower‑right corner of the pane, select **Agent** to enable Agent mode.
4. Enter a prompt describing the issue, such as *“Why is my latency so high?”* or *“Analyze error patterns from the last week.”* ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Capabilities for Latency and Error Analysis

Genie Code provides the following capabilities relevant to latency and error investigation:

### Latency Investigation

- Investigate **high latency or timeout issues** using metrics, events, and inference table data.
- Analyze **performance metrics** such as request latency over time.
- Compare current performance with historical baselines to identify spikes or trends. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Error Analysis

- Analyze **error patterns** from service logs and inference tables.
- Determine which errors users are encountering and whether they stem from misconfigurations, resource constraints, or model behavior.
- Diagnose **deployment failures** using build logs, events, and endpoint state. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Health Checks and Configuration Review

- Assess **scaling and resource utilization** to identify if underprovisioning contributes to latency.
- Review endpoint configuration against best practices (e.g., concurrency settings, inference table setup).
- Compare current and pending configurations with a risk assessment. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Example Prompts

The following prompts are recommended for latency and error analysis:

- `"Why is my latency so high?"`
- `"Analyze the latency spike from this morning."`
- `"Show me the performance metrics for the last 24 hours."`
- `"What errors are my users hitting?"`
- `"Analyze error patterns from the last week."`
- `"Show me recent requests to this endpoint."`
- `"Help me fix deployment errors."`
- `"Is my endpoint configured correctly?"` ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Limitations

- Genie Code is a **read-only** advisor; it cannot modify endpoint configurations, scaling policies, or deployments.
- Only **custom model serving endpoints** are supported; foundation model endpoints are not yet covered.
- Requires **Partner-powered AI features** and a supported region. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The platform for deploying custom and foundation models on Databricks.
- [Genie Code](/concepts/genie-code.md) – The AI assistant that powers observability and troubleshooting.
- [Inference Table](/concepts/inference-tables.md) – A storage table that captures request and response data for analysis.
- [Endpoint Health Monitoring](/concepts/endpoint-health-metrics.md) – Broader monitoring and alerting for model serving endpoints.
- Databricks Partner-Powered AI – The feature enabling third‑party AI integrations like Genie Code.
- Model Serving Debugging Guide – Databricks documentation for step‑by‑step troubleshooting.

## Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
