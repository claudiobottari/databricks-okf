---
title: Advanced usage of Databricks Connect | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/advanced
ingestedAt: "2026-06-18T08:06:08.886Z"
---

note

This article covers Databricks Connect for Databricks Runtime 14.0 and above.

This article describes topics that go beyond the basic setup of Databricks Connect.

## Configure the Spark Connect connection string[​](#configure-the-spark-connect-connection-string "Direct link to Configure the Spark Connect connection string")

In addition to connecting to your cluster using the options outlined in [Configure a connection to a cluster](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#cluster), a more advanced option is connecting using the Spark Connect connection string. You can pass the string in the `remote` function or set the `SPARK_REMOTE` environment variable.

*   Python
*   Scala

To set the connection string using the `remote` function:

Python

    from databricks.connect import DatabricksSessionworkspace_instance_name = retrieve_workspace_instance_name()token                   = retrieve_token()cluster_id              = retrieve_cluster_id()spark = DatabricksSession.builder.remote(   f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id}").getOrCreate()

Alternatively, set the `SPARK_REMOTE` environment variable:

    sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>

Then initialize the `DatabricksSession` class:

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()

## Use Spark Connect server with Databricks Connect[​](#use-spark-connect-server-with-databricks-connect "Direct link to Use Spark Connect server with Databricks Connect")

You can optionally run Databricks Connect against an open source Spark Connect server.

important

Some features available in Databricks Runtime and Databricks Connect are exclusive to Databricks or not yet released in open source Apache Spark. If your code relies on these features, the following steps may fail with errors.

1.  Start a local Spark Connect server. See [How to use Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html?utm_source=chatgpt.com#how-to-use-spark-connect)
    
2.  Configure Databricks Connect. Set the environment variable `SPARK_REMOTE` to point to your local Spark Connect server. See [Connecting to Spark Connect using Clients](https://github.com/apache/spark/blob/master/sql/connect/docs/client-connection-string.md).
    
        export SPARK_REMOTE="sc://localhost"
    
3.  Initialize the Databricks session:
    
    *   Python
    *   Scala
    
    Python
    
        from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()
    

Databricks Connect communicates with the Databricks Clusters via gRPC over HTTP/2.

To have better control over the requests coming from clients, advanced users may choose to install a proxy service between the client and the Databricks cluster. In some cases the proxies may require custom headers in the HTTP requests.

Use the header() method to add custom headers to HTTP requests:

*   Python
*   Scala

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.header('x-custom-header', 'value').getOrCreate()

## Certificates[​](#certificates "Direct link to Certificates")

If your cluster relies on a custom SSL/TLS certificate to resolve a Databricks workspace fully qualified domain name (FQDN), you must set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` on your local development machine. This environment variable must be set to the full path to the installed certificate on the cluster.

*   Python
*   Scala

The following example sets this environment variable:

Python

    import osos.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"

For other ways to set environment variables, see your operating system's documentation.

## Logging and debug logs[​](#logging-and-debug-logs "Direct link to Logging and debug logs")

*   Python
*   Scala

Databricks Connect for Python produces logs using standard [Python logging](https://docs.python.org/3/library/logging.html).

Logs are emitted to the standard error stream (_stderr_) and by default they are turned off. Setting an environment variable `SPARK_CONNECT_LOG_LEVEL=debug` will modify this default and print all log messages at the `DEBUG` level and higher.
