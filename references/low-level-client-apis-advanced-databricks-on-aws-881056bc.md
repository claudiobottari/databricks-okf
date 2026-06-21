---
title: Low-level client APIs (advanced) | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/low-level-api
ingestedAt: "2026-06-18T08:16:37.273Z"
---

The [`MlflowClient`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient) APIs provide direct, fine-grained control over trace lifecycle management. While the [Function Decorator APIs](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator) handle most use cases elegantly, client APIs are essential for advanced scenarios requiring explicit control over trace creation, custom trace IDs, or integration with existing observability systems.

## When to use client APIs[​](#when-to-use-client-apis "Direct link to When to use client APIs")

**Use client APIs for:**

*   Custom trace ID generation schemes
*   Integration with existing trace systems
*   Complex trace lifecycle management
*   Advanced span hierarchies
*   Custom trace state management

**Avoid Client APIs for:**

*   Simple function tracing (use `@mlflow.trace`)
*   Local Python applications (use context managers)
*   Quick prototyping (use high-level APIs)
*   Integration with auto-tracing

## Core concepts[​](#core-concepts "Direct link to Core concepts")

### Trace lifecycle[​](#trace-lifecycle "Direct link to Trace lifecycle")

Every trace follows a strict lifecycle that must be managed explicitly:

Mermaid

    graph LR    A[Start Trace] --> B[Start Span 1]    B --> C[Start Span 2]    C --> D[End Span 2]    D --> E[End Span 1]    E --> F[End Trace]

important

Every `start_trace` or `start_span` call must have a corresponding `end_trace` or `end_span` call. Failing to close spans will result in incomplete traces.

### Key identifiers[​](#key-identifiers "Direct link to Key identifiers")

Understanding these identifiers is crucial for client API usage:

## Getting started[​](#getting-started "Direct link to Getting started")

### Initialize the client[​](#initialize-the-client "Direct link to Initialize the client")

Python

    from mlflow import MlflowClient# Initialize client with default tracking URIclient = MlflowClient()# Or specify a custom tracking URIclient = MlflowClient(tracking_uri="databricks")

### Start a trace[​](#start-a-trace "Direct link to Start a trace")

Unlike high-level APIs, you must explicitly start a trace before adding spans using [`client.start_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.start_trace):

Python

    # Start a new trace - this creates the root spanroot_span = client.start_trace(    name="my_application_flow",    inputs={"user_id": "123", "action": "generate_report"},    attributes={"environment": "production", "version": "1.0.0"})# Extract the request_id for subsequent operationsrequest_id = root_span.request_idprint(f"Started trace with ID: {request_id}")

### Add child spans[​](#add-child-spans "Direct link to Add child spans")

Create a hierarchy of spans using [`client.start_span()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.start_span) to represent your application's workflow:

Python

    # Create a child span for data retrievaldata_span = client.start_span(    name="fetch_user_data",    request_id=request_id,  # Links to the trace    parent_id=root_span.span_id,  # Creates parent-child relationship    inputs={"user_id": "123"},    attributes={"database": "users_db", "query_type": "select"})# Create a sibling span for processingprocess_span = client.start_span(    name="process_data",    request_id=request_id,    parent_id=root_span.span_id,  # Same parent as data_span    inputs={"data_size": "1024KB"},    attributes={"processor": "gpu", "batch_size": 32})

### End spans[​](#end-spans "Direct link to End spans")

End spans using [`client.end_span()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.end_span) in reverse order of creation (LIFO - Last In, First Out):

Python

    # End the data retrieval spanclient.end_span(    request_id=data_span.request_id,    span_id=data_span.span_id,    outputs={"record_count": 42, "cache_hit": True},    attributes={"duration_ms": 150})# End the processing spanclient.end_span(    request_id=process_span.request_id,    span_id=process_span.span_id,    outputs={"processed_records": 42, "errors": 0},    status="OK")

### End a trace[​](#end-a-trace "Direct link to End a trace")

Complete the trace by ending the root span using [`client.end_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.end_trace):

Python

    # End the root span (completes the trace)client.end_trace(    request_id=request_id,    outputs={"report_url": "https://example.com/report/123"},    attributes={"total_duration_ms": 1250, "status": "success"})

## Practical examples[​](#practical-examples "Direct link to Practical examples")

### Example 1: Error handling[​](#example-1-error-handling "Direct link to Example 1: Error handling")

Proper error handling ensures traces are completed even when exceptions occur:

Python

    def traced_operation():    client = MlflowClient()    root_span = None    try:        # Start trace        root_span = client.start_trace("risky_operation")        # Start child span        child_span = client.start_span(            name="database_query",            request_id=root_span.request_id,            parent_id=root_span.span_id        )        try:            # Risky operation            result = perform_database_query()            # End child span on success            client.end_span(                request_id=child_span.request_id,                span_id=child_span.span_id,                outputs={"result": result},                status="OK"            )        except Exception as e:            # End child span on error            client.end_span(                request_id=child_span.request_id,                span_id=child_span.span_id,                status="ERROR",                attributes={"error": str(e)}            )            raise    except Exception as e:        # Log error to trace        if root_span:            client.end_trace(                request_id=root_span.request_id,                status="ERROR",                attributes={"error_type": type(e).__name__, "error_message": str(e)}            )        raise    else:        # End trace on success        client.end_trace(            request_id=root_span.request_id,            outputs={"status": "completed"},            status="OK"        )

### Example 2: Custom trace management[​](#example-2-custom-trace-management "Direct link to Example 2: Custom trace management")

Implement custom trace ID generation and management for integration with existing systems:

Python

    import uuidfrom datetime import datetimeclass CustomTraceManager:    """Custom trace manager with business-specific trace IDs"""    def __init__(self):        self.client = MlflowClient()        self.active_traces = {}    def generate_trace_id(self, user_id: str, operation: str) -> str:        """Generate custom trace ID based on business logic"""        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")        return f"{user_id}_{operation}_{timestamp}_{uuid.uuid4().hex[:8]}"    def start_custom_trace(self, user_id: str, operation: str, **kwargs):        """Start trace with custom ID format"""        trace_name = self.generate_trace_id(user_id, operation)        root_span = self.client.start_trace(            name=trace_name,            attributes={                "user_id": user_id,                "operation": operation,                "custom_trace_id": trace_name,                **kwargs            }        )        self.active_traces[trace_name] = root_span        return root_span    def get_active_trace(self, trace_name: str):        """Retrieve active trace by custom name"""        return self.active_traces.get(trace_name)# Usagemanager = CustomTraceManager()trace = manager.start_custom_trace(    user_id="user123",    operation="report_generation",    report_type="quarterly")

### Example 3: Batch processing with nested spans[​](#example-3-batch-processing-with-nested-spans "Direct link to Example 3: Batch processing with nested spans")

Track complex workflows with multiple levels of nesting:

Python

    def batch_processor(items):    client = MlflowClient()    # Start main trace    root = client.start_trace(        name="batch_processing",        inputs={"batch_size": len(items)}    )    results = []    # Process each item    for i, item in enumerate(items):        # Create span for each item        item_span = client.start_span(            name=f"process_item_{i}",            request_id=root.request_id,            parent_id=root.span_id,            inputs={"item_id": item["id"]}        )        try:            # Validation span            validation_span = client.start_span(                name="validate",                request_id=root.request_id,                parent_id=item_span.span_id            )            is_valid = validate_item(item)            client.end_span(                request_id=validation_span.request_id,                span_id=validation_span.span_id,                outputs={"is_valid": is_valid}            )            if is_valid:                # Processing span                process_span = client.start_span(                    name="transform",                    request_id=root.request_id,                    parent_id=item_span.span_id                )                result = transform_item(item)                results.append(result)                client.end_span(                    request_id=process_span.request_id,                    span_id=process_span.span_id,                    outputs={"transformed": result}                )            # End item span            client.end_span(                request_id=item_span.request_id,                span_id=item_span.span_id,                status="OK"            )        except Exception as e:            # Handle errors gracefully            client.end_span(                request_id=item_span.request_id,                span_id=item_span.span_id,                status="ERROR",                attributes={"error": str(e)}            )    # End main trace    client.end_trace(        request_id=root.request_id,        outputs={            "processed_count": len(results),            "success_rate": len(results) / len(items)        }    )    return results

## Best practices[​](#best-practices "Direct link to Best practices")

### Use context managers for safety[​](#use-context-managers-for-safety "Direct link to Use context managers for safety")

Create custom context managers to ensure spans are always closed:

Python

    from contextlib import contextmanager@contextmanagerdef traced_span(client, name, request_id, parent_id=None, **kwargs):    """Context manager for safe span management"""    span = client.start_span(        name=name,        request_id=request_id,        parent_id=parent_id,        **kwargs    )    try:        yield span    except Exception as e:        client.end_span(            request_id=span.request_id,            span_id=span.span_id,            status="ERROR",            attributes={"error": str(e)}        )        raise    else:        client.end_span(            request_id=span.request_id,            span_id=span.span_id,            status="OK"        )# Usagewith traced_span(client, "my_operation", request_id, parent_id) as span:    # Your code here    result = perform_operation()

### Implement trace state management[​](#implement-trace-state-management "Direct link to Implement trace state management")

Manage trace state for complex applications:

Python

    class TraceStateManager:    """Manage trace state across application components"""    def __init__(self):        self.client = MlflowClient()        self._trace_stack = []    @property    def current_trace(self):        """Get current active trace"""        return self._trace_stack[-1] if self._trace_stack else None    def push_trace(self, name: str, **kwargs):        """Start a new trace and push to stack"""        if self.current_trace:            # Create child span if trace exists            span = self.client.start_span(                name=name,                request_id=self.current_trace.request_id,                parent_id=self.current_trace.span_id,                **kwargs            )        else:            # Create new trace            span = self.client.start_trace(name=name, **kwargs)        self._trace_stack.append(span)        return span    def pop_trace(self, **kwargs):        """End current trace and pop from stack"""        if not self._trace_stack:            return        span = self._trace_stack.pop()        if self._trace_stack:            # End child span            self.client.end_span(                request_id=span.request_id,                span_id=span.span_id,                **kwargs            )        else:            # End root trace            self.client.end_trace(                request_id=span.request_id,                **kwargs            )

### Add meaningful attributes[​](#add-meaningful-attributes "Direct link to Add meaningful attributes")

Enrich your traces with context that aids debugging:

Python

    # Good: Specific, actionable attributesclient.start_span(    name="llm_call",    request_id=request_id,    parent_id=parent_id,    attributes={        "model": "gpt-4",        "temperature": 0.7,        "max_tokens": 1000,        "prompt_template": "rag_v2",        "user_tier": "premium"    })# Bad: Generic, unhelpful attributesclient.start_span(    name="process",    request_id=request_id,    parent_id=parent_id,    attributes={"step": 1, "data": "some data"})

## Common pitfalls[​](#common-pitfalls "Direct link to Common pitfalls")

**Avoid these common mistakes:**

1.  **Forgetting to end spans** - Always use try/finally or context managers
2.  **Incorrect parent-child relationships** - Double-check span IDs
3.  **Mixing high-level and low-level APIs** - They don't interoperate
4.  **Hardcoding trace IDs** - Always generate unique IDs
5.  **Ignoring thread safety** - Client APIs are not thread-safe by default

## Next steps[​](#next-steps "Direct link to Next steps")

Continue your journey with these recommended actions and tutorials.

*   [Debug & observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Analyze traces created with client APIs
*   [Query traces via SDK](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk) - Programmatically access your traced data
*   [Function Decorator APIs](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator) - Simpler alternative for most use cases
