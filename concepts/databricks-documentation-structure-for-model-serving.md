---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05fdcb3bd1d69cd78bdcd2dacdf734bfec963c0dd44ddd11b9973ee300839873
  pageDirectory: concepts
  sources:
    - applicable-model-terms-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-documentation-structure-for-model-serving
    - DDSFMS
  citations:
    - file: applicable-model-terms-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: 403-permission_denied-serverless-budget-policy-error.md
    - file: 8xh100-single-node-configuration.md
    - file: filename.md
    - file: file-a.md
    - file: file-b.md
    - file: filename.md:START-END
    - file: 403-permission_denied-serverless-budget-policy-error.md#cause
    - file: 8xh100-single-node-configuration.md#verification
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Documentation Structure for Model Serving
description: The URL path convention used by Databricks to organize model-serving documentation under /aws/en/machine-learning/model-serving/.
tags:
  - documentation
  - site-structure
  - model-serving
timestamp: "2026-06-19T14:03:03.345Z"
---

# Databricks Documentation Structure for Model Serving

The **Databricks Documentation Structure for Model Serving** defines the standard format used by this wiki for all pages related to model serving on Databricks. Each page is a self-contained concept article that follows a consistent metadata schema, markdown content layout, source attribution convention, and internal linking pattern. The structure is designed to make information machine‑readable, traceable to its original documentation, and easy to cross‑reference.

## Page Metadata

Every page begins with a YAML frontmatter block that stores structured metadata. The following fields are present in all model‑serving pages:

- **`title`** – The page name, e.g. “403 PERMISSION_DENIED Serverless Budget Policy Error”.  
- **`summary`** – A one‑sentence overview of the concept.  
- **`sources`** – A list of source documents that the page draws from, each ending in `.md`.  
- **`kind`** – Always set to `concept` for these pages.  
- **`createdAt`** and **`updatedAt`** – ISO timestamps for the page’s creation and last revision.  
- **`tags`** – An array of tag strings (e.g. `databricks`, `mlflow`, `error`).  
- **`aliases`** – Alternative page names (e.g. `403-permission_denied-serverless-budget-policy-error`).  
- **`confidence`** – A numeric value between 0 and 1 indicating the author’s confidence in the factual accuracy of the extracted content.  
- **`provenanceState`** – Either `extracted` (directly from source) or `inferred` (logical deduction).  
- **`inferredParagraphs`** – Integer count of paragraphs that are the author’s inference rather than direct extraction.

These fields are uniformly present across all provided model‑serving pages. ^[applicable-model-terms-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Content Format

The body of each page is written in Markdown and includes:

- **Prose paragraphs** that explain the concept. Each paragraph ends with a citation marker (see “Citation Conventions” below).  
- **Code blocks** (fenced with triple backticks) that show command examples or API usage. These are not cited individually.  
- **Tables** that summarise options, error values, or configuration parameters.  
- **Lists** (ordered and unordered) for enumerating steps, causes, or related concepts.

All content is organised under headings (H2, H3) that break the page into logical sections such as “Overview”, “Cause”, “Solution”, “Related Concepts”. The phrasing is neutral and informative. ^[403-permission_denied-serverless-budget-policy-error.md, 8xh100-single-node-configuration.md]

## Citation Conventions

Every factual claim is attributed to its source document using a citation marker at the end of the paragraph (or, for specific sentences, at the end of that sentence). Three citation forms are used:

| Form | Example | Source file |
|------|---------|-------------|
| Single‑source paragraph | `^[filename.md]` | visible in all pages |
| Multi‑source paragraph | `^[file-a.md, file-b.md]` | used when a claim is supported by multiple sources |
| Claim‑level (line range) | `^[filename.md:START-END]` | used for precise line referencing |

The source file name is always the original Databricks documentation page, converted to a Markdown filename (e.g. `configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md`). This convention ensures every statement can be traced back to the official documentation. ^[403-permission_denied-serverless-budget-policy-error.md#cause, 8xh100-single-node-configuration.md#verification]

## Linking

Pages use wikilinks to connect to related concepts. Examples from the provided pages include:

- [MLflow](/concepts/mlflow.md)  
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)  
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)  
- [Custom Judges](/concepts/custom-judges.md)  
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)  

These links appear inline in the prose and are also listed in a “Related Concepts” section near the end of each page. The linked pages themselves follow the same documentation structure. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Sources Section

Every page concludes with a `## Sources` heading that lists the source document(s) from which the page was derived. This list contains only the filename(s) of the original Databricks documentation. No external URLs or additional references are included. ^[applicable-model-terms-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – The overarching feature that these pages document.  
- Documentation Metadata Schema – The formal definition of the YAML frontmatter fields.  
- Source Attribution Best Practices – Further guidelines on how citations are managed in this wiki.  
- Wiki Page Anatomy – A general guide to the content and structure of all wiki pages.

## Sources

- applicable-model-terms-databricks-on-aws.md  
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md  
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md  
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md  
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md  
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [applicable-model-terms-databricks-on-aws.md](/references/applicable-model-terms-databricks-on-aws-2e13c689.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
4. 403-permission_denied-serverless-budget-policy-error.md
5. 8xh100-single-node-configuration.md
6. filename.md
7. file-a.md
8. file-b.md
9. filename.md:START-END
10. 403-permission_denied-serverless-budget-policy-error.md#cause
11. 8xh100-single-node-configuration.md#verification
12. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
