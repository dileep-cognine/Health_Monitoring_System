from typing import Dict, Any
from src.processors.base import DataProcessor


class MetricsProcessor(DataProcessor):
    """
    Processor for validating and normalizing system-wide metrics.

    Handles metrics such as CPU, memory, and disk usage by ensuring
    required fields are present and converting values to floats.
    """

    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Validate incoming metrics data.

        Args:
            data (Dict[str, Any]): Raw metrics data.

        Returns:
            bool: True if all required metric keys are present,
            otherwise False.
        """
        required_keys = {"cpu", "memory", "disk"}
        return isinstance(data, dict) and required_keys.issubset(data.keys())

    def process(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Normalize validated metrics data.

        Args:
            data (Dict[str, Any]): Validated raw metrics data.

        Returns:
            Dict[str, float]: Normalized metrics with float values.

        Raises:
            ValueError: If the input data fails validation.
        """
        if not self.validate(data):
            raise ValueError("Invalid metrics data")

        # Normalize metrics to float values
        return {
            "cpu": float(data["cpu"]),
            "memory": float(data["memory"]),
            "disk": float(data["disk"]),
        }


class CPUProcessor(DataProcessor):
    """
    Processor dedicated to extracting and normalizing CPU metrics.
    """

    def validate(self, data: Dict[str, Any]) -> None:
        """
        Validate CPU metric data.

        Args:
            data (Dict[str, Any]): Raw metrics data.

        Raises:
            ValueError: If CPU data is missing.
        """
        if "cpu" not in data:
            raise ValueError("CPU data missing")

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract and normalize CPU metric data.

        Args:
            data (Dict[str, Any]): Raw metrics data.

        Returns:
            Dict[str, Any]: Dictionary containing CPU metric name
            and normalized value.
        """
        return {
            "metric": "cpu",
            "value": float(data["cpu"])
        }
