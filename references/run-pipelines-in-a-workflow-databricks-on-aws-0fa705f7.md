---
title: Run pipelines in a workflow | Databricks on AWS
source: https://docs.databricks.com/aws/en/ldp/workflows
ingestedAt: "2026-06-18T08:07:58.569Z"
---

You can run a pipeline as part of a data processing workflow with Lakeflow Jobs, Apache Airflow, or Azure Data Factory.

## Jobs[​](#jobs "Direct link to Jobs")

You can orchestrate multiple tasks in a Databricks job to implement a data processing workflow. To include a pipeline in a job, use the **Pipeline** task when you create a job. See [Pipeline task for jobs](https://docs.databricks.com/aws/en/jobs/pipeline).

## Apache Airflow[​](#apache-airflow "Direct link to Apache Airflow")

[Apache Airflow](https://airflow.apache.org/) is an open source solution for managing and scheduling data workflows. Airflow represents workflows as directed acyclic graphs (DAGs) of operations. You define a workflow in a Python file and Airflow manages the scheduling and execution. For information on installing and using Airflow with Databricks, see [Orchestrate Lakeflow Jobs with Apache Airflow](https://docs.databricks.com/aws/en/jobs/how-to/use-airflow-with-jobs).

To run a pipeline as part of an Airflow workflow, use the [DatabricksSubmitRunOperator](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/_api/airflow/providers/databricks/operators/databricks/index.html#airflow.providers.databricks.operators.databricks.DatabricksSubmitRunOperator).

### Requirements[​](#requirements "Direct link to Requirements")

The following are required to use the Airflow support for Lakeflow Spark Declarative Pipelines:

*   Airflow version 2.1.0 or later.
*   The [Databricks provider](https://pypi.org/project/apache-airflow-providers-databricks/) package version 2.1.0 or later.

### Example[​](#example "Direct link to Example")

The following example creates an Airflow DAG that triggers an update for the pipeline with the identifier `8279d543-063c-4d63-9926-dae38e35ce8b`:

Python

    from airflow import DAGfrom airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperatorfrom airflow.utils.dates import days_agodefault_args = {  'owner': 'airflow'}with DAG('ldp',         start_date=days_ago(2),         schedule_interval="@once",         default_args=default_args         ) as dag:  opr_run_now=DatabricksSubmitRunOperator(    task_id='run_now',    databricks_conn_id='CONNECTION_ID',    pipeline_task={"pipeline_id": "8279d543-063c-4d63-9926-dae38e35ce8b"}  )

Replace `CONNECTION_ID` with the identifier for an [Airflow connection](https://docs.databricks.com/aws/en/jobs/how-to/use-airflow-with-jobs) to your workspace.

Save this example in the `airflow/dags` directory and use the Airflow UI to [view and trigger](https://docs.databricks.com/aws/en/jobs/how-to/use-airflow-with-jobs) the DAG. Use the pipeline UI to view the details of the pipeline update.

## Azure Data Factory[​](#azure-data-factory "Direct link to Azure Data Factory")

note

Lakeflow Spark Declarative Pipelines and Azure Data Factory each include options to configure the number of retries when a failure occurs. If retry values are configured on your pipeline **and** on the Azure Data Factory activity that calls the pipeline, the number of retries is the Azure Data Factory retry value multiplied by the pipeline retry value.

For example, if a pipeline update fails, Lakeflow Spark Declarative Pipelines retries the update up to five times by default. If the Azure Data Factory retry is set to three, and your pipeline uses the default of five retries, your failing pipeline might be retried up to fifteen times. To avoid excessive retry attempts when pipeline updates fail, Databricks recommends limiting the number of retries when configuring the pipeline or the Azure Data Factory activity that calls the pipeline.

To change the retry configuration for your pipeline, use the `pipelines.numUpdateRetryAttempts` setting when configuring the pipeline.

Azure Data Factory is a cloud-based ETL service that lets you orchestrate data integration and transformation workflows. Azure Data Factory directly supports running Databricks tasks in a workflow, including [notebooks](https://learn.microsoft.com/azure/data-factory/transform-data-using-databricks-notebook), JAR tasks, and Python scripts. You can also include a pipeline in a workflow by calling the pipeline REST [API](https://docs.databricks.com/api/workspace/pipelines) from an Azure Data Factory [Web activity](https://learn.microsoft.com/azure/data-factory/control-flow-web-activity). For example, to trigger a pipeline update from Azure Data Factory:

1.  [Create a data factory](https://learn.microsoft.com/azure/data-factory/quickstart-create-data-factory-portal#create-a-data-factory) or open an existing data factory.
    
2.  When creation completes, open the page for your data factory and click the **Open Azure Data Factory Studio** tile. The Azure Data Factory user interface appears.
    
3.  Create a new Azure Data Factory pipeline by selecting **Pipeline** from the **New** drop-down menu in the Azure Data Factory Studio user interface.
    
4.  In the **Activities** toolbox, expand **General** and drag the **Web** activity to the pipeline canvas. Click the **Settings** tab and enter the following values:
    
    note
    
    As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use [OAuth tokens](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m).
    
    If you use personal access token authentication, Databricks recommends using personal access tokens belonging to [service principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals#tokens).
    
    *   **URL**: `https://<databricks-instance>/api/2.0/pipelines/<pipeline-id>/updates`.
        
        Replace `<get-workspace-instance>`.
        
        Replace `<pipeline-id>` with the pipeline identifier.
        
    *   **Method**: Select **POST** from the drop-down menu.
        
    *   **Headers**: Click **\+ New**. In the **Name** text box, enter `Authorization`. In the **Value** text box, enter `Bearer <personal-access-token>`.
        
        Replace `<personal-access-token>` with a Databricks [personal access token](https://docs.databricks.com/api/workspace/tokenmanagement).
        
    *   **Body**: To pass additional request parameters, enter a JSON document containing the parameters. For example, to start an update and reprocess all data for the pipeline: `{"full_refresh": "true"}`. If there are no additional request parameters, enter empty braces (`{}`).
        

To test the Web activity, click **Debug** on the pipeline toolbar in the Data Factory UI. The output and status of the run, including errors, are displayed in the **Output** tab of the Azure Data Factory pipeline. Use the pipelines UI to view the details of the pipeline update.

tip

A common workflow requirement is to start a task after completion of a previous task. Because the pipeline `updates` request is asynchronous, returning after starting the update but before it completes, tasks in your Azure Data Factory pipeline with a dependency on the pipeline update must wait for the update to complete. An option to wait for update completion is adding an [Until activity](https://learn.microsoft.com/azure/data-factory/control-flow-until-activity) following the Web activity that triggers the Lakeflow Spark Declarative Pipelines update. In the Until activity:

1.  Add a [Wait activity](https://learn.microsoft.com/azure/data-factory/control-flow-wait-activity) to wait a configured number of seconds for update completion.
2.  Add a Web activity following the Wait activity that uses the pipeline update details request to get the status of the update. The `state` field in the response returns the current state of the update, including if it has completed.
3.  Use the value of the `state` field to set the terminating condition for the Until activity. You can also use a [Set Variable activity](https://learn.microsoft.com/azure/data-factory/control-flow-set-variable-activity) to add a pipeline variable based on the `state` value and use this variable for the terminating condition.
