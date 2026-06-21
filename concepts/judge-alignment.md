---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f851fb8e1e6ce73acb88f8e528e842bd74454d0fc2b47dedc6d1ed4113ff361
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - judge-alignment
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Judge Alignment
description: A process that teaches LLM judges to match human evaluation standards through systematic feedback, improving agreement with human assessments by 30-50 percent.
tags:
  - llm-evaluation
  - alignment
  - mlflow
  - genai
timestamp: "2026-06-19T22:04:54.128Z"
---

# Judge Alignment

**Judge alignment** is a process that teaches [LLM Judges](/concepts/llm-judges.md) to match human evaluation standards through systematic feedback. By collecting human corrections on a judge’s initial assessments, the alignment workflow refines the judge’s evaluation criteria so that it produces scores more closely aligned with domain‑expert judgments. This typically improves agreement with human assessments by 30 to 50 percent compared to the baseline judge. ^[align-judges-with-humans-databricks-on-aws.md]

The same alignment workflow applies to both [built‑in LLM judges](/concepts/built-in-llm-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`. Use alignment with built‑in judges to adapt their generic criteria to your domain, or with custom judges to refine specialized evaluation logic. ^[align-judges-with-humans-databricks-on-aws.md]

## Workflow

Judge alignment follows a three‑step workflow: ^[align-judges-with-humans-databricks-on-aws.md]

1. **Generate initial assessments** – Use a built‑in or custom judge to evaluate traces and establish a baseline.  
2. **Collect human feedback** – Domain experts review and correct judge assessments.  
3. **Align and deploy** – Invoke the judge’s `align()` method to create a new judge that is more aligned with human feedback.  

The system supports the optimizers available in the package `mlflow.genai.judges.optimizers`. ^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- **MLflow 3.4.0 or above** – Required for all judge alignment features. ^[align-judges-with-humans-databricks-on-aws.md]  
- **A judge to align** – Can be a built‑in judge or a custom judge created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]  
- **Matching assessment names** – The human feedback assessment name must exactly match the judge’s `name` attribute. For built‑in judges this is the default snake_case name (e.g. `relevance_to_query` for `RelevanceToQuery`) unless overridden with `name=` when instantiating the class. For custom judges it is the `name` passed to `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]  
- **Not supported for session‑level judges** – Multi‑turn judges such as `ConversationCompleteness` cannot be aligned. ^[align-judges-with-humans-databricks-on-aws.md]

## Step 1: Set up the judge and generate traces

Set up your initial judge and produce a set of traces with judge assessments. You can achieve reasonable alignment with at least 10 traces, but 50–100 traces yield better results. ^[align-judges-with-humans-databricks-on-aws.md]

For a built‑in judge, instantiate it directly (e.g. `RelevanceToQuery()`). For a custom judge, use `make_judge()` from the `mlflow.genai.judges` module. Then run your application to generate traces, evaluate each trace with the judge, and log the judge’s assessment to the trace using `mlflow.log_feedback()`. Use the judge’s `name` attribute as the feedback `name`. ^[align-judges-with-humans-databricks-on-aws.md]

## Step 2: Collect human feedback

Collect human feedback to teach the judge your quality standards. You can provide feedback through the Databricks UI or programmatically. ^[align-judges-with-humans-databricks-on-aws.md]

- **Databricks UI review**: Navigate to the MLflow experiment in the Databricks workspace, open the **Traces** tab, review each trace and its judge assessment, and add human feedback using the UI. Ensure the feedback name matches the judge’s `name` attribute exactly. ^[align-judges-with-humans-databricks-on-aws.md]  
- **Programmatic feedback**: Write code that submits human‑corrected assessments. ^[align-judges-with-humans-databricks-on-aws.md]

### Best practices for feedback collection ^[align-judges-with-humans-databricks-on-aws.md]

- Include multiple domain experts to capture varied perspectives.  
- Aim for at least 30% negative examples (poor/fair ratings).  
- Provide detailed rationales for ratings.  
- Cover edge cases and common scenarios to ensure representative samples.

## Step 3: Align and register the judge

Once sufficient human feedback is available (at least 10 traces), call the judge’s `align()` method. By default, the **MemAlign** optimizer is used automatically; you can optionally specify a different optimizer. ^[align-judges-with-humans-databricks-on-aws.md]

```python
aligned_judge = initial_judge.align(traces_for_alignment)
```

After alignment, register the aligned judge for production use. Use a new name to distinguish it from the original judge:

```python
aligned_judge.register(
    experiment_id=experiment_id,
    name=f"{initial_judge.name}_aligned",
    tags={"alignment_date": "2025-10-23", "num_traces": str(len(traces_for_alignment))}
)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Enable detailed logging

To monitor the alignment process, enable debug logging for the optimizer:

```python
import logging
logging.getLogger("mlflow.genai.judges.optimizers.memalign").setLevel(logging.DEBUG)
```

Then run alignment with verbose output. ^[align-judges-with-humans-databricks-on-aws.md]

## Validate alignment

Compare judge performance before and after alignment on a hold‑out test set. An example validation function iterates over test traces, compares both judges’ scores to human ground truth, and returns accuracy improvement metrics. ^[align-judges-with-humans-databricks-on-aws.md]

## Custom alignment optimizers

For specialized alignment strategies, extend the `AlignmentOptimizer` base class from `mlflow.genai.judges.base`. Your custom optimizer implements its own `align()` method and can be passed to the judge’s `align()` method. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent‑based or expectation‑based evaluation. ^[align-judges-with-humans-databricks-on-aws.md]

## Related concepts

- [Built‑in LLM judges](/concepts/built-in-llm-judges.md) – Pre‑configured judges for common quality dimensions.  
- [Custom Judges](/concepts/custom-judges.md) – Judges defined with custom prompts using `make_judge()`.  
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – Overview of the scorer framework.  
- [MLflow](/concepts/mlflow.md) – The platform that enables tracing, evaluation, and alignment.  
- [Trace](/concepts/traces.md) – Unit of evaluation that contains inputs, outputs, and intermediate steps.  
- [Feedback](/concepts/feedback-object.md) – Annotations (human or judge) attached to traces.  
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying aligned judges at scale.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
