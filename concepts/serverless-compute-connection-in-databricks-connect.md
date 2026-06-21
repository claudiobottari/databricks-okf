---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b903aad754aa027364a274a5be0f9ce077c23a4c5731c0bd9f9d584df05defd4
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-connection-in-databricks-connect
    - SCCIDC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Serverless compute connection in Databricks Connect
description: Configuration for connecting to serverless compute using DATABRICKS_SERVERLESS_COMPUTE_ID=auto, serverless_compute_id=auto in profiles, or builder.serverless()/remote(serverless=True).
tags:
  - databricks
  - serverless
  - configuration
timestamp: "2026-06-19T09:20:03.879Z"
---

---  
title: Serverless Compute Connection in Databricks Connect  
summary: Configuring Databricks Connect to connect to serverless compute instead of a classic cluster, using serverless_compute_id=auto or builder.serverless().  
sources:  
  - compute-configuration-for-databricks-connect-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T14:40:57.699Z"  
updatedAt: "2026-06-18T14:40:57.699Z"  
tags:  
  - serverless  
  - configuration  
  - databricks-connect  
aliases:  
  - serverless-compute-connection-in-databricks-connect  
  - SCCIDC  
confidence: 1  
provenanceState: extracted  
inferredParagraphs: 0  
---

## Serverless Compute Connection in Databricks Connect

**Serverless Compute Connection** in Databricks Connect enables you to connect popular IDEs (such as Visual Studio Code, PyCharm, RStudio Desktop, and IntelliJ IDEA), notebook servers, and custom applications to Databricks serverless compute instead of classic clusters. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Requirements

Databricks Connect for Python and Scala supports connecting to serverless compute. To use this feature, you must meet the version requirements for connecting to serverless compute as specified in the Databricks Connect usage requirements documentation. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Configuration Methods

You can configure a connection to serverless compute using one of the following methods.

#### Environment Variable (Python)

Set the local environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`. When this environment variable is set, Databricks Connect ignores the `cluster_id` configuration. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

#### Configuration Profile (Python)

Create or update a local Databricks configuration profile with `serverless_compute_id = auto`, then reference that profile from your code. For example:

```
[DEFAULT]
host = https://my-workspace.cloud.databricks.com/
serverless_compute_id = auto
token = dapi123...
```
^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

#### [DatabricksSession](/concepts/databrickssession.md) Builder API (Python or Scala)

Use the `DatabricksSession` builder to configure a serverless connection directly in code. Two options are available:

**Using the `serverless()` method:**
```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()
```
^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

**Using the `remote()` method with `serverless=True`:**
```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
```
^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Connection Validation

To validate that your environment, default credentials, and connection to serverless compute are correctly set up for Databricks Connect, run the `databricks-connect test` command. This command fails with a non-zero exit code and a corresponding error message when it detects any incompatibility, such as when the Databricks Connect version is incompatible with the Databricks serverless compute version. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

In Databricks Connect 14.3 and above, you can also validate your environment using `validateSession()`:

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```
^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Behavior When Serverless is Configured

When `DATABRICKS_SERVERLESS_COMPUTE_ID` is set to `auto` or the `.serverless()` method is used, Databricks Connect ignores any `cluster_id` configuration, ensuring the connection is directed to serverless compute rather than a classic cluster. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework for connecting external applications to Databricks compute
- Serverless Compute — On-demand compute resources managed by Databricks
- [Classic Compute Configuration in Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Alternative connection method for traditional clusters
- [Databricks Configuration Profiles](/concepts/databricks-configuration-profiles.md) — Local configuration files for authentication and connection settings
- [DatabricksSession](/concepts/databrickssession.md) — The primary API class for establishing a connection

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
