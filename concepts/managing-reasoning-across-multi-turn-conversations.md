---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b997aad84c3bd25a2b550fbbfa574537c6733e60fd6ca70ef329f1dc8b930ac
  pageDirectory: concepts
  sources:
    - query-reasoning-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managing-reasoning-across-multi-turn-conversations
    - MRAMC
  citations:
    - file: query-reasoning-models-databricks-on-aws.md
title: Managing Reasoning Across Multi-Turn Conversations
description: Technique for handling reasoning blocks in multi-turn conversations where only the last assistant turn's reasoning is visible to the model; optionally omitting or including reasoning blocks depending on whether the model needs to reason over prior steps.
tags:
  - reasoning
  - conversation-management
  - llm-inference
  - databricks
timestamp: "2026-06-19T20:03:16.209Z"
---

# Managing Reasoning Across Multi-Turn Conversations

When using reasoning models like `databricks-claude-sonnet-4-5` in multi-turn conversations, special care is needed to handle reasoning tokens (also called thinking blocks) across turns. The way these tokens are passed back to the model determines whether the model can reason over its previous thought process. This page describes the behavior and provides best practices for preserving or discarding reasoning context across multiple exchanges. ^[query-reasoning-models-databricks-on-aws.md]

## How Reasoning Tokens Behave Across Turns

In the `databricks-claude-sonnet-4-5` model, only the reasoning blocks associated with the **last** assistant turn or tool-use session are visible to the model and counted as input tokens when forming the next response. Earlier reasoning blocks from previous turns are effectively ignored by the model unless explicitly included again in the message history. ^[query-reasoning-models-databricks-on-aws.md]

## Omitting Reasoning Tokens (When Not Needed)

If your application does not require the model to reason over its own prior reasoning process, you can simplify the conversation history by omitting the reasoning block entirely. When constructing the next request, include only the textual content of the assistant's response (the `text` content block) without the `reasoning` block. This reduces token usage and speeds up processing. ^[query-reasoning-models-databricks-on-aws.md]

```python
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"},
        {"role": "assistant", "content": text_content},
        {"role": "user", "content": "Can you explain in a way that a 5-year-old child can understand?"}
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
print("Answer:", answer)
```

In this example, only the `text_content` of the assistant's first response is included; the reasoning block from the first turn is discarded. ^[query-reasoning-models-databricks-on-aws.md]

## Including Reasoning Tokens (When Needed)

If your use case requires the model to reason over its previous reasoning process—for example, when building experiences that surface intermediate reasoning steps or when the model must refine its thought process—you must include the **full, unmodified** assistant message from the previous turn, including its `reasoning` block. ^[query-reasoning-models-databricks-on-aws.md]

```python
assistant_message = response.choices[0].message
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"},
        {"role": "assistant", "content": text_content},
        {"role": "user", "content": "Can you explain in a way that a 5-year-old child can understand?"},
        assistant_message,
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
print("Answer:", answer)
```

Here, `assistant_message` contains both the `text` and the `reasoning` block. By placing it in the message history before the new `user` query, the model can consider its prior reasoning when generating the next response. ^[query-reasoning-models-databricks-on-aws.md]

## Choosing the Right Approach

- **Omit reasoning blocks** when you want to reduce input token counts and do not need the model to revisit its intermediate reasoning. This is suitable for straightforward follow-up questions where the context from the previous answer text is sufficient.
- **Include reasoning blocks** when the model should build upon or correct its earlier thought process, or when you are building interactive applications that display the model's reasoning to end users. ^[query-reasoning-models-databricks-on-aws.md]

## Related Concepts

- [Foundation Model API](/concepts/foundation-model-apis.md) – The unified API used to interact with reasoning models.
- [Chat completions](/concepts/chat-completions-api.md) – The endpoint through which reasoning models are queried.
- Reasoning models – Models that produce special reasoning tokens for step-by-step thinking.
- Claude Sonnet 4-5 – The specific model mentioned for multi-turn reasoning management.
- [Thinking Budget Tokens](/concepts/thinking-budget-tokens.md) – The `budget_tokens` parameter that controls how many tokens the model can use for reasoning.
- Tool use with reasoning models – Tool-use sessions also produce reasoning blocks that need similar management.

## Sources

- query-reasoning-models-databricks-on-aws.md

# Citations

1. [query-reasoning-models-databricks-on-aws.md](/references/query-reasoning-models-databricks-on-aws-54bb3acc.md)
