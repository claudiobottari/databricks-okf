---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b8c0c19ec6802baa996e3f976b236bc711ed2569aa076cd172310d913647194
  pageDirectory: concepts
  sources:
    - query-reasoning-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reasoning-tokens
  citations:
    - file: query-reasoning-models-databricks-on-aws.md
title: Reasoning Tokens
description: Special tokens that let a model 'think' through a prompt internally via step-by-step reasoning before producing visible output tokens; some models expose these tokens to users while others discard them.
tags:
  - machine-learning
  - reasoning
  - tokenization
  - llm-inference
timestamp: "2026-06-19T20:03:08.903Z"
---

# Reasoning Tokens

**Reasoning Tokens** are a special category of tokens used by reasoning-optimized foundation models to perform step-by-step internal deliberation before generating a final answer. Unlike standard input and output tokens, reasoning tokens enable the model to "think" through a prompt, breaking it down and considering different approaches to responding. ^[query-reasoning-models-databricks-on-aws.md]

## Overview

Reasoning models introduce reasoning tokens in addition to standard input and output tokens. These tokens allow the model to engage in an internal reasoning process before generating its final visible output. This capability gives foundation models enhanced abilities to tackle complex tasks that benefit from step-by-step analysis rather than immediate response generation. ^[query-reasoning-models-databricks-on-aws.md]

## Transparency and Visibility

Different model families handle reasoning tokens differently in terms of transparency. Some models, such as `databricks-claude-sonnet-4-5`, expose reasoning tokens to users, making the step-by-step thought process visible in the API response. Other models, such as the OpenAI o series, discard reasoning tokens internally and do not expose them in the final output. ^[query-reasoning-models-databricks-on-aws.md]

## API Structure

Reasoning tokens appear in the API response as content blocks with a `type` of `"reasoning"`. These blocks contain summary text with signatures that validate the reasoning output. In contrast, the model's final answer is provided in text content blocks (`"type": "text"`). ^[query-reasoning-models-databricks-on-aws.md]

### Example Response Structure

```python
ChatCompletionMessage(
    role="assistant",
    content=[
        {
            "type": "reasoning",
            "summary": [
                {
                    "type": "summary_text",
                    "text": ("The question is asking about the scientific explanation..."),
                    "signature": ("EqoBCkgIARABGAIiQAhCWRmlaLuPiHaF357JzGmloqLqkeBm3cHG9NFTxKMyC/9bBdBInUsE3IZk6RxWge...")
                }
            ]
        },
        {
            "type": "text",
            "text": ("# Why the Sky Is Blue\n\nThe sky appears blue because of...")
        }
    ]
)
```

^[query-reasoning-models-databricks-on-aws.md]

## Budget Tokens

When querying reasoning models, users can specify a `budget_tokens` parameter within the `thinking` configuration block. This parameter controls the maximum number of reasoning tokens the model can use during its internal deliberation process. Setting an appropriate budget allows balancing between reasoning depth and response speed. ^[query-reasoning-models-databricks-on-aws.md]

## Managing Reasoning Across Multi-Turn Conversations

For models like `databricks-claude-sonnet-4-5`, reasoning blocks behave differently across conversation turns. Only the reasoning blocks associated with the last assistant turn or tool-use session are visible to the model and counted as input tokens in subsequent turns. ^[query-reasoning-models-databricks-on-aws.md]

### Omitting Reasoning Tokens

If you don't need the model to reason over its prior steps, you can omit the reasoning block entirely when passing the assistant message back to the model. This approach simplifies the conversation context and reduces token usage. ^[query-reasoning-models-databricks-on-aws.md]

### Preserving Reasoning Context

If you need the model to reason over its previous reasoning process—for example, when building experiences that surface intermediate reasoning—you must include the full, unmodified assistant message, including the reasoning block from the previous turn. This preserves the reasoning context for the model to build upon. ^[query-reasoning-models-databricks-on-aws.md]

## Related Concepts

- [Foundation Model API](/concepts/foundation-model-apis.md) — The unified API for interacting with all foundation models, including reasoning models.
- [Chat Completions Endpoint](/concepts/chat-completions-api.md) — The endpoint used to query reasoning models.
- Token Budget Management — Controlling token usage for cost and performance optimization.
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — The broader category of foundation models.
- Prompt Engineering for Reasoning Models — Best practices for crafting effective prompts that leverage reasoning capabilities.

## Sources

- query-reasoning-models-databricks-on-aws.md

# Citations

1. [query-reasoning-models-databricks-on-aws.md](/references/query-reasoning-models-databricks-on-aws-54bb3acc.md)
