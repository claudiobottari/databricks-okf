---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55e47b0695f28bf861463a02af16e42f3ee4d45126b3e30255de036235dd3fda
  pageDirectory: concepts
  sources:
    - tracing-mistral-databricks-on-aws.md
  confidence: 0.75
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-tracing
    - MGT
    - Deploy agents with tracing
    - GenAI Agent Tracing
    - GenAI Tracing
    - GenAI tracing
    - Generative AI Tracing
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
    - file: tracing-mistral-databricks-on-aws.md
    - file: tracing-instructor-databricks-on-aws.md
title: MLflow GenAI Tracing
description: An MLflow subsystem that captures and visualizes the end-to-end execution traces of generative AI models and LLM API calls for debugging and observability.
tags:
  - mlflow
  - genai
  - tracing
  - observability
timestamp: "2026-06-19T23:12:38.102Z"
---

---
title: [MLflow](/concepts/mlflow.md) GenAI Tracing
summary: [MLflow](/concepts/mlflow.md)'s tracing capability for Python and TypeScript generative AI applications, offering automatic, manual, and combined instrumentation approaches. Supports tracing for popular LLM libraries including Mistral AI.
sources:
  - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  - tracing-instructor-databricks-on-aws.md
  - tracing-mistral-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:19:57.181Z"
updatedAt: "2026-06-19T10:44:59.232Z"
tags:
  - [MLflow](/concepts/mlflow.md)
  - generative-ai
  - tracing
  - mistral
aliases:
  - mlflow-genai-tracing
  - MGT
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

## [MLflow](/concepts/mlflow.md) GenAI Tracing

**MLflow GenAI Tracing** is a feature that records the sequence of operations and data flow within a generative AI application, providing observability into model calls, tool invocations, and custom logic steps during development and production use. It is part of the [MLflow](/concepts/mlflow.md) ecosystem and is designed to help developers debug, optimize, and validate complex AI workflows.

## Tracing Approaches

[MLflow](/concepts/mlflow.md) supports three approaches to instrumenting a Python or TypeScript generative AI application with [Traces](/concepts/traces.md):^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### [Automatic Tracing](/concepts/automatic-tracing.md)

The **automatic tracing** approach requires only a single line of code — `mlflow.<library>.autolog()` — to automatically capture app logic for over 20 supported libraries. This is the fastest way to get [Traces](/concepts/traces.md) working, and the recommended starting point for most applications.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### [Manual Tracing](/concepts/manual-tracing.md)

**Manual tracing** is designed for custom logic and complex workflows where full control over what gets traced is needed. It can be implemented using [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) or low-level APIs. Developers can also combine manual and [Automatic Tracing](/concepts/automatic-tracing.md) for complete coverage.^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## [Automatic Tracing](/concepts/automatic-tracing.md) with Mistral AI

[MLflow](/concepts/mlflow.md) provides built-in [Automatic Tracing](/concepts/automatic-tracing.md) for [Mistral AI](/concepts/mistral-ai-python-sdk.md) models. To enable it, call `mlflow.mistral.autolog()` before instantiating the Mistral client. This captures API calls to `client.chat.complete()` and similar methods, logging inputs, outputs, latency, and metadata as [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md).^[tracing-mistral-databricks-on-aws.md]

The following example demonstrates [Automatic Tracing](/concepts/automatic-tracing.md) with the Mistral Python SDK on Databricks:^[tracing-mistral-databricks-on-aws.md]

```python
from mistralai import Mistral
import [[mlflow|MLflow]]

# Turn on auto tracing for Mistral AI
[[mlflow|MLflow]].mistral.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] on Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/mistral-demo")

# Configure your API key
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

# Use the chat complete method
chat_response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role": "user",
            "content": "Who is the best French painter? Answer in one short sentence.",
        },
    ],
)
print(chat_response.choices[0].message)
```

## Enabling [Traces](/concepts/traces.md) on Databricks (Instructor Example)

To enable tracing on Databricks with other LLM providers, set the tracking URI to `databricks` and specify an experiment. The following example demonstrates [Automatic Tracing](/concepts/automatic-tracing.md) with the Instructor library, which integrates structured extraction with LLMs:^[tracing-instructor-databricks-on-aws.md]

```python
import instructor
from pydantic import BaseModel
from openai import OpenAI
import [[mlflow|MLflow]]

[[mlflow|MLflow]].openai.autolog()

[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/instructor-demo")

class ExtractUser(BaseModel):
    name: str
    age: int

client = instructor.from_openai(OpenAI())

res = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=ExtractUser,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(f"Name: {res.name}, Age:{res.age}")
```

In both examples, `mlflow.<library>.autolog()` automatically captures API calls to [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md), and the tracking URI is set to `databricks` for integration with the Databricks workspace.^[tracing-instructor-databricks-on-aws.md, tracing-mistral-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Assessing LLM and agent quality using judges
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizing runs and [Traces](/concepts/traces.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [Custom Judges](/concepts/custom-judges.md) — LLM-based [[scorers|Scorers]] that evaluate agent quality
- [Mistral AI](/concepts/mistral-ai-python-sdk.md) — Supported LLM provider for [Automatic Tracing](/concepts/automatic-tracing.md)

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
- tracing-instructor-databricks-on-aws.md
- tracing-mistral-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
2. [tracing-mistral-databricks-on-aws.md](/references/tracing-mistral-databricks-on-aws-6af10854.md)
3. [tracing-instructor-databricks-on-aws.md](/references/tracing-instructor-databricks-on-aws-f65fc687.md)
