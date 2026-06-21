---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b13b0acbbf415c3f7ee426dbbe83d9c97b7759297a9c255d4f4ab5794116b41
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - judge-alignment-three-step-workflow
    - JATW
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Judge Alignment Three-Step Workflow
description: "The standard workflow for aligning judges: generate initial assessments, collect human feedback, then align and deploy using the judge's align() method."
tags:
  - workflow
  - llm-evaluation
  - mlflow
timestamp: "2026-06-19T17:32:12.255Z"
---

# Judge Alignment Three-Step Workflow

**Judge Alignment Three-Step Workflow** is a systematic process for adapting [LLM Judges](/concepts/llm-judges.md) to match human evaluation standards. By collecting human feedback on judge assessments and using an optimizer to refine the judge's instructions, alignment can improve agreement with human evaluators by 30 to 50 percent compared to baseline judges. The same workflow applies to both [Built-in Judges](/concepts/built-in-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- MLflow 3.4.0 or above (install with `%pip install --upgrade "mlflow[databricks]>=3.4.0" databricks_openai dspy`). ^[align-judges-with-humans-databricks-on-aws.md]
- A judge to align — either a built-in judge or a custom judge created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]
- The human feedback assessment name must exactly match the judge's `name` attribute. For built-in judges the default is a snake_case string (e.g., `relevance_to_query`); for custom judges it is the name passed to `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]
- Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`. ^[align-judges-with-humans-databricks-on-aws.md]

## The Three-Step Workflow

### Step 1: Set Up the Judge and Generate Traces

Instantiate the initial judge (built-in or custom) and generate traces with judge assessments. At least 10 traces are recommended; 50–100 yield better results. Each trace should include the judge's output (value and rationale) logged via `mlflow.log_feedback()` using the judge's `name` as the feedback name. ^[align-judges-with-humans-databricks-on-aws.md]

Example with a built-in judge:

```python
from mlflow.genai.scorers import RelevanceToQuery
experiment = mlflow.set_experiment("/Shared/relevance-alignment")
initial_judge = RelevanceToQuery()

# ... generate traces (e.g., 50 product descriptions) ...
for i in range(50):
    trace_id = mlflow.get_last_active_trace_id()
    judge_result = initial_judge(trace=trace)
    mlflow.log_feedback(
        trace_id=trace_id,
        name=initial_judge.name,
        value=judge_result.value,
        rationale=judge_result.rationale,
    )
```

^[align-judges-with-humans-databricks-on-aws.md]

### Step 2: Collect Human Feedback

Domain experts review the traces and correct the judge assessments. Feedback can be collected through the MLflow UI or programmatically. The feedback name must match the judge's `name` attribute exactly. ^[align-judges-with-humans-databricks-on-aws.md]

Best practices for feedback collection:
- **Diverse reviewers**: Include multiple domain experts.
- **Balanced examples**: Include at least 30% negative (poor/fair) ratings.
- **Clear rationales**: Provide detailed explanations for each rating.
- **Representative samples**: Cover edge cases and common scenarios.

^[align-judges-with-humans-databricks-on-aws.md]

### Step 3: Align and Deploy the Judge

Once sufficient human feedback exists, invoke the judge's `align()` method to create a new, improved judge. By default the MemAlign optimizer is used. The aligned judge can then be registered for production use. ^[align-judges-with-humans-databricks-on-aws.md]

```python
traces_for_alignment = mlflow.search_traces(
    experiment_ids=[experiment_id], max_results=100, return_type="list"
)
if len(traces_for_alignment) >= 10:
    aligned_judge = initial_judge.align(traces_for_alignment)
    aligned_judge.register(
        experiment_id=experiment_id,
        name=f"{initial_judge.name}_aligned",
        tags={"alignment_date": "2025-10-23", "num_traces": str(len(traces_for_alignment))}
    )
```

^[align-judges-with-humans-databricks-on-aws.md]

An explicit optimizer can also be passed (e.g., `MyCustomOptimizer`). See [Alignment Optimizers](/concepts/alignment-optimizers.md) for the available optimizers in `mlflow.genai.judges.optimizers`. ^[align-judges-with-humans-databricks-on-aws.md]

## Enabling Detailed Logging

To monitor the alignment process, enable debug logging for the optimizer:

```python
import logging
logging.getLogger("mlflow.genai.judges.optimizers.memalign").setLevel(logging.DEBUG)
aligned_judge = initial_judge.align(traces_for_alignment)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Validating Alignment

After alignment, compare the original and aligned judges on a held-out test set. A helper function can compute accuracy against human ground truth and measure improvement. ^[align-judges-with-humans-databricks-on-aws.md]

```python
def test_alignment_improvement(original_judge, aligned_judge, test_traces):
    # ... compute original_correct, aligned_correct ...
    return {"original_accuracy": ..., "aligned_accuracy": ..., "improvement": ...}
```

^[align-judges-with-humans-databricks-on-aws.md]

## Creating Custom Alignment Optimizers

For specialized alignment strategies, extend the `AlignmentOptimizer` base class from `mlflow.genai.judges.base`. The custom optimizer must implement an `align(judge, traces)` method that returns a new `Judge` instance with improved instructions. ^[align-judges-with-humans-databricks-on-aws.md]

```python
from mlflow.genai.judges.base import AlignmentOptimizer, Judge

class MyCustomOptimizer(AlignmentOptimizer):
    def align(self, judge: Judge, traces) -> Judge:
        # Extract feedback, analyze disagreements, generate improved instructions
        return make_judge(name=judge.name, instructions=improved_instructions, model=judge.model)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation. ^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md)
- [Built-in Judges](/concepts/built-in-judges.md)
- [Custom Judges](/concepts/custom-judges.md)
- [Judge Alignment](/concepts/judge-alignment.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- [Alignment Optimizers](/concepts/alignment-optimizers.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- [Trace Evaluation](/concepts/mlflow-trace-based-evaluation.md)

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
