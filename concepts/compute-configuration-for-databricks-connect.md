---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84449077214306bc45ed6e725ddb24542ebd888bf6b0c6a8556baf846df3013f
  pageDirectory: concepts
  sources:
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-configuration-for-databricks-connect
    - CCFDC
    - Classic Compute Configuration in Databricks Connect
    - Cluster Configuration for Databricks Connect
    - Proxy Configuration for Databricks Connect
    - Proxy configuration for Databricks Connect
    - compute configuration requirements for Databricks Connect
    - Databricks cluster configuration for Databricks Connect
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: Compute configuration for Databricks Connect
description: Configuration details for setting up Databricks compute clusters to work with Databricks Connect.
tags:
  - databricks
  - compute
  - configuration
timestamp: "2026-06-19T14:47:14.704Z"
---

We'll generate the requested page based strictly on the provided material and instructions.

---

## Compute configuration for Databricks Connect

**Compute configuration for Databricks Connect** refers to the Databricks cluster settings, cluster policies, and cluster libraries that you must prepare on your Databricks workspace so that a local Databricks Connect client (for Scala, Python, or R) can attach to it and execute Spark code remotely. The configuration includes choosing a compatible Databricks Runtime version and ensuring the cluster is accessible to the client.

### Overview

A Databricks Connect client connects to a remote Databricks compute cluster running in the workspace. You must configure the cluster to match the version of the Databricks Connect package you are using. ^[databricks-connect-for-scala-databricks-on-aws.md]

For [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), the compute must be running **Databricks Runtime 13.3 LTS** or above. The client version must be compatible with that runtime. ^[databricks-connect-for-scala-databricks-on-aws.md]

You can find the full compatibility requirements — including supported runtime versions, network settings, and authentication methods — in the [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) article. ^[databricks-connect-for-scala-databricks-on-aws.md]

### Cluster configuration

The cluster that Databricks Connect attaches to must:

- Be running a supported Databricks Runtime version (13.3 LTS or newer for Scala).
- Have cluster access mode set to **Single user** or **No isolation shared** if required by your workspace configuration.
- Be **running** (not terminated) when the client attempts to connect.

For the most up‑to‑date list of supported runtime and client versions, see [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md). ^[databricks-connect-for-scala-databricks-on-aws.md]

### How to configure

1. **Create or select a cluster** in the Databricks workspace with a compatible Databricks Runtime version.
2. **Install the Databricks Connect library** on the cluster if needed (for some client versions, the library is pre‑installed on the runtime; for others you must add it manually).
3. **Configure authentication** – the client authenticates via a [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) or an OAuth token, depending on your workspace security settings.
4. **Start the cluster** – the client can only connect to an active, running cluster.

Full step‑by‑step instructions are provided in the [Install Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) guide. ^[databricks-connect-for-scala-databricks-on-aws.md]

### Related articles

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Python client instructions
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – R client instructions  
- Migrate to Databricks Connect for Scala – Migration from older runtime versions
- Troubleshooting Databricks Connect – Common issues and fixes
- [Limitations of Databricks Connect](/concepts/limitations-of-dbutils-in-databricks-connect.md) – Behavioral constraints

### Sources

- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
