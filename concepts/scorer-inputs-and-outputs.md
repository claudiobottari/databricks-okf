---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2812a63ccab3024a15d34995bfd174cc4875e618a133c76e6f15201aad462e9b
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-inputs-and-outputs
    - outputs and Scorer inputs
    - SIAO
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer inputs and outputs
description: Scorers receive inputs (request), outputs (response), expectations (ground truth), and trace (complete MLflow trace), and return simple values or rich Feedback objects.
tags:
  - mlflow
  - scoring
  - evaluation
timestamp: "2026-06-19T17:44:31.464Z"
---

---
title: Scorer inputs and outputs
summary: The four input parameters (inputs, outputs, expectations, trace) that scorers receive and the return types (simple values or Feedback objects) they produce.
sources:
  - code-based-scorer-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:36:39.963Z"
updatedAt: "2026-06-18T14:36:39.963Z"
tags:
  - mlflow
  - evaluation
  - scorer-api
aliases:
  - scorer-inputs-and-outputs
  - outputs and Scorer inputs
  - SIAO
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 2
---

# Scorer inputs and outputs

**Scorer inputs and outputs** define the data that custom code-based scorers receive and return when evaluating AI applications. Scorers are functions that assess the quality, safety, or behavior of model outputs, and their input/output contract determines what information is available for evaluation and how results are structured. ^[code-based-scorer-reference-databricks-on-aws.md]

## Inputs

Scorers receive the complete [[MLflow trace]] containing all spans, attributes, and outputs. MLflow also extracts commonly needed data and passes it as named arguments. All input arguments are optional, so scorers should declare only what they need. ^[code-based-scorer-reference-databricks-on-aws.md]

The available input parameters are:

- **`inputs`**: The request sent to the application (for example, user query, context). This is a dictionary of input argument names and values.
- **`outputs`**: The response from the application (for example, generated text, tool calls). This can be any type.
- **`expectations`**: Ground truth or labels (for example, expected response, guidelines). This is a dictionary of label names and values.
- **`trace`**: The complete MLflow trace including all spans, allowing analysis of intermediate steps, latency, tool usage, and more. The trace is passed as an instantiated `mlflow.entities.Trace` class. ^[code-based-scorer-reference-databricks-on-aws.md]

When running `mlflow.genai.evaluate()`, the `inputs`, `outputs`, and `expectations` parameters can be specified in the `data` argument, or parsed from the trace. ^[code-based-scorer-reference-databricks-on-aws.md]

For [Production Monitoring](/concepts/production-monitoring.md), registered scorers always parse the `inputs` and `outputs` parameters from the trace. The `expectations` parameter is not available in production monitoring contexts. ^[code-based-scorer-reference-databricks-on-aws.md]

## Outputs

Scorers can return different types of values depending on evaluation needs: simple values for straightforward assessments, or rich [Feedback](/concepts/feedback-object.md) objects for detailed evaluations with scores, rationales, and metadata. ^[code-based-scorer-reference-databricks-on-aws.md]

### Simple values

Simple values are used for straightforward pass/fail or numeric assessments. Scorers can return `int`, `float`, `bool`, or `str` types. For example, a scorer might return the word count of a response as an integer, or return `"yes"` or `"no"` to indicate whether a citation is present. ^[code-based-scorer-reference-databricks-on-aws.md]

### Rich Feedback objects

For detailed assessments, scorers can return a `Feedback` object or a list of `Feedback` objects. Each `Feedback` object can include: ^[code-based-scorer-reference-databricks-on-aws.md]

- **`value`**: The assessment score, which can be numeric, boolean, string, or other types.
- **`rationale`**: A textual explanation of the assessment.
- **`source`**: An `AssessmentSource` object indicating the source of the assessment, such as `"HUMAN"`, `"CODE"`, or `"LLM_JUDGE"`.
- **`metadata`**: Additional metadata about the assessment, such as annotator information.

When returning multiple feedback objects as a list, each feedback should have the `name` field specified. Those names are displayed as separate metrics in the evaluation results. ^[code-based-scorer-reference-databricks-on-aws.md]

## Metric naming behavior

The metric names that appear in evaluation and monitoring results follow specific rules: ^[code-based-scorer-reference-databricks-on-aws.md]

1. If the scorer returns one or more `Feedback` objects, then `Feedback.name` fields take precedence, if specified.
2. For primitive return values or unnamed `Feedback` objects, the function name (for the `@scorer` decorator) or the `Scorer.name` field (for the `Scorer` class) is used.

All metrics must have distinct names. If a scorer returns a list of `Feedback` objects, then each `Feedback` in the list must have a distinct name. ^[code-based-scorer-reference-databricks-on-aws.md]

## Error handling

When a scorer encounters an error for a trace, MLflow can capture error details and continue executing gracefully. Two approaches are available: ^[code-based-scorer-reference-databricks-on-aws.md]

- **Let exceptions propagate (recommended)**: MLflow automatically captures the exception and creates a `Feedback` object with `value` set to `None` and `error` containing the exception details, error message, and stack trace.
- **Handle exceptions explicitly**: Catch exceptions and return a `Feedback` object with `None` value and error details, optionally using `AssessmentError` for structured error reporting with error codes.

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — How to define custom scorers using the `@scorer` decorator or `Scorer` class
- [[MLflow Trace|MLflow traces]] — The complete execution trace that scorers can analyze
- [Feedback objects](/concepts/feedback-objects.md) — Rich assessment results with scores, rationales, and metadata
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — How scorers are used in production contexts
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
