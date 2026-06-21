---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc043255443227c7fc1b1328330d7ca664deaefc06359036b0f89ea4665549ab
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-for-genai-agents
    - EDFGA
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Evaluation Dataset for GenAI Agents
description: Dataset structure for evaluation containing inputs (conversation messages), optional expectations, and test cases for scoring GenAI agent responses
tags:
  - testing
  - dataset
  - genai
  - evaluation
timestamp: "2026-06-18T14:46:45.051Z"
---

Here is the wiki page for "Evaluation Dataset for GenAI Agents", written based solely on the provided source material.

---

## Evaluation Dataset for GenAI Agents

An **evaluation dataset** (or eval dataset) is a structured collection of test cases used to measure the performance of a GenAI agent against defined quality criteria. It serves as the shared input when running an [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) or when assessing a single agent’s behavior with [Custom Judges](/concepts/custom-judges.md) and [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md).^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Structure

Each entry in an evaluation dataset is a dictionary that contains the following fields:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | dict | The conversation history (or other input) that is passed to the agent by `mlflow.genai.evaluate()`. |
| `expectations` | dict (optional) | A set of expected behaviors or properties that judges can reference to perform a correctness check. |

The `inputs` dictionary typically includes a `messages` list that contains the full conversation history—user messages, assistant responses, and any additional context—that the agent will process. Each entry in the `messages` list has a `role` (e.g., `"user"`, `"assistant"`) and a `content` string.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The `expectations` dictionary contains boolean or descriptive flags (e.g., `should_provide_pricing: True`, `should_ask_for_receipt: False`) that judges can use to compare the agent’s output against pre-defined correctness criteria. These expectations are optional; when omitted, the judge evaluates the agent’s output purely on its own merits.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example

The following is a sample evaluation dataset entry from the Custom Judges (make_judge)|Create a custom judge using make_judge() tutorial:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"},
            ],
        },
        "expectations": {
            "should_provide_pricing": True,
            "should_offer_alternatives": True,
        },
    },
    {
        "inputs": {
            "messages": [
                {
                    "role": "user",
                    "content": "Can I return the microwave I bought 2 months ago?",
                },
            ],
        },
        "expectations": {
            "should_mention_return_policy": True,
            "should_ask_for_receipt": False,
        },
    },
]
```

### Usage

An evaluation dataset is used with `mlflow.genai.evaluate()`. The function accepts the dataset as the `data` parameter and a `predict_fn` (the agent being evaluated). One or more [[scorers]] (judges) are provided to assess the agent’s outputs against the defined criteria. The same dataset can be used across multiple runs to compare different agent configurations, as shown in the [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) workflow.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)
```

### Best Practices

- **Use a representative evaluation dataset.** The test cases should reflect the range of real-world inputs the agent will encounter in production. Include both common and edge-case scenarios.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Include expectations when possible.** Providing expectations allows judges to perform a correctness check, which can reveal whether the agent’s behavior aligns with desired outcomes.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Keep the dataset consistent across comparisons.** To reliably compare two agent configurations, use the same evaluation dataset for both runs. Any difference in scores will then reflect changes in agent behavior rather than inconsistencies in the evaluation data.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Update the dataset as you gather feedback.** As you collect expert annotations on agent outputs, you can refine the evaluation dataset to better reflect real-world usage patterns. See Align judges with human feedback.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Related Concepts

- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using the same evaluation dataset to compare two agent variants.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that evaluate agent outputs against specific criteria.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges and evaluation datasets for continuous quality monitoring.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis.

### Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
