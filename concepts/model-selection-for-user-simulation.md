---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80af6e0fa07020edd9e9ec35c74877372816653fea4370224749f2c48a29f824
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-selection-for-user-simulation
    - MSFUS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Model Selection for User Simulation
description: Choosing which LLM powers the simulated user in conversation simulation via the user_model parameter, supporting provider-prefixed model formats (e.g., 'anthropic:/claude-sonnet-4-20250514'), with specific data residency and privacy considerations for Azure OpenAI and EU workspaces.
tags:
  - mlflow
  - llm
  - privacy
  - conversational-ai
timestamp: "2026-06-19T14:25:50.321Z"
---

# Model Selection for User Simulation

**Model Selection for User Simulation** refers to choosing the appropriate LLM (large language model) to generate realistic user interactions during synthetic conversation simulation. The choice of user model directly impacts the quality, diversity, and fidelity of simulated conversations used for testing conversational AI agents.

## Overview

When using [Conversation Simulation](/concepts/conversation-simulation.md) to generate synthetic multi-turn conversations, a user simulation LLM generates realistic user messages that drive the conversation toward defined goals. Selecting the right model affects how naturally the simulated user behaves, how well it follows the defined persona, and how effectively it pursues the conversation goal. ^[conversation-simulation-databricks-on-aws.md]

## Configuration

The user model is specified via the `user_model` parameter when creating a `ConversationSimulator`. The parameter follows the format `"<provider>:/<model>"`, where provider indicates the model hosting service and model identifies the specific LLM to use. ^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7,  # Passed to the user simulation LLM
)
```

Additional LLM parameters such as `temperature` can be passed to control the variability of simulated user responses. ^[conversation-simulation-databricks-on-aws.md]

## Supported Model Providers

The [MLflow GenAI](/concepts/mlflow-3-for-genai.md) platform supports multiple model providers for user simulation. Model formats follow the pattern `"<provider>:/<model>"`. For the full list of supported providers, refer to the [MLflow documentation on supported models](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/custom-judges/supported-models). ^[conversation-simulation-databricks-on-aws.md]

## Model Hosting and Regional Considerations

LLM-based conversation simulation may use third-party services to simulate user interactions, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of Abuse Monitoring, so no prompts or responses are stored with Azure OpenAI. ^[conversation-simulation-databricks-on-aws.md]

Regional hosting differs based on workspace location:

- **European Union (EU) workspaces**: Conversation simulation uses models hosted in the EU.
- **All other regions**: Conversation simulation uses models hosted in the US.

^[conversation-simulation-databricks-on-aws.md]

## Disabling Partner-Powered AI Features

If the workspace disables Partner-powered AI features, conversation simulation cannot call partner-powered models. In this case, you can still use conversation simulation by providing your own model using a supported provider. ^[conversation-simulation-databricks-on-aws.md]

## Selection Criteria

### Model Quality and Capabilities

- **Persona adherence**: The model should faithfully follow the persona definition, including technical expertise level, communication style, and emotional state.
- **Goal pursuit**: The model should naturally drive the conversation toward the specified goal without being overly directive or losing focus.
- **Turn coherence**: The model should maintain conversational context across multiple turns and respond appropriately to agent replies.

### Performance Considerations

- **Latency**: Faster models reduce total simulation time, especially for large test suites with multiple conversation turns.
- **Cost**: Different providers and models have varying pricing structures that should be considered for large-scale simulation runs.
- **Throughput**: The model's API rate limits and concurrent request handling affect how quickly simulations complete.

### Use Case Examples

| Scenario | Recommended Model Consideration | Rationale |
|----------|-------------------------------|-----------|
| Red-teaming | More capable, creative model | Better at exploring edge cases and adversarial scenarios |
| Beginner user simulation | Instruction-following model | More likely to ask for guidance and follow step-by-step |
| Technical support testing | Domain-capable model | Can generate realistic technical questions and follow-ups |
| Large-scale regression testing | Lower-cost, faster model | Enables running many test cases efficiently |

## Related Concepts

- [Conversation Simulation](/concepts/conversation-simulation.md) — The overall workflow for generating synthetic conversations
- Persona — User characteristics and communication style for simulation
- Goal — The desired outcome driving simulated user behavior
- Test Cases — Input definitions for simulated conversations
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — Platform for agent evaluation and monitoring
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers for evaluating agent quality
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost control for serverless workloads including simulation

## Best Practices

1. **Match model to persona complexity**: Simpler personas may work well with smaller, faster models, while complex personas with nuanced behavior typically require more capable models.
2. **Test with multiple models**: Evaluate different user models to find the best fit for your specific use case and domain.
3. **Consider regional requirements**: Choose a provider and model consistent with your data residency and compliance needs.
4. **Balance quality and cost**: For large-scale testing, consider using a more capable model for a smaller representative set and a faster model for regression suites.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
