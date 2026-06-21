---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c36c2f97cab0ce114aceaace2040e9a10c3b1331dd3b415b2b4dcadcac161a8
  pageDirectory: concepts
  sources:
    - query-reasoning-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - api-response-structure-for-reasoning-models
    - ARSFRM
  citations:
    - file: query-reasoning-models-databricks-on-aws.md
title: API Response Structure for Reasoning Models
description: The chat completions API response for reasoning models includes both a reasoning block (with summary text and signature) and a text block (the final answer), allowing clients to access the model's step-by-step thinking.
tags:
  - api
  - reasoning
  - databricks
  - llm-inference
timestamp: "2026-06-19T20:03:31.201Z"
---

# API Response Structure for Reasoning Models

Reasoning models extend the standard [Chat Completions API](/concepts/chat-completions-api.md) response by including a special reasoning content block that reveals the model’s step-by-step thought process before the final answer. This page describes the structure of that response, how to extract reasoning and answer text, and how reasoning blocks behave in multi-turn conversations.

## Response Object

All reasoning models accessed through the Databricks Foundation Model API return a `ChatCompletionMessage` object. The `content` field is an array of content blocks, each with a `type` property. For reasoning models, the array contains at least two blocks:

- A **reasoning** block (type `"reasoning"`) that holds the model’s internal thought process.
- A **text** block (type `"text"`) that contains the final answer.

The following is an example of a full response:

```python
ChatCompletionMessage(
    role="assistant",
    content=[
        {
            "type": "reasoning",
            "summary": [
                {
                    "type": "summary_text",
                    "text": ("The question is asking about the scientific explanation for why the sky appears blue... "),
                    "signature": ("EqoBCkgIARABGAIiQAhCWRmlaLuPiHaF357JzGmloqLqkeBm3cHG9NFTxKMyC/9bBdBInUsE3IZk6RxWge...")
                }
            ]
        },
        {
            "type": "text",
            "text": (
                "# Why the Sky Is Blue\n\n"
                "The sky appears blue because of a phenomenon called Rayleigh scattering. Here's how it works..."
            )
        }
    ],
    refusal=None,
    annotations=None,
    audio=None,
    function_call=None,
    tool_calls=None
)
```

^[query-reasoning-models-databricks-on-aws.md]

## Reasoning Content Block

The reasoning block (`type: "reasoning"`) contains a `summary` array. Each element in the array is a `summary_text` object with:

- `type`: always `"summary_text"`.
- `text`: the reasoning text (the model’s chain-of‑thought).
- `signature`: a cryptographic signature used to verify the integrity of the reasoning text.

To extract the reasoning from the API response, access `response.choices[0].message.content[0]["summary"][0]["text"]` (assuming the reasoning block is the first element). ^[query-reasoning-models-databricks-on-aws.md]

## Text Content Block

The text block (`type: "text"`) contains the final answer that the model returns after its internal reasoning. This is the visible output intended for the end user. It can be extracted as `response.choices[0].message.content[1]["text"]`. ^[query-reasoning-models-databricks-on-aws.md]

## Reasoning Across Multiple Turns

In multi-turn conversations with `databricks-claude-sonnet-4-5`, only the reasoning blocks from the **last assistant turn or tool‑use session** are visible to the model on subsequent turns and counted as input tokens. This design means:

- If you do not need the model to reason over its previous thinking, you can omit the reasoning block entirely when building the next request. Pass only the `text` content. ^[query-reasoning-models-databricks-on-aws.md]
- If you need the model to reason over its prior reasoning process (e.g., to refine or critique past steps), you must include the **full, unmodified assistant message** from the previous turn, including the reasoning block. The example below shows how to continue a thread while preserving the reasoning block: ^[query-reasoning-models-databricks-on-aws.md]

```python
assistant_message = response.choices[0].message
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"},
        {"role": "assistant", "content": text_content},         # text-only
        {"role": "user", "content": "Can you explain in a way that a 5-year-old child can understand?"},
        assistant_message,                                      # includes full reasoning block
        {"role": "user", "content": "Can you simplify the previous answer?"}
    ],
    max_tokens=20480,
    extra_body={
        "thinking": {
            "type": "enabled",
            "budget_tokens": 10240
        }
    }
)
answer = response.choices[0].message.content[1]["text"]
```

^[query-reasoning-models-databricks-on-aws.md]

## Models That Hide Reasoning Tokens

Not all reasoning models expose the reasoning block in the API response. For example, models in the OpenAI o series generate reasoning tokens internally but discard them; the final output only contains the text block. In contrast, `databricks-claude-sonnet-4-5` includes the reasoning content block as described above. ^[query-reasoning-models-databricks-on-aws.md]

## Related Concepts

- [Chat Completions API](/concepts/chat-completions-api.md) – The endpoint used to query all reasoning models.
- [Foundation Model API](/concepts/foundation-model-apis.md) – Unified API for Databricks Foundation Models.
- Reasoning Models – Overview of models with reasoning capabilities.
- Claude Sonnet 4-5 – Example model that exposes reasoning tokens.
- Multi-turn Conversations – Managing context across multiple requests.

## Sources

- query-reasoning-models-databricks-on-aws.md

# Citations

1. [query-reasoning-models-databricks-on-aws.md](/references/query-reasoning-models-databricks-on-aws-54bb3acc.md)
