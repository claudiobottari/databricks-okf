---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a3ee43eba17d87d178d3b7035c4827150f71f5f94456dcb980ba635af5c14a5
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judge-metrics-with-make_judge
    - CJMWM
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
    - file: A/B Comparison of Agent Configurations
title: Custom Judge Metrics with make_judge
description: Creating domain-specific evaluation criteria using the make_judge API to assess LLM outputs against custom requirements like sentence count compliance.
tags:
  - evaluation
  - metrics
  - llm-judges
timestamp: "2026-06-18T12:11:48.663Z"
---

# Custom Judge Metrics with make_judge

**Custom Judge Metrics with make_judge** refers to the use of the `mlflow.genai.make_judge()` function to create LLM-based scorers that evaluate agent or model outputs against specific quality criteria. These judges are a central component of [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) and enable fine-grained, automated quality assessment of GenAI agents.

## Overview

The `make_judge` function allows you to define a custom judge — an LLM that scores outputs based on instructions you provide. Unlike built-in scorers (such as `Correctness`), custom judges let you target domain-specific behaviors like sentence length compliance, tool call correctness, or issue resolution status.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

Judges are passed to `mlflow.genai.evaluate()` via the `scorers` parameter, alongside any predefined scorers. When evaluation runs, the judge examines the input, output, and optionally the full execution trace, then returns a structured feedback value.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Creating a Custom Judge

A custom judge is created with `make_judge()` and requires three arguments: a `name`, `instructions`, and a `feedback_value_type`. Optionally, you can specify which [LLM endpoint](/concepts/model-serving-endpoint.md) the judge should use via the `model` parameter. If omitted, MLflow uses a default model.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Basic Syntax

```python
from mlflow.genai import make_judge
from typing import Literal

sentence_count_judge = make_judge(
    name="sentence_count_compliance",
    instructions=(
        "Evaluate if this summary follows the 2-sentence requirement.\n"
        "Summary: {{ outputs }}\n"
        "Count the sentences carefully and determine if the summary has exactly 2 sentences."
    ),
    feedback_value_type=Literal["correct", "incorrect"],
)
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The `{{ outputs }}` placeholder is automatically replaced with the agent's response during evaluation. For judges that analyze both inputs and outputs, you can also use `{{ inputs }}` and, for trace-based judges, `{{ trace }}`.

### Feedback Value Types

The `feedback_value_type` defines the set of possible scores the judge can return. Common types include:^[evaluate-and-compare-prompt-versions-databricks-on-aws.md, A/B Comparison of Agent Configurations]

| Type | Example Values | Use Case |
|------|---------------|----------|
| `Literal["correct", "incorrect"]` | `"correct"`, `"incorrect"` | Binary correctness checks |
| `Literal["fully_resolved","partially_resolved","needs_follow_up"]` | Ordinal assessment of resolution quality |
| `bool` | `True`, `False` | Simple boolean evaluation (e.g., “was the right tool called?”) |

### Specifying the Judge Model

By default, the judge uses the same model as the evaluation run. To use a different model, set the `model` parameter:

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

^[A/B Comparison of Agent Configurations]

## Types of Judges

### Input/Output Judges

The default judge type evaluates the agent’s behavior by inspecting the conversation history (inputs) and the agent’s final response (outputs). Instructions can reference `{{ inputs }}` and `{{ outputs }}`. These judges are suitable for assessing factual coverage, style adherence, or outcome quality.^[A/B Comparison of Agent Configurations]

### Trace-Based Judges

A trace-based judge analyzes the full execution [trace](/concepts/traces.md) of an agent call, including tool invocations, intermediate reasoning steps, and their results. This enables validation of tool usage, chain-of-thought correctness, and internal decision-making. To create a trace-based judge, include `{{ trace }}` in the judge’s instructions. The `model` parameter must be specified explicitly when using `{{ trace }}`.^[A/B Comparison of Agent Configurations]

```python
trace_judge = make_judge(
    name="tool_usage_analysis",
    instructions=(
        "Given the execution trace in {{ trace }}, evaluate whether the agent "
        "selected the correct tools and used them appropriately."
    ),
    feedback_value_type=Literal["good", "needs_improvement", "poor"],
    model="databricks:/databricks-gpt-5-mini",
)
```

## Integrating with Evaluation

Custom judges are passed to `mlflow.genai.evaluate()` as part of the `scorers` list. MLflow automatically calls each judge on every row of the evaluation dataset and aggregates the results into metrics.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    predictions=predictions_fn,
    scorers=[
        sentence_count_judge,
        Correctness(),
        # Additional judges...
    ],
)
```

The aggregated metric for a judge is named `<judge_name>/mean` (e.g., `sentence_count_compliance/mean`). You can retrieve these from the `metrics` dictionary of the evaluation result.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Using Judges for A/B Comparison

A key use case for custom judges is [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). By applying the same set of judges to two or more agent variants evaluated against the same dataset, you obtain directly comparable scores. Differences in judge ratings then reflect changes in agent behavior rather than inconsistencies in evaluation criteria.^[A/B Comparison of Agent Configurations]

For example, toggling a behavior flag (such as `RESOLVE_ISSUES`) and evaluating both configurations with identical judges reveals which variant better meets quality goals. See [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) for a full workflow.

## Best Practices

- **Start simple.** Begin with a basic judge instruction and refine it based on results.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Align judges with human feedback.** As you gather expert annotations, adjust judge instructions to better mirror human quality assessments.^[A/B Comparison of Agent Configurations]
- **Use consistent judges across comparisons.** Always reuse the same judges when comparing different configurations or prompt versions to ensure fairness.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Test edge cases.** Include challenging examples in your evaluation dataset to stress-test the judge.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Document judge instructions.** Keep a record of judge definitions so that evaluations remain reproducible.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using judges to compare agent variants
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Deeper analysis using execution traces
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) — Built-in scorers like `Correctness`
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- LLM Endpoint — The model serving endpoint used by judges

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md
- A/B Comparison of Agent Configurations (page derived from create-a-custom-judge-using-make_judge-databricks-on-aws.md)

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
2. A/B Comparison of Agent Configurations
