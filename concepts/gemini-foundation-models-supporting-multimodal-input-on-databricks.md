---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67dabaa2252b56a58f60fd33ca6bc65a13d722569626c214ded6a7fc56e7a428
  pageDirectory: concepts
  sources:
    - query-audio-and-video-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gemini-foundation-models-supporting-multimodal-input-on-databricks
    - GFMSMIOD
  citations:
    - file: query-audio-and-video-models-databricks-on-aws.md
title: Gemini Foundation Models Supporting Multimodal Input on Databricks
description: The list of Gemini pay-per-token foundation models on Databricks that support audio and video inputs, including databricks-gemini-3-1-pro, databricks-gemini-3-pro, and others.
tags:
  - machine-learning
  - model-serving
  - gemini
  - supported-models
timestamp: "2026-06-19T20:02:10.387Z"
---

# Gemini Foundation Models Supporting Multimodal Input on Databricks

**Gemini Foundation Models Supporting Multimodal Input on Databricks** refers to the capability of specific Gemini pay-per-token foundation models available through Databricks Foundation Model APIs to process audio and video inputs alongside text. This multimodal support enables users to analyze, transcribe, summarize, and reason about media content directly through API calls. ^[query-audio-and-video-models-databricks-on-aws.md]

## Overview

Databricks provides access to Gemini foundation models that accept audio and video inputs through two API options: the [Chat Completions API](/concepts/chat-completions-api.md) and the [Google Gemini API](/concepts/google-gemini-api-on-databricks.md). Media can be provided either as a publicly accessible URL or as base64-encoded inline data. This capability is available only for pay-per-token serving endpoints, not for provisioned throughput endpoints. ^[query-audio-and-video-models-databricks-on-aws.md]

## Requirements

To use multimodal input with Gemini models on Databricks, you must meet the standard requirements for querying foundation models, including appropriate workspace configuration and authentication. You must also Install the appropriate package|install the required package for your chosen client option — either the OpenAI Python library (for the Chat Completions API) or the Google Generative AI Python library (for the Google Gemini API). ^[query-audio-and-video-models-databricks-on-aws.md]

## Input Methods

Users can supply audio and video inputs to Gemini models through two methods: ^[query-audio-and-video-models-databricks-on-aws.md]

- **URL**: Pass a publicly accessible URL to the media file. For video inputs, YouTube URLs are also supported.
- **Base64 inline data**: Encode the media file as a base64 string and pass it as a data URI (for example, `data:video/mp4;base64,<encoded_data>`).

## Chat Completions API

The Chat Completions API supports media inputs through the `video_url` and `audio_url` content types within the `messages` array. Each content item includes a `url` field that accepts either a web URL or a base64 data URI. ^[query-audio-and-video-models-databricks-on-aws.md]

For video input, use the `video_url` content type with a `video_url` object containing the `url` field. For audio input, use the `audio_url` content type with an `audio_url` object containing the `url` field. Both can appear alongside `text` content types in a single message. ^[query-audio-and-video-models-databricks-on-aws.md]

## Google Gemini API

The Google Gemini API supports media inputs through the `inlineData` (base64-encoded) and `fileData` (URL reference) structures within the `parts` array of a `Content` object. ^[query-audio-and-video-models-databricks-on-aws.md]

For video or audio input, use `fileData` with `mime_type` and `file_uri` fields for URL references, or use `inlineData` with `mime_type` and `data` fields for base64-encoded content. Both can be combined with text `Part` objects in a single request. ^[query-audio-and-video-models-databricks-on-aws.md]

## Supported Models

Audio and video inputs are supported on the following Gemini pay-per-token foundation models. See [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) for region availability. ^[query-audio-and-video-models-databricks-on-aws.md]

- `databricks-gemini-3-1-pro`
- `databricks-gemini-3-pro`
- `databricks-gemini-2-5-pro`
- `databricks-gemini-3-1-flash-lite`
- `databricks-gemini-3-flash`
- `databricks-gemini-2-5-flash`

## Limitations

Multimodal input has two primary limitations: ^[query-audio-and-video-models-databricks-on-aws.md]

- Audio and video inputs are only available on Gemini pay-per-token foundation models. Provisioned throughput endpoints are not supported.
- Multiple audio or video inputs can be included in a single request, but large files increase latency and token usage.

## Related Concepts

- [Chat Completions API](/concepts/chat-completions-api.md) — The primary API for sending multimodal requests to Gemini models.
- [Google Gemini API](/concepts/google-gemini-api-on-databricks.md) — An alternative API for sending multimodal requests using the Google Generative AI SDK.
- Query vision models — Related capability for processing image inputs.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The underlying infrastructure for serving Gemini models on Databricks.
- [Pay-per-token serving](/concepts/pay-per-token-serving-mode.md) — The billing model used for multimodal Gemini endpoints.

## Sources

- query-audio-and-video-models-databricks-on-aws.md

# Citations

1. [query-audio-and-video-models-databricks-on-aws.md](/references/query-audio-and-video-models-databricks-on-aws-744ec6c3.md)
