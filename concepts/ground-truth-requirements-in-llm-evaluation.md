---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5491054cd3ea0a0600d46bcbc4b0fa96d60ea9c822c365f935020a80272ee5c
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ground-truth-requirements-in-llm-evaluation
    - GTRILE
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Ground Truth Requirements in LLM Evaluation
description: A design distinction among built-in judges where some evaluators require ground truth labels (e.g., Correctness, RetrievalSufficiency) and others evaluate purely based on inputs and outputs.
tags:
  - llm-evaluation
  - evaluation-design
  - mlflow
timestamp: "2026-06-19T09:11:37.562Z"
---

Here is the wiki page for "Ground Truth Requirements in LLM Evaluation", written based solely on the provided source material.

---

## Ground Truth Requirements in LLM Evaluation

**Ground Truth Requirements in LLM Evaluation** refers to the need for providing reference data (labeled as `expectations` or `ground truth`) to certain [Built-in LLM Judges](/concepts/built-in-llm-judges.md) so they can accurately assess whether an LLM's output is correct, sufficient, or faithful. Not all judges require ground truth, but those that do use it as a fixed point of comparison to score the quality of the response.

### Overview

In [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md), some judges evaluate outputs by comparing them against a known correct answer or an expected set of facts. This reference data is called **ground truth** (or **expectations** in the MLflow API). The presence or absence of ground truth determines which built-in judges can be used and what they measure. ^[built-in-llm-judges-databricks-on-aws.md]

### Judges That Require Ground Truth

The following built-in LLM judges require ground truth to function:

| Judge | Required Arguments | What It Evaluates |
|---|---|---|
| [`Correctness`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_correct) | `inputs`, `outputs`, `expectations` | Is the response correct as compared to the provided ground truth? |
| [`RetrievalSufficiency`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_context_sufficient) | `inputs`, `outputs`, `expectations` | Does the context provide all necessary information to generate a response that includes the ground truth facts? |
| [`ToolCallCorrectness`](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/tool-call/correctness/) | `inputs`, `outputs`, `expectations` | Are the tool calls and arguments correct for the user query? |

^[built-in-llm-judges-databricks-on-aws.md]

All three require the `expectations` argument in addition to `inputs` and `outputs`, meaning the ground truth data must be explicitly supplied in the evaluation dataset.

### Judges That Do NOT Require Ground Truth

Several judges evaluate quality without any reference to ground truth. They work solely with `inputs` and `outputs`: ^[built-in-llm-judges-databricks-on-aws.md]

- `RelevanceToQuery` – Is the response directly relevant to the user's request?
- `RetrievalRelevance` – Is the retrieved context directly relevant to the user's request?
- `Safety` – Is the content free from harmful, offensive, or toxic material?
- `RetrievalGroundedness` – Is the response grounded in the information provided in the context? Is the agent hallucinating?
- `Guidelines` – Does the response meet specified natural language criteria?
- `ToolCallEfficiency` – Are the tool calls efficient without redundancy?

Two additional judges (`ExpectationsGuidelines` and `RetrievalSufficiency`) require `expectations` in their arguments. `ExpectationsGuidelines` evaluates whether the response meets per-example natural language criteria, while `RetrievalSufficiency` checks if the context includes all necessary information to generate a response containing the ground truth facts. ^[built-in-llm-judges-databricks-on-aws.md]

### When Ground Truth Is Required

Ground truth is used to evaluate:

- **Correctness** – Comparing the model's output to a known correct answer
- **Sufficiency** – Checking whether the retrieved context contains enough information to reproduce the ground truth
- **Tool call correctness** – Validating that the model invoked the right tools with the right arguments for the intended task

When ground truth is not provided for these judges, they either cannot run or their evaluation score will be incomplete without the reference data.

### Best Practices

- **Provide ground truth for correctness and sufficiency evaluations.** When you need to know whether an output is factually correct or whether the context is sufficient, include `expectations` in your evaluation dataset.
- **Use ground truth-free judges for safety and relevance.** For quick quality checks on safety, relevance, and groundedness, use judges that do not require ground truth.
- **Align expectations with your use case.** Ground truth can be a single correct answer, a set of required facts, or a checklist of key points that the response must cover.
- **Consider custom judges.** When built-in judges don't match your quality criteria, build [Custom LLM Judges](/concepts/custom-llm-judges.md) that may or may not require ground truth.

### Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Predefined scorers for common quality dimensions
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – User-defined evaluators for domain-specific criteria
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) – The broader process of assessing model output quality
- Ground Truth – The reference data used for comparison
- [Expectations in Evaluation](/concepts/expectations-in-mlflow-evaluation.md) – The `expectations` argument in MLflow's evaluation API

### Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
