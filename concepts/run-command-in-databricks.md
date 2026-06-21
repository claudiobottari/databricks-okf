---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dacf940191abf98d455b3c8620cbdac4a098ce808660be9206ef16f38b97177a
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - run-command-in-databricks
    - "%CID"
    - CI/CD
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: "%run command in Databricks"
description: A magic command that imports and executes another notebook inline, making its functions and variables available in the calling notebook.
tags:
  - databricks
  - notebook-orchestration
  - code-modularization
timestamp: "2026-06-19T19:52:27.848Z"
---

# `%run` command in Databricks

The **`%run`** command is a Databricks notebook magic that allows you to include and execute the contents of another notebook within the current notebook. It is primarily used for [code modularization](/concepts/databricks-notebook-code-modularization.md) – placing shared functions or configuration in a separate notebook and reusing them across multiple notebooks – and for chaining notebooks that represent the steps of an analysis pipeline. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Key characteristics

When you use `%run`, the called notebook is executed immediately and inline. All functions, variables, and temporary views defined in the called notebook become available in the calling notebook after the `%run` cell finishes. This makes `%run` a simple tool for sharing code without packaging it as a library. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Usage

The `%run` command must appear in a notebook cell **by itself** – it cannot be combined with other code in the same cell. The path to the target notebook can be specified as:

- A **relative path** using the `./` prefix to refer to a notebook in the same directory: `%run ./shared-code-notebook`
- A **subdirectory relative path**: `%run ./dir/notebook`
- An **absolute path**: `%run /Users/username@organization.com/directory/notebook`

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

When the target notebook contains Databricks widgets, `%run` executes it using the widget’s default values by default. You can override these values by passing parameters; see the Databricks widgets documentation for details. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Limitations

- `%run` **cannot** be used to run a Python file (`.py`) and import its contents. To reuse code from a Python file, use workspace files, package the code as a Python library, or install a library on the cluster. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Because the called notebook runs inline, any side effects (such as modifying global state) are immediately visible in the calling notebook. This can be useful but also requires careful management of namespaces.
- `%run` does not support returning a value or passing parameters in the same way as [dbutils.notebook.run()](/concepts/dbutilsnotebookrun.md).

## Comparison with `dbutils.notebook.run()`

While `%run` executes the target notebook inline in the same JVM, the `dbutils.notebook.run()` method starts a **new job** to run the notebook asynchronously. `dbutils.notebook.run()` allows you to pass parameters and retrieve a return value (a string), enabling more complex workflows such as conditional branching and retry logic. However, `%run` is simpler and directly shares the namespace, making it ideal for importing helper functions. Both methods are complements: use `%run` for modularization and `dbutils.notebook.run()` for orchestration with dependencies. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Related concepts

- [dbutils.notebook.run()](/concepts/dbutilsnotebookrun.md)
- Databricks notebooks
- Databricks widgets
- workspace files
- [code modularization](/concepts/databricks-notebook-code-modularization.md)
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)

## Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
