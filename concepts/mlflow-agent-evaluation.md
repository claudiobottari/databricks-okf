---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1909e8f06b0d24f0c3042feac8ef7509b49e80fa4b03fb189034a0ac3fa18e2c
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-agent-evaluation
    - MAE
    - AI Agent Evaluation
    - Agent Evaluation
    - Agent evaluation
    - MLflow GenAI Agent Evaluation
    - agent evaluation
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: MLflow Agent Evaluation
description: Comprehensive evaluation framework for AI agents, LLMs, RAG systems, and GenAI applications covering the entire development lifecycle from testing through production monitoring.
tags:
  - mlflow
  - evaluation
  - ai-agents
timestamp: "2026-06-19T18:41:11.922Z"
---

```markdown
---
title: MLflow Agent Evaluation
summary: Comprehensive evaluation framework for AI agents and LLMs, supporting multi-component, multi-turn conversation assessment across the entire development lifecycle.
sources:
  - evaluate-and-monitor-ai-agents-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:12:05.094Z"
updatedAt: "2026-06-18T12:12:05.094Z"
tags:
  - mlflow
  - evaluation
  - ai-agents
aliases:
  - mlflow-agent-evaluation
  - MAE
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Agent Evaluation

**MLflow Agent Evaluation** is a comprehensive framework within [[MLflow 3]] for measuring, improving, and maintaining the quality of AI agents, LLM-based applications, [[Retrieval Augmented Generation (RAG)|RAG]] systems, and other [[MLflow GenAI Evaluate API|GenAI]] applications. It supports the entire development lifecycle from offline testing through production monitoring, enabling iterative quality optimization. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Overview

Evaluating AI agents and LLMs is more complex than traditional ML model evaluation because these applications involve multiple components, multi-turn conversations, and nuanced quality criteria. Both qualitative and quantitative metrics require specialized evaluation approaches to accurately assess performance. MLflow Agent Evaluation addresses these challenges with a unified framework. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

The evaluation and monitoring components build upon [[MLflow Tracing]], which provides real-time trace logging across development, testing, and production phases. Traces can be evaluated during development using built-in or custom [[LLM Judges and Scorers]], and production monitoring can reuse the same judges and scorers for consistent evaluation throughout the application lifecycle. Domain experts can provide feedback using an integrated [[MLflow Review App|Review App]] for collecting human feedback, producing evaluation data for further iteration. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Key Components

### Evaluation Harness

The [[MLflow GenAI Evaluation Harness|MLflow Evaluation Harness]] evaluates AI agents during development by running traces through built-in or custom judges. This allows developers to assess agent performance against defined quality criteria before deploying to production. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### LLM Judges and Scorers

[[LLM Judges and Scorers]] are AI-powered evaluators that assess agent outputs against specific quality dimensions. These include:

- **Built-in judges** for common criteria such as correctness, safety, and helpfulness
- **Custom judges** created using the make_judge()|Make Judge API for domain-specific evaluation needs
- **Per-category judges** that evaluate metrics like professionalism or creativity for specific use cases

### Production Monitoring

[[Production Quality Monitoring (MLflow GenAI)|Production Monitoring for GenAI]] enables continuous quality assessment of deployed agents using the same judges and scorers used during development. This ensures consistent evaluation standards from testing through production. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Human Feedback Integration

The [[MLflow Review App|Review App]] allows domain experts to provide feedback on agent outputs, producing high-quality evaluation data that can be used to further refine judges and agent behavior. This creates a continuous improvement loop. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Integration with [[mlflow-tracing|MLflow Tracing]]

Traces provide the foundational data for evaluation and monitoring. During development, traces are captured and evaluated against judges. In production, the same trace infrastructure supports real-time monitoring with the same evaluation criteria, enabling consistent quality assessment across all phases. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Migrating from MLflow 2

Agent Evaluation is integrated with managed MLflow 3. The Agent Evaluation SDK methods are available using the `mlflow[databricks]>=3.1` SDK. See Migrate to MLflow 3 from Agent Evaluation for guidance on updating MLflow 2 Agent Evaluation code to use MLflow 3. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related Concepts

- [[A/B Comparison of Agent Configurations]] — Comparing agent variants using custom judges
- [[Custom Judges]] — LLM-based scorers for evaluating agent quality
- [[MLflow Trace-based Evaluation|Trace-Based Evaluation]] — Using execution traces for deeper quality analysis
- Human Feedback Alignment — Improving judge accuracy with expert annotations
- [[MLflow Experiment|MLflow Experiments]] — The organizational unit for MLflow runs and evaluations
- [[Scheduled Scorers (MLflow GenAI)|Scheduled Scorers]] — Production monitoring workflows
- [[Synthetic Evaluation Data Generation|Synthetic Evaluation Generation]] — Creating evaluation datasets

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md
```

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
