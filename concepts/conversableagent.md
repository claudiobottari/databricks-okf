---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91a01f0fac8a417216061fe75d400c2ab36d7b17e2de8598c04514b21dfdc310
  pageDirectory: concepts
  sources:
    - tracing-ag2-databricks-on-aws.md
    - tracing-autogen-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - conversableagent
  citations:
    - file: tracing-autogen-databricks-on-aws.md
    - file: tracing-ag2-databricks-on-aws.md
title: ConversableAgent
description: The fundamental agent class in AG2 (AutoGen 0.2) used to define conversational agents with system messages, LLM configs, and termination logic.
tags:
  - ag2
  - agent-framework
  - conversational-ai
timestamp: "2026-06-19T23:08:07.177Z"
---

# ConversableAgent

**ConversableAgent** is a core class in the [AutoGen](/concepts/autogen-auto-tracing.md) (and AG2) framework, used to define an agent that can participate in multi-agent conversations. It is imported from the `autogen` package and supports tool registration, LLM-driven responses, and configurable termination conditions. ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

## Overview

A `ConversableAgent` can act as either an assistant that proposes tool calls or a user proxy that executes tool calls and interacts with other agents. It is typically initialized with a name, system message, and an LLM configuration. The agent can be customized to run in fully automated mode (`human_input_mode="NEVER"`) or with simulated human input. ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

The class is central to building multi-agent workflows where agents communicate via chat messages. ConversableAgents can register tool functions for the LLM to propose and for another agent to execute, enabling tool-augmented reasoning. ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

## Key Parameters

- **name** (str): A unique identifier for the agent, used in conversation logs and tracing.
- **system_message** (str): The system prompt that sets the agent's role and behavior.
- **llm_config** (dict or False): Configuration for the LLM backend, typically containing a `config_list` with model and API key details. Set to `False` to disable an LLM (e.g., for a tool-execution-only agent).
- **is_termination_msg** (callable): A function that checks if a message should end the conversation. Often checks for the presence of `"TERMINATE"` in message content.
- **human_input_mode** (str): Controls when human input is solicited. In automated workflows, `"NEVER"` is used. ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

## Tool Registration

A `ConversableAgent` supports registering tools for two purposes:

- **`register_for_llm`**: Registers a function with the agent so that the LLM can propose its invocation. The function is decorated with a description and is typically registered on the assistant agent.
- **`register_for_execution`**: Registers the same function for actual execution. This is usually called on a [User Proxy Agent](/concepts/user-proxy-agent.md) that runs the tool code. ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

Both methods accept a `name` and `description` parameter. The registered function can have a type-annotated signature (e.g., using `Annotated` and `Literal`) to guide the LLM’s argument generation. ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

## Chat Initiation

The `initiate_chat` method starts a conversation between two ConversableAgents. It takes the recipient agent and an initial `message` string. The conversation proceeds until a termination condition is met (e.g., the recipient returns a message containing `"TERMINATE"`). ^[tracing-autogen-databricks-on-aws.md, tracing-ag2-databricks-on-aws.md]

## Tracing Integration with [MLflow](/concepts/mlflow.md)

ConversableAgent workflows can be automatically traced using [MLflow](/concepts/mlflow.md) tracing capabilities. The following [MLflow](/concepts/mlflow.md) functions enable observability:

- `mlflow.ag2.autolog()` (for AG2) or `mlflow.autogen.autolog()` (for AutoGen) — Enables [Automatic Tracing](/concepts/automatic-tracing.md) of agent interactions.
- `mlflow.set_tracking_uri("databricks")` — Routes [Traces](/concepts/traces.md) to a Databricks workspace.
- `mlflow.set_experiment(...)` — Specifies the experiment under which [Traces](/concepts/traces.md) are logged.

Once enabled, every agent chat, tool call, and LLM invocation is recorded as a trace, providing full visibility into multi-agent workflows. ^[tracing-ag2-databricks-on-aws.md, tracing-autogen-databricks-on-aws.md]

## Example Usage

A typical pattern defines an assistant agent with an LLM and a tool-execution agent. The assistant registers a calculator tool for the LLM, and the user proxy registers the same tool for execution. The conversation is initiated with a math problem, and the assistant returns `"TERMINATE"` when the task is complete. ^[tracing-ag2-databricks-on-aws.md, tracing-autogen-databricks-on-aws.md]

```python
from autogen import ConversableAgent

assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant... Return 'TERMINATE' when done.",
    llm_config={"config_list": [{"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

user_proxy = ConversableAgent(
    name="Tool Agent",
    llm_config=False,
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", ""),
    human_input_mode="NEVER",
)
```

## Related Concepts

- [AutoGen](/concepts/autogen-auto-tracing.md) / AG2 — The frameworks that provide the `ConversableAgent` class.
- Multi-Agent Systems — The broader paradigm of coordinating multiple autonomous agents.
- Tool Use — How agents leverage external functions via registration.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Mechanism for recording agent conversations and tool calls.
- agent — General concept of an autonomous program interacting with its environment.

## Sources

- tracing-autogen-databricks-on-aws.md
- tracing-ag2-databricks-on-aws.md

# Citations

1. [tracing-autogen-databricks-on-aws.md](/references/tracing-autogen-databricks-on-aws-04b86736.md)
2. [tracing-ag2-databricks-on-aws.md](/references/tracing-ag2-databricks-on-aws-417b54da.md)
