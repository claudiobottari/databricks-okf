---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96c9bd3b84a0747a869a263a20bbe495097e0ce152aaac72324c771827a4b7be
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-evaluation-dataset-design
    - AEDD
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: create-a-custom-judge-using_make_judge-databricks-on-aws.md
title: Agent Evaluation Dataset Design
description: Evaluation datasets for GenAI agents consist of input message histories and optional `expectations` dictionaries that define expected agent behaviors, enabling both input/output evaluation and correctness checking.
tags:
  - mlflow
  - genai
  - testing
  - datasets
timestamp: "2026-06-18T11:12:55.713Z"
---

# Agent Evaluation Dataset Design

**Agent Evaluation Dataset Design** refers to the process of constructing structured input datasets — typically conversation histories, expected outcomes, and metadata — that are used to evaluate the quality, correctness, and safety of GenAI agents through automated scoring and [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) evaluation. A well-designed evaluation dataset is foundational for obtaining reliable, repeatable assessment of agent behavior across different configurations, prompts, or system variants.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Dataset Structure

An agent evaluation dataset consists of one or more test cases, each represented as a dictionary (or row in a table) containing fields that the evaluation framework feeds into the agent function and the scoring judges.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Core Fields

| Field | Description |
|---|---|
| `inputs` | Conversation history passed to the agent. Typically a list of message dicts with `role` and `content` keys. Required. |
| `expectations` (optional) | Ground-truth or expected behaviors against which judges compare the agent's outputs. The schema is application-defined. |

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Inputs Field

The `inputs` field contains the conversation messages that the agent receives. Each message follows a standard chat format:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
{
    "inputs": {
        "messages": [
            {"role": "system", "content": "..."},        # Optional system prompt
            {"role": "user", "content": "..."},          # User turns
            {"role": "assistant", "content": "..."},     # Previous assistant turns (if multi-turn)
            {"role": "user", "content": "..."},          # Latest user query
        ]
    }
}
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
```

Multi-turn conversations are supported by including previous assistant and user messages as part of the history. The agent function processes this list and generates a response for the latest user turn.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Expectations Field

The `expectations` field is an optional dictionary that encodes what the agent should or should not do. Judges can reference these expectations in their instructions to check for specific behaviors.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
"expectations": {
    "should_provide_pricing": True,
    "should_offer_alternatives": True,
    "should_mention_return_policy": True,
}
```

The expectations schema is free-form; it should be designed to match the criteria that your [Custom Judges](/concepts/custom-judges.md) are instructed to check.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Designing Test Cases

### Cover Edge Cases and Negatives

Include test cases that exercise both expected behavior and failure modes. A dataset that only contains successful interactions will not reveal regressions or weaknesses in the agent. For example, include queries that:

- The agent handles well (to confirm no regression)
- The agent should not handle well (to measure degradation awareness)
- Require tool calls (to validate tool selection)
- Involve frustrated or escalated users (to test tone and handling)^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Toggle Agent Configurations

Design the dataset so it can be evaluated against multiple agent configurations. By keeping the dataset fixed and varying the agent's system prompt, model, or toolset, you can compare judge scores across configurations to identify which changes improve or degrade performance.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example Evaluation Dataset

The following example from a customer support evaluation shows a dataset with four test cases covering pricing questions, return policy queries, account troubleshooting, and frustrated user scenarios:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"},
            ],
        },
        "expectations": {
            "should_provide_pricing": True,
            "should_offer_alternatives": True,
        },
    },
    {
        "inputs": {
            "messages": [
                {
                    "role": "user",
                    "content": "Can I return the microwave I bought 2 months ago?",
                },
            ],
        },
        "expectations": {
            "should_mention_return_policy": True,
            "should_ask_for_receipt": False,
        },
    },
    {
        "inputs": {
            "messages": [
                {
                    "role": "user",
                    "content": "I'm having trouble with my account. I can't log in.",
                },
                {
                    "role": "assistant",
                    "content": "I'm sorry to hear that. Are you using our website or mobile app?",
                },
                {"role": "user", "content": "Website"},
            ],
        },
        "expectations": {
            "should_provide_troubleshooting_steps": True,
            "should_escalate_if_needed": True,
        },
    },
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "I'm having trouble logging in."},
                {"role": "assistant", "content": "Are you using the website or app?"},
                {"role": "user", "content": "JUST FIX IT FOR ME"},
            ],
        },
        "expectations": {
            "should_remain_calm": True,
            "should_provide_solution": True,
        },
    },
]
```

## Best Practices

### Separate Inputs from Expected Behaviors

Keep `inputs` focused on the conversation that the agent receives. Place what the agent should do (or not do) in a separate field like `expectations`, rather than encoding expected behaviors in the conversation messages themselves. This separation allows judges to compare actual outputs against explicit criteria.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Include Multi-Turn Conversations

Real-world agent interactions are rarely single-turn. Include test cases with multiple user and assistant turns to evaluate the agent's ability to maintain context, follow conversational flow, and handle corrections or follow-ups.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Align Judge Instructions with Dataset Fields

When designing [Custom Judges](/concepts/custom-judges.md), reference the fields in your dataset. Judges can use `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, and `{{ trace }}` template variables to access evaluation data. If your `expectations` field contains custom keys like `should_remain_calm`, write judge instructions that reference those keys explicitly.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Version Your Dataset

Evaluation datasets should be versioned alongside the agent code. When the agent's behavior changes (due to prompt updates, model changes, or tool additions), the fixed dataset provides a stable benchmark for before-and-after comparison.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Using the Dataset

Evaluation datasets are consumed by [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) via [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate). The function passes each `inputs` to the agent's `predict_fn`, collects the agent's outputs, and then passes the inputs, outputs, expectations, and optional traces to each scorer (judge) in the `scorers` list.^[create-a-custom-judge-using_make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)
```

The same dataset can be evaluated multiple times against different agent configurations to produce comparative scores.^[create-a-custom-judge-using_make_judge-databricks-on-aws.md]

## Related Concepts

- Custom Judges (make_judge)|Custom judges using make_judge() — Creating LLM-based judges that score agent outputs
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework that consumes evaluation datasets
- [Trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) — Judges that analyze execution traces for tool usage patterns
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying evaluation datasets for continuous monitoring
- Align judges with human feedback — Improving judge accuracy over time
- Feedback (MLflow) — The structured output from judges
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Required when evaluation uses serverless compute

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
2. create-a-custom-judge-using_make_judge-databricks-on-aws.md
