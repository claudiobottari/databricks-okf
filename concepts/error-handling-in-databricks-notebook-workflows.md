---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25b4aae6796fe6e5b78cf59723252aa163def9d973f1d8d377c9975c5a311da4
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-in-databricks-notebook-workflows
    - EHIDNW
    - Error Handling in Databricks
    - Error handling in Databricks
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: Error handling in Databricks notebook workflows
description: Strategies for handling errors and implementing retry logic when using dbutils.notebook.run(), which throws WorkflowException on failure.
tags:
  - databricks
  - error-handling
  - reliability
timestamp: "2026-06-19T19:53:07.796Z"
---

# Error Handling in Databricks Notebook Workflows

**Error Handling in Databricks Notebook Workflows** refers to the techniques and patterns for managing failures when using `dbutils.notebook.run()` to orchestrate notebook workflows. When a called notebook encounters an error, it throws a `WorkflowException` that must be caught and handled properly to build resilient pipelines.

## Understanding WorkflowException

When you use `dbutils.notebook.run()` to start a notebook as a job, any unhandled exception in the called notebook causes the `run()` call to throw a `WorkflowException` in the calling notebook. This exception propagates up the call stack unless explicitly caught, which would cause the parent notebook to fail as well. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Retry Pattern

A common pattern for handling errors in notebook workflows is to implement a retry mechanism with exponential backoff. The following Python example defines a `run_with_retry` function that retries a notebook run up to a specified maximum number of attempts if a `WorkflowException` is thrown: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

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

run_with_retry("LOCATION_OF_CALLEE_NOTEBOOK", 60, max_retries = 5)
```

The function catches the `Exception` (which includes `WorkflowException`) and retries. If the number of retries exceeds the specified maximum, it re-raises the original exception. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Timeout Errors

The `timeout_seconds` parameter in `dbutils.notebook.run()` controls how long the calling notebook waits for the called notebook to complete. A value of `0` means no timeout. If the called notebook does not finish within the specified time, the `run()` call throws an exception. Additionally, if Databricks is down for more than 10 minutes, the notebook run fails regardless of the `timeout_seconds` value. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Jobs Created via dbutils.notebook.run

Jobs created using the `dbutils.notebook` API must complete in 30 days or less. Any job exceeding this duration will fail. This is a system-enforced upper bound on execution time. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Error Handling vs. %run

It is important to note that the error handling patterns described here apply only to `dbutils.notebook.run()`, not to `%run`. When using `%run` to import a notebook, the called notebook executes inline in the same JVM. If the `%run` notebook fails, the error propagates immediately to the calling notebook without an opportunity to catch it programmatically — `%run` must be in a cell by itself and cannot be wrapped in a try-except block. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Best Practices

- Wrap calls to `dbutils.notebook.run()` in try-except blocks to handle transient failures.
- Implement retry logic with a maximum retry count to avoid infinite loops.
- Use the `timeout_seconds` parameter to prevent hanging workflows.
- Return meaningful exit values from called notebooks using `dbutils.notebook.exit()` to signal success or failure status to the calling notebook.
- Consider the 30-day job duration limit when designing long-running workflows.

## Related Concepts

- [dbutils.notebook.run()](/concepts/dbutilsnotebookrun.md) — The API method used to start notebook jobs
- %run — The inline notebook inclusion command, which does not support error handling
- Databricks Workflows — Job orchestration framework on Databricks
- [Notebook Modularization](/concepts/databricks-notebook-code-modularization.md) — Techniques for organizing code across notebooks
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — Scheduled and triggered job execution

## Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
