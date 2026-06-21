---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26b5087a1f304a0eab48f0a60f7ffbf70202c3ea2d3a71efd128a90a1b399a16
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-feedback-object
    - MGFO
  citations:
    - file: correctness-judge-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow GenAI Feedback Object
description: A structured output returned by LLM judges containing a binary value (yes/no) and a detailed rationale explaining the evaluation result.
tags:
  - mlflow
  - llm-evaluation
  - api
timestamp: "2026-06-19T14:28:07.305Z"
---

---
title: MLflow GenAI Feedback Object
summary: The structured object returned by MLflow GenAI judges, containing a `value` (e.g., "yes"/"no") and a `rationale` explaining the reasoning.
sources:
  - correctness-judge-databricks-on-aws.md
  - create-a-custom-judge-using-make_judge-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:15:00.004Z"
updatedAt: "2026-06-18T08:15:00.004Z"
tags:
  - mlflow
  - genai
  - evaluation
  - feedback
aliases:
  - feedback-object
  - mlflow-genai-feedback
confidence: 0.9
provenanceState: inferred
inferredParagraphs: 2
---

# MLflow GenAI Feedback Object

The **Feedback Object** in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) is the result returned by LLM-based judges (scorers) when evaluating the quality of a GenAI application’s response. It encapsulates the judge’s verdict and the reasoning behind it.

## Structure

Every Feedback object has two primary attributes:

- **`value`**: A string (or boolean) representing the judge’s decision. For built-in judges such as `Correctness`, the value is either `"yes"` (the response is factually correct) or `"no"` (incorrect). For custom judges created with `make_judge()`, the value type is determined by the `feedback_value_type` parameter (e.g., `bool` yielding `True`/`False`, or an enum string). ^[correctness-judge-databricks-on-aws.md] ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

- **`rationale`**: A detailed textual explanation of why the judge assigned that value. The rationale may list which facts were supported or missing, or describe how the response met or failed the evaluation criteria. ^[correctness-judge-databricks-on-aws.md]

## Usage

Feedback objects are typically consumed after a judge is invoked directly or as part of an `mlflow.genai.evaluate()` call.

### Direct invocation

```python
from mlflow.genai.scorers import Correctness

judge = Correctness()
feedback = judge(
    inputs={"request": "What is MLflow?"},
    outputs={"response": "MLflow is the largest open source AI engineering platform."},
    expectations={"expected_facts": ["MLflow is open-source"]}
)
print(feedback.value)        # "yes"
print(feedback.rationale)    # Explanation of why the response is correct
```

### Within an evaluation run

When using `mlflow.genai.evaluate()`, each row’s Feedback objects are aggregated into the evaluation results table. The feedback values across all rows can then be analyzed to compute quality metrics for the entire evaluation dataset. ^[correctness-judge-databricks-on-aws.md]

## Interpretation

- For the `Correctness` judge: a `value` of `"yes"` means the response contains the expected facts (or matches the expected response); `"no"` means the response is missing or contradicts the expected information. ^[correctness-judge-databricks-on-aws.md]
- For custom judges: the `value` directly corresponds to the `feedback_value_type` chosen at creation (e.g., a boolean, a string enum). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The `rationale` provides transparency, enabling developers to debug judge behavior or to manually review borderline cases.

## Related Concepts

- [Built-in Judges (MLflow GenAI)](/concepts/built-in-judges-mlflow.md) – Pre‑defined scorers such as `Correctness` that return Feedback objects.
- [Custom Judges (MLflow GenAI)](/concepts/custom-scorers-mlflow-genai.md) – User‑defined judges that also produce Feedback objects with a user‑specified value type.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API that aggregates Feedback objects across a dataset.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – A technique where judges analyze execution traces; Feedback objects from trace‑based judges include tool‑call correctness.

## Sources

- correctness-judge-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
