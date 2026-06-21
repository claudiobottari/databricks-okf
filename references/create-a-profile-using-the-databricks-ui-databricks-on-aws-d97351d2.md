---
title: Create a profile using the Databricks UI | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui
ingestedAt: "2026-06-18T08:04:16.036Z"
---

This article demonstrates create a data profile using the Databricks UI. You can also use [the API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api).

To access the Databricks UI, do the following:

1.  In the workspace left sidebar, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) to open [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/).
    
2.  Navigate to the table you want to profile.
    
3.  Click the **Quality** tab.
    
4.  If [anomaly detection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/) is not enabled for this schema, click **Enable**.
    
    ![Data profiling quality tab, not enabled yet.](https://docs.databricks.com/aws/en/assets/images/quality-tab-new-f83e8fd3369e702ce587d436836f20dc.png)
    
    If anomaly detection is enabled for this schema, click **Configure**.
    
    ![Data profiling quality tab, already enabled.](https://docs.databricks.com/aws/en/assets/images/quality-tab-4382749bd593f7235259c97328c605d4.png)
    
5.  In the **Data Quality Monitoring** dialog, in the **Data profiling** field, click **Configure**.
    
    ![Data quality monitor dialog.](https://docs.databricks.com/aws/en/assets/images/quality-dialog-b7c5d37a6fe88be6e2e2fb492db272b9.png)
    
6.  In the dialog, select the **Profile type**. The following sections describe the profile type options and the additional selections for each type.
    

## Profiling[​](#profiling "Direct link to Profiling")

From the **Profile type** drop-down menu, select the type of profile you want to create. The profile types are shown in the table.

If you select `TimeSeries` or `Inference`, additional parameters are required and are described in the following sections.

note

*   When you first create a time series or inference profile, the profile analyzes only data from the 30 days prior to its creation. After the profile is created, all new data is processed.
*   Monitors defined on materialized views do not support incremental processing.

tip

For `TimeSeries` and `Inference` profiles, it's a best practice to enable change data feed (CDF) on your table. When CDF is enabled, only newly appended data is processed, rather than re-processing the entire table every refresh. This makes execution more efficient and reduces costs as you scale profiling across many tables.

### `TimeSeries` profile[​](#timeseries-profile "Direct link to timeseries-profile")

For a `TimeSeries` profile, you must make the following selections:

*   Specify the **Metric granularities** that determine how to partition the data in windows across time.
*   Specify the **Timestamp column**, the column in the table that contains the timestamp. The timestamp column data type must be either `TIMESTAMP` or a type that can be converted to timestamps using the `to_timestamp` [PySpark function](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_timestamp.html).

### `Inference` profile[​](#inference-profile "Direct link to inference-profile")

For a `Inference` profile, in addition to the granularities and the timestamp, you must make the following selections:

*   Select the **Problem type**, either classification or regression.
*   Specify the **Prediction column**, the column containing the model's predicted values.
*   Optionally specify the **Label column**, the column containing the ground truth for model predictions.
*   Specify the **Model ID column**, the column containing the id of the model used for prediction.

## Advanced options[​](#advanced-options "Direct link to advanced-options")

In the **Advanced options** section, you can set the schedule, add email notifications, add custom metrics and slicing expressions, and change the default profile configuration.

### Schedule[​](#schedule "Direct link to schedule")

To set up a profile to run on a scheduled basis, select **Refresh on schedule** and select the frequency and time for the profile to run. If you do not want the profile to run automatically, select **Refresh manually**. If you select **Refresh manually**, you can later refresh the metrics from the **Quality** tab.

### Notifications[​](#notifications "Direct link to notifications")

To set up email notifications for a profile, enter the email to be notified and select the notifications to enable. Up to 5 emails are supported per notification event type.

### Metrics[​](#metrics "Direct link to metrics")

In the **Metrics** section, you can choose to change the following default settings:

*   **Metrics tables schema name**: The Unity Catalog schema where the metric tables created by the profile are stored. This location must be in the format {catalog}.{schema}. By default, this is set to the same schema location as the profiled table. You can specify a different location.
    
*   **Assets directory**: The absolute path to an existing directory to store data profiling assets. By default, assets are stored in the default directory: "/Users/{user\_name}/databricks\_lakehouse\_monitoring/{table\_name}". If you enter a different location in this field, assets are created under "/{table\_name}" in the directory you specify. This directory can be anywhere in the workspace. For profiles intended to be shared within an organization, you can use a path in the "/Shared/" directory.
    
    This field cannot be left blank.
    

You can also specify the following settings:

*   **Unity Catalog baseline table name**: Name of a table or view that contains baseline data for comparison.
*   **Metric slicing expressions**: Slicing expressions let you define subsets of the table to profile in addition to the table as a whole. To create a slicing expression, click **Add expression** and enter the expression definition. For example the expression `"col_2 > 10"` generates two slices: one for `col_2 > 10` and one for `col_2 <= 10`. As another example, the expression `"col_1"` will generate one slice for each unique value in `col_1`. The data is grouped by each expression independently, resulting in a separate slice for each predicate and its complements.
*   **Custom metrics**: Custom metrics appear in the metric tables like any built-in metric. To configure a custom metric, click **Add custom metric**.
    *   Enter a **Name** for the custom metric.
    *   Select the custom metric **Type**. Choose from: `Aggregate`, `Derived`, or `Drift`.
    *   From the drop-down list in **Input columns**, select the columns to apply the metric to.
    *   In the **Output type** field, select the Spark data type of the metric.
    *   In the **Definition** field, enter SQL code that defines the custom metric.

## Edit profile settings in the UI[​](#edit-profile-settings-in-the-ui "Direct link to edit-profile-settings-in-the-ui")

After you have created a profile, you can make changes to the profile's settings by clicking **Configure** on the **Quality** tab.

![Configure an existing profile.](https://docs.databricks.com/aws/en/assets/images/configure-profile-55d777802c98d0228961ff6dca563d7f.png)

In the **Data profiling** section of the dialog, click **Configure**.

![Update profile dialog.](https://docs.databricks.com/aws/en/assets/images/update-profile-5c275ce9b61bd94a9d2681d67716d61c.png)

## Refresh and view profile results in the UI[​](#refresh-and-view-profile-results-in-the-ui "Direct link to refresh-and-view-profile-results-in-the-ui")

To run the profile manually, click **View refresh history**. A dialog opens showing all previous profiles. Click **Refresh metrics** to trigger a profile update.

To see the refresh history, you must use the Databricks workspace from which data profiling was enabled.

For information about the statistics that are stored in profile metric tables, see [Monitor metric tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output). Metric tables are Unity Catalog tables. You can query them in notebooks or in the SQL query explorer, and view them in Catalog Explorer.

## Control access to profile outputs[​](#control-access-to-profile-outputs "Direct link to Control access to profile outputs")

The metric tables and dashboard created by a profile are owned by the user who created the profile. You can use Unity Catalog privileges to control access to metric tables. To share dashboards within a workspace, click the **Share** button on the upper-right side of the dashboard.

## Delete a profile from the UI[​](#delete-a-profile-from-the-ui "Direct link to Delete a profile from the UI")

To delete a profile from the UI, follow the instructions in [Edit profile settings in the UI](#edit-profile) to open the **Update profile** dialog. From the **Update** dropdown menu, select **Delete**.

![Delete a profile.](https://docs.databricks.com/aws/en/assets/images/delete-profile-a557f4209bbc7a1e8d73c286e8b0c5d2.png)
