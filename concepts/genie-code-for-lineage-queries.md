---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3110f67705e963696edcc756f44c0d7fe13ed38919dac536136712a4007cef15
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-for-lineage-queries
    - GCFLQ
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: Genie Code for Lineage Queries
description: Natural-language assistant in Catalog Explorer that can answer lineage questions via commands like /getTableLineages and /getTableInsights to show dependencies and usage patterns.
tags:
  - genie
  - lineage
  - ai-assistant
timestamp: "2026-06-19T18:05:01.618Z"
---

```markdown
---
title: Genie Code for Lineage Queries
summary: Natural language interface within Catalog Explorer using Genie Code commands like /getTableLineages and /getTableInsights to ask lineage questions such as 'show me downstream lineages' or 'who queries this table most often'.
sources:
  - data-lineage-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:58:59.848Z"
updatedAt: "2026-06-18T14:58:59.848Z"
tags:
  - genie-code
  - ai-assistant
  - lineage
aliases:
  - genie-code-for-lineage-queries
  - GCFLQ
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 1
---

# Genie Code for Lineage Queries

**Genie Code for Lineage Queries** is a natural language interface in Databricks that allows users to ask questions about [[data lineage]] using simple commands rather than writing complex SQL queries against system tables. It provides an interactive way to explore upstream and downstream dependencies for tables in [[Unity Catalog]].

## Overview

Genie Code, accessible from Catalog Explorer, enables users to query data lineage information using conversational language. It can answer questions about table relationships, dependencies, and usage patterns without requiring users to manually query lineage system tables or navigate the lineage graph. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Getting Lineage Information

To use Genie Code for lineage queries:

1. In the workspace sidebar, click the **Catalog** icon to open Catalog Explorer.
2. Browse or search for the catalog, click the catalog name, and then click the **Genie Code** icon in the upper-right corner.
3. At the Genie Code prompt, type:
   - `/getTableLineages` to view upstream and downstream dependencies.
   - `/getTableInsights` to access metadata-driven insights, such as user activity and query patterns.

These queries enable Genie Code to answer questions like "show me downstream lineages" or "who queries this table most often." ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Capabilities

Genie Code can answer natural language questions about lineage, including: ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

- **Upstream dependencies**: Which tables, jobs, or queries produce data for a given table.
- **Downstream dependencies**: Which tables, dashboards, and jobs consume data from a given table.
- **Usage patterns**: Which users query a table most frequently and what query patterns exist.
- **Impact analysis**: Identifying downstream assets affected by changes to a table.

## Related Concepts

- [[Data Lineage in Unity Catalog]] — The underlying lineage system that Genie Code queries.
- [[Catalog Explorer]] — The interface where Genie Code is accessed.
- [[Lineage System Tables]] — The programmatic API for lineage queries.
- Table Insights — Usage trends and popularity metrics for tables.
- Genie AI Assistant — The broader AI assistant functionality in Databricks.

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
