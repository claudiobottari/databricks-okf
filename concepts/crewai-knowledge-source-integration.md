---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7bccba0163dfec4e2f5605c6685cabcca1ceb651b339ff07ff4f1c4f0d66c77
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crewai-knowledge-source-integration
    - CKSI
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: CrewAI Knowledge Source Integration
description: CrewAI agents can attach knowledge sources (e.g., StringKnowledgeSource) with metadata for contextual awareness
tags:
  - crewai
  - knowledge
  - agents
  - memory
timestamp: "2026-06-19T23:10:27.491Z"
---

# CrewAI Knowledge Source Integration

**CrewAI Knowledge Source Integration** refers to the mechanism by which CrewAI agents can incorporate external knowledge sources into their workflows. This integration allows agents to access structured information during task execution, enhancing their ability to provide contextually relevant responses and make informed decisions. ^[tracing-crewai-databricks-on-aws.md]

## Overview

CrewAI supports the inclusion of knowledge sources that agents can reference during task execution. These sources provide additional context and information beyond what is available in the agent's base training data or system prompt. Knowledge sources are configured as part of the Crew definition and are accessible to all agents within that crew. ^[tracing-crewai-databricks-on-aws.md]

## Knowledge Source Types

CrewAI provides several types of knowledge sources for integrating external information:

- **StringKnowledgeSource**: Allows embedding string-based content directly into the crew's knowledge base. This is useful for providing specific facts, user preferences, or reference material.
- **File-based sources**: Support for loading knowledge from various file formats.
- **Custom knowledge sources**: Developers can implement custom knowledge source classes for specialized data formats or retrieval mechanisms.

^[tracing-crewai-databricks-on-aws.md]

## Configuration

Knowledge sources are configured within the `Crew` object definition using the `knowledge` parameter. The configuration includes:

- **`sources`**: A list of knowledge source objects that the crew should have access to.
- **`metadata`**: Optional metadata that can be associated with the knowledge sources for filtering or categorization purposes.

^[tracing-crewai-databricks-on-aws.md]

### Example: StringKnowledgeSource

The following example demonstrates how to create and use a `StringKnowledgeSource` within a CrewAI workflow:

```python
from crewai import Agent, Crew, Task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

content = "Users name is John. He is 30 years old and lives in San Francisco."
string_source = StringKnowledgeSource(
    content=content,
    metadata={"preference": "personal"}
)

crew = Crew(
    agents=[city_selector_agent, local_expert_agent],
    tasks=[identify_task, gather_task],
    verbose=True,
    memory=True,
    knowledge={
        "sources": [string_source],
        "metadata": {"preference": "personal"},
    },
)
```

^[tracing-crewai-databricks-on-aws.md]

## Integration with [MLflow Tracing](/concepts/mlflow-tracing.md)

When [MLflow Tracing](/concepts/mlflow-tracing.md) is enabled for CrewAI via `mlflow.crewai.autolog()`, the tracing system automatically captures information about knowledge source operations, including:

- Memory load and write operations
- Latency of knowledge retrieval operations
- Any exceptions raised during knowledge access

This provides observability into how agents interact with their knowledge sources during task execution. ^[tracing-crewai-databricks-on-aws.md]

## Related Concepts

- CrewAI — The open-source framework for orchestrating multi-agent AI systems
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Automatic trace capture for CrewAI workflows
- CrewAI Agent Configuration — How agents are configured with tools and knowledge
- CrewAI Task Execution — How tasks are executed within a crew
- StringKnowledgeSource — A specific knowledge source type for string-based content

## Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
