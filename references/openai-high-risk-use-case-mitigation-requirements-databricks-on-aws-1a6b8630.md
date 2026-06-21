---
title: OpenAI high risk use case mitigation requirements | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/open-ai-mitigation-requirements
ingestedAt: "2026-06-18T08:12:19.969Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Agents](https://docs.databricks.com/aws/en/agents/)
*   [Query LLMs and agents](https://docs.databricks.com/aws/en/agents/query-llms)
*   [Serve and query foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview)
*   Mitigation requirements for OpenAI models

Last updated on **May 7, 2026**

In this page, learn about the mitigation requirements for OpenAI high risk use cases. You are responsible for implementing these requirements when using OpenAI models on Databricks

## Mitigation requirements[​](#mitigation-requirements "Direct link to Mitigation requirements")

End users must implement the following requirements when using OpenAI for the following high-risk use cases:

High-risk use case

Description

Mitigation

Applications involving chat or conversations

Applications that enable users to interact with a conversational agent

Verify that such applications are grounded or topical meaning that users interacting with the application do not have unrestricted access to query the model with general inputs that generate unrestricted outputs.

Applications accessible to users outside your organization

Authenticate or monitor such users through one of the following mechanisms:

*   Two factor or multi-factor authentication.
*   Logging of individual end user IDs for visibility and remediation.
*   Logging of individual IP addresses for visibility and remediation.

Applications involving code generation or transformation scenarios

*   Conduct human review of any code before it is used in production.
*   Limit user-based risk by either restricting code generation to internal users or implementing client-side monitoring for misuse.

Applications enabling image inputs

You are required to ensure that such inputs are restricted to low risk and topical images.
