---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a5479ff66222a1e1584868ed2cc5c88a0a211b0ba89858793dc731fe1e41610
  pageDirectory: concepts
  sources:
    - openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-user-authentication-for-ai-systems
    - EUAFAS
  citations:
    - file: openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md
title: External User Authentication for AI Systems
description: Requirements for authenticating or monitoring users outside an organization who interact with AI applications, including multi-factor authentication and activity logging.
tags:
  - AI-security
  - authentication
  - auditing
timestamp: "2026-06-19T19:50:47.877Z"
---

# External User Authentication for AI Systems

**External User Authentication for AI Systems** refers to the security mechanisms and requirements that organizations must implement when making AI applications — particularly those powered by foundation models like OpenAI — accessible to users outside the organization. These requirements are designed to mitigate risks associated with unauthorized access, misuse, and lack of accountability in high-risk AI use cases.

## Overview

When AI applications are accessible to users outside an organization, additional authentication and monitoring controls are necessary. Databricks mandates specific mitigation requirements for high-risk use cases involving OpenAI models, particularly when external users can interact with the system. These requirements ensure visibility, accountability, and the ability to respond to potential misuse. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Authentication Requirements

For applications accessible to users outside the organization, one of the following authentication or monitoring mechanisms must be implemented:

- **Two-factor or multi-factor authentication (MFA)**: Require external users to verify their identity through a second factor beyond just a password.
- **Logging of individual end user IDs**: Maintain auditable logs that associate each interaction with a specific user identity for visibility and remediation purposes.
- **Logging of individual IP addresses**: Capture and store IP address information for each end user to enable visibility and remediation if misuse is detected.

^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Related High-Risk Use Cases

External user authentication requirements apply specifically to applications categorized as high-risk. The following use cases trigger these authentication obligations:

### Applications Involving Chat or Conversations

Applications that enable users to interact with a conversational agent must be verified as **grounded or topical**. This means users interacting with the application do not have unrestricted access to query the model with general inputs that generate unrestricted outputs. The authentication mechanisms above ensure that if misuse occurs, it can be traced back to a specific user. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

### Code Generation or Transformation Scenarios

For applications involving code generation, additional requirements beyond authentication include:

- Human review of any code before it is used in production.
- Restricting code generation to internal users or implementing client-side monitoring for misuse.

^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

### Applications Enabling Image Inputs

When applications accept image inputs from external users, organizations must ensure that such inputs are restricted to low risk and topical images. ^[openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md]

## Implementation Considerations

Organizations deploying Foundation Models or OpenAI models on Databricks that will be accessed by external users should:

1. Identify whether the application falls into a high-risk use case category.
2. Select and implement at least one of the required authentication or monitoring mechanisms.
3. Ensure the application is grounded or topical if it involves conversational interfaces.
4. Establish logging and monitoring procedures to review user activity and respond to incidents.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying and querying AI models.
- OpenAI Model Mitigation Requirements — Broader risk mitigation guidelines for OpenAI models.
- Foundation Model Overview — Overview of foundation model serving on Databricks.
- User Authentication — General authentication mechanisms for cloud platforms.
- Application Security — Security considerations for AI-powered applications.
- [Audit Logging](/concepts/abac-policy-audit-logging.md) — Practices for recording user activity for security and compliance.

## Sources

- openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md

# Citations

1. [openai-high-risk-use-case-mitigation-requirements-databricks-on-aws.md](/references/openai-high-risk-use-case-mitigation-requirements-databricks-on-aws-1a6b8630.md)
