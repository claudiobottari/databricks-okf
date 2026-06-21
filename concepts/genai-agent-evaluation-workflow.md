---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f174ba7b2aa294f914f8ef24217cd29e959816384bdc82fcc332160a52846373
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-agent-evaluation-workflow
    - GAEW
    - Agent Evaluation (MLflow 2.x)
    - GenAI agent evaluation
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: GenAI Agent Evaluation Workflow
description: End-to-end process of creating an agent, defining custom judges, building a test dataset, and running evaluations to compare agent configurations
tags:
  - workflow
  - evaluation
  - genai
timestamp: "2026-06-19T14:29:26.065Z"
---

# GenAI Agent Evaluation Workflow

**GenAI Agent Evaluation Workflow** refers to the process of systematically assessing the quality and behavior of generative AI agents using LLM-based scorers (judges) against predefined criteria. This workflow enables developers to evaluate agent performance offline before deployment and monitor quality continuously in production.

## Overview

The evaluation workflow centers around using custom judges — LLM-based scorers that evaluate agent responses against specific quality criteria. These judges can analyze different aspects of agent behavior, including conversation outcomes, adherence to expected behaviors, and tool usage correctness. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Key Components

### Evaluation Dataset

The evaluation consists of test cases that are passed to the agent during evaluation. Each entry contains `inputs` (typically conversation history) and optional `expectations` that judges can reference for correctness checking. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Custom Judges

Custom judges are created using `make_judge()` and evaluate agent outputs against specific criteria. There are two primary types of judges: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

- **Input/Output Judges**: Analyze conversation history (inputs) and agent responses (outputs) to evaluate outcomes such as issue resolution status or behavioral adherence.
- **Trace-Based Judges**: Analyze the full execution trace of an agent call, including tool invocations and intermediate reasoning steps. These judges include `{{ trace }}` in their instructions and require a model specification.

### Agent Configuration

Agent behavior is typically controlled through code-level variables that toggle specific behaviors. This allows for comparing different configurations side-by-side using the same evaluation dataset and judges. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Evaluation Process

### 1. Define Custom Judges

Create judges that evaluate different criteria for your use case. Each judge returns structured feedback values that quantify agent performance. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
from mlflow.genai.judges import make_judge
from typing import Literal

issue_resolution_judge = make_judge(
    name="issue_resolution",
    instructions=(
        "Evaluate if the customer's issue was resolved in the conversation.\n\n"
        "User's messages: {{ inputs }}\n"
        "Agent's responses: {{ outputs }}"
    ),
    feedback_value_type=Literal["fully_resolved", "partially_resolved", "needs_follow_up"],
)
```

### 2. Prepare the Evaluation Dataset

Build a dataset of representative test cases that reflect the range of real-world inputs the agent will encounter in production. Each test case includes inputs and optional expectations. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### 3. Run Evaluation

Use `mlflow.genai.evaluate()` to run the agent against the dataset with the defined judges. Multiple judges can be used together to evaluate different aspects of agent behavior. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=agent_function,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)
```

### 4. Compare Configurations

Run the same evaluation dataset against multiple agent configurations using consistent judges. By comparing score distributions across runs, developers can quantify the impact of changes to system prompts, model selection, or tool sets before promoting a configuration to production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Feedback Values

Each judge returns structured feedback values that can be compared across configurations: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

| Judge Type | Example Feedback Values | Purpose |
|------------|------------------------|---------|
| Issue Resolution | `fully_resolved`, `partially_resolved`, `needs_follow_up` | Assesses outcome quality |
| Expected Behaviors | `meets_expectations`, `partially_meets`, `does_not_meet` | Checks specific behaviors |
| Tool Call Correctness | `true`, `false` | Validates tool usage |

## Best Practices

- **Control one variable at a time.** Change only the agent behavior being tested (e.g., system prompt, model, or tool set) while keeping all other factors constant. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Use a representative evaluation dataset.** Test cases should reflect the range of real-world inputs the agent will encounter. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Align judges with human feedback.** As you gather expert annotations on agent outputs, fine-tune the judges to better reflect human quality assessments. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Document configurations.** Record the exact parameters, prompts, and code versions used for each configuration to ensure reproducibility. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Production Monitoring

Custom judges can be deployed for continuous quality monitoring in production. This allows teams to track agent performance over time and detect regressions as agent configurations or underlying models change. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate agent quality
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Side-by-side comparison using consistent judges
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- Align Judges with Human Feedback — Improving judge accuracy with expert annotations
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
