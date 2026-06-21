---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff126b849cc0c90f44dd73595590a48b52244b8b7eafdff9de5be19f9b9420a8
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset-for-conversation-testing
    - MEDFCT
    - mlflow-evaluation-dataset-for-reproducible-testing
    - MEDFRT
    - Reproducible Testing
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: MLflow Evaluation Dataset for Conversation Testing
description: Persisting conversation test cases as reproducible MLflow Evaluation Datasets using create_dataset and merge_records.
tags:
  - mlflow
  - testing
  - reproducibility
  - datasets
timestamp: "2026-06-19T09:24:47.872Z"
---

```yaml
---
title: MLflow Evaluation Dataset for Conversation Testing
summary: A mechanism to persist test cases as an MLflow Evaluation Dataset using `create_dataset` and `merge_records`, enabling reproducible testing by storing and retrieving conversation test case scenarios.
sources:
  - conversation-simulation-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:10:33.556Z"
updatedAt: "2026-06-18T11:10:33.556Z"
tags:
  - mlflow
  - testing
  - reproducibility
  - datasets
aliases:
  - mlflow-evaluation-dataset-for-conversation-testing
  - MEDFCT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Evaluation Dataset for Conversation Testing

An **MLflow Evaluation Dataset for Conversation Testing** is a structured, versioned collection of test scenarios used to drive [[conversation simulation]] workflows. It replaces ad‑hoc test case lists with a persistent, shareable dataset that can be versioned, audited, and reused across experiments.^[conversation-simulation-databricks-on-aws.md]

## Purpose

When testing a conversational AI agent, you typically define a set of test cases — each describing a goal a simulated user should achieve. Without an evaluation dataset, test cases live only in the Python code that creates the simulator, making them hard to share, track, or reproduce. By persisting test cases as an MLflow dataset, you can:^[conversation-simulation-databricks-on-aws.md]

- **Reproduce tests** across different agent versions or simulator configurations.
- **Version‑test scenarios** alongside model artifacts and experiment runs.
- **Audit coverage** — inspect which goals, personas, and contexts were tested.
- **Share scenarios** between teams without distributing source code.

## Creating an Evaluation Dataset

Use `mlflow.genai.datasets.create_dataset` to create a named dataset, then populate it with your test cases via `merge_records`:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset

dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records(
    [
        {"inputs": {"goal": "Successfully configure experiment tracking"}},
        {"inputs": {"goal": "Debug a deployment error", "persona": "Senior engineer"}},
    ]
)
```

Each record in the dataset corresponds to one test case. A test case is a dictionary that may contain:

| Field | Required | Description |
|-------|----------|-------------|
| `goal` | Yes | What the simulated user wants to achieve – specific and actionable |
| `persona` | No | How the simulated user communicates (default: helpful user) |
| `context` | No | Extra parameters passed to the agent's `predict_fn` via `**kwargs` |

^[conversation-simulation-databricks-on-aws.md]

### Using a DataFrame

You can also create a dataset from a pandas DataFrame:^[conversation-simulation-databricks-on-aws.md]

```python
import pandas as pd
from mlflow.genai.datasets import create_dataset

df = pd.DataFrame([
    {"goal": "Successfully configure experiment tracking"},
    {"goal": "Debug a deployment error", "persona": "Senior engineer"},
    {"goal": "Set up a CI/CD pipeline for ML"},
])

dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records([{"inputs": row.to_dict()} for _, row in df.iterrows()])
```

## Using an Evaluation Dataset with a Simulator

Once created, pass the dataset (or its test cases) to a [[ConversationSimulator]]:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import get_dataset
from mlflow.genai.simulators import ConversationSimulator

dataset = get_dataset(name="conversation_test_cases")

simulator = ConversationSimulator(
    test_cases=dataset,
    max_turns=5,
)
```

The simulator reads test cases from the dataset and generates synthetic multi‑turn conversations for each one. You can then pass the simulator to `mlflow.genai.evaluate()` with your [[scorers]] for evaluation.^[conversation-simulation-databricks-on-aws.md]

### Example: End-to-End Workflow

```python
import mlflow
from mlflow.genai.datasets import create_dataset, get_dataset
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety
from openai import OpenAI

client = OpenAI()

# 1. Create a reusable dataset
dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records([
    {"inputs": {"goal": "Successfully configure experiment tracking"}},
    {"inputs": {"goal": "Debug a deployment error", "persona": "Senior engineer"}},
])

# 2. Retrieve the dataset later
dataset = get_dataset(name="conversation_test_cases")

# 3. Define the agent
def predict_fn(input: list[dict], **kwargs):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input,
    )
    return response.choices[0].message.content

# 4. Simulate and evaluate
simulator = ConversationSimulator(test_cases=dataset, max_turns=5)
results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[ConversationCompleteness(), Safety()],
)
```

## Generating Test Cases from Existing Conversations

Use `mlflow.genai.simulators.generate_test_cases` to extract test scenarios from real production conversations stored in MLflow sessions:^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases

sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

test_cases = generate_test_cases(sessions)
```

You can then persist the generated test cases back into an evaluation dataset for future reuse:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset

dataset = create_dataset(name="generated_scenarios")
dataset.merge_records([{"inputs": tc} for tc in test_cases])
```

## Dataset Fields for Test Cases

Each test case stored in the dataset follows the same schema as the test case dictionaries documented on the [[ConversationSimulator]] page.

### Goal

The goal describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open‑ended enough to allow natural dialogue. Good goals describe the expected outcome so the simulator knows when the user’s intent has been accomplished:^[conversation-simulation-databricks-on-aws.md]

```python
# Good goals
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
{"goal": "Understand when to use experiments vs. runs in MLflow"}
{"goal": "Identify and fix why model artifacts aren't being logged"}

# Less effective
{"goal": "Learn about MLflow"}
{"goal": "Get help"}
```

### Persona

The persona shapes how the simulated user communicates. If not specified, a default helpful user persona is used:^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Reduce model serving latency", "persona": "You are a senior ML engineer who asks precise technical questions"}
{"goal": "Set up experiment tracking", "persona": "You are new to MLflow and need step-by-step explanations"}
```

### Context

The context field passes additional parameters to your `predict_fn` via `**kwargs`. Commonly used for personalization or session state:^[conversation-simulation-databricks-on-aws.md]

```python
{
    "goal": "Get personalized model recommendations",
    "context": {
        "user_id": "enterprise_user_42",
        "subscription_tier": "premium",
        "preferred_framework": "pytorch",
    }
}
```

## Experimental Status

Conversation simulation, including evaluation dataset creation and management, is **experimental**. The API and behavior might change in future releases.^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [[Conversation simulation]] – The process of generating synthetic multi‑turn conversations.
- [[MLflow evaluation dataset]] – General‑purpose dataset for persisting evaluation inputs.
- [[ConversationSimulator]] – The simulator that consumes test cases.
- MLflow sessions – The session store that holds production conversation data.
- [[Scorers]] – Evaluation functions that assess simulated conversations.
- [[MLflow 3 for GenAI|MLflow GenAI]] – The broader MLflow framework for generative AI evaluation.

## Sources

- conversation-simulation-databricks-on-aws.md
```

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
