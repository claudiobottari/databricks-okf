---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11b7eb524adf7f1c63ea18cb0f6edd70e8b0e2c3e2b5247c9e7f21bbd5eda3fa
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - building-python-wheels-with-setuptools
    - BPWWS
  citations:
    - file: filename.md
    - file: source-a.md
    - file: source-b.md
    - file: filename.md:START-END
    - file: filename.md#LSTART-LEND
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
title: Building Python Wheels with setuptools
description: The process of using setuptools and the wheel package to compile Python source code into a .whl distribution file via the 'python3 setup.py bdist_wheel' command.
tags:
  - python
  - packaging
  - build-tools
timestamp: "2026-06-19T23:20:42.838Z"
---

You are a wiki author. Write a clear, well-structured markdown page about "Building Python Wheels with setuptools".
Draw facts only from the provided source material.
Include a ## Sources section at the end listing the source document.
Suggest wikilinks to related concepts where appropriate.
Write in a neutral, informative tone. Be concise but thorough.

Source attribution: at the end of each prose paragraph, append a citation
marker showing which source file(s) the paragraph drew from.
Format: ^[filename.md] for single-source, ^[source-a.md, source-b.md] for multi-source.
When a single sentence makes a specific factual claim and you can identify the
exact line range it came from, you may use the claim-level form
^[filename.md:START-END] (or ^[filename.md#LSTART-LEND]) at the end of that
sentence — START and END are 1-indexed line numbers in the source file.
Paragraph-level citations remain the default; only switch to claim-level form
when it materially improves verifiability and the line range is unambiguous.
Place citations only at the end of prose paragraphs or sentences — not on
headings, list items, or code blocks.
Source filenames are visible as `--- SOURCE: filename.md ---` headers in the content below.

If a paragraph is your inference rather than a direct extraction, leave it
uncited — downstream lint rules will count uncited paragraphs as 'inferred'
to compute the page's provenance metadata.



Related wiki pages for cross-referencing:

---
title: my_test_package package
summary: Python package that contains the __main__.py entry point and uses setuptools to build a wheel for Databricks [Lakeflow Jobs](/concepts/lakeflow-jobs.md).
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:44:21.953Z"
updatedAt: "2026-06-20T10:44:21.953Z"
tags:
  - databricks
  - jobs
  - python-wheel
aliases: []
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: Python wheel
summary: A standard packaging format for Python applications; used with the [Python Wheel Task](/concepts/python-wheel-task.md) in Databricks Jobs to run packaged code reliably and efficiently.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:34:13.298Z"
updatedAt: "2026-06-20T10:34:13.298Z"
tags:
  - databricks
  - packaging
  - python
aliases:
  - Python wheel file
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: setuptools
summary: A Python packaging library used to create Python wheel distributions; works with the `setup.py` script to define package metadata, entry points, and dependencies.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:34:55.158Z"
updatedAt: "2026-06-20T10:34:55.158Z"
tags:
  - databricks
  - packaging
  - python
aliases: []
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: entry_points
summary: A dictionary in setup.py that maps entry point group names to callable functions; used by the [Python Wheel Task](/concepts/python-wheel-task.md) to determine which function to invoke.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:35:42.126Z"
updatedAt: "2026-06-20T10:35:42.126Z"
tags:
  - databricks
  - packaging
  - python-wheel
  - setup.py
aliases: []
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: setuptools.setup
summary: The primary function in setuptools used to configure package metadata, dependencies, and entry points in a setup.py script.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:36:16.080Z"
updatedAt: "2026-06-20T10:36:16.080Z"
tags:
  - packaging
  - python
  - setuptools
aliases: []
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: find_packages
summary: A setuptools utility function that automatically discovers Python packages in the project directory based on include/exclude patterns.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:36:57.363Z"
updatedAt: "2026-06-20T10:36:57.363Z"
tags:
  - packaging
  - python
  - setuptools
aliases: []
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: bdist_wheel
summary: A setuptools command that compiles the package artifacts into a .whl file suitable for distribution and installation via pip.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: command
createdAt: "2026-06-20T10:37:33.430Z"
updatedAt: "2026-06-20T10:37:33.430Z"
tags:
  - packaging
  - python
  - setuptools
  - wheel
aliases:
  - python3 setup.py bdist_wheel
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: Databricks Jobs
summary: A workflow orchestration service on Databricks that runs tasks including Python wheel tasks and other job types.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:49:38.730Z"
updatedAt: "2026-06-20T10:49:38.730Z"
tags:
  - databricks
  - jobs
aliases:
  - [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

---
title: __main__.py
summary: A Python module that serves as the entry point for a package; when a wheel runs in a Databricks job, __main__.py's main() function is called by setuptools entry_points.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:50:20.048Z"
updatedAt: "2026-06-20T10:50:20.048Z"
tags:
  - python
  - packaging
aliases: []
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

---
title: __init__.py
summary: A file marking a directory as a Python package; typically contains metadata like __version__ and __author__.
sources:
  - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:51:00.317Z"
updatedAt: "2026-06-20T10:51:00.317Z"
tags:
  - python
  - packaging
aliases: []
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Building Python Wheels with setuptools

**Building Python Wheels with setuptools** describes the process of packaging Python applications into the `.whl` format, which is the standard distribution format for Python code as defined by PEP 427. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md] Wheels are used to ensure fast and reliable installation of Python code. This page explains the steps required to create a Python wheel from a sample project using `setuptools`.

## Prerequisites

Building a wheel requires Python 3 and the `wheel` and `setuptools` Python packages. Both can be installed via `pip`: ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

```bash
pip install wheel setuptools
```

## Project Structure

To build a wheel, you must first create a project directory and organize your Python source code. A typical structure includes:

- A main script that serves as the [entry point for the package](/concepts/entry-points-in-python-wheels.md) — conventionally named `__main__.py` inside a package directory.
- A package initialization file (`__init__.py`) that contains metadata such as `__version__` and `__author__`.
- A `setup.py` script at the project root that defines the package configuration for setuptools.

The following example assumes a project directory such as `databricks_wheel_test`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Creating the Python Source Files

### `__main__.py`

The entry point script handles command-line arguments and contains the main logic. The example below defines a `main()` function that prints the arguments passed to the script: ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

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

This file should be saved at the path `my_test_code/__main__.py`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

### `__init__.py`

A minimal `__init__.py` stores package‑level metadata. Create it at `my_test_code/__init__.py`: ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

```python
__version__ = "0.0.1"
__author__ = "Databricks"
```

## Configuring `setup.py`

The `setup.py` script is the configuration file that setuptools uses to build the wheel. It imports find_packages from setuptools to automatically discover sub‑packages and calls setuptools.setup with the package metadata. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

The `entry_points` dictionary defines the name of the entry point that can be invoked at runtime. In each value of `entry_points`, the identifier before the `=` sign (e.g., `run`) becomes the entry point name. This name is used to configure a [Python Wheel Task](/concepts/python-wheel-task.md) in [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md). ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

Save this script to a file named `setup.py` in the root of the project directory: ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

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

## Building the Wheel

With the `setup.py` script in place, run the bdist_wheel command from the project root: ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

```bash
python3 setup.py bdist_wheel
```

This command creates the Python wheel file and saves it. For the example above, the output is placed at `dist/my_test_package-0.0.1-py3.none-any.whl`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Using the Wheel in Databricks Jobs

A built wheel can be uploaded and used in a [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) task of type **Python wheel**. During task configuration, the **Package name** field must match the value assigned to the `name` parameter in `setup.py` (e.g., `my_test_package`), and the **Entry point** field must match one of the entry point names defined in the `entry_points` dictionary (e.g., `run`). Arguments can be passed to the task as positional or keyword arguments; they are provided to the Python script as command‑line arguments. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Related Concepts

- Python wheel
- setuptools
- entry_points
- bdist_wheel
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md)
- my_test_package package

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. filename.md
2. source-a.md
3. source-b.md
4. filename.md:START-END
5. filename.md#LSTART-LEND
6. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
