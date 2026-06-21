---
title: Read data shared using Open ID Connect (OIDC) federation in an M2M flow | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m
ingestedAt: "2026-06-18T08:06:00.336Z"
---

This page describes how data recipients can use a Python client registered in their own identity provider (IdP) to establish access to OpenSharing shares created in Databricks.

This "machine-to-machine" (M2M) OAuth Client Credentials grant flow is typically used in scenarios where an application, such as a nightly job running on a virtual machine, accesses data autonomously. This authentication flow uses OIDC federation. The recipient's IdP issues JSON Web Tokens (JWTs) that serve as short-lived OAuth tokens, which Databricks authenticates. This [Databricks-to-open sharing](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks) authentication flow is for recipients who do not have access to a Unity Catalog\-enabled Databricks workspace.

Open OIDC federation is an alternative to using long-lived Databricks-issued bearer tokens to connect non-Databricks recipients to providers. In the OAuth Client Credentials grant flow, an OAuth application is registered as a Service Principal (SP) in the recipient's IdP. No long-lived secrets or credentials are shared between Databricks, the provider, and the recipient. For information about using bearer tokens to manage authentication to shares instead, see [Create a recipient object for non-Databricks users using bearer tokens (Databricks-to-Open sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token).

This page is intended for recipients. For information about how providers can enable OIDC federation for recipients in Databricks, see [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed).

For information about the "user-to-machine" (U2M) flow, see [Read data shared using Open ID Connect (OIDC) federation in a U2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m).

## Register an app in your IdP[​](#register-an-app-in-your-idp "Direct link to Register an app in your IdP")

Before you can use OIDC federation to give your client application access to OpenSharing shares, you must register an OAuth application in your IdP. This section describes how to register an OAuth application in Microsoft Entra ID. For other IdPs, see their documentation.

### Register an app in Microsoft Entra ID[​](#register-an-app-in-microsoft-entra-id "Direct link to Register an app in Microsoft Entra ID")

These instructions are intended as general guidance and are not guaranteed to be kept up-to-date. For detailed app registration instructions, see this [Microsoft quickstart](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app).

1.  Sign in to the Microsoft Entra admin center as at least an Application Developer.
2.  Go to **App registrations** and create a new registration without a redirect URL.
3.  Go to **Certificates & Secrets > Create a secret** for your app.
4.  Copy the secret value and store it securely.
5.  On the **App registrations > Overview** page for the app, copy the **Application (client) ID**
6.  Modify the app to be a V2 application by updating the manifest:
    1.  In the app's **Manage** section, select **Manifest**.
    2.  In the editor, set `accessTokenAcceptedVersion` to `2`.
    3.  Save the changes.

### Send required information to the Databricks data provider[​](#send-required-information-to-the-databricks-data-provider "Direct link to send-required-information-to-the-databricks-data-provider")

If you, as a recipient, use Microsoft Entra ID, you can get the fields required by the provider by following these instructions. Always refer to Microsoft Entra ID documentation for the most up-to-date instructions.

*   **Issuer URL**: `https://login.microsoftonline.com/{tenantId}/v2.0`, replacing `{tenantId}` with your Entra tenant ID. If you don't know your tenant ID, see the [Microsoft Entra ID documentation](https://learn.microsoft.com/entra/fundamentals/how-to-find-tenant).
    
*   **Subject Claim**: Refers to the field in the JWT payload that identifies the entity accessing the data. The specific field used depends on your Identity Provider (IdP) and use cases. For example, for M2M applications in Microsoft Entra ID, the subject claim is `azp`, which represents the client ID of the application authorized to use the token. For more details, see the [Microsoft Entra ID Access token claims reference](https://learn.microsoft.com/en-us/entra/identity-platform/access-token-claims-reference)
    
*   **Subject**: Refers to the unique identifier of the registered OAuth application in the recipient's Identity Provider (IdP).  
    For example, in Microsoft Entra ID, this is the **Application (client) ID**. If you did not copy the client ID during registration, you can retrieve it by following the steps specific to your IdP. For Microsoft Entra ID, follow these steps:
    
    1.  Navigate to **App registrations** in the Microsoft Entra admin center.
    2.  Select your registered OAuth application.
    3.  Locate the **Application (client) ID** on the Overview page.
    
    For other IdPs, refer to their documentation to retrieve the equivalent identifier.
    
*   **Audience**: For machine-to-Databricks authentication, typically you use the resource's `clientId`, but you can specify any other valid resource identifier.
    
    You should have copied this in the previous step. If not, navigate to the Microsoft Entra admin center, search for **App registrations**, select your registered application, and then locate the **Application (client) ID** on the Overview page. You could also use a different resource ID.
    

Share issuer, subject claim, subject, and audience with the provider.

### Configure your app to use the OAuth profile file shared by the Databricks provider[​](#configure-your-app-to-use-the-oauth-profile-file-shared-by-the-databricks-provider "Direct link to Configure your app to use the OAuth profile file shared by the Databricks provider")

To configure your app to access OpenSharing shares from the provider:

1.  Go to the OIDC profile portal URL that the Databricks provider shared with you.
    
    Request the URL if you haven't yet received it.
    
2.  On the portal page, select the **M2M** tile and, under **For OAuth**, click **Download file**.
    
3.  Modify the downloaded `oauth_config.share` JSON file to add your `clientId`, `clientSecret`, and `scope`.
    
    You should have copied the client ID and client secret when you registered your app. You cannot retrieve the client secret again. To retrieve the client ID, see the instructions in the previous section.
    
    If you choose to use the app's `{clientId}` as the audience, the scope should be `{clientId}/.default`. For example, if the audience is `61a80fb9-ce0c-4794-9f7f-2ba42a7b76f6`, the scope should be `61a80fb9-ce0c-4794-9f7f-2ba42a7b76f6/.default`.
    
    Sample profile:
    
    JSON
    
        {  "shareCredentialsVersion": 2,  "endpoint": "https://oregon.cloud.databricks.com/api/2.0/delta-sharing/metastores/11a11aaa-11aa-11a12-11aa-111a1aa11111/recipients/a11da11aa1-a1a1-11a1-a11a-1111a11111aa",  "tokenEndpoint": "https://login.microsoftonline.com/a111a111-1111-1aaa-1aa1-1aa1111aa1/oauth2/v2.0/token",  "type": "oauth_client_credentials",  "clientId": "[REPLACE_WITH_YOUR_CLIENT_ID]",  "clientSecret": "[REPLACE_WITH_YOUR_CLIENT_SECRET]",  "scope": "[REPLACE_WITH_YOUR_SCOPE]"}
    
4.  Install and configure the latest OpenSharing Python OSS client.
    
    You must have the latest version of the OpenSharing Python OSS client.
    
    Bash
    
        python3 -m venv .venvsource .venv/bin/activatepip3 install "delta-sharing>=1.3.1"
    
5.  Save the updated `oauth_config.share` file.
    
6.  Test the configuration:
    
    Create a test script, `test.py`:
    
    Python
    
        import delta_sharing# Point to the profile file. It can be a file on the local file system or a file on a remote storage. profile_file = "oauth_config.share" # Create a SharingClient. client = delta_sharing.SharingClient(profile_file) # # List all shared tables. tables = client.list_all_tables() print(tables) # replace the following line with the coordinates of the shared table #table_url = profile_file + "#sample_share.sample_db.sample_table" # Fetch 10 rows from a table and convert it to a Pandas DataFrame. # This can be used to read sample data from a table that cannot fit in the memory. #df = delta_sharing.load_as_pandas(table_url, limit=10) #print(df)
    
    Run the script:
    
    The script should list the shared tables.
