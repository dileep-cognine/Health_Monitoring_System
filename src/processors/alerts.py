from typing import Dict, Any
from src.processors.base import DataProcessor


class AlertProcessor(DataProcessor):
    """
    Processor responsible for generating human-readable alert messages.

    This processor validates metric event data and formats it into
    an alert message when threshold conditions are met.
    """

    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Validate incoming alert data.

        Args:
            data (Dict[str, Any]): Metric event data to validate.

        Returns:
            bool: True if the data contains the required fields
            and structure, otherwise False.
        """
        return (
            isinstance(data, dict)
            and "metric" in data
            and "value" in data
        )

    def process(self, data: Dict[str, Any]) -> str:
        """
        Generate an alert message from validated metric data.

        Args:
            data (Dict[str, Any]): Validated metric event data.

        Returns:
            str: Formatted alert message.

        Raises:
            ValueError: If the input data fails validation.
        """
        if not self.validate(data):
            raise ValueError("Invalid alert data")

        return (
            f"ALERT: {data['metric']} crossed threshold "
            f"with value {data['value']}"
        )
