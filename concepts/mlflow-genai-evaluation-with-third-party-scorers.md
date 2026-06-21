---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5255a401fb3be8bc885e8bf25cd99521f4bc5170529da9cc4e48e5c5d8763e9d
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-with-third-party-scorers
    - MGEWTS
  citations:
    - file: arixe-phoenix-scorers-databricks-on-aws.md
title: MLflow GenAI evaluation with third-party scorers
description: The integration pattern for using external evaluation scorers, such as Arize Phoenix, within MLflow's mlflow.genai.evaluate() function by passing them in the scorers list parameter.
tags:
  - mlflow
  - genai-evaluation
  - integration-pattern
timestamp: "2026-06-19T09:03:31.043Z"
---

# MLflow GenAI Evaluation with Third-Party Scorers

**MLflow GenAI evaluation with third-party scorers** enables developers to extend the built-in evaluation capabilities of [MLflow GenAI](/concepts/mlflow-3-for-genai.md) by integrating external scoring libraries and custom evaluators. This approach allows teams to leverage specialized evaluation metrics from the broader AI ecosystem alongside MLflow's native scoring infrastructure.

## Overview

MLflow GenAI provides a flexible evaluation framework through `mlflow.genai.evaluate()`. While the platform includes built-in judges and scorers, it also supports integration with third-party libraries that offer specialized evaluation capabilities. This extensibility is particularly valuable for evaluating LLM outputs and agent behaviors using established frameworks from the open-source community. ^[arixe-phoenix-scorers-databricks-on-aws.md]

## Third-Party Scorer Libraries

### Arize Phoenix Scorers

One example of third-party scorer integration is the Arize Phoenix library, which provides scorers like `Hallucination` and `Relevance` that can be used directly within MLflow evaluation workflows. These scorers are designed to assess LLM output quality for common issues such as factual inaccuracy (hallucination) and contextual appropriateness (relevance). ^[arixe-phoenix-scorers-databricks-on-aws.md]

To use Arize Phoenix scorers, import them from `mlflow.genai.scorers.phoenix`:

```python
from mlflow.genai.scorers.phoenix import Hallucination, Relevance
```

## Setting Up an Evaluation Dataset

When using third-party scorers, the evaluation dataset must provide the fields that the scorers require. Typically, this includes:

- `inputs`: The query or prompt passed to the model
- `outputs`: The model's response to be evaluated
- `expectations`: Reference information (such as context or ground truth) that scorers use for comparison

```python
eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
        "expectations": {
            "context": "MLflow is an ML platform for experiment tracking and model deployment."
        },
    },
]
```

## Running Evaluation with Third-Party Scorers

To run an evaluation that includes third-party scorers, pass the scorer instances in the `scorers` parameter of `mlflow.genai.evaluate()`:

```python
import mlflow

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

Each third-party scorer typically requires a model specification to power its LLM-based judgment. In the example above, the scorers use a Databricks-hosted model endpoint, but the specific model depends on the scorer's requirements and available resources. ^[arixe-phoenix-scorers-databricks-on-aws.md]

## How Third-Party Scorers Work

Third-party scorers integrate with MLflow's evaluation framework by implementing the same interface as built-in scorers. They receive individual evaluation records (containing inputs, outputs, and expectations) and return structured scores. This design allows them to be used interchangeably with [Custom Judges](/concepts/custom-judges.md) created via `make_judge()` or built-in MLflow scorers. ^[arixe-phoenix-scorers-databricks-on-aws.md]

## Common Use Cases

| Use Case | Example Scorer | Purpose |
|----------|----------------|---------|
| Factual accuracy | `Hallucination` | Detect unsupported or fabricated information |
| Context relevance | `Relevance` | Measure how well outputs relate to provided context |
| Custom criteria | Custom third-party scorers | Evaluate domain-specific quality dimensions |

## Combining Scorers

You can combine third-party scorers with built-in or custom scorers in a single evaluation run:

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
        my_custom_judge,
    ],
)
```

This flexibility allows comprehensive evaluation pipelines that assess multiple quality dimensions simultaneously. ^[arixe-phoenix-scorers-databricks-on-aws.md]

## Best Practices

- **Understand scorer requirements**: Each third-party scorer expects specific fields in the evaluation dataset (e.g., `context` for relevance checks). Ensure your data includes the required fields.
- **Specify appropriate models**: Third-party LLM-based scorers require a model endpoint. Choose a model that balances evaluation quality, latency, and cost for your use case.
- **Align scorer criteria with your goals**: Select scorers that measure dimensions relevant to your application's quality standards.
- **Combine with custom judges**: Use third-party scorers for established metrics (like hallucination) alongside [Custom Judges](/concepts/custom-judges.md) for domain-specific criteria.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework for GenAI applications
- [Custom Judges](/concepts/custom-judges.md) — Building your own evaluation criteria with `make_judge()`
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous monitoring
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants using evaluation
- Arize Phoenix — Open-source LLM observability library providing third-party scorers

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. arixe-phoenix-scorers-databricks-on-aws.md
