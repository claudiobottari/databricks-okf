---
title: Orchestrate Databricks notebooks and modularize code | Databricks on AWS
source: https://docs.databricks.com/aws/en/notebooks/notebook-workflows
ingestedAt: "2026-06-18T08:18:29.647Z"
---

You can orchestrate Databricks notebooks and modularize code using Lakeflow Jobs, `dbutils.notebook.run()`, workspace files, and `%run`. Choose a method based on your need for scheduling, parameter passing, and version control.

## Orchestration and code modularization methods[​](#orchestration-and-code-modularization-methods "Direct link to Orchestration and code modularization methods")

The following table compares the methods available for orchestrating notebooks and modularizing code in notebooks.

### `%run` vs. `dbutils.notebook.run()`[​](#run-vs-dbutilsnotebookrun "Direct link to run-vs-dbutilsnotebookrun")

The `%run` command allows you to include another notebook within a notebook. You can use `%run` to modularize your code by putting supporting functions in a separate notebook. You can also use it to concatenate notebooks that implement the steps in an analysis. When you use `%run`, the called notebook is immediately executed and the functions and variables defined in it become available in the calling notebook.

The `dbutils.notebook` API complements `%run` because it lets you pass parameters to and return values from a notebook. This allows you to build complex workflows and pipelines with dependencies. For example, you can get a list of files in a directory and pass the names to another notebook, which is impossible with `%run`. You can also create if-then-else workflows based on return values.

Unlike `%run`, the `dbutils.notebook.run()` method starts a new job to run the notebook.

Like all of the `dbutils` APIs, these methods are available only in Python and Scala. However, you can use `dbutils.notebook.run()` to invoke an R notebook.

## Use `%run` to import a notebook[​](#use-run-to-import-a-notebook "Direct link to use-run-to-import-a-notebook")

In this example, the first notebook defines a function, `reverse`, which is available in the second notebook after you use the `%run` magic to execute `shared-code-notebook`.

![Shared code notebook](https://docs.databricks.com/aws/en/assets/images/shared-code-notebook-4f13a29c4f1bcf255feb2c1ed75fe63e.png)

![Notebook import example](https://docs.databricks.com/aws/en/assets/images/notebook-import-example-a7f806bb68d4c956d8d5fc64ffd9bffe.png)

Because both notebooks are in the same directory in the workspace, use the prefix `./` in `./shared-code-notebook` to indicate that the path should be resolved relative to the currently running notebook. You can organize notebooks into directories, such as `%run ./dir/notebook`, or use an absolute path like `%run /Users/username@organization.com/directory/notebook`.

note

*   `%run` must be in a cell _by itself_, because it runs the entire notebook inline.
*   You _cannot_ use `%run` to run a Python file and `import` the entities defined in that file into a notebook. To import from a Python file, see [Modularize your code using files](https://docs.databricks.com/aws/en/notebooks/share-code#reference-source-code-files-using-git). Or, package the file into a Python library, create a Databricks [library](https://docs.databricks.com/aws/en/libraries/) from that Python library, and [install the library into the cluster](https://docs.databricks.com/aws/en/libraries/cluster-libraries#install-libraries) you use to run your notebook.
*   When you use `%run` to run a notebook that contains widgets, by default the specified notebook runs with the widget's default values. You can also pass values to widgets; see [Use Databricks widgets with %run](https://docs.databricks.com/aws/en/notebooks/widgets#widgets-and-percent-run).

## Use `dbutils.notebook.run` to start a new job[​](#use-dbutilsnotebookrun-to-start-a-new-job "Direct link to use-dbutilsnotebookrun-to-start-a-new-job")

Run a notebook and return its exit value. The method starts an ephemeral job that runs immediately.

The methods available in the `dbutils.notebook` API are `run` and `exit`. Both parameters and return values must be strings.

**`run(path: String, timeout_seconds: int, arguments: Map): String`**

The `timeout_seconds` parameter controls the timeout of the run (0 means no timeout). The call to `run` throws an exception if it doesn't finish within the specified time. If Databricks is down for more than 10 minutes, the notebook run fails regardless of `timeout_seconds`.

The `arguments` parameter sets widget values of the target notebook. Specifically, if the notebook you are running has a widget named `A`, and you pass a key-value pair `("A": "B")` as part of the arguments parameter to the `run()` call, then retrieving the value of widget `A` will return `"B"`. You can find the instructions for creating and working with widgets in the [Databricks widgets](https://docs.databricks.com/aws/en/notebooks/widgets) page.

note

*   The `arguments` parameter accepts only Latin characters (ASCII character set). Using non-ASCII characters returns an error.
*   Jobs created using the `dbutils.notebook` API must complete in 30 days or less.

### `run` usage[​](#run-usage "Direct link to run-usage")

*   Python
*   Scala

Python

    dbutils.notebook.run("notebook-name", 60, {"argument": "data", "argument2": "data2", ...})

## Pass structured data between notebooks[​](#pass-structured-data-between-notebooks "Direct link to Pass structured data between notebooks")

This section illustrates how to pass structured data between notebooks.

*   Python
*   Scala

Python

    # Example 1 - returning data through temporary views.# You can only return one string using dbutils.notebook.exit(), but since called notebooks reside in the same JVM, you can# return a name referencing data stored in a temporary view.## In callee notebookspark.range(5).toDF("value").createOrReplaceGlobalTempView("my_data")dbutils.notebook.exit("my_data")## In caller notebookreturned_table = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)global_temp_db = spark.conf.get("spark.sql.globalTempDatabase")display(table(global_temp_db + "." + returned_table))# Example 2 - returning data through DBFS.# For larger datasets, you can write the results to DBFS and then return the DBFS path of the stored data.## In callee notebookdbutils.fs.rm("/tmp/results/my_data", recurse=True)spark.range(5).toDF("value").write.format("parquet").save("dbfs:/tmp/results/my_data")dbutils.notebook.exit("dbfs:/tmp/results/my_data")## In caller notebookreturned_table = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)display(spark.read.format("parquet").load(returned_table))# Example 3 - returning JSON data.# To return multiple values, you can use standard JSON libraries to serialize and deserialize results.## In callee notebookimport jsondbutils.notebook.exit(json.dumps({  "status": "OK",  "table": "my_data"}))## In caller notebookimport jsonresult = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)print(json.loads(result))

## Handle errors[​](#handle-errors "Direct link to Handle errors")

This section illustrates how to handle errors.

*   Python
*   Scala

Python

    # Errors throw a WorkflowException.def run_with_retry(notebook, timeout, args = {}, max_retries = 3):  num_retries = 0  while True:    try:      return dbutils.notebook.run(notebook, timeout, args)    except Exception as e:      if num_retries > max_retries:        raise e      else:        print("Retrying error", e)        num_retries += 1run_with_retry("LOCATION_OF_CALLEE_NOTEBOOK", 60, max_retries = 5)

## Run multiple notebooks concurrently[​](#run-multiple-notebooks-concurrently "Direct link to Run multiple notebooks concurrently")

You can run multiple notebooks at the same time by using standard Scala and Python constructs such as Threads ([Scala](https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html), [Python](https://docs.python.org/3/library/threading.html)) and Futures ([Scala](https://docs.scala-lang.org/overviews/core/futures.html), [Python](https://docs.python.org/3/library/multiprocessing.html)). The example notebooks demonstrate how to use these constructs.

1.  Download the following four notebooks. The notebooks are written in Scala.
2.  Import the notebooks into a single folder in the workspace.
3.  Run the **Run concurrently** notebook.

#### Run concurrently notebook

#### Run in parallel notebook

#### Testing notebook

#### Testing-2 notebook
