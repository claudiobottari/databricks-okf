---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60d39dd7bf9735e95ee459a6b8967388bd84e787f2b56bcecda04bccdf3b23f3
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-best-practice-guidance
    - GCBPG
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Genie Code Best Practice Guidance
description: Provides recommendations on scaling configurations, endpoint states, monitoring setup, and links to relevant documentation.
tags:
  - best-practices
  - scaling
  - monitoring
  - genie-code
timestamp: "2026-06-19T19:44:23.969Z"
---

# Genie Code Best Practice Guidance

**Genie Code Best Practice Guidance** refers to the set of recommendations, diagnostics, and optimization advice that Genie Code provides for [Model Serving](/concepts/model-serving.md) endpoints on Databricks. When used as an observability companion, Genie Code analyzes endpoint configurations, identifies issues, and suggests improvements based on established best practices. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Overview

Genie Code functions as a read-only advisor for model serving endpoints. It can inspect endpoints and provide recommendations, but cannot modify configurations or deployments. It provides clear, step-by-step instructions and links to documentation so users can make changes themselves. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

This guidance is available only for [custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md). To use it, workspaces must have partner-powered AI features enabled and be in a supported region. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Verification

### Requirements

Workspaces must meet the following prerequisites:
- Partner-powered AI features enabled for both the account and workspace.
- Workspace located in a supported region for Genie Code. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Best Practice Recommendation Categories

### Configuration and Scaling

Genie Code reviews endpoint configuration against best practices and recommends optimal scaling configurations for both production and development workloads. It analyzes concurrency settings, resource utilization, and scaling parameters to ensure the endpoint is appropriately provisioned for its expected traffic patterns. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

Common recommendations include:
- Adjusting concurrency settings for production workloads.
- Identifying misconfigurations or resource constraints.
- Comparing current and pending configurations with risk assessment. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Endpoint Health and Monitoring

Genie Code can check endpoint health and deployment states, assess scaling and resource utilization, and guide users on monitoring and observability setup. It helps identify potential issues before they impact production traffic. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Deployment Best Practices

For deployment failures, Genie Code diagnoses issues using build logs, events, and endpoint state. It can explain endpoint states and transitions, helping users understand why a deployment is stuck in a pending state or why errors are occurring. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Performance Optimization

When investigating performance issues, Genie Code analyzes latency spikes, timeout issues, and error patterns using metrics, events, and inference table data. It provides guidance on how to resolve performance bottlenecks and optimize endpoint behavior. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Using Genie Code for Guidance

To access best practice guidance:
1. Navigate to a model serving endpoint page.
2. Click the sparkle Genie Code icon to open the Genie Code pane.
3. In the lower-right corner, select **Agent** to enable Agent mode.
4. Enter a prompt describing what help is needed. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Recommended Prompts

**Health checks:**
- "Check the health of this endpoint."
- "Is my endpoint configured correctly?"
- "Review my endpoint's scaling configuration."

**Deployment failures:**
- "/diagnose" or "Why did my deployment fail?"
- "Help me fix deployment errors."
- "My endpoint is stuck in a pending state."

**Latency debugging:**
- "Why is my latency so high?"
- "Analyze the latency spike from this morning."
- "Show me the performance metrics for the last 24 hours."

**Configuration review:**
- "What changed in my pending configuration?"
- "Is my concurrency setting appropriate for production?"
- "Show me my inference table configuration."

**Request history:**
- "Show me recent requests to this endpoint."
- "What errors are my users hitting?"
- "Analyze error patterns from the last week."

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform for deploying and serving models on Databricks.
- [Genie Code](/concepts/genie-code.md) — The AI-powered assistant for Databricks.
- Model Serving Observability — Monitoring and diagnostics for endpoints.
- Model Serving Debugging — Troubleshooting deployment and latency issues.
- Production Optimization for Model Serving — Guidelines for production-ready endpoints.
- [Inference Tables](/concepts/inference-tables.md) — Logging and analysis of inference requests.
- [Endpoint Health Monitoring](/concepts/endpoint-health-metrics.md) — Tracking endpoint status and performance.

## Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
