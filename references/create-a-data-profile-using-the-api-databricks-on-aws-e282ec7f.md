---
title: Create a data profile using the API | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api
ingestedAt: "2026-06-18T08:04:14.612Z"
---

This page describes how to create a data profile in Databricks using the Databricks SDK and describes the parameters used in API calls. You can also create and manage a data profile using the REST API.

For reference information, see the [data profiling SDK reference](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dataquality/data_quality.html) and the [REST API reference](https://docs.databricks.com/api/workspace/dataquality).

You can create a profile on any managed or external Delta table registered in Unity Catalog. Only a single profile can be created in a Unity Catalog metastore for any table.

## Requirements[​](#requirements "Direct link to Requirements")

To use the most recent version of the API, use the following command at the beginning of your notebook to install the Python client:

Python

    %pip install "databricks-sdk>=0.68.0"

To authenticate to use the Databricks SDK in your environment, see [Authentication](https://databricks-sdk-py.readthedocs.io/en/latest/authentication.html).

## Profile types[​](#profile-types "Direct link to profile-types")

When you create a profile, you select one of the following profile types: `TimeSeries`, `InferenceLog`, or `Snapshot`. This section briefly describes each option. For details, see the [data profiling SDK reference](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/dataquality/data_quality.html) or the [REST API reference](https://docs.databricks.com/api/workspace/dataquality).

note

*   When you first create a time series or inference profile, Databricks analyzes only data from the 30 days prior to its creation. After the profile is created, all new data is processed.
*   Profiles defined on materialized views do not support incremental processing.

tip

For `TimeSeries` and `Inference` profiles, it's a best practice to enable change data feed (CDF) on your table. When CDF is enabled, only newly appended data is processed, rather than re-processing the entire table every refresh. This makes execution more efficient and reduces costs as you scale across many tables.

### `TimeSeries` profile[​](#timeseries-profile "Direct link to timeseries-profile")

A `TimeSeries` profile compares data distributions across time windows. For a `TimeSeries` profile, you must provide the following:

*   A timestamp column (`timestamp_column`). The timestamp column data type must be either `TIMESTAMP` or a type that can be converted to timestamps using the `to_timestamp` [PySpark function](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_timestamp.html).
*   The set of `granularities` over which to calculate metrics. The following granularities are available:
    *   AGGREGATION\_GRANULARITY\_5\_MINUTES
    *   AGGREGATION\_GRANULARITY\_30\_MINUTES
    *   AGGREGATION\_GRANULARITY\_1\_HOUR
    *   AGGREGATION\_GRANULARITY\_1\_DAY
    *   AGGREGATION\_GRANULARITY\_1\_WEEK
    *   AGGREGATION\_GRANULARITY\_2\_WEEKS
    *   AGGREGATION\_GRANULARITY\_3\_WEEKS
    *   AGGREGATION\_GRANULARITY\_4\_WEEKS
    *   AGGREGATION\_GRANULARITY\_1\_MONTH
    *   AGGREGATION\_GRANULARITY\_1\_YEAR

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, TimeSeriesConfig, AggregationGranularity, DataProfilingStatus, RefreshState, Refreshw = WorkspaceClient()schema = w.schemas.get(full_name=f"{catalog}.{schema}")table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")config = DataProfilingConfig( output_schema_id=schema.schema_id, assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}", time_series=TimeSeriesConfig(    timestamp_column="ts",    granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]), slicing_exprs=["type='Red'"])info = w.data_quality.create_monitor(   monitor=Monitor(     object_type="table",     # object_type is always "table" for data profiling     object_id=table.table_id,     data_profiling_config=config,   ),)

### `InferenceLog` profile[​](#inferencelog-profile "Direct link to inferencelog-profile")

An `InferenceLog` profile is similar to a `TimeSeries` profile but also includes model quality metrics. `InferenceLog` profiles use the following parameters:

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, InferenceLogConfig, InferenceProblemType, AggregationGranularity, DataProfilingStatus, RefreshState, Refreshw = WorkspaceClient()schema = w.schemas.get(full_name=f"{catalog}.{schema}")table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")config = DataProfilingConfig( output_schema_id=schema.schema_id, assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}", inference_log=InferenceLogConfig(    problem_type=InferenceProblemType.INFERENCE_PROBLEM_TYPE_CLASSIFICATION,    prediction_column="preds",    model_id_column="model_ver",    label_column="label", # optional    timestamp_column="ts",    granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]))info = w.data_quality.create_monitor(   monitor=Monitor(     object_type="table",     object_id=table.table_id,     data_profiling_config=config,   ),)

For `InferenceLog` profiles, slices are automatically created based on the distinct values of `model_id_col`.

### `Snapshot` profile[​](#snapshot-profile "Direct link to snapshot-profile")

In contrast to `TimeSeries`, a `Snapshot` profiles how the full contents of the table change over time. Metrics are calculated over all data in the table, and reflect the table state at each time the profile is refreshed.

note

The maximum table size for a snapshot profile is 4TB. For larger tables, use time series profiles instead.

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, SnapshotConfig, DataProfilingStatus, RefreshState, Refreshw = WorkspaceClient()schema = w.schemas.get(full_name=f"{catalog}.{schema}")table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")table_id = table.table_idtable_object_type = "table"config = DataProfilingConfig( output_schema_id=schema.schema_id, assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}", snapshot=SnapshotConfig(), slicing_exprs=["type='Red'"])

## Refresh and view results[​](#refresh-and-view-results "Direct link to refresh-and-view-results")

To see the refresh history, you must use the Databricks workspace from which data profiling was enabled.

To refresh metrics tables, use `create_refresh`. For example:

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()run_info = w.data_quality.create_refresh(  object_type=table_object_type, object_id=table_id, refresh=Refresh(   object_type=table_object_type,   object_id=table_id, ))

When you call `create_refresh` from a notebook, the metric tables are created or updated. This calculation runs on serverless compute, not on the cluster that the notebook is attached to. You can continue to run commands in the notebook while the statistics are updated.

For information about the statistics that are stored in metric tables, see [Monitor metric tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output) Metric tables are Unity Catalog tables. You can query them in notebooks or in the SQL query explorer, and view them in Catalog Explorer.

To display the history of all refreshes associated with a profile, use `list_refreshes`.

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()it = w.data_quality.list_refresh(object_type=table_object_type, object_id=table_id)

To get the status of a specific run that has been queued, running, or finished, use `get_refresh`.

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()it = w.data_quality.list_refresh(object_type=table_object_type, object_id=table_id)run_info = next(it, None)while run_info.state in (RefreshState.MONITOR_REFRESH_STATE_PENDING, RefreshState.MONITOR_REFRESH_STATE_RUNNING):  run_info = w.data_quality.get_refresh(object_type=table_object_type, object_id=table_id, refresh_id=run_info.refresh_id)  time.sleep(30)

## View profile settings[​](#view-profile-settings "Direct link to View profile settings")

You can review profile settings using the API `get_monitor`.

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")w.data_quality.get_monitor(object_type="table", object_id=table.table_id)

## Schedule[​](#schedule "Direct link to schedule")

To set up a profile to run on a scheduled basis, use the `schedule` parameter of `create_monitor`:

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.catalog import MonitorTimeSeries, MonitorCronSchedulew = WorkspaceClient()schema = w.schemas.get(full_name=f"{catalog}.{schema}")table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")config = DataProfilingConfig( output_schema_id=schema.schema_id, snapshot=SnapshotConfig(), schedule=CronSchedule(        quartz_cron_expression="0 0 12 * * ?", # schedules a refresh every day at 12 noon        timezone_id="PST", ))info = w.data_quality.create_monitor(   monitor=Monitor(     object_type="table",     object_id=table.table_id,     data_profiling_config=config,   ),)

See [cron expressions](https://en.wikipedia.org/wiki/Cron) for more information.

## Notifications[​](#notifications "Direct link to notifications")

To set up notifications for a profile, use the `notifications` parameter of `create_monitor`:

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, SnapshotConfig, NotificationSettings, NotificationDestinationw = WorkspaceClient()schema = w.schemas.get(full_name=f"{catalog}.{schema}")table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")config = DataProfilingConfig( output_schema_id=schema.schema_id, snapshot=SnapshotConfig(), notification_settings=NotificationSettings(        # Notify the given email when a monitoring refresh fails or times out.        on_failure=NotificationDestination(            email_addresses=["your_email@domain.com"]        ) ))info = w.data_quality.create_monitor(   monitor=Monitor(     object_type="table",     object_id=table.table_id,     data_profiling_config=config,   ),)

A maximum of 5 email addresses is supported per event type (for example, “on\_failure”).

## Control access to metric tables[​](#control-access-to-metric-tables "Direct link to Control access to metric tables")

The metric tables and dashboard created by a profile are owned by the user who created the profile. You can use Unity Catalog privileges to control access to metric tables. To share dashboards within a workspace, use the **Share** button at the upper-right of the dashboard.

## Delete a profile[​](#delete-a-profile "Direct link to Delete a profile")

To delete a profile:

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")w.data_quality.delete_monitor(object_type="table", object_id=table.table_id)

This command does not delete the profile tables and the dashboard created by the profile. You must delete those assets in a separate step, or you can save them in a different location.

## Example notebooks[​](#example-notebooks "Direct link to example-notebooks")

The following example notebooks illustrate how to create a profile, refresh the profile, and examine the metric tables it creates.

## Notebook example: Time series profile[​](#notebook-example-time-series-profile "Direct link to Notebook example: Time series profile")

This notebook illustrates how to create a `TimeSeries` type profile.

#### TimeSeries profile example notebook

## Notebook example: Inference profile (regression)[​](#notebook-example-inference-profile-regression "Direct link to Notebook example: Inference profile (regression)")

This notebook illustrates how to create a `InferenceLog` type profile for a regression problem.

#### Inference profile regression example notebook

## Notebook example: Inference profile (classification)[​](#notebook-example-inference-profile-classification "Direct link to Notebook example: Inference profile (classification)")

This notebook illustrates how to create a `InferenceLog` type profile for a classification problem.

#### Inference profile classification example notebook

## Notebook example: Snapshot profile[​](#notebook-example-snapshot-profile "Direct link to Notebook example: Snapshot profile")

This notebook illustrates how to create a `Snapshot` type profile.

#### Snapshot profile example notebook
