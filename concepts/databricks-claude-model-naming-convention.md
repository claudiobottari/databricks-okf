---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7384e77f206d52081cb68fd678ce6c9dc09e1f35a9cd72f72680c46b9212b271
  pageDirectory: concepts
  sources:
    - query-with-the-anthropic-messages-api-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-claude-model-naming-convention
    - DCMNC
  citations:
    - file: query-with-the-anthropic-messages-api-databricks-on-aws.md
    - file: "from the provided list: `databricks-claude-sonnet-4-5`"
    - file: "`databricks-claude-opus-4-7`"
    - file: etc.
title: Databricks Claude Model Naming Convention
description: The naming pattern for Anthropic Claude models hosted on Databricks, using the prefix 'databricks-claude-' followed by the model tier and version (e.g., databricks-claude-sonnet-4-5).
tags:
  - model-serving
  - naming
  - anthropic
timestamp: "2026-06-19T20:05:24.273Z"
---

# Databricks Claude Model Naming Convention

The **Databricks Claude Model Naming Convention** is the standardized format used to identify Anthropic Claude models served through Databricks, particularly via the [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md) and the [Chat Completions API](/concepts/chat-completions-api.md). The convention encodes the model family, variant, and version in a single string that Databricks uses as the `model` parameter when making inference requests. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Format

The naming pattern follows the structure:

```
databricks-claude-{family}-{major}-{minor}
```

Where:
- `databricks-claude-` is the fixed prefix identifying a Databricks-hosted Claude model.
- `{family}` is the Claude model family: `opus`, `sonnet`, or `haiku`.
- `{major}` is the major version number.
- `{minor}` is the minor version number (separated by a hyphen, not a dot).

All components are lowercased and separated by hyphens. ^[from the provided list: `databricks-claude-sonnet-4-5`, `databricks-claude-opus-4-7`, etc.]

## Examples

The following model names are supported for Databricks-hosted foundation models: ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

- `databricks-claude-opus-4-7`
- `databricks-claude-opus-4-6`
- `databricks-claude-sonnet-4-6`
- `databricks-claude-sonnet-4-5`
- `databricks-claude-haiku-4-5`
- `databricks-claude-opus-4-5`
- `databricks-claude-opus-4-1`
- `databricks-claude-sonnet-4`

## Usage

When querying a Claude model via the Anthropic Messages API, you pass the full model name as the `model` parameter: ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

```python
client.messages.create(
    model="databricks-claude-sonnet-4-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "..."}],
)
```

The same convention applies when using the [Chat Completions API](/concepts/chat-completions-api.md) for Claude models. External models (e.g., those provisioned via AWS Bedrock) may have different naming formats and are not covered by this convention. ^[query-with-the-anthropic-messages-api-databricks-on-aws.md]

## Related Concepts

- [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md) – The API that uses these model names in queries.
- [Chat Completions API](/concepts/chat-completions-api.md) – Alternative unified API for all model providers.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The Databricks service that hosts these models.
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) – The full list of available models and their retirement status.
- Claude model versions – Versioning policy for Claude models on Databricks.

## Sources

- query-with-the-anthropic-messages-api-databricks-on-aws.md

# Citations

1. [query-with-the-anthropic-messages-api-databricks-on-aws.md](/references/query-with-the-anthropic-messages-api-databricks-on-aws-5094c68d.md)
2. from the provided list: `databricks-claude-sonnet-4-5`
3. `databricks-claude-opus-4-7`
4. etc.
