---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 017d8ddd73364c8e0a2f8fa03179a17cb376392bab91df54c6a70477c04f8302
  pageDirectory: concepts
  sources:
    - query-with-the-google-gemini-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - google-genai-sdk-custom-endpoint-configuration
    - GGSCEC
  citations:
    - file: query-with-the-google-gemini-api-databricks-on-aws.md
      start: 7
      end: 24
title: Google GenAI SDK Custom Endpoint Configuration
description: Using the google.genai Python SDK with custom base_url and headers in http_options to route API calls through a Databricks serving endpoint instead of directly to Google.
tags:
  - google-genai
  - sdk
  - configuration
  - python
timestamp: "2026-06-19T20:06:10.294Z"
---

# Google GenAI SDK Custom Endpoint Configuration

**Google GenAI SDK Custom Endpoint Configuration** refers to the process of configuring the Google GenAI SDK to route API requests through a custom endpoint rather than using the default Google Cloud endpoint. This is particularly useful when deploying Google Gemini models through an alternative serving infrastructure, such as a Databricks serving endpoint.

## Overview

The Google GenAI Client SDK (`google.genai`) supports an `http_options` configuration which allows developers to specify a custom base URL and headers for API requests. This enables the SDK to be pointed at alternative model serving platforms, such as a Databricks serving endpoint, rather than the default Google API endpoint. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]

## Configuration

To configure a custom endpoint, provide an `HttpOptions` object with the desired `base_url` when creating the `genai.Client`. The `base_url` should point to the URL of the serving endpoint that hosts the Gemini model. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]

Custom headers, such as an `Authorization` header, can be passed via the `headers` dictionary within the `HttpOptions` to authenticate with the serving endpoint. The example uses a `Bearer` token for authentication. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]

### Example

The following example demonstrates configuring the Google GenAI SDK to use a Databricks serving endpoint at `https://example.staging.cloud.databricks.com/serving-endpoints/gemini`: ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]

```python
from google import genai
from google.genai import types
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = genai.Client(
    api_key="databricks",
    http_options=types.HttpOptions(
        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",
        headers={
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        },
    ),
)

response = client.models.generate_content(
    model="databricks-gemini-2-5-pro",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part(text="What is a mixture of experts model?")],
        ),
    ],
    config=types.GenerateContentConfig(
        max_output_tokens=256,
    ),
)

print(response.text)
```

## Key Components

The following components are part of the custom endpoint configuration:

- **`api_key`**: The API key used for authentication with the endpoint. When using a Databricks serving endpoint, the value `"databricks"` is used. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]
- **`http_options`**: An instance of `types.HttpOptions` that contains the custom endpoint configuration, including `base_url` and `headers`. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]
- **`base_url`**: The URL of the custom serving endpoint, such as a Databricks model serving endpoint. This replaces the default Google API URL. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]
- **`headers`**: A dictionary of HTTP headers to include in requests. Commonly used for authentication, such as a `Bearer` token. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]

## Model Specification

When using a custom endpoint, the `model` parameter in the `generate_content` call specifies the model name as it is recognized by the serving endpoint. In the example above, the model is referenced as `"databricks-gemini-2-5-pro"` which is the name registered at the Databricks serving endpoint. ^[query-with-the-google-gemini-api-databricks-on-aws.md:7-24]

## Use Cases

Custom endpoint configuration is essential in environments where:

- The Google Gemini API is accessed through a proxy or intermediary serving layer.
- Model serving is managed through a private or on-premises infrastructure.
- Authentication and routing must be controlled through custom headers.

## Related Concepts

- Google GenAI SDK — The software development kit for interacting with Google's generative AI models.
- [Google Gemini API](/concepts/google-gemini-api-on-databricks.md) — The API for accessing Google Gemini models.
- [Model Serving](/concepts/model-serving.md) — The process of deploying and running machine learning models for inference.
- Serving Endpoint — A URL that provides access to a deployed model.

## Sources

- query-with-the-google-gemini-api-databricks-on-aws.md

# Citations

1. [query-with-the-google-gemini-api-databricks-on-aws.md:7-24](/references/query-with-the-google-gemini-api-databricks-on-aws-8dbd37cc.md)
