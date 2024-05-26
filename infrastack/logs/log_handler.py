import os

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")


from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource



def LogHandler(service_name, logger, infrastackai_api_key=None):
    if infrastackai_api_key is None:
        infrastackai_api_key = os.getenv("INFRASTACKAI_API_KEY")
    if not infrastackai_api_key:
        raise ValueError("infrastackai_api_key is required")


    resource = Resource.create({"service.name": service_name})
    # Create and set the logger provider
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)

    # Create the OTLP log exporter that sends logs to configured destination
    exporter = OTLPLogExporter(timeout=30,endpoint="https://collector-us1-http.infrastack.ai/v1/logs", headers=(("infrastack-api-key", infrastackai_api_key),))
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))


    # Attach OTLP handler to root logger
    handler = LoggingHandler(logger_provider=logger_provider)
    logger.addHandler(handler)
        