---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 821703022dfc1b82db63691ed9fbfa1510337cda2f1b1963dd83645b9b93aa10
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customer-service-chatbot-evaluation-patterns
    - CSCEP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Customer Service Chatbot Evaluation Patterns
description: Real-world patterns for evaluating customer service chatbots using guidelines judges, covering tone, policy compliance, urgent situations, cancellations, and billing disputes.
tags:
  - use-cases
  - customer-service
  - genai
timestamp: "2026-06-19T17:55:52.940Z"
---

# Customer Service Chatbot Evaluation Patterns

**Customer Service Chatbot Evaluation Patterns** refer to structured, reusable approaches for assessing the quality, compliance, and tone of chatbot responses using [LLM Judge](/concepts/llm-judges.md) frameworks. These patterns leverage natural language guidelines to systematically evaluate chatbot outputs in both offline evaluation and production monitoring scenarios.

## Overview

Customer service chatbots require evaluation across multiple dimensions simultaneously: tone, policy compliance, factual accuracy, and context‑appropriate behavior. The [Guidelines() Judge](/concepts/guidelines-llm-judge.md) and [ExpectationsGuidelines() Judge](/concepts/expectationsguidelines-judge-per-row-guidelines.md) from MLflow provide a flexible mechanism to encode these requirements as pass/fail natural language criteria. Global guidelines apply uniformly across all interactions, while per‑row guidelines allow domain experts to specify different criteria for different scenarios. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Global Guidelines Patterns

Global guidelines are defined once and applied to every chatbot response in an evaluation or production trace. Common patterns include:

- **Tone and empathy guidelines** that enforce a professional yet warm brand voice, require acknowledgment of emotional context (e.g., frustration, anger) before jumping to solutions, and prohibit minimization phrases like “simply” or “just”. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Policy compliance guidelines** covering refund and return policies, data privacy (never ask for full credit card numbers, SSN, passwords), and commitment limitations (no guaranteed delivery dates without system verification). These guidelines can be grouped into multiple separate criteria or a single compound guideline. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Structure and completeness guidelines** that require specific sections (greeting, addressing the question, ending with an offer) or constrain response length. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Global guidelines are ideal for enforcing brand standards and regulatory requirements that do not change from one interaction to another.

## Per‑Row Guidelines Patterns

Per‑row guidelines (via the `ExpectationsGuidelines` judge) let domain experts define custom evaluation criteria for individual examples. This pattern is especially valuable for testing how a chatbot handles edge cases or high‑stakes scenarios. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Three canonical customer service scenarios illustrate the approach:

1. **Urgent package delay** – Guidelines require acknowledging both the delay and an imminent deadline, expressing genuine empathy, offering immediate actionable solutions (e.g., same‑day pickup, overnight shipping at no charge), and including compensation options (shipping refund, discount) without being asked. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
2. **Cancellation request** – Guidelines mandate respecting the customer’s decision (no guilt‑inducing language), providing complete cancellation steps, clarifying data retention policies, and optionally mentioning one gentle retention offer as a soft alternative. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
3. **Duplicate charge dispute** – Guidelines require immediately validating the concern without skepticism, providing specific resolution details (exact refund timeline, pending reversal, confirmation email with transaction ID), and proactively addressing potential financial impacts such as overdraft fee reimbursement. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Each scenario includes multiple sub‑guidelines that can be evaluated independently or as a composite. The judge returns a binary pass/fail (`yes`/`no`) along with a rationale explaining the decision. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Key Evaluation Dimensions

Customer service chatbot evaluation patterns typically cover these dimensions:

| Dimension | Example Guideline |
|-----------|------------------|
| Empathy & Tone | “If the customer expresses frustration, the first sentence must acknowledge their emotion.” |
| Policy Adherence | “The response must not promise refunds beyond the 30‑day return window.” |
| Actionability | “The response must end with a specific next step or open‑ended offer to help.” |
| Data Privacy | “The response must never ask for full credit card numbers, SSN, or passwords.” |
| Compensation Handling | “The response must include compensation options without being asked.” |

These dimensions are encoded as natural language rules that reference context variables such as `request`, `response`, `retrieved_documents`, or custom fields like `user_tier`. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices for Writing Guidelines

- **Be specific and measurable** – Prefer “Must not include specific pricing amounts or percentages” over “Don’t talk about money.”
- **Use clear pass/fail conditions** – Replace “Handle pricing questions appropriately” with “If asked about pricing, the response must direct users to the pricing page.”
- **Reference context explicitly** – Use variables from the evaluation context (e.g., `retrieved_documents`, `user_preferences`) in the guideline text.
- **Structure complex requirements** – Use bullet‑point style inside a single guideline string to enumerate multiple conditions.
- **Group related rules** – Combine several sub‑requirements under one guideline for readability and to reduce the number of judges. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [LLM Judge](/concepts/llm-judges.md) – General framework for evaluating GenAI outputs using language models.
- [Guidelines() Judge](/concepts/guidelines-llm-judge.md) – Prebuilt judge for applying global pass/fail criteria.
- [ExpectationsGuidelines() Judge](/concepts/expectationsguidelines-judge-per-row-guidelines.md) – Prebuilt judge for per‑row expert‑defined criteria.
- Offline Evaluation – Running judges on pre‑collected datasets.
- [Production Monitoring](/concepts/production-monitoring.md) – Applying judges continuously to live chatbot traces.
- [MLflow Evaluate](/concepts/mlflow-genai-evaluate-api.md) – The API used to orchestrate evaluations.
- Customer Service Chatbot – The application domain addressed by these patterns.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
