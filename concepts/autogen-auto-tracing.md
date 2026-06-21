---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7989ccfe64e6c59935a4842fc1c50de2f970b14e548e8fe7bd447b78503b8fd
  pageDirectory: concepts
  sources:
    - tracing-autogen-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autogen-auto-tracing
    - AutoGen Tracing
    - AutoGen
    - Autogen
    - agent tracing
  citations:
    - file: tracing-autogen-databricks-on-aws.md
title: AutoGen Auto-Tracing
description: MLflow's automatic tracing capability for AutoGen agent workflows, enabled via mlflow.autogen.autolog()
tags:
  - mlflow
  - autogen
  - tracing
timestamp: "2026-06-19T23:09:33.304Z"
---

# AutoGen Auto-Tracing

**AutoGen Auto-Tracing** refers to the ability to automatically capture and log [Traces](/concepts/traces.md) of agent‑to‑agent interactions, tool calls, and LLM invocations within [AutoGen](/concepts/autogen-auto-tracing.md) multi‑agent workflows using [MLflow](/concepts/mlflow.md). By calling `mlflow.autogen.autolog()`, all agent conversations, function calls, and termination messages are recorded as [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md), enabling observability, debugging, and performance analysis of complex multi‑agent systems. ^[tracing-autogen-databricks-on-aws.md]

## Enabling Auto-Tracing

Auto-tracing for AutoGen is activated by invoking `mlflow.autogen.autolog()` **before** any AutoGen agents are created or used. After this call, every interaction between agents — including messages, tool registrations, and tool executions — will be automatically traced to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-autogen-databricks-on-aws.md]

The following setup is typically required:

- Ensure LLM provider environment variables (e.g., `OPENAI_API_KEY`) are set.
- Set the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) to point to a Databricks workspace (e.g., `mlflow.set_tracking_uri("databricks")`).
- Set an experiment with `mlflow.set_experiment()`, for example `/Shared/autogen-tracing-demo`.

A minimal configuration looks like:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].autogen.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/autogen-tracing-demo")
```

^[tracing-autogen-databricks-on-aws.md]

## Example Workflow

In a typical AutoGen setup, a `ConversableAgent` (e.g., an assistant) is paired with a [User Proxy Agent](/concepts/user-proxy-agent.md). Tools are registered on the assistant for LLM suggestion and on the proxy for execution. When the user proxy initiates a chat, the entire conversation — including tool selection, tool execution, and the final response — is traced automatically. ^[tracing-autogen-databricks-on-aws.md]

The following excerpt demonstrates the key agent and tool registration code:

```python
from autogen import [[conversableagent|ConversableAgent]]

assistant = [[conversableagent|ConversableAgent]](
    name="Assistant",
    system_message="...",
    llm_config={"config_list": config_list},
)

user_proxy = [[conversableagent|ConversableAgent]](
    name="Tool Agent",
    llm_config=False,
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", ""),
    human_input_mode="NEVER",
)

assistant.register_for_llm(name="calculator", description="A simple calculator")(calculator)
user_proxy.register_for_execution(name="calculator")(calculator)
```

^[tracing-autogen-databricks-on-aws.md]

After `user_proxy.initiate_chat(assistant, message="What is (44231 + 13312 / (230 - 20)) * 4?")`, the trace records each step, including the intermediate tool calls and the final result. ^[tracing-autogen-databricks-on-aws.md]

## Integration with Databricks

When used on Databricks, auto‑tracing sends the generated [Traces](/concepts/traces.md) to the [MLflow Experiment](/concepts/mlflow-experiment.md) specified via `mlflow.set_experiment()`. The trace data can then be inspected in the Databricks UI under the experiment's **Traces** tab. This allows teams to monitor agent behavior, identify bottlenecks, and debug failures in production or development. ^[tracing-autogen-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – General mechanism for capturing and storing execution [Traces](/concepts/traces.md).
- [AutoGen](/concepts/autogen-auto-tracing.md) – Multi‑agent conversation framework for LLM‑powered agents.
- [ConversableAgent](/concepts/conversableagent.md) – The base agent class used in AutoGen.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Techniques for assessing agent performance (often uses [Traces](/concepts/traces.md)).
- [LLM Observability](/concepts/genai-observability.md) – The practice of monitoring and analyzing LLM calls.
- [Databricks MLflow Experiment](/concepts/databricks-mlflow-experiment-setup.md) – The organizational unit for [MLflow](/concepts/mlflow.md) runs and [Traces](/concepts/traces.md).

## Sources

- tracing-autogen-databricks-on-aws.md

# Citations

1. [tracing-autogen-databricks-on-aws.md](/references/tracing-autogen-databricks-on-aws-04b86736.md)
