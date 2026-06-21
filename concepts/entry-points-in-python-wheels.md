---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 699ca13446320963ca78a12475b28e98e72f112465698991fd50a83c65002c84
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - entry-points-in-python-wheels
    - EPIPW
    - entry point for the package
  citations:
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
      start: 60
      end: 75
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
      start: 88
      end: 95
title: Entry Points in Python Wheels
description: A mechanism in setup.py that maps a named entry point to a specific function in the package, used to define which code runs when a wheel task executes.
tags:
  - python
  - packaging
  - setup.py
timestamp: "2026-06-19T23:19:53.815Z"
---

# Entry Points in Python Wheels

**Entry Points in Python Wheels** are a standard mechanism defined in `setup.py` that tell the Python package installer how a package should be invoked as a command, task, or plugin. In the context of a Python wheel distributed via [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md), entry points specify which function in the wheel should be called when the job task runs. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Structure of an Entry Point

An entry point is declared in the `entry_points` argument of `setup()` in `setup.py`. Each entry point consists of:

- **Group** – A logical category (for example, `console_scripts`, `group_1`, or a plugin namespace).
- **Name** – The command or task name that users (or systems) use to reference the entry point.
- **Value** – A string in the format `module:function`, where `module` is the importable Python module path and `function` is the callable to execute. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

For example, the following `setup.py` snippet defines a single entry point named `run` inside the group `group_1`:

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

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md#L60-L75]

In this example:
- The group is `group_1` (a custom group, though `console_scripts` is the most common standard group).
- The entry point name is `run`.
- The function that gets called is `my_test_code.__main__.main`.

## Entry Points in a Databricks Job

When a Databricks Jobs|Job uses a [Python Wheel Task](/concepts/python-wheel-task.md), the **Entry point** field in the task configuration must match the name of one of the entry points defined in the wheel’s `setup.py`. In the example above, the entry point name is `run`. During job execution, Databricks calls the function referenced by that entry point (`my_test_code.__main__.main`) and passes any defined parameters as command–line arguments. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md#L88-L95]

## Related Concepts

- setuptools – The Python packaging library that processes `entry_points`.
- console_scripts – The most common entry point group used to install command‑line scripts.
- __main__.py – The typical file that contains the entry‑point function.
- setup.py – The metadata file where entry points are declared.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) – The workflow system that uses entry points to launch wheel tasks.

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
2. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md:60-75](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
3. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md:88-95](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
