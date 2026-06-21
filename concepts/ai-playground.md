---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5bef2804bacbed965e7ebc1ec50d5b01df1f8c66a0cae1e6b58689752d65cc0
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-playground
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
    - file: use-foundation-models-databricks-on-aws.md
title: AI Playground
description: A Databricks interface for interactively experimenting with supported foundation models before deploying them into production workloads.
tags:
  - databricks
  - user-interface
  - experimentation
timestamp: "2026-06-19T18:13:44.238Z"
---

```markdown
---
title: AI Playground
summary: A chat-like environment within Databricks workspaces for testing, prompting, and comparing large language models
sources:
  - deploy-models-using-model-serving-databricks-on-aws.md
  - use-foundation-models-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:59:42.065Z"
updatedAt: "2026-06-19T10:11:48.847Z"
tags:
  - llm
  - testing
  - ui
aliases:
  - ai-playground
confidence: 0.93
provenanceState: merged
inferredParagraphs: 0
---

# AI Playground

**AI Playground** is a chat-like environment within Databricks workspaces where users can test, prompt, and compare large language models (LLMs) interactively, without needing to set up separate inference infrastructure. It provides an intuitive interface for experimenting with prompts and model behavior before deploying models to production. ^[deploy-models-using-model-serving-databricks-on-aws.md, use-foundation-models-databricks-on-aws.md]

## Overview

The AI Playground allows data scientists, ML engineers, and other users to interact with supported LLMs in a conversational setting. Users can try different prompts, adjust model parameters, and compare responses from multiple models side-by-side — all from within the Databricks workspace UI. This enables rapid prototyping and prompt engineering without writing code or configuring serving endpoints. ^[deploy-models-using-model-serving-databricks-on-aws.md, use-foundation-models-databricks-on-aws.md]

## Key Features

### Interactive Chat Interface

The Playground presents a chat-like interface where users can send prompts to a selected model and view its responses in real time. This conversational format is particularly suited for testing LLMs and refining system prompts for GenAI agent applications.

### Model Comparison

Users can compare the outputs of different models on the same prompt, helping to choose the best model for a given task. This is useful for evaluating trade-offs between model quality, latency, and cost before committing to a deployment.

### Prompt Experimentation

The Playground supports iterative prompt development. Users can tweak prompts, adjust parameters such as temperature and max tokens, and immediately observe how changes affect the model's output.

## Relationship to Model Serving

AI Playground is complementary to [[Model Serving]]. While the Playground is designed for ad-hoc testing and exploration, Model Serving provides the production-grade REST API endpoints for integrating models into applications at scale. Models tested in the Playground can later be deployed via Model Serving for real-time or batch inference. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Supported Models

The AI Playground supports the same set of models available through Databricks [[Foundation Model APIs]], including [[Databricks-hosted foundation models]] such as Meta Llama, GTE-Large, and Mistral-7B, as well as any [[External models]] configured in the workspace (e.g., GPT-4 from OpenAI, Anthropic Claude). ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Use Cases

- **Prompt engineering**: Refining system prompts and few-shot examples before building an agent or deploying a model.
- **Model selection**: Comparing several models on representative inputs to determine which performs best for a specific task.
- **Rapid prototyping**: Quickly validating that a model can understand and respond to the types of queries expected in a production application.
- **Training and onboarding**: Enabling team members to become familiar with different LLMs and their capabilities without requiring API keys or code.

## Access and Availability

AI Playground is available directly within the Databricks workspace. No additional setup or account configuration is required beyond enabling the workspace for serverless compute. Workspace administrators can manage access through standard [[Unity Catalog]] permissions and [[serving endpoint ACLs]]. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [[Model Serving]] — Production deployment of LLMs and custom models as REST APIs
- [[Foundation Model APIs]] — Programmatic access to Databricks-hosted and external foundation models
- GenAI agent — AI agents that can be built and tested using the Playground
- Prompt engineering — The practice of designing effective prompts for LLMs
- [[External models]] — Third-party model endpoints governed through Databricks
- [[AI Functions]] — SQL functions for integrating model inference into analytics pipelines

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md
- use-foundation-models-databricks-on-aws.md
```

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
2. [use-foundation-models-databricks-on-aws.md](/references/use-foundation-models-databricks-on-aws-8c2af434.md)
