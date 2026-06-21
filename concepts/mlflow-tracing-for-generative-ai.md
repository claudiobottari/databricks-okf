---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33e4f8ee664ccc92080f272d8a7bad657d008c2b63b42edbef8aa6586b293cc1
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-generative-ai
    - MTFGA
    - Generative AI
  citations:
    - file: databricks-autologging-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Tracing for Generative AI
description: An MLflow feature that uses autolog to enable or disable tracing for generative AI model integrations including OpenAI, LangChain, LangGraph, LlamaIndex, and AutoGen.
tags:
  - mlflow
  - generative-ai
  - tracing
  - llm
timestamp: "2026-06-18T11:32:58.554Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) for Generative AI

**MLflow Tracing** is a capability within [MLflow](/concepts/mlflow.md) that captures detailed execution traces from GenAI agent and large language model (LLM) workflows, enabling developers to inspect, debug, and evaluate the step-by-step behavior of their generative AI applications. ^[databricks-autologging-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) records the full execution path of an AI agent, including intermediate reasoning steps, tool invocations, and their results. This provides visibility into how an agent arrives at its responses, which is essential for [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md), [Production Monitoring](/concepts/production-monitoring.md), and quality evaluation with [Custom Judges](/concepts/custom-judges.md). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Enabling [MLflow Tracing](/concepts/mlflow-tracing.md)

[MLflow Tracing](/concepts/mlflow-tracing.md) is enabled through the `autolog` feature within supported model framework integrations. You control whether tracing is active by passing the appropriate parameter to a framework's `autolog()` function. ^[databricks-autologging-databricks-on-aws.md]

### For Supported Frameworks

The following integrations support trace enablement through their `autolog` implementations: ^[databricks-autologging-databricks-on-aws.md]

- OpenAI
- LangChain
- LangGraph
- LlamaIndex
- [AutoGen](/concepts/autogen-auto-tracing.md)

### Example: Enable Tracing for LlamaIndex

To enable tracing when using a LlamaIndex model:

```python
import mlflow

mlflow.llama_index.autolog(log_traces=True)
```

^[databricks-autologging-databricks-on-aws.md]

### Example: Enable Tracing for OpenAI

```python
import mlflow

mlflow.openai.autolog(log_traces=True)
```

^[databricks-autologging-databricks-on-aws.md]

## Autologging Behavior on Different Compute Types

| Compute Type | Tracing Autologging Behavior |
|-------------|-------------------------------|
| Interactive Databricks clusters (not serverless) | Automatically enabled when training models in supported frameworks |
| [Serverless compute](/concepts/serverless-gpu-compute.md) | Not automatically enabled — must explicitly call the framework's `autolog()` with `log_traces=True` |

^[databricks-autologging-databricks-on-aws.md]

## Using Traces in Evaluation

When [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluates an agent, it can collect traces from each agent call and make them available to [Trace-based Judges](/concepts/trace-based-judges.md) for scoring. Trace-based judges analyze the full execution trace to determine if the agent used appropriate tools for the user's request. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Creating a Trace-Based Judge

To create a judge that evaluates trace contents, include `{{ trace }}` in the judge's instructions:

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Trace-based judges can evaluate:

+ Whether tool calls were appropriate for the user's intent
+ The order in which tools were invoked
+ Intermediate reasoning steps and their quality
+ Error handling and recovery in the agent's execution path

## Benefits for Agent Development

Developers use [MLflow Tracing](/concepts/mlflow-tracing.md) to:

+ **Understand agent behavior**: See which tools an agent called and in what sequence, making it easier to identify bugs or suboptimal behavior. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
+ **Compare configurations**: Run the same [Evaluation Dataset](/concepts/evaluation-dataset.md) through two agent configurations (e.g., with and without a RESOLVE_ISSUES flag) and compare the resulting traces. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
+ **Align with human feedback**: As you gather expert annotations on agent outputs, use the traces to fine-tune judging criteria to better reflect human quality assessments. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
+ **Monitor production quality**: Deploy [Trace-based Judges](/concepts/trace-based-judges.md) to continuously evaluate agent quality in production, flagging regressions when tool usage patterns deviate from expected behavior.

## Trace Data and Security

All trace data captured by [MLflow Tracing](/concepts/mlflow-tracing.md) is stored in [MLflow Tracking](/concepts/mlflow-tracking.md) runs and is secured by [MLflow Experiment permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md). Administrators control access to trace data using the same [Unity Catalog](/concepts/unity-catalog.md) permissions that govern other MLflow artifacts. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — The automatic logging system that powers [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for quality assessment
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that can consume trace data
- make_judge()|Make Judge API — API for creating trace-aware judges
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The evaluation framework for generative AI models
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent behaviors using traces
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Continuous quality monitoring with trace analysis
- LlamaIndex — Framework with trace-enabled autologging
- LangChain — Framework with trace-enabled autologging
- OpenAI — Framework with trace-enabled autologging

## Sources

- databricks-autologging-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
