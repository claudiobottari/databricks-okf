---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8261cdd03524ad2eea9b86c46996662f280146086f3296f55295513ae01e2c8f
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-managed-evaluation
    - M3ME
    - mlflow-3-agent-evaluation-sdk
    - M3AES
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: MLflow 3 Managed Evaluation
description: Managed Agent Evaluation integrated with MLflow 3 using the mlflow[databricks]>=3.1 SDK, superseding MLflow 2 Agent Evaluation.
tags:
  - mlflow
  - migration
  - sdk
timestamp: "2026-06-18T12:12:21.028Z"
---

Here is the wiki page for "MLflow 3 Managed Evaluation".

---

**MLflow 3 Managed Evaluation** is the component of [MLflow 3](/concepts/mlflow-3.md) that provides integrated, lifecycle-wide capabilities for measuring, improving, and maintaining the quality of [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications, including AI agents, LLMs, RAG systems, and other large language model applications. It is designed to handle the unique complexity of evaluating these systems, which involve multi-component architectures, multi-turn conversations, and nuanced quality criteria requiring both qualitative and quantitative assessment. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## The Evaluation and Monitoring Workflow

Managed Evaluation in MLflow 3 is built to support an iterative optimization workflow, from development through production. It is tightly integrated with [MLflow Tracing](/concepts/mlflow-tracing.md), which provides real-time trace logging during development, testing, and production. These traces serve as the foundation for evaluation.

Traces captured during development can be assessed using [LLM Judges](/concepts/llm-judges.md) and [[scorers]]—both built-in and custom—via the [Evaluation Harness](/concepts/evaluation-harness.md). This allows for rapid, offline iteration during the development phase. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

Once an application is deployed, [Production Monitoring](/concepts/production-monitoring.md) can reuse the same set of judges and scorers. This ensures a consistent evaluation standard across the entire application lifecycle, from development to live production.

To further refine the evaluation, domain experts can provide feedback on live agent behavior using the integrated [Review App](/concepts/mlflow-review-app.md) for human feedback collection. The outputs from this process can then be used as evaluation data for subsequent development cycles. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

The diagram below illustrates this high-level iterative workflow:

![Overview diagram of MLflow 3 evaluation and monitoring](https://docs.databricks.com/aws/en/assets/images/flowchart-00c729ac75207b58d9c2243583a30d5a.png) ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Key Capabilities

- **Iterative Optimization:** Facilitates a continuous cycle of development, testing, monitoring, and feedback collection to iteratively improve GenAI application quality. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Consistent Evaluation:** Ensures that the same evaluation criteria (judges, scorers) are applied during development, testing, and production, eliminating inconsistencies between stages. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Trace-Based Evaluation:** Leverages detailed execution traces to analyze complex agent behavior, including tool calls and reasoning steps. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]
- **Human-in-the-Loop:** Integrated human feedback capabilities allow domain experts to provide direct input on agent performance, which can be used to fine-tune evaluation criteria or create ground-truth data. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Integration with MLflow 3

Agent Evaluation is a core part of managed MLflow 3. The SDK methods for Agent Evaluation are available using the `mlflow[databricks]>=3.1` SDK. Users must migrate from MLflow 2 Agent Evaluation to update their existing codebase to use the new MLflow 3 features. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [LLM Judges](/concepts/llm-judges.md)
- [Evaluation Harness](/concepts/evaluation-harness.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md)
- [MLflow 3](/concepts/mlflow-3.md)
- [MLflow 2](/concepts/mlflow.md)
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- [[Scorers]]
- [Review App](/concepts/mlflow-review-app.md)

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
