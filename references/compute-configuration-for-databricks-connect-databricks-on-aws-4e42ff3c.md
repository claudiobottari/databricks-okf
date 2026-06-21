---
title: Compute configuration for Databricks Connect | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config
ingestedAt: "2026-06-18T08:06:10.528Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This page describes different ways of configuring a connection between Databricks Connect and your Databricks [cluster](#cluster) or [serverless compute](#serverless).

Databricks Connect enables you to connect popular IDEs such as Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ IDEA, notebook servers, and other custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

## Setup[​](#setup "Direct link to Setup")

Before you begin, you need the following:

*   Databricks Connect installed. For installation requirements, see [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).
*   The Databricks [workspace instance name](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url). This is the **Server Hostname** value for your compute. See [Get connection details for a Databricks compute resource](https://docs.databricks.com/aws/en/integrations/compute-details).
*   If you are connecting to classic compute, the ID of your cluster. You can retrieve the cluster ID from the URL. See [Compute resource URL and ID](https://docs.databricks.com/aws/en/workspace/workspace-details#compute-resource-url-and-id).

## Configure a connection to a cluster[​](#configure-a-connection-to-a-cluster "Direct link to configure-a-connection-to-a-cluster")

There are multiple ways to configure the connection to your cluster. Databricks Connect searches for configuration properties in the following order, and uses the first configuration it finds. For advanced configuration information, see [Advanced usage of Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/advanced).

1.  [The DatabricksSession class's remote() method](#remote-method).
2.  [A Databricks configuration profile](#config-profile)
3.  [The DATABRICKS\_CONFIG\_PROFILE environment variable](#config-profile-env-var)
4.  [An environment variable for each configuration property](#all-env-var)
5.  [A Databricks configuration profile named DEFAULT](#default-config-profile)

### The `DatabricksSession` class's `remote()` method[​](#the-databrickssession-classs-remote-method "Direct link to the-databrickssession-classs-remote-method")

For this option, which applies to [Authenticate with Databricks personal access tokens (legacy)](https://docs.databricks.com/aws/en/dev-tools/auth/pat) only, specify the workspace instance name, the Databricks personal access token, and the ID of the cluster.

You can initialize the `DatabricksSession` class in several ways:

*   Set the `host`, `token`, and `cluster_id` fields in `DatabricksSession.builder.remote()`.
*   Use the Databricks SDK's `Config` class.
*   Specify a Databricks configuration profile along with the `cluster_id` field.

Instead of specifying these connection properties in your code, Databricks recommends configuring properties through environment variables or configuration files, as described throughout this section. The following code examples assume that you provide some implementation of the proposed `retrieve_*` functions to get the necessary properties from the user or from some other configuration store, such as [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).

The code for each of these approaches is as follows:

*   Python
*   Scala

Python

    # Set the host, token, and cluster_id fields in DatabricksSession.builder.remote.# If you have already set the DATABRICKS_CLUSTER_ID environment variable with the# cluster's ID, you do not also need to set the cluster_id field here.from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.remote(host       = f"https://{retrieve_workspace_instance_name()}",token      = retrieve_token(),cluster_id = retrieve_cluster_id()).getOrCreate()

*   Python
*   Scala

Python

    # Use the Databricks SDK's Config class.# If you have already set the DATABRICKS_CLUSTER_ID environment variable with the# cluster's ID, you do not also need to set the cluster_id field here.from databricks.connect import DatabricksSessionfrom databricks.sdk.core import Configconfig = Config(host       = f"https://{retrieve_workspace_instance_name()}",token      = retrieve_token(),cluster_id = retrieve_cluster_id())spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

*   Python
*   Scala

Python

    # Specify a Databricks configuration profile along with the `cluster_id` field.# If you have already set the DATABRICKS_CLUSTER_ID environment variable with the# cluster's ID, you do not also need to set the cluster_id field here.from databricks.connect import DatabricksSessionfrom databricks.sdk.core import Configconfig = Config(profile    = "<profile-name>",cluster_id = retrieve_cluster_id())spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

### A Databricks configuration profile[​](#a-databricks-configuration-profile "Direct link to a-databricks-configuration-profile")

For this option, create or identify a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) containing the field `cluster_id` and any other fields that are necessary for the [Databricks authentication type](https://docs.databricks.com/aws/en/dev-tools/auth/#auth-types) that you want to use.

The required configuration profile fields for each authentication type are as follows:

*   For Databricks [personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat): `host` and `token`.
*   For [OAuth machine-to-machine (M2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) (where supported): `host`, `client_id`, and `client_secret`.
*   For [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) (where supported): `host`.

Then set the name of this configuration profile through the configuration class.

note

You can use the `auth login` command's `--configure-cluster` option to automatically add the `cluster_id` field to a new or existing configuration profile. For more information, run the command `databricks auth login -h`.

You can specify `cluster_id` in a couple of ways:

*   Include the `cluster_id` field in your configuration profile, and then just specify the configuration profile's name.
*   Specify the configuration profile name along with the `cluster_id` field.

If you have already set the `DATABRICKS_CLUSTER_ID` environment variable with the cluster's ID, you do not also need to specify `cluster_id`.

The code for each of these approaches is as follows:

*   Python
*   Scala

Python

    # Include the cluster_id field in your configuration profile, and then# just specify the configuration profile's name:from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.profile("<profile-name>").getOrCreate()

*   Python
*   Scala

Python

    # Specify the configuration profile name along with the cluster_id field.# In this example, retrieve_cluster_id() assumes some custom implementation that# you provide to get the cluster ID from the user or from some other# configuration store:from databricks.connect import DatabricksSessionfrom databricks.sdk.core import Configconfig = Config(profile    = "<profile-name>",cluster_id = retrieve_cluster_id())spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

### The `DATABRICKS_CONFIG_PROFILE` environment variable[​](#the-databricks_config_profile-environment-variable "Direct link to the-databricks_config_profile-environment-variable")

For this option, create or identify a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) containing the field `cluster_id` and any other fields that are necessary for the [Databricks authentication type](https://docs.databricks.com/aws/en/dev-tools/auth/#auth-types) that you want to use.

If you have already set the `DATABRICKS_CLUSTER_ID` environment variable with the cluster's ID, you do not also need to specify `cluster_id`.

The required configuration profile fields for each authentication type are as follows:

*   For Databricks [personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat): `host` and `token`.
*   For [OAuth machine-to-machine (M2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) (where supported): `host`, `client_id`, and `client_secret`.
*   For [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) (where supported): `host`.

note

You can use the `auth login` command's `--configure-cluster` to automatically add the `cluster_id` field to a new or existing configuration profile. For more information, run the command `databricks auth login -h`.

Set the `DATABRICKS_CONFIG_PROFILE` environment variable to the name of this configuration profile. Then initialize the `DatabricksSession` class:

*   Python
*   Scala

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()

### An environment variable for each configuration property[​](#an-environment-variable-for-each-configuration-property "Direct link to an-environment-variable-for-each-configuration-property")

For this option, set the `DATABRICKS_CLUSTER_ID` environment variable and any other environment variables that are necessary for the [Databricks authentication type](https://docs.databricks.com/aws/en/dev-tools/auth/#auth-types) that you want to use.

The required environment variables for each authentication type are as follows:

*   For Databricks [personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat): `DATABRICKS_HOST` and `DATABRICKS_TOKEN`.
*   For [OAuth machine-to-machine (M2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m): `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, and `DATABRICKS_CLIENT_SECRET`.
*   For [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m): `DATABRICKS_HOST`.

Then initialize the `DatabricksSession` class:

*   Python
*   Scala

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()

### A Databricks configuration profile named `DEFAULT`[​](#a-databricks-configuration-profile-named-default "Direct link to a-databricks-configuration-profile-named-default")

For this option, create or identify a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) containing the field `cluster_id` and any other fields that are necessary for the [Databricks authentication type](https://docs.databricks.com/aws/en/dev-tools/auth/#auth-types) that you want to use.

If you have already set the `DATABRICKS_CLUSTER_ID` environment variable with the cluster's ID, you do not also need to specify `cluster_id`.

The required configuration profile fields for each authentication type are as follows:

*   For Databricks [personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat): `host` and `token`.
*   For [OAuth machine-to-machine (M2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) (where supported): `host`, `client_id`, and `client_secret`.
*   For [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) (where supported): `host`.

Name this configuration profile `DEFAULT`.

note

You can use the `auth login` command's `--configure-cluster` option to automatically add the `cluster_id` field to the `DEFAULT` configuration profile. For more information, run the command `databricks auth login -h`.

Then initialize the `DatabricksSession` class:

*   Python
*   Scala

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()

## Configure a connection to serverless compute[​](#configure-a-connection-to-serverless-compute "Direct link to configure-a-connection-to-serverless-compute")

Databricks Connect for Python and Scala support connecting to serverless compute. To use this feature, version requirements for connecting to serverless must be met. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).

For Python, you can configure a connection to serverless compute in your local environment:

*   Set the local environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`. If this environment variable is set, Databricks Connect ignores the `cluster_id`.
    
*   In a local Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles), set `serverless_compute_id = auto`, then reference that profile from your code.
    
        [DEFAULT]host = https://my-workspace.cloud.databricks.com/serverless_compute_id = autotoken = dapi123...
    

Or for Python or Scala:

*   Python
*   Scala

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.serverless().getOrCreate()

Python

    from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.remote(serverless=True).getOrCreate()

## Validate the connection to Databricks[​](#validate-the-connection-to-databricks "Direct link to validate-the-connection-to-databricks")

To validate that your environment, default credentials, and connection to compute are correctly set up for Databricks Connect, run the `databricks-connect test` command:

This command fails with a non-zero exit code and a corresponding error message when it detects any incompatibility in the setup, such as when the Databricks Connect version is incompatible with the Databricks serverless compute version. For Databricks Connect version support information, see [Databricks Connect versions](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).

In Databricks Connect 14.3 and above, you can also validate your environment using `validateSession()`:

    DatabricksSession.builder.validateSession(True).getOrCreate()

## Disabling Databricks Connect[​](#disabling-databricks-connect "Direct link to Disabling Databricks Connect")

Databricks Connect (and the underlying Spark Connect) services can be disabled on any given cluster.

To disable the Databricks Connect service, set the following [Spark configuration](https://docs.databricks.com/aws/en/compute/configure#spark-configuration) on the cluster.

    spark.databricks.service.server.enabled false
