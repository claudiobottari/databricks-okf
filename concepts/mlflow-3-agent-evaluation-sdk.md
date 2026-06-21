---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 157a51d6805739c770f938000e1e3a49c50521bb2e26c8bcca664a02002340c5
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-agent-evaluation-sdk
    - M3AES
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: MLflow 3 Agent Evaluation SDK
description: The `mlflow[databricks]>=3.1` SDK that provides Agent Evaluation methods as part of the managed MLflow 3 platform.
tags:
  - mlflow
  - sdk
  - migration
timestamp: "2026-06-19T18:41:33.452Z"
---

Here is the wiki page for "MLflow 3 Agent Evaluation SDK", written solely from the provided source material.

---

# MLflow 3 Agent Evaluation SDK

The **MLflow 3 Agent Evaluation SDK** provides programmatic tools for evaluating, monitoring, and improving AI agents and large language model (LLM) applications built on [MLflow 3](/concepts/mlflow-3.md). It offers a unified interface for offline evaluation, production monitoring, and human feedback collection, extending the capabilities of [MLflow Tracing](/concepts/mlflow-tracing.md).

## Overview

The Agent Evaluation SDK is part of the managed MLflow 3 platform. It is designed to help developers iteratively optimize the quality of GenAI applications by measuring performance across multiple components, multi-turn conversations, and nuanced quality criteria. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Package and version

The SDK methods are available via the `mlflow[databricks]>=3.1` Python package. Users upgrading from Agent Evaluation in MLflow 2 should follow the [migration guide from MLflow 2 Agent Evaluation](/concepts/mlflow-3-migration-from-mlflow-2x.md) to update their code. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Key capabilities

- **Trace-based evaluation** – Traces from development, testing, and production can be evaluated using built-in or custom [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md). Traces are logged in real time and can be scored offline. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Production monitoring** – The same judges and scorers used during development can be deployed for continuous quality monitoring in production, ensuring consistent evaluation across the application lifecycle. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Human feedback integration** – Domain experts can provide feedback through an integrated [Review App](/concepts/mlflow-review-app.md), producing evaluation data that can be used for further iteration. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Migration from MLflow 2 Agent Evaluation

The SDK is integrated with managed MLflow 3. Developers who used the MLflow 2 Agent Evaluation SDK should refer to the dedicated migration documentation to adopt the new APIs and package structure. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related concepts

- [MLflow 3](/concepts/mlflow-3.md) – The platform underlying the Agent Evaluation SDK.
- [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) – Customizable evaluators for agent outputs.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Real-time trace logging used as input for evaluation.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Reusing judges in production.
- [Review App](/concepts/mlflow-review-app.md) – Interface for collecting human feedback.

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
