# Introduction

Welcome to the InfraStack AI Python SDK! This SDK is designed to help developers and development teams integrate advanced observability capabilities into their applications. InfraStack AI provides next-generation observability tools that allow you to ship high-quality code and gain actionable insights in milliseconds.

## Capabilities

Currently, this SDK supports:

1. **Flask Instrumentation**: Easily instrument your Flask applications to monitor and trace requests and performance.
2. **Logging**: Send logs to InfraStack AI for centralized log management and analysis.
3. **Tracing**: Create and manage traces to monitor the performance and behavior of your application.

We are actively working on adding support for Django FastAPI and LLM's, so stay tuned for more updates!

## Installation

```console
pip3 install infrastack
```


## Integrations

### Flask Instrument

To instrument your Flask application with InfraStack AI, use the following code snippet:

```python
from infrastack import FlaskInstrument
from flask import Flask

app = Flask(__name__)

FlaskInstrument("your_service_name", app, infrastackai_api_key="your_infrastack_api_key")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

### Logging

To send logs to InfraStack AI, use the following code snippet:

```python
from infrastack import LogHandler
import logging

logger = logging.getLogger(__name__)
LogHandler("your_service_name", logger, infrastackai_api_key="your_infrastack_api_key")

logger.info("TEST")
```

### Tracing

To create and use a tracer with InfraStack AI, use the following code snippet:

```python
from infrastack import CreateTracer

my_tracer = CreateTracer("your_service_name", "trace_name", infrastackai_api_key="your_infrastack_api_key")

with my_tracer.start_span("scope-create-version") as span:
    span.set_attribute("version", "0.0.0")
    span.set_attribute("scope", "create-version")
    span.set_attribute("author", "Your Name")
    print("hi")
```



### OpenAI Instrument

To instrument your OpenAI API calls with InfraStack AI, use the following code snippet:

```python
from infrastack import OpenAIInstrument
from openai import OpenAI

# Initialize OpenAIInstrument
instrument = OpenAIInstrument("your_service_name", catch_content=False, infrastackai_api_key="your_infrastack_api_key")

# Example OpenAI API call
client = OpenAI(api_key="your_openai_api_key")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": [{"type": "text", "text": "Hi"}]}
    ]
)

print(response)
```



## Note on API Key Configuration

The InfraStack AI SDK provides two methods for configuring your API key:

1. **Passing it as a Parameter**: You can directly pass the `infrastackai_api_key` as a parameter when initializing the Flask instrument, log handler, or tracer.

2. **Environment Variable (.env)**: Alternatively, you can set the `INFRASTACKAI_API_KEY` as an environment variable. If this environment variable is set, the SDK will automatically use it, and you do not need to pass the API key as a parameter.



## Contributing

We welcome contributions! Please submit a pull request or open an issue to get started.