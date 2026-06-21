---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9cf7382b0d55726453073ed38bc0e0682d666316083b6f6ce5639e45a135c24
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-workspace-requirements
    - DCWR
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Workspace Requirements
description: Prerequisites for using Databricks Connect including Unity Catalog enablement, compute version compatibility, and cluster access mode requirements.
tags:
  - databricks
  - configuration
  - workspace
timestamp: "2026-06-19T18:11:02.426Z"
---

```markdown
---
title: Databricks Connect Workspace Requirements
summary: Workspace-level prerequisites for using Databricks Connect, including Unity Catalog enablement, compute version compatibility, serverless compute setup, and cluster access mode configuration.
sources:
  - databricks-connect-usage-requirements-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:49:53.230Z"
updatedAt: "2026-06-19T14:47:52.055Z"
tags:
  - databricks
  - workspace-configuration
  - prerequisites
aliases:
  - databricks-connect-workspace-requirements
  - DCWR
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## Databricks Connect Workspace Requirements

**Databricks Connect Workspace Requirements** define the configuration and capabilities a Databricks workspace must have to support connections from local IDEs or scripts using the Databricks Connect client library. These requirements ensure that the workspace can properly route requests from the client to the target compute resource. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Unity Catalog Must Be Enabled

To use Databricks Connect, both the Databricks account and the workspace must have [[Unity Catalog]] enabled. Unity Catalog provides centralized access control and metadata management, which is a prerequisite for Databricks Connect's remote execution model. See the guides on [getting started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) and [enabling a workspace for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Compute Version Compatibility

The Databricks Runtime version of the target compute resource (cluster or serverless compute) must be **greater than or equal to** the version of the Databricks Connect package installed locally. Databricks recommends using the most recent Databricks Connect package that matches the Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

To use features available in a later Databricks Runtime release, you must upgrade the Databricks Connect package. Compatibility details for each release are listed in the [Databricks Connect release notes](https://docs.databricks.com/aws/en/release-notes/dbconnect/). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Serverless Compute Requirements

If connecting to Serverless Compute, the workspace must meet the general [requirements for serverless compute](https://docs.databricks.com/aws/en/compute/serverless/#requirements). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

Serverless compute support was introduced in Databricks Connect version 15.1. Versions of Databricks Connect that are lower than or equal to the Databricks Runtime release running on serverless are fully compatible. To verify compatibility, use the [validate connection](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#validate) command. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Cluster Access Mode

If connecting to a traditional cluster, the target cluster must use an **Assigned** or **Shared** cluster access mode. These modes allow external clients to connect via Databricks Connect. Access modes are configured in the cluster's advanced settings. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode) for more details. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Related Concepts

- [[Databricks Connect]] – Overview of the client library and connection workflow.
- [[Unity Catalog]] – Prerequisite for Databricks Connect.
- Serverless Compute – Alternative compute target with its own requirements.
- Cluster Access Modes – Configuration that determines whether a cluster accepts external connections.
- Databricks Authentication – Required for local environment setup (OAuth U2M/M2M, etc.).

### Sources

- databricks-connect-usage-requirements-databricks-on-aws.md
```

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
