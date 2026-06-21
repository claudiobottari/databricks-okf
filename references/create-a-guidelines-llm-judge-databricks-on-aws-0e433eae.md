---
title: Create a guidelines LLM judge | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/guidelines
ingestedAt: "2026-06-18T08:14:53.823Z"
---

Guidelines LLM judges use pass/fail natural language criteria to evaluate GenAI outputs. They excel at evaluating:

*   **Compliance**: "Must not include pricing information"
*   **Style/tone**: "Maintain professional, empathetic tone"
*   **Requirements**: "Must include specific disclaimers"
*   **Accuracy**: "Use only facts from provided context"

For detailed documentation and additional examples, see the [MLflow Guidelines judges documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/guidelines/).

Guidelines LLM judges provide the following benefits:

*   **Business-friendly**: Domain experts write criteria without coding
*   **Flexible**: Update criteria without code changes
*   **Interpretable**: Clear pass/fail conditions
*   **Fast iteration**: Rapidly test new criteria

## Ways to use guidelines judges[​](#ways-to-use-guidelines-judges "Direct link to Ways to use guidelines judges")

MLflow provides the following guidelines judges:

1.  **[Built-in `Guidelines()` judge](#prebuilt-guidelines-scorer)**: Apply global guidelines uniformly to all rows. Evaluates app inputs and outputs only. Works in both offline evaluation and production monitoring.
2.  **[Built-in `ExpectationsGuidelines()` judge](#prebuilt-expectationsguidelines-scorer)**: Apply per-row guidelines labeled by domain experts in an evaluation dataset. Evaluates app inputs and outputs only. For offline evaluation only.

For API details, see the MLflow documentation:

*   [`Guidelines`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Guidelines)
*   [`ExpectationsGuidelines`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.ExpectationsGuidelines)

## How guidelines work[​](#how-guidelines-work "Direct link to How guidelines work")

Guidelines judges use a specially-tuned LLM to evaluate whether text meets your specified criteria. The judge:

1.  **Receives context**: Any JSON dictionary containing the data to evaluate (for example, `request`, `response`, `retrieved_documents`, `user_preferences`). You can reference these keys by name directly in your guidelines. See [Reference context variables](#reference-context-variables)
2.  **Applies guidelines**: Your natural language rules defining pass/fail conditions.
3.  **Makes judgment**: Returns a binary pass/fail score with detailed rationale.

For more information about the models powering the LLM judges, see [Information about the models powering LLM judges](#llm-judge-trust).

You can change the judge model by using the `model` argument in the judge definition. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name.

## Prerequisites for running the examples[​](#prerequisites-for-running-the-examples "Direct link to Prerequisites for running the examples")

1.  Install MLflow and required packages.
    
    Python
    
        %pip install --upgrade "mlflow[databricks]>=3.4.0"dbutils.library.restartPython()
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    

## `Guidelines()` judge: global guidelines[​](#-guidelines-judge-global-guidelines "Direct link to -guidelines-judge-global-guidelines")

The `Guidelines` judge applies uniform guidelines across all rows in your evaluation or traces in production monitoring. It automatically extracts request and response data from your trace and evaluates it against your guidelines.

In your guideline, refer to the app's inputs as the `request` and the app's outputs as the `response`. The following code creates some simple guidelines.

Python

    from mlflow.genai.scorers import Guidelinesimport mlflow# Example datadata = [    {        "inputs": {"question": "What is the capital of France?"},        "outputs": {"response": "The capital of France is Paris."}    },    {        "inputs": {"question": "What is the capital of Germany?"},        "outputs": {"response": "The capital of Germany is Berlin."}    }]# Create scorers with global guidelinesenglish = Guidelines(    name="english",    guidelines=["The response must be in English"])clarity = Guidelines(    name="clarity",    guidelines=["The response must be clear, coherent, and concise"],    model="databricks:/databricks-gpt-oss-120b",  # Optional custom judge model)# Evaluate with global guidelinesresults = mlflow.genai.evaluate(    data=data,    scorers=[english, clarity])

The following example creates an evaluation dataset containing sample inputs and outputs. It then defines and executes a guideline that judges the tone of the response.

Python

    from mlflow.genai.scorers import Guidelinesimport mlflow# Create evaluation dataset with pre-computed outputseval_dataset = [    {        "inputs": {            "messages": [{"role": "user", "content": "My order hasn't arrived yet"}]        },        "outputs": {            "choices": [{                "message": {                    "content": "I understand your concern about the delayed order. Let me help you track it right away."                }            }]        },    },    {        "inputs": {            "messages": [{"role": "user", "content": "How do I reset my password?"}]        },        "outputs": {            "choices": [{                "message": {                    "content": "To reset your password, click 'Forgot Password' on the login page. You'll receive an email within 5 minutes."                }            }]        },    }]# Run evaluation on existing outputsresults = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[Guidelines(name="tone", guidelines="The response must maintain a courteous, respectful tone throughout. It must show empathy for customer concerns in the request"),])

### Parameters[​](#parameters "Direct link to Parameters")

### How the Guidelines judge parses your app's inputs and outputs[​](#how-the-guidelines-judge-parses-your-apps-inputs-and-outputs "Direct link to how-the-guidelines-judge-parses-your-apps-inputs-and-outputs")

The Guidelines judge automatically extracts data from your trace to create the guideline's context with the keys `request` and `response`.

### Request[​](#request "Direct link to Request")

The `request` field is extracted from the provided `inputs`.

*   If `inputs` contains a `messages` key with an [array of OpenAI format chat messages](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages) then:
    *   If there is a single message, `request` is that message's `content`.
    *   If there is more than one message, `request` is the entire messages array serialized to a JSON string.
*   Otherwise, `request` is the entire `inputs` dict serialized to a JSON string.

### Request examples[​](#request-examples "Direct link to Request examples")

**Single message input**:

Python

    # Inputinputs = {    "messages": [        {"role": "user", "content": "How can I reset my password?"}    ]}# Parsed request"How can I reset my password?"

**Multi-turn conversation**:

Python

    # Inputinputs = {    "messages": [        {"role": "user", "content": "What is MLflow?"},        {"role": "assistant", "content": "MLflow is an open source AI engineering platform..."},        {"role": "user", "content": "Tell me more about tracing"}    ]}# Parsed request (JSON string)'[{"role": "user", "content": "What is MLflow?"}, {"role": "assistant", "content": "MLflow is an open source AI engineering platform..."}, {"role": "user", "content": "Tell me more about tracing"}]'

**Arbitrary dict**:

Python

    # Inputinputs = {"key1": "Explain MLflow evaluation", "key2": "something else"}# Parsed request'{"key1": "Explain MLflow evaluation", "key2": "something else"}'

### Response[​](#response "Direct link to Response")

The `response` field is extracted from the provided `outputs`:

*   If `outputs` contains an OpenAI format [ChatCompletions](https://platform.openai.com/docs/api-reference/chat/object) object:
    *   `response` is the first choice's `content`
*   If `outputs` contains a `messages` key with an [array of OpenAI format chat messages](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages)
    *   `response` is the last message's `content`
*   Otherwise, `response` is the `outputs` serialized to a JSON string.

### Response examples[​](#response-examples "Direct link to Response examples")

**ChatCompletion output**:

Python

    # Output (simplified)outputs = {    "choices": [{        "message": {            "content": "MLflow evaluation helps measure GenAI quality..."        }    }]}# Parsed response"MLflow evaluation helps measure GenAI quality..."

**Messages format output**:

Python

    # Outputoutputs = {    "messages": [        {"role": "user", "content": "What are the ..."}        {"role": "assistant", "content": "Here are the key features..."}    ]}# Parsed response"Here are the key features..."

**Arbitrary dict**:

Python

    # Inputinputs = {"key1": "Explain MLflow evaluation", "key2": "something else"}# Parsed request'{"key1": "Explain MLflow evaluation", "key2": "something else"}'

## `ExpectationsGuidelines()` judge: per-row guidelines[​](#-expectationsguidelines-judge-per-row-guidelines "Direct link to -expectationsguidelines-judge-per-row-guidelines")

The `ExpectationsGuidelines` judge evaluates against row-specific guidelines from domain experts. This allows different evaluation criteria for each example in your dataset.

### When to use[​](#when-to-use "Direct link to When to use")

Use this judge when:

*   You have domain experts who have labeled specific examples with custom guidelines
*   Different rows require different evaluation criteria

### Example[​](#example "Direct link to Example")

In your guideline, refer to the app's inputs as the `request` and the app's outputs as the `response`.

Python

    from mlflow.genai.scorers import ExpectationsGuidelinesimport mlflow# Dataset with per-row guidelinesdata = [    {        "inputs": {"question": "What is the capital of France?"},        "outputs": "The capital of France is Paris.",        "expectations": {            "guidelines": ["The response must be factual and concise"]        }    },    {        "inputs": {"question": "How to learn Python?"},        "outputs": "You can read a book or take a course.",        "expectations": {            "guidelines": ["The response must be helpful and encouraging"]        }    }]# Evaluate with per-row guidelinesresults = mlflow.genai.evaluate(    data=data,    scorers=[ExpectationsGuidelines()])

### Return values[​](#return-values "Direct link to Return values")

Guidelines judges return an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object containing:

*   `value`: `"yes"` (meets guidelines) or `"no"` (fails guidelines)
*   `rationale`: Detailed explanation of why the content passed or failed
*   `name`: The assessment name (either provided or auto-generated)
*   `error`: Error details if evaluation failed

## Best practices for writing effective guidelines[​](#best-practices-for-writing-effective-guidelines "Direct link to best-practices-for-writing-effective-guidelines")

Well-written guidelines are crucial for accurate evaluation. This section describes best practices when writing guidelines.

### Reference context variables[​](#reference-context-variables "Direct link to Reference context variables")

Include any key from your context dictionary directly in guidelines:

Python

    # Example 1: Validate against retrieved documentscontext = {    "request": "What is the refund policy?",    "response": "You can return items within 30 days for a full refund.",    "retrieved_documents": ["Policy: Returns accepted within 30 days", "Policy: No refunds after 30 days"]}guideline = "The response must only include information from retrieved_documents"# Example 2: Check user preferencescontext = {    "request": "Recommend a restaurant",    "response": "I suggest trying the new steakhouse downtown",    "user_preferences": {"dietary_restrictions": "vegetarian", "cuisine": "Italian"}}guideline = "The response must respect user_preferences when making recommendations"# Example 3: Enforce business rulescontext = {    "request": "Can you apply a discount?",    "response": "I've applied a 15% discount to your order",    "max_allowed_discount": 10,    "user_tier": "silver"}guideline = "The response must not exceed max_allowed_discount for the user_tier"# Example 4: Multiple constraintscontext = {    "request": "Tell me about product features",    "response": "This product includes features A, B, and C",    "approved_features": ["A", "B", "C", "D"],    "deprecated_features": ["X", "Y", "Z"]}guideline = """The response must:- Only mention approved_features- Not include deprecated_features"""

### Additional guidelines[​](#additional-guidelines "Direct link to Additional guidelines")

**Be specific and measurable** ✅ "The response must not include specific pricing amounts or percentages" ❌ "Don't talk about money"

**Use clear pass/fail conditions** ✅ "If asked about pricing, the response must direct users to the pricing page" ❌ "Handle pricing questions appropriately"

**Reference context explicitly** ✅ "The response must only use facts present in retrieved\_context" ❌ "Be factual"

**Structure complex requirements**

Python

    guideline = """The response must:- Include a greeting if first message- Address the user's specific question- End with an offer to help further- Not exceed 150 words"""

## Real world examples[​](#real-world-examples "Direct link to Real world examples")

### Customer service chatbot[​](#customer-service-chatbot "Direct link to Customer service chatbot")

Here are practical guidelines examples for evaluating a customer service chatbot across different scenarios:

#### Global guidelines for all interactions[​](#global-guidelines-for-all-interactions "Direct link to Global guidelines for all interactions")

Python

    from mlflow.genai.scorers import Guidelinesimport mlflow# Define global standards for all customer interactionstone_guidelines = Guidelines(    name="customer_service_tone",    guidelines="""The response must maintain our brand voice which is:    - Professional yet warm and conversational (avoid corporate jargon)    - Empathetic, acknowledging emotional context before jumping to solutions    - Proactive in offering help without being pushy    Specifically:    - If the customer expresses frustration, anger, or disappointment, the first sentence must acknowledge their emotion    - The response must use "I" statements to take ownership (e.g., "I understand" not "We understand")    - The response must avoid phrases that minimize concerns like "simply", "just", or "obviously"    - The response must end with a specific next step or open-ended offer to help, not generic closings""")compliance_guidelines = Guidelines(    name="policy_compliance",    guidelines=[        """Refund and return policies:        - The response must not promise refunds beyond the 30-day return window        - The response must mention restocking fees for electronics (15%) if discussing returns        - For items over $500, the response must note that manager approval is required        - The response must not waive shipping fees without checking customer loyalty tier""",        """Data privacy and security:        - The response must never ask for full credit card numbers, SSN, or passwords        - The response must not reference other customers' orders or information        - When discussing order details, the response must only reference the last 4 digits of payment methods        - The response must direct customers to secure portal for updating payment information""",        """Commitment limitations:        - The response must not guarantee specific delivery dates without system verification        - The response must include disclaimer about "estimated" times when discussing shipping        - The response must not promise price matches without mentioning the verification process        - For out-of-stock items, the response must not commit to restock dates"""    ])# Example customer service datacustomer_interactions = [    {        "inputs": {            "messages": [{"role": "user", "content": "I've been waiting 2 hours on hold! This is ridiculous!"}]        },        "outputs": {            "choices": [{                "message": {                    "content": "I completely understand your frustration about the long wait time. That's absolutely not the experience we want you to have. I'm here to help you right now - what can I assist you with today?"                }            }]        }    },    {        "inputs": {            "messages": [{"role": "user", "content": "Can I return my laptop? I bought it 45 days ago."}]        },        "outputs": {            "choices": [{                "message": {                    "content": "I'd be happy to look into return options for you. Since our standard return window is 30 days and your purchase was 45 days ago, I'll need to check if there are any exceptions we can make. For electronics like laptops, we do have a 15% restocking fee. May I have your order number to review your specific situation?"                }            }]        }    }]# Evaluate customer service interactionsresults = mlflow.genai.evaluate(    data=customer_interactions,    scorers=[tone_guidelines, compliance_guidelines])

#### Per-row guidelines for specific scenarios[​](#per-row-guidelines-for-specific-scenarios "Direct link to Per-row guidelines for specific scenarios")

Python

    from mlflow.genai.scorers import ExpectationsGuidelinesimport mlflow# Dataset with scenario-specific guidelinescustomer_service_data = [    {        "inputs": {            "messages": [{"role": "user", "content": "My package is 3 weeks late and I need it for an event tomorrow!"}]        },        "outputs": {            "choices": [{                "message": {                    "content": "I can absolutely understand how stressful this must be, especially with your event tomorrow. I'm so sorry your package has been delayed for 3 weeks - that's completely unacceptable. Let me help you immediately. I'm checking our local store inventory right now for same-day pickup options. I'm also processing a full refund of your shipping costs and applying a 25% discount to your order for this inconvenience. Would you prefer overnight delivery to arrive by 10 AM tomorrow, or would same-day pickup from our downtown location work better for you? I'm also connecting you with our escalation team - you'll receive a call within the next hour at the number on your account."                }            }]        },        "expectations": {            "guidelines": [                """The response must handle this urgent situation with exceptional care:                - First acknowledge both the delay AND the urgent tomorrow deadline                - Express genuine empathy using phrases like "I can absolutely understand how stressful this must be"                - Must NOT make excuses or blame shipping partners""",                """The response must provide immediate actionable solutions:                - Offer to check local store availability for same-day pickup                - If available, offer overnight shipping at no charge given the delay                - Provide direct escalation path: manager callback within 2 hours                - Include the executive customer service email for formal complaints""",                """The response must include compensation options without being asked:                - Mention automatic refund of original shipping costs                - Offer 20-30% discount on current order due to inconvenience                - Provide credit for future purchase if customer prefers"""            ]        }    },    {        "inputs": {            "messages": [{"role": "user", "content": "How do I cancel my subscription?"}]        },        "outputs": {            "choices": [{                "message": {                    "content": "I can help you cancel your subscription right away. Here's how: 1) Click 'Account Settings' in the top right corner, 2) Select 'Subscription' from the menu, 3) Click 'Cancel Subscription' and confirm. Your access will continue until March 15, 2024 (the end of your current billing period), and you won't be charged again. All your saved data and preferences will be kept for 30 days if you decide to return. You're entitled to a prorated refund of $12.50 for the unused portion of this month. Alternatively, if you'd prefer, I can offer you a 50% discount for the next 3 months or help you switch to our Basic plan which is $4.99/month."                }            }]        },        "expectations": {            "guidelines": [                """The response must respect the customer's decision to cancel:                - No guilt-inducing language or excessive retention attempts                - No hiding the cancellation process behind multiple steps                - Must not require phone calls if account was created online                - Acknowledge their right to cancel immediately without questions""",                """The response must provide complete cancellation information:                - State the exact steps (maximum 3) to cancel online                - Clarify the last billing date and when access ends                - Explain what happens to their data, saved preferences, and history                - Mention the 30-day reactivation window where data is preserved                - Note any partial month refunds they're entitled to""",                """The response may include ONE gentle retention offer:                - Can mention a pause option instead of cancellation                - Can offer a one-time discount or downgrade option                - Must present this as optional, after the cancellation instructions                - Must use soft language like 'alternatively' or 'if you'd prefer'"""            ]        }    },    {        "inputs": {            "messages": [{"role": "user", "content": "I was charged twice for my order #12345"}]        },        "outputs": {            "choices": [{                "message": {                    "content": "I see the duplicate charge on your order #12345, and I'll resolve this for you right away. I've initiated the refund for the duplicate charge of $157.99. For credit cards, you'll see this reflected in 3-5 business days, and you should see a pending reversal on your account within 24 hours. I'm sending you a confirmation email right now with the refund transaction ID (REF-789012) and all the details. Your case reference number is CS-456789 if you need to follow up. Since this occurred near month-end, if this causes any overdraft fees, please let us know - we'll reimburse up to $35 in bank fees. Our billing team's direct line is 1-800-555-0123 ext 2 if you need immediate assistance. This won't affect your credit or any future orders with us, and we're investigating our payment system to prevent this from happening again."                }            }]        },        "expectations": {            "guidelines": [                """The response must immediately validate the customer's concern:                - Acknowledge the duplicate charge without skepticism                - Must not ask for proof or screenshots initially                - Express understanding of the inconvenience and potential financial impact                - Take ownership with phrases like 'I'll resolve this for you right away'""",                """The response must provide specific resolution details:                - State exact refund timeline (e.g., '3-5 business days for credit cards, 5-7 for debit')                - Mention that they'll see a pending reversal within 24 hours                - Offer to send detailed confirmation email with transaction IDs                - Provide a reference number for this billing dispute                - Include the direct billing department contact for follow-up""",                """The response must address potential concerns proactively:                - If near month-end, acknowledge potential impact on their budget                - Offer to provide a letter for their bank if overdraft fees occurred                - Mention our overdraft reimbursement policy (up to $35)                - Assure that this won't affect their credit or future orders                - Note that we're investigating to prevent future occurrences"""            ]        }    }]results = mlflow.genai.evaluate(    data=customer_service_data,    scorers=[ExpectationsGuidelines()])

Here are practical guidelines examples for evaluating a document extraction application:

Python

    from mlflow.genai.scorers import Guidelinesimport mlflow# Define extraction accuracy standardsextraction_accuracy = Guidelines(    name="extraction_accuracy",    guidelines=[        """Field extraction completeness and accuracy:        - The response must extract ALL requested fields, using exact values from source        - For ambiguous data, the response must extract the most likely value and include a confidence score        - When multiple values exist for one field (e.g., multiple addresses), extract all and label them        - Preserve original formatting for IDs, reference numbers, and codes (including leading zeros)        - For missing fields, use null with reason: {"field": null, "reason": "not_found"} """,        """Numerical and financial data handling:        - Currency values must preserve exact decimal places as shown in source        - Must differentiate between currencies if multiple are present (USD, EUR, etc.)        - Percentage values must clarify if they're decimals (0.15) or percentages (15%)        - For calculated fields (totals, tax), must match source exactly - no recalculation        - Negative values must be preserved with proper notation (-$100 or ($100))""",        """Entity recognition and validation:        - Company names must be extracted exactly as written (including suffixes like Inc., LLC)        - Person names must preserve original order and formatting        - Must not merge similar entities (e.g., "John Smith" and "J. Smith" are kept separate)        - Email addresses and phone numbers must be validated for basic format        - Physical addresses must include all components present in source"""    ])format_compliance = Guidelines(    name="output_format",    guidelines="""Output structure must meet these enterprise data standards:    JSON Structure Requirements:    - Must be valid JSON that passes strict parsing    - All field names must use snake_case consistently    - Nested objects must maintain hierarchy from source document    - Arrays must be used for multiple values, never concatenated strings    Data Type Standards:    - Dates: ISO 8601 format (YYYY-MM-DD) with timezone if available    - Timestamps: ISO 8601 with time (YYYY-MM-DDTHH:MM:SSZ)    - Currency: {"amount": 1234.56, "currency": "USD", "formatted": "$1,234.56"}    - Phone: {"number": "+14155551234", "formatted": "(415) 555-1234", "type": "mobile"}    - Boolean: true/false (not "yes"/"no" or 1/0)    Metadata Requirements:    - Include extraction_timestamp in UTC    - Include source_page for multi-page documents    - Include confidence_score (0-1) for each ML-extracted field    - Include validation_flags array for any data quality issues detected""")# Example document extraction dataextraction_tasks = [    {        "inputs": {            "document_text": "Invoice #INV-2024-001\nDate: 2024-01-15\nBill To: Acme Corp\n123 Main St, Suite 100\nAnytown, CA 94000\n\nItems:\n- Widget Pro (SKU: WP-100) - Qty: 10 x $50.00 = $500.00\n- Service Fee - $100.00\n\nSubtotal: $600.00\nTax (8.75%): $52.50\nTotal: $652.50\n\nDue Date: 2024-02-15\nPayment Terms: Net 30",            "fields_to_extract": ["invoice_number", "customer", "total_amount", "due_date", "line_items"]        },        "outputs": {            "invoice_number": "INV-2024-001",            "customer": {                "name": "Acme Corp",                "address": {                    "street": "123 Main St, Suite 100",                    "city": "Anytown",                    "state": "CA",                    "zip": "94000"                }            },            "total_amount": {                "amount": 652.50,                "currency": "USD",                "formatted": "$652.50"            },            "due_date": "2024-02-15",            "line_items": [                {                    "description": "Widget Pro",                    "sku": "WP-100",                    "quantity": 10,                    "unit_price": 50.00,                    "total": 500.00                },                {                    "description": "Service Fee",                    "quantity": 1,                    "unit_price": 100.00,                    "total": 100.00                }            ],            "extraction_timestamp": "2024-01-20T10:30:00Z",            "source_page": 1,            "confidence_score": 0.95        }    },    {        "inputs": {            "document_text": "Contract between TechStart Inc. and CloudProvider LLC\nEffective Date: January 1, 2024\nContract ID: C-2024-789\n\nThis agreement outlines cloud hosting services...\nMonthly Fee: €5,000\nContract Term: 24 months\nCancellation: 90 days written notice required",            "fields_to_extract": ["contract_id", "parties", "monthly_fee", "term_length"]        },        "outputs": {            "contract_id": "C-2024-789",            "parties": [                {"name": "TechStart Inc.", "role": "customer"},                {"name": "CloudProvider LLC", "role": "provider"}            ],            "monthly_fee": {                "amount": 5000.00,                "currency": "EUR",                "formatted": "€5,000"            },            "term_length": {                "duration": 24,                "unit": "months"            },            "cancellation_notice": {                "days": 90,                "type": "written"            },            "extraction_timestamp": "2024-01-20T10:35:00Z",            "confidence_score": 0.92        }    }]# Evaluate document extractionsresults = mlflow.genai.evaluate(    data=extraction_tasks,    scorers=[extraction_accuracy, format_compliance])

#### Per-row guidelines for document types[​](#per-row-guidelines-for-document-types "Direct link to Per-row guidelines for document types")

Python

    from mlflow.genai.scorers import ExpectationsGuidelinesimport mlflow# Dataset with document-type specific guidelinesdocument_extraction_data = [    {        "inputs": {            "document_type": "invoice",            "document_text": "Invoice #INV-2024-001\nBill To: Acme Corp\nAmount: $1,234.56\nDue Date: 2024-03-15"        },        "outputs": {            "invoice_number": "INV-2024-001",            "customer": "Acme Corp",            "total_amount": 1234.56,            "due_date": "2024-03-15"        },        "expectations": {            "guidelines": [                """Invoice identification and classification:                - Must extract invoice_number preserving exact format including prefixes/suffixes                - Must identify invoice type (standard, credit memo, proforma) if specified                - Must extract both invoice date and due date, calculating days until due                - Must identify if this is a partial, final, or supplementary invoice                - For recurring invoices, must extract frequency and period covered""",                """Financial data extraction and validation:                - Line items must be extracted as array with: description, quantity, unit_price, total                - Must identify and separate: subtotal, tax amounts (with rates), shipping, discounts                - Currency must be identified explicitly, not assumed to be USD                - For discounts, must specify if percentage or fixed amount and what it applies to                - Payment terms must be extracted (e.g., "Net 30", "2/10 Net 30")                - Must flag any mathematical inconsistencies between line items and totals""",                """Vendor and customer information:                - Must extract complete billing and shipping addresses as separate objects                - Company names must include any DBA ("doing business as") variations                - Must extract tax IDs, business registration numbers if present                - Contact information must be categorized (billing contact vs. delivery contact)                - Must preserve any customer account numbers or reference codes"""            ]        }    },    {        "inputs": {            "document_type": "contract",            "document_text": "This agreement between Party A and Party B commences on January 1, 2024..."        },        "outputs": {            "parties": ["Party A", "Party B"],            "effective_date": "2024-01-01",            "term_length": "Not specified"        },        "expectations": {            "guidelines": [                """Party identification and roles:                - Must extract all parties with their full legal names and entity types (Inc., LLC, etc.)                - Must identify party roles (buyer/seller, licensee/licensor, employer/employee)                - Must extract any parent company relationships or guarantors mentioned                - Must capture all representatives, their titles, and authority to sign                - Must identify jurisdiction for each party if specified""",                """Critical dates and terms extraction:                - Must differentiate between: execution date, effective date, and expiration date                - Must extract notice periods for termination (e.g., "30 days written notice")                - Must identify any automatic renewal clauses and their conditions                - Must extract all milestone dates and deliverable deadlines                - For amendments, must note which version/date of original contract is modified""",                """Obligations and risk analysis:                - Must extract all payment terms, amounts, and schedules                - Must identify liability caps, indemnification clauses, and insurance requirements                - Must flag any non-standard clauses that deviate from typical contracts                - Must extract all conditions precedent and subsequent                - Must identify dispute resolution mechanism (arbitration, litigation, jurisdiction)                - Must extract any non-compete, non-solicitation, or confidentiality periods"""            ]        }    },    {        "inputs": {            "document_type": "medical_record",            "document_text": "Patient: John Doe\nDOB: 1985-06-15\nDiagnosis: Type 2 Diabetes\nMedications: Metformin 500mg"        },        "outputs": {            "patient_name": "John Doe",            "date_of_birth": "1985-06-15",            "diagnoses": ["Type 2 Diabetes"],            "medications": [{"name": "Metformin", "dosage": "500mg"}]        },        "expectations": {            "guidelines": [                """HIPAA compliance and privacy protection:                - Must never extract full SSN (only last 4 digits if needed for matching)                - Must never include full insurance policy numbers or member IDs                - Must redact or generalize sensitive mental health or substance abuse information                - For minors, must flag records requiring additional consent for sharing                - Must not extract genetic testing results without explicit permission flag""",                """Clinical data extraction standards:                - Diagnoses must use ICD-10 codes when available, with lay descriptions                - Medications must include: generic name, brand name, dosage, frequency, route, start date                - Must differentiate between active medications and discontinued/past medications                - Allergies must specify type (drug, food, environmental) and reaction severity                - Lab results must include: value, unit, reference range, abnormal flags                - Vital signs must include measurement date/time and measurement conditions""",                """Data quality and medical accuracy:                - Must flag any potentially dangerous drug interactions if multiple meds listed                - Must identify if vaccination records are up-to-date based on CDC guidelines                - Must extract both chief complaint and final diagnosis separately                - For chronic conditions, must note date of first diagnosis vs. most recent visit                - Must preserve clinical abbreviations but also provide expansions                - Must extract provider name, credentials, and NPI number if available"""            ]        }    }]results = mlflow.genai.evaluate(    data=document_extraction_data,    scorers=[ExpectationsGuidelines()])

## Information about the models powering LLM judges[​](#information-about-the-models-powering-llm-judges "Direct link to information-about-the-models-powering-llm-judges")

*   LLM judges might use third-party services to evaluate your GenAI applications, including Azure OpenAI operated by Microsoft.
*   For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI.
*   For European Union (EU) workspaces, LLM judges use models hosted in the EU. All other regions use models hosted in the US.
*   Disabling [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered) prevents the LLM judge from calling partner-powered models. You can still use LLM judges by providing your own model.
*   LLM judges are intended to help customers evaluate their GenAI agents/applications, and LLM judge outputs should not be used to train, improve, or fine-tune an LLM.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Use built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Evaluate quality with MLflow's other research-backed, built-in LLM judges
*   [Create custom LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) - Build custom judges for your specific needs
*   [Align judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) - Improve judge accuracy to match your quality standards
