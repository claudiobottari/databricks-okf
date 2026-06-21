---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c1047705ec50a43d91755696176efeb34099489de4fe04d1984bcc3c3cfe51a
  pageDirectory: concepts
  sources:
    - provider-native-apis-databricks-on-aws.md
    - query-with-the-openai-responses-api-databricks-on-aws.md
    - web-search-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - openai-responses-api-on-databricks
    - ORA(D
    - OpenAI Responses API
    - Query with the OpenAI Responses API
  citations:
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
    - file: provider-native-apis-databricks-on-aws.md
    - file: web-search-on-databricks-databricks-on-aws.md
title: OpenAI Responses API (on Databricks)
description: Databricks-hosted access to OpenAI's Responses API for GPT-5 and GPT-4o models, supporting text and image inputs.
tags:
  - openai
  - databricks
  - api
timestamp: "2026-06-19T19:58:54.949Z"
---

# OpenAI Responses API (on Databricks)

The **OpenAI Responses API** is a provider‑native API on Databricks that provides direct access to OpenAI‑specific features beyond the unified [Chat Completions API](/concepts/chat-completions-api.md). It supports multi‑step workflows, custom tools, and built‑in platform tools for OpenAI models served through Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md). ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Overview

The Responses API is an alternative to the Chat Completions API and is compatible only with OpenAI pay‑per‑token foundation models and external models (OpenAI and Azure OpenAI model providers). For a unified API that works across all providers, Databricks recommends using the Chat Completions API. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

Available native APIs on Databricks include OpenAI Responses, [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md), and [Google Gemini API](/concepts/google-gemini-api-on-databricks.md). ^[provider-native-apis-databricks-on-aws.md]

## Requirements

- Users must meet the general requirements listed in the Score foundation models documentation. ^[query-with-the-openai-responses-api-databricks-on-aws.md]
- The appropriate client package must be installed on the cluster based on the chosen querying client option (e.g., `databricks_openai` for the Databricks‑specific client, or the standard `openai` package). ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Features

### Custom tools

Custom tools allow the model to return arbitrary string output instead of JSON‑formatted function arguments. This is useful for code generation, applying patches, or any use case requiring unstructured output. Custom tools are only supported with GPT‑5 series models (`databricks-gpt-5`, `databricks-gpt-5-1`, `databricks-gpt-5-2`, `databricks-gpt-5-4`, `databricks-gpt-5-5`, `databricks-gpt-5-5-pro`). ^[query-with-the-openai-responses-api-databricks-on-aws.md]

### Built‑in tools

Built‑in tools let the model call platform‑provided capabilities without requiring the user to implement the tool backend. These tools return structured outputs and are fully managed by Databricks. Supported built‑in tools for pay‑per‑token foundation models include:

- `function` – Traditional structured function calling
- `custom` – Custom user‑defined tools
- `apply_patch` – Code patching operations
- `shell` – Shell command execution
- `image_generation` – Image generation
- `mcp` – Model Context Protocol tools
- `web_search` – Web search on Databricks

^[query-with-the-openai-responses-api-databricks-on-aws.md]

### Web search

Web search for OpenAI models is only available through the Responses API (not through the Chat Completions API). To enable it, pass a `web_search` tool in the request. Web search is supported on all OpenAI pay‑per‑token foundation models. ^[web-search-on-databricks-databricks-on-aws.md]

## Supported models

### Databricks‑hosted foundation models (pay‑per‑token)

- `databricks-gpt-5-5-pro`
- `databricks-gpt-5-5`
- `databricks-gpt-5-4`
- `databricks-gpt-5-4-mini`
- `databricks-gpt-5-4-nano`
- `databricks-gpt-5-3-codex`
- `databricks-gpt-5-2`
- `databricks-gpt-5-2-codex`
- `databricks-gpt-5-1`
- `databricks-gpt-5-1-codex-max`
- `databricks-gpt-5-1-codex-mini`
- `databricks-gpt-5`
- `databricks-gpt-5-mini`
- `databricks-gpt-5-nano`

^[query-with-the-openai-responses-api-databricks-on-aws.md]

### External models

- OpenAI model provider
- Azure OpenAI model provider

^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Supported input types

OpenAI GPT models on Databricks accept **text** and **image** inputs. For image format and size requirements, see Query vision models. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Limitations

The following limitations apply to pay‑per‑token foundation models (external models support all Responses API parameters and tools):

- The parameters `background`, `store`, `previous_response_id`, and `service_tier` are not supported and return a 400 error if specified.
- Background processing and stored responses are not supported.
- Service tier selection is managed by Databricks.

^[query-with-the-openai-responses-api-databricks-on-aws.md]

For web search specifically:

- Web search is only available on pay‑per‑token endpoints (not provisioned throughput).
- It is not available for workspaces with HIPAA/BAA compliance enabled.
- Web search for OpenAI models is not available when cross‑region processing is disabled, unless the workspace is in an eligible geo (Americas or Europe).

^[web-search-on-databricks-databricks-on-aws.md]

## Related concepts

- [Chat Completions API](/concepts/chat-completions-api.md) – Unified API for all providers.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of model serving on Databricks.
- Function calling on Databricks – Structured function calling.
- Web search on Databricks – Grounding model responses with real‑time web data.
- GPT-5 – Primary model family for the Responses API on Databricks.
- [Provider native APIs](/concepts/provider-native-apis-databricks.md) – Overview of all native APIs available.

## Sources

- query-with-the-openai-responses-api-databricks-on-aws.md
- web-search-on-databricks-databricks-on-aws.md
- provider-native-apis-databricks-on-aws.md

# Citations

1. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
2. [provider-native-apis-databricks-on-aws.md](/references/provider-native-apis-databricks-on-aws-188451d9.md)
3. [web-search-on-databricks-databricks-on-aws.md](/references/web-search-on-databricks-databricks-on-aws-a73c2fc3.md)
