---
title: Workspace Model Registry webhooks | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/model-registry-webhooks
ingestedAt: "2026-06-18T08:14:11.757Z"
---

Webhooks enable you to listen for Workspace Model Registry events so your integrations can automatically trigger actions. You can use webhooks to automate and integrate your machine learning pipeline with existing CI/CD tools and workflows. For example, you can trigger CI builds when a new model version is created or notify your team members through Slack each time a model transition to production is requested.

Webhooks are available through the [Databricks REST API](https://docs.databricks.com/api/workspace/experiments) or the Python client `databricks-registry-webhooks` on [PyPI](https://pypi.org/project/databricks-registry-webhooks/).

## Webhook events[​](#webhook-events "Direct link to Webhook events")

You can specify a webhook to trigger upon one or more of these events:

*   **MODEL\_VERSION\_CREATED**: A new model version was created for the associated model.
*   **MODEL\_VERSION\_TRANSITIONED\_STAGE**: A model version's stage was changed.
*   **TRANSITION\_REQUEST\_CREATED**: A user requested a model version's stage be transitioned.
*   **COMMENT\_CREATED**: A user wrote a comment on a registered model.
*   **REGISTERED\_MODEL\_CREATED**: A new registered model was created. This event type can only be specified for a registry-wide webhook, which can be created by not specifying a model name in the create request.
*   **MODEL\_VERSION\_TAG\_SET**: A user set a tag on the model version.
*   **MODEL\_VERSION\_TRANSITIONED\_TO\_STAGING**: A model version was transitioned to staging.
*   **MODEL\_VERSION\_TRANSITIONED\_TO\_PRODUCTION**: A model version was transitioned to production.
*   **MODEL\_VERSION\_TRANSITIONED\_TO\_ARCHIVED**: A model version was archived.
*   **TRANSITION\_REQUEST\_TO\_STAGING\_CREATED**: A user requested a model version be transitioned to staging.
*   **TRANSITION\_REQUEST\_TO\_PRODUCTION\_CREATED**: A user requested a model version be transitioned to production.
*   **TRANSITION\_REQUEST\_TO\_ARCHIVED\_CREATED**: A user requested a model version be archived.

## Types of webhooks[​](#types-of-webhooks "Direct link to Types of webhooks")

There are two types of webhooks based on their trigger targets:

*   **Webhooks with HTTP endpoints (HTTP registry webhooks)**: Send triggers to an HTTP endpoint.
*   **Webhooks with job triggers (job registry webhooks)**: Trigger a job in a Databricks workspace. If IP allowlisting is enabled in the job's workspace, you must allowlist the workspace IPs of the model registry. See [IP allowlisting for job registry webhooks](#ip-allowlisting) for more information.

There are also two types of webhooks based on their scope, with different access control requirements:

*   **Model-specific webhooks**: The webhook applies to a specific registered model. You must have CAN MANAGE permissions on the registered model to create, modify, delete, or test model-specific webhooks.
*   **Registry-wide webhooks**: The webhook is triggered by events on any registered model in the workspace, including the creation of a new registered model. To create a registry-wide webhook, omit the `model_name` field on creation. You must have workspace admin permissions to create, modify, delete, or test registry-wide webhooks.

## Webhook payload[​](#webhook-payload "Direct link to Webhook payload")

Each event trigger has minimal fields included in the payload for the outgoing request to the webhook endpoint.

*   Sensitive information like artifact path location is excluded. Users and principals with appropriate ACLs can use client or REST APIs to query the Model Registry for this information.
*   Payloads are not encrypted. See [Security](#security) for information on how to validate that Databricks is the source of the webhook.
*   The `text` field facilitates Slack integration. To send a Slack message, provide a Slack webhook endpoint as the webhook URL.

### Job registry webhook payload[​](#job-registry-webhook-payload "Direct link to Job registry webhook payload")

The payload for a job registry webhook depends on the type of job and is sent to the `jobs/run-now` endpoint in the target workspace.

#### Single-task jobs[​](#single-task-jobs "Direct link to Single-task jobs")

Single-task jobs have one of three payloads based on the task type.

##### Notebook and Python wheel jobs[​](#notebook-and-python-wheel-jobs "Direct link to Notebook and Python wheel jobs")

Notebook and Python wheel jobs have a JSON payload with a parameter dictionary that contains a field `event_message`.

JSON

    {  "job_id": 1234567890,  "notebook_params": {    "event_message": "<Webhook Payload>"  }}

##### Python, JAR, and Spark Submit jobs[​](#python-jar-and-spark-submit-jobs "Direct link to Python, JAR, and Spark Submit jobs")

Python, JAR, and Spark submit jobs have a JSON payload with a parameter list.

JSON

    {  "job_id": 1234567890,  "python_params": ["<Webhook Payload>"]}

##### All other jobs[​](#all-other-jobs "Direct link to All other jobs")

All other types of jobs have a JSON payload with no parameters.

#### Multi-task jobs[​](#multi-task-jobs "Direct link to Multi-task jobs")

Multi-task jobs have a JSON payload with all parameters populated to account for different task types.

JSON

    {  "job_id": 1234567890,  "notebook_params": {    "event_message": "<Webhook Payload>"  },  "python_named_params": {    "event_message": "<Webhook Payload>"  },  "jar_params": ["<Webhook Payload>"],  "python_params": ["<Webhook Payload>"],  "spark_submit_params": ["<Webhook Payload>"]}

### Example payloads[​](#example-payloads "Direct link to Example payloads")

#### event: `MODEL_VERSION_TRANSITIONED_STAGE`[​](#event-model_version_transitioned_stage "Direct link to event-model_version_transitioned_stage")

**Response**

    POST/your/endpoint/for/event/model-versions/stage-transition--data {  "event": "MODEL_VERSION_TRANSITIONED_STAGE",  "webhook_id": "c5596721253c4b429368cf6f4341b88a",  "event_timestamp": 1589859029343,  "model_name": "Airline_Delay_SparkML",  "version": "8",  "to_stage": "Production",  "from_stage": "None",  "text": "Registered model 'someModel' version 8 transitioned from None to Production."}

#### event: `MODEL_VERSION_TAG_SET`[​](#event-model_version_tag_set "Direct link to event-model_version_tag_set")

**Response**

    POST/your/endpoint/for/event/model-versions/tag-set--data {  "event": "MODEL_VERSION_TAG_SET",  "webhook_id": "8d7fc634e624474f9bbfde960fdf354c",  "event_timestamp": 1589859029343,  "model_name": "Airline_Delay_SparkML",  "version": "8",  "tags": [{"key":"key1","value":"value1"},{"key":"key2","value":"value2"}],  "text": "example@example.com set version tag(s) 'key1' => 'value1', 'key2' => 'value2' for registered model 'someModel' version 8."}

**Response**

    POST/your/endpoint/for/event/comments/create--data {  "event": "COMMENT_CREATED",  "webhook_id": "8d7fc634e624474f9bbfde960fdf354c",  "event_timestamp": 1589859029343,  "model_name": "Airline_Delay_SparkML",  "version": "8",  "comment": "Raw text content of the comment",  "text": "A user commented on registered model 'someModel' version 8."}

## Security[​](#security "Direct link to Security")

For security, Databricks includes the X-Databricks-Signature in the header computed from the payload and the shared secret key associated with the webhook using the [HMAC with SHA-256 algorithm](https://en.wikipedia.org/wiki/HMAC).

In addition, you can include a standard Authorization header in the outgoing request by specifying one in the `HttpUrlSpec` of the webhook.

### Client verification[​](#client-verification "Direct link to Client verification")

If a shared secret is set, the payload recipient should verify the source of the HTTP request by using the shared secret to HMAC-encode the payload, and then comparing the encoded value with the `X-Databricks-Signature` from the header. This is particularly important if SSL certificate validation is disabled (that is, if the `enable_ssl_verification` field is set to `false`).

note

`enable_ssl_verification` is `true` by default. For self-signed certificates, this field must be `false`, and the destination server must disable certificate validation.

For security purposes, Databricks recommends that you perform secret validation with the HMAC-encoded portion of the payload. If you disable host name validation, you increase the risk that a request could be maliciously routed to an unintended host.

Python

    import hmacimport hashlibimport jsonsecret = shared_secret.encode('utf-8')signature_key = 'X-Databricks-Signature'def validate_signature(request):  if not request.headers.has_key(signature_key):    raise Exception('No X-Signature. Webhook not be trusted.')  x_sig = request.headers.get(signature_key)  body = request.body.encode('utf-8')  h = hmac.new(secret, body, hashlib.sha256)  computed_sig = h.hexdigest()  if not hmac.compare_digest(computed_sig, x_sig.encode()):    raise Exception('X-Signature mismatch. Webhook not be trusted.')

If an Authorization header is set, clients should verify the source of the HTTP request by verifying the bearer token or authorization credentials in the Authorization header.

### IP allowlisting for job registry webhooks[​](#ip-allowlisting-for-job-registry-webhooks "Direct link to ip-allowlisting-for-job-registry-webhooks")

To use a webhook that triggers job runs in a different workspace that has IP allowlisting enabled, you must [allowlist](https://docs.databricks.com/aws/en/security/network/front-end/ip-access-list-workspace) the region NAT IP where the webhook is located to accept incoming requests.

If the webhook and the job are in the same workspace, you do not need to add any IPs to your allowlist.

Contact your accounts team to identify the IPs you need to allowlist.

## Audit logging[​](#audit-logging "Direct link to Audit logging")

If audit logging is enabled for your workspace, the following events are included in the audit logs:

*   Create webhook
*   Update webhook
*   List webhook
*   Delete webhook
*   Test webhook
*   Webhook trigger

### Webhook trigger audit logging[​](#webhook-trigger-audit-logging "Direct link to Webhook trigger audit logging")

For webhooks with HTTP endpoints, the HTTP request sent to the URL specified for the webhook along with the URL and `enable_ssl_verification` values are logged.

For webhooks with job triggers, the `job_id` and `workspace_url` values are logged.

## Examples[​](#examples "Direct link to Examples")

This section includes:

*   [HTTP registry webhook workflow example](#http-registry-webhook-example-workflow).
*   [job registry webhook workflow example](#job-registry-webhook-example-workflow).
*   [list webhooks example](#list-registry-webhooks-example).
*   two [example notebooks](#notebooks): one illustrating the REST API, and one illustrating the Python client.

### HTTP registry webhook example workflow[​](#http-registry-webhook-example-workflow "Direct link to HTTP registry webhook example workflow")

#### 1\. Create a webhook[​](#1-create-a-webhook "Direct link to 1. Create a webhook")

When an HTTPS endpoint is ready to receive the webhook event request, you can create a webhook using the webhooks Databricks REST API. For example, the webhook's URL can point to Slack to post messages to a channel.

Bash

    $ curl -X POST -H "Authorization: Bearer <access-token>" -d \'{"model_name": "<model-name>",  "events": ["MODEL_VERSION_CREATED"],  "description": "Slack notifications",  "status": "TEST_MODE",  "http_url_spec": {    "url": "https://hooks.slack.com/services/...",    "secret": "anyRandomString"    "authorization": "Bearer AbcdEfg1294"}}' https://<databricks-instance>/api/2.0/mlflow/registry-webhooks/create

Python

    from databricks_registry_webhooks import RegistryWebhooksClient, HttpUrlSpechttp_url_spec = HttpUrlSpec(  url="https://hooks.slack.com/services/...",  secret="secret_string",  authorization="Bearer AbcdEfg1294")http_webhook = RegistryWebhooksClient().create_webhook(  model_name="<model-name>",  events=["MODEL_VERSION_CREATED"],  http_url_spec=http_url_spec,  description="Slack notifications",  status="TEST_MODE")

**Response**

    {"webhook": {   "id":"1234567890",   "creation_timestamp":1571440826026,   "last_updated_timestamp":1582768296651,   "status":"TEST_MODE",   "events":["MODEL_VERSION_CREATED"],   "http_url_spec": {     "url": "https://hooks.slack.com/services/...",     "enable_ssl_verification": True}}}

You can also create an HTTP registry webhook with the [Databricks Terraform provider](https://docs.databricks.com/aws/en/dev-tools/terraform/) and [databricks\_mlflow\_webhook](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/mlflow_webhook).

#### 2\. Test the webhook[​](#2-test-the-webhook "Direct link to 2. Test the webhook")

The previous webhook was created in `TEST_MODE`, so a mock event can be triggered to send a request to the specified URL. However, the webhook does not trigger on a real event. The test endpoint returns the received status code and body from the specified URL.

Bash

    $ curl -X POST -H "Authorization: Bearer <access-token>" -d \'{"id": "1234567890"}' \https://<databricks-instance>/api/2.0/mlflow/registry-webhooks/test

Python

    from databricks_registry_webhooks import RegistryWebhooksClienthttp_webhook = RegistryWebhooksClient().test_webhook(  id="1234567890")

**Response**

    { "status":200, "body":"OK"}

#### 3\. Update the webhook to active status[​](#3-update-the-webhook-to-active-status "Direct link to 3. Update the webhook to active status")

To enable the webhook for real events, set its status to `ACTIVE` through an update call, which can also be used to change any of its other properties.

Bash

    $ curl -X PATCH -H "Authorization: Bearer <access-token>" -d \'{"id": "1234567890", "status": "ACTIVE"}' \https://<databricks-instance>/api/2.0/mlflow/registry-webhooks/update

Python

    from databricks_registry_webhooks import RegistryWebhooksClienthttp_webhook = RegistryWebhooksClient().update_webhook(  id="1234567890",  status="ACTIVE")

**Response**

    {"webhook": {   "id":"1234567890",   "creation_timestamp":1571440826026,   "last_updated_timestamp":1582768296651,   "status": "ACTIVE",   "events":["MODEL_VERSION_CREATED"],   "http_url_spec": {     "url": "https://hooks.slack.com/services/...",     "enable_ssl_verification": True}}}

#### 4\. Delete the webhook[​](#4-delete-the-webhook "Direct link to 4. Delete the webhook")

To disable the webhook, set its status to `DISABLED` (using a similar update command as above), or delete it.

Bash

    $ curl -X DELETE -H "Authorization: Bearer <access-token>" -d \'{"id": "1234567890"}' \https://<databricks-instance>/api/2.0/mlflow/registry-webhooks/delete

Python

    from databricks_registry_webhooks import RegistryWebhooksClienthttp_webhook = RegistryWebhooksClient().delete_webhook(  id="1234567890")

**Response**

### Job registry webhook example workflow[​](#job-registry-webhook-example-workflow "Direct link to Job registry webhook example workflow")

The workflow for managing job registry webhooks is similar to HTTP registry webhooks, with the only difference being the `job_spec` field that replaces the `http_url_spec` field.

With webhooks, you can trigger jobs in the same workspace or in a different workspace. The workspace is specified using the optional parameter `workspace_url`. If no `workspace_url` is present, the default behavior is to trigger a job in the same workspace as the webhook.

#### Requirements[​](#requirements "Direct link to Requirements")

*   An existing [job](https://docs.databricks.com/aws/en/jobs/).
*   A [personal access token](https://docs.databricks.com/api/workspace/tokenmanagement). Note that access tokens can only be read by the MLflow service and cannot be returned by Databricks users in the Model Registry API.

note

As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use [OAuth tokens](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m).

If you use personal access token authentication, Databricks recommends using personal access tokens belonging to [service principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals#tokens).

#### Create a job registry webhook[​](#create-a-job-registry-webhook "Direct link to Create a job registry webhook")

Bash

    $ curl -X POST -H "Authorization: Bearer <access-token>" -d \ '{"model_name": "<model-name>",  "events": ["TRANSITION_REQUEST_CREATED"],  "description": "Job webhook trigger",  "status": "TEST_MODE",  "job_spec": {    "job_id": "1",    "workspace_url": "https://my-databricks-workspace.com",    "access_token": "dapi12345..."}}'https://<databricks-instance>/api/2.0/mlflow/registry-webhooks/create

Python

    from databricks_registry_webhooks import RegistryWebhooksClient, JobSpecjob_spec = JobSpec(  job_id="1",  workspace_url="https://my-databricks-workspace.com",  access_token="dapi12345...")job_webhook = RegistryWebhooksClient().create_webhook(  model_name="<model-name>",  events=["TRANSITION_REQUEST_CREATED"],  job_spec=job_spec,  description="Job webhook trigger",  status="TEST_MODE")

**Response**

    {"webhook": {   "id":"1234567891",   "creation_timestamp":1591440826026,   "last_updated_timestamp":1591440826026,   "status":"TEST_MODE",   "events":["TRANSITION_REQUEST_CREATED"],   "job_spec": {     "job_id": "1",     "workspace_url": "https://my-databricks-workspace.com"}}}

You can also create a job registry webhook with the [Databricks Terraform provider](https://docs.databricks.com/aws/en/dev-tools/terraform/) and [databricks\_mlflow\_webhook](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/mlflow_webhook).

### List registry webhooks example[​](#list-registry-webhooks-example "Direct link to List registry webhooks example")

Bash

    $ curl -X GET -H "Authorization: Bearer <access-token>" -d \ '{"model_name": "<model-name>"}'https://<databricks-instance>/api/2.0/mlflow/registry-webhooks/list

Python

    from databricks_registry_webhooks import RegistryWebhooksClientwebhooks_list = RegistryWebhooksClient().list_webhooks(model_name="<model-name>")

**Response**

    {"webhooks": [{   "id":"1234567890",   "creation_timestamp":1571440826026,   "last_updated_timestamp":1582768296651,   "status": "ACTIVE",   "events":["MODEL_VERSION_CREATED"],   "http_url_spec": {     "url": "https://hooks.slack.com/services/...",     "enable_ssl_verification": True}},{   "id":"1234567891",   "creation_timestamp":1591440826026,   "last_updated_timestamp":1591440826026,   "status":"TEST_MODE",   "events":["TRANSITION_REQUEST_CREATED"],   "job_spec": {     "job_id": "1",     "workspace_url": "https://my-databricks-workspace.com"}}]}

### Notebooks[​](#notebooks "Direct link to Notebooks")

#### MLflow Model Registry webhooks REST API example notebook

#### MLflow Model Registry webhooks Python client example notebook
