---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee889dc9b43428d1faf5d813eb528c8675f432101f037b0586a0c058077837bd
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expectations-based-evaluation
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Expectations-Based Evaluation
description: A pattern for offline evaluation where ground-truth 'expectations' are supplied alongside inputs and passed to custom scorers for comparison.
tags:
  - mlflow
  - evaluation
  - expectations
  - offline
timestamp: "2026-06-19T09:13:44.020Z"
---

# Expectations-Based Evaluation

**Expectations-Based Evaluation** is a pattern in [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) where ground-truth labels or expected outcomes are provided alongside the evaluation data to assess the quality of an AI agent’s responses. By comparing the agent’s outputs against these predefined expectations, developers can measure exact matches, keyword presence, or other custom criteria in offline evaluation runs.^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

When running `mlflow.genai.evaluate()`, expectations can be supplied as part of the evaluation dataset. This is especially valuable for offline evaluation, where ground truth is available to benchmark model performance. In contrast, [Production Monitoring](/concepts/production-monitoring.md) typically lacks expectations because it evaluates live traffic without ground truth. If the same scorer is used for both offline and online evaluation, it should be designed to handle expectations gracefully — for example, by checking whether the `expectations` field exists before attempting to use it.^[code-based-scorer-examples-databricks-on-aws.md]

## Providing Expectations

Expectations can be included in the `data` argument of `mlflow.genai.evaluate()` in two ways:

- **`expectations` column or field**: When the data argument is a list of dictionaries or a Pandas DataFrame, each row can contain an `expectations` key. The value associated with this key is passed directly to your custom scorer.^[code-based-scorer-examples-databricks-on-aws.md]
- **`trace` column or field**: If the data argument is the DataFrame returned by `mlflow.search_traces()`, it includes a `trace` field containing any `Expectation` data associated with the traces.^[code-based-scorer-examples-databricks-on-aws.md]

The structure of the expectations is flexible; typical examples include an `expected_response` string and a list of `expected_keywords`. The following dataset illustrates this pattern:^[code-based-scorer-examples-databricks-on-aws.md]

```python
expectations_eval_dataset_list = [
    {
        "inputs": {"messages": [{"role": "user", "content": "What is 2+2?"}]},
        "expectations": {
            "expected_response": "2+2 equals 4.",
            "expected_keywords": ["4", "four", "equals"],
        }
    },
    {
        "inputs": {"messages": [{"role": "user", "content": "Describe MLflow in one sentence."}]},
        "expectations": {
            "expected_response": "MLflow is an open-source platform to streamline machine learning development, including tracking experiments, packaging code into reproducible runs, and sharing and deploying models.",
            "expected_keywords": ["mlflow", "open-source", "platform", "machine learning"],
        }
    },
    {
        "inputs": {"messages": [{"role": "user", "content": "Say hello."}]},
        "expectations": {
            "expected_response": "Hello there!",
        }
    }
]
```

## Implementing Expectations-Based Scorers

Custom [Code-based Scorers](/concepts/code-based-scorers.md) can access the expectations parameter to compute evaluation metrics. Two common patterns are exact-match scoring and keyword-presence checking.

### Exact Match Scorer

This scorer checks if the agent’s output exactly matches the `expected_response` provided in the expectations. It returns a boolean value:^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def exact_match(outputs: str, expectations: dict[str, Any]) -> bool:
    return outputs == expectations["expected_response"]
```

### Keyword Presence Scorer

This scorer verifies that all `expected_keywords` appear in the agent’s response, regardless of case, and returns a [Feedback](/concepts/feedback-object.md) object with a rationale:^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def keyword_presence_scorer(outputs: str, expectations: dict[str, Any]) -> Feedback:
    expected_keywords = expectations.get("expected_keywords")
    if expected_keywords is None:
        return Feedback(value="yes", rationale="No keywords were expected in the response.")
    missing_keywords = []
    for keyword in expected_keywords:
        if keyword.lower() not in outputs.lower():
            missing_keywords.append(keyword)
    if not missing_keywords:
        return Feedback(value="yes", rationale="All expected keywords are present in the response.")
    else:
        return Feedback(value="no", rationale=f"Missing keywords: {', '.join(missing_keywords)}.")
```

Both scorers can be used together with other evaluators (such as the built-in `Safety` scorer) in a single `mlflow.genai.evaluate()` call.^[code-based-scorer-examples-databricks-on-aws.md]

## Design Considerations

Because production monitoring typically does not include expectations, scorers intended for both offline and online evaluation should handle missing expectations gracefully. One approach is to check for the presence of the expectations field and return a neutral value or skip the expectation-based checks when ground truth is absent.^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom scoring functions that can accept expectations as input.
- Feedback (MLflow) – The object returned by scorers to capture evaluation results.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The broader framework that supports expectations-based evaluation.
- [Production Monitoring](/concepts/production-monitoring.md) – Online evaluation context where expectations are typically absent.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Data structures used to supply expectations to evaluation runs.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
