---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33cb51aa5dfe15c338fd7d51ba277428b1905178770b62df75ffb3d011d91572
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - evaluation-chaining-and-conditional-guidelines
    - Conditional Guidelines and Evaluation Chaining
    - ECACG
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Evaluation Chaining and Conditional Guidelines
description: A workflow pattern where evaluation results are reused to filter problematic traces and re-evaluate with different scorers or guidelines based on context.
tags:
  - mlflow
  - evaluation
  - chaining
  - guidelines
timestamp: "2026-06-19T09:13:59.902Z"
---

---
title: Evaluation Chaining and Conditional Guidelines
summary: Techniques for chaining evaluation results and applying conditional logic with guidelines using custom scorers in MLflow Evaluation for GenAI.
sources:
  - code-based-scorer-examples-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T22:00:00.000Z"
updatedAt: "2026-06-18T22:00:00.000Z"
tags:
  - mlflow
  - evaluation
  - genai
  - custom-scorers
  - guidelines
aliases:
  - evaluation-chaining-and-conditional-guidelines
  - ECACG
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Evaluation Chaining and Conditional Guidelines

**Evaluation Chaining** and **Conditional Guidelines** are two advanced patterns for building flexible, context-aware evaluation workflows with custom [Code-based Scorers](/concepts/code-based-scorers.md) in MLflow Evaluation for GenAI.

## Evaluation Chaining

Evaluation chaining allows you to run an initial evaluation, filter the results (e.g., to problematic traces), and then perform a follow-up evaluation on that subset. This is useful for iterative improvement of your AI application. ^[code-based-scorer-examples-databricks-on-aws.md]

The typical workflow is:

1. Run an evaluation with a broad scorer (such as `Safety()`) on your evaluation dataset.
2. Retrieve the traces from the results using `mlflow.search_traces()`.
3. Filter the traces to those where the scorer indicated a problem (e.g., `safety_failures`).
4. Use the filtered subset as input for a second evaluation, optionally with a different scorer (like `Guidelines`) or an updated version of your app.

Below is a conceptual example from the source material:

```python
results1 = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[Safety()]
)

traces = mlflow.search_traces(run_id=results1.run_id)

safety_failures = traces[traces['assessments'].apply(
    lambda x: any(a['assessment_name'] == 'Safety' and a['feedback']['value'] == 'no' for a in x)
)]

if len(safety_failures) > 0:
    results2 = mlflow.genai.evaluate(
        data=safety_failures,
        predict_fn=updated_app,
        scorers=[Guidelines(
            name="content_policy",
            guidelines="Response must follow our content policy"
        )]
    )
```

This pattern enables you to apply more detailed or expensive scorers only on the cases that need deeper inspection, or to focus iterative improvements on the most challenging inputs. ^[code-based-scorer-examples-databricks-on-aws.md]

## Conditional Guidelines

Conditional guidelines allow you to use different [Guidelines judges](/concepts/guidelines-llm-judges.md) within a single custom scorer based on context, such as user attributes or input features. This is achieved by wrapping a `Guidelines` judge inside a [[Scorers|@scorer]]-decorated function that inspects the input and selects the appropriate set of guidelines. ^[code-based-scorer-examples-databricks-on-aws.md]

The source material demonstrates a scorer that applies different guidelines depending on a `user_tier` field in the input:

```python
@scorer
def premium_service_validator(inputs, outputs, trace=None):
    user_tier = inputs.get("user_tier", "standard")

    if user_tier == "premium":
        premium_judge = Guidelines(
            name="premium_experience",
            guidelines=[
                "The response must acknowledge the user's premium status",
                "The response must provide detailed explanations with at least 3 specific examples",
                "The response must offer priority support options ...",
                "The response must not include any upselling or promotional content"
            ]
        )
        return premium_judge(inputs=inputs, outputs=outputs)
    else:
        standard_judge = Guidelines(
            name="standard_experience",
            guidelines=[
                "The response must be helpful and professional",
                "The response must be concise (under 100 words)",
                "The response may mention premium features as upgrade options"
            ]
        )
        return standard_judge(inputs=inputs, outputs=outputs)
```

This pattern allows you to enforce different quality standards for different segments of users while keeping a consistent evaluation pipeline. ^[code-based-scorer-examples-databricks-on-aws.md]

## Combining Chaining and Conditional Logic

These two patterns can be used together. For example, you might chain evaluations to first identify low-quality segments with a broad scorer, then apply conditional guidelines on the filtered traces to drill down into specific user-tier violations. Both approaches rely on the [custom scorer](/concepts/custom-scorers-mlflow-genai.md) framework in `mlflow.genai.evaluate()`.

## Related Concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md)
- [Guidelines judges](/concepts/guidelines-llm-judges.md)
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md)
- mlflow.search_traces()
- [Safety scorer](/concepts/safety-scorer-in-mlflow.md)
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
