---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c774ceb0950acf3259d3260df49ab76f72a0772a4b3bb966948d70722be84b12
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-evaluation-dataset-design
    - GEDD
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: GenAI Evaluation Dataset Design
description: Practice of designing structured evaluation datasets with diverse input templates to systematically test GenAI application behavior across different scenarios.
tags:
  - evaluation
  - datasets
  - genai
timestamp: "2026-06-19T13:50:11.324Z"
---

# GenAI Evaluation Dataset Design

**GenAI Evaluation Dataset Design** refers to the process and best practices for constructing the data inputs used to evaluate a GenAI application with MLflow. A well-designed evaluation dataset is the foundation for measuring application quality, safety, and adherence to guidelines.

## Purpose

The evaluation dataset provides the test cases that are passed to a prediction function and scored by judges (LLM judges)|judges. Each entry in the dataset represents a unique input scenario that the application must handle. By running the same dataset across different versions of an application — for example, after modifying a system prompt — developers can compare results side by side to see whether quality has improved. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Dataset Structure

An evaluation dataset is a list of dictionaries. Each dictionary contains the inputs for a single evaluation case. The `inputs` key holds the parameters that will be passed to the prediction function. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The following example shows a dataset for a sentence‑completion game (Mad Libs style). Each case provides a `template` string containing blanks that the application must fill in:

```python
eval_data = [
    {
        "inputs": {
            "template": "Yesterday, ____ (person) brought a ____ (item) and used it to ____ (verb) a ____ (object)"
        }
    },
    {
        "inputs": {
            "template": "I wanted to ____ (verb) but ____ (person) told me to ____ (verb) instead"
        }
    },
    {
        "inputs": {
            "template": "The ____ (adjective) ____ (animal) likes to ____ (verb) in the ____ (place)"
        }
    },
    {
        "inputs": {
            "template": "My favorite ____ (food) is made with ____ (ingredient) and ____ (ingredient)"
        }
    },
    {
        "inputs": {
            "template": "When I grow up, I want to be a ____ (job) who can ____ (verb) all day"
        }
    },
    {
        "inputs": {
            "template": "When two ____ (animals) love each other, they ____ (verb) under the ____ (place)"
        }
    },
    {
        "inputs": {
            "template": "The monster wanted to ____ (verb) all the ____ (plural noun) with its ____ (body part)"
        }
    },
]
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The dataset covers a variety of sentence structures and parts of speech to stress‑test the application’s creativity and adherence to the template. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Key Considerations

- **Coverage**: Include a diverse set of inputs that represent the range of real‑world scenarios the application will encounter. In the example above, templates differ in structure (e.g., past tense, future tense, plural nouns) to avoid over‑fitting the model to a single pattern. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Clarity**: Each input key (e.g., `template`) should match the parameter name expected by the prediction function. The function defined in the demo accepts a `template` argument, so the dataset uses that key. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Simplicity**: For initial evaluations, a small dataset (e.g., 5–10 entries) is sufficient to get meaningful feedback on prompt changes. The demo uses seven entries. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Passing the Dataset to Evaluation

The dataset is passed to `mlflow.genai.evaluate()` via the `data` parameter. The evaluation harness calls the provided `predict_fn` once per entry, passing the `inputs` dictionary as keyword arguments. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=scorers,
)
```

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The overall framework for evaluating GenAI applications.
- [Judges and Scorers](/concepts/llm-judges-and-scorers.md) – The components that score each evaluation output against defined criteria.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using the same dataset across different application versions for side‑by‑side comparison.
- [Guidelines Scorer](/concepts/guidelines-scorer.md) – A scorer that checks outputs against natural‑language rules.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
