---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8d584efd1fbd12c6c87640b09fde303a1e5e2a7fe9fa5332bdbe923d634d962
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-managed-functions-as-ai-agent-tools
    - UCMFAAAT
  citations:
    - file: ai-governance-databricks-on-aws.md
title: Unity Catalog managed functions as AI agent tools
description: Unity Catalog functions used as agent tools or for data transformations, enabling governed access to external APIs and data processing within AI workflows.
tags:
  - unity-catalog
  - ai-agents
  - functions
timestamp: "2026-06-18T14:20:56.647Z"
---

# Unity Catalog Managed Functions as AI Agent Tools

**Unity Catalog managed functions** are user-defined functions (UDFs) registered in [Unity Catalog](/concepts/unity-catalog.md) that can be used as tools for GenAI agent systems or for general data transformations. They are part of the [AI Governance](/concepts/ai-governance.md) framework that extends Unity Catalog's data governance capabilities—access control, lineage, and audit—to AI assets. ^[ai-governance-databricks-on-aws.md]

## AI Governance Context

Unity Catalog treats functions as securable objects. Administrators can grant and revoke access to these functions using standard Unity Catalog privileges, just as they do for tables, models, and other securable objects. This means that when a function is used as an agent tool, the same governance policies that protect data also control which agents or users can invoke the function. ^[ai-governance-databricks-on-aws.md]

## Usage as Agent Tools

Agent tools are components that a GenAI agent can call to perform actions, retrieve information, or interact with external systems. A Unity Catalog managed function becomes an agent tool by being registered in Unity Catalog and then referenced by the agent's tool configuration. The function can contain SQL, Python, or other executable logic, and its execution is governed by Unity Catalog permissions. ^[ai-governance-databricks-on-aws.md]

The typical workflow is:

1. **Create the function** in Unity Catalog using standard SQL DDL (e.g., `CREATE FUNCTION`).
2. **Grant `EXECUTE` privilege** on the function to the principal (user, service principal, or group) that will run the agent.
3. **Register the function as a tool** in the agent's definition, so the agent can call it during inference.

For detailed steps, see the documentation on creating custom AI agent tools using Unity Catalog functions.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance system for data and AI assets.
- [AI Governance](/concepts/ai-governance.md) — The broader framework for managing AI assets and traffic.
- GenAI agent — An AI system that can invoke tools to accomplish tasks.
- Custom agent tools — A general concept for tools used by agents, which can be Unity Catalog functions.

## Sources

- ai-governance-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)
