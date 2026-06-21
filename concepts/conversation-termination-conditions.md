---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b7a7fd1a3f84ce7b74163b4cdb4e2be7f3f773da349cc7ab64b987f621deadd
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-termination-conditions
    - CTC
  citations:
    - file: conversation-simulation-databricks-on-aws.md
      start: 198
      end: 204
    - file: conversation-simulation-databricks-on-aws.md
      start: 200
      end: 201
    - file: conversation-simulation-databricks-on-aws.md
      start: 202
      end: 204
title: Conversation Termination Conditions
description: Rules that stop simulated conversations when max turns are reached or the simulator detects the user's goal has been achieved.
tags:
  - mlflow
  - conversational-ai
  - simulation
timestamp: "2026-06-19T09:23:54.770Z"
---

# Conversation Termination Conditions

**Conversation Termination Conditions** define the rules that determine when a simulated conversation in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) ends. These conditions are configured as part of the [ConversationSimulator](/concepts/conversationsimulator.md) and control how many turns a synthetic user and agent exchange before evaluation stops.

## Overview

During [Conversation Simulation](/concepts/conversationsimulator.md), the simulator generates multi-turn interactions between a synthetic user (driven by an LLM) and the agent under test. Without termination conditions, conversations could run indefinitely. MLflow applies two built‑in stopping rules, evaluated after each turn, to end the conversation at a natural point. ^[conversation-simulation-databricks-on-aws.md#L198-L204]

## Termination Conditions

### Max Turns Reached

The `max_turns` parameter (set when creating the `ConversationSimulator`) places an upper limit on the number of user‑agent exchanges. For example, a simulator created with `max_turns=5` allows at most five pairs of user message and agent response. This condition prevents runaway conversations and controls evaluation cost. ^[conversation-simulation-databricks-on-aws.md#L200-L201]

### Goal Achieved

The simulator uses an LLM to check after each turn whether the user’s stated **goal** (provided in the test case) has been accomplished. Once the simulator detects goal completion, the conversation stops. This condition ensures that conversations end naturally when the agent successfully satisfies the user’s request, avoiding unnecessary turns after resolution. ^[conversation-simulation-databricks-on-aws.md#L202-L204]

## Practical Implications

- **Evaluation consistency**: Both conditions are evaluated automatically; users do not need to define custom termination logic.
- **Cost control**: Setting an appropriate `max_turns` prevents excessive LLM calls during simulation, especially for complex or open‑ended goals.
- **Realism vs. efficiency**: The “goal achieved” condition makes simulations more realistic by ending when the user’s intent is fulfilled, while `max_turns` acts as a safety net for edge cases where the simulator cannot detect goal completion.

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) – The API that accepts `max_turns` and test case definitions.
- [Conversation Simulation](/concepts/conversationsimulator.md) – The broader workflow for generating synthetic conversations.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The evaluation framework that consumes simulated conversations.
- [Test Cases for Simulation](/concepts/test-cases-for-conversation-simulation.md) – The goal, persona, and context fields that drive termination.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md:198-204](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
2. [conversation-simulation-databricks-on-aws.md:200-201](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
3. [conversation-simulation-databricks-on-aws.md:202-204](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
