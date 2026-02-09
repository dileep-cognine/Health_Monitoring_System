from src.patterns.factory import ProcessorFactory
from src.processors.metrics import MetricsProcessor


def test_cpu_processor_creation():
    """
    Verify that the ProcessorFactory creates a MetricsProcessor.

    This test ensures that the factory correctly maps the
    "metrics" identifier to the MetricsProcessor class.
    """
    processor = ProcessorFactory.create_processor("metrics")
    assert isinstance(processor, MetricsProcessor)
