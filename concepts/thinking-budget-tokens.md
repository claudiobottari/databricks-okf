---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 930790f3e0721bf779b8fba26590fa507fb210f425716686ca2135a5e7accfac
  pageDirectory: concepts
  sources:
    - query-reasoning-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - thinking-budget-tokens
    - TBT
  citations:
    - file: query-reasoning-models-databricks-on-aws.md
title: Thinking Budget Tokens
description: A configurable parameter (budget_tokens) that controls how many tokens the model can allocate to its internal reasoning/thinking process before generating the final answer.
tags:
  - reasoning
  - token-budget
  - llm-inference
  - configuration
timestamp: "2026-06-19T20:03:21.861Z"
---

## Thinking Budget Tokens

**Thinking Budget Tokens** is a parameter used with reasoning models accessed through the Databricks Foundation Model API. It controls the maximum number of tokens the model can allocate for its internal reasoning (or "thinking") process before generating the final visible answer. This parameter is specific to the chat completions endpoint when the `thinking` block is enabled. ^[query-reasoning-models-databricks-on-aws.md]

### Overview

Reasoning models, such as `databricks-claude-sonnet-4-5`, introduce special reasoning tokens in addition to standard input and output tokens. These tokens allow the model to "think" through the prompt—breaking it down and considering different response strategies—before producing the final answer. Some models expose these reasoning tokens to users, while others discard them. The `budget_tokens` parameter limits how many tokens can be spent on this internal reasoning phase. ^[query-reasoning-models-databricks-on-aws.md]

### Usage in the API

When querying a reasoning model via the chat completions endpoint, the `budget_tokens` value is specified inside the `extra_body` argument under a `thinking` object. For example:

```python
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

In this example, `budget_tokens` is set to 10240, and `max_tokens` is 20480. The `budget_tokens` value must not exceed the `max_tokens` limit, as the total token output includes both reasoning tokens and the final answer tokens. ^[query-reasoning-models-databricks-on-aws.md]

### Multi-Turn Conversations

In multi-turn conversations, only the reasoning blocks from the last assistant turn or tool-use session are visible to the model and counted as input tokens on subsequent turns. If you want the model to reason over its previous reasoning process (e.g., to refine its chain-of-thought across turns), you must include the full, unmodified assistant message—including its reasoning block—in the next request. The `budget_tokens` parameter can be set independently for each turn. ^[query-reasoning-models-databricks-on-aws.md]

### Related Concepts

- Query reasoning models – How to write query requests for reasoning models.
- [Foundation Model API](/concepts/foundation-model-apis.md) – Unified API for interacting with all foundation models.
- [Chat completions endpoint](/concepts/chat-completions-api.md) – The API endpoint used for reasoning model queries.
- Query a chat model – General guidance on chat model queries.

### Sources

- query-reasoning-models-databricks-on-aws.md

# Citations

1. [query-reasoning-models-databricks-on-aws.md](/references/query-reasoning-models-databricks-on-aws-54bb3acc.md)
