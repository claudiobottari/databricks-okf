---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f4d283a03acad580c928e1033454d20ba4cc54bd04ccc6d5021d86ea94201d3
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judge-scorers
    - CJS
    - Custom LLM judge scorers
    - Custom LLM Scorers
    - Custom LLM scorers
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Custom Judge Scorers
description: Custom evaluation metrics created using MLflow's make_judge API with custom prompt instructions to assess specific criteria like sentence count compliance.
tags:
  - evaluation
  - scorers
  - genai
timestamp: "2026-06-19T18:40:52.977Z"
---

# Custom Judge Scorers

**Custom Judge Scorers** are user-defined evaluators in the [MLflow](/concepts/mlflow.md) GenAI evaluation framework that use a custom prompt to judge model outputs according to specific criteria. Unlike built-in scorers (e.g., `Correctness`), a custom judge allows you to define your own instructions and feedback schema, enabling domain‑specific quality checks such as adherence to a required output format, tone, or factual completeness. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Usage with `make_judge`

Custom judge scorers are created using the `mlflow.genai.make_judge` function. This function accepts the following key parameters: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

- **`name`** – A human‑readable label for the judge (e.g., `"sentence_count_compliance"`). The name is used as a prefix in evaluation metric keys.
- **`instructions`** – A prompt template that tells the judge how to evaluate the output. The template can reference `{{ outputs }}` to access the model’s response; for pair‑wise comparisons you may also use `{{ inputs }}` or `{{ references }}`.
- **`feedback_value_type`** – A `Literal` type defining the set of allowed feedback values, e.g., `Literal["correct", "incorrect"]`. The judge must output one of these values.

The resulting object can be passed to `mlflow.genai.evaluate()` as part of the `scorers` list and will produce metrics such as `{name}/mean` (the proportion of outputs that received the highest‑ranked feedback value). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Example

The following example creates a custom judge that verifies whether a summary contains exactly two sentences: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from typing import Literal
from mlflow.genai import make_judge

sentence_count_judge = make_judge(
    name="sentence_count_compliance",
    instructions="""
Evaluate if this summary follows the 2-sentence requirement.
Summary: {{ outputs }}
Count the sentences carefully and determine if the summary has exactly 2 sentences.
""",
    feedback_value_type=Literal["correct", "incorrect"],
)
```

This judge can then be used alongside built‑in scorers during comparative evaluation of prompt versions. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Integration with Evaluation

Custom judge scorers are designed to work seamlessly with the broader MLflow evaluation workflow: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

scorers = [
    Correctness(),          # built‑in scorer
    sentence_count_judge,   # custom judge
]

with mlflow.start_run(run_name="summary_v1_eval"):
    results = mlflow.genai.evaluate(
        predict_fn=my_summary_function,
        data=eval_dataset,
        scorers=scorers,
    )
```

The evaluation results include metrics for both the built‑in scorer and the custom judge, allowing you to compare composite scores and select the best‑performing prompt version. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) – The set of built‑in evaluators such as `Correctness` and `Faithfulness`.
- [Evaluation Harness](/concepts/evaluation-harness.md) – The underlying engine that orchestrates `mlflow.genai.evaluate()`.
- [Prompt Evaluation](/concepts/prompt-version-evaluation.md) – The broader practice of systematically testing prompt versions.
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) – The general technique of using a language model as an evaluator.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
