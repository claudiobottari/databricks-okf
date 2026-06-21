---
title: Query reasoning models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-reason-models
ingestedAt: "2026-06-18T08:12:36.657Z"
---

In this article, you learn how to write query requests for foundation models optimized for reasoning tasks, and send them to your Foundation Model API endpoint.

Databricks Foundation Model API provides a unified API to interact with all Foundation Models, including reasoning models. Reasoning gives foundation models enhanced capabilities to tackle complex tasks. Some models also provide transparency by revealing their step-by-step thought process before delivering a final answer.

## Types of reasoning models[​](#types-of-reasoning-models "Direct link to Types of reasoning models")

There are two types of models, reasoning-only and hybrid. The following table describes how different models use different approaches to control reasoning:

## Query examples[​](#query-examples "Direct link to Query examples")

All reasoning models are accessed through the [chat completions](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models#query-chat) endpoint.

*   Claude model example
*   GPT-5.1
*   GPT OSS model example
*   Gemini model example

Python

    import osfrom openai import OpenAIclient = OpenAI(  api_key=os.environ.get('YOUR_DATABRICKS_TOKEN'),  base_url=os.environ.get('YOUR_DATABRICKS_BASE_URL')  )response = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[{"role": "user", "content": "Why is the sky blue?"}],    max_tokens=20480,    extra_body={        "thinking": {            "type": "enabled",            "budget_tokens": 10240        }    })msg = response.choices[0].messagereasoning = msg.content[0]["summary"][0]["text"]answer = msg.content[1]["text"]print("Reasoning:", reasoning)print("Answer:", answer)

The API response includes both thinking and text content blocks:

Python

    ChatCompletionMessage(    role="assistant",    content=[        {            "type": "reasoning",            "summary": [                {                    "type": "summary_text",                    "text": ("The question is asking about the scientific explanation for why the sky appears blue... "),                    "signature": ("EqoBCkgIARABGAIiQAhCWRmlaLuPiHaF357JzGmloqLqkeBm3cHG9NFTxKMyC/9bBdBInUsE3IZk6RxWge...")                }            ]        },        {            "type": "text",            "text": (                "# Why the Sky Is Blue\n\n"                "The sky appears blue because of a phenomenon called Rayleigh scattering. Here's how it works..."            )        }    ],    refusal=None,    annotations=None,    audio=None,    function_call=None,    tool_calls=None)

## Manage reasoning across multiple turns[​](#manage-reasoning-across-multiple-turns "Direct link to Manage reasoning across multiple turns")

This section is specific to the `databricks-claude-sonnet-4-5` model.

In multi-turn conversations, only the reasoning blocks associated with the last assistant turn or tool-use session are visible to the model and counted as input tokens.

If you don't want to pass reasoning tokens back to the model (for example, you don't need it to reason over its prior steps), you can omit the reasoning block entirely. For example:

Python

    response = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[        {"role": "user", "content": "Why is the sky blue?"},        {"role": "assistant", "content": text_content},        {"role": "user", "content": "Can you explain in a way that a 5-year-old child can understand?"}    ],    max_tokens=20480,    extra_body={        "thinking": {            "type": "enabled",            "budget_tokens": 10240        }    })answer = response.choices[0].message.content[1]["text"]print("Answer:", answer)

However, if you do need the model to reason over its previous reasoning process - for instance, if you're building experiences that surface its intermediate reasoning - you must include the full, unmodified assistant message, including the reasoning block from the previous turn. Here's how to continue a thread with the full assistant message:

Python

    assistant_message = response.choices[0].messageresponse = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[        {"role": "user", "content": "Why is the sky blue?"},        {"role": "assistant", "content": text_content},        {"role": "user", "content": "Can you explain in a way that a 5-year-old child can understand?"},        assistant_message,        {"role": "user", "content": "Can you simplify the previous answer?"}    ],    max_tokens=20480,    extra_body={        "thinking": {            "type": "enabled",            "budget_tokens": 10240        }    })answer = response.choices[0].message.content[1]["text"]print("Answer:", answer)

## How does a reasoning model work?[​](#how-does-a-reasoning-model-work "Direct link to How does a reasoning model work?")

Reasoning models introduce special reasoning tokens in addition to the standard input and output tokens. These tokens let the model "think" through the prompt, breaking it down and considering different ways to respond. After this internal reasoning process, the model generates its final answer as visible output tokens. Some models, like `databricks-claude-sonnet-4-5`, display these reasoning tokens to users, while others, such as the OpenAI o series, discard them and do not expose them in the final output.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query an embedding model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-embedding-models).
*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).
*   [Query vision models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-vision-models).
