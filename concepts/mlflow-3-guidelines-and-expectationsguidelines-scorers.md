---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 923a121fd7255cf9ae2be5bc1c282d74697b494314e63c895cd59ee2f0af0541
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-guidelines-and-expectationsguidelines-scorers
    - ExpectationsGuidelines Scorers and MLflow 3 Guidelines
    - M3GAES
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: MLflow 3 Guidelines and ExpectationsGuidelines Scorers
description: Global guidelines from MLflow 2.x are replaced by explicit Guidelines() scorer instances, and per-example guidelines use the ExpectationsGuidelines scorer with expectations.guidelines fields in the evaluation data.
tags:
  - mlflow
  - scorers
  - guidelines
timestamp: "2026-06-19T19:35:10.877Z"
---

# MLflow 3 Guidelines and ExpectationsGuidelines Scorers

**Guidelines** and **ExpectationsGuidelines** are predefined scorers in MLflow 3 that evaluate whether an agent's response adheres to a set of specified rules or criteria. They are part of the `mlflow.genai.scorers` module and replace the `guideline_adherence` judge from MLflow 2.x Agent Evaluation. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Overview

In MLflow 3, evaluating guideline adherence is handled through explicit scorer objects rather than the automatic judge selection behavior of MLflow 2.x. The `Guidelines` scorer checks responses against a fixed set of rules defined at evaluation time, while the `ExpectationsGuidelines` scorer evaluates responses against per-example guidelines provided in the evaluation data. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Guidelines Scorer

The `Guidelines` scorer evaluates whether a response meets a set of predefined criteria defined at the evaluation level. It replaces the `global_guidelines` configuration from MLflow 2.x and the `guideline_adherence` judge. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Usage

Import the `Guidelines` scorer and pass it to `mlflow.genai.evaluate()`:

```python
from mlflow.genai.scorers import Guidelines

# Define guidelines as a dictionary or list
guidelines = {
    "clarity": ["Response must be clear and concise"],
    "accuracy": "Response must be factually accurate",
}

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=my_agent,
    scorers=[
        Guidelines(name="clarity", guidelines=guidelines["clarity"]),
        Guidelines(name="accuracy", guidelines=guidelines["accuracy"]),
    ]
)
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

Each `Guidelines` instance requires:
- **name**: A string identifier for the guideline (e.g., `"clarity"`)
- **guidelines**: A string or list of strings describing the criteria to evaluate

### Migration from global_guidelines

In MLflow 2.x, guidelines were configured via `evaluator_config["databricks-agent"]["global_guidelines"]`. In MLflow 3, each guideline must be explicitly converted to a `Guidelines()` scorer instance. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

**MLflow 2.x:**
```python
global_guidelines = {
    "tone": ["Response must be professional and courteous"],
    "format": ["Response must use bullet points for lists"]
}
```

**MLflow 3.x:**
```python
scorers=[
    Guidelines(name="tone", guidelines="Response must be professional and courteous"),
    Guidelines(name="format", guidelines="Response must use bullet points for lists"),
]
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## ExpectationsGuidelines Scorer

The `ExpectationsGuidelines` scorer evaluates responses against per-example guidelines provided in the evaluation dataset. This is useful when different examples in your evaluation set have different criteria — for example, requiring that certain topics are covered in specific responses, or that the response follows a particular style. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Data Format

Each evaluation data entry must include `expectations.guidelines` as a list of guideline strings:

```python
eval_data = [
    {
        "inputs": {"input": "What is MLflow?"},
        "outputs": {
            "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."
        },
        "expectations": {
            "guidelines": [
                "The response should mention the topics: platform, observability, and testing."
            ]
        }
    }
]
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Usage

```python
from mlflow.genai.scorers import ExpectationsGuidelines

expectations_guideline = ExpectationsGuidelines()

results = mlflow.genai.evaluate(
    data=eval_data,  # Each row must have expectations.guidelines
    predict_fn=my_agent,
    scorers=[expectations_guideline]
)
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### When to Use ExpectationsGuidelines vs. Correctness

If you need to check for specific factual content (e.g., "MLflow is open-source"), use the `Correctness` scorer with an `expected_facts` field instead of guidelines. Use `ExpectationsGuidelines` when the criteria are about style, coverage, or adherence to rules that vary per example. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Custom Scorer with meets_guidelines Judge

For advanced use cases requiring additional context (such as retrieved documents), you can call the `meets_guidelines` judge directly within a custom scorer:

```python
from mlflow.genai.scorers import scorer
from mlflow.genai import judges

@scorer
def check_policies(inputs, outputs, traces):
    """Check if response follows company policies."""
    retrieved_context = traces.data.spans[0].attributes.get("retrieved_context", [])
    context_text = '\n'.join([c['content'] for c in retrieved_context])
    return judges.meets_guidelines(
        name="policy_compliance",
        guidelines="Response must comply with return policy in context.",
        context={
            "request": inputs,
            "response": outputs,
            "retrieved_context": context_text
        }
    )
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 Scorers](/concepts/mlflow-scorers.md) — Overview of all predefined and custom scorers
- [MLflow 3 Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework for GenAI applications
- MLflow 3 Agents and Tracing — Tracing infrastructure used by scorers
- [MLflow 3 LLM Judges](/concepts/mlflow-llm-judges.md) — The underlying judge functions wrapped by predefined scorers
- [Correctness Scorer](/concepts/correctness-scorer.md) — A predefined scorer for factual accuracy evaluation

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
