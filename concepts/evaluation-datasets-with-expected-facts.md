---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 582955f1ab7b882bc1164bd8ae7ec8cc6d90156992819c0334a1c0104af5fe34
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-datasets-with-expected-facts
    - EDWEF
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Evaluation Datasets with Expected Facts
description: Building structured evaluation datasets that pair input content with expected facts to serve as ground truth for prompt performance measurement.
tags:
  - evaluation
  - datasets
  - testing
timestamp: "2026-06-18T15:36:45.010Z"
---

# Evaluation Datasets with Expected Facts

**Evaluation Datasets with Expected Facts** are structured datasets used in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation to assess the quality of LLM-generated outputs. Each example in the dataset pairs an `inputs` object — the prompt context or content passed to the model — with an `expectations` dictionary containing an `expected_facts` list. These facts represent the key pieces of information that a high-quality response should include from the source material. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

By grounding evaluation in a predefined set of expected facts, developers can automatically measure factual coverage using scorers like `Correctness()`, which checks whether the generated output mentions each expected fact. This approach provides a quantitative, reproducible way to compare different [prompt versions](/concepts/prompt-versioning.md) or agent configurations. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Structure

An evaluation dataset is stored as a Unity Catalog table (created via `mlflow.genai.datasets.create_dataset()`) and populated with records using `merge_records()`. Each record must contain:

- **`inputs`**: A dictionary whose keys correspond to template variables in the prompt (e.g., `"content"`). The values are the input text or context.
- **`expectations`**: A dictionary with a key `expected_facts`, whose value is a list of strings. Each string describes a single fact that the output should reflect. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Example Record

```python
{
    "inputs": {
        "content": "Remote work has fundamentally changed ..."
    },
    "expectations": {
        "expected_facts": [
            "remote work changed collaboration",
            "digital tools adoption",
            "productivity remained stable",
            "challenges with company culture",
            "work-life balance issues",
            "global talent recruitment"
        ]
    }
}
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Purpose

Expected facts serve as the ground truth for automated correctness evaluation. When a scorer like `Correctness()` is applied, it compares the generated output against the list of expected facts and produces a coverage score. This score tells developers what fraction of the required facts the output correctly includes. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

In a typical prompt version comparison workflow:

1. Create an evaluation dataset containing multiple examples with expected facts.
2. Evaluate each prompt version using the same dataset and scorers, including `Correctness()`.
3. Compare the correctness scores to select the best-performing version. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Creating an Evaluation Dataset

The following steps are demonstrated in the source material:

- **Create the dataset** using `mlflow.genai.datasets.create_dataset(uc_table_name=...)`.
- **Define examples** as a list of dictionaries, each with `inputs` and `expectations` keys.
- **Add examples** to the dataset via `eval_dataset.merge_records(evaluation_examples)`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The dataset is persisted in Unity Catalog and can be reused across multiple evaluation runs, ensuring consistent comparison.

## Best Practices

- **Cover edge cases**: Include challenging examples with expected facts to test model robustness.
- **Keep facts atomic**: Write each expected fact as a single, self-contained statement.
- **Align facts with task requirements**: For summarization, facts should capture the core claims; for question answering, facts should match the correct answer content.
- **Use consistent datasets**: Evaluate all prompt versions against the same set of expected facts to ensure fair comparison. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Prerequisites

Working with evaluation datasets in MLflow requires:

- MLflow 3.1.0 or higher.
- Unity Catalog privileges: `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` on the target [Catalog and Schema](/concepts/catalog-and-schema.md).
- An LLM endpoint (e.g., OpenAI API or Databricks Model Serving) to run the prompts being evaluated. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework that uses these datasets.
- [Correctness Scorer](/concepts/correctness-scorer.md) — The built-in scorer that checks expected facts.
- [Custom Judges](/concepts/custom-judges.md) — User-defined scorers that can also reference expected facts.
- [Prompt Version Management](/concepts/prompt-version-management.md) — The workflow of comparing prompt versions with evaluation datasets.
- [Prompt Registry](/concepts/prompt-registry.md) — Where prompt versions are stored and aliased.
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying storage for evaluation datasets.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
