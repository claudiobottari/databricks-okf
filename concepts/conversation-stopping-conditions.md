---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf3c343fe6a606a9d506bbc209d25bee03b1960bd5474b0404408b893b49c57d
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-stopping-conditions
    - CSC
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Conversation Stopping Conditions
description: "Rules that determine when a simulated conversation ends: reaching the max_turns limit or detecting the user's goal has been accomplished."
tags:
  - simulation
  - control-flow
  - conversational-ai
timestamp: "2026-06-19T17:52:05.448Z"
---

# Conversation Stopping Conditions

**Conversation Stopping Conditions** define the rules that terminate a simulated multi-turn conversation in MLflow's conversation simulation framework. When any one of these conditions is met, the simulation ends and no further turns are generated. ^[conversation-simulation-databricks-on-aws.md]

## Max Turns Reached

The simulation stops when the number of conversation turns exceeds the `max_turns` limit configured on the [ConversationSimulator](/concepts/conversationsimulator.md). This prevents infinite loops and bounds the length of simulated interactions. ^[conversation-simulation-databricks-on-aws.md]

## Goal Achieved

The simulation stops when the simulator detects that the simulated user's goal — as described in the test case — has been accomplished. The goal should describe the expected outcome so that the simulator can determine when the user's intent is fulfilled. ^[conversation-simulation-databricks-on-aws.md]

## Interaction Between Conditions

Conversations stop when **either** the maximum number of turns is reached **or** the goal is achieved. The first condition to be true ends the simulation. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) — The class that accepts test cases and the `max_turns` configuration.
- [Conversation Simulation](/concepts/conversationsimulator.md) — The overall feature for synthetic multi‑turn testing.
- Test Cases — The goals and personas that drive the simulated user's behavior.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that consumes simulated conversations.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
