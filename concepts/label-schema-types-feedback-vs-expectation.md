---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1e224b15d09ec939156d659e869e9f41cb3cccba27d2b876b6441f78d67ea4b
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - label-schema-types-feedback-vs-expectation
    - LSTFVE
    - Feedback types (Feedback vs. Expectation)
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: "Label Schema Types: Feedback vs Expectation"
description: "Two fundamental assessment types for labeling schemas: Feedback (subjective opinions, ratings, preferences) and Expectation (objective ground truth, correct answers, expected behavior)."
tags:
  - mlflow
  - schema-design
  - genai
timestamp: "2026-06-19T14:33:07.638Z"
---

# Label Schema Types: Feedback vs Expectation

**Label Schema Types: Feedback vs Expectation** are the two fundamental categories of assessments that can be collected when labeling [Traces](/concepts/traces.md) in the [Review App](/concepts/mlflow-review-app.md). Each [Labeling Schema](/concepts/labeling-schema.md) belongs to either the `feedback` type or the `expectation` type, determining whether the collected data represents subjective human judgment or objective ground truth. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

When you create a labeling session, you associate it with one or more labeling schemas. Each schema defines an assessment that is attached to a trace. The schema type controls the nature of the question shown to reviewers and how the resulting data should be interpreted. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The two types are:

- **Feedback** – Used for subjective assessments such as ratings, preferences, or opinions.
- **Expectation** – Used for objective ground truth such as correct answers, expected behavior, or required facts. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Feedback Schemas

Feedback schemas capture the reviewer’s personal evaluation of an agent’s response. Typical use cases include:

- Rating response quality on a scale (e.g., Poor, Fair, Good, Excellent).
- Selecting which issues are present in a response (e.g., factual error, inappropriate tone).
- Providing a numeric confidence score in one’s own assessment.

Because feedback is subjective, results may vary across reviewers. Feedback schemas are suitable when you want to gauge human perception of quality, tone, safety, or other qualitative attributes. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Custom Feedback Example

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical

tone_schema = schemas.create_label_schema(
    name="response_tone",
    type="feedback",
    title="Is the response tone appropriate for the context?",
    input=InputCategorical(options=["Too formal", "Just right", "Too casual"]),
    enable_comment=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Expectation Schemas

Expectation schemas capture objective ground truth that is independent of the reviewer’s personal opinion. Typical use cases include:

- Listing facts that a correct response must contain.
- Providing the expected correct answer for a given input.
- Specifying guidelines the output should adhere to.

Expectation schemas are commonly used with [Built-in LLM Judges](/concepts/built-in-llm-judges.md), which reference expectation values during automated evaluation. The data collected through expectation schemas can serve as a reference standard for comparing agent outputs. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Custom Expectation Example

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputTextList

facts_schema = schemas.create_label_schema(
    name="required_facts",
    type="expectation",
    title="What facts must be included in a correct response?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List key facts that any correct response must contain."
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Comparison Table

| Aspect                                  | Feedback                                         | Expectation                                           |
|-----------------------------------------|--------------------------------------------------|-------------------------------------------------------|
| **Nature**                              | Subjective – reflects reviewer’s opinion         | Objective – defines ground truth                      |
| **Examples**                            | Ratings, preference, safety assessment           | Correct answer, required facts, expected behavior     |
| **Use in automated evaluation**         | Can be used to train or align judges             | Referenced by built-in LLM judges                     |
| **Built-in schema names**               | No pre‑defined names for feedback                | `expected_facts`, `guidelines`, `expected_response`   |
| **Best suited for**                     | Human quality perception, tone, appropriateness  | Verifiable correctness, rule‑based checks             |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Built-in LLM Judges

MLflow provides predefined schema names that use the `expectation` type. These names (`EXPECTED_FACTS`, `GUIDELINES`, `EXPECTED_RESPONSE`) correspond to the built-in [LLM Judges](/concepts/llm-judges.md) and are used to collect ground‑truth data that those judges later consume during evaluation. You can create custom schemas with these names to ensure compatibility with the built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Choosing Between Feedback and Expectation

When designing a labeling schema, consider what you need to know about the agent’s output:

- Use **feedback** when the assessment is inherently subjective and depends on the reviewer’s judgment (e.g., “Was the tone appropriate?”).
- Use **expectation** when there is a single correct answer or a set of objective requirements that any acceptable response must satisfy (e.g., “What facts must be included?”).

Selecting the correct type ensures that the labeled data is interpreted properly in downstream tasks such as [Judge Alignment](/concepts/judge-alignment.md) and evaluation dataset creation. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Review App](/concepts/mlflow-review-app.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Human feedback collection](/concepts/mlflow-human-feedback-collection.md)
- Alignment judges with human feedback

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
