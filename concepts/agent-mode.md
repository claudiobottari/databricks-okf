---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc2caa106139c98fd625d6faabb79d052c92c776c83a4a0ee5942e4e9e679171
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-mode
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Agent Mode
description: A toggle in the Genie Code pane that enables interactive, prompt-driven troubleshooting and analysis of model serving endpoints.
tags:
  - genie-code
  - interactive
  - troubleshooting
timestamp: "2026-06-19T19:44:09.208Z"
---

# Agent Mode

**Agent Mode** is a feature within [Genie Code](/concepts/genie-code.md) that transforms the Genie Code pane into an observability companion for [Model Serving](/concepts/model-serving.md) endpoints. When activated, Agent Mode enables Genie Code to diagnose issues, analyze performance, and provide guidance — all in a read‑only, step‑by‑step advisory capacity. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## How to Enable

Agent Mode is toggled on from a model serving endpoint page:

1. Navigate to a model serving endpoint page.
2. Click the Genie Code icon to open the Genie Code pane.
3. In the lower‑right corner of the pane, select **Agent**.

Once enabled, you can enter prompts such as “Check the health of this endpoint” or “Why is my latency so high?” to start the analysis. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Capabilities

When Agent Mode is active, Genie Code can perform the following tasks:

- **Health checks and diagnostics** – Review endpoint status, deployment states, configuration best practices, and scaling/resource utilization. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- **Troubleshooting and analysis** – Diagnose deployment failures using build logs and events; investigate high latency or timeouts with metrics, events, and inference table data; analyze error patterns; identify misconfigurations or resource constraints; compare current and pending configurations with risk assessment. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- **Guidance and best practices** – Recommend optimal scaling configurations for production and development; explain endpoint states and transitions; guide monitoring and observability setup; search Databricks documentation and provide links to relevant articles. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Requirements

To use Agent Mode for model serving observability, the workspace must have:

- Partner‑powered AI features enabled for both the account and workspace.
- The workspace in a supported region. Genie Code is a Designated Service that uses Geos to manage data residency.

Additionally, Agent Mode currently supports only **custom model serving endpoints**. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Limitations

Agent Mode is a **read‑only advisor**. It can inspect endpoints and provide recommendations, but it cannot modify configurations or trigger deployments. Any changes must be made manually by the user using the provided step‑by‑step instructions and documentation links. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Related Concepts

- [Genie Code](/concepts/genie-code.md) – The overall AI assistant on Databricks.
- [Model Serving](/concepts/model-serving.md) – The deployment and management of ML models as endpoints.
- [Endpoint Health Monitoring](/concepts/endpoint-health-metrics.md) – The practice of tracking endpoint status and performance.
- Observability – The ability to understand and diagnose system behavior.

## Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
