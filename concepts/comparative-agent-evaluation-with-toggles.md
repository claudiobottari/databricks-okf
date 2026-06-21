---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c1d038a7dd45c8785fd2ddb43349f6a5f080677d604e9072f4d8627dd1ea847
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - comparative-agent-evaluation-with-toggles
    - CAEWT
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Comparative Agent Evaluation with Toggles
description: A technique using global configuration flags (e.g., RESOLVE_ISSUES) to switch between agent behaviors and compare evaluation results across different agent configurations.
tags:
  - mlflow
  - evaluation
  - testing
  - comparison
timestamp: "2026-06-19T09:27:14.189Z"
---

# Comparative Agent Evaluation with Toggles

**Comparative Agent Evaluation with Toggles** is a technique for assessing how changes to an GenAI agent's behavior affect its quality by running [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) across two or more configurations controlled by a code-level flag (toggle). By switching the toggle, practitioners can perform an [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) while keeping the evaluation dataset and judges constant, isolating the impact of the changed behavior. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Overview

Toggles are commonly used to turn specific agent features on or off — such as whether the agent attempts to resolve a customer issue, uses a particular tool, or follows a different system prompt. The evaluation workflow first collects the judge scores for one toggle value, then flips the toggle and re-evaluates the same dataset. The resulting scores across judges can be compared to determine which configuration better meets the defined quality criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Implementation

### Step 1: Define the toggle

The toggle is typically a global Boolean variable that controls a section of the agent’s logic. A common pattern is to modify the system prompt or the agent’s decision-making based on the toggle’s value. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
# Global toggle to control agent behavior
RESOLVE_ISSUES = False
```

Inside the agent function, the toggle can alter instructions, tool selection, or response generation:

```python
@mlflow.trace
def customer_support_agent(messages):
    system_prompt_postfix = (
        "Do your best to NOT resolve the issue."
        if not RESOLVE_ISSUES
        else ""
    )
    # ... build messages and call LLM
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Step 2: Run evaluation for each toggle value

Use `mlflow.genai.evaluate()` with the same evaluation dataset and set of judges for both toggle settings. The judges can include [input/output judges](/concepts/inputoutput-and-expectation-judges.md) and [Trace-based Judges](/concepts/trace-based-judges.md). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
# Evaluate with toggle OFF (e.g., agent does NOT try to resolve)
RESOLVE_ISSUES = False
result_off = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[issue_resolution_judge, expected_behaviors_judge, tool_call_judge],
)

# Evaluate with toggle ON (agent DOES try to resolve)
RESOLVE_ISSUES = True
result_on = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[issue_resolution_judge, expected_behaviors_judge, tool_call_judge],
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Step 3: Compare scores

Each judge returns structured feedback values (e.g., `fully_resolved`, `partially_resolved`, `needs_follow_up` for an issue‑resolution judge, or `True`/`False` for a tool‑call correctness judge). By comparing the distribution of these values across the two evaluation runs, developers can see which toggle setting produces better outcomes. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- **Control one toggle at a time.** Only change the aspect of behavior under test (e.g., prompt, tool set, model) while keeping all other parameters identical. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Use a representative evaluation dataset.** The test cases should mirror the variety of inputs the agent will see in production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Apply the same judges across all runs.** This ensures score differences reflect agent behavior changes, not evaluation inconsistency. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Log toggle values alongside results.** Record the toggle state and code version to make comparisons reproducible.

## Related Concepts

- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — The broader pattern for comparing agent variants.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used in the evaluation.
- make_judge()|Make Judge API — The `make_judge()` function for defining judges.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework that supports this workflow.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis.
- Align judges with human feedback — Improving judge accuracy with expert annotations.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
