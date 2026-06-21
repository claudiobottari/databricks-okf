---
title: Databricks Connect usage requirements | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements
ingestedAt: "2026-06-18T08:06:36.546Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article provides usage requirements for Databricks Connect. For information about Databricks Connect, see [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

## Workspace requirements[​](#workspace-requirements "Direct link to workspace-requirements")

To use Databricks Connect to connect to your workspace:

*   Your Databricks account and workspace must have Unity Catalog enabled. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) and [Enable a workspace for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces).
    
*   The Databricks Runtime version of your compute must be greater than or equal to the Databricks Connect package version. Databricks recommends that you use the most recent Databricks Connect package that matches your Databricks Runtime version.
    
    To use features that are available in later versions of the Databricks Runtime, you must upgrade the Databricks Connect package. See the [Databricks Connect release notes](https://docs.databricks.com/aws/en/release-notes/dbconnect/) for a list of available Databricks Connect releases. For Databricks Runtime version release notes, see [Databricks Runtime release notes versions and compatibility](https://docs.databricks.com/aws/en/release-notes/runtime/).
    
*   If you are connecting to [serverless compute](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#serverless), your workspace must meet the [requirements for serverless compute](https://docs.databricks.com/aws/en/compute/serverless/#requirements).
    
    note
    
    Serverless compute is supported starting with Databricks Connect version 15.1. Versions of Databricks Connect that are lower than or equal to the Databricks Runtime release on serverless are fully compatible. See [Release notes](https://docs.databricks.com/aws/en/release-notes/serverless/#release-notes). To verify if the Databricks Connect version is compatible with serverless compute, see [Validate the connection to Databricks](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#validate).
    
*   If you are connecting to a [cluster](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#cluster), your target cluster must use a cluster access mode of Assigned or Shared. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode).
    

## Local environment requirements[​](#local-environment-requirements "Direct link to Local environment requirements")

To install Databricks Connect, your local development environment must meet the following requirements:

*   Python
*   Scala

*   Authentication to Databricks is configured. Depending on the [Databricks authentication type](https://docs.databricks.com/aws/en/dev-tools/auth/#auth-types) there might be requirements:
    
    *   For [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m), you must use the Databricks CLI to authenticate before you run your code. To install and configure the Databricks CLI, see [Install or update the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install). See also the [Databricks Connect for Python tutorial](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-cluster).
        
    *   [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) and [OAuth machine-to-machine (M2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) are supported on Databricks SDK for Python 0.19.0 and above. To update your project's installed version of the Databricks SDK for Python, see [Get started with the Databricks SDK for Python](https://docs.databricks.com/aws/en/dev-tools/sdk-python#get-started).
        
*   Python 3 is installed, and the minor version of Python installed meets the version requirements in the [version compatibility table](#versions) below.
    
*   If you are using user-defined functions (UDFs), the local minor version of Python matches the minor version of Python of the Databricks Runtime version of the cluster or serverless compute. To find the minor Python version of the Databricks Runtime version of your cluster, refer to the _System environment_ section of the Databricks Runtime release notes for that version. See [Databricks Runtime release notes versions and compatibility](https://docs.databricks.com/aws/en/release-notes/runtime/) and [Serverless compute release notes](https://docs.databricks.com/aws/en/release-notes/serverless/).
    

### Databricks Connect versions[​](#databricks-connect-versions "Direct link to databricks-connect-versions")

The following table shows supported Databricks Connect and compatible language versions. Databricks Connect version numbers correspond to Databricks Runtime version numbers. See the [Databricks Connect release notes](https://docs.databricks.com/aws/en/release-notes/dbconnect/) for a list of available Databricks Connect releases. For Databricks Runtime version release notes, see [Databricks Runtime release notes versions and compatibility](https://docs.databricks.com/aws/en/release-notes/runtime/).

*   Python
*   Scala

#### End-of-support versions[​](#end-of-support-versions "Direct link to End-of-support versions")

Databricks Connect follows the Databricks Runtime [support lifecycles](https://docs.databricks.com/aws/en/release-notes/runtime/databricks-runtime-ver#databricks-runtime-support-lifecycles). The following versions have reached end-of-support. If you're using a version of Databricks Connect that has reached end-of-support, upgrade to a [supported version](#versions).

*   Python
*   Scala
