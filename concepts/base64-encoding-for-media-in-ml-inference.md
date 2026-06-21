---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 340de9fb80b91d06761e9bf353042fe4336284dd2cb46eb9c9bf71c022403a8f
  pageDirectory: concepts
  sources:
    - query-audio-and-video-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - base64-encoding-for-media-in-ml-inference
    - BEFMIMI
  citations:
    - file: query-audio-and-video-models-databricks-on-aws.md
title: Base64 Encoding for Media in ML Inference
description: The technical process of encoding local audio or video files as base64 strings for inline transmission to model serving endpoints, using Python's base64 library.
tags:
  - machine-learning
  - data-processing
  - encoding
timestamp: "2026-06-19T20:02:18.911Z"
---

## Base64 Encoding for Media in ML Inference

**Base64 Encoding for Media in ML Inference** is a technique for including audio or video data directly in API requests to machine learning models. Instead of providing a URL to an external file, the media file is encoded as a base64 string and embedded inline as a data URI. This approach is supported by Gemini foundation models on Databricks through the [Chat Completions API](/concepts/chat-completions-api.md) and the [Google Gemini API](/concepts/google-gemini-api-on-databricks.md).

### How It Works

The media file (e.g., `video.mp4` or `audio.mp3`) is read in binary mode, encoded using standard base64 encoding, and then decoded to a UTF‑8 string. The resulting string is placed in a data URI of the form `data:{mime_type};base64,{encoded_data}`. For example, a video file would be represented as `data:video/mp4;base64,AAAA...`. ^[query-audio-and-video-models-databricks-on-aws.md]

In Python, this is done using the `base64` standard library:

```python
with open("video.mp4", "rb") as f:
    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")
```

The resulting `video_b64` string is then passed to the model serving API.

### Use with Databricks Model Serving

When querying Gemini foundation models on Databricks, base64‑encoded media can be used in two ways:

1. **Chat Completions API**: Include base64 data in the `video_url` or `audio_url` content type fields within the `messages` array. The `url` field accepts either a web URL or a base64 data URI. ^[query-audio-and-video-models-databricks-on-aws.md]

2. **Google Gemini API**: Use the `inline_data` part with a `Blob` object that contains the base64‑encoded data and the correct MIME type. ^[query-audio-and-video-models-databricks-on-aws.md]

Both methods allow multiple media inputs in a single request.

### Limitations

- Base64 encoding increases the payload size by approximately 33% compared to the raw binary file, which can affect latency and token usage. ^[query-audio-and-video-models-databricks-on-aws.md]
- Supported only on Gemini pay‑per‑token foundation models; provisioned throughput endpoints do not support audio/video input. ^[query-audio-and-video-models-databricks-on-aws.md]
- Large files increase latency and token consumption, even when using base64 encoding. ^[query-audio-and-video-models-databricks-on-aws.md]

### Related Concepts

- Data URI – Format used to embed inline media in web APIs.
- [Chat Completions API](/concepts/chat-completions-api.md) – Endpoint that accepts base64‑encoded audio/video.
- Gemini Models – Supported model family for base64‑encoded media inference.
- URL-based media input – Alternative method using publicly accessible URLs.
- Token Usage in ML Inference – Impact of large inline payloads on cost and performance.

### Sources

- query-audio-and-video-models-databricks-on-aws.md

# Citations

1. [query-audio-and-video-models-databricks-on-aws.md](/references/query-audio-and-video-models-databricks-on-aws-744ec6c3.md)
