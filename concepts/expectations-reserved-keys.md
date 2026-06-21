---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05a97decf149316a711ccfa2970c691cea388f5a0204039213ba91254f9bb9c8
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expectations-reserved-keys
    - ERK
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Expectations Reserved Keys
description: Built-in reserved keys in the expectations field (guidelines, expected_facts, expected_response) used by MLflow's LLM judges for structured ground-truth evaluation.
tags:
  - mlflow
  - evaluation
  - llm-judges
timestamp: "2026-06-19T18:43:14.835Z"
---

# Expectations Reserved Keys

**Expectations Reserved Keys** are a set of predefined key names within the `expectations` field of an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) that are interpreted by built-in LLM judges during GenAI app evaluation. When you define expectations for evaluation records, these reserved keys have special meaning and are used by automated scoring algorithms. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Overview

In MLflow's evaluation framework, each dataset record can include an `expectations` field containing the expected or ground-truth output for that input. The `expectations` object supports several reserved keys that are recognized by MLflow's built-in LLM judges. These keys allow you to provide structured guidance and reference material that judges use when scoring model outputs. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Reserved Keys

The following keys are reserved within the `expectations` field:

### `guidelines`

The `guidelines` key is used to provide instructions or rules that the LLM judge should follow when evaluating the response. This allows you to specify custom evaluation criteria beyond the default behavior of the judge. ^[evaluation-dataset-reference-databricks-on-aws.md]

### `expected_facts`

The `expected_facts` key contains a set of factual statements that the model's response should include. The LLM judge uses this to verify whether the generated output contains the required factual information. ^[evaluation-dataset-reference-databricks-on-aws.md]

### `expected_response`

The `expected_response` key holds the ideal or golden response for the given input. The LLM judge can compare the model's actual output against this expected response to assess similarity or correctness. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Usage in Evaluation Records

When creating evaluation dataset records, you can include these reserved keys in the `expectations` field as part of the record's JSON structure. For example:

```json
{
    "inputs": "What is the capital of France?",
    "expectations": {
        "expected_facts": ["Paris is the capital of France"],
        "expected_response": "The capital of France is Paris."
    }
}
```

^[evaluation-dataset-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — The dataset schema that contains the `expectations` field
- [LLM Judges](/concepts/llm-judges.md) — Automated evaluators that use expectations for scoring
- [GenAI App Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — The broader evaluation framework for generative AI applications
- [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) — Complete schema definition for evaluation datasets
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for evaluation runs

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
