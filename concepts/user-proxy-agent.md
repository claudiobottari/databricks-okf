---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b702aa5f9395d60837ee2d605bd76a5bf6a1552cd142acf95dc6314cd650af08
  pageDirectory: concepts
  sources:
    - tracing-autogen-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-proxy-agent
    - UPA
  citations:
    - file: tracing-autogen-databricks-on-aws.md
title: User Proxy Agent
description: An AutoGen agent that acts as an intermediary to execute tool calls and manage conversation termination, typically with human_input_mode='NEVER' for automated workflows
tags:
  - autogen
  - agent
  - automation
timestamp: "2026-06-19T23:09:42.509Z"
---

# User Proxy Agent

The **User Proxy Agent** is a type of conversational agent in the [AutoGen](/concepts/autogen-auto-tracing.md) framework that acts as an intermediary for executing tool calls and managing interactions between a human user (or a simulated user) and other agents. It is created using the `ConversableAgent` class with specific configuration parameters that disable its own LLM and control its behavior regarding termination and user input. ^[tracing-autogen-databricks-on-aws.md]

## Role in Multi-Agent Workflows

In a typical AutoGen workflow, the user proxy agent is paired with an LLM‑powered assistant agent. The assistant agent generates structured messages that request tool calls, and the user proxy agent is responsible for executing those tool calls against registered functions. This separation allows the LLM agent to focus on reasoning while the user proxy handles deterministic execution. ^[tracing-autogen-databricks-on-aws.md]

## Configuration

The user proxy agent is instantiated with the following key parameters:

- **`name`**: A human‑readable identifier for the agent. In practice it is often set to `"Tool Agent"` to indicate its role. ^[tracing-autogen-databricks-on-aws.md]
- **`llm_config=False`**: Disables the agent’s own LLM, ensuring it does not generate free‑form text responses but instead relies on the conversation structure. ^[tracing-autogen-databricks-on-aws.md]
- **`is_termination_msg`**: A function that inspects each received message and returns `True` if the message content contains the string `"TERMINATE"`. This condition ends the conversation when the assistant signals completion. ^[tracing-autogen-databricks-on-aws.md]
- **`human_input_mode="NEVER"`**: Indicates that the agent should never prompt a human for input. The agent runs fully autonomously, executing tool calls and passing messages without waiting for user intervention. ^[tracing-autogen-databricks-on-aws.md]

## Tool Registration

Functions that the assistant agent may invoke are registered with the user proxy agent using the `register_for_execution` method. This binds the function’s name to the proxy’s execution environment, enabling the proxy to call the function when the assistant requests it. Similarly, the assistant agent registers the same function for LLM use via `register_for_llm` so it can formulate tool‑call requests. ^[tracing-autogen-databricks-on-aws.md]

## Interaction with the LLM Agent

The conversation between the user proxy and the assistant is initiated using the `initiate_chat` method on the user proxy. The user proxy sends the initial message (e.g., a user‑specified prompt) to the assistant agent. After the assistant responds—possibly with tool‑call requests—the user proxy executes the requested tool and returns the result. This cycle continues until the assistant sends a `"TERMINATE"` signal. ^[tracing-autogen-databricks-on-aws.md]

## Termination Logic

The termination condition is defined by the `is_termination_msg` callback. In the standard configuration, the conversation ends when the assistant’s message contains `"TERMINATE"`. The user proxy agent interprets this as a signal that the task is complete and stops further processing. ^[tracing-autogen-databricks-on-aws.md]

## Usage Example

The following code snippet, taken from the documentation, demonstrates the creation and use of a user proxy agent in an AutoGen workflow: ^[tracing-autogen-databricks-on-aws.md]

```python
user_proxy = [[conversableagent|ConversableAgent]](
    name="Tool Agent",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None
    and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)
# ... register tool with assistant and with user_proxy
response = user_proxy.initiate_chat(
    assistant,
    message="What is (44231 + 13312 / (230 - 20)) * 4?"
)
```

## Related Concepts

- [ConversableAgent](/concepts/conversableagent.md) – The base class used to create both assistant and user proxy agents.
- [AutoGen](/concepts/autogen-auto-tracing.md) – The multi‑agent conversation framework.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Workflows that evaluate the performance of agent systems.
- [MLflow](/concepts/mlflow.md) – Used for tracing AutoGen workflows (can be enabled with `mlflow.autogen.autolog()`).
- Tool Agent – An alias or alternative name for the user proxy agent when focused on tool execution.

## Sources

- tracing-autogen-databricks-on-aws.md

# Citations

1. [tracing-autogen-databricks-on-aws.md](/references/tracing-autogen-databricks-on-aws-04b86736.md)
