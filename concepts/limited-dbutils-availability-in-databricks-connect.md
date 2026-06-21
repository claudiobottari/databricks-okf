---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64dfa6755519b18a1d5e8b65c17b3d3b853d69cdfaec71e63af40ad879ab3918
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limited-dbutils-availability-in-databricks-connect
    - LDAIDC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Limited dbutils availability in Databricks Connect
description: Only the `fs` and `secrets` Databricks Utilities are available via dbutils in Databricks Connect; all other utilities are unavailable.
tags:
  - databricks
  - dbutils
  - limitations
timestamp: "2026-06-19T18:15:40.231Z"
---

---

title: Limited dbutils Availability in Databricks Connect
summary: Only dbutils.fs (file system) and dbutils.secrets utilities are available through Databricks Connect; all other Databricks Utilities are not supported in this remote context.
sources:
  - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:10:02.080Z"
updatedAt: "2026-06-18T15:10:02.080Z"
tags:
  - databricks
  - dbutils
  - limitations
aliases:
  - limited-dbutils-availability-in-databricks-connect
  - LDAIDC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Limited dbutils Availability in Databricks Connect

**Limited dbutils Availability in Databricks Connect** refers to the restriction that only two specific Databricks Utilities — `dbutils.fs` and `dbutils.secrets` — are accessible when using the `WorkspaceClient` class through the Databricks SDK for Python in a Databricks Connect environment. No other Databricks Utilities functionality is available through `dbutils` in this context. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Overview

[Databricks Connect](/concepts/databricks-connect.md) enables users to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. When using Databricks Connect for Python, developers access Databricks Utilities through the `WorkspaceClient` class's `dbutils` variable. However, the full suite of Databricks Utilities typically available in a notebook environment is not available through this interface. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available Utilities

The following utilities are accessible via `dbutils` in Databricks Connect:

- **`dbutils.fs`** — Provides access to the file system utility (dbutils.fs) for managing files on Databricks file system (DBFS) and other storage locations. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- **`dbutils.secrets`** — Provides access to the secrets utility (dbutils.secrets) for retrieving secrets stored in Databricks secret scopes. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

All other Databricks Utilities — including utilities for managing notebooks, widgets, jobs, and other Databricks workspace features — are **not** available through `dbutils` in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Workaround Using Databricks SDK

For functionality beyond the limited `dbutils` availability, developers can use the Databricks SDK for Python directly to access any available Databricks REST API. The `WorkspaceClient` class from the Databricks SDK for Python is included in Databricks Connect and can be used to interact with a wide range of Databricks APIs that are not limited to the two available utilities. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initialization

To initialize `WorkspaceClient` for accessing `dbutils`, users must provide authentication information to the Databricks SDK with the workspace. The recommended approach is to create a configuration profile or set environment variables (`DATABRICKS_HOST` and `DATABRICKS_TOKEN`) rather than hard-coding credentials. The `SPARK_REMOTE` environment variable used for Databricks Connect is not recognized by the Databricks SDK for Python. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework for connecting to Databricks clusters from external environments.
- Databricks SDK for Python — The underlying SDK providing `WorkspaceClient` and API access.
- Databricks Utilities — The full set of utilities available in standard Databricks notebooks.
- [WorkspaceClient](/concepts/workspaceclient-and-dbutils.md) — The class providing `dbutils` access in Databricks Connect.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
