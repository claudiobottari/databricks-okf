---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5978a36c842b2f818c31c818ebe246fa721161027fc320164749af024283cd67
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - prompt-iteration-workflow
    - PIW
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Prompt Iteration Workflow
description: A methodology for iteratively improving LLM prompts by defining evaluation criteria, running evaluations, reviewing results in the MLflow UI, refining prompts, and comparing runs.
tags:
  - prompt-engineering
  - workflow
  - iterative-development
timestamp: "2026-06-19T17:23:16.613Z"
---

# Prompt Iteration Workflow

The **Prompt Iteration Workflow** is a structured cycle for systematically improving a generative AI (GenAI) application’s prompts by evaluating outputs, analyzing results, refining the prompt, and re-evaluating. This iterative process uses MLflow’s evaluation framework to quantify changes in quality and to compare multiple prompt versions side by side in the MLflow UI. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

A typical prompt iteration workflow consists of the following phases:

1. **Define a baseline prompt** – Create an initial system prompt for the GenAI application.  
2. **Set evaluation criteria** – Choose one or more scorers (e.g., [Guidelines Scorer](/concepts/guidelines-scorer.md), [Safety Scorer](/concepts/safety-scorer-in-mlflow.md)) that measure desired qualities such as humour, safety, or template adherence.  
3. **Run evaluation** – Use `mlflow.genai.evaluate()` to score the application’s outputs against a prepared evaluation dataset.  
4. **Review results** – Inspect scores, individual outputs, and trace details in the MLflow UI to identify weaknesses.  
5. **Refine the prompt** – Adjust the system prompt to address the weaknesses (e.g., add rules, examples, or constraints).  
6. **Re-run evaluation** – Apply the same evaluation dataset and scorers to the updated prompt.  
7. **Compare results** – Use the MLflow UI’s run comparison view to assess improvement across scorers.  

The cycle repeats until the prompt meets the desired quality thresholds. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Example: Mad Libs Sentence Completion

In the MLflow 10‑minute demo, a sentence‑completion app is built to fill blanks in a Mad Libs‑style template. The initial system prompt asks the model to be “creative and edgy.” Evaluation scorers include `Guidelines` for language consistency, funniness, child‑safety, and template matching, plus a built-in `Safety` scorer. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

After the first evaluation, the results show that some outputs are not appropriate for children. The prompt is then revised to be explicit about child‑appropriate silliness and absurdity (e.g., “make choices that are SILLY, UNEXPECTED, and ABSURD (but appropriate for kids)”). The revised prompt also includes example completions. The evaluation is re‑run with the same dataset and scorers, and the two runs are compared in the MLflow UI. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Best Practices

- **Use multiple dimensions of quality** – Combine several scorers (e.g., correctness, safety, style) to get a holistic view of prompt performance.  
- **Keep evaluation data fixed** – Reuse the same evaluation dataset across iterations to enable consistent comparisons.  
- **Leverage the MLflow UI** – The run comparison view makes it easy to spot which metrics improved or regressed after a prompt change.  
- **Document prompt versions** – Treat each prompt as a distinct code artifact tied to an [MLflow Run](/concepts/mlflow-run.md) for reproducibility. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework that powers the automated scoring and comparison.  
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – Pre‑built and custom scorers used to evaluate outputs.  
- [Guidelines Scorer](/concepts/guidelines-scorer.md) – A scorer that checks whether outputs follow a user‑written guideline.  
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) – A built‑in scorer for detecting harmful or unsafe content.  
- Evaluate and Improve a GenAI Application – The full tutorial that expands on the iteration workflow.

## Sources

- [10-minute demo: Evaluate a GenAI app | Databricks on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/eval) (ingested 2026‑06‑18) – source file `10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md`

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
