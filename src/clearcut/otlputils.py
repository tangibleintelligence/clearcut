"""
Inits the OTLP framework.

TODO should we use the logger instrumenter?
"""
from contextlib import contextmanager

from opentelemetry import propagate, trace, context
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.propagators.textmap import CarrierT
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import Tracer
from opentelemetry.util.types import AttributeValue


def init_tracer_provider():
    provider = TracerProvider()
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)

    _tracer_provider_inited = True


init_tracer_provider()


def get_tracer(name: str) -> Tracer:
    return trace.get_tracer(name)


def set_attribute(key: str, value: AttributeValue):
    """Set attribute on current span."""
    trace.get_current_span().set_attribute(key, value)


@contextmanager
def context_from_carrier(headers_carrier: CarrierT):
    """Set up OTEL context, and clear it after exiting block"""
    token = None
    try:
        ctx = propagate.extract(headers_carrier)
        token = context.attach(ctx)
        yield
    finally:
        if token is not None:
            context.detach(token)


def carrier_from_context() -> CarrierT:
    """Return a carrier of the current OTLP context."""
    carrier = {}
    propagate.inject(carrier)
    return carrier
