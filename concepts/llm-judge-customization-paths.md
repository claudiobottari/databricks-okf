---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b292c9386d7f7199cc842526ad299e121af575d76a28c87555f42d72c388158e
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judge-customization-paths
    - LJCP
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: LLM Judge Customization Paths
description: Alternatives to built-in judges, including custom LLM judges for more control and Python code-based scorers, enabling users to tailor evaluation to their specific use cases.
tags:
  - llm-evaluation
  - customization
  - databricks
timestamp: "2026-06-19T17:42:29.670Z"
---

# LLM Judge Customization Paths

LLM judges are [scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) that use an LLM to evaluate quality dimensions (e.g., relevance, safety, groundedness) of a GenAI application. Built-in LLM judges provide a quick start, but when more control is needed, several customization paths are available. These paths form a spectrum from zero‑configuration use to fully custom solutions. ^[built-in-llm-judges-databricks-on-aws.md]

## Path 1: Use Built‑in LLM Judges As‑Is

Built‑in LLM judges are predefined scorers that use Databricks‑hosted LLMs. They evaluate common quality dimensions without requiring any configuration beyond specifying the required arguments (typically `inputs` and `outputs`, and sometimes `expectations`). Available judges include `RelevanceToQuery`, `RetrievalRelevance`, `Safety`, `RetrievalGroundedness`, `Correctness`, `RetrievalSufficiency`, `Guidelines`, `ExpectationsGuidelines`, `ToolCallCorrectness`, and `ToolCallEfficiency`. Multi‑turn judges are also available for conversational AI systems. ^[built-in-llm-judges-databricks-on-aws.md]

## Path 2: Select the LLM That Powers a Judge

For any LLM judge (built‑in or custom), you can choose which underlying LLM to use. This allows you to trade off cost, latency, and evaluation quality. The Databricks documentation provides guidance on selecting the LLM that powers a judge. ^[built-in-llm-judges-databricks-on-aws.md]

## Path 3: Build a Custom LLM Judge

When built‑in judges do not fit your use case, you can build a [Custom LLM Judge](/concepts/custom-llm-judge.md). Custom judges let you define your own evaluation criteria and prompt template while still leveraging an LLM for scoring. This path gives more control over the evaluation logic without requiring hand‑written code. ^[built-in-llm-judges-databricks-on-aws.md]

## Path 4: Use Python Code‑Based Scorers

For maximum flexibility, you can implement a scorer entirely in Python using [code‑based scorers](/concepts/code-based-scorers.md). This path is appropriate when you need to execute arbitrary logic, call external APIs, or implement complex scoring algorithms that cannot be expressed as an LLM prompt. ^[built-in-llm-judges-databricks-on-aws.md]

## Path 5: Align Judges with Human Feedback

To improve the accuracy and domain‑specificity of your judges, you can [align judges with human feedback](/concepts/aligning-judges-with-human-experts.md). This process adjusts the judge’s behavior based on human‑rated examples, making it more reliable for your particular application and reducing the gap between automated evaluation and human judgment. ^[built-in-llm-judges-databricks-on-aws.md]

---

These customization paths are ordered from least to most effort and control. Start with built‑in judges for rapid prototyping, then move to custom judges or code‑based scorers as your evaluation requirements become more nuanced. Aligning judges with human feedback can be applied at any stage to further refine quality assessment.

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
