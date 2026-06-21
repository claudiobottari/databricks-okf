---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6acbddee6d7af0cf974781098bb350c13e8aa364dde0a466cba3ca59f461246
  pageDirectory: concepts
  sources:
    - use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configuring-a-lakeflow-job-for-python-wheels
    - CALJFPW
  citations:
    - file: use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md
title: Configuring a Lakeflow Job for Python Wheels
description: The step-by-step process of creating a Databricks job that uses a Python wheel task, including specifying package name, entry point, compute resources, and the wheel file itself.
tags:
  - databricks
  - jobs
  - configuration
timestamp: "2026-06-19T23:20:07.412Z"
---

# Configuring a Lakeflow Job for Python Wheels

**Configuring a Lakeflow Job for Python Wheels** describes how to package a Python application as a [wheel file](https://peps.python.org/pep-0427/) and run it as a task in a [Lakeflow Job](/concepts/lakeflow-jobs.md) on Databricks. Using a [Python Wheel Task](/concepts/python-wheel-task.md) ensures fast and reliable installation of Python code in jobs by bundling all dependencies and entry points into a single distributable artifact. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Before you begin

To follow the example, you need:

- Python 3 installed on your local machine.
- The Python `wheel` and `setuptools` packages, which can be installed via `pip install wheel setuptools`.

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Step 1: Create a local directory for the example

Create a local directory to hold the example code and generated artifacts, for example `databricks_wheel_test`. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Step 2: Create the example Python script

Create a Python script that will serve as the entry point of the wheel. Save it as `my_test_code/__main__.py`:

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

Create a metadata file `my_test_code/__init__.py`:

```python
__version__ = "0.0.1"
__author__ = "Databricks"
```

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Step 3: Create the setup.py script

The `setup.py` script defines the package metadata and entry points used by the Databricks workflow. In the example below, the value before `=` in `entry_points` (here `run`) is the name of the entry point used to configure the [Python Wheel Task](/concepts/python-wheel-task.md).

Save the following as `setup.py` in the root of your directory:

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

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Step 4: Build the Python wheel file

From the directory containing `setup.py`, run the following command:

```bash
python3 setup.py bdist_wheel
```

This creates the wheel file and saves it to `dist/my_test_package-0.0.1-py3.none-any.whl`.

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Step 5: Create a Lakeflow Job to run the Python wheel file

1. In your Databricks workspace, click the **Jobs & Pipelines** icon in the sidebar.
2. Click **Create**, then **Job**.
3. Click the **Python wheel** tile to configure the first task. If the tile is not visible, click **Add another task type** and search for **Python wheel**.
4. Optionally rename the job from the default **New Job `<date-time>`**.
5. Enter a name for the task.
6. In **Type**, select **Python wheel** if not already selected.
7. In **Package name**, enter `my_test_package` (the value of the `name` parameter in `setup.py`).
8. In **Entry point**, enter `run` (the entry point name defined in `setup.py`).
9. In **Compute**, select an existing Job Cluster|job cluster or create a new one.
10. Specify your Python wheel file by uploading it or referencing a workspace path.
11. Under **Parameters**:
    - Choose **Positional arguments** and enter a JSON-formatted array of strings, e.g. `["first argument","first value","second argument","second value"]`.
    - Or choose **Keyword arguments** and add key-value pairs.
12. Click **Create task**.

^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Step 6: Run the job and view results

Click the **Run Now** button to start the workflow. To view run details, click the **Runs** tab and then the link in the **Start time** column for the run. When the run completes, the output appears in the **Output** pane, including the arguments passed to the task. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Next steps

To learn more about creating and running jobs, see [Lakeflow Jobs](/concepts/lakeflow-jobs.md) documentation. ^[use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md]

## Related concepts

- [Python wheel file](/concepts/python-wheel-files.md) – Standard format for Python package distribution.
- [Entry points](/concepts/mlflow-project-entry-points.md) – Named functions defined in `setup.py` that serve as task entry points.
- Job clusters – Compute resources for running Lakeflow tasks.
- Workflows – Orchestration of multiple tasks in a job.

## Sources

- use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws.md](/references/use-a-python-wheel-file-in-lakeflow-jobs-databricks-on-aws-889ac45c.md)
