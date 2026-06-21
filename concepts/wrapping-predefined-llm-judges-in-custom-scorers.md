---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43b6033729eb0a49db4139f550601f2119113a95305972b2b6de6350b2ac249b
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - wrapping-predefined-llm-judges-in-custom-scorers
    - WPLJICS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Wrapping predefined LLM judges in custom scorers
description: The pattern of wrapping MLflow's built-in LLM judge functions inside custom code-based scorers to preprocess trace data or post-process judge feedback
tags:
  - mlflow
  - evaluation
  - llm-judge
timestamp: "2026-06-18T10:57:45.331Z"
---

# Wrapping predefined LLM judges in custom scorers

**Wrapping predefined LLM judges in custom scorers** is a pattern in MLflow Evaluation for GenAI where you create a custom code-based scorer that calls one of MLflow's built-in LLM judges internally. This allows you to preprocess trace data before passing it to the judge, post-process the judge's feedback, or combine multiple judges into a single evaluation step. ^[code-based-scorer-examples-databricks-on-aws.md]

## Motivation

MLflow provides several built-in LLM judges, such as `is_context_relevant`, that evaluate specific quality dimensions of an AI application's responses. However, these judges expect inputs in a particular format. When your application's data structure differs from what the judge expects — for example, when your inputs are nested dictionaries or include additional context fields — you need a custom scorer to bridge the gap. ^[code-based-scorer-examples-databricks-on-aws.md]

Wrapping a predefined judge in a custom scorer lets you:

- Extract and transform the relevant data from your trace or evaluation input before passing it to the judge.
- Apply different judges conditionally based on user attributes or other context.
- Combine multiple judges into a single scoring step.
- Add custom error handling or fallback logic around the judge's evaluation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Basic pattern

The fundamental pattern is to define a function decorated with `@scorer` that accepts the inputs and outputs of your application, performs any necessary transformation, then calls a predefined LLM judge and returns its result.

The example below wraps the `is_context_relevant` judge to evaluate whether an assistant's response is relevant to the user's query. The `sample_app` in this example uses an `inputs` dictionary with the structure `{"messages": [{"role": ..., "content": ...}, ...]}`. The scorer extracts the content of the last user message and passes it as the `request` parameter to the relevance judge, along with the response as context. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import Trace, Feedback
from mlflow.genai.judges import is_context_relevant
from mlflow.genai.scorers import scorer
from typing import Any

@scorer
def is_message_relevant(inputs: dict[str, Any], outputs: str) -> Feedback:
    last_user_message_content = None
    if "messages" in inputs and isinstance(inputs["messages"], list):
        for message in reversed(inputs["messages"]):
            if message.get("role") == "user" and "content" in message:
                last_user_message_content = message["content"]
                break
    if not last_user_message_content:
        raise Exception("Could not extract the last user message from inputs to evaluate relevance.")
    # Call the relevance_to_query judge. It will return a Feedback object.
    return is_context_relevant(
        request=last_user_message_content,
        context={"response": outputs},
    )
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Conditional logic with guidelines

You can wrap [Guidelines judges](/concepts/guidelines-llm-judges.md) in custom scorers to apply different guidelines based on user attributes, request metadata, or other context available in the evaluation data. This enables differentiated evaluation without defining separate scorers for each case. ^[code-based-scorer-examples-databricks-on-aws.md]

For example, a custom scorer can extract a `user_tier` field from the inputs and apply different guideline sets: premium users receive evaluation against detailed, personalized guidelines, while standard users are evaluated against concise guidelines. The same `@scorer` function handles both paths by instantiating different `Guidelines` judges depending on the detected tier. ^[code-based-scorer-examples-databricks-on-aws.md]

## Using expectations with wrapped judges

When wrapping a predefined LLM judge, you can also incorporate [expectations](/concepts/expectation-vs-feedback-labels.md) — ground truth values provided in the evaluation dataset. The custom scorer receives the `expectations` parameter and can use it to validate the judge's output, compare results against expected scores, or pass expected values to the judge as additional context. ^[code-based-scorer-examples-databricks-on-aws.md]

## Error handling

When wrapping predefined judges, you can implement error handling at two levels:

- **Inside the custom scorer**: Catch exceptions from the judge call and return a `Feedback` object with an `AssessmentError` to indicate failure without halting evaluation.
- **Letting errors propagate**: If the raised exception is not caught, MLflow handles it gracefully and continues evaluation with the remaining scorers. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) — The general mechanism for defining evaluation metrics in MLflow Evaluation for GenAI
- [Predefined LLM judges](/concepts/scorers-and-llm-judges.md) — Built-in evaluation judges provided by MLflow
- [Guidelines judges](/concepts/guidelines-llm-judges.md) — LLM judges that evaluate responses against custom guidelines
- MLflow Evaluation for GenAI — The evaluation framework for generative AI applications
- [Feedback objects](/concepts/feedback-objects.md) — The data structure used to return evaluation results from scorers
- [Production monitoring with scorers](/concepts/production-monitoring-with-custom-scorer-functions.md) — Deploying custom scorers for continuous monitoring

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
