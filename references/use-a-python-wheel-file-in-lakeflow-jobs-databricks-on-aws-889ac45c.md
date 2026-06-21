---
title: Use a Python wheel file in Lakeflow Jobs | Databricks on AWS
source: https://docs.databricks.com/aws/en/jobs/how-to/use-python-wheels-in-workflows
ingestedAt: "2026-06-18T08:07:55.669Z"
---

A Python [wheel file](https://peps.python.org/pep-0427/) is a standard way to package and distribute the files required to run a Python application. Using the Python wheel task, you can ensure fast and reliable installation of Python code in your jobs. This article provides an example of creating a Python wheel file and a job that runs the application packaged in the Python wheel file. In this example, you:

*   Create the Python files defining an example application.
*   Bundle the example files into a Python wheel file.
*   Create a job to run the Python wheel file.
*   Run the job and view the results.

## Before you begin[​](#before-you-begin "Direct link to before-you-begin")

You need the following to complete this example:

*   Python3
    
*   The Python `wheel` and `setuptool` packages. You can use `pip` to install these packages. For example, you can run the following command to install these packages:
    
    Bash
    
        pip install wheel setuptools
    

## Step 1: Create a local directory for the example[​](#step-1-create-a-local-directory-for-the-example "Direct link to step-1-create-a-local-directory-for-the-example")

Create a local directory to hold the example code and generated artifacts, for example, `databricks_wheel_test`.

## Step 2: Create the example Python script[​](#step-2-create-the-example-python-script "Direct link to step-2-create-the-example-python-script")

The following Python example is a simple script that reads input arguments and prints out those arguments. Copy this script and save it to a path called `my_test_code/__main__.py` in the directory you created in the previous step.

Python

    """The entry point of the Python Wheel"""import sysdef main():  # This method will print the provided arguments  print('Hello from my func')  print('Got arguments:')  print(sys.argv)if __name__ == '__main__':  main()

The following file contains metadata describing the package. Save this to a path called `my_test_code/__init__.py` in the directory you created in step 1.

Python

    __version__ = "0.0.1"__author__ = "Databricks"

## Step 4: Create the Python wheel file[​](#step-4-create-the-python-wheel-file "Direct link to step-4-create-the-python-wheel-file")

Converting the Python artifacts into a Python wheel file requires specifying package metadata such as the package name and entry points. The following script defines this metadata.

note

The `entry_points` defined in this script are used to run the package in the Databricks workflow. In each value in `entry_points`, the value before `=` (in this example, `run`) is the name of the entry point and is used to configure the Python wheel task.

1.  Save this script in a file named `setup.py` in the root of the directory you created in step 1:
    
    Python
    
        from setuptools import setup, find_packagesimport my_test_codesetup(  name='my_test_package',  version=my_test_code.__version__,  author=my_test_code.__author__,  url='https://databricks.com',  author_email='john.doe@databricks.com',  description='my test wheel',  packages=find_packages(include=['my_test_code']),  entry_points={    'group_1': 'run=my_test_code.__main__:main'  },  install_requires=[    'setuptools'  ])
    
2.  Change into the directory you created in step 1, and run the following command to package your code into the Python wheel distribution:
    
    Bash
    
        python3 setup.py bdist_wheel
    

This command creates the Python wheel file and saves it to the `dist/my_test_package-0.0.1-py3.none-any.whl` file in your directory.

## Step 5. Create a job to run the Python wheel file[​](#step-5-create-a-job-to-run-the-python-wheel-file "Direct link to step-5-create-a-job-to-run-the-python-wheel-file")

1.  In your workspace, click ![Workflows icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zLjc1IDRDNC40NDAzNiA0IDUgMy40NDAzNiA1IDIuNzVDNSAyLjA1OTY0IDQuNDQwMzYgMS41IDMuNzUgMS41QzMuMDU5NjQgMS41IDIuNSAyLjA1OTY0IDIuNSAyLjc1QzIuNSAzLjQ0MDM2IDMuMDU5NjQgNCAzLjc1IDRaTTYuMzk2NDggMy41QzYuMDcwMDIgNC42NTQyNSA1LjAwODc4IDUuNSAzLjc1IDUuNUMyLjIzMTIyIDUuNSAxIDQuMjY4NzggMSAyLjc1QzEgMS4yMzEyMiAyLjIzMTIyIDAgMy43NSAwQzUuMDA4NzggMCA2LjA3MDAyIDAuODQ1NzQ4IDYuMzk2NDggMkgxMS42MjVDMTMuNDg5IDIgMTUgMy41MTEwNCAxNSA1LjM3NUMxNSA3LjE5OTQgMTMuNTUyNCA4LjY4NTY5IDExLjc0MzIgOC43NDc5N0w4LjQzNTk0IDExLjExMDNDOC4xNzUxNiAxMS4yOTY2IDcuODI0ODUgMTEuMjk2NiA3LjU2NDA4IDExLjExMDNMNC4yNjQxNiA4Ljc1MzIyQzMuMjgwMjIgOC44MTA1OCAyLjUgOS42MjY2OCAyLjUgMTAuNjI1QzIuNSAxMS42NjA1IDMuMzM5NDcgMTIuNSA0LjM3NSAxMi41SDkuNjAzNTJDOS45Mjk5OCAxMS4zNDU3IDEwLjk5MTIgMTAuNSAxMi4yNSAxMC41QzEzLjc2ODggMTAuNSAxNSAxMS43MzEyIDE1IDEzLjI1QzE1IDE0Ljc2ODggMTMuNzY4OCAxNiAxMi4yNSAxNkMxMC45OTEyIDE2IDkuOTI5OTggMTUuMTU0MyA5LjYwMzUyIDE0SDQuMzc1QzIuNTExMDQgMTQgMSAxMi40ODkgMSAxMC42MjVDMSA4LjgwMDYgMi40NDc1OCA3LjMxNDMgNC4yNTY4MSA3LjI1MjAzTDcuNTY0MDggNC44ODk2OUM3LjgyNDg1IDQuNzAzNDMgOC4xNzUxNiA0LjcwMzQzIDguNDM1OTQgNC44ODk2OUwxMS43MzU5IDcuMjQ2NzhDMTIuNzE5OCA3LjE4OTQxIDEzLjUgNi4zNzMzMiAxMy41IDUuMzc1QzEzLjUgNC4zMzk0NyAxMi42NjA1IDMuNSAxMS42MjUgMy41SDYuMzk2NDhaTTEzLjUgMTMuMjVDMTMuNSAxMy45NDA0IDEyLjk0MDQgMTQuNSAxMi4yNSAxNC41QzExLjU1OTYgMTQuNSAxMSAxMy45NDA0IDExIDEzLjI1QzExIDEyLjU1OTYgMTEuNTU5NiAxMiAxMi4yNSAxMkMxMi45NDA0IDEyIDEzLjUgMTIuNTU5NiAxMy41IDEzLjI1Wk04LjAwMDAxIDYuNDIxNjdMNS43OTAzNSA4TDguMDAwMDEgOS41NzgzM0wxMC4yMDk3IDhMOC4wMDAwMSA2LjQyMTY3WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) **Jobs & Pipelines** in the sidebar.
    
2.  Click **Create**, then **Job**.
    
3.  Click the **Python wheel** tile to configure the first task. If the **Python wheel** tile is not available, click **Add another task type** and search for **Python wheel**.
    
4.  Optionally, replace the name of the job, which defaults to **`New Job <date-time>`**, with your job name.
    
5.  In **Task name**, enter a name for the task.
    
6.  If necessary, select **Python wheel** from the **Type** drop-down menu.
    
7.  In **Package name**, enter `my_test_package`. The **Package Name** value is the name of the Python package to import. In this example, the package name is the value assigned to the `name` parameter in `setup.py`.
    
8.  In **Entry point**, enter `run`. The entry point is one of the values specified in the `entry_points` collection in the `setup.py` script. In this example, `run` is the only entry point defined.
    
9.  In **Compute**, select an existing job cluster or **Add new job cluster**.
    
10.  Specify your Python wheel file:
     
11.  In **Parameters**, select **Positional arguments** or **Keyword arguments** to enter the key and the value of each parameter. Both positional and keyword arguments are passed to the Python wheel task as command-line arguments.
     
     *   To enter positional arguments, enter parameters as a JSON-formatted array of strings, for example: `["first argument","first value","second argument","second value"]`.
     *   To enter keyword arguments, click **\+ Add** and enter a key and value. Click **\+ Add** again to enter more arguments.
12.  Click **Create task**.
     

## Step 6: Run the job and view the job run details[​](#step-6-run-the-job-and-view-the-job-run-details "Direct link to step-6-run-the-job-and-view-the-job-run-details")

Click ![Run Now Button](data:image/png;base64,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) to run the workflow. To view [details for the run](https://docs.databricks.com/aws/en/jobs/monitor#job-run-details), click the **Runs** tab, then click the link in the **Start time** column for the run in the [job runs](https://docs.databricks.com/aws/en/jobs/monitor#view-job-run-list) view.

When the run completes, the output displays in the **Output** pane, including the arguments passed to the task.

## Next steps[​](#next-steps "Direct link to next-steps")

To learn more about creating and running jobs, see [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/).
