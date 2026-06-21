---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ddcd160519a60d072eaf7b4ec214c9cf0092e6d45cd3b8f42a2315eb81e1c879
  pageDirectory: concepts
  sources:
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predict_fn-patterns-in-mlflow-evaluation
    - PPIME
    - predict_fn Patterns
  citations:
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: predict_fn Patterns in MLflow Evaluation
description: Common patterns for defining or wrapping prediction functions used with mlflow.genai.evaluate(), including direct calls, wrappers, endpoint evaluation, and logged model evaluation.
tags:
  - mlflow
  - evaluation
  - predict_fn
timestamp: "2026-06-19T19:38:25.162Z"
---

## predict_fn Patterns in MLflow Evaluation

The `predict_fn` parameter in `mlflow.genai.evaluate()` is a callable that receives named arguments corresponding to the keys in the evaluation dataset’s `inputs` field. The function must return a dictionary whose keys are used by scorers. Different integration scenarios—such as calling a GenAI app directly, adapting existing apps, evaluating deployed endpoints, or wrapping logged models—require different `predict_fn` patterns. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Call Your App Directly

When the parameter names of your GenAI app match the keys in the evaluation dataset’s `inputs`, you can pass the app directly as `predict_fn`. This is the simplest pattern and avoids any wrapper overhead.

*Use when:* Your app’s function signature (e.g., `def my_chatbot_app(question: str)`) aligns with the dataset keys (e.g., `"inputs": {"question": "..."}`).

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety

@mlflow.trace
def my_chatbot_app(question: str) -> dict:
    response = f"I can help you with: {question}"
    return {"response": response}

eval_data = [
    {"inputs": {"question": "What is MLflow?"}},
    {"inputs": {"question": "How do I track experiments?"}}
]

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=my_chatbot_app,   # Direct reference, no wrapper needed
    scorers=[RelevanceToQuery(), Safety()]
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Wrap Your App in a Callable

If your app expects different parameter names or data structures than those in the evaluation dataset, create a wrapper function that translates between the two interfaces. This allows you to adapt arbitrary GenAI apps without modifying the app itself.

*Use when:* Parameter name mismatches exist (e.g., `user_message` vs `question`) or data format conversions are required (string to list, JSON parsing, etc.).

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety

@mlflow.trace
def customer_support_bot(user_message: str, chat_history: list = None) -> dict:
    context = f"History: {chat_history}" if chat_history else "New conversation"
    return {"bot_response": f"Helping with: {user_message}. {context}", "confidence": 0.95}

def evaluate_support_bot(question: str, history: str = None) -> dict:
    chat_history = history.split("|") if history else []
    result = customer_support_bot(user_message=question, chat_history=chat_history)
    return {"response": result["bot_response"], "confidence_score": result["confidence"]}

eval_data = [
    {"inputs": {"question": "Reset password", "history": "logged in|forgot email"}},
    {"inputs": {"question": "Track my order"}}
]

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=evaluate_support_bot,   # Wrapper handles translation
    scorers=[RelevanceToQuery(), Safety()]
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Evaluate a Deployed Endpoint

Use `mlflow.genai.to_predict_fn()` to create a `predict_fn` for any deployed endpoint — such as a Model Serving chat endpoint, a Custom Agent, or a custom endpoint. The function automatically extracts traces from tracing-enabled endpoints for full observability.

*Use when:* You want to evaluate an endpoint already deployed on Databricks without reimplementing its logic.

**Important:** The function performs a `**kwargs` pass-through. The evaluation data must match the input format your endpoint expects (e.g., `messages` for chat endpoints). Mismatches cause an error.

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery

predict_fn = mlflow.genai.to_predict_fn("endpoints:/my-chatbot-endpoint")

results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=predict_fn,
    scorers=[RelevanceToQuery()]
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

### Evaluate a Logged Model

Logged MLflow models (e.g., PyFunc or LangChain flavors) typically accept a single input parameter (like `model_inputs`), while `predict_fn` expects named parameters matching dataset keys. Wrap the model’s `predict` method in a function that unpacks the named arguments.

*Use when:* Loading a model from the Model Registry or MLflow Model Log and evaluating it with the standard evaluation harness.

**Best practice:** Load the model once outside the wrapper to avoid reloading on every evaluation call.

```python
import mlflow
from mlflow.genai.scorers import Safety

model = mlflow.pyfunc.load_model("models:/catalog.schema.chatbot@staging")

def evaluate_model(question: str) -> dict:
    return model.predict({"question": question})

results = mlflow.genai.evaluate(
    data=[{"inputs": {"question": "Tell me about MLflow"}}],
    predict_fn=evaluate_model,
    scorers=[Safety()]
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

---

### Additional Notes

- The `predict_fn` must accept keyword arguments that exactly match the keys in the `inputs` dictionary of each evaluation record. For endpoints, `mlflow.genai.to_predict_fn` handles this mapping. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]
- All `predict_fn` patterns work with the full suite of built-in and custom scorers. See [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md) for available options.
- The data input to `evaluate()` can be an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md), a list of dictionaries, a Pandas DataFrame, or a Spark DataFrame. The `predict_fn` pattern you choose is independent of the data source, except that the dataset’s `inputs` keys must align with the `predict_fn` signature.

---

### Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md)
- mlflow.genai.to_predict_fn
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [PyFunc Model Flavor](/concepts/custom-mlflow-pyfunc-model.md)
- LangChain Integration

---

### Sources

- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
