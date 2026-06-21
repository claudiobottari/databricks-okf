---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a360c77240fae6b3613d27550fa6a9c77bb2e2b2160d1dcf73dc30ee8354ccb
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-for-genai-applications
    - EDFGA
    - Evaluation of GenAI applications
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Evaluation Dataset for GenAI Applications
description: Structured input datasets used in MLflow evaluation, containing template-based examples with multiple test cases for assessing GenAI app performance.
tags:
  - evaluation
  - datasets
  - testing
  - genai
timestamp: "2026-06-19T21:53:59.849Z"
---

#Evaluation Dataset for GenAI Applications

An **Evaluation Dataset** for GenAI Applications is a structured collection of input examples used to measure the quality, safety, and alignment of a generative AI system (such as a chatbot, sentence‐completion model, or content generator). Evaluation datasets are a core component of the [MLflow](/concepts/mlflow.md) evaluation framework and are passed to `mlflow.genai.evaluate()` along with a prediction function and a set of [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Structure

In MLflow, an evaluation dataset is typically defined as a Python list of dictionaries. Each dictionary contains at least an `"inputs"` key whose value is itself a dictionary of keyword arguments that will be passed to the application’s prediction function (`predict_fn`). For example, a GenAI app that fills in sentence templates might receive a `"template"` argument: ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

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
    # ... more examples ...
]
```

The framework also supports including an `"expected"` key for supervised evaluation or ground‑truth comparisons, though the basic demo uses only `"inputs"`. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Role in the Evaluation Workflow

1. **Create the app** – Define a prediction function (e.g., `generate_game`) that calls an LLM.  
2. **Design the evaluation dataset** – Compose a representative set of inputs that exercise different capabilities or edge cases.  
3. **Define evaluation criteria** – Choose one or more [[Scorers]], such as `Guidelines` (rule‑based checks) or `Safety` (built‑in harmfulness detection).  
4. **Run the evaluation** – Call `mlflow.genai.evaluate(data=eval_data, predict_fn=..., scorers=...)`. The framework runs each input through the app, collects the outputs, and scores them against the criteria.  
5. **Review results** – Inspect per‑example scores and aggregate metrics in the MLflow UI.

## Best Practices

- **Cover diverse scenarios** – Include both typical inputs and edge cases (e.g., ambiguous templates, missing fields, offensive language prompts).  
- **Keep the dataset manageable** – A small set of well‑chosen examples (as few as 5–10) can reveal systemic issues. Larger datasets provide greater statistical reliability.  
- **Iterate with the app** – After improving the System Prompt or model, re‑run the same evaluation dataset to compare results across runs.  
- **Use expected outputs** when available – For regression testing, include ground‑truth answers to compute accuracy or similarity metrics.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The overarching evaluation framework.  
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – Components that score outputs against criteria such as funniness, safety, or template adherence.  
- Prompt Engineering – The practice of crafting system prompts; evaluation datasets help measure prompt quality.  
- [Evaluation Run](/concepts/evaluation-run.md) – A logged execution of the evaluation workflow in MLflow.  
- GenAI Application – The application under test (e.g., a sentence‑completion bot).  
- [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md) – Automatically creating evaluation data (not covered in the basic demo, but related).

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
