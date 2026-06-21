---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a26219f7e41ca97bb85dd5260970cb94fcdd4b009de940b124301a161c38694
  pageDirectory: concepts
  sources:
    - tracing-autogen-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-agent-workflow-termination
    - MWT
    - Agent Termination
    - Multi-Agent Workflow
  citations:
    - file: tracing-autogen-databricks-on-aws.md
      start: 28
      end: 31
    - file: tracing-autogen-databricks-on-aws.md
    - file: tracing-autogen-databricks-on-aws.md
      start: 35
      end: 37
title: Multi-Agent Workflow Termination
description: The pattern of using a TERMINATE keyword in agent messages to signal the end of a multi-agent conversation
tags:
  - autogen
  - multi-agent
  - workflow
timestamp: "2026-06-19T23:09:43.761Z"
---

## Multi-Agent Workflow Termination

**Multi-Agent Workflow Termination** refers to the mechanism by which a multi-agent conversation (such as an [AutoGen](/concepts/autogen-auto-tracing.md)-based system) stops after its task has been completed. In cooperative agent setups, one agent must signal to the others that the work is done; the termination condition determines when the conversation loop ends.

### Termination via a Keyword

In AutoGen, the standard pattern is to include a termination keyword—typically `"TERMINATE"`—in the message content. The assistant agent is instructed to return `"TERMINATE"` when the task is finished. For example, an assistant’s system message may state: ^[tracing-autogen-databricks-on-aws.md#L28-L31]

> Return `'TERMINATE'` when the task is done.

When the assistant sends a message containing the string `"TERMINATE"`, the conversation is considered complete. The termination check is implemented by setting the `is_termination_msg` parameter on an agent (commonly the [User Proxy Agent](/concepts/user-proxy-agent.md)) to a function that evaluates the message. ^[tracing-autogen-databricks-on-aws.md]

### Termination Condition Function

AutoGen’s `ConversableAgent` accepts an `is_termination_msg` callable that receives a message dictionary and returns a boolean. A typical termination condition is: ^[tracing-autogen-databricks-on-aws.md#L35-L37]

```python
is_termination_msg=lambda msg: msg.get("content") is not None
    and "TERMINATE" in msg["content"]
```

This condition ensures that:
- The message has a `content` field (not `None`).
- The `content` string contains the substring `"TERMINATE"`.

If the condition returns `True`, the agent conversation stops. No further messages are exchanged. ^[tracing-autogen-databricks-on-aws.md]

### Termination Context in Multi-Agent Workflows

Multi-agent workflows on Databricks are often instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) to capture the full conversation history. The termination event is part of the traced span data, enabling developers to review when and how the workflow ended. The example code sets `human_input_mode="NEVER"` on the [User Proxy Agent](/concepts/user-proxy-agent.md), meaning the termination is fully automated—no human intervention is required to stop the conversation. ^[tracing-autogen-databricks-on-aws.md]

### Related Concepts

- [AutoGen](/concepts/autogen-auto-tracing.md) – The agent framework that implements the termination mechanism.
- [ConversableAgent](/concepts/conversableagent.md) – The base agent class that supports `is_termination_msg`.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Captures inference [Traces](/concepts/traces.md) for multi-agent workflows, including termination events.
- Agent Termination Message – The specific message pattern used to signal task completion.

### Sources

- tracing-autogen-databricks-on-aws.md

# Citations

1. [tracing-autogen-databricks-on-aws.md:28-31](/references/tracing-autogen-databricks-on-aws-04b86736.md)
2. [tracing-autogen-databricks-on-aws.md](/references/tracing-autogen-databricks-on-aws-04b86736.md)
3. [tracing-autogen-databricks-on-aws.md:35-37](/references/tracing-autogen-databricks-on-aws-04b86736.md)
