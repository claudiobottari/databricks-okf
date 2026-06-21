---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0171fb84484b6d9592f9025026ad296f96dc4ec1d8a875b46708616f3288a8f
  pageDirectory: concepts
  sources:
    - provisioned-throughput-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - log-probability-for-chat-completion
    - LPFCC
    - Log probability
  citations:
    - file: provisioned-throughput-foundation-model-apis-databricks-on-aws.md
title: Log Probability for Chat Completion
description: The logprobs parameter for chat completion tasks that provides token log probabilities for classification, model uncertainty assessment, and evaluation metrics.
tags:
  - databricks
  - inference
  - logging
timestamp: "2026-06-19T19:59:11.814Z"
---

# Log Probability for Chat Completion

**Log Probability for Chat Completion** refers to the use of the `logprobs` parameter in the [Chat Completions API](/concepts/chat-completions-api.md) to return the log probability of each token being sampled during generation. This feature is available on [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) endpoints and is used for tasks such as classification, model uncertainty assessment, and evaluation metrics. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Usage

When making a chat completion request, you can include the `logprobs` parameter to request log probabilities for the tokens in the generated output. The response then includes, for each token, its log probability under the model’s distribution at the time of generation. Databricks supports this parameter for compatible foundation models deployed via provisioned throughput endpoints. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Common Use Cases

- **Classification**: Using the log probability of a generated class token as a confidence score.
- **Model Uncertainty**: Inspecting how likely the model considers its own output to assess reliability.
- **Evaluation Metrics**: Computing metrics like perplexity or log-likelihood over generated text.

The parameter is configured at request time; see the [Chat Completions API](/concepts/chat-completions-api.md) reference for full parameter details. ^[provisioned-throughput-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Chat Completions API](/concepts/chat-completions-api.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Serving](/concepts/model-serving.md)
- [Log probability](/concepts/log-probability-for-chat-completion.md)

## Sources

- provisioned-throughput-foundation-model-apis-databricks-on-aws.md

# Citations

1. [provisioned-throughput-foundation-model-apis-databricks-on-aws.md](/references/provisioned-throughput-foundation-model-apis-databricks-on-aws-0afb43fa.md)
