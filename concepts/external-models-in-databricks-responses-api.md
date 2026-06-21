---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2472eaebce542b86deca244379976182cc48d273e27bd06edabf49dd8d12f3bd
  pageDirectory: concepts
  sources:
    - query-with-the-openai-responses-api-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-models-in-databricks-responses-api
    - EMIDRA
  citations:
    - file: query-with-the-openai-responses-api-databricks-on-aws.md
title: External Models in Databricks Responses API
description: Support for externally hosted models (OpenAI provider, Azure OpenAI provider) that can be queried via the Responses API with full parameter and tool support, unlike Databricks-hosted pay-per-token models.
tags:
  - external-models
  - Azure
  - OpenAI
  - Databricks
timestamp: "2026-06-19T20:06:32.819Z"
---

# External Models in Databricks Responses API

The **External Models in Databricks Responses API** feature allows you to use OpenAI-hosted models (including those accessed via Azure OpenAI) through Databricks’ implementation of the OpenAI Responses API. This API is an alternative to the [Chat Completions API](/concepts/chat-completions-api.md) that provides additional capabilities such as custom tools and multi-step workflows. External models have broader support than Databricks’ own pay-per-token foundation models, with all Responses API parameters and tools available. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Supported External Model Providers

Databricks supports external models from the following providers through the Responses API:

- **OpenAI model provider** – Direct OpenAI endpoints.
- **Azure OpenAI model provider** – Microsoft Azure’s hosted OpenAI service.

These providers are listed in the “External models” section of the supported models documentation. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Capabilities and Limitations

External models support **all** Responses API parameters and tools, unlike Databricks-hosted pay-per-token foundation models which have certain restrictions (e.g., `store`, `previous_response_id`, `background`, and `service_tier` are not supported). For external models, you can use the full set of parameters, including:

- `tools` – custom tools, built-in tools (e.g., `apply_patch`, `shell`, `image_generation`, `web_search`, `mcp`), and traditional `function` calling.
- Multi-step workflows that chain responses.
- Any other parameter defined by the Responses API.

There are no additional limitations beyond what the OpenAI Responses API itself imposes. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Usage Example

To query an external model using the Responses API, specify the model serving endpoint name as the `model` input. The endpoint must be configured to point to an OpenAI or Azure OpenAI model. The following example uses the `databricks_openai` client:

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
response = client.responses.create(
    model="your-external-model-endpoint-name",
    input=[{"role": "user", "content": "Explain quantum computing."}],
    max_output_tokens=256
)
```

You can also use the standard OpenAI Python client or the REST API. Replace `model` with the Databricks model serving endpoint name for the external model. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Requirements

- See the general [requirements for scoring foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
- Install the appropriate client package (`databricks_openai` or `openai`) based on your preferred querying option. ^[query-with-the-openai-responses-api-databricks-on-aws.md]

## Related Concepts

- [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md) – The underlying protocol.
- [Chat Completions API](/concepts/chat-completions-api.md) – Alternative API for chatbot-style interactions.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of model serving on Databricks.
- [Pay-per-token foundation models](/concepts/pay-per-token-foundation-model-apis.md) – Databricks-hosted models with feature restrictions.
- [External Models](/concepts/external-models.md) – General concept of using third-party models on Databricks.
- Custom Tools – Supported for external models through the Responses API.

## Sources

- query-with-the-openai-responses-api-databricks-on-aws.md

# Citations

1. [query-with-the-openai-responses-api-databricks-on-aws.md](/references/query-with-the-openai-responses-api-databricks-on-aws-0558036c.md)
