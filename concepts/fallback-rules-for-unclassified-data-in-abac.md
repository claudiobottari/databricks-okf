---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8075825cfe8ac0d6b5787bfba5556c3f60c70fc07cf3ef7b1fd8f833091e3d9
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fallback-rules-for-unclassified-data-in-abac
    - FRFUDIA
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Fallback Rules for Unclassified Data in ABAC
description: Implementing default restrictive tags and policies for unclassified or untagged data objects to prevent unprotected data exposure.
tags:
  - attribute-based-access-control
  - data-governance
  - security
timestamp: "2026-06-19T17:40:21.441Z"
---

```markdown
# Fallback Rules for Unclassified Data in ABAC

**Fallback Rules for Unclassified Data in ABAC** are governance mechanisms that automatically protect data objects that lack appropriate Data Classification Tags in an [[Attribute-Based Access Control (ABAC)]] system. They ensure that untagged or misclassified data is not left unprotected due to missing or incorrect tags. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Rationale

Tagging is a security boundary in ABAC. If a user can change tags on a data asset, they can change which policies apply to it. Wrong or missing tags can leave data unprotected or inaccessible because policies only apply when the right tags are in place. Fallback rules mitigate this risk by ensuring that the absence of a proper tag results in a restrictive default, not an open one. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

### Apply a Default Restrictive Tag

Use automation to apply a default restrictive tag (such as `classification : unverified`) to new data objects as soon as they are created. This tag signals that the object has not yet been reviewed by a data steward and should be treated with heightened caution. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Create a Restrictive Policy for the Default Tag

Define an [[ABAC (Attribute-Based Access Control)]] policy that restricts access to objects bearing the default classification tag. For example, a policy might block all read or write operations on objects tagged `classification : unverified` unless the user is a designated data steward or governance administrator. This ensures that unclassified data cannot be accessed broadly until a steward inspects and re-tags it. ^[best-practices-for-abac-policies-databricks-on-aws.md]

For a concrete implementation example, see [[Prevent access until sensitive columns are tagged]]. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Automate Tag Enforcement

Rather than relying solely on manual tagging, integrate automated processes into your data pipeline that:
- Apply the default tag at object creation time.
- Trigger notifications to data stewards when new unclassified objects appear.
- Remove the default tag and apply appropriate classification tags after steward review.

^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [[Attribute-Based Access Control (ABAC)]] — The overall access control model that uses tags for policy evaluation.
- Data Classification Tags — The taxonomy of tags (e.g., `sensitivity`, `classification`) that drive ABAC policies.
- [[Prevent access until sensitive columns are tagged]] — A detailed pattern showing how to implement fallback rules.
- [[Governed Tags]] — Controls for restricting who can create and modify tags.
- Tag Governance — Broader practices for managing tagging taxonomies and permissions.
- ABAC Policy Design Best Practices — Guidance on creating effective, maintainable ABAC policies.

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md
```

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
