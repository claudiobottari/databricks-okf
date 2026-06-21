---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50440feff1cee4119e901911f6de110f45837f8f4da3f0ae7bd1a791f0eb7397
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - document-extraction-accuracy-evaluation
    - DEAE
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Document Extraction Accuracy Evaluation
description: Patterns for evaluating document extraction applications with guidelines judges, covering field extraction completeness, numerical handling, entity recognition, and document-type-specific criteria.
tags:
  - use-cases
  - document-processing
  - genai
timestamp: "2026-06-19T17:56:06.033Z"
---

# Document Extraction Accuracy Evaluation

**Document Extraction Accuracy Evaluation** is the process of assessing how well an AI system extracts structured data from unstructured documents such as invoices, contracts, and medical records. This evaluation typically uses [LLM Judges](/concepts/llm-judges.md) with pass/fail criteria to verify the completeness, correctness, and consistency of extracted fields. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Overview

Document extraction accuracy evaluation focuses on three primary dimensions: field-level completeness and accuracy, numerical and financial data handling, and entity recognition and validation. Each dimension defines specific pass/fail criteria that an extraction system must meet. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Evaluation Dimensions

### Field Extraction Completeness and Accuracy

The system must extract all requested fields using exact values from the source document. For ambiguous data, the system should extract the most likely value and include a confidence score. When multiple values exist for a single field — such as multiple addresses — all values should be extracted and labeled appropriately. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Original formatting must be preserved for IDs, reference numbers, and codes, including leading zeros. For missing fields, the system should return `null` with a reason, such as `{"field": null, "reason": "not_found"}`. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Numerical and Financial Data Handling

Currency values must preserve exact decimal places as shown in the source. The system must differentiate between multiple currencies if present (for example, USD vs. EUR). Percentage values must clarify whether they are decimals (0.15) or percentages (15%). For calculated fields such as totals and tax, the extracted values must match the source exactly without recalculation. Negative values must be preserved with proper notation, such as `-$100` or `($100)`. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Entity Recognition and Validation

Company names must be extracted exactly as written, including suffixes like Inc., LLC, or GmbH. Person names must preserve original order and formatting. Similar but distinct entities — for example, "John Smith" and "J. Smith" — must be kept separate rather than merged. Email addresses and phone numbers must be validated for basic format correctness, and physical addresses must include all components present in the source. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Output Format Compliance

Beyond field-level accuracy, evaluation should verify that the output structure meets enterprise data standards. The output must be valid JSON with consistent snake_case field names. Nested objects must maintain the hierarchy from the source document, and arrays must be used for multiple values — never concatenated strings. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Data Type Standards

- **Dates**: ISO 8601 format (`YYYY-MM-DD`) with timezone if available
- **Timestamps**: ISO 8601 with time (`YYYY-MM-DDTHH:MM:SSZ`)
- **Currency**: Structured as `{"amount": 1234.56, "currency": "USD", "formatted": "$1,234.56"}`
- **Phone**: Structured as `{"number": "+14155551234", "formatted": "(415) 555-1234", "type": "mobile"}`
- **Boolean**: `true`/`false` (not `"yes"`/`"no"` or `1`/`0`)

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Metadata Requirements

The extraction output should include an `extraction_timestamp` in UTC, a `source_page` indicator for multi-page documents, a `confidence_score` (0–1) for each machine-learning-extracted field, and a `validation_flags` array for any data quality issues detected. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Document-Type-Specific Guidelines

### Invoices

Invoice extraction evaluation must verify that the invoice number is preserved with exact formatting, including prefixes and suffixes. Line items should be extracted as an array with description, quantity, unit price, and total. The system must identify and separate subtotal, tax amounts (with rates), shipping costs, and discounts. Currency must be identified explicitly rather than assumed to be USD. Payment terms such as "Net 30" or "2/10 Net 30" must be extracted, and any mathematical inconsistencies between line items and totals must be flagged. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Contracts

Contract extraction evaluation must verify that all parties are extracted with their full legal names and entity types. Party roles must be identified (buyer/seller, licensee/licensor, employer/employee). The system must differentiate between execution date, effective date, and expiration date, and must extract notice periods for termination, automatic renewal clauses, and milestone dates. Payment terms, liability caps, indemnification clauses, and insurance requirements must all be extracted. Dispute resolution mechanisms and non-compete, non-solicitation, or confidentiality periods should be flagged. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Medical Records

Medical record extraction evaluation must ensure HIPAA compliance and privacy protection. The system must never extract full Social Security numbers — only the last four digits if needed for matching. Diagnoses must use ICD-10 codes when available, with lay descriptions. Medications must include generic name, brand name, dosage, frequency, route, and start date. The system must differentiate between active and discontinued medications. Allergies must specify type (drug, food, environmental) and reaction severity. Lab results must include value, unit, reference range, and abnormal flags. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Implementation with Guidelines Judges

Document extraction accuracy evaluation can be implemented using [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) with either global or per-row guidelines. A `Guidelines()` judge applies uniform criteria across all documents, while an `ExpectationsGuidelines()` judge applies different criteria per document type or per row in the evaluation dataset. Guidelines judges return a binary pass/fail score with detailed rationale explaining why the content passed or failed each criterion. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — AI-based evaluators for GenAI outputs
- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) — Pass/fail judges using natural language criteria
- Data Quality Assessment — Broader evaluation of data quality
- Document Understanding — AI techniques for processing documents
- Named Entity Recognition (NER) — Identifying entities in text

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
