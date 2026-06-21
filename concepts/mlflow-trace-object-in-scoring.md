---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 770853098467e42c0cf892df5adddfb625bec825e4c0e0bdb45936925032b55c
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-object-in-scoring
    - MTOIS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Trace object in scoring
description: Accessing full MLflow Trace objects within custom scorers to retrieve spans, timing, inputs, outputs, and attributes for fine-grained metric calculation.
tags:
  - mlflow
  - tracing
  - scorers
  - monitoring
timestamp: "2026-06-18T14:36:33.898Z"
---

# MLflow Trace Object in Scoring

The **MLflow Trace object** captures the full execution record of a GenAI agent call, providing structured access to spans, inputs, outputs, attributes, and timing information. In MLflow Evaluation for GenAI, the Trace object enables fine-grained metrics that go beyond simple input/output analysis, such as measuring response latency or validating tool usage sequences.

## Using the Trace in Code-Based Scorers

Custom code-based scorers can receive the Trace object as a parameter, allowing direct inspection of the agent’s execution internals. The Trace object is an instance of `mlflow.entities.Trace`. Within a scorer function, you can search for specific spans by type — for example, `SpanType.CHAT_MODEL` — and access their start and end times to compute performance metrics. ^[code-based-scorer-examples-databricks-on-aws.md]

The following example checks whether the LLM response time falls within an acceptable limit: ^[code-based-scorer-examples-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import scorer
from mlflow.entities import Trace, Feedback, SpanType

@scorer
def llm_response_time_good(trace: Trace) -> Feedback:
    llm_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]
    response_time = (llm_span.end_time_ns - llm_span.start_time_ns) / 1e9
    max_duration = 5.0
    if response_time <= max_duration:
        return Feedback(
            value="yes",
            rationale=f"LLM response time {response_time:.2f}s is within the {max_duration}s limit."
        )
    else:
        return Feedback(
            value="no",
            rationale=f"LLM response time {response_time:.2f}s exceeds the {max_duration}s limit."
        )
```

In addition to accessing timing, you can retrieve any span attribute, input, or output from the Trace, enabling custom calculations like token usage counts or intermediate reasoning checks. ^[code-based-scorer-examples-databricks-on-aws.md]

When evaluating pre‑existing traces — for example, those retrieved via `mlflow.search_traces()` — the returned DataFrame includes a `trace` column that can be passed directly to scorers expecting a Trace parameter. ^[code-based-scorer-examples-databricks-on-aws.md]

## Using the Trace in LLM Judges

Trace-based [judges](/concepts/llm-judges.md) evaluate the full execution record of an agent call, including tool invocations, intermediate reasoning steps, and their results. To create a trace-based judge, include the `{{ trace }}` placeholder in the judge’s instructions. Unlike code-based scorers, trace-based judges are LLM-driven and require a model specification. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Example from an A/B comparison scenario: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

This approach is particularly useful for validating that an agent followed the correct decision path or used the expected tools, rather than just checking the final output. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The framework that produces and stores Trace objects.
- [Code-based Scorers](/concepts/code-based-scorers.md) — Python functions that accept Trace and return Feedback.
- [Trace-based Judges](/concepts/trace-based-judges.md) — LLM judges that analyze the full Trace.
- Span — A unit of work within a Trace (e.g., an LLM call or tool invocation).
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The offline evaluation API that supports both code-based and LLM judges.

## Sources

- code-based-scorer-examples-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
