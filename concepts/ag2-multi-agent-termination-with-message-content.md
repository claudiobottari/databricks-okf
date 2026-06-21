---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dc770ac761748be64ad62ed9bf167afe9e0fa98f946e746f63f866de4f9123a
  pageDirectory: concepts
  sources:
    - tracing-ag2-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ag2-multi-agent-termination-with-message-content
    - AMTWMC
  citations:
    - file: tracing-ag2-databricks-on-aws.md
title: AG2 Multi-Agent Termination with Message Content
description: A pattern where a conversational agent workflow terminates when a specific string (e.g., 'TERMINATE') appears in a message's content, controlled via the is_termination_msg callback.
tags:
  - ag2
  - multi-agent
  - workflow-control
timestamp: "2026-06-19T23:08:15.711Z"
---

---
title: "AG2 Multi-Agent Termination with Message Content"
summary: "In AG2 (AutoGen 0.2), agent conversations can be terminated based on the content of a received message, typically when the assistant returns a specific string such as 'TERMINATE'."
confidence: 0.95
provenanceState: extracted
---

# AG2 Multi-Agent Termination with Message Content

In AG2 (AutoGen 0.2), a multi-agent conversation can be programmatically terminated by inspecting the **content** of a message. This mechanism is commonly used to end a dialogue when an agent has completed its task.

## Overview

Termination on message content is configured via the `is_termination_msg` parameter of the [ConversableAgent](/concepts/conversableagent.md) class. This parameter accepts a callable that receives a message dictionary and returns `True` if the conversation should stop. The callable is evaluated after each message is sent by the agent.

A typical pattern is to check whether the `"content"` key of the message contains a termination token — most often the string `"TERMINATE"`. The assistant agent is instructed in its system message to return `"TERMINATE"` when the task is done.

## Configuration

The following snippet from the source example shows the setup:

```python
user_proxy = [[conversableagent|ConversableAgent]](
    name="Tool Agent",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)
```

- `is_termination_msg`: A lambda that checks if the `"content"` field exists and contains the substring `"TERMINATE"`.
- `human_input_mode="NEVER"`: Ensures the agent never asks for human input; termination is driven solely by message content.

The assistant’s system message instructs it to return `"TERMINATE"` when finished:

```python
assistant = [[conversableagent|ConversableAgent]](
    name="Assistant",
    system_message=(
        "You are a helpful AI assistant. You can help with simple calculations. "
        "Return 'TERMINATE' when the task is done."
    ),
    llm_config={"config_list": config_list},
)
```

Once the assistant generates a message containing `"TERMINATE"`, the `is_termination_msg` predicate returns `True`, and the conversation ends. ^[tracing-ag2-databricks-on-aws.md]

## Usage

This pattern is especially useful in tool‑using or multi‑step workflows where the assistant must signal completion. For example, after performing a calculation, the assistant returns `"TERMINATE"` to stop the dialogue and prevent further turns.

The termination check is applied to every message received by the agent. If the predicate returns `True`, the conversation stops immediately without processing further messages.

## Related Concepts

- AG2 (AutoGen 0.2)
- [ConversableAgent](/concepts/conversableagent.md)
- [Agent Termination](/concepts/multi-agent-workflow-termination.md)
- Human Input Mode
- Tool Registration in AG2
- MLflow AG2 Auto‑tracing — The source example uses `mlflow.ag2.autolog()` to trace the terminated conversation.

## Sources

- tracing-ag2-databricks-on-aws.md

# Citations

1. [tracing-ag2-databricks-on-aws.md](/references/tracing-ag2-databricks-on-aws-417b54da.md)
