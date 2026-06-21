---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f00915a8c10856ad462698e26282c2f04b64adcfbfb686e783e60cec12448a02
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parameter-passing-in-python-wheel-tasks
    - PPIPWT
  citations:
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
title: Parameter Passing in Python Wheel Tasks
description: How positional arguments (JSON array of strings) and keyword arguments (key-value pairs) are passed to a Python wheel task as command-line arguments.
tags:
  - databricks
  - jobs
  - parameters
timestamp: "2026-06-19T23:20:11.550Z"
---

# Parameter Passing in Python Wheel Tasks

**Parameter Passing in Python Wheel Tasks** refers to how arguments and configuration values are supplied to a Python application packaged as a wheel file when it is executed as a task in a Databricks Lakeflow Job. Parameters are passed as command‑line arguments to the Python entry point defined in the wheel’s metadata. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Types of Parameters

The Databricks job UI supports two categories of parameters for Python wheel tasks:

- **Positional arguments**: These are entered as a JSON‑formatted array of strings. For example, `["first argument","first value","second argument","second value"]`. The array is passed in order to the script. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]
- **Keyword arguments**: These are entered as key‑value pairs in the UI (click **+ Add** and provide a key and value). Multiple keyword arguments can be added by clicking **+ Add** again. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

Both positional and keyword arguments are ultimately forwarded to the [Python Wheel Task](/concepts/python-wheel-task.md) as **command‑line arguments**. The script’s entry point receives them via `sys.argv`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## How Parameters Are Received by the Wheel

The [Python Wheel Task](/concepts/python-wheel-task.md) executes the entry point defined in `setup.py` (for example, `run=my_test_code.__main__:main`). The `main()` function receives the arguments through `sys.argv`, just like any script run from the command line. A simple example entry point prints the provided arguments: ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

```python
import sys

def main():
    print('Hello from my func')
    print('Got arguments:')
    print(sys.argv)
```

If the wheel is called with positional arguments `["alpha", "beta"]`, the output would show `['alpha', 'beta']` in `sys.argv`. Keyword arguments are similarly flattened into the list; the exact order depends on the UI submission mechanism.

## Configuring Parameters in the Job UI

When creating or editing a [Python Wheel Task](/concepts/python-wheel-task.md) in the Databricks job UI:

1. In the **Parameters** section, choose either **Positional arguments** or **Keyword arguments**.
2. For positional arguments, enter the JSON array directly.
3. For keyword arguments, add keys and values using the **+ Add** button.
4. The task’s **Package name** (e.g., `my_test_package`) and **Entry point** (e.g., `run`) must match the values in the wheel’s `setup.py` — the entry point determines which function receives the arguments. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Related Concepts

- [Python wheel file](/concepts/python-wheel-files.md) – The packaging format used for the task.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – The workflow orchestration platform where wheel tasks run.
- Entry point configuration – How `setup.py` defines the function that processes parameters.
- Command‑line argument parsing – Techniques for parsing `sys.argv` in the entry point.
- Positional vs keyword arguments – The two UI‑supported parameter types.

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
