---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 633fe8f6fbb7d7205991cabe3ddd516b6d668422e624631fc5a965415a35d66f
  pageDirectory: concepts
  sources:
    - tracing-gemini-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-concepts-and-workflow
    - Workflow and MLflow Tracing Concepts
    - MTCAW
    - Tracing Concepts
  citations:
    - file: tracing-gemini-databricks-on-aws.md
title: MLflow Tracing Concepts and Workflow
description: The tracing workflow includes understanding how MLflow captures and organizes trace data, using the Trace UI to analyze application behavior, and setting up quality assessment for Gemini-powered applications.
tags:
  - mlflow
  - tracing
  - workflow
  - observability
timestamp: "2026-06-19T23:11:58.658Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Concepts and Workflow

**MLflow Tracing** is a feature that automatically captures and logs detailed information about GenAI model invocations, enabling observability, debugging, and quality assessment of AI applications. When enabled, [MLflow](/concepts/mlflow.md) records [Traces](/concepts/traces.md) — structured records of API calls — and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-gemini-databricks-on-aws.md]

## Core Concepts

### [Traces](/concepts/traces.md)

A **trace** is a record of a single invocation of a GenAI model or service. Each trace captures the inputs (prompts), outputs (completions), latency, model name, and additional metadata such as `temperature` and `max_tokens` if specified. [Traces](/concepts/traces.md) can also capture function calling responses and any exceptions that are raised. ^[tracing-gemini-databricks-on-aws.md]

### Nested [Traces](/concepts/traces.md)

[MLflow Tracing](/concepts/mlflow-tracing.md) supports **nested traces**, meaning that when a GenAI SDK call triggers sub-calls (for example, a multi-turn conversation or a chain of tool calls), each sub-call is captured as a child trace within the parent trace. This provides a hierarchical view of the application's execution flow. ^[tracing-gemini-databricks-on-aws.md]

### Autologging

**Autologging** is the mechanism by which [MLflow](/concepts/mlflow.md) automatically enables tracing for a specific GenAI SDK. For example, calling `mlflow.gemini.autolog()` enables [Automatic Tracing](/concepts/automatic-tracing.md) for all Google Gemini SDK calls made within the same Python process. ^[tracing-gemini-databricks-on-aws.md]

## Workflow

### 1. Enable Autologging

To begin tracing, call the autolog function for the desired integration before making any SDK calls. For Gemini:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].gemini.autolog()
```

^[tracing-gemini-databricks-on-aws.md]

### 2. Configure Tracking

Set the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) and experiment where [Traces](/concepts/traces.md) will be logged:

```python
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/gemini-demo")
```

^[tracing-gemini-databricks-on-aws.md]

### 3. Make SDK Calls

After autologging is enabled, any supported SDK call is automatically traced. For example, a single text generation call:

```python
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="The opposite of hot is"
)
```

^[tracing-gemini-databricks-on-aws.md]

### 4. View [Traces](/concepts/traces.md)

[Traces](/concepts/traces.md) are logged to the active [MLflow Experiment](/concepts/mlflow-experiment.md) and can be viewed in the [MLflow](/concepts/mlflow.md) UI. The Trace UI provides tools to analyze latency, inspect inputs and outputs, and debug application behavior. ^[tracing-gemini-databricks-on-aws.md]

## Supported Capabilities

[MLflow Tracing](/concepts/mlflow-tracing.md) captures the following information for each traced call:

- **Prompts and completion responses** — The full input text and the model's generated output
- **Latencies** — The time taken for each API call
- **Model name** — The identifier of the model used (e.g., `gemini-1.5-flash`)
- **Additional metadata** — Parameters such as `temperature` and `max_tokens`, if specified
- **Function calling** — Any function calling responses returned by the model
- **Exceptions** — Any errors raised during the call

^[tracing-gemini-databricks-on-aws.md]

### Multi-turn Conversations

[MLflow](/concepts/mlflow.md) supports tracing multi-turn chat interactions. Each message sent in a chat session is captured as part of the trace:

```python
chat = client.chats.create(model='gemini-1.5-flash')
response = chat.send_message("In one sentence, explain how a computer works to a young child.")
response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?")
```

^[tracing-gemini-databricks-on-aws.md]

### Embeddings

Tracing also supports [Embeddings API](/concepts/embeddings-api.md) calls:

```python
result = client.models.embed_content(model="text-embedding-004", contents="Hello world")
```

^[tracing-gemini-databricks-on-aws.md]

## Limitations

- On serverless compute clusters, autologging is **not automatically enabled**. You must explicitly call the autolog function (e.g., `mlflow.gemini.autolog()`) to enable tracing. ^[tracing-gemini-databricks-on-aws.md]
- For the Gemini integration, only **synchronous calls** for text interactions are traced. Async APIs are not traced. ^[tracing-gemini-databricks-on-aws.md]
- Full inputs may not be recorded for **multi-modal inputs** (e.g., images or audio). ^[tracing-gemini-databricks-on-aws.md]

## Disabling Autologging

Auto tracing can be disabled globally by calling:

```python
[[mlflow|MLflow]].gemini.autolog(disable=True)
# or
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-gemini-databricks-on-aws.md]

## Next Steps

After enabling tracing, you can:

- **Debug and observe your app** — Use the Trace UI to analyze your application's behavior
- **Evaluate your app's quality** — Set up quality assessment for your GenAI-powered application

^[tracing-gemini-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where [Traces](/concepts/traces.md) are logged
- [MLflow Autologging](/concepts/mlflow-autologging.md) — The mechanism that enables [Automatic Tracing](/concepts/automatic-tracing.md)
- [Google Gemini SDK](/concepts/google-gemini-api-on-databricks.md) — The GenAI SDK supported by this tracing integration
- Trace UI — The interface for viewing and analyzing [Traces](/concepts/traces.md)
- [GenAI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — Quality assessment workflows that build on tracing data

## Sources

- tracing-gemini-databricks-on-aws.md

# Citations

1. [tracing-gemini-databricks-on-aws.md](/references/tracing-gemini-databricks-on-aws-52fc6461.md)
