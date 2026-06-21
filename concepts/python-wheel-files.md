---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8215daaa7fec5d67483d0f9db802d8a3cd32ac376cba194786daa6add7134da4
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-wheel-files
    - PWF
    - Python Wheel File
    - Python wheel file
    - Python Wheel File Dependencies
    - wheel file
  citations:
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
title: Python Wheel Files
description: A standard packaging format (.whl) for distributing Python applications, containing code, metadata, and dependencies.
tags:
  - python
  - packaging
  - distribution
timestamp: "2026-06-19T23:21:06.076Z"
---

# Python Wheel Files

A **Python wheel file** is a standard packaging format (PEP 427) used to bundle and distribute the files required to run a Python application.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md] Wheels are a binary distribution format that enable faster and more reliable installation compared to source distributions, as they eliminate the need for the end-user to run the build process during installation.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Overview

Python wheel files (`.whl` extension) package Python code and its dependencies into a single archive that can be directly installed. The wheel format contains a built distribution of a package, meaning the source code has already been compiled into bytecode and the package is ready for installation on the target system.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Structure

A wheel file is a ZIP archive that contains:

1. **Package metadata** — Information about the package, including its name, version, author, and dependencies.
2. **Python source files** — The compiled or source code that constitutes the application.
3. **Entry points** — Definitions that specify how the package should be invoked, which are critical for running the package as a task in a workflow system.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Creating a Python Wheel File

To create a Python wheel, a developer typically:

1. Writes the Python application code and package metadata files (such as `__init__.py` and `__main__.py`).
2. Defines a `setup.py` script using `setuptools` to specify package metadata, including the package name, version, author, and entry points.
3. Runs the build command to generate the wheel file.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

The standard build command is:

```bash
python3 setup.py bdist_wheel
```

This command produces a wheel file, typically saved to a `dist/` directory, with a filename of the form `my_test_package-0.0.1-py3-none-any.whl`.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Package Name and Entry Points

In the context of Databricks workflows, the `setup.py` script defines two critical pieces of metadata:

- **Package name** — The value assigned to the `name` parameter in `setup.py`. This is the name used to import the package.
- **Entry points** — Defined in the `entry_points` collection in `setup.py`. The value before `=` in each entry point (e.g., `run`) is the name of the entry point and is used to configure the [Python Wheel Task](/concepts/python-wheel-task.md) in a workflow.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Using Python Wheel Files in [Lakeflow Jobs](/concepts/lakeflow-jobs.md)

A [Python Wheel Task](/concepts/python-wheel-task.md) allows users to run packaged Python code as part of a Databricks job. The workflow integration supports the wheel format because it provides fast and reliable installation of the packaged code into the job's execution environment.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Configuring a [Python Wheel Task](/concepts/python-wheel-task.md)

When creating a job to run a Python wheel:

1. **Package name** — Enter the name of the Python package to import. This corresponds to the `name` parameter in `setup.py`.
2. **Entry point** — Specify one of the values from the `entry_points` collection in `setup.py`. This tells the job which function to call as the main entry point for the application.
3. **Parameters** — Provide positional or keyword arguments as command-line arguments to the [Python Wheel Task](/concepts/python-wheel-task.md).^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Passing Arguments

Arguments are passed to the [Python Wheel Task](/concepts/python-wheel-task.md) as command-line arguments:

- **Positional arguments** — Entered as a JSON-formatted array of strings (e.g., `["first argument","first value","second argument","second value"]`).
- **Keyword arguments** — Added as key-value pairs using the **+ Add** button.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

The `sys.argv` list in the Python script receives these arguments at runtime.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### Workflow Integration

When a Python wheel file is used as a task in a job:

- The wheel file is uploaded to the Databricks workspace.
- The job provisions a compute cluster and installs the wheel into the cluster environment.
- The task executes the entry point function with the provided arguments.
- Output from the task is displayed in the job run's **Output** pane when the run completes.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Advantages over Source Distributions

Python wheel files offer several benefits over source distributions (tarballs, `.tar.gz`):

- **Faster installation** — No need to run the build step on the target machine; the package is ready to install.
- **Smaller size** — Wheels can exclude test files and other artifacts not needed at runtime.
- **Reliable dependency resolution** — Wheels declare their dependencies explicitly, making them compatible with dependency resolvers like `pip`.^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]
- **Deterministic build** — The wheel format ensures that the same binary is installed regardless of the target platform (for pure-Python wheels) or that platform-specific builds are available for binary extensions.

## Related Concepts

- PEP 427 — The Python packaging standard that defines the wheel format.
- setuptools — The package used to build and distribute Python wheels.
- [Python Wheel Task](/concepts/python-wheel-task.md) — A Databricks job task type that runs a Python wheel file.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The Databricks job execution system that supports wheel tasks.
- pip — The Python package installer, used to install wheel packages.
- bdist_wheel — The setuptools command that builds a wheel file.
- [Entry points](/concepts/mlflow-project-entry-points.md) — Invokable functions defined in the wheel's metadata.

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
