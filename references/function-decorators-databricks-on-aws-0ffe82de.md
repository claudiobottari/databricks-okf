---
title: Function decorators | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator
ingestedAt: "2026-06-18T08:16:34.936Z"
---

The [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator allows you to create a span for any function. Function decorators provide the simplest path to adding tracing with minimal code changes.

*   MLflow detects the parent-child relationships between functions, making it compatible with auto-tracing integrations.
*   Captures exceptions during function execution and records them as span events.
*   Automatically logs the function's name, inputs, outputs, and execution time.
*   Can be used alongside auto-tracing features.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   MLflow 3
*   MLflow 2.x

This page requires the following packages:

*   `mlflow[databricks]` 3.1 and above: Core MLflow functionality with GenAI features and Databricks connectivity.
*   `openai` 1.0.0 and above: (Optional) Only if your custom code interacts with OpenAI; replace with other SDKs if needed.

Install the basic requirements:

Python

    %pip install --upgrade "mlflow[databricks]>=3.1"# %pip install --upgrade openai>=1.0.0 # Install if needed

## Basic example[​](#basic-example "Direct link to Basic example")

The following code is a minimum example of using the decorator for tracing Python functions.

Decorator Order

To ensure complete observability, the [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator should generally be the outermost one if using multiple decorators. See [Using @mlflow.trace with Other Decorators](#multi-decorator) for a detailed explanation and examples.

Python

    import mlflow@mlflow.trace(span_type="func", attributes={"key": "value"})def add_1(x):    return x + 1@mlflow.trace(span_type="func", attributes={"key1": "value1"})def minus_1(x):    return x - 1@mlflow.trace(name="Trace Test")def trace_test(x):    step1 = add_1(x)    return minus_1(step1)trace_test(4)

![Tracing decorator](https://docs.databricks.com/aws/en/assets/images/trace-decorator-8ae22208121b562582947549f8b9a46e.png)

note

When a trace contains multiple spans with same name, MLflow appends an auto-incrementing suffix to them, such as `_1`, `_2`.

## Customize spans[​](#customize-spans "Direct link to Customize spans")

The [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator accepts following arguments to customize the span to be created:

*   `name` parameter to override the span name from the default (the name of decorated function)
*   `span_type` parameter to set the type of span. Set either one of built-in [Span Types](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts#span-types) or a string.
*   `attributes` parameter to add custom attributes to the span.

Decorator Order

When combining [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) with other decorators (for example from web frameworks), it's crucial for it to be the outermost. For a clear example of correct vs. incorrect ordering, please refer to [Using @mlflow.trace with Other Decorators](#multi-decorator).

Python

    @mlflow.trace(    name="call-local-llm", span_type=SpanType.LLM, attributes={"model": "gpt-4o-mini"})def invoke(prompt: str):    return client.invoke(        messages=[{"role": "user", "content": prompt}], model="gpt-4o-mini"    )

Alternatively, you can update an active or live span dynamically inside the function by using [`mlflow.get_current_active_span`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.get_current_active_span) API.

Python

    @mlflow.trace(span_type=SpanType.LLM)def invoke(prompt: str):    model_id = "gpt-4o-mini"    # Get the current span (created by the @mlflow.trace decorator)    span = mlflow.get_current_active_span()    # Set the attribute to the span    span.set_attributes({"model": model_id})    return client.invoke(messages=[{"role": "user", "content": prompt}], model=model_id)

See [Span tracing with context managers](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/span-tracing) for more examples of editing [`LiveSpan`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.LiveSpan) objects.

## Use `@mlflow.trace` with other decorators[​](#-use-mlflowtrace-with-other-decorators "Direct link to -use-mlflowtrace-with-other-decorators")

When applying multiple decorators to a single function, it's crucial to place [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) as the **outermost** decorator (the one at the very top). This ensures that MLflow can capture the entire execution of the function, including the behavior of any inner decorators.

If [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) is not the outermost decorator, its visibility into the function's execution may be limited or incorrect, potentially leading to incomplete traces or misrepresentation of the function's inputs, outputs, and execution time.

Consider the following conceptual example:

Python

    import mlflowimport functoolsimport time# A hypothetical additional decoratordef simple_timing_decorator(func):    @functools.wraps(func)    def wrapper(*args, **kwargs):        start_time = time.time()        result = func(*args, **kwargs)        end_time = time.time()        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds by simple_timing_decorator.")        return result    return wrapper# Correct order: @mlflow.trace is outermost@mlflow.trace(name="my_decorated_function_correct_order")@simple_timing_decorator# @another_framework_decorator # e.g., @app.route("/mypath") from Flaskdef my_complex_function(x, y):    # Function logic here    time.sleep(0.1) # Simulate work    return x + y# Incorrect order: @mlflow.trace is NOT outermost@simple_timing_decorator@mlflow.trace(name="my_decorated_function_incorrect_order")# @another_framework_decoratordef my_other_complex_function(x, y):    time.sleep(0.1)    return x * y# Example callsif __name__ == "__main__":    print("Calling function with correct decorator order:")    my_complex_function(5, 3)    print("\nCalling function with incorrect decorator order:")    my_other_complex_function(5, 3)

In the `my_complex_function` example (correct order), [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) will capture the full execution, including the time added by `simple_timing_decorator`. In `my_other_complex_function` (incorrect order), the trace captured by MLflow might not accurately reflect the total execution time or could miss modifications to inputs/outputs made by `simple_timing_decorator` before [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) sees them.

Tags can be added to traces to provide additional metadata at the trace level. There are a few different ways to set tags on a trace. Please refer to the [attach custom tags guide](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/attach-tags/) for the other methods.

Python

    @mlflow.tracedef my_func(x):    mlflow.update_current_trace(tags={"fruit": "apple"})    return x + 1

## Customize request and response previews in the UI[​](#customize-request-and-response-previews-in-the-ui "Direct link to Customize request and response previews in the UI")

The Traces tab in the MLflow UI displays a list of traces, and the `Request` and `Response` columns show a preview of the end-to-end input and output of each trace. This allows you to quickly understand what each trace represents.

By default, these previews are truncated to a fixed number of characters. However, you can customize what's shown in these columns by using the `request_preview` and `response_preview` parameters within the `mlflow.update_current_trace()` function. This is particularly useful for complex inputs or outputs where the default truncation might not show the most relevant information.

Below is an example of setting a custom request preview for a trace that processes a long document and user instructions, aiming to render the most relevant information in the UI's `Request` column:

Python

    import mlflow@mlflow.trace(name="Summarization Pipeline")def summarize_document(document_content: str, user_instructions: str):    # Construct a custom preview for the request column    # For example, show beginning of document and user instructions    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."    mlflow.update_current_trace(request_preview=request_p)    # Simulate LLM call    # messages = [    #     {"role": "system", "content": "Summarize the following document based on user instructions."},    #     {"role": "user", "content": f"Document: {document_content}\nInstructions: {user_instructions}"}    # ]    # completion = client.chat.completions.create(model="gpt-4o-mini", messages=messages)    # summary = completion.choices[0].message.content    summary = f"Summary of document starting with '{document_content[:20]}...' based on '{user_instructions}'"    # Customize the response preview    response_p = f"Summary: {summary[:50]}..."    mlflow.update_current_trace(response_preview=response_p)    return summary# Example Calllong_document = "This is a very long document that contains many details about various topics..." * 10instructions = "Focus on the key takeaways regarding topic X."summary_result = summarize_document(long_document, instructions)# print(summary_result)

By setting `request_preview` and `response_preview` on the trace (typically the root span), you control how the overall interaction is summarized in the main trace list view, making it easier to identify and understand traces at a glance.

## Automatic exception handling[​](#automatic-exception-handling "Direct link to Automatic exception handling")

If an `Exception` is raised during processing of a trace-instrumented operation, an indication will be shown within the UI that the invocation was not successful and a partial capture of data will be available to aid in debugging. Additionally, details about the Exception that was raised will be included within `Events` of the partially completed span, further aiding the identification of where issues are occurring within your code.

![Trace Error](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/trace-exception.gif)

## Combine with auto-tracing[​](#combine-with-auto-tracing "Direct link to Combine with auto-tracing")

Manual tracing seamlessly integrates with MLflow's auto-tracing capabilities. See [Combine manual and automatic tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic#combine-manual-automatic).

## Complex workflow tracing[​](#complex-workflow-tracing "Direct link to Complex workflow tracing")

For complex workflows with multiple steps, use nested spans to capture detailed execution flow:

Python

    @mlflow.trace(name="data_pipeline")def process_data_pipeline(data_source: str):    # Extract phase    with mlflow.start_span(name="extract") as extract_span:        raw_data = extract_from_source(data_source)        extract_span.set_outputs({"record_count": len(raw_data)})    # Transform phase    with mlflow.start_span(name="transform") as transform_span:        transformed = apply_transformations(raw_data)        transform_span.set_outputs({"transformed_count": len(transformed)})    # Load phase    with mlflow.start_span(name="load") as load_span:        result = load_to_destination(transformed)        load_span.set_outputs({"status": "success"})    return result

## Multi-threading[​](#multi-threading "Direct link to multi-threading")

MLflow Tracing is thread-safe, traces are isolated by default per thread. But you can also create a trace that spans multiple threads with a few additional steps.

MLflow uses Python's built-in [ContextVar](https://docs.python.org/3/library/contextvars.html) mechanism to ensure thread safety, which is not propagated across threads by default. Therefore, you need to manually copy the context from the main thread to the worker thread, as shown in the example below.

Python

    import contextvarsfrom concurrent.futures import ThreadPoolExecutor, as_completedimport mlflowfrom mlflow.entities import SpanTypeimport openaiclient = openai.OpenAI()# Enable MLflow Tracing for OpenAImlflow.openai.autolog()@mlflow.tracedef worker(question: str) -> str:    messages = [        {"role": "system", "content": "You are a helpful assistant."},        {"role": "user", "content": question},    ]    response = client.chat.completions.create(        model="gpt-4o-mini",        messages=messages,        temperature=0.1,        max_tokens=100,    )    return response.choices[0].message.content@mlflow.tracedef main(questions: list[str]) -> list[str]:    results = []    # Almost same as how you would use ThreadPoolExecutor, but two additional steps    #  1. Copy the context in the main thread using copy_context()    #  2. Use ctx.run() to run the worker in the copied context    with ThreadPoolExecutor(max_workers=2) as executor:        futures = []        for question in questions:            ctx = contextvars.copy_context()            futures.append(executor.submit(ctx.run, worker, question))        for future in as_completed(futures):            results.append(future.result())    return resultsquestions = [    "What is the capital of France?",    "What is the capital of Germany?",]main(questions)

![Multi threaded tracing](https://docs.databricks.com/aws/en/assets/images/tracing-multi-thread-acfb6f382ce45e030c95b7c0536749bf.png)

tip

In contrast, `ContextVar` is copied to **async** tasks by default. Therefore, you don't need to manually copy the context when using `asyncio`, which might be an easier way to handle concurrent I/O-bound tasks in Python with MLflow Tracing.

## Streaming outputs[​](#streaming-outputs "Direct link to Streaming outputs")

The [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator can be used to trace functions that return a generator or an iterator, since MLflow 2.20.2.

Python

    @mlflow.tracedef stream_data():    for i in range(5):        yield i

The above example will generate a trace with a single span for the `stream_data` function. By default, MLflow will capture all elements yielded by the generator as a list in the span's output. In the example above, the output of the span will be `[0, 1, 2, 3, 4]`.

note

A span for a stream function will start when the returned iterator starts to be **consumed**, and will end when the iterator is exhausted, or an exception is raised during the iteration.

### Using output reducers[​](#using-output-reducers "Direct link to Using output reducers")

If you want to aggregate the elements to be a single span output, you can use the `output_reducer` parameter to specify a custom function to aggregate the elements. The custom function should take a list of yielded elements as inputs.

Python

    from typing import List, Any@mlflow.trace(output_reducer=lambda x: ",".join(x))def stream_data():    for c in "hello":        yield c

In the example above, the output of the span will be `"h,e,l,l,o"`. The raw chunks can still be found in the `Events` tab of the span in the MLflow Trace UI, allowing you to inspect individual yielded values when debugging.

### Common output reducer patterns[​](#common-output-reducer-patterns "Direct link to Common output reducer patterns")

Here are some common patterns for implementing output reducers:

#### Token aggregation[​](#token-aggregation "Direct link to Token aggregation")

Python

    from typing import List, Dict, Anydef aggregate_tokens(chunks: List[str]) -> str:    """Concatenate streaming tokens into complete text"""    return "".join(chunks)@mlflow.trace(output_reducer=aggregate_tokens)def stream_text():    for word in ["Hello", " ", "World", "!"]:        yield word

#### Metrics aggregation[​](#metrics-aggregation "Direct link to Metrics aggregation")

Python

    def aggregate_metrics(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:    """Aggregate streaming metrics into summary statistics"""    values = [c["value"] for c in chunks if "value" in c]    return {        "count": len(values),        "sum": sum(values),        "average": sum(values) / len(values) if values else 0,        "max": max(values) if values else None,        "min": min(values) if values else None    }@mlflow.trace(output_reducer=aggregate_metrics)def stream_metrics():    for i in range(10):        yield {"value": i * 2, "timestamp": time.time()}

#### Error collection[​](#error-collection "Direct link to Error collection")

Python

    def collect_results_and_errors(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:    """Separate successful results from errors"""    results = []    errors = []    for chunk in chunks:        if chunk.get("error"):            errors.append(chunk["error"])        else:            results.append(chunk.get("data"))    return {        "results": results,        "errors": errors,        "success_rate": len(results) / len(chunks) if chunks else 0,        "has_errors": len(errors) > 0    }

## Advanced example: OpenAI streaming[​](#advanced-example-openai-streaming "Direct link to Advanced example: OpenAI streaming")

The following is an advanced example that uses the `output_reducer` to consolidate ChatCompletionChunk output from an OpenAI LLM into a single message object.

tip

We recommend using the [auto-tracing for OpenAI](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/openai) for production use cases, which handles this automatically. The example below is for demonstration purposes.

Python

    import mlflowimport openaifrom openai.types.chat import *from typing import Optionaldef aggregate_chunks(outputs: list[ChatCompletionChunk]) -> Optional[ChatCompletion]:    """Consolidate ChatCompletionChunks to a single ChatCompletion"""    if not outputs:        return None    first_chunk = outputs[0]    delta = first_chunk.choices[0].delta    message = ChatCompletionMessage(        role=delta.role, content=delta.content, tool_calls=delta.tool_calls or []    )    finish_reason = first_chunk.choices[0].finish_reason    for chunk in outputs[1:]:        delta = chunk.choices[0].delta        message.content += delta.content or ""        message.tool_calls += delta.tool_calls or []        finish_reason = finish_reason or chunk.choices[0].finish_reason    base = ChatCompletion(        id=first_chunk.id,        choices=[Choice(index=0, message=message, finish_reason=finish_reason)],        created=first_chunk.created,        model=first_chunk.model,        object="chat.completion",    )    return base@mlflow.trace(output_reducer=aggregate_chunks)def predict(messages: list[dict]):    client = openai.OpenAI()    stream = client.chat.completions.create(        model="gpt-4o-mini",        messages=messages,        stream=True,    )    for chunk in stream:        yield chunkfor chunk in predict([{"role": "user", "content": "Hello"}]):    print(chunk)

In the example above, the generated `predict` span will have a single chat completion message as the output, which is aggregated by the custom reducer function.

### Real-world use cases[​](#real-world-use-cases "Direct link to Real-world use cases")

Here are additional examples of output reducers for common GenAI scenarios:

#### LLM response with JSON parsing[​](#llm-response-with-json-parsing "Direct link to LLM response with JSON parsing")

Python

    from typing import List, Dict, Anyimport jsondef parse_json_from_llm(content: str) -> str:    """Extract and clean JSON from LLM responses that may include markdown"""    # Remove common markdown code block wrappers    if content.startswith("```json") and content.endswith("```"):        content = content[7:-3]  # Remove ```json prefix and ``` suffix    elif content.startswith("```") and content.endswith("```"):        content = content[3:-3]  # Remove generic ``` wrappers    return content.strip()def json_stream_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:    """Aggregate LLM streaming output and parse JSON response"""    full_content = ""    metadata = {}    errors = []    # Process different chunk types    for chunk in chunks:        chunk_type = chunk.get("type", "content")        if chunk_type == "content" or chunk_type == "token":            full_content += chunk.get("content", "")        elif chunk_type == "metadata":            metadata.update(chunk.get("data", {}))        elif chunk_type == "error":            errors.append(chunk.get("error"))    # Return early if errors occurred    if errors:        return {            "status": "error",            "errors": errors,            "raw_content": full_content,            **metadata        }    # Try to parse accumulated content as JSON    try:        cleaned_content = parse_json_from_llm(full_content)        parsed_data = json.loads(cleaned_content)        return {            "status": "success",            "data": parsed_data,            "raw_content": full_content,            **metadata        }    except json.JSONDecodeError as e:        return {            "status": "parse_error",            "error": f"Failed to parse JSON: {str(e)}",            "raw_content": full_content,            **metadata        }@mlflow.trace(output_reducer=json_stream_reducer)def generate_structured_output(prompt: str, schema: dict):    """Generate structured JSON output from an LLM"""    # Simulate streaming JSON generation    yield {"type": "content", "content": '{"name": "John", '}    yield {"type": "content", "content": '"email": "john@example.com", '}    yield {"type": "content", "content": '"age": 30}'}    # Add metadata    trace_id = mlflow.get_current_active_span().request_id if mlflow.get_current_active_span() else None    yield {"type": "metadata", "data": {"trace_id": trace_id, "model": "gpt-4"}}

#### Structured output generation with OpenAI[​](#structured-output-generation-with-openai "Direct link to Structured output generation with OpenAI")

Here's a complete example of using output reducers with OpenAI to generate and parse structured JSON responses:

Python

    import jsonimport mlflowimport openaifrom typing import List, Dict, Any, Optionaldef structured_output_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:    """    Aggregate streaming chunks into structured output with comprehensive error handling.    Handles token streaming, metadata collection, and JSON parsing.    """    content_parts = []    trace_id = None    model_info = None    errors = []    for chunk in chunks:        chunk_type = chunk.get("type", "token")        if chunk_type == "token":            content_parts.append(chunk.get("content", ""))        elif chunk_type == "trace_info":            trace_id = chunk.get("trace_id")            model_info = chunk.get("model")        elif chunk_type == "error":            errors.append(chunk.get("message"))    # Join all content parts    full_content = "".join(content_parts)    # Base response    response = {        "trace_id": trace_id,        "model": model_info,        "raw_content": full_content    }    # Handle errors    if errors:        response["status"] = "error"        response["errors"] = errors        return response    # Try to extract and parse JSON    try:        # Clean markdown wrappers if present        json_content = full_content.strip()        if json_content.startswith("```json") and json_content.endswith("```"):            json_content = json_content[7:-3].strip()        elif json_content.startswith("```") and json_content.endswith("```"):            json_content = json_content[3:-3].strip()        parsed_data = json.loads(json_content)        response["status"] = "success"        response["data"] = parsed_data    except json.JSONDecodeError as e:        response["status"] = "parse_error"        response["error"] = f"JSON parsing failed: {str(e)}"        response["error_position"] = e.pos if hasattr(e, 'pos') else None    return response@mlflow.trace(output_reducer=structured_output_reducer)async def generate_customer_email(    customer_name: str,    issue: str,    sentiment: str = "professional") -> None:    """    Generate a structured customer service email response.    Demonstrates real-world streaming with OpenAI and structured output parsing.    """    client = openai.AsyncOpenAI()    system_prompt = """You are a customer service assistant. Generate a professional email response in JSON format:    {        "subject": "email subject line",        "greeting": "personalized greeting",        "body": "main email content addressing the issue",        "closing": "professional closing",        "priority": "high|medium|low"    }"""    user_prompt = f"Customer: {customer_name}\nIssue: {issue}\nTone: {sentiment}"    try:        # Stream the response        stream = await client.chat.completions.create(            model="gpt-4o-mini",            messages=[                {"role": "system", "content": system_prompt},                {"role": "user", "content": user_prompt}            ],            stream=True,            temperature=0.7        )        # Yield streaming tokens        async for chunk in stream:            if chunk.choices[0].delta.content:                yield {                    "type": "token",                    "content": chunk.choices[0].delta.content                }        # Add trace metadata        if current_span := mlflow.get_current_active_span():            yield {                "type": "trace_info",                "trace_id": current_span.request_id,                "model": "gpt-4o-mini"            }    except Exception as e:        yield {            "type": "error",            "message": f"OpenAI API error: {str(e)}"        }# Example usageasync def main():    # This will automatically aggregate the streamed output into structured JSON    async for chunk in generate_customer_email(        customer_name="John Doe",        issue="Product arrived damaged",        sentiment="empathetic"    ):        # In practice, you might send these chunks to a frontend        print(chunk.get("content", ""), end="", flush=True)

Integration Benefits

This example showcases several real-world patterns:

*   **Streaming UI updates**: Tokens can be displayed as they arrive
*   **Structured output validation**: JSON parsing ensures response format
*   **Error resilience**: Handles API errors and parsing failures gracefully
*   **Trace correlation**: Links streaming output to MLflow traces for debugging

#### Multi-model response aggregation[​](#multi-model-response-aggregation "Direct link to Multi-model response aggregation")

Python

    def multi_model_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:    """Aggregate responses from multiple models"""    responses = {}    latencies = {}    for chunk in chunks:        model = chunk.get("model")        if model:            responses[model] = chunk.get("response", "")            latencies[model] = chunk.get("latency", 0)    return {        "responses": responses,        "latencies": latencies,        "fastest_model": min(latencies, key=latencies.get) if latencies else None,        "consensus": len(set(responses.values())) == 1    }

### Testing output reducers[​](#testing-output-reducers "Direct link to Testing output reducers")

Output reducers can be tested independently of the tracing framework, making it easy to ensure they handle edge cases correctly:

Python

    import unittestfrom typing import List, Dict, Anydef my_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:    """Example reducer to be tested"""    if not chunks:        return {"status": "empty", "total": 0}    total = sum(c.get("value", 0) for c in chunks)    errors = [c for c in chunks if c.get("error")]    return {        "status": "error" if errors else "success",        "total": total,        "count": len(chunks),        "average": total / len(chunks) if chunks else 0,        "error_count": len(errors)    }class TestOutputReducer(unittest.TestCase):    def test_normal_case(self):        chunks = [            {"value": 10},            {"value": 20},            {"value": 30}        ]        result = my_reducer(chunks)        self.assertEqual(result["status"], "success")        self.assertEqual(result["total"], 60)        self.assertEqual(result["average"], 20.0)    def test_empty_input(self):        result = my_reducer([])        self.assertEqual(result["status"], "empty")        self.assertEqual(result["total"], 0)    def test_error_handling(self):        chunks = [            {"value": 10},            {"error": "Network timeout"},            {"value": 20}        ]        result = my_reducer(chunks)        self.assertEqual(result["status"], "error")        self.assertEqual(result["total"], 30)        self.assertEqual(result["error_count"], 1)    def test_missing_values(self):        chunks = [            {"value": 10},            {"metadata": "some info"},  # No value field            {"value": 20}        ]        result = my_reducer(chunks)        self.assertEqual(result["total"], 30)        self.assertEqual(result["count"], 3)

Performance Considerations

*   Output reducers receive all chunks in memory at once. For very large streams, consider implementing streaming alternatives or chunking strategies.
*   The span remains open until the generator is fully consumed, which impacts latency metrics.
*   Reducers should be stateless and avoid side effects for predictable behavior.

## Supported function types[​](#supported-function-types "Direct link to Supported function types")

The [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) decorator currently supports the following types of functions:

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Span Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/span-tracing) - Trace specific code blocks with more granular control
*   [Low-Level Client APIs](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/low-level-api) - Learn advanced scenarios requiring full control
*   [Debug & observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Use your manually traced app for debugging
