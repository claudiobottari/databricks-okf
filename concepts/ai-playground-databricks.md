---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f6283f570475d810ade01f67849b39565b8bc096180047eee9ca78b0806e9a2
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-playground-databricks
    - AP(
    - ai-playground-on-databricks
    - APOD
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Playground (Databricks)
description: Chat-like environment within the Databricks workspace for testing, prompting, and comparing supported large language models before deployment.
tags:
  - llm
  - testing
  - playground
  - databricks
timestamp: "2026-06-19T18:30:07.627Z"
---

# AI Playground (Databricks)

**AI Playground** is a chat-like interface within the Databricks workspace where users can test, prompt, and compare large language models (LLMs) without needing to configure a serving endpoint or write code. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

The AI Playground provides an interactive environment for experimenting with supported LLMs. It is part of Databricks’ [Model Serving](/concepts/model-serving.md) ecosystem, which offers a unified interface to deploy, govern, and query AI models. Users can interact with models through a simple chat interface to explore model behavior, test prompts, and compare outputs across different foundation models. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Key Features

- **Chat-like interface**: A conversational UI for prompting and testing LLMs. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Model comparison**: Users can test multiple models side by side to evaluate responses. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **No endpoint configuration required**: The Playground abstracts away endpoint setup, letting users focus on experimentation. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Integration with [Foundation Model APIs](/concepts/foundation-model-apis.md)**: Access to Databricks-hosted foundation models such as Meta-Llama and other supported architectures. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Use Cases

AI Playground is designed for:

- **Prompt engineering**: Rapidly iterating on prompts to find optimal phrasing for a task. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Model evaluation**: Comparing different models (e.g., Llama vs. Mistral) for a specific use case before deploying to production. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Learning and exploration**: Familiarizing yourself with LLM capabilities without writing custom code. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Prototyping**: Quickly testing whether a foundation model meets a requirement before moving to Custom Models or [External Models](/concepts/external-models.md). ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Availability

AI Playground is available within your Databricks workspace. It works with supported LLMs accessible through [Foundation Model APIs](/concepts/foundation-model-apis.md). The feature is ready to use without additional setup beyond enabling [Model Serving](/concepts/model-serving.md) in the workspace. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The underlying infrastructure for deploying and querying models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – APIs providing access to Databricks-hosted foundation models.
- [External Models](/concepts/external-models.md) – Models hosted outside Databricks (e.g., GPT-4 from OpenAI).
- Custom Models – User-defined Python models in MLflow format.
- [AI Functions](/concepts/ai-functions.md) – SQL-based functions for batch inference with LLMs.
- [MLflow](/concepts/mlflow.md) – The experiment tracking framework used for model management.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
