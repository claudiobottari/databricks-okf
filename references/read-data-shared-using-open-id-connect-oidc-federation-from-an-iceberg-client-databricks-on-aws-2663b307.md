---
title: Read data shared using Open ID Connect (OIDC) federation from an Iceberg client | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-iceberg
ingestedAt: "2026-06-18T08:05:58.835Z"
---

This page describes how Open ID Connect (OIDC) federation data recipients can use an Iceberg REST Catalog (IRC) client, such as OSS Spark or Snowflake, to access OpenSharing shares created in Databricks.

If you are using bearer tokens to manage authentication instead, see [Create a recipient object for non-Databricks users using bearer tokens (Databricks-to-Open sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token).

This page is intended for recipients. For information about how providers can enable OIDC federation for recipients in Databricks, see [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed).

## Get your Iceberg profile from the OIDC portal[​](#get-your-iceberg-profile-from-the-oidc-portal "Direct link to Get your Iceberg profile from the OIDC portal")

1.  Go to the OIDC profile portal URL that the Databricks provider shared with you.
    
    Request the URL if you haven't yet received it.
    
2.  On the portal page, click **Download file**.
    
3.  In the downloaded file, replace `clientId`, `clientSecret`, and `scope` with your values.
    
4.  Import the share profile file with your client code.
    

You can access the data using any Iceberg REST Catalog.

### Snowflake[​](#snowflake "Direct link to Snowflake")

In your Snowflake worksheet, run the following command to create a catalog integration. You can also copy the SQL command from the OIDC profile portal your provider shared with you.

Replace the placeholder values before running it:

*   `<catalog-integration-name>`: A name for the catalog integration.
*   `<catalog-uri>`: The Iceberg REST Catalog endpoint from your downloaded profile file.
*   `<share-name>`: The share name granted to you.
*   `<oauth-token-uri>`: Your IdP's OAuth token endpoint.
*   `<oauth-client-id>` and `<oauth-client-secret>`: Your OAuth credentials.
*   `<oauth-scope>`: Your OAuth scope.

SQL

    USE ROLE ACCOUNTADMIN;CREATE OR REPLACE CATALOG INTEGRATION <catalog-integration-name>    CATALOG_SOURCE = ICEBERG_REST    TABLE_FORMAT = ICEBERG    REST_CONFIG = (        CATALOG_URI = '<catalog-uri>'        WAREHOUSE = '<share-name>'        ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS    )    REST_AUTHENTICATION = (        TYPE = OAUTH        OAUTH_TOKEN_URI = '<oauth-token-uri>'        OAUTH_CLIENT_ID = '<oauth-client-id>'        OAUTH_CLIENT_SECRET = '<oauth-client-secret>'        OAUTH_ALLOWED_SCOPES = ('<oauth-scope>')    )    REFRESH_INTERVAL_SECONDS = 30    ENABLED = TRUE;

Create a linked database that uses the catalog integration. Replace `<database-name>` with a name for the database.

SQL

    CREATE DATABASE <database-name>    LINKED_CATALOG = (        CATALOG = <catalog-integration-name>    );

### OSS Spark[​](#oss-spark "Direct link to OSS Spark")

The following example reads shared data from an Iceberg REST Catalog using OSS Spark. Run it from a Spark installation that includes the Iceberg Spark runtime and AWS bundle JARs.

Replace the placeholder values before running it:

*   `<spark-home>`: The path to your Spark installation.
*   `<iceberg-jars-path>`: The path to your Iceberg JAR files.
*   `<catalog-uri>`: The Iceberg REST Catalog endpoint from your downloaded profile file.
*   `<share-name>`: The share name granted to you.
*   `<oauth-token-uri>`: Your IdP's OAuth token endpoint.
*   `<oauth-client-id>` and `<oauth-client-secret>`: Your OAuth credentials.
*   `<oauth-scope>`: Your OAuth scope.
*   `<spark-script>`: The path to the Scala script to run.

Bash

    JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 PATH=/usr/lib/jvm/java-17-openjdk-amd64/bin:$PATH <spark-home>/bin/spark-shell \  --jars <iceberg-jars-path>/iceberg-spark-runtime-4.0_2.13-1.10.2.jar,<iceberg-jars-path>/iceberg-aws-bundle-1.10.2.jar \  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \  --conf spark.sql.catalog.databricks=org.apache.iceberg.spark.SparkCatalog \  --conf spark.sql.catalog.databricks.type=rest \  --conf spark.sql.catalog.databricks.uri=<catalog-uri> \  --conf spark.sql.catalog.databricks.warehouse=<share-name> \  --conf spark.sql.catalog.databricks.rest.auth.type=oauth2 \  --conf spark.sql.catalog.databricks.oauth2-server-uri=<oauth-token-uri> \  --conf spark.sql.catalog.databricks.credential=<oauth-client-id>:<oauth-client-secret> \  --conf spark.sql.catalog.databricks.scope=<oauth-scope> \  --conf spark.sql.catalog.databricks.io-impl=org.apache.iceberg.aws.s3.S3FileIO \  < <spark-script>
