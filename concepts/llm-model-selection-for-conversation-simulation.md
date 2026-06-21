---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d61fd33b1eecb5b47bf692823f2952257a308205f703f062375125666fc584b
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-model-selection-for-conversation-simulation
    - LMSFCS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: LLM Model Selection for Conversation Simulation
description: Configuring which LLM powers the simulated user in conversation simulation, supporting provider-prefixed model names and regional hosting constraints.
tags:
  - mlflow
  - llm
  - configuration
  - conversational-ai
timestamp: "2026-06-19T09:23:52.349Z"
---

# LLM Model Selection for Conversation Simulation

**LLM Model Selection for Conversation Simulation** refers to the choice of underlying language model used by the [ConversationSimulator](/concepts/conversationsimulator.md) to generate realistic user utterances during synthetic multi-turn conversations. The selection determines the quality, cost, latency, and privacy characteristics of the simulated interactions.

## Overview

The `ConversationSimulator` in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) uses a large language model (LLM) to simulate the end-user side of a conversation. By default, a system-chosen model is used, but practitioners can override this to control fidelity, response style, or deployment constraints. ^[conversation-simulation-databricks-on-aws.md]

## Specifying a Custom Model

The simulation model is set via the `user_model` parameter when constructing a `ConversationSimulator`. The value must follow the format `"<provider>:/<model>"`. Additional generation parameters (e.g., `temperature`) can be passed to the user simulation LLM. ^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7,
)
```

## Supported Providers

Models are referenced by a provider prefix followed by a colon and a forward slash. Supported providers include (but are not limited to) those listed in the [MLflow custom judge supported models documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/custom-judges/supported-models). ^[conversation-simulation-databricks-on-aws.md]

Commonly used provider patterns include:

- `openai:/gpt-4o-mini`
- `anthropic:/claude-sonnet-4-20250514`
- `databricks:/databricks-meta-llama-3-1-405b-instruct`

## Regional Hosting and Data Privacy

LLM-based conversation simulation may leverage third-party services such as Azure OpenAI operated by Microsoft. Databricks has opted out of Abuse Monitoring for Azure OpenAI, meaning no prompts or responses are stored with Azure OpenAI. ^[conversation-simulation-databricks-on-aws.md]

For European Union (EU) workspaces, simulation models are hosted within the EU. All other regions use models hosted in the United States. ^[conversation-simulation-databricks-on-aws.md]

## Disabling Partner-Powered AI

If the workspace has **Partner-powered AI features** disabled, conversation simulation will not be able to call partner-hosted models. In that case, users must provide their own model via the `user_model` parameter to continue using the simulator. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) – The class that orchestrates synthetic conversation generation.
- GenAI Agent Evaluation – The broader evaluation workflow that includes simulation.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework for building and evaluating generative AI applications.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that can evaluate simulated conversations.
- Generate Test Cases from Conversations – Creating test scenarios from production data.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
