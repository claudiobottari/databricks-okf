---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cee8093ff2e0e473bac1fc6bfb2b0d63aa40af22576c6a83e4d884e1af7d5d31
  pageDirectory: concepts
  sources:
    - query-audio-and-video-models-databricks-on-aws.md
    - web-search-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - google-gemini-api-integration-on-databricks
    - GGAIOD
  citations:
    - file: query-audio-and-video-models-databricks-on-aws.md
    - file: web-search-on-databricks-databricks-on-aws.md
title: Google Gemini API Integration on Databricks
description: Using the Google Gemini API client on Databricks to send media as inlineData (base64) or fileData (URL reference) within the parts array, with Databricks-specific authentication.
tags:
  - api
  - model-serving
  - gemini
timestamp: "2026-06-19T20:02:32.481Z"
---

# Google Gemini API Integration on Databricks

**Google Gemini API Integration on Databricks** enables users to interact with Google's Gemini family of multimodal foundation models through Databricks serving infrastructure. The integration supports both the Google Gemini native API and the OpenAI-compatible Chat Completions API, allowing developers to send text, audio, video, and web search-enabled prompts to Gemini models hosted on Databricks.

## Overview

The Google Gemini API on Databricks provides a unified interface for accessing Gemini foundation models through Databricks' managed model serving endpoints. Users can query models using either the native Google Gemini client library or the OpenAI-compatible API, providing flexibility for existing codebases and workflows. ^[query-audio-and-video-models-databricks-on-aws.md]

## Authentication

All requests to Gemini models on Databricks require authentication using a Databricks personal access token or service principal token. The token is passed in the `Authorization` header as a Bearer token when using the HTTP API, or as the `api_key` parameter when using the Google Gemini client library. ^[query-audio-and-video-models-databricks-on-aws.md, web-search-on-databricks-databricks-on-aws.md]

## Supported Models

Gemini models are available as pay-per-token foundation models through Databricks' [Foundation Model APIs](/concepts/foundation-model-apis.md). Audio and video inputs are supported on the following models: ^[query-audio-and-video-models-databricks-on-aws.md]

- `databricks-gemini-3-1-pro`
- `databricks-gemini-3-pro`
- `databricks-gemini-2-5-pro`
- `databricks-gemini-3-1-flash-lite`
- `databricks-gemini-3-flash`
- `databricks-gemini-2-5-flash`

## Query Methods

Two primary API paths are available for querying Gemini models:

### Chat Completions API (OpenAI-compatible)

The OpenAI-compatible [Chat Completions API](/concepts/chat-completions-api.md) allows users to pass audio and video input using `video_url` and `audio_url` content types in the `messages` array. Each content item includes a `url` field that accepts either a web URL or a base64 data URI. ^[query-audio-and-video-models-databricks-on-aws.md]

**Example — video input with Python:**

```python
import os
import base64
from openai import OpenAI

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url=DATABRICKS_BASE_URL
)

with open("video.mp4", "rb") as f:
    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="databricks-gemini-3-1-pro",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Summarize what happens."},
            {"type": "video_url", "video_url": {"url": "https://example.com/sample-video.mp4"}},
            {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}}
        ]
    }],
    max_tokens=1024
)
print(response.choices[0].message.content)
```

^[query-audio-and-video-models-databricks-on-aws.md]

### Google Gemini API (Native)

The [Google Gemini API](/concepts/google-gemini-api-on-databricks.md) uses the Google Gemini client library to pass media as `inlineData` (base64-encoded) or `fileData` (URL reference) within the `parts` array. ^[query-audio-and-video-models-databricks-on-aws.md]

**Example — audio input with Python:**

```python
from google import genai
from google.genai import types
import base64
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

with open("audio.mp3", "rb") as f:
    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.models.generate_content(
    model="databricks-gemini-3-1-pro",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part(text="Transcribe this audio and summarize."),
                types.Part(
                    file_data=types.FileData(
                        mime_type="audio/mp3",
                        file_uri="https://example.com/sample-audio.mp3",
                    )
                ),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="audio/mp3",
                        data=audio_b64,
                    )
                ),
            ],
        ),
    ],
    config=types.GenerateContentConfig(
        max_output_tokens=1024,
    ),
)
print(response.text)
```

^[query-audio-and-video-models-databricks-on-aws.md]

## Web Search Integration

Web search can be enabled for Gemini models to retrieve real-time information from the internet. For the Chat Completions API, pass `google_search` as a top-level parameter in the request body. For the native Gemini API, pass `google_search` as a tool. ^[web-search-on-databricks-databricks-on-aws.md]

**Example with Chat Completions API:**

```python
response = client.chat.completions.create(
    model="databricks-gemini-2-5-pro",
    messages=[{"role": "user", "content": "What are the best Italian restaurants in San Francisco?"}],
    extra_body={"google_search": {}}
)
```

^[web-search-on-databricks-databricks-on-aws.md]

**Example with native Gemini API:**

```python
response = client.models.generate_content(
    model="databricks-gemini-2-5-pro",
    contents=[types.Content(
        role="user",
        parts=[types.Part(text="What are the best Italian restaurants in San Francisco?")]
    )],
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())]
    ),
)
```

^[web-search-on-databricks-databricks-on-aws.md]

## Limitations

- Audio and video inputs are only available on Gemini pay-per-token foundation models. Provisioned throughput endpoints are not supported. ^[query-audio-and-video-models-databricks-on-aws.md]
- Multiple audio or video inputs can be included in a single request, but large files increase latency and token usage. ^[query-audio-and-video-models-databricks-on-aws.md]
- Web search is only available on pay-per-token foundation model endpoints. Provisioned throughput endpoints do not support web search. ^[web-search-on-databricks-databricks-on-aws.md]
- Web search is not available for workspaces with HIPAA/BAA compliance enabled. ^[web-search-on-databricks-databricks-on-aws.md]
- Web search for Gemini models is not available when cross-region processing is disabled. ^[web-search-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The managed serving infrastructure for Gemini and other models
- [Chat Completions API](/concepts/chat-completions-api.md) — OpenAI-compatible interface for model queries
- [Google Gemini API](/concepts/google-gemini-api-on-databricks.md) — Native Python client library for Gemini interactions
- Web search on Databricks — Grounding responses with real-time internet data
- [Query audio and video models](/concepts/multimodal-foundation-models.md) — Sending multimodal inputs to Gemini models
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — General model deployment and inference infrastructure

## Sources

- query-audio-and-video-models-databricks-on-aws.md
- web-search-on-databricks-databricks-on-aws.md

# Citations

1. [query-audio-and-video-models-databricks-on-aws.md](/references/query-audio-and-video-models-databricks-on-aws-744ec6c3.md)
2. [web-search-on-databricks-databricks-on-aws.md](/references/web-search-on-databricks-databricks-on-aws-a73c2fc3.md)
