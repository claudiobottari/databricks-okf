---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c40c3172927ef29c02f0a472d0c384c71905ea2060fc8ec0f832ee6be18da35
  pageDirectory: concepts
  sources:
    - query-reasoning-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reasoning-models-foundation-model-api
    - RM(MA
    - Query Reasoning Models|reasoning models
  citations:
    - file: query-reasoning-models-databricks-on-aws.md
title: Reasoning Models (Foundation Model API)
description: Foundation models optimized for step-by-step reasoning tasks, accessed via Databricks' unified chat completions endpoint, with support for revealing internal thought processes before delivering final answers.
tags:
  - machine-learning
  - foundation-models
  - reasoning
  - databricks
timestamp: "2026-06-19T20:03:37.236Z"
---

Here is the wiki page for "Reasoning Models (Foundation Model API)".

---

## Reasoning Models (Foundation Model API)

**Reasoning Models** are a class of Foundation Models offered through the Databricks [Foundation Model API](/concepts/foundation-model-apis.md) that are optimized for complex, multi-step reasoning tasks. Unlike standard chat or completion models, reasoning models introduce a structured "thinking" phase — an internal step-by-step deliberation — before producing a final answer. ^[query-reasoning-models-databricks-on-aws.md]

Reasoning gives foundation models enhanced capabilities to tackle complex tasks. Some models also provide transparency by revealing their step-by-step thought process before delivering a final answer. ^[query-reasoning-models-databricks-on-aws.md]

### Types of Reasoning Models

There are two types of reasoning models: **reasoning-only** and **hybrid**. These models use different approaches to control when and how the reasoning process is invoked. ^[query-reasoning-models-databricks-on-aws.md]

### How Reasoning Works

Reasoning models introduce special *reasoning tokens* in addition to standard input and output tokens. These tokens allow the model to "think" through the prompt, breaking it down into sub-problems and evaluating different approaches before generating a final answer as visible output tokens. ^[query-reasoning-models-databricks-on-aws.md]

The visibility of these reasoning tokens varies by model:
- Some models, like `databricks-claude-sonnet-4-5`, expose the reasoning tokens to users as content blocks in the API response.
- Other models, such as the OpenAI o-series, discard the reasoning tokens and do not expose them in the final output. ^[query-reasoning-models-databricks-on-aws.md]

### API Access

All reasoning models are accessed through the **chat completions** endpoint at `/chat/completions`, the same endpoint used for standard Chat models (Foundation Model API). You send a request using the OpenAI-compatible Python client library. ^[query-reasoning-models-databricks-on-aws.md]

The following Python snippet shows a typical request using the `databricks-claude-sonnet-4-5` model, which supports an explicit thinking block:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('YOUR_DATABRICKS_TOKEN'),
    base_url=os.environ.get('YOUR_DATABRICKS_BASE_URL')
)

response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    max_tokens=20480,
    extra_body={
        "thinking": {
            "type": "enabled",
            "budget_tokens": 10240
        }
    }
)
```

^[query-reasoning-models-databricks-on-aws.md]

The `thinking` field in `extra_body` enables the reasoning block and sets a token budget for the reasoning phase. The API response contains a structured content array with both reasoning and text content blocks. ^[query-reasoning-models-databricks-on-aws.md]

### Response Structure

The API response from a reasoning model includes a `ChatCompletionMessage` object where the `content` is an array of blocks. For models that expose reasoning, this array contains:

1. A **reasoning block** (type `"reasoning"`) with a summary field that contains the model's intermediate reasoning.
2. A **text block** (type `"text"`) containing the final answer.

```python
msg = response.choices[0].message
reasoning = msg.content[0]["summary"][0]["text"]
answer = msg.content[1]["text"]
print("Reasoning:", reasoning)
print("Answer:", answer)
```

^[query-reasoning-models-databricks-on-aws.md]

### Managing Reasoning Across Multiple Turns

For the `databricks-claude-sonnet-4-5` model in multi-turn conversations, only the reasoning blocks associated with the **last** assistant turn or tool-use session are visible to the model and counted as input tokens. ^[query-reasoning-models-databricks-on-aws.md]

- If you don't need the model to reason over its prior steps, you can **omit** the reasoning block from the assistant message and send only the text content.
- If you need the model to reason over its previous reasoning process (e.g., for experiences that surface intermediate reasoning), you must include the **full, unmodified assistant message**, including the reasoning block from the previous turn. ^[query-reasoning-models-databricks-on-aws.md]

### Related Concepts

- Chat models (Foundation Model API) — The base endpoint through which reasoning models are accessed.
- [Foundation Model API](/concepts/foundation-model-apis.md) — The unified API for interacting with all foundation models on Databricks.
- Prompt engineering — Techniques for crafting effective prompts, including for reasoning models.
- [Model Serving](/concepts/model-serving.md) — The infrastructure that hosts foundation model endpoints.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — A workload that may benefit from reasoning models.

### Sources

- query-reasoning-models-databricks-on-aws.md

# Citations

1. [query-reasoning-models-databricks-on-aws.md](/references/query-reasoning-models-databricks-on-aws-54bb3acc.md)
