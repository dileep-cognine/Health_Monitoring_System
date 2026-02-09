from typing import Type

from src.processors.base import DataProcessor
from src.processors.metrics import MetricsProcessor
from src.processors.logs import LogProcessor
from src.processors.alerts import AlertProcessor
from src.processors.metrics import CPUProcessor


class ProcessorFactory:
    """
    Factory class for creating DataProcessor instances.

    This factory uses a registry-based approach to dynamically
    instantiate the appropriate processor implementation based
    on a string identifier.
    """

    _registry: dict[str, Type[DataProcessor]] = {
        "cpu": CPUProcessor,
        "metrics": MetricsProcessor,
        "logs": LogProcessor,
        "alerts": AlertProcessor,
    }

    @classmethod
    def create_processor(cls, processor_type: str) -> DataProcessor:
        """
        Create and return a DataProcessor instance based on type.

        Args:
            processor_type (str): Identifier of the processor to create
                (e.g., "cpu", "metrics", "logs", "alerts").

        Returns:
            DataProcessor: Instantiated processor corresponding
            to the requested type.

        Raises:
            ValueError: If the processor type is not registered
            or supported.
        """
        processor_type = processor_type.lower()

        if processor_type not in cls._registry:
            raise ValueError(
                f"Unsupported processor type: {processor_type}"
            )

        return cls._registry[processor_type]()
