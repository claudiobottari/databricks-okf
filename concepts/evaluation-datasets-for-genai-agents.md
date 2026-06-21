---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac3c1574b60cc33f212bf9274302a10becb9d1a5ccb3f7ad600148369df1c3d0
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-datasets-for-genai-agents
    - EDFGA
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: a-b-comparison-of-agent-configurations.md
title: Evaluation Datasets for GenAI Agents
description: Structured test datasets containing inputs (conversation messages) and optional expectations fields used to evaluate GenAI agents with custom judges.
tags:
  - mlflow
  - evaluation
  - datasets
  - testing
timestamp: "2026-06-19T09:26:57.491Z"
---

# Evaluation Datasets for GenAI Agents

**Evaluation Datasets for GenAI Agents** are structured collections of test cases used to assess the quality, safety, and correctness of generative AI agents through offline evaluation. They serve as the input ground truth for running [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md), enabling developers to compare different agent configurations, detect regressions, and validate improvements before deployment.

## Structure of an Evaluation Dataset

Each entry in an evaluation dataset is a dictionary that contains at least one field and can optionally include a second field: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

- **`inputs`** (required) – The conversation history or input prompt passed to the agent during inference. Typically structured as a list of message dictionaries with `role` and `content` keys, for example:
  ```python
  {"role": "user", "content": "How much does a microwave cost?"}
  ```
  The entire `inputs` object is passed to the agent’s predict function by `mlflow.genai.evaluate()`.

- **`expectations`** (optional) – A dictionary of expected behaviors or correctness criteria that judges can reference when scoring agent outputs. These expectations are not exposed to the agent but are provided to the judge, allowing it to compare the response against predefined desired outcomes. For example:
  ```python
  {"should_provide_pricing": True, "should_offer_alternatives": True}
  ```

Both fields are arbitrary JSON-serialisable objects; the schema is not fixed beyond these two top-level keys.

## Creating an Evaluation Dataset

Datasets are typically created as a list of such dictionaries, representing a variety of scenarios the agent is expected to handle. A representative dataset should: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, a-b-comparison-of-agent-configurations.md]

- Cover the range of real-world inputs the agent will encounter in production.
- Include edge cases, adversarial inputs, and common failure modes.
- Be identical across A/B comparisons to ensure fair evaluation of different agent configurations.

## Using the Dataset in Evaluation

The dataset is passed to the `data` parameter of `mlflow.genai.evaluate()`. Each entry’s `inputs` is fed to the agent, and the optional `expectations` are made available to judges that reference them via the `{{ expectations }}` template variable. The evaluation returns scores from each judge for every entry in the dataset. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[issue_resolution_judge, expected_behaviors_judge],
)
```

## Best Practices

- **Use a shared dataset for comparisons.** When comparing two agent configurations (e.g., system prompt variants), always evaluate against the same dataset. This isolates the effect of the changed variable. ^[a-b-comparison-of-agent-configurations.md]
- **Keep the dataset versioned.** Store evaluation datasets alongside model code in a repository to reproduce results and track dataset drift over time.
- **Synthesise diverse cases.** Consider generating synthetic conversations that reflect real user interactions; see [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md).
- **Align expectations with judges.** As you gather human expert annotations on agent outputs, update the expectations in the evaluation dataset to better mirror human quality assessments. See Align Judges with Human Feedback.

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that use the dataset’s expectations and traces to evaluate agent outputs.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Running the same dataset against multiple agent versions and comparing judge scores.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The offline evaluation framework that consumes evaluation datasets.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Judges that analyse full agent execution traces, benefiting from trace information included in the evaluation dataset.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges that use similar dataset patterns for continuous quality monitoring.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- a-b-comparison-of-agent-configurations.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
2. a-b-comparison-of-agent-configurations.md
