---
title: What is OpenSharing? | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/
ingestedAt: "2026-06-18T08:05:12.032Z"
---

This page introduces OpenSharing in Databricks, the secure data sharing platform that lets you share data and AI assets in Databricks with users outside your organization, regardless of whether they use Databricks. OpenSharing is also the basis for [Databricks Marketplace](https://docs.databricks.com/aws/en/marketplace/), an open forum for exchanging data products, and [Clean Rooms](https://docs.databricks.com/aws/en/clean-rooms/), a secure and privacy-protecting environment where multiple parties can work together on sensitive enterprise data.

OpenSharing is also available as an [open-source project](https://opensharing.io/) that you can use to share Delta tables from other platforms.

## How does OpenSharing work?[​](#how-does-opensharing-work "Direct link to how-does-opensharing-work")

[OpenSharing](https://opensharing.io/) is an [open protocol](https://go.delta.io/sharing) developed by Databricks for secure data sharing with other organizations. It works regardless of the computing platforms those organizations use.

There are a few ways to share data using OpenSharing:

1.  **The Databricks-to-Databricks sharing protocol**, which lets you share data and AI assets from your Unity Catalog\-enabled workspace with users who also have access to a Unity Catalog\-enabled Databricks workspace.
    
    This approach uses the OpenSharing server that is built into Databricks. It supports some OpenSharing features that are not supported in the other protocols, including notebook sharing, Unity Catalog volume sharing, Unity Catalog AI model sharing, Unity Catalog data governance, auditing, and usage tracking for both providers and recipients. The integration with Unity Catalog simplifies setup and governance for both providers and recipients and improves performance.
    
    See [What is the OpenSharing Databricks-to-Databricks protocol?](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks).
    
2.  **The Databricks-to-Open sharing protocol**, which lets you share tabular data that you manage in a Unity Catalog\-enabled Databricks workspace with users on any computing platform.
    
    This approach uses the OpenSharing server that is built into Databricks and is useful when you manage data using Unity Catalog and want to share it with users who don't use Databricks or don't have access to a Unity Catalog\-enabled Databricks workspace. The integration with Unity Catalog on the provider side simplifies setup and governance for providers.
    
    See [What is the OpenSharing Databricks-to-Open sharing protocol?](https://docs.databricks.com/aws/en/delta-sharing/share-data-open).
    
3.  **A customer-managed implementation of the open-source OpenSharing server**, which lets you share from any platform to any platform, whether Databricks or not.
    
    The Databricks documentation does not cover instructions for setting up your own OpenSharing server. See [the open source project](https://go.delta.io/sharing).
    
4.  **The SAP Business Data Cloud (BDC) Connector for Databricks**, which lets you share data between your Unity Catalog\-enabled workspace and an SAP BDC account.
    
    This approach uses the SAP BDC Connector, which utilizes OpenSharing for live, zero-copy access to SAP BDC data products.
    
    See [What is the SAP BDC Connector for Databricks?](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/#what-is).
    

The primary concepts underlying OpenSharing in Databricks are _shares_, _providers_, and _recipients_.

In OpenSharing, a _share_ is a read-only collection of tables and table partitions that a provider wants to share with one or more recipients. If your recipient uses a Unity Catalog\-enabled Databricks workspace, you can also include notebook files, views (including dynamic views that restrict access at the row and column level), Unity Catalog volumes, and Unity Catalog models in a share.

You can add or remove tables, streaming tables, managed Iceberg tables, views, materialized views, volumes, models, and notebook files from a share at any time, and you can assign or revoke data recipient access to a share at any time.

In a Unity Catalog\-enabled Databricks workspace, a share is a securable object registered in Unity Catalog. If you remove a share from your Unity Catalog metastore, all recipients of that share lose the ability to access it.

See [Create shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/create-share).

### What is a provider?[​](#what-is-a-provider "Direct link to What is a provider?")

A _provider_ is an entity that shares data with a recipient. If you are a provider and you want to take advantage of the built-in Databricks OpenSharing server and manage shares and recipients using Unity Catalog, you need at least one Databricks workspace that is enabled for Unity Catalog. You do not need to migrate all of your existing workspaces to Unity Catalog. You can simply create a new Unity Catalog\-enabled workspace for your OpenSharing needs.

If a recipient is on a Unity Catalog\-enabled Databricks workspace, the provider is also a Unity Catalog securable object that represents the provider organization and associates that organization with a set of shares.

### What is a recipient?[​](#what-is-a-recipient "Direct link to What is a recipient?")

A _recipient_ is an entity that receives shares from a provider. In Unity Catalog, a share is a securable object that represents an organization and associates it with a credential or secure sharing identifier that allows that organization to access one or more shares.

As a data provider (sharer), you can define multiple recipients for any given Unity Catalog metastore, but if you want to share data from multiple metastores with a particular user or group of users, you must define the recipient separately for each metastore. A recipient can have access to multiple shares.

If a provider deletes a recipient from their Unity Catalog metastore, that recipient loses access to all shares it could previously access.

See [Create data recipients for OpenSharing (Databricks-to-Databricks sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient).

## Databricks-to-Open sharing versus Databricks-to-Databricks sharing[​](#databricks-to-open-sharing-versus-databricks-to-databricks-sharing "Direct link to databricks-to-open-sharing-versus-databricks-to-databricks-sharing")

This section describes the two protocols for sharing from a Databricks workspace that is enabled for Unity Catalog.

note

This section assumes that the provider is on a Unity Catalog\-enabled Databricks workspace. To learn about setting up an open-source OpenSharing server to share from a non-Databricks platform or non-Unity Catalog workspace, see [the open source project](https://go.delta.io/sharing).

The way a provider uses OpenSharing in Databricks depends on who they are sharing data with:

*   _Open sharing_ lets you share data with any user, whether or not they have access to Databricks.
*   _Databricks-to-Databricks sharing_ lets you share data with Databricks users whose workspace is attached to a Unity Catalog metastore that is different from yours. Databricks-to-Databricks also supports notebook, volume, and model sharing, which is not available in Databricks-to-Open sharing.

### What is open OpenSharing?[​](#what-is-open-opensharing "Direct link to what-is-open-opensharing")

If you want to share data with users outside of your Databricks workspace, regardless of whether they use Databricks, you can use open OpenSharing to share your data securely. As a data provider, you manage authentication with the sharing recipient using either of the following methods:

*   You generate a long-lived bearer token and share it securely with the recipient. They use the token to authenticate and get read access to the tables you've included in the shares you've given them access to.
*   You use Open ID Connect (OIDC) federation, granting short-lived Databricks OAuth tokens to the recipient in exchange for JWT tokens that the recipient's identity provider (IdP) passes to Databricks.

Recipients can access the shared data using many computing tools and platforms, including:

*   Databricks
*   Apache Spark
*   Pandas
*   Power BI

For a full list of OpenSharing connectors and information about how to use them, see the [OpenSharing](https://opensharing.io/) documentation.

See also [What is the OpenSharing Databricks-to-Open sharing protocol?](https://docs.databricks.com/aws/en/delta-sharing/share-data-open).

### What is Databricks-to-Databricks OpenSharing?[​](#what-is-databricks-to-databricks-opensharing "Direct link to what-is-databricks-to-databricks-opensharing")

If you want to share data with users who have a Databricks workspace that is [enabled for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces), you can use Databricks-to-Databricks OpenSharing. Databricks-to-Databricks sharing lets you share data with users in other Databricks accounts, whether they're on AWS, Azure, or GCP. It's also a great way to securely share data across different Unity Catalog metastores in your own Databricks account. Note that there is no need to use OpenSharing to share data between workspaces attached to the same Unity Catalog metastore, because in that scenario you can use Unity Catalog itself to manage access to data across workspaces.

One advantage of Databricks-to-Databricks sharing is that the share recipient doesn't need a token to access the share, and the provider doesn't need to manage recipient tokens. The security of the sharing connection—including all identity verification, authentication, and auditing—is managed entirely through OpenSharing and the Databricks platform. Another advantage is the ability to share Databricks notebook files, Unity Catalog volumes, and Unity Catalog models.

See also [What is the OpenSharing Databricks-to-Databricks protocol?](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks).

## How do provider admins set up OpenSharing?[​](#how-do-provider-admins-set-up-opensharing "Direct link to how-do-provider-admins-set-up-opensharing")

This section gives an overview of how providers can enable OpenSharing and initiate sharing from a Unity Catalog\-enabled Databricks workspace. For open-source OpenSharing, see [the open source project](https://go.delta.io/sharing).

Databricks-to-Databricks sharing between Unity Catalog metastores in the same account is always enabled. If you are a provider who wants to enable OpenSharing to share data with Databricks workspaces in other accounts or non-Databricks clients, a Databricks account admin or metastore admin performs the following setup steps (at a high level):

1.  Enable OpenSharing for the Unity Catalog metastore that manages the data you want to share.
    
    note
    
    You do not need to enable OpenSharing on your metastore if you intend to use OpenSharing to share data only with users on other Unity Catalog metastores in your account. Metastore-to-metastore sharing within a single Databricks account is enabled by default.
    
    See [Enable OpenSharing on a metastore](https://docs.databricks.com/aws/en/delta-sharing/set-up#enable).
    
2.  Create a share that includes data assets registered in the Unity Catalog metastore.
    
    If you are sharing with a non-Databricks recipient (known as Databricks-to-Open sharing) you can include tables in the Delta format. If you plan to use [Databricks-to-Databricks sharing](#d-to-d), you can also add views, Unity Catalog volumes, Unity Catalog models, and notebook files to a share.
    
    See [Create shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/create-share).
    
3.  Create a recipient.
    
    See [Create data recipients for OpenSharing (Databricks-to-Databricks sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient).
    
    If your recipient is not a Databricks user, or does not have access to a Databricks workspace that is enabled for Unity Catalog, you must use [Databricks-to-Open sharing](#open). You can either generate bearer-token-based credentials for that recipient or use OIDC federation.
    
    If your recipient has access to a Databricks workspace that is enabled for Unity Catalog, you can use [Databricks-to-Databricks sharing](#d-to-d), and no token-based credentials are required. You request a _sharing identifier_ from the recipient and use it to establish the secure connection.
    
    tip
    
    Use yourself as a test recipient to try out the setup process.
    
4.  Grant the recipient access to one or more shares.
    
    See [Manage access to OpenSharing data shares (for providers)](https://docs.databricks.com/aws/en/delta-sharing/grant-access).
    
5.  Send the recipient the information they need to connect to the share (Databricks-to-Open sharing only).
    
    For Databricks-to-Open sharing using bearer tokens, use a secure channel to send the recipient an activation link that allows them to download their token-based credentials. See [Send the recipient their connection information](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token#send).
    
    For Databricks-to-Open sharing using OIDC token federation, send the generated portal URL. See [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed).
    
    For Databricks-to-Databricks sharing, the data included in the share becomes available in the recipient's Databricks workspace as soon as you grant them access to the share.
    

The recipient can now access the shared data.

Recipients access shared data assets in read-only format. Shared notebook files are read-only, but they can be cloned and then modified and run in the recipient workspace just like any other notebook.

Secure access depends on the sharing model:

*   Databricks-to-Open sharing (recipient does not have a Databricks workspace enabled for Unity Catalog) has two options:
    
    *   In the bearer token flow, the recipient provides the credential whenever they access the data in their tool of choice, including Apache Spark, pandas, Power BI, Databricks, and many more. See [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open).
    *   In the OIDC token federation flow, the recipient or the recipient's client app accesses the data using their own identity provider (IdP). See [Read data shared using Open ID Connect (OIDC) federation in a U2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m) and [Read data shared using Open ID Connect (OIDC) federation in an M2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m).
*   Databricks-to-Databricks (recipient workspace is enabled for Unity Catalog): The recipient accesses the data using Databricks. They can use Unity Catalog to grant and deny access to other users in their Databricks account. See [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).
    

Whenever the data provider updates data tables or volumes in their own Databricks account, the updates appear in near real time in the recipient's system. To learn how to access data that has been shared with you using OpenSharing, see [Access data shared with you using OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/recipient).

Data providers on Unity Catalog\-enabled Databricks workspaces can use Databricks audit logging and system tables to monitor the creation and modification of shares and recipients, and can monitor recipient activity on shares. See [Audit and monitor data sharing](https://docs.databricks.com/aws/en/delta-sharing/audit-logs).

Data recipients who use shared data in a Databricks workspace can use Databricks audit logging and system tables to understand who is accessing which data. See [Audit and monitor data sharing](https://docs.databricks.com/aws/en/delta-sharing/audit-logs).

## Sharing volumes[​](#sharing-volumes "Direct link to Sharing volumes")

You can share volumes using the Databricks-to-Databricks sharing flow. See [Add volumes to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#volumes) (for providers) and [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks) (for recipients).

## Sharing models[​](#sharing-models "Direct link to Sharing models")

You can share models using the Databricks-to-Databricks sharing flow. See [Add models to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#models) (for providers) and [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks) (for recipients).

## Sharing notebooks[​](#sharing-notebooks "Direct link to Sharing notebooks")

You can use OpenSharing to share notebook files using the Databricks-to-Databricks sharing flow. See [Add notebook files to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-remove-notebook-files) (for providers) and [Read shared notebooks](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#preview-notebook-files) (for recipients).

## Restricting access at the row and column level when sharing views[​](#restricting-access-at-the-row-and-column-level-when-sharing-views "Direct link to Restricting access at the row and column level when sharing views")

You can share dynamic views that restrict access to certain table data based on recipient properties. See [Add dynamic views to a share to filter rows and columns](https://docs.databricks.com/aws/en/delta-sharing/create-share#dynamic-views).

## OpenSharing and streaming[​](#opensharing-and-streaming "Direct link to opensharing-and-streaming")

OpenSharing supports Apache Spark Structured Streaming. A provider can share a table with history or a streaming table so that a recipient can use it as a Structured Streaming source, processing shared data incrementally with low latency. Recipients can also perform [Delta Lake time travel queries](https://docs.databricks.com/aws/en/tables/history) on tables shared with history.

To learn how to share tables with history, see [Add tables to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-tables). To learn how to use shared tables as streaming sources, see [Query a table using Apache Spark Structured Streaming](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#streaming-source) (for recipients of Databricks-to-Databricks sharing) or [Access a shared table using Spark Structured Streaming](https://docs.databricks.com/aws/en/delta-sharing/read-data-open#streaming-source) (for recipients of Databricks-to-Open sharing data).

To learn how to share streaming tables, see [Add streaming tables to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#streaming-tables).

See also [Structured Streaming concepts](https://docs.databricks.com/aws/en/structured-streaming/concepts).

## Delta Lake feature support matrix[​](#delta-lake-feature-support-matrix "Direct link to delta-lake-feature-support-matrix")

OpenSharing supports most Delta Lake features when you share a table. This support matrix lists:

*   Delta features that require specific versions of Databricks Runtime, the open-source OpenSharing Spark connector, or the open-source OpenSharing Python connector.
*   Partially supported features.

## OpenSharing FAQs[​](#opensharing-faqs "Direct link to opensharing-faqs")

The following are frequently asked questions about OpenSharing.

### Do I need Unity Catalog to use OpenSharing?[​](#do-i-need-unity-catalog-to-use-opensharing "Direct link to do-i-need-unity-catalog-to-use-opensharing")

No, you do not need Unity Catalog to share (as a provider) or consume shared data (as a recipient). However, Unity Catalog provides benefits such as support for non-tabular and AI asset sharing, out-of-the-box governance, simplicity, and query performance.

Providers can share data in two ways:

*   Put the assets to share under Unity Catalog management and share them using the built-in Databricks OpenSharing server.
    
    You do not need to migrate all assets to Unity Catalog. You need only one Databricks workspace that is enabled for Unity Catalog to manage assets that you want to share. In some accounts, new workspaces are enabled for Unity Catalog automatically. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).
    
*   Implement the [Databricks-to-Open sharing server](https://go.delta.io/sharing) to share data, without necessarily using your Databricks account.
    

Recipients can consume data in two ways:

*   Without a Databricks workspace. Use open source OpenSharing connectors that are available for many data platforms, including Power BI, pandas, and open source Apache Spark. See [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open) and the [OpenSharing open source project](https://opensharing.io/).
    
*   In a Databricks workspace. Recipient workspaces don't need to be enabled for Unity Catalog, but there are advantages of governance, simplicity, and performance if they are.
    
    Recipient organizations who want these advantages don't need to migrate all assets to Unity Catalog. You need only one Databricks workspace that is enabled for Unity Catalog to manage assets that are shared with you. In some accounts, new workspaces are enabled for Unity Catalog automatically. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).
    

See [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open) and [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).

### Do I need to be a Databricks customer to use OpenSharing?[​](#do-i-need-to-be-a-databricks-customer-to-use-opensharing "Direct link to do-i-need-to-be-a-databricks-customer-to-use-opensharing")

No, OpenSharing is an open protocol. You can share non-Databricks data with recipients on any data platform. Providers can configure an open OpenSharing server to share from any computing platform. Recipients can consume shared data using open source OpenSharing connectors for many data products, including Power BI, pandas, and open source Spark.

However, using OpenSharing on Databricks, especially sharing from a Unity Catalog\-enabled workspace, has many advantages.

For details, see the first question in this FAQ.

### How do I incur and check OpenSharing costs?[​](#how-do-i-incur-and-check-opensharing-costs "Direct link to how-do-i-incur-and-check-opensharing-costs")

The cost of OpenSharing incurs when sharing and accessing views, materialized views, and streaming tables. These are the potential sources of cost for sharing:

*   Compute cost, charged by Databricks.

*   Storage and network transfer (egress) cost, charged by the storage vendor, or by Databricks if the provider uses [SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider#billing).

*   Foreign compute source cost, when sharing foreign schemas and tables.

The method by which compute is performed and who pays for it depends on several factors:

*   The type of recipient compute
*   Whether sharing occurs within the same Databricks account or across accounts

The following table describes the billing method for sharing and accessing _views_ using OpenSharing:

\* When you use OpenSharing with a recipient using Serverless compute in a different account, or with a recipient in the same account, there is no incremental charge. This means there is no additional cost for materializing the data asset.

When sharing _foreign tables_ (Beta), materialization is always performed and stored on the provider's side. For foreign Iceberg tables, materialization is performed on the provider's side when sharing with an open recipient not using an Iceberg client. Providers might see an additional charge attributed to default storage used for data materialization. There are no compute costs for foreign tables during Beta.

Billing attribution is also queryable using the [Billable usage system table reference](https://docs.databricks.com/aws/en/admin/system-tables/billing) and [OpenSharing materialization history system table reference](https://docs.databricks.com/aws/en/admin/system-tables/materialization). If the recipient pays for attribution, then only the recipient can see the associated record in the system table. For example queries, see [Sample queries](https://docs.databricks.com/aws/en/admin/system-tables/materialization#sample-queries).

### Does OpenSharing incur egress costs?[​](#does-opensharing-incur-egress-costs "Direct link to does-opensharing-incur-egress-costs")

OpenSharing within a region incurs no egress cost. Unlike other data sharing platforms, OpenSharing does not require data replication. This model has many advantages, but it means that your cloud vendor may charge data egress fees when you share data across clouds or regions. Databricks supports sharing from Cloudflare R2, which incurs no egress fees, and provides other tools and recommendations to monitor and avoid egress fees. See [Monitor and manage OpenSharing egress costs (for providers)](https://docs.databricks.com/aws/en/delta-sharing/manage-egress).

However, if the provider uses [SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider#billing), data transfer is billed by Databricks instead of the cloud vendor.

### Do recipients have direct access to the underlying data in shared views, materialized views, and streaming tables?[​](#do-recipients-have-direct-access-to-the-underlying-data-in-shared-views-materialized-views-and-streaming-tables "Direct link to do-recipients-have-direct-access-to-the-underlying-data-in-shared-views-materialized-views-and-streaming-tables")

For shared views, materialized views, and streaming tables, the data recipient has direct access if one of the following is true:

*   The recipient uses serverless compute or non-dedicated classic compute on the same Databricks account.
*   The recipient uses serverless compute on a different Databricks account.

Otherwise, data is materialized and filtered on the provider side.

The data materialization is stored under the shared data asset's parent storage location.

When sharing materialized assets, the compute processes the request by applying necessary filters and creating temporary materialization cached in the provider's storage. This filtered data is delivered to recipients using pre-signed short-lived URLs, ensuring secure access while maintaining provider-to-recipient access control.

### Can providers revoke recipient access?[​](#can-providers-revoke-recipient-access "Direct link to Can providers revoke recipient access?")

Yes, recipient access can be revoked on-demand and at specified levels of granularity. You can deny recipient access to specific shares and specific IP addresses, filter tabular data for a recipient, revoke recipient tokens, and delete recipients entirely. See [Revoke recipient access to a share](https://docs.databricks.com/aws/en/delta-sharing/grant-access#revoke) and [Create data recipients for OpenSharing (Databricks-to-Databricks sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient).

### Isn't it insecure to use pre-signed URLs?[​](#isnt-it-insecure-to-use-pre-signed-urls "Direct link to Isn't it insecure to use pre-signed URLs?")

OpenSharing uses pre-signed URLs to provide temporary access to a file in object storage. They are only given to recipients that already have access to the shared data. They are secure because they are short-lived and don't expand the level of access beyond what recipients have already been granted.

### Are the tokens used in the OpenSharing Databricks-to-Open sharing protocol secure?[​](#are-the-tokens-used-in-the-opensharing-databricks-to-open-sharing-protocol-secure "Direct link to are-the-tokens-used-in-the-opensharing-databricks-to-open-sharing-protocol-secure")

Because OpenSharing enables cross-platform sharing—unlike other available data sharing platforms—the sharing protocol requires an open token. Providers can ensure token security by configuring the token lifetime, setting networking controls, and revoking access on demand. In addition, the token does not expand the level of access beyond what recipients have already been granted. See [Security considerations for tokens](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token#security-considerations).

If you prefer not to use tokens to manage access to recipient shares, you should use [Databricks-to-Databricks sharing](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks) or contact your Databricks account team for alternatives.

### What is the difference between Lakeflow Connect and OpenSharing?[​](#what-is-the-difference-between-lakeflow-connect-and-opensharing "Direct link to what-is-the-difference-between-lakeflow-connect-and-opensharing")

OpenSharing allows you to securely share live data across platforms, clouds, and regions. Databricks recommends ingestion using managed connectors because they scale to accommodate high data volumes, low-latency querying, and third-party API limits. However, you might want to query your data without moving it.

When you have a choice between managed connectors and OpenSharing, choose OpenSharing for the following scenarios:

*   Limiting data duplication.
*   Querying the freshest possible data.

## Limitations[​](#limitations "Direct link to limitations")

### Table format and feature support[​](#table-format-and-feature-support "Direct link to Table format and feature support")

**Format requirements:**

*   Tabular data must be in [Delta](https://docs.databricks.com/aws/en/delta/) or [managed Iceberg](https://docs.databricks.com/aws/en/tables/managed) table format. You can easily convert Parquet tables to Delta—and back again. See [CONVERT TO DELTA](https://docs.databricks.com/aws/en/sql/language-manual/delta-convert-to-delta).
*   OpenSharing can only read UniForm tables as Delta tables.

**Unsupported tables:**

*   Providers can't share tables that use liquid clustering with partition filtering.
*   Providers can't share R2 tables with V2 checkpoint.
*   Providers can't share tables with collations enabled.
*   Providers can't share tables with row filters or column masks.
*   Providers can't share `SHALLOW CLONE` tables. Databricks does not support presigning URLs for Delta logs that reference absolute paths.
*   Providers can't share [managed Iceberg tables](https://docs.databricks.com/aws/en/tables/managed) to external Iceberg clients. See [Add managed Iceberg tables to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#managed-iceberg) and [Enable sharing to external Iceberg clients](https://docs.databricks.com/aws/en/delta-sharing/create-share#iceberg-clients).
*   [Foreign key constraints](https://docs.databricks.com/aws/en/tables/constraints) are not available in shared tables.

### Databricks-to-Databricks sharing only[​](#databricks-to-databricks-sharing-only "Direct link to Databricks-to-Databricks sharing only")

The following assets can only be shared using the Databricks-to-Databricks sharing flow:

*   Notebook sharing. See [Add notebook files to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-remove-notebook-files) and [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).
*   Volume sharing. See [Add volumes to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#volumes) (for providers) and [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).
*   Model sharing. See [Add models to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#models) (for providers) and [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).

### Views[​](#views "Direct link to Views")

*   Shareable views must be defined on Delta tables or other shareable views. See [Add views to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#views) (for providers) and [Read shared views](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#views) (for recipients).

### Streaming[​](#streaming "Direct link to Streaming")

*   OpenSharing doesn't support changing `responseFormat` while a streaming source is running or during streaming restarts.

### Recipient metadata[​](#recipient-metadata "Direct link to Recipient metadata")

*   The tables in `information_schema` from a shared catalog reflect metadata stored in Unity Catalog. This metadata is updated from the provider only when you query the shared table directly or run a command such as [DESCRIBE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-describe-table) or [REFRESH FOREIGN](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-refresh-foreign). Until then, `information_schema` might appear stale compared to the provider's data.

### Resource and technical limits[​](#resource-and-technical-limits "Direct link to Resource and technical limits")

*   There are limits on the number of files in metadata allowed for a shared table. To learn more, see [Resource limit exceeded errors](https://docs.databricks.com/aws/en/delta-sharing/troubleshooting#resource-limits).
*   Schemas named `information_schema` cannot be imported into a Unity Catalog metastore, because that schema name is reserved in Unity Catalog.

See also [Delta Lake feature support matrix](#delta-matrix).

Deleting a parent object, such as a catalog or schema, triggers a cascade delete of its child objects, even if those child objects are included in active shares. After a cascade delete removes an asset, you can't re-add an asset with the same name to the share.

To avoid this issue, remove assets from all shares before you delete their parent objects.

## Resource quotas[​](#resource-quotas "Direct link to resource-quotas")

Databricks enforces resource quotas on all OpenSharing securable objects. These quotas are listed in [Resource limits](https://docs.databricks.com/aws/en/resources/limits). If you expect to exceed these resource limits, contact your Databricks account team.

You can monitor your quota usage using the Unity Catalog resource quotas APIs. See [Monitor your usage of Unity Catalog resource quotas](https://docs.databricks.com/aws/en/resources/manage-resource-quotas).

## Next steps[​](#next-steps "Direct link to next-steps")

*   [Enable your Databricks account for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/set-up)
*   [Create shares](https://docs.databricks.com/aws/en/delta-sharing/create-share)
*   [Create recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient)
*   Learn more about the [Databricks-to-Open sharing](https://docs.databricks.com/aws/en/delta-sharing/share-data-open) and [Databricks-to-Databricks](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks) sharing models
*   [Learn how recipients access shared data](https://docs.databricks.com/aws/en/delta-sharing/recipient)
