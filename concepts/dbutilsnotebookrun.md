---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 860825d35bb692a8cd727e4915472b6e03c678d7d8d19348ac983ea858d8d4ba
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsnotebookrun
    - dbutils.notebook
    - DBUtils
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: dbutils.notebook.run()
description: An API method to call a Databricks notebook as a separate job, supporting parameter passing via widgets and return values via dbutils.notebook.exit().
tags:
  - databricks
  - notebook-orchestration
  - api
timestamp: "2026-06-19T19:52:26.541Z"
---

## `dbutils.notebook.run()`

**`dbutils.notebook.run()`** is a method in the dbutils API on Databricks that starts an ephemeral job to execute another notebook as a separate process. It enables the orchestration of complex workflows by passing parameters to a target notebook, retrieving its exit value, and handling dependencies such as conditional branching or retries. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Overview

The method is available in Python and Scala notebooks. It complements the `%run` magic command: while `%run` imports a notebook inline (making its functions and variables available in the current scope), `dbutils.notebook.run()` launches a separate job, allowing parameter passing and return values that `%run` cannot provide. For example, you can get a list of files in a directory and pass the names to a called notebook, or create if‑then‑else workflows based on the return value. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Syntax

```python
dbutils.notebook.run(path: String, timeout_seconds: int, arguments: Map): String
```

The method takes three parameters:

- **`path`** – The workspace path to the target notebook (relative or absolute).
- **`timeout_seconds`** – The maximum time in seconds before the run times out. A value of `0` means no timeout. If the run does not complete within the specified time, an exception is thrown. If Databricks is down for more than 10 minutes, the run fails regardless of `timeout_seconds`.
- **`arguments`** – A map of key‑value pairs that set widget values in the target notebook. For example, if the target notebook has a widget named `A`, passing `{"A": "B"}` causes the widget to return `"B"`. Only Latin characters (ASCII) are accepted in the arguments map; non‑ASCII characters cause an error.

The return value is a string produced by the target notebook’s call to `dbutils.notebook.exit()`. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Behavior

- Jobs created via `dbutils.notebook.run()` are ephemeral and run immediately.
- The called notebook executes in its own job context. Variables and functions defined in it are **not** available in the calling notebook after completion.
- The target notebook can be written in R, even though `dbutils.notebook.run()` is only callable from Python or Scala. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Jobs must complete within 30 days; otherwise, the run fails. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Comparison with `%run`

| Feature | `dbutils.notebook.run()` | `%run` |
|---------|--------------------------|--------|
| Execution model | Starts a new job (separate process) | Imports notebook inline in the same JVM |
| Parameter passing | Yes, via the `arguments` map | Limited; can set widget defaults only |
| Return value | String via `dbutils.notebook.exit()` | None |
| Access to definitions | No | Yes, functions and variables become available |
| Language support | Python and Scala (caller) | Python, Scala, R, SQL |
| Suitable for | Workflows with dependencies, scheduling, conditional logic | Code modularization, shared libraries |

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Error handling

Errors from `dbutils.notebook.run()` throw a `WorkflowException`. The following example shows a retry wrapper:

```python
def run_with_retry(notebook, timeout, args = {}, max_retries = 3):
  num_retries = 0
  while True:
    try:
      return dbutils.notebook.run(notebook, timeout, args)
    except Exception as e:
      if num_retries > max_retries:
        raise e
      else:
        print("Retrying error", e)
        num_retries += 1
```

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Passing structured data between notebooks

Because `dbutils.notebook.exit()` only accepts a single string, you can pass larger or structured data indirectly:

- **Temporary views** – The called notebook creates a global temporary view and returns its name. The caller reads the view.
- **DBFS** – The called notebook writes a dataset to DBFS and returns the path. The caller loads it.
- **JSON** – Serialize multiple values as JSON in the called notebook and deserialize them in the caller.

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Running multiple notebooks concurrently

Standard concurrency constructs (Python `threading` or Scala `Futures`) can be used to run several notebooks in parallel via `dbutils.notebook.run()`. Databricks provides example notebooks demonstrating this pattern. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Related concepts

- dbutils.notebook.exit() – The companion method for returning values.
- %run – The inline notebook import command.
- Databricks notebooks – Basic unit of execution.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – Alternative orchestration method.
- Widgets – Used to parameterize notebooks.
- DBFS – Storage layer for passing large data between notebooks.

### Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
