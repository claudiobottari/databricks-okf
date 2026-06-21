---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 197a3f9eecf2d6a6d2105405490d015211571c5c032afd7f1792999ceffb64ea
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-scoped-vs-notebook-scoped-library-installation
    - CVNLI
    - Compute-scoped libraries
    - Notebook-scoped Python libraries
    - notebook-scoped R libraries
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Compute-Scoped vs Notebook-Scoped Library Installation
description: "Two methods for installing additional libraries on Databricks: compute-scoped libraries (available to all notebooks on a compute resource) and notebook-scoped Python libraries (available only to a specific notebook session)."
tags:
  - databricks
  - libraries
  - notebooks
timestamp: "2026-06-18T11:41:40.340Z"
---

# Compute-Scoped vs Notebook-Scoped Library Installation

**Compute-scoped vs notebook-scoped library installation** refers to two distinct approaches for installing additional Python libraries (and other language dependencies) on a Databricks compute resource. The choice determines the visibility and lifecycle of the installed library: compute-scoped libraries are available to all notebooks running on that compute resource, while notebook-scoped libraries are confined to a single notebook session. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Overview

[Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML) bundles many popular machine learning and deep learning libraries out of the box. However, users often need additional libraries not included in the runtime. Databricks provides two primary mechanisms for such installations, plus the option of using an init script. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Compute-Scoped Installation

Compute-scoped libraries are installed at the compute resource (cluster) level. Once installed, the library becomes available to **all notebooks** that run on that compute resource, across any user, for the entire lifetime of the resource (until the library is uninstalled or the resource is terminated).

**How to install:**
- Use the Databricks UI or API to [create a compute-scoped library](https://docs.databricks.com/aws/en/libraries/cluster-libraries#install-libraries).
- Alternatively, use an [init script](https://docs.databricks.com/aws/en/init-scripts/cluster-scoped) to install libraries during compute creation. Init scripts run before the cluster is ready for use, ensuring the library is available from the moment the cluster starts.

| Attribute | Detail |
|-----------|--------|
| Scope | All notebooks on the compute resource |
| Persistence | Persists across notebook sessions and restarts (until uninstalled) |
| Management overhead | Lower (install once, use everywhere on that compute) |

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Notebook-Scoped Installation

Notebook-scoped libraries are installed within a single notebook session using the `%pip` magic command or by calling `pip` directly from the notebook. The library is available **only for that specific notebook session** and is not shared with other notebooks on the same compute resource.

**How to install:**
- In a Python notebook, run `%pip install <package-name>`.
- Databricks also supports [Notebook-scoped Python libraries](https://docs.databricks.com/aws/en/libraries/notebooks-python-libraries) for version pinning and dependency management.

| Attribute | Detail |
|-----------|--------|
| Scope | Single notebook session |
| Persistence | Lost when the notebook session ends (detach or stop) |
| Management overhead | Higher (reinstall per session) |

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Choosing Between Compute-Scoped and Notebook-Scoped

The choice depends on the use case:

- **Compute-scoped** is ideal for libraries that are widely needed across multiple notebooks and users, or for packages that take a long time to install. It centralizes dependency management and reduces session startup time.
- **Notebook-scoped** is preferable for experimental work, one-off analyses, or when testing a library before committing it to a compute-scoped installation. It avoids interfering with other notebooks and allows each session to have an isolated environment.

Both approaches coexist: a notebook-scoped installation can override a compute-scoped library for that session, enabling flexible testing without affecting other users.

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The pre-configured runtime that includes many common ML libraries.
- Cluster-scoped libraries – The formal feature for compute-scoped installation.
- [Notebook-scoped Python libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md) – The feature for session-only installation.
- [Init scripts](/concepts/init-script-allowlisting.md) – An alternative method for compute-scoped installation at cluster start.
- Library Management Best Practices – Guidance on maintaining library versions and dependencies.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
