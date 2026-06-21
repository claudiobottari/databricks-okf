---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00919d41d4b08a9a1eac7eeebd5ad27b310f205f6d6eec436de3bf5f3404dbfd
  pageDirectory: concepts
  sources:
    - query-reasoning-models-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reasoning-only-vs-hybrid-models
    - RVHM
  citations:
    - file: query-reasoning-models-databricks-on-aws.md
title: Reasoning-Only vs Hybrid Models
description: Classification of reasoning models into reasoning-only (dedicated reasoning models) and hybrid (models that can toggle reasoning on/off), controlling how step-by-step thinking is enabled during inference.
tags:
  - machine-learning
  - reasoning
  - model-types
timestamp: "2026-06-19T20:02:59.240Z"
---

# Reasoning-Only vs Hybrid Models

**Reasoning-Only vs Hybrid Models** describes a classification of foundation models that have been optimized for reasoning tasks. Reasoning models use special [Reasoning Tokens](/concepts/reasoning-tokens.md) to let the model "think" through a complex prompt before delivering a final answer. The two categories—reasoning-only and hybrid—differ in how they control the use of reasoning capabilities. ^[query-reasoning-models-databricks-on-aws.md]

## Reasoning-Only Models

Reasoning-only models are designed exclusively for tasks that require step-by-step deliberation. They always apply reasoning tokens internally and do not offer a mode to bypass the reasoning process. The model's output may or may not expose the reasoning tokens to the user, depending on the specific model implementation. For example, the OpenAI o series discards reasoning tokens and does not reveal them in the final output. ^[query-reasoning-models-databricks-on-aws.md]

## Hybrid Models

Hybrid models can operate either as a reasoning model or a standard [chat completion model](/concepts/chat-completions-api.md). They allow the caller to decide whether to enable reasoning on a per-request basis. Typically, the caller provides a `thinking` block in the request body to activate reasoning and set a budget for the number of reasoning tokens. An example is `databricks-claude-sonnet-4-5`, which displays reasoning tokens in the API response when reasoning is enabled. ^[query-reasoning-models-databricks-on-aws.md]

## How Reasoning Models Work

Both types of models introduce special reasoning tokens in addition to standard input and output tokens. These tokens allow the model to break down the prompt, consider different approaches, and generate an internal chain of thought. After this internal reasoning process, the model produces its final answer as visible output tokens. Some models, like `databricks-claude-sonnet-4-5`, expose the reasoning tokens in the API response, while others, such as the OpenAI o series, discard them after use. ^[query-reasoning-models-databricks-on-aws.md]

## Key Differences

| Feature | Reasoning-Only | Hybrid |
|---------|---------------|--------|
| Reasoning mode | Always enabled | Selectable per request |
| Request control | Not available | `thinking` block with `enabled` and `budget_tokens` |
| Token exposure in response | Varies by model (e.g., discarded by OpenAI o series) | Exposed by models like `databricks-claude-sonnet-4-5` |

^[query-reasoning-models-databricks-on-aws.md]

## Querying Reasoning Models

All reasoning models—whether reasoning-only or hybrid—are accessed through the [chat completions endpoint](/concepts/chat-completions-api.md) via the [Foundation Model API](/concepts/foundation-model-apis.md). The API endpoint and authentication are the same as for standard chat models. Hybrid models require an `extra_body` parameter with a `thinking` object to activate reasoning and set the token budget. ^[query-reasoning-models-databricks-on-aws.md]

## Related Concepts

- [Foundation Model API](/concepts/foundation-model-apis.md)
- [Chat completions endpoint](/concepts/chat-completions-api.md)
- [Reasoning Tokens](/concepts/reasoning-tokens.md)
- [Thinking Budget Tokens](/concepts/thinking-budget-tokens.md)
- Claude Sonnet 4.5 on Databricks

## Sources

- query-reasoning-models-databricks-on-aws.md

# Citations

1. [query-reasoning-models-databricks-on-aws.md](/references/query-reasoning-models-databricks-on-aws-54bb3acc.md)
