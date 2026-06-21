---
title: Access trace data | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/access-trace-data
ingestedAt: "2026-06-18T08:17:54.212Z"
---

This page demonstrates how to access every aspect of trace data including metadata, spans, assessments, and more. Once you learn how to access trace data, see [Examples: Analyzing traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces)

The MLflow [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) object consists of two main components:

*   [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo), metadata about the trace:
    
    *   [ID and status](#basic-metadata)
    *   [Preview data](#preview-data)
    *   [Timing](#timing)
    *   [Tags](#tags)
    *   [Token usage](#token-usage)
    *   [Assessments](#assessments)
*   [`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData), the actual execution data:
    
    *   [Spans](#spans)
    *   [Full request and response data](#request-response)

**API Reference:** [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo)

Python

    # Primary identifiersprint(f"Trace ID: {trace.info.trace_id}")print(f"Client Request ID: {trace.info.client_request_id}")# Status informationprint(f"State: {trace.info.state}")  # OK, ERROR, IN_PROGRESSprint(f"Status (deprecated): {trace.info.status}")  # Use state instead# Request/response previews (truncated)print(f"Request preview: {trace.info.request_preview}")print(f"Response preview: {trace.info.response_preview}")

### Storage location and experiment[​](#storage-location-and-experiment "Direct link to Storage location and experiment")

Python

    # Trace storage locationlocation = trace.info.trace_locationprint(f"Location type: {location.type}")# If stored in MLflow experimentif location.mlflow_experiment:    print(f"Experiment ID: {location.mlflow_experiment.experiment_id}")    # Shortcut property    print(f"Experiment ID: {trace.info.experiment_id}")# If stored in Databricks inference tableif location.inference_table:    print(f"Table: {location.inference_table.full_table_name}")

## Request and response previews[​](#-request-and-response-previews "Direct link to -request-and-response-previews")

The [`request_preview`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) and [`response_preview`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) properties provide truncated summaries of the full request and response data, making it easy to quickly understand what happened without loading the complete payloads.

Python

    request_preview = trace.info.request_previewresponse_preview = trace.info.response_previewprint(f"Request preview: {request_preview}")print(f"Response preview: {response_preview}")# Compare with full request/response datafull_request = trace.data.request  # Complete request textfull_response = trace.data.response  # Complete response textif full_request and request_preview:    print(f"Full request length: {len(full_request)} characters")    print(f"Preview is {len(request_preview)/len(full_request)*100:.1f}% of full request")

**API Reference:** [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) timing properties

Python

    # Timestamps (milliseconds since epoch)print(f"Start time (ms): {trace.info.request_time}")print(f"Timestamp (ms): {trace.info.timestamp_ms}")  # Alias for request_time# Durationprint(f"Execution duration (ms): {trace.info.execution_duration}")print(f"Execution time (ms): {trace.info.execution_time_ms}")  # Alias# Convert to human-readable formatimport datetimestart_time = datetime.datetime.fromtimestamp(trace.info.request_time / 1000)print(f"Started at: {start_time}")

**API Reference:** [`TraceInfo.tags`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) and [`TraceInfo.trace_metadata`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo)

Python

    # Tags (mutable, can be updated after creation)print("Tags:")for key, value in trace.info.tags.items():    print(f"  {key}: {value}")# Access specific tagsprint(f"Environment: {trace.info.tags.get('environment')}")print(f"User ID: {trace.info.tags.get('user_id')}")# Trace metadata (immutable, set at creation)print("\nTrace metadata:")for key, value in trace.info.trace_metadata.items():    print(f"  {key}: {value}")# Deprecated aliasprint(f"Request metadata: {trace.info.request_metadata}")  # Same as trace_metadata

## Token usage information[​](#-token-usage-information "Direct link to -token-usage-information")

MLflow Tracing can track token usage of LLM calls, using token counts returned by LLM provider APIs.

Python

    # Get aggregated token usage (if available)token_usage = trace.info.token_usageif token_usage:    print(f"Input tokens: {token_usage.get('input_tokens')}")    print(f"Output tokens: {token_usage.get('output_tokens')}")    print(f"Total tokens: {token_usage.get('total_tokens')}")

How you track token usage depends on the LLM provider. The following table describes different methods for tracking token usage across various providers and platforms.

## Assessments[​](#-assessments "Direct link to -assessments")

Find assessments with `search_assessments()`.

**API Reference:** [`Trace.search_assessments`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.search_assessments)

Python

    # 1. Get all assessmentsall_assessments = trace.search_assessments()print(f"Total assessments: {len(all_assessments)}")# 2. Search by namehelpfulness = trace.search_assessments(name="helpfulness")if helpfulness:    assessment = helpfulness[0]    print(f"Helpfulness: {assessment.value}")    print(f"Source: {assessment.source.source_type} - {assessment.source.source_id}")    print(f"Rationale: {assessment.rationale}")# 3. Search by typefeedback_only = trace.search_assessments(type="feedback")expectations_only = trace.search_assessments(type="expectation")print(f"Feedback assessments: {len(feedback_only)}")print(f"Expectation assessments: {len(expectations_only)}")# 4. Search by span IDspan_assessments = trace.search_assessments(span_id=retriever_span.span_id)print(f"Assessments for retriever span: {len(span_assessments)}")# 5. Get all assessments including overridden onesall_including_invalid = trace.search_assessments(all=True)print(f"All assessments (including overridden): {len(all_including_invalid)}")# 6. Combine criteriahuman_feedback = trace.search_assessments(    type="feedback",    name="helpfulness")for fb in human_feedback:    print(f"Human feedback: {fb.name} = {fb.value}")

Access assessment details

Python

    # Get detailed assessment informationfor assessment in trace.info.assessments:    print(f"\nAssessment: {assessment.name}")    print(f"  Type: {type(assessment).__name__}")    print(f"  Value: {assessment.value}")    print(f"  Source: {assessment.source.source_type.value}")    print(f"  Source ID: {assessment.source.source_id}")    # Optional fields    if assessment.rationale:        print(f"  Rationale: {assessment.rationale}")    if assessment.metadata:        print(f"  Metadata: {assessment.metadata}")    if assessment.error:        print(f"  Error: {assessment.error}")    if hasattr(assessment, 'span_id') and assessment.span_id:        print(f"  Span ID: {assessment.span_id}")

## Work with Spans[​](#-work-with-spans "Direct link to -work-with-spans")

Spans are the building blocks of traces, representing individual operations or units of work. The [`Span`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span) class represents immutable, completed spans retrieved from traces.

### Access span properties[​](#access-span-properties "Direct link to Access span properties")

**API Reference:** [`TraceData.spans`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData), [`Span`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span), and [`SpanType`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.SpanType)

Python

    # Access all spans from a tracespans = trace.data.spansprint(f"Total spans: {len(spans)}")# Get a specific spanspan = spans[0]# Basic propertiesprint(f"Span ID: {span.span_id}")print(f"Name: {span.name}")print(f"Type: {span.span_type}")print(f"Trace ID: {span.trace_id}")  # Which trace this span belongs toprint(f"Parent ID: {span.parent_id}")  # None for root spans# Timing information (nanoseconds)print(f"Start time: {span.start_time_ns}")print(f"End time: {span.end_time_ns}")duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000print(f"Duration: {duration_ms:.2f}ms")# Status informationprint(f"Status: {span.status}")print(f"Status code: {span.status.status_code}")print(f"Status description: {span.status.description}")# Inputs and outputsprint(f"Inputs: {span.inputs}")print(f"Outputs: {span.outputs}")# Iterate through all spansfor span in spans:    print(f"\nSpan: {span.name}")    print(f"  ID: {span.span_id}")    print(f"  Type: {span.span_type}")    print(f"  Duration (ms): {(span.end_time_ns - span.start_time_ns) / 1_000_000:.2f}")    # Parent-child relationships    if span.parent_id:        print(f"  Parent ID: {span.parent_id}")

### Find specific spans[​](#find-specific-spans "Direct link to find-specific-spans")

Use [`search_spans()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.search_spans) to find spans matching specific criteria:

Python

    import refrom mlflow.entities import SpanType# 1. Search by exact nameretriever_spans = trace.search_spans(name="retrieve_documents")print(f"Found {len(retriever_spans)} retriever spans")# 2. Search by regex patternpattern = re.compile(r".*_tool$")tool_spans = trace.search_spans(name=pattern)print(f"Found {len(tool_spans)} tool spans")# 3. Search by span typechat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)llm_spans = trace.search_spans(span_type="CHAT_MODEL")  # String also worksprint(f"Found {len(chat_spans)} chat model spans")# 4. Search by span IDspecific_span = trace.search_spans(span_id=retriever_spans[0].span_id)print(f"Found span: {specific_span[0].name if specific_span else 'Not found'}")# 5. Combine criteriatool_fact_check = trace.search_spans(    name="fact_check_tool",    span_type=SpanType.TOOL)print(f"Found {len(tool_fact_check)} fact check tool spans")# 6. Get all spans of a typeall_tools = trace.search_spans(span_type=SpanType.TOOL)for tool in all_tools:    print(f"Tool: {tool.name}")

#### Intermediate outputs[​](#intermediate-outputs "Direct link to Intermediate outputs")

Python

    # Get intermediate outputs from non-root spansintermediate = trace.data.intermediate_outputsif intermediate:    print("\nIntermediate outputs:")    for span_name, output in intermediate.items():        print(f"  {span_name}: {output}")

### Span attributes[​](#span-attributes "Direct link to Span attributes")

**API Reference:** [`Span.get_attribute`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span.get_attribute) and [`SpanAttributeKey`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.tracing.html#mlflow.tracing.constant.SpanAttributeKey)

Python

    from mlflow.tracing.constant import SpanAttributeKey# Get a chat model spanchat_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]# Get all attributesprint("All span attributes:")for key, value in chat_span.attributes.items():    print(f"  {key}: {value}")# Get specific attributespecific_attr = chat_span.get_attribute("custom_attribute")print(f"Custom attribute: {specific_attr}")# Access chat-specific attributes using SpanAttributeKeymessages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)tools = chat_span.get_attribute(SpanAttributeKey.CHAT_TOOLS)print(f"Chat messages: {messages}")print(f"Available tools: {tools}")# Access token usage from spaninput_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")print(f"Span token usage - Input: {input_tokens}, Output: {output_tokens}")

### Advanced span operations[​](#advanced-span-operations "Direct link to Advanced span operations")

#### Convert spans to/from dictionaries[​](#convert-spans-tofrom-dictionaries "Direct link to Convert spans to/from dictionaries")

Python

    # Convert span to dictionaryspan_dict = span.to_dict()print(f"Span dict keys: {span_dict.keys()}")# Recreate span from dictionaryfrom mlflow.entities import Spanreconstructed_span = Span.from_dict(span_dict)print(f"Reconstructed span: {reconstructed_span.name}")

#### Advanced span analysis[​](#advanced-span-analysis "Direct link to Advanced span analysis")

Python

    def analyze_span_tree(trace):    """Analyze the span hierarchy and relationships."""    spans = trace.data.spans    # Build parent-child relationships    span_dict = {span.span_id: span for span in spans}    children = {}    for span in spans:        if span.parent_id:            if span.parent_id not in children:                children[span.parent_id] = []            children[span.parent_id].append(span)    # Find root spans    roots = [s for s in spans if s.parent_id is None]    def print_tree(span, indent=0):        duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000        status_icon = "✓" if span.status.status_code == SpanStatusCode.OK else "✗"        print(f"{'  ' * indent}{status_icon} {span.name} ({span.span_type}) - {duration_ms:.1f}ms")        # Print children        for child in sorted(children.get(span.span_id, []),                          key=lambda s: s.start_time_ns):            print_tree(child, indent + 1)    print("Span Hierarchy:")    for root in roots:        print_tree(root)    # Calculate span statistics    total_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000                     for s in spans)    llm_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000                   for s in spans if s.span_type in [SpanType.LLM, SpanType.CHAT_MODEL])    retrieval_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000                        for s in spans if s.span_type == SpanType.RETRIEVER)    print(f"\nSpan Statistics:")    print(f"  Total spans: {len(spans)}")    print(f"  Total time: {total_time:.1f}ms")    print(f"  LLM time: {llm_time:.1f}ms ({llm_time/total_time*100:.1f}%)")    print(f"  Retrieval time: {retrieval_time:.1f}ms ({retrieval_time/total_time*100:.1f}%)")    # Find critical path (longest duration path from root to leaf)    def find_critical_path(span):        child_paths = []        for child in children.get(span.span_id, []):            path, duration = find_critical_path(child)            child_paths.append((path, duration))        span_duration = (span.end_time_ns - span.start_time_ns) / 1_000_000        if child_paths:            best_path, best_duration = max(child_paths, key=lambda x: x[1])            return [span] + best_path, span_duration + best_duration        else:            return [span], span_duration    if roots:        critical_paths = [find_critical_path(root) for root in roots]        critical_path, critical_duration = max(critical_paths, key=lambda x: x[1])        print(f"\nCritical Path ({critical_duration:.1f}ms total):")        for span in critical_path:            duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000            print(f"  → {span.name} ({duration_ms:.1f}ms)")# Use the analyzeranalyze_span_tree(trace)

## Request and response data[​](#-request-and-response-data "Direct link to -request-and-response-data")

Python

    # Get root span request/response (backward compatibility)request_json = trace.data.requestresponse_json = trace.data.response# Parse JSON stringsimport jsonif request_json:    request_data = json.loads(request_json)    print(f"Request: {request_data}")if response_json:    response_data = json.loads(response_json)    print(f"Response: {response_data}")

## Data export and conversion[​](#data-export-and-conversion "Direct link to Data export and conversion")

### Convert to dictionary[​](#convert-to-dictionary "Direct link to Convert to dictionary")

**API Reference:** [`Trace.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_dict)

Python

    # Convert entire trace to dictionarytrace_dict = trace.to_dict()print(f"Trace dict keys: {trace_dict.keys()}")print(f"Info keys: {trace_dict['info'].keys()}")print(f"Data keys: {trace_dict['data'].keys()}")# Convert individual componentsinfo_dict = trace.info.to_dict()data_dict = trace.data.to_dict()# Reconstruct trace from dictionaryfrom mlflow.entities import Tracereconstructed_trace = Trace.from_dict(trace_dict)print(f"Reconstructed trace ID: {reconstructed_trace.info.trace_id}")

### JSON serialization[​](#json-serialization "Direct link to JSON serialization")

**API Reference:** [`Trace.to_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_json)

Python

    # Convert to JSON stringtrace_json = trace.to_json()print(f"JSON length: {len(trace_json)} characters")# Pretty print JSONtrace_json_pretty = trace.to_json(pretty=True)print("Pretty JSON (first 500 chars):")print(trace_json_pretty[:500])# Load trace from JSONfrom mlflow.entities import Traceloaded_trace = Trace.from_json(trace_json)print(f"Loaded trace ID: {loaded_trace.info.trace_id}")

### Pandas DataFrame conversion[​](#pandas-dataframe-conversion "Direct link to Pandas DataFrame conversion")

**API Reference:** [`Trace.to_pandas_dataframe_row`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_pandas_dataframe_row)

Python

    # Convert trace to DataFrame rowrow_data = trace.to_pandas_dataframe_row()print(f"DataFrame row keys: {list(row_data.keys())}")# Create DataFrame from multiple tracesimport pandas as pd# Get multiple tracestraces = mlflow.search_traces(max_results=5)# If you have individual trace objectstrace_rows = [t.to_pandas_dataframe_row() for t in [trace]]df = pd.DataFrame(trace_rows)print(f"DataFrame shape: {df.shape}")print(f"Columns: {df.columns.tolist()}")# Access specific data from DataFrameprint(f"Trace IDs: {df['trace_id'].tolist()}")print(f"States: {df['state'].tolist()}")print(f"Durations: {df['execution_duration'].tolist()}")

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Examples: Analyzing traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces) - Analyze traces for specific use cases.
