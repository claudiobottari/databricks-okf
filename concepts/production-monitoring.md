---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36f1bd710e186db38ab0a5fce482ed6d578b90cf9e8d53f627b5aefc103bf977
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - production-monitoring
    - Production Monitoring for LLMs
    - Production monitoring service
    - Set up production monitoring
    - production monitoring service
    - Production quality monitoring
    - Production tracing
    - production monitoring with MLflow
    - production quality monitoring
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: Production Monitoring
description: Capability to reuse LLM judges and scorers from development to monitor GenAI applications in production, ensuring consistent evaluation throughout the application lifecycle.
tags:
  - mlflow
  - monitoring
  - production
timestamp: "2026-06-19T18:41:24.711Z"
---

# Production Monitoring

**Production monitoring** is the phase of the AI application lifecycle in which deployed AI agents, large language models (LLMs), RAG systems, or other generative AI applications are continuously assessed for quality and performance. It is a component of MLflow 3’s evaluation and monitoring capabilities, which support the entire development lifecycle from testing through production. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Overview

Production monitoring reuses the same judges and scorers that were used during development evaluation. This ensures consistent evaluation criteria across all lifecycle stages, enabling teams to detect regressions, track performance trends, and maintain application quality over time. The evaluation and monitoring component builds upon [MLflow Tracing](/concepts/mlflow-tracing.md), which provides real-time trace logging in development, testing, and production phases. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Workflow

The production monitoring workflow fits into a larger iterative cycle:

1. **Development and testing** – Traces are evaluated using built-in or custom [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md).
2. **Production** – The same judges and scorers are reused to monitor live traffic.
3. **Human feedback** – Domain experts can provide feedback using an integrated [Review App](/concepts/mlflow-review-app.md), producing evaluation data that can be used for further iteration. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

This closed loop allows teams to iteratively optimize the quality of their GenAI applications by incorporating both automated metrics and human judgment. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Key Concepts

- **MLflow Tracing** – Enables real-time trace logging across all phases, providing the data that powers production monitoring dashboards and alerts. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Judges and Scorers** – Functions that compute quality, safety, or correctness metrics; they are authored during development and reused in production. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Review App** – A human feedback interface that allows domain experts to annotate traces and produce ground-truth data for continuous improvement. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Agent Evaluation** – The broader capability that includes production monitoring as one of its lifecycle phases. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md)
- [Review App](/concepts/mlflow-review-app.md)
- [AI Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- RAG Evaluation

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
