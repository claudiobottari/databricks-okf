---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 186952dbbcb45176cb35ead485dbf3e81724a82c6de3af280bb380936214eed5
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-selection-for-conversation-simulation
    - MSFCS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Model Selection for Conversation Simulation
description: Configuring which LLM powers the simulated user, including provider format patterns, region-specific hosting for EU vs US, and the ability to disable partner-powered models.
tags:
  - mlflow
  - LLM
  - configuration
timestamp: "2026-06-19T17:52:07.603Z"
---

# Model Selection for Conversation Simulation

**Model selection for conversation simulation** refers to choosing the large language model (LLM) that generates realistic user messages during synthetic multi-turn conversations in MLflow. The simulator uses an LLM to act as the simulated user, responding to the agent under test based on defined goals and personas.^[conversation-simulation-databricks-on-aws.md]

## Default Model Behavior

By default, the `ConversationSimulator` uses a built-in model to generate user messages. The specific default model depends on the workspace region:^[conversation-simulation-databricks-on-aws.md]

- For **European Union (EU) workspaces**, conversation simulation uses models hosted in the EU.
- All **other regions** use models hosted in the US.

These models are provided through partner-powered AI services. For Azure OpenAI, Databricks has opted out of Abuse Monitoring, so no prompts or responses are stored with Azure OpenAI.^[conversation-simulation-databricks-on-aws.md]

## Custom Model Selection

You can specify a different model for the simulated user using the `user_model` parameter when creating the `ConversationSimulator`:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import ConversationSimulator

simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7,  # Passed to the user simulation LLM
)
```

^[conversation-simulation-databricks-on-aws.md]

## Supported Model Formats

Model identifiers follow the pattern `"<provider>:/<model>"`. The following providers are supported:^[conversation-simulation-databricks-on-aws.md]

| Provider Prefix | Example |
|---|---|
| `anthropic:/` | `anthropic:/claude-sonnet-4-20250514` |
| `openai:/` | `openai:/gpt-4o-mini` |
| `databricks:/` | `databricks:/databricks-meta-llama-3-1-70b-instruct` |
| `azure-openai:/` | `azure-openai:/deployment-name` |
| `bedrock:/` | `bedrock:/anthropic.claude-v2` |

See the [MLflow documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/custom-judges/supported-models) for the full list of supported providers.^[conversation-simulation-databricks-on-aws.md]

## Passing Parameters to the Simulation Model

Additional parameters can be passed to the user simulation LLM using keyword arguments in the `ConversationSimulator` constructor:^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="openai:/gpt-4o-mini",
    temperature=0.7,
    max_tokens=256,
)
```

These parameters are forwarded to the underlying LLM provider's API.^[conversation-simulation-databricks-on-aws.md]

## Disabling Partner-Powered Models

Disabling **Partner-powered AI features** prevents the conversation simulator from calling partner-powered models. If partner-powered models are disabled, you can still use conversation simulation by providing your own model via the `user_model` parameter.^[conversation-simulation-databricks-on-aws.md]

## When to Use a Custom Model

Consider using a custom model for the simulated user when:^[conversation-simulation-databricks-on-aws.md]

- **Testing different user interaction patterns**: A more advanced model can simulate more nuanced or adversarial user behaviors for red-teaming scenarios.
- **Meeting data residency requirements**: You can select a model hosted in a specific region to comply with data governance policies.
- **Partners are disabled**: If Partner-powered AI features are turned off, you must provide your own model.
- **Controlling cost**: You can choose a smaller or less expensive model for routine test scenarios.
- **Improving consistency**: Lowering the `temperature` parameter produces more deterministic and repeatable user simulations.

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) — The class that orchestrates synthetic multi-turn conversations
- Red-teaming — Stress-testing agents with diverse user behaviors at scale
- [Test Cases for Conversation Simulation](/concepts/test-cases-for-conversation-simulation.md) — Defining goals, personas, and context for simulated conversations
- Predict function for agents — The function interface for the agent under test
- [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) — Controls for partner-hosted model services

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
