---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 735163254eca9223880b7f0d9eabe2018c3f1e3f0f5ae35a69d523e36f972cf2
  pageDirectory: concepts
  sources:
    - query-audio-and-video-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-multimodal-model-serving-on-databricks
    - LOMMSOD
  citations:
    - file: query-audio-and-video-models-databricks-on-aws.md
title: Limitations of Multimodal Model Serving on Databricks
description: "Constraints for audio and video inputs on Databricks: only available on Gemini pay-per-token models (not provisioned throughput), and large files increase latency and token usage."
tags:
  - machine-learning
  - model-serving
  - limitations
timestamp: "2026-06-19T20:02:10.316Z"
---

# Limitations of Multimodal Model Serving on Databricks

**Multimodal Model Serving** on Databricks enables querying audio, video, and other non-text inputs through foundation model endpoints. However, serving these modalities comes with several key limitations that users should understand before integrating them into production workflows.

## Supported Model Types

Audio and video inputs are supported only on Gemini pay-per-token foundation models. These include `databricks-gemini-3-1-pro`, `databricks-gemini-3-pro`, `databricks-gemini-2-5-pro`, `databricks-gemini-3-1-flash-lite`, `databricks-gemini-3-flash`, and `databricks-gemini-2-5-flash`. ^[query-audio-and-video-models-databricks-on-aws.md]

## Provisioned Throughput Not Supported

A significant limitation is that **provisioned throughput endpoints are not supported** for audio and video inputs. Only pay-per-token serving is available. This restricts the ability to reserve dedicated capacity for predictable workloads with media inputs. ^[query-audio-and-video-models-databricks-on-aws.md]

## Latency and Token Consumption

Multiple audio or video inputs can be included in a single request, but large files increase latency and token usage. There is no stated maximum file size, but users should expect higher response times and costs proportional to the size and number of media files submitted. ^[query-audio-and-video-models-databricks-on-aws.md]

## Input Methods and Encoding Overhead

Media can be provided as publicly accessible URLs or as base64-encoded inline data. While base64 encoding offers flexibility for local files, it adds overhead in payload size (approximately 33%) compared to raw binary, which can further increase latency and token consumption. YouTube URLs are additionally supported for video input. ^[query-audio-and-video-models-databricks-on-aws.md]

## API Compatibility

Multimodal inputs are supported through two API pathways: the Chat Completions API and the Google Gemini API. Each requires specific content type structures (e.g., `video_url`, `audio_url` in Chat Completions; `inlineData`, `fileData` in the Gemini API). The available feature set and behavior may vary depending on which API a user chooses. ^[query-audio-and-video-models-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Serving on Databricks](/concepts/foundation-model-serving-endpoints-databricks.md)
- [Chat Completions API](/concepts/chat-completions-api.md)
- [Google Gemini API](/concepts/google-gemini-api-on-databricks.md)
- Query vision models
- [Pay-per-token vs Provisioned Throughput](/concepts/pay-per-token-vs-provisioned-throughput-modes.md)
- Token Usage and Cost Estimation

## Sources

- query-audio-and-video-models-databricks-on-aws.md

# Citations

1. [query-audio-and-video-models-databricks-on-aws.md](/references/query-audio-and-video-models-databricks-on-aws-744ec6c3.md)
