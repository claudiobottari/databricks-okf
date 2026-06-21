---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6b296e857970b0b6c76dbc8a85dd1170e8dc8cfd79dfd96233a529a2f9adb28
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-usage-impact-of-function-calling
    - TUIOFC
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Token Usage Impact of Function Calling
description: Using function calling increases input and output token consumption due to prompt injection and tool definitions, directly affecting billing costs.
tags:
  - billing
  - tokens
  - function-calling
timestamp: "2026-06-19T10:41:06.874Z"
---

## Token Usage Impact of Function Calling

**Token Usage Impact of Function Calling** refers to the increase in input and output token consumption when using function calling (tool use) with large language models. Function calling enhances the reliability of structured outputs but comes with additional token overhead that affects both latency and billing.

### How Function Calling Affects Token Consumption

To improve the quality of tool calls, providers like Databricks apply prompt injection and other techniques behind the scenes. These techniques increase the number of input tokens sent to the model and the number of output tokens generated. The more tools defined in the `tools` parameter, the larger the input token count becomes. ^[function-calling-on-databricks-databricks-on-aws.md]

### Billing Implications

Because token consumption directly determines the cost of model serving (especially in pay-per-token endpoints), increased token usage from function calling results in higher billing. Users should account for this overhead when designing applications that rely on structured tool calls. ^[function-calling-on-databricks-databricks-on-aws.md]

### Best Practices for Managing Token Impact

- **Limit the number of tools.** The source material notes that the maximum number of functions in `tools` is 32, but using fewer tools reduces input token overhead. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Keep JSON schemas simple.** Heavily nested schemas degrade generation quality and may further increase token usage; flatten schemas when possible. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Use single-turn function calling when possible.** Multi-turn calls compound token usage across turns. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Monitor token counts.** Track input and output token usage in your application to estimate costs and tune the number of tools.

### Related Concepts

- [Function Calling on Databricks](/concepts/supported-models-for-function-calling-on-databricks.md)
- [Token-Based Pricing](/concepts/pay-per-token-pricing.md)
- Prompt Injection
- Tool Use with LLMs
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)

### Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
