---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 238439316be180169f46d18d921b4a070ea662c9c141895a28124804e7767788
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
    - develop-code-based-scorers-databricks-on-aws.md
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
    - tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-genai
    - MTFG
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
    - file: tracing-crewai-databricks-on-aws.md
    - file: mlflow-mcp-server-databricks-on-aws.md
title: MLflow Tracing for GenAI
description: MLflow capability for adding traces to Python and TypeScript generative AI applications
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T22:00:11.591Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI

**MLflow Tracing for GenAI** is an instrumentation framework within MLflow 3 that provides observability for generative AI applications by recording the inputs, outputs, and execution flow of LLM calls and agent operations. Tracing enables developers to debug, profile, and understand the behavior of GenAI applications during development and production. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) captures detailed execution traces for GenAI applications. Each trace records the sequence of operations — including LLM requests, tool calls, agent decisions, and their results — along with metadata such as latency, token counts, and any exceptions. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

Traces are organized into **spans**, which represent individual operations. Simple applications generate flat traces with a single span, while complex GenAI agents produce nested span structures that reveal the full execution tree, including sub-calls to tools, memory operations, and multiple LLM invocations. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Enabling Tracing

### Automatic Tracing (Autolog)

MLflow provides `autolog()` functions for supported frameworks that automatically instrument calls without requiring manual changes to application code. To enable tracing, call the appropriate autolog function for your library: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
import mlflow

# For OpenAI-compatible calls
mlflow.openai.autolog()

# For CrewAI multi-agent workflows
mlflow.crewai.autolog()
```

On serverless compute clusters, autologging is not automatically enabled and must be explicitly called. ^[tracing-crewai-databricks-on-aws.md]

### Manual Tracing with Decorators

The `@mlflow.trace` decorator allows you to define how traces are organized by instrumenting specific functions: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
@mlflow.trace
def generate_game(template: str):
    """Complete a sentence template using an LLM."""
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": template},
        ],
    )
    return response.choices[0].message.content
```

### Disabling Tracing

Auto-tracing can be disabled globally: ^[tracing-crewai-databricks-on-aws.md]

```python
mlflow.crewai.autolog(disable=True)
# or
mlflow.autolog(disable=True)
```

## Integrations

[MLflow Tracing](/concepts/mlflow-tracing.md) integrates with 20+ SDKs and frameworks. Supported integrations include: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

- **OpenAI** — Via `mlflow.openai.autolog()`, captures chat completions, input prompts, responses, and token counts
- **CrewAI** — Via `mlflow.crewai.autolog()`, captures tasks, agent assignments, LLM calls, memory operations, latency, and exceptions ^[tracing-crewai-databricks-on-aws.md]
- **Anthropic, LangGraph, and others** — See [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) for the full list

For a complete list of supported libraries, see the [MLflow Tracing integrations documentation](/concepts/mlflow-tracing-integrations.md). ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Trace Data Captured

Depending on the integration, MLflow traces automatically capture: ^[tracing-crewai-databricks-on-aws.md]

- Input prompts and completion responses
- Token counts (input and output)
- Latency of each operation
- Nested span structure showing the execution tree
- Tool invocations and their results
- Memory load and write operations
- Any exceptions raised during execution

## Querying and Analyzing Traces

### Programmatic Search

Traces can be searched programmatically using the MLflow API: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
traces = mlflow.search_traces(max_results=10)
```

This allows you to analyze trace data, retrieve specific traces by experiment ID or trace ID, and integrate trace data into custom workflows. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md, mlflow-mcp-server-databricks-on-aws.md]

### MLflow MCP Server

The [MLflow MCP Server](/concepts/mlflow-mcp-server.md) enables AI applications and coding assistants to interact with traces programmatically through the Model Context Protocol (MCP). It exposes all MLflow trace management operations, allowing AI assistants to: ^[mlflow-mcp-server-databricks-on-aws.md]

- Search and retrieve trace data
- Analyze trace performance and behavior
- Log feedback and assessments
- Manage trace tags and metadata
- Delete traces and assessments

This is particularly useful for integrating trace analysis into coding workflows. For example, you can ask an AI assistant to "search for traces from experiment ID 12345" or "show me the most recent traces with errors." ^[mlflow-mcp-server-databricks-on-aws.md]

To use the MCP server with Databricks, configure your MCP client (such as VS Code, Cursor, or Claude Desktop) with the Databricks workspace URL and authentication token. See the open source MLflow MCP server documentation for complete setup instructions. ^[mlflow-mcp-server-databricks-on-aws.md]

## Trace Visualization

Trace visualization in the MLflow UI shows inputs, outputs, and the structure of calls. For simple applications, traces show basic insights such as input and output token counts. For more complex agents, the visualization displays nested spans that help developers understand and debug agent behavior. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Collecting Feedback on Traces

MLflow supports collecting human feedback on traces through the [Review App](/concepts/mlflow-review-app.md) and programmatic APIs: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Creating Labeling Sessions

Use `mlflow.genai.labeling` to create labeling sessions and share traces with expert reviewers: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical
from mlflow.genai.labeling import create_labeling_session

humor_schema = create_label_schema(
    name="response_humor",
    type="feedback",
    title="Rate how funny the response is",
    input=InputCategorical(options=["Very funny", "Slightly funny", "Not funny"]),
    overwrite=True
)

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[humor_schema.name],
)

traces = mlflow.search_traces(max_results=10)
labeling_session.add_traces(traces)

print(f"Share this link with reviewers: {labeling_session.url}")
```

### Logging User Feedback

Within applications, user feedback can be logged using `mlflow.log_feedback()`. See Collect user feedback for more information. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Integration with Evaluation and Monitoring

Tracing integrates with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) and [Production Monitoring](/concepts/production-monitoring.md). The same scorers used during development — including built-in scorers like Safety and custom [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) scorers — can be deployed to monitor production traffic. This enables a continuous feedback loop from development through production. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- MLflow Evaluation for GenAI — Using scorers to judge quality of GenAI outputs
- [MLflow Production Monitoring for GenAI](/concepts/mlflow-production-monitoring.md) — Deploying evaluation in production
- Collecting Human Feedback — Review App and programmatic feedback collection
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — Using LLMs to evaluate outputs
- [GenAI Agents](/concepts/genai-agent-observability.md) — Complex agent applications that benefit from tracing

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md
- mlflow-mcp-server-databricks-on-aws.md
- tracing-crewai-databricks-on-aws.md
- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
2. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
3. [mlflow-mcp-server-databricks-on-aws.md](/references/mlflow-mcp-server-databricks-on-aws-8d2ac0cf.md)
