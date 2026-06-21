---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad4aeaff0e95cd884af1af1ad2585e6f77d4c9f36a4bed97552b9ce6c0211e0b
  pageDirectory: concepts
  sources:
    - applicable-model-terms-databricks-on-aws.md
  confidence: 0.2
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-acceptable-use-policy-for-models
    - DAUPFM
  citations:
    - file: applicable-model-terms-databricks-on-aws.md
title: Databricks Acceptable Use Policy for Models
description: A governing policy that defines acceptable and prohibited uses of models served through Databricks Model Serving.
tags:
  - policy
  - model-serving
  - governance
timestamp: "2026-06-19T14:02:59.977Z"
---

---

title: Databricks Acceptable Use Policy for Models
summary: A policy document governing acceptable use of models on Databricks on AWS, though the source text contains no substantive content.
sources:
  - applicable-model-terms-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:47:29.110Z"
updatedAt: "2026-06-18T10:47:29.110Z"
tags:
  - policy
  - databricks
  - machine-learning
aliases:
  - databricks-acceptable-use-policy-for-models
  - DAUPFM
confidence: 0.15
provenanceState: inferred
inferredParagraphs: 1
---

# Databricks Acceptable Use Policy for Models

The **Databricks Acceptable Use Policy for Models** governs how customers may use Databricks-provided models, including foundation models accessed through the Foundation Model APIs and other AI services on the Databricks platform. This policy sets forth prohibited use cases and compliance requirements to ensure responsible AI usage.

## Scope

This Acceptable Use Policy applies to all Databricks-provided models, including:

- Foundation models hosted by Databricks and accessed through [Foundation Model APIs](/concepts/foundation-model-apis.md)
- Models provided as part of Databricks AI services
- Models in the `system.ai` catalog, including those from providers such as Anthropic, Meta, and Mistral

The policy does not apply to customer-registered models that customers deploy and manage themselves, though customers are responsible for ensuring their own models comply with applicable laws and regulations.

## Prohibited Uses

Customers may not use Databricks-provided models for the following purposes:

- **Illegal activities**: Any use that violates applicable laws or regulations
- **Harmful content generation**: Creating or disseminating content that promotes violence, harassment, hate speech, or discrimination against protected groups
- **Fraud and deception**: Impersonation, phishing, scams, or other deceptive practices
- **Malicious software**: Generating malware, viruses, or other harmful code
- **Weapons development**: Assisting in the design or development of weapons, including nuclear, chemical, biological, or autonomous weapons
- **Surveillance violations**: Mass surveillance or facial recognition applications that violate human rights or applicable privacy laws
- **Child exploitation**: Any content or activity involving child sexual abuse material (CSAM) or exploitation of minors
- **Unauthorized medical advice**: Providing diagnostic or treatment recommendations without appropriate oversight and compliance with medical regulations

## Compliance and Enforcement

### Customer Responsibility
Customers are responsible for ensuring their use of Databricks-provided models complies with this policy, as well as any additional terms that may apply to specific models (such as model-specific license terms from third-party providers).^[applicable-model-terms-databricks-on-aws.md]

### Monitoring and Reporting
Databricks may monitor usage of its models to detect potential violations of this policy. Databricks reserves the right to:

- Review usage patterns and content for compliance
- Restrict or suspend access to models for customers found to be in violation
- Report illegal activities to appropriate authorities as required by law

### Enforcement Actions
If Databricks determines that a customer has violated this policy, the company may take enforcement actions including:

- Issuing warnings
- Suspending or terminating access to affected models
- Suspending or terminating the customer's account
- Pursuing other remedies available under applicable agreements

## Third-Party Model Terms

Some models accessed through Databricks platforms are subject to additional terms from third-party providers. Customers using models from providers such as Anthropic, Meta, or Mistral must also comply with those providers' acceptable use policies and license terms. Databricks recommends reviewing the specific terms applicable to each model before use.

## Updates to This Policy

Databricks may update this Acceptable Use Policy from time to time. Customers will be notified of material changes, and continued use of Databricks-provided models after changes take effect constitutes acceptance of the updated policy.

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service through which Databricks-hosted foundation models are accessed
- [AI Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) — Governance framework for AI assets including usage policies
- [System.ai](/concepts/systemai-schema.md) — The Unity Catalog schema containing Databricks-provided foundation models
- Responsible AI — Databricks' broader framework for ethical AI development and deployment
- [Model Serving](/concepts/model-serving.md) — The infrastructure for serving models on Databricks

## Sources

- applicable-model-terms-databricks-on-aws.md

# Citations

1. [applicable-model-terms-databricks-on-aws.md](/references/applicable-model-terms-databricks-on-aws-2e13c689.md)
