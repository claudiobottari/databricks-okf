---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 299c7df2c81866f60fa23ff255860798ee739fe1928700c531bc45fac9028100
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ab-comparison-of-agent-configurations
    - ACOAC
    - A/B comparisons of agent configurations
    - comparison operators
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: A/B Comparison of Agent Configurations
description: Using custom judges to compare different agent configurations (e.g., toggling a behavior flag) by running `mlflow.genai.evaluate()` separately on each variant and comparing judge ratings across the same evaluation dataset.
tags:
  - mlflow
  - genai
  - evaluation
  - experimentation
timestamp: "2026-06-18T11:13:02.271Z"
---

# A/B Comparison of Agent Configurations

**A/B Comparison of Agent Configurations** refers to the practice of evaluating two or more versions of a GenAI agent side-by-side to compare their performance against defined quality criteria. This approach allows developers to systematically assess how changes to agent behavior — such as system prompt modifications, tool selection, or model choice — affect the quality of responses.

## Overview

A/B comparison is central to iterative agent development in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). By running the same evaluation dataset against multiple agent configurations and scoring the outputs with consistent [judges](/concepts/llm-judges.md), teams can quantify the impact of changes before promoting a configuration to production.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Running an A/B Comparison

### Defining Agent Configurations

Agent configurations are typically controlled through code-level variables that toggle specific behaviors. For example, a global flag like `RESOLVE_ISSUES` can switch between a "good" agent that attempts to resolve customer issues and a "bad" agent that does not.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
# Configuration A: Agent does NOT try to resolve issues
RESOLVE_ISSUES = False

# Configuration B: Agent DOES try to resolve issues
RESOLVE_ISSUES = True
```

### Creating a Shared Evaluation Dataset

Both configurations should be evaluated against the same [Evaluation Dataset](/concepts/evaluation-dataset.md) to ensure fair comparison. Each entry in the dataset contains `inputs` (the conversation history passed to the agent) and optional `expectations` that judges can reference.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Applying Consistent Judges

Use the same set of [Custom Judges](/concepts/custom-judges.md) for both configurations. Judges are LLM-based scorers that evaluate outputs against specific quality criteria. In an A/B comparison, deploying the same judges across both runs ensures that differences in scores reflect changes in agent behavior rather than inconsistencies in the evaluation criteria.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
# Evaluate Configuration A (unresolved)
result_unresolved = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)

# Evaluate Configuration B (resolved)
result_resolved = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)
```

## Types of Judges for A/B Comparison

### Input/Output Judges

These judges evaluate the agent's behavior by analyzing conversation history (inputs) and agent responses (outputs). Common criteria include issue resolution status and adherence to expected behaviors.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Trace-Based Judges

Trace-based judges analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. These judges can validate whether appropriate tools were called for a given user request. To create a trace-based judge, include `{{ trace }}` in the judge's instructions.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    # Trace-based judges require a model specification
    model="databricks:/databricks-gpt-5-mini",
)
```

## Interpreting Results

Each judge returns structured feedback values that can be compared across configurations:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

| Judge | Feedback Values | Purpose |
|-------|-----------------|---------|
| `issue_resolution` | `fully_resolved`, `partially_resolved`, `needs_follow_up` | Assesses outcome quality |
| `expected_behaviors` | `meets_expectations`, `partially_meets`, `does_not_meet` | Checks specific behaviors |
| `tool_call_correctness` | `true`, `false` | Validates tool usage |

By comparing score distributions across the two runs, developers can determine which configuration better satisfies the defined quality criteria.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- **Control one variable at a time.** Change only the agent behavior being tested (e.g., system prompt, model, or tool set) while keeping all other factors constant.
- **Use a representative evaluation dataset.** The test cases should reflect the range of real-world inputs the agent will encounter in production.
- **Align judges with human feedback.** As you gather expert annotations on agent outputs, fine-tune the judges to better reflect human quality assessments. See Align judges with human feedback.
- **Document configurations.** Record the exact parameters, prompts, and code versions used for each configuration to ensure reproducibility.

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate agent quality
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis
- Human Feedback Alignment — Improving judge accuracy with expert annotations

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
