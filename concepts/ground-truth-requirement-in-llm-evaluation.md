---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c37321c6aaebabd5eb7ad86221a3886a1c0981fc9d4f5bcaaf0c0055c87a5687
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ground-truth-requirement-in-llm-evaluation
    - GTRILE
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Ground truth requirement in LLM evaluation
description: Design pattern where some LLM judges (Correctness, RetrievalSufficiency, ToolCallCorrectness) require ground truth expectations as input, while others (RelevanceToQuery, Safety, RetrievalGroundedness) do not.
tags:
  - llm-evaluation
  - evaluation-design
  - mlflow
timestamp: "2026-06-18T10:55:13.626Z"
---

# Ground truth requirement in LLM evaluation

**Ground truth requirement in LLM evaluation** refers to the need for a known correct answer or reference fact (the "ground truth") to assess certain quality dimensions of an LLM's output. Not all evaluation judges require ground truth; the requirement depends on what the judge is measuring. Built-in LLM judges in [MLflow](/concepts/mlflow.md) and Databricks make this distinction explicit. ^[built-in-llm-judges-databricks-on-aws.md]

## Which judges require ground truth

The following built-in LLM judges mandate the presence of a `expectations` column (the ground truth) in the evaluation dataset:

| Judge | What it evaluates | Ground truth required? |
|---|---|---|
| `Correctness` | Is the response correct as compared to the provided ground truth? | Yes |
| `RetrievalSufficiency` | Does the context provide all necessary information to generate a response that includes the ground truth facts? | Yes |
| `ToolCallCorrectness` | Are the tool calls and arguments correct for the user query? | Yes |

All other built-in judges listed in the documentation—`RelevanceToQuery`, `RetrievalRelevance`, `Safety`, `RetrievalGroundedness`, `Guidelines`, `ExpectationsGuidelines`, and `ToolCallEfficiency`—do not require ground truth. ^[built-in-llm-judges-databricks-on-aws.md]

Note that `ExpectationsGuidelines` does not require a ground truth answer, but it does expect per-example natural language criteria in the `expectations` field. ^[built-in-llm-judges-databricks-on-aws.md]

## Why ground truth is needed

Judges that evaluate **correctness** or **sufficiency** compare the LLM's response against a known reference. For example:

- The `Correctness` judge answers: "Is the response correct as compared to the provided ground truth?" ^[built-in-llm-judges-databricks-on-aws.md]
- The `RetrievalSufficiency` judge answers: "Does the context provide all necessary information to generate a response that includes the ground truth facts?" ^[built-in-llm-judges-databricks-on-aws.md]
- The `ToolCallCorrectness` judge checks whether the tool calls and arguments are correct for the user query, which requires knowing the correct tool usage. ^[built-in-llm-judges-databricks-on-aws.md]

Without a ground truth, these dimensions cannot be objectively scored by an LLM judge.

## Usage considerations

When designing an evaluation dataset, prepare ground truth entries in the `expectations` column only for the judges that require it. For other judges, the `inputs` and `outputs` columns suffice.

For multi-turn conversations, MLflow provides separate multi-turn judges that evaluate entire conversation histories. These judges may also have ground truth requirements; consult the [MLflow predefined scorers documentation](/concepts/mlflow-genai-predefined-scorers.md) for details. ^[built-in-llm-judges-databricks-on-aws.md]

If you need to evaluate a quality dimension that is not covered by built-in judges, you can build a [Custom LLM Judge](/concepts/custom-llm-judge.md) or a Python [code-based scorer](/concepts/code-based-scorers.md). These custom approaches let you define your own ground truth logic as needed. ^[built-in-llm-judges-databricks-on-aws.md]

## Related concepts

- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md) — The broader practice of assessing LLM quality
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined scorers for common evaluation dimensions
- [Custom LLM Judge](/concepts/custom-llm-judge.md) — User-defined judges for specialized metrics
- [Code-based scorer](/concepts/code-based-scorers.md) — Python-based evaluation functions
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework that hosts these judges
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The input data format for LLM evaluation

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
