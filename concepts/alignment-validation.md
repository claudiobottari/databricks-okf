---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1eb51bad816cb116a478d8fc3365e3b15e9b6a40234045af65e56d1a26d568d3
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alignment-validation
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Alignment Validation
description: The practice of comparing original and aligned judge performance against human ground truth to measure improvement in accuracy after alignment.
tags:
  - validation
  - evaluation
  - mlflow
timestamp: "2026-06-19T17:32:35.634Z"
---

# Alignment Validation

**Alignment validation** is the methodology for testing whether [Judge Alignment](/concepts/judge-alignment.md) improved an LLM judge by comparing the original judge's accuracy against the aligned judge's accuracy using human ground truth on test traces.^[align-judges-with-humans-databricks-on-aws.md]

## Purpose

Alignment validation serves to confirm that the alignment process produced meaningful improvement before deploying the aligned judge into production. The validation answers two key questions:^[align-judges-with-humans-databricks-on-aws.md]

1. **Did alignment improve accuracy?** Quantify the difference between the original and aligned judge's agreement with human assessments.
2. **Is the improvement sufficient?** Determine whether the aligned judge meets quality requirements for production use.

## Validation Methodology

The validation process compares both judges against human-provided ground truth on a held-out set of traces:^[align-judges-with-humans-databricks-on-aws.md]

1. Collect test traces containing human feedback that were not used during alignment.
2. Run both the original judge and the aligned judge on each test trace.
3. For each trace, compare each judge's assessment value against the human feedback value.
4. Calculate accuracy metrics for both judges and compute the improvement.

### Example Validation Implementation

The following function demonstrates the standard approach:^[align-judges-with-humans-databricks-on-aws.md]

```python
def test_alignment_improvement(
    original_judge, aligned_judge, test_traces: list
) -> dict:
    """Compare judge performance before and after alignment."""
    original_correct = 0
    aligned_correct = 0
    for trace in test_traces:
        # Get human ground truth from trace assessments
        feedbacks = trace.search_assessments(type="feedback")
        human_feedback = next(
            (f for f in feedbacks if f.source.source_type == "HUMAN"), None
        )
        if not human_feedback:
            continue
        # Get judge evaluations
        original_eval = original_judge(trace=trace)
        aligned_eval = aligned_judge(trace=trace)
        # Check agreement with human
        if original_eval.value == human_feedback.value:
            original_correct += 1
        if aligned_eval.value == human_feedback.value:
            aligned_correct += 1
    total = len(test_traces)
    return {
        "original_accuracy": original_correct / total,
        "aligned_accuracy": aligned_correct / total,
        "improvement": (aligned_correct - original_correct) / total,
    }
```

## Expected Improvements

Judge alignment typically improves agreement with human assessments by 30 to 50 percent compared to baseline judges.^[align-judges-with-humans-databricks-on-aws.md] The actual improvement depends on factors such as the quality and quantity of human feedback, the representativeness of training traces, and the complexity of the evaluation criteria.

## Relationship to Judge Alignment Workflow

Alignment validation is the final step in the judge alignment workflow, which consists of three phases:^[align-judges-with-humans-databricks-on-aws.md]

1. **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments.
3. **Align and validate**: Invoke the judge's `align()` method to create an aligned judge, then validate the improvement using test traces before deployment.

## Best Practices

- **Use a held-out test set**: Validate on traces that were not used during alignment to avoid overestimating improvement.^[align-judges-with-humans-databricks-on-aws.md]
- **Include sufficient traces**: Test with at least 10 traces, though 50-100 traces provide more reliable validation.^[align-judges-with-humans-databricks-on-aws.md]
- **Ensure balanced examples**: Include both positive and negative examples (at least 30% poor/fair ratings) for meaningful accuracy measurement.^[align-judges-with-humans-databricks-on-aws.md]
- **Track metadata**: Record alignment dates and trace counts when registering aligned judges to monitor performance drift over time.^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) — The process of teaching LLM judges to match human evaluation standards
- [LLM Judges](/concepts/llm-judges.md) — AI evaluators used for assessing model outputs
- [Built-in Judges](/concepts/built-in-judges.md) — Predefined judges such as `RelevanceToQuery`, `Safety`, and `Correctness`
- [Custom Judges](/concepts/custom-judges.md) — Judges created with `make_judge()` for specialized evaluation criteria
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Domain expert assessments used to train aligned judges
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying aligned judges at scale after validation

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
