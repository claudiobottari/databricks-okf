---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b89aa5b852ad830e3503f6bc1fc324753e7e2f18953f18b66bc02d0fe26e3b7
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-wheel-task
    - PWT
    - Python Wheel
    - Python wheel
    - Python
  citations:
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
title: Python Wheel Task
description: A Databricks Jobs task type that runs applications packaged as Python wheel files, enabling fast and reliable code execution.
tags:
  - databricks
  - jobs
  - python
timestamp: "2026-06-19T23:20:01.967Z"
---

# Python Wheel Task

A **Python Wheel Task** is a job task type in Databricks [Lakeflow Jobs](/concepts/lakeflow-jobs.md) that runs an application packaged as a Python wheel file. Using a Python wheel ensures fast and reliable installation of Python code in jobs because a wheel is a standard, pre-built distribution format (see [PEP 427](https://peps.python.org/pep-0427/)). ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Overview

To use a Python wheel task, you first create a Python wheel file from your code, then configure a job to reference that wheel and specify the entry point to execute. The task supports both positional and keyword arguments, which are passed as command-line arguments to the entry point. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Creating a Python Wheel File

The wheel file is built using `setuptools` and the `wheel` package. The example below demonstrates a minimal Python package `my_test_code` with an entry point script `__main__.py` and a `setup.py` configuration.

### Example Package Structure

```text
databricks_wheel_test/
├── my_test_code/
│   ├── __init__.py
│   └── __main__.py
└── setup.py
```

### Entry Point Script (`my_test_code/__main__.py`)

```python
"""The entry point of the Python Wheel"""
import sys

def main():
    # This method will print the provided arguments
    print('Hello from my func')
    print('Got arguments:')
    print(sys.argv)

if __name__ == '__main__':
    main()
```

The `main()` function is the function that will be invoked when the wheel is run. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Package Metadata (`my_test_code/__init__.py`)

```python
__version__ = "0.0.1"
__author__ = "Databricks"
```

### `setup.py`

```python
from setuptools import setup, find_packages
import my_test_code

setup(
  name='my_test_package',
  version=my_test_code.__version__,
  author=my_test_code.__author__,
  url='https://databricks.com',
  author_email='john.doe@databricks.com',
  description='my test wheel',
  packages=find_packages(include=['my_test_code']),
  entry_points={
    'group_1': 'run=my_test_code.__main__:main'
  },
  install_requires=[
    'setuptools'
  ]
)
```

The `entry_points` dictionary defines the entry point(s) for the wheel. In this example, `run` is the name of the entry point and maps to `my_test_code.__main__:main`. This `run` value is used later when configuring the Python wheel task. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Building the Wheel

From the directory containing `setup.py`, run:

```bash
python3 setup.py bdist_wheel
```

This creates the wheel file, e.g., `dist/my_test_package-0.0.1-py3-none-any.whl`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Creating a Job with a Python Wheel Task

1. In your workspace, click **Jobs & Pipelines** in the sidebar.
2. Click **Create**, then **Job**.
3. Click the **Python wheel** tile to configure the first task. If the tile is not available, click **Add another task type** and search for **Python wheel**.
4. Optionally, rename the job.
5. In **Task name**, enter a name for the task.
6. If necessary, select **Python wheel** from the **Type** drop-down.
7. In **Package name**, enter `my_test_package`. This is the value of the `name` parameter in `setup.py`.
8. In **Entry point**, enter `run`. This matches the entry point name defined in the `entry_points` collection.
9. In **Compute**, select an existing job cluster or **Add new job cluster**.
10. Specify the Python wheel file location.
11. In **Parameters**, choose **Positional arguments** or **Keyword arguments**:
    - Positional arguments are entered as a JSON array of strings, e.g., `["first argument","first value","second argument","second value"]`.
    - Keyword arguments are entered as key-value pairs.
    Both types are passed to the Python wheel task as command-line arguments.
12. Click **Create task**. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Running the Job and Viewing Results

Click **Run Now** to execute the workflow. After the run completes, the output (including any printed arguments) appears in the **Output** pane of the run details. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Related Concepts

- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The orchestration service for running tasks.
- Python Wheel — The standard Python packaging format.
- Job Compute — Clusters used to execute job tasks.
- Parameter Passing in Jobs — How arguments are supplied to tasks.

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
