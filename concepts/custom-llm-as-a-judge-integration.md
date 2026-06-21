---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 019bc77d12e1b22cd9629f02963ffc98a9db4e01a9c507a1af8b37b041ff1313
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-as-a-judge-integration
    - CLI
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Custom LLM-as-a-Judge Integration
description: Using an external or custom LLM within a scorer by making API calls and parsing structured JSON output for evaluation feedback.
tags:
  - mlflow
  - llm-judge
  - evaluation
  - genai
timestamp: "2026-06-19T09:13:53.670Z"
---

# Custom LLM-as-a-Judge Integration

**Custom LLM-as-a-Judge Integration** refers to the practice of using a user-specified large language model (LLM) to evaluate the quality of outputs from another AI application. In MLflow GenAI evaluation, this is implemented through a [code-based scorer](/concepts/code-based-scorers.md) that calls an external LLM, parses its structured response, and returns a [Feedback](/concepts/feedback-object.md) object representing the judge’s assessment.

## Overview

MLflow’s evaluation framework allows developers to define arbitrary scoring logic via the `@scorer` decorator or the `Scorer` base class. A common pattern is to delegate the rating to an LLM judge – either a Databricks-hosted model or an externally hosted one – by constructing a system prompt and a user prompt that asks the judge to evaluate the original query and the AI’s response. The judge’s output is then parsed and converted into a graded feedback value. ^[code-based-scorer-examples-databricks-on-aws.md]

## Implementation

### Prompts for the Judge LLM

The developer defines two prompts:

- **System prompt**: Instructs the judge to be impartial, specifies the output format (e.g., a JSON object with keys `score` and `rationale`), and provides an example.
- **User prompt**: Includes the original user query and the AI’s response, and asks for the evaluation.

### API Call

Within the scorer function, the judge LLM is called using an OpenAI-compatible client (e.g., `DatabricksOpenAI` or a standard `openai` client). The temperature is typically set to `0.0` for more deterministic ratings. ^[code-based-scorer-examples-databricks-on-aws.md]

### Parsing the Judge’s Response

The judge LLM’s text output is parsed as JSON (e.g., with `json.loads()`), and the numerical score and textual rationale are extracted. These are used to construct a `Feedback` object. ^[code-based-scorer-examples-databricks-on-aws.md]

## Example

The following snippet (adapted from Example 5) shows a scorer that uses a custom LLM to evaluate answer quality:

```python
@scorer
def answer_quality(inputs: dict, outputs: str) -> Feedback:
    user_query = inputs["messages"][-1]["content"]
    judge_response = client.chat.completions.create(
        model="databricks-claude-sonnet-4-5",
        messages=[
            {"role": "system", "content": judge_system_prompt},
            {"role": "user", "content": judge_user_prompt.format(
                user_query=user_query, llm_response_from_app=outputs
            )},
        ],
        temperature=0.0,
    )
    judge_result = json.loads(judge_response.choices[0].message.content)
    return Feedback(
        value=int(judge_result["score"]),
        rationale=judge_result["rationale"],
        source=AssessmentSource(
            source_type=AssessmentSourceType.LLM_JUDGE,
            source_id="claude-sonnet-4-5",
        )
    )
```

The `source` field documents that the assessment came from a specific LLM judge, which is important for traceability and auditing. ^[code-based-scorer-examples-databricks-on-aws.md]

## Viewing and Editing Judge Assessments

After evaluation, the trace can be opened in the MLflow UI. The resulting assessment (named after the scorer function) shows the score, rationale, timestamp, and judge model name. If the judge assessment is incorrect, users can **edit the score** by clicking the Edit button. The new assessment supersedes the original judge assessment, and the edit history is preserved for future reference. ^[code-based-scorer-examples-databricks-on-aws.md]

## Use Cases

- **Quality scoring** on a 1–5 scale for factual accuracy, helpfulness, or safety.
- **Guidelines compliance** by wrapping a Guidelines judge inside a custom scorer that supplies different guidelines based on user attributes (see Example 10). ^[code-based-scorer-examples-databricks-on-aws.md]
- **Chained evaluation**: After an initial run with a safety judge, problematic traces can be filtered and re-evaluated with a more specific custom LLM judge (Example 9). ^[code-based-scorer-examples-databricks-on-aws.md]

## Best Practices

- **Provide a clear output format** (e.g., JSON with specified schema) in the judge’s system prompt.
- **Set temperature to 0.0** for consistent, deterministic ratings.
- **Include a `source`** in the `Feedback` object to identify which LLM model was used as the judge.
- **Validate the judge’s output** and handle parsing errors gracefully (see [Error handling in scorers](/concepts/error-handling-in-scorers.md)).

## Related Concepts

- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Feedback Object](/concepts/feedback-object.md)
- [AssessmentSource](/concepts/assessmentsource-entity.md)
- [Guidelines Judge](/concepts/guidelines-llm-judge.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md)

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
