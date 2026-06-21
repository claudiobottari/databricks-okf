---
title: Model Serving limits and regions | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits
ingestedAt: "2026-06-18T08:12:13.523Z"
---

This article summarizes the limitations and region availability for Databricks Model Serving and supported endpoint types.

## Resource and payload limits[​](#resource-and-payload-limits "Direct link to Resource and payload limits")

Model Serving imposes default limits to ensure reliable performance. If you have feedback on these limits, reach out to your Databricks account team.

The limits in this section apply to custom model and [AI agent](https://docs.databricks.com/aws/en/generative-ai/agent-framework/deploy-agent) endpoints only. For Foundation Model APIs and external model resource and payload limits, see [Foundation Model APIs rate limits and quotas](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits).

### Custom models and AI agents[​](#custom-models-and-ai-agents "Direct link to Custom models and AI agents")

## Networking and security limitations[​](#networking-and-security-limitations "Direct link to Networking and security limitations")

*   Model Serving endpoints are protected by [access control](https://docs.databricks.com/aws/en/security/auth/access-control/#serving-endpoints) and respect networking-related ingress rules configured on the workspace, like IP allowlists and [PrivateLink](https://docs.databricks.com/aws/en/security/network/classic/privatelink).
*   By default, Model Serving does not support PrivateLink to external endpoints. Support for this functionality is evaluated and implemented on a per-region basis. Reach out to your Databricks account team for more information.
*   Model Serving does not provide security patches to existing model images because of the risk of destabilization to production deployments. A new model image created from a new model version will contain the latest patches. Reach out to your Databricks account team for more information.
*   You can restrict outbound network access from Model Serving endpoints by configuring network policies. See [Manage network policies for serverless egress control](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies).

### Compliance security profile standards: CPU and GPU workloads[​](#-compliance-security-profile-standards-cpu-and-gpu-workloads "Direct link to -compliance-security-profile-standards-cpu-and-gpu-workloads")

The following table lists the region availability and supported compliance security profile compliance standards for model serving on CPU and GPU workloads including external models.

note

These compliance standards require served containers to be built in the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. However, if this automated job fails, an event log message like the following appears and provides guidance on how to ensure your endpoints stay within compliance requirements:

`"Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."`

### Compliance security profile standards: Foundation Model APIs workloads[​](#compliance-security-profile-standards-foundation-model-apis-workloads "Direct link to compliance-security-profile-standards-foundation-model-apis-workloads")

The table lists the supported compliance security profile compliance standards for the following Foundation Model APIs workloads:

*   Provisioned throughput
*   Pay-per-token
*   Batch inference using AI Functions and Databricks-hosted models

note

These compliance standards require served containers to be built in the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. However, if this automated job fails, an event log message like the following appears and provides guidance on how to ensure your endpoints stay within compliance requirements:

`"Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."`

\* Some models require [cross geography routing](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing) for provisioned throughput and therefore are not UK Cyber Essentials Plus compliant. Reach out to your Databricks account team for more information.

## Foundation Model APIs limits[​](#foundation-model-apis-limits "Direct link to foundation-model-apis-limits")

For detailed information about Foundation Model APIs, including resource and payload limits for foundation and external models, see [Foundation Model APIs rate limits and quotas](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits).

## Region availability[​](#region-availability "Direct link to region-availability")

note

If you require an endpoint in an unsupported region, reach out to your Databricks account team.

If your workspace is deployed in a region that supports model serving but is served by a [control plane](https://docs.databricks.com/aws/en/getting-started/high-level-architecture#architecture) in an unsupported region, the workspace does not support model serving. If you attempt to use model serving in such a workspace, you will see in an error message stating that your workspace is not supported. Reach out to your Databricks account team for more information.

See [Model serving features availability](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws) for more information on regional availability of each Model Serving feature.

For Databricks-hosted foundation model region availability, see [Foundation models hosted on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview#aws-models).
