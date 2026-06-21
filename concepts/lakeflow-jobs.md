---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 302c49486a15152538a96fd30e62ac40fc8756b7b1d9236cc6d03e99c4f14cc0
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakeflow-jobs
    - Lakeflow Job
  citations:
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
title: Lakeflow Jobs
description: Databricks' job orchestration platform for running automated workflows, including Python wheel tasks, on AWS.
tags:
  - databricks
  - workflows
  - orchestration
timestamp: "2026-06-19T23:19:44.259Z"
---

# Lakeflow Jobs

**Lakeflow Jobs** is the job orchestration and scheduling service on Databricks that enables users to run data processing, machine learning, and analytics workloads as automated workflows. It provides a unified platform for creating, scheduling, monitoring, and managing production jobs.

## Overview

Lakeflow Jobs allows users to define workflows composed of one or more tasks, each of which can run different types of workloads, including Python scripts, notebooks, [Python Wheel Files](/concepts/python-wheel-files.md), and more. Jobs can be triggered on a schedule, on demand, or in response to events. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

The service is designed for production use cases, providing features such as automatic retries, alerting, and detailed run history for monitoring and debugging. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Task Types

Lakeflow Jobs supports multiple task types, including:

- **Notebook tasks** — Run Databricks notebooks as job tasks.
- **Python wheel tasks** — Execute Python applications packaged as wheel files, enabling fast and reliable installation of Python code in jobs. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]
- **Python script tasks** — Run arbitrary Python scripts.
- **SQL tasks** — Execute SQL queries on Databricks SQL warehouses.
- **dbt tasks** — Run dbt transformations.
- **Delta Live Tables (DLT) pipeline tasks** — Trigger DLT pipeline updates.

## Python Wheel Tasks

A Python [wheel file](/concepts/python-wheel-files.md) is a standard packaging format for distributing Python applications. Using the [Python Wheel Task](/concepts/python-wheel-task.md) in Lakeflow Jobs ensures fast and reliable installation of Python code. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Configuring a [Python Wheel Task](/concepts/python-wheel-task.md)

When creating a [Python Wheel Task](/concepts/python-wheel-task.md), you specify:

- **Package name** — The name of the Python package to import, matching the `name` parameter in `setup.py`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]
- **Entry point** — One of the values specified in the `entry_points` collection in `setup.py`, defining which function to call when the task runs. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]
- **Parameters** — Positional or keyword arguments passed to the [Python Wheel Task](/concepts/python-wheel-task.md) as command-line arguments. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Creating a Python Wheel for Jobs

To use a Python wheel in a Lakeflow Job, you first create a wheel file locally using `setuptools` and the `wheel` package. The `setup.py` file defines package metadata, including `entry_points` that specify which function serves as the task's entry point. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

Example `setup.py` structure:

```python
from setuptools import setup, find_packages

setup(
  name='my_test_package',
  version='0.0.1',
  packages=find_packages(include=['my_test_code']),
  entry_points={
    'group_1': 'run=my_test_code.__main__:main'
  },
  install_requires=[
    'setuptools'
  ]
)
```

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

The wheel file is built using the command `python3 setup.py bdist_wheel`, which creates a `.whl` file in the `dist/` directory. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Creating and Running Jobs

To create a job in Lakeflow Jobs:

1. Click **Jobs & Pipelines** in the sidebar.
2. Click **Create**, then **Job**.
3. Select a task type (e.g., **Python wheel**) to configure the first task.
4. Provide a task name, package name, entry point, and compute configuration.
5. Specify parameters as positional or keyword arguments.
6. Click **Create task**.

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

After creating a job, you can run it immediately or set up a schedule. Run details, including output and logs, are available in the **Runs** tab. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Monitoring and Debugging

Lakeflow Jobs provides a job run details view where you can inspect the status, duration, and output of each run. The **Output** pane displays task output, including any arguments passed to the task. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Related Concepts

- Workflows — The broader orchestration framework on Databricks.
- Job Clusters — Compute resources configured for job execution.
- Task Dependencies — Define execution order and conditional logic between tasks.
- Job Scheduling — Configure recurring job runs.
- Job Alerts — Set up notifications for job status changes.
- [Python Wheel File](/concepts/python-wheel-files.md) — Standard packaging format for Python applications.

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
