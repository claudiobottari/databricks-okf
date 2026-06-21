---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eca425d55cb7a14fe5f68519ad16dc63242eade1ec9cbd7099723dda164ba509
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - generating-test-cases-from-production-conversations
    - GTCFPC
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Generating Test Cases from Production Conversations
description: Extracting structured test cases (goals and personas) from existing production conversation sessions using mlflow.genai.simulators.generate_test_cases, enabling test scenarios that reflect real user behavior.
tags:
  - mlflow
  - testing
  - conversational-ai
  - data-generation
timestamp: "2026-06-19T14:25:35.216Z"
---

---

title: Generating Test Cases from Production Conversations
summary: A workflow in MLflow that extracts goals and personas from existing production conversation sessions (via `mlflow.search_sessions` and `generate_test_cases`) to create test cases that reflect real user behavior.
sources:
  - conversation-simulation-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:09:47.546Z"
updatedAt: "2026-06-18T11:09:47.546Z"
tags:
  - mlflow
  - testing
  - data-generation
  - production
aliases:
  - generating-test-cases-from-production-conversations
  - GTCFPC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## Generating Test Cases from Production Conversations

**Generating test cases from production conversations** is a feature of [MLflow](/concepts/mlflow.md)'s conversation simulation system that allows you to extract synthetic evaluation scenarios from real user sessions. By analyzing existing conversation traces, MLflow can infer the goals and personas exhibited in those interactions and produce a set of test cases that reflect actual user behavior. ^[conversation-simulation-databricks-on-aws.md]

This approach addresses the challenge of building representative test suites for conversational AI agents. Instead of manually writing scenarios or waiting for enough production data, you can programmatically derive test cases that cover the breadth of real-world usage patterns. ^[conversation-simulation-databricks-on-aws.md]

### Prerequisites

Install MLflow 3.10.0 or later:

```bash
pip install --upgrade 'mlflow[databricks]>=3.10'
```

^[conversation-simulation-databricks-on-aws.md]

### Basic Workflow

1. **Retrieve existing conversation sessions** from an MLflow experiment using `mlflow.search_sessions()`.
2. **Generate test cases** by calling `generate_test_cases()` on those sessions.
3. **(Optional) Persist the test cases** as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) for reproducibility.
4. **Use the test cases** with a [ConversationSimulator](/concepts/conversationsimulator.md) in `mlflow.genai.evaluate()`.

^[conversation-simulation-databricks-on-aws.md]

### Generating Test Cases from Sessions

The `generate_test_cases` function extracts goals and personas from production conversation sessions. Each session is typically a sequence of turns stored in an MLflow experiment's **Sessions** tab. The function returns a list of test case dictionaries, each containing a `goal` and optionally a `persona`, that can be passed directly to a `ConversationSimulator`. ^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

# Get existing sessions from your experiment
sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

# Generate test cases by extracting goals and personas from sessions
test_cases = generate_test_cases(sessions)

# Use generated test cases with the simulator
simulator = ConversationSimulator(test_cases=test_cases)
```

^[conversation-simulation-databricks-on-aws.md]

### Persisting Test Cases as an MLflow Dataset

For reproducible testing, you can save the generated test cases as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) using `mlflow.genai.datasets`. This allows you to version and reuse the same scenario set across evaluation runs. ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset

dataset = create_dataset(name="generated_scenarios")
dataset.merge_records([{"inputs": tc} for tc in test_cases])

# Later, load the dataset and create the simulator
simulator = ConversationSimulator(test_cases=dataset)
```

^[conversation-simulation-databricks-on-aws.md]

### When to Use This Approach

Generating test cases from production conversations is especially valuable when:

- You want to base your evaluation suite on real user behavior rather than hand‑crafted scenarios.
- You need to quickly expand test coverage after an agent update or deployment.
- You are conducting red‑teaming or stress‑testing with diverse, realistic user personas.

The extracted test cases can be combined with manually defined ones to create a balanced evaluation set that covers both common and edge‑case interactions. ^[conversation-simulation-databricks-on-aws.md]

### Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) – The class that runs simulated conversations from test cases.
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) – Persistent storage for reproducible test scenarios.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Containers for runs, sessions, and traces.
- [[Scorers]] – Functions that evaluate each turn or the full conversation.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
