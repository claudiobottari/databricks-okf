---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bef54088d86f5fd16892cd9d706d623f245b60d4822c7b83d14728b13ca911db
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-llm-judge
    - GLJ
    - Guidelines Judge
    - Guidelines judge
    - Guidelines() Judge
    - LLM Judge|Guidelines LLM judges
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Guidelines LLM Judge
description: A pass/fail LLM-based evaluator that uses natural language criteria to assess GenAI outputs for compliance, tone, accuracy, and requirements.
tags:
  - llm-evaluation
  - mlflow
  - genai
timestamp: "2026-06-19T17:55:39.747Z"
---

# Guidelines LLM Judge

A **Guidelines LLM Judge** is a type of [LLM Judge](/concepts/llm-judges.md) that uses natural language pass/fail criteria to evaluate the outputs of a GenAI agent. Instead of scoring on a numeric scale, it checks whether the response satisfies explicit, human-readable rules such as compliance requirements, tone specifications, or factual accuracy constraints. This approach lets domain experts describe quality standards in plain language without writing code. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Guidelines judges are especially well-suited for evaluating:

- **Compliance** — e.g., "Must not include pricing information"
- **Style / tone** — e.g., "Maintain a professional, empathetic tone"
- **Requirements** — e.g., "Must include specific disclaimers"
- **Accuracy** — e.g., "Use only facts from provided context"

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Benefits

Guidelines LLM judges offer several advantages over code-based evaluation approaches:

- **Business-friendly**: Domain experts write evaluation criteria in natural language without writing code. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Flexible**: Criteria can be updated without code changes. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Interpretable**: Each evaluation returns a clear pass/fail result with a detailed rationale. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Fast iteration**: New criteria can be tested rapidly by modifying the text of the guidelines. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Types of Guidelines Judges

MLflow provides two built-in guidelines judge classes:

1. **`Guidelines()`** — Applies a single set of global guidelines uniformly to every row in an evaluation dataset or to every trace in [Production Monitoring for GenAI|production monitoring](/concepts/production-monitoring-for-genai-applications.md). It evaluates app inputs (`request`) and outputs (`response`). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
2. **`ExpectationsGuidelines()`** — Applies per-row guidelines that are labeled by domain experts in the evaluation dataset. Each row can have its own custom guidelines. This judge is available for offline evaluation only. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

For full API documentation, see the MLflow references for [`Guidelines`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Guidelines) and [`ExpectationsGuidelines`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.ExpectationsGuidelines). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## How Guidelines Judges Work

A guidelines judge uses a specially-tuned LLM to decide whether a response meets its specified criteria. The evaluation proceeds through three steps:

1. **Receive context**: The judge is given a context dictionary that typically contains keys like `request` (the app's input) and `response` (the app's output). Additional keys, such as `retrieved_documents` or `user_preferences`, can be included and referenced directly in guidelines. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
2. **Apply guidelines**: The judge reads your natural language rules, which define pass/fail conditions. The rules can reference any key from the context dictionary. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
3. **Make judgment**: The judge returns a binary pass/fail score (`"yes"` or `"no"`) along with a detailed rationale explaining why the content passed or failed each guideline. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

The return type is an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object containing `value`, `rationale`, `name`, and `error` (if evaluation failed). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Parsing of Request and Response

The `Guidelines` judge automatically extracts `request` and `response` from the provided `inputs` and `outputs` of each trace or row.

**Request parsing:**
- If `inputs` contains a `messages` key with an OpenAI-format chat array, the `request` is either the single message's `content` (when one message) or the entire array serialized to a JSON string (when multiple messages).
- Otherwise, `request` is the entire `inputs` dict serialized to JSON.

**Response parsing:**
- If `outputs` is an OpenAI-format [ChatCompletion](/concepts/chat-completions-api.md) object, `response` is the first choice's `content`.
- If `outputs` contains a `messages` key with an array of chat messages (OpenAI format), `response` is the last message's `content`.
- Otherwise, `response` is the `outputs` dict serialized to JSON.

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Example Usage

### Global Guidelines with `Guidelines()`

```python
from mlflow.genai.scorers import Guidelines
import mlflow

data = [
    {
        "inputs": {"question": "What is the capital of France?"},
        "outputs": {"response": "The capital of France is Paris."}
    },
    {
        "inputs": {"question": "What is the capital of Germany?"},
        "outputs": {"response": "The capital of Germany is Berlin."}
    }
]

english = Guidelines(
    name="english",
    guidelines=["The response must be in English"]
)

results = mlflow.genai.evaluate(
    data=data,
    scorers=[english]
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

A custom judge model can be specified via the `model` parameter using `<provider>:/<model-name>` format (e.g., `"databricks:/databricks-gpt-oss-120b"`). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Per-Row Guidelines with `ExpectationsGuidelines()`

```python
from mlflow.genai.scorers import ExpectationsGuidelines
import mlflow

data = [
    {
        "inputs": {"question": "What is the capital of France?"},
        "outputs": "The capital of France is Paris.",
        "expectations": {
            "guidelines": ["The response must be factual and concise"]
        }
    },
    {
        "inputs": {"question": "How to learn Python?"},
        "outputs": "You can read a book or take a course.",
        "expectations": {
            "guidelines": ["The response must be helpful and encouraging"]
        }
    }
]

results = mlflow.genai.evaluate(
    data=data,
    scorers=[ExpectationsGuidelines()]
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices for Writing Guidelines

Well-written guidelines are critical for accurate evaluation. The source document recommends the following:

### Reference Context Variables Directly

Include any key from your context dictionary in the guideline text. For example, if your context contains `retrieved_documents`, you can write a guideline like "The response must only include information from `retrieved_documents`". ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### General Guidelines

- **Be specific and measurable.** ✅ "The response must not include specific pricing amounts or percentages" ❌ "Don't talk about money". ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Use clear pass/fail conditions.** ✅ "If asked about pricing, the response must direct users to the pricing page" ❌ "Handle pricing questions appropriately". ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Reference context explicitly.** ✅ "The response must only use facts present in `retrieved_context`" ❌ "Be factual". ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Structure complex requirements** using bullet points within a single guideline string. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Real-World Examples

The source document provides extensive examples for two domains:

- **Customer service chatbot** — Global guidelines for tone and policy compliance, plus per-row guidelines for urgent situations (late package, subscription cancellation, duplicate charge). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Document extraction application** — Global guidelines for extraction accuracy and output format, plus per-row guidelines for specific document types (invoice, contract, medical record). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

These examples demonstrate how to define detailed, actionable criteria and how to pass per-row expectations in the `expectations.guidelines` field of the dataset. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Information About the Models Powering LLM Judges

- LLM judges may use third-party services, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of Abuse Monitoring, so no prompts or responses are stored with Azure OpenAI. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- For European Union (EU) workspaces, LLM judges use models hosted in the EU. All other regions use models hosted in the US. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- Disabling [Partner-Powered AI Features](/concepts/partner-powered-ai-features-on-databricks.md) prevents the LLM judge from calling partner-powered models. You can still use LLM judges by providing your own model. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- LLM judges are intended to help evaluate GenAI applications; their outputs should not be used to train, improve, or fine-tune an LLM. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [LLM Judge](/concepts/llm-judges.md) — The general category of LLM-based evaluators
- [Custom Judges](/concepts/custom-judges.md) — Building judges for specific needs beyond predefined criteria
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader evaluation framework
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges in production monitoring
- Align Judges with Human Feedback — Improving judge accuracy with expert annotations

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
