---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3d9bcd7a8e4eb49012fd6ba14a801c607e80d19d98d60dfdac801fdb1b96608
  pageDirectory: concepts
  sources:
    - optimize-prompts-tutorial-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - correctness-scorer-in-mlflow-genai
    - CSIMG
  citations:
    - file: optimize-prompts-tutorial-databricks-on-aws.md
title: Correctness Scorer in MLflow GenAI
description: An evaluation scorer that assesses whether model outputs match expected responses based on provided ground-truth labels and facts
tags:
  - evaluation
  - scoring
  - mlflow
timestamp: "2026-06-19T19:52:40.963Z"
---

# Correctness Scorer in MLflow GenAI

The **Correctness Scorer** is a built-in evaluation metric in MLflow GenAI used to assess the factual accuracy of model outputs against expected ground truth information. It is part of the `mlflow.genai.scorers` module and is commonly employed in Prompt Optimization workflows to guide automated prompt improvement.

## Overview

The Correctness Scorer evaluates whether a model's generated response contains accurate information when compared against provided ground truth facts or expected outputs. It uses an underlying LLM judge to perform this evaluation, making it an [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) approach to automated evaluation. ^[optimize-prompts-tutorial-databricks-on-aws.md]

## Usage

The Correctness Scorer is instantiated by specifying the model to use as the judge for evaluating correctness. This is typically a capable language model that can assess whether the generated output matches the expected facts. ^[optimize-prompts-tutorial-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

scorer = Correctness(model="databricks:/databricks-gpt-5")
```

## Application in Prompt Optimization

The Correctness Scorer is a key component in Prompt Optimization using the GEPA (Generation Evaluation Prompting Adjustment) optimizer. When optimizing prompts, the scorer evaluates each candidate prompt's outputs against the training data's expected responses and facts. ^[optimize-prompts-tutorial-databricks-on-aws.md]

Typical usage within an optimization workflow:

```python
from mlflow.genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]
from mlflow.genai.scorers import Correctness

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),
    scorers=[Correctness(model="databricks:/databricks-gpt-5")],
)
```

## Integration with Training Data

The Correctness Scorer works with training data that includes `expectations` containing `expected_facts`. These facts define the ground truth information that the generated response should contain. The scorer evaluates the response against these facts to produce a correctness score. ^[optimize-prompts-tutorial-databricks-on-aws.md]

Training data structure example:

```python
dataset = [
    {
        "inputs": {"query": "Your input query here"},
        "outputs": {"response": "BACKGROUND"},
        "expectations": {"expected_facts": ["Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'"]}
    }
]
```

## Related Concepts

- Prompt Optimization — The workflow in which Correctness Scorer is commonly used
- [GEPA Prompt Optimizer](/concepts/gepapromptoptimizer.md) — The optimization algorithm that uses scorers for prompt improvement
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The evaluation paradigm underlying the Correctness Scorer
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for managing and evaluating generative AI applications
- [[GPT-OSS 20B]] — Example model used alongside the Correctness Scorer in optimization workflows

## Sources

- optimize-prompts-tutorial-databricks-on-aws.md

# Citations

1. [optimize-prompts-tutorial-databricks-on-aws.md](/references/optimize-prompts-tutorial-databricks-on-aws-b91f2148.md)
