---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81e0aaaf3ba3240e0faf9a853a426f97205e4577578968db1112bccd59ff7cd7
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-playground-on-databricks
    - APOD
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Playground on Databricks
description: A chat-like environment within Databricks workspaces for testing, prompting, and comparing large language models interactively before deploying them via Model Serving.
tags:
  - llm
  - testing
  - ui
timestamp: "2026-06-19T15:10:27.573Z"
---

---
title: AI Playground on Databricks
summary: A chat-like environment within Databricks for testing, prompting, and comparing supported large language models.
sources:
  - deploy-models-using-model-serving-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:11:40.108Z"
updatedAt: "2026-06-18T08:11:40.108Z"
tags:
  - databricks
  - ai-playground
  - llm
  - experimentation
aliases:
  - AI Playground
  - AI Playground on Databricks
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AI Playground on Databricks

**AI Playground** is an interactive chat-like environment within the Databricks workspace that allows users to test, prompt, and compare supported large language models (LLMs). It provides a no-code interface for rapid experimentation with LLMs before moving to production. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

The AI Playground is designed to make it easy to explore the behavior of various LLMs. Users can enter prompts, view model responses, and compare outputs from different models side by side. This helps in selecting the right model for an application, tuning prompt strategies, and understanding model capabilities without needing to write code or set up endpoints. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Usage Context

The AI Playground is part of the broader [Model Serving](/concepts/model-serving.md) ecosystem on Databricks. It is mentioned in the context of interacting with foundation models that are available through [Foundation Model APIs](/concepts/foundation-model-apis.md) (Databricks-hosted models like Meta Llama, Mistral, GTE-Large) or [External Models](/concepts/external-models.md) (third-party models hosted outside Databricks, such as GPT-4 from OpenAI). The playground serves as a quick-start tool for testing these models prior to deploying them via Model Serving endpoints. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Availability

The AI Playground is available directly from your Databricks workspace. No additional setup is required, though access to specific models in the playground may depend on workspace entitlements and the configured serverless compute enablement for Model Serving. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The unified platform for deploying AI models; the AI Playground is a companion experimentation tool.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Provides pay-per-token and provisioned throughput access to Databricks-hosted LLMs.
- [External Models](/concepts/external-models.md) – Allows integration with third-party LLM providers, which can also be tested in the AI Playground.
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) – The category of models that the playground is designed to interact with.
- Prompt Engineering – Best practices for crafting prompts, often explored in the AI Playground.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
