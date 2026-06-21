---
title: Databricks online tables (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/feature-store/online-tables
ingestedAt: "2026-06-18T08:02:49.692Z"
---

Preview

Online tables are in Public Preview in the following regions: `us-east-1`, `us-west-2`, `eu-west-1`, `ap-southeast-1`, `ap-southeast-2`. For pricing information, see [Online Tables pricing](https://www.databricks.com/product/pricing/online-tables).

An online table is a read-only copy of a Delta Table that is stored in row-oriented format optimized for online access. Online tables are fully serverless tables that auto-scale throughput capacity with the request load and provide low latency and high throughput access to data of any scale. Online tables are designed to work with Model Serving, Feature Serving, and retrieval-augmented generation (RAG) applications where they are used for fast data lookups.

You can also use online tables in queries using [Lakehouse Federation](https://docs.databricks.com/aws/en/query-federation/). When using Lakehouse Federation, you must use a Serverless SQL warehouse to access online tables. Only read operations (`SELECT`) are supported. This capability is intended for interactive or debugging purposes only and should not be used for production or mission critical workloads.

Creating an online table using the Databricks UI is a one-step process. Just select the Delta table in Catalog Explorer and select **Create online table**. You can also use the REST API or the Databricks SDK to create and manage online tables. See [Work with online tables using APIs](#api-sdk).

## Requirements[​](#requirements "Direct link to Requirements")

*   The workspace must be enabled for Unity Catalog. Follow the [documentation](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) to create a Unity Catalog Metastore, enable it in a workspace, and create a Catalog.
*   A model must be registered in Unity Catalog to access online tables.
*   A Databricks admin must accept the Serverless Terms of Service in the account console.

## Work with online tables using the UI[​](#work-with-online-tables-using-the-ui "Direct link to Work with online tables using the UI")

This section describes how to create and delete online tables, and how to check the status and trigger updates of online tables.

### Create an online table using the UI[​](#create-an-online-table-using-the-ui "Direct link to Create an online table using the UI")

You create an online table using Catalog Explorer. For information about required permissions, see [User permissions](#permissions).

1.  To create an online table, the source Delta table must have a primary key. If the Delta table you want to use does not have a primary key, create one by following these instructions: [Use an existing Delta table in Unity Catalog as a feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc#use-existing-uc-table).
    
2.  In Catalog Explorer, navigate to the source table that you want to sync to an online table. From the **Create** menu, select **Online table**.
    
    ![select create online table](https://docs.databricks.com/aws/en/assets/images/create-online-table-473e834357fdf2f576706b4a9100850f.png)
    
3.  Use the selectors in the dialog to configure the online table.
    
    ![configure online table dialog](https://docs.databricks.com/aws/en/assets/images/create-online-table-dlg-58a18f30b560ef4a046628995b4d6ab8.png)
    
    **Name**: Name to use for the online table in Unity Catalog.
    
    **Primary Key**: Column(s) in the source table to use as primary key(s) in the online table.
    
    **Time series Key**: (Optional). Column in the source table to use as time series key. When specified, the online table includes only the row with the latest time series key value for each primary key.
    
    **Sync mode**: Specifies how the synchronization pipeline updates the online table. Select one of **Snapshot**, **Triggered**, or **Continuous**.
    

note

To support **Triggered** or **Continuous** sync mode, the source table must have [Change data feed](https://docs.databricks.com/aws/en/tables/features/change-data-feed) enabled.

1.  When you are done, click **Confirm**. The online table page appears.
2.  The new online table is created under the catalog, schema, and name specified in the creation dialog. In Catalog Explorer, the online table is indicated by ![online table icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFKADAAQAAAABAAAAFAAAAACy3fD9AAABjklEQVQ4Ec2UsYrCQBCG/4iNJkEwCIKFprMRtEklmEK0sc0z+EyaRxBsbSwEC1vRSpIilYVFiAiCIt45K7uX5fQMnAc3kOzs7L9fZjOTKB83wxst9UYWQ6U50Pd9BEHAp4nHbDYLy7KQTt9RAui6Li6XS2JQXJjP51GtVllIAAlGwXa7Hdf+6G+3W4zHYxwOB6ETQIpomgbTNMXiK+dRPf+uKJQNHWE6nb5KTKyHYSh87khHJiBdvzEJGC/K+XzGcDhErVZDq9V6+AxelPiiBIwX5XQ6MV0ul3taqGKxiFKpBMMwBFMCiugTh79f3lqZTAaVSkVSJwYul0tMJhPU63VROMqs0WhIwMRtQ8dLpWQ578Pj8SigiTMkYLfbZRv5kWmy2WwwGo3Q7/dRKBSQGEibOWi1WmGxWFCIWRRFmM1mcBznC6goCnvaYDBgouv1ysb1eg1VVdHpdO67b/dyuQxd19l8t9vB8zymoYDIsNlsYj6fSx86Cfb7/bdmp1aii4zGXq8H27bZXPn3f+xPkM2EfLFP96EAAAAASUVORK5CYII=).

### Get status and trigger updates using the UI[​](#get-status-and-trigger-updates-using-the-ui "Direct link to Get status and trigger updates using the UI")

To check the status of the online table, click the name of the table in the Catalog to open it. The online table page appears with the **Overview** tab open. The **Data Ingest** section shows the status of the latest update. To trigger an update, click **Sync now**. The **Data Ingest** section also includes a link to the pipeline that updates the table.

![view of online table page in catalog](https://docs.databricks.com/aws/en/assets/images/online-table-in-catalog-9abc629baf6cc4b16e840be66deeac36.png)

### Schedule periodic updates[​](#schedule-periodic-updates "Direct link to Schedule periodic updates")

For online tables with **Snapshot** or **Triggered** sync mode, you can schedule automatic periodic updates. The update schedule is managed by the pipeline that updates the table.

1.  In Catalog Explorer, navigate to the online table.
2.  In the **Data Ingest** section, click the link to the pipeline.
3.  In the upper-right corner, click **Schedule**, and add a new schedule or update existing schedules.

### Delete an online table using the UI[​](#delete-an-online-table-using-the-ui "Direct link to Delete an online table using the UI")

From the online table page, select **Delete** from the ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) kebab menu.

## Work with online tables using APIs[​](#work-with-online-tables-using-apis "Direct link to work-with-online-tables-using-apis")

You can also use the Databricks SDK or the REST API to create and manage online tables.

For reference information, see the reference documentation for the [Databricks SDK for Python](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/online_tables.html) or the [REST API](https://docs.databricks.com/api/workspace/onlinetables).

### Requirements[​](#requirements-1 "Direct link to Requirements")

Databricks SDK version 0.20 or above.

### Create an online table using APIs[​](#create-an-online-table-using-apis "Direct link to Create an online table using APIs")

*   Databricks SDK - Python
*   REST API

Python

    from pprint import pprintfrom databricks.sdk import WorkspaceClientfrom databricks.sdk.service.catalog import *w = WorkspaceClient(host='https://xxx.databricks.com', token='xxx')# Create an online tablespec = OnlineTableSpec(  primary_key_columns=["pk_col"],  source_table_full_name="main.default.source_table",  run_triggered=OnlineTableSpecTriggeredSchedulingPolicy.from_dict({'triggered': 'true'}))online_table = OnlineTable(  name="main.default.my_online_table",  # Fully qualified table name  spec=spec  # Online table specification)w.online_tables.create_and_wait(table=online_table)

The online table automatically starts syncing after it is created.

### Get status and trigger refresh using APIs[​](#get-status-and-trigger-refresh-using-apis "Direct link to Get status and trigger refresh using APIs")

You can view the status and the spec of the online table following the example below. If your online table is not continuous and you would like to trigger a manual refresh of its data, you can use the pipeline API to do so.

Use the pipeline ID associated with the online table in the online table spec and start a new update on the pipeline to trigger the refresh. This is equivalent to clicking **Sync now** in the online table UI in Catalog Explorer.

*   Databricks SDK - Python
*   REST API

Python

    pprint(w.online_tables.get('main.default.my_online_table'))# Sample responseOnlineTable(name='main.default.my_online_table',    spec=OnlineTableSpec(perform_full_copy=None,        pipeline_id='some-pipeline-id',        primary_key_columns=['pk_col'],        run_continuously=None,        run_triggered={},        source_table_full_name='main.default.source_table',        timeseries_key=None),    status=OnlineTableStatus(continuous_update_status=None,        detailed_state=OnlineTableState.PROVISIONING,        failed_status=None,        message='Online Table creation is '            'pending. Check latest status in '            'Lakeflow Declarative Pipelines: '            'https://xxx.databricks.com/pipelines/some-pipeline-id',        provisioning_status=None,        triggered_update_status=None))# Trigger an online table refresh by calling the pipeline API. To discard all existing data# in the online table before refreshing, set "full_refresh" to "True". This is useful if your# online table sync is stuck due to, for example, the source table being deleted and recreated# with the same name while the sync was running.w.pipelines.start_update(pipeline_id='some-pipeline-id', full_refresh=True)

### Delete an online table using APIs[​](#delete-an-online-table-using-apis "Direct link to Delete an online table using APIs")

*   Databricks SDK - Python
*   REST API

Python

    w.online_tables.delete('main.default.my_online_table')

Deleting the online table stops any ongoing data synchronization and releases all its resources.

## Serve online table data using a feature serving endpoint[​](#serve-online-table-data-using-a-feature-serving-endpoint "Direct link to Serve online table data using a feature serving endpoint")

For models and applications hosted outside of Databricks, you can create a feature serving endpoint to serve features from online tables. The endpoint makes features available at low latency using a REST API.

1.  Create a feature spec.
    
    When you create a feature spec, you specify the source Delta table. This allows the feature spec to be used in both offline and online scenarios. For online lookups, the serving endpoint automatically uses the online table to perform low-latency feature lookups.
    
    The source Delta table and the online table must use the same primary key.
    
    The feature spec can be viewed in the **Function** tab in Catalog Explorer.
    
    Python
    
        from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookupfe = FeatureEngineeringClient()fe.create_feature_spec(  name="catalog.default.user_preferences_spec",  features=[    FeatureLookup(      table_name="user_preferences",      lookup_key="user_id"    )  ])
    
2.  Create a feature serving endpoint.
    
    This step assumes that you have created an online table named `user_preferences_online_table` that synchonizes data from the Delta table `user_preferences`. Use the feature spec to create a feature serving endpoint. The endpoint makes data available through a REST API using the associated online table.
    
    note
    
    The user who performs this operation must be the owner of both the offline table and online table.
    
    *   Databricks SDK - Python
    *   Python API
    
    Python
    
        from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInputworkspace = WorkspaceClient()# Create endpointendpoint_name = "fse-location"workspace.serving_endpoints.create_and_wait(  name=endpoint_name,  config=EndpointCoreConfigInput(    served_entities=[      ServedEntityInput(        entity_name=feature_spec_name,        scale_to_zero_enabled=True,        workload_size="Small"      )    ]  ))
    
3.  Get data from the feature serving endpoint.
    
    To access the API endpoint, send an HTTP POST request to the endpoint URL. The example shows how to do this using Python APIs. For other languages and tools, see [Feature Serving](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving).
    
    Python
    
        # Set up credentialsexport DATABRICKS_TOKEN=...
    
    Python
    
        url = "https://{workspace_url}/serving-endpoints/user-preferences/invocations"headers = {'Authorization': f'Bearer {DATABRICKS_TOKEN}', 'Content-Type': 'application/json'}data = {  "dataframe_records": [{"user_id": user_id}]}data_json = json.dumps(data, allow_nan=True)response = requests.request(method='POST', headers=headers, url=url, data=data_json)if response.status_code != 200:  raise Exception(f'Request failed with status {response.status_code}, {response.text}')print(response.json()['outputs'][0]['hotel_preference'])
    

## Use online tables with RAG applications[​](#use-online-tables-with-rag-applications "Direct link to Use online tables with RAG applications")

RAG applications are a common use case for online tables. You create an online table for the structured data that the RAG application needs and host it on a feature serving endpoint. The RAG application uses the feature serving endpoint to look up relevant data from the online table.

The typical steps are as follows:

1.  Create a feature serving endpoint.
2.  Create a tool using LangChain or any similar package that uses the endpoint to look up relevant data.
3.  Use the tool in a LangChain agent or similar agent to retrieve relevant data.
4.  Create a model serving endpoint to host the application.

For step-by-step instructions and an example notebook, see [Example: use features with structured RAG applications](https://docs.databricks.com/aws/en/machine-learning/feature-store/rag).

## Notebook examples[​](#notebook-examples "Direct link to notebook-examples")

The following notebook illustrates how to publish features to online tables for real-time serving and automated feature lookup.

#### Online tables demo notebook

## Use online tables with Model Serving[​](#use-online-tables-with-model-serving "Direct link to Use online tables with Model Serving")

You can use online tables to look up features for Model Serving. When you sync a feature table to an online table, models trained using features from that feature table automatically look up feature values from the online table during inference. No additional configuration is required.

1.  Use a `FeatureLookup` to train the model.
    
    For model training, use features from the offline feature table in the model training set, as shown in the following example:
    
    Python
    
        training_set = fe.create_training_set(  df=id_rt_feature_labels,  label='quality',  feature_lookups=[      FeatureLookup(          table_name="user_preferences",          lookup_key="user_id"      )  ],  exclude_columns=['user_id'],)
    
2.  Serve the model with Model Serving. The model automatically looks up features from the online table. See [Model Serving with automatic feature lookup](https://docs.databricks.com/aws/en/machine-learning/feature-store/automatic-feature-lookup) for details.
    

## User permissions[​](#user-permissions "Direct link to user-permissions")

You must have the following permissions to create an online table:

*   `SELECT` privilege on the source table.
*   `USE CATALOG` privilege on the destination catalog.
*   `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema.

To manage the data synchronization pipeline of an online table, you must either be the owner of the online table or be granted the REFRESH privilege on the online table. Users who do not have `USE CATALOG` and `USE SCHEMA` privileges on the catalog will not see the online table in Catalog Explorer.

The Unity Catalog metastore must have [Privilege Model Version 1.0](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model).

## Endpoint permission model[​](#endpoint-permission-model "Direct link to Endpoint permission model")

A unique service principal is automatically created for a feature serving or model serving endpoint with limited permissions required to query data from online tables. This service principal allows endpoints to access data independently of the user who created the resource and ensures that the endpoint can continue to function if the creator leaves the workspace.

The lifetime of this service principal is the lifetime of the endpoint. Audit logs may indicate system generated records for the owner of the Unity Catalog catalog granting necessary privileges to this service principal.

## Limitations[​](#limitations "Direct link to Limitations")

*   Only one online table is supported per source table.
*   An online table and its source table can have at most 1000 columns.
*   Columns of data types ARRAY, MAP, or STRUCT cannot be used as primary keys in the online table.
*   If a column is used as a primary key in the online table, all rows in the source table where the column contains null values are ignored.
*   Foreign, system, and internal tables are not supported as source tables.
*   Source tables without Delta change data feed enabled support only the **Snapshot** sync mode.
*   OpenSharing tables are only supported in the **Snapshot** sync mode.
*   Catalog, schema, and table names of the online table can only contain alphanumeric characters and underscores, and must not start with numbers. Dashes (`-`) are not allowed.
*   Columns of String type are limited to 64KB length.
*   Column names are limited to 64 characters in length.
*   The maximum size of the row is 2MB.
*   The combined size of all online tables in a Unity Catalog metastore during public preview is 2TB uncompressed user data.
*   The maximum read throughput for a metastore is approximately 750 MB/sec.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### I don't see the **Create online table** option[​](#i-dont-see-the-create-online-table-option "Direct link to i-dont-see-the-create-online-table-option")

The cause is usually that the table you are trying to sync from (the source table) is not a supported type. Make sure the source table's Securable Kind (shown in the Catalog Explorer **Details** tab) is one of the supported options below:

*   `TABLE_EXTERNAL`
*   `TABLE_DELTA`
*   `TABLE_DELTA_EXTERNAL`
*   `TABLE_DELTASHARING`
*   `TABLE_DELTASHARING_MUTABLE`
*   `TABLE_STREAMING_LIVE_TABLE`
*   `TABLE_STANDARD`
*   `TABLE_FEATURE_STORE`
*   `TABLE_FEATURE_STORE_EXTERNAL`
*   `TABLE_VIEW`
*   `TABLE_VIEW_DELTASHARING`
*   `TABLE_MATERIALIZED_VIEW`

### I can't select either **Triggered** or **Continuous** sync modes when I create an online table[​](#i-cant-select-either-triggered-or-continuous-sync-modes-when-i-create-an-online-table "Direct link to i-cant-select-either-triggered-or-continuous-sync-modes-when-i-create-an-online-table")

This happens if the source table does not have Delta change data feed enabled or if it is a View or materialized view. To use the **Incremental** sync mode, either enable change data feed on the source table, or use a non-view table.

### Online table update fails or status shows offline[​](#online-table-update-fails-or-status-shows-offline "Direct link to Online table update fails or status shows offline")

To begin troubleshooting this error, click the pipeline id that appears in the **Overview** tab of the online table in Catalog Explorer.

![online tables pipeline failure](https://docs.databricks.com/aws/en/assets/images/online-tables-failed-pipeline-80fd13797fbc284dc89c33feb8a9084f.png)

On the pipeline UI page that appears, click on the entry that says “Failed to resolve flow '\_\_online\_table”.

![online tables pipeline error message](https://docs.databricks.com/aws/en/assets/images/online-tables-pipeline-error-54630bd1b8bccd3d80266150b5003930.png)

A popup appears with details in the **Error details** section.

![online tables details of error](https://docs.databricks.com/aws/en/assets/images/online-tables-error-details-122778cf32fa1c386a8cf329575ef28c.png)

Common causes of errors include the following:

*   The source table was deleted, or deleted and recreated with the same name, while the online table was synchronizing. This is particularly common with continuous online tables, because they are constantly synchronizing.
    
*   The source table cannot be accessed through Serverless Compute due to firewall settings. In this situation, the **Error details** section might show the error message “Failed to start the Lakeflow Spark Declarative Pipelines service on cluster xxx…”.
    
*   The aggregate size of online tables exceeds the 2 TB (uncompressed size) metastore-wide limit. The 2 TB limit refers to the uncompressed size after expanding the Delta table in row-oriented format. The size of the table in row-format can be significantly larger than the size of the Delta table shown in Catalog Explorer, which refers to the compressed size of the table in a column-oriented format. The difference can be as large as 100x, depending on the content of the table.
    
    To estimate the uncompressed, row-expanded size of a Delta table, use the following query from a Serverless SQL Warehouse. The query returns the estimated expanded table size in bytes. Successfully executing this query also confirms that Serverless Compute can access the source table.
    
    SQL
    
        SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
