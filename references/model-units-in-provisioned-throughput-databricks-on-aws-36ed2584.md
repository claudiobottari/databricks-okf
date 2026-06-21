---
title: Model units in provisioned throughput | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/model-units
ingestedAt: "2026-06-18T08:11:09.350Z"
---

Model units are a unit of throughput which determine how much work your endpoint can handle per minute. When you create a new [provisioned throughput endpoint](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis), you specify how many model units to provision for each model served.

The amount of work required to process each request to your endpoint depends on the size of both the input and the generated output. As the number of input and output tokens increases, the amount of work required to process a request also increases. Generating output tokens is more resource-intensive than processing input tokens. The work required for each request grows in a non-linear fashion as the input or output token counts increase, meaning that for a given amount of model units, your endpoint can handle either:

*   **Multiple small requests** at a time.
*   **Fewer long-context requests** at a time before it runs out of capacity.

For example, with a medium-sized workload with 3500 input tokens and 300 output tokens, you can estimate the tokens per second throughput for a given number of model units:

Model

Model Units

Estimated Tokens per Second

Llama 4 Maverick

50

3250

## Models that use model units[​](#models-that-use-model-units "Direct link to Models that use model units")

All [foundation models supported for provisioned throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) provision inference capacity using _model units_, with the exception of the legacy models listed below.

note

Model serving endpoints that serve models from the following legacy model families provision inference capacity based on tokens per second ranges configured during [endpoint creation](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis):

*   Meta Llama 3.3
*   Meta Llama 3.2 3B
*   Meta Llama 3.2 1B
*   Meta Llama 3.1
*   GTE v1.5 (English)
*   BGE v1.5 (English)
*   DeepSeek R1 (not available in Unity Catalog)
*   Meta Llama 3
*   Meta Llama 2
*   DBRX
*   Mistral
*   Mixtral
*   MPT
