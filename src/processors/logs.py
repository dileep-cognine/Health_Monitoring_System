from typing import Any, Dict
from src.processors.base import DataProcessor


class LogProcessor(DataProcessor):
    """
    Processor responsible for validating and normalizing log entries.

    Converts raw log strings into structured dictionary formats
    suitable for downstream processing or storage.
    """

    def validate(self, data: Any) -> bool:
        """
        Validate a log entry.

        Args:
            data (Any): Raw log data to validate.

        Returns:
            bool: True if the log entry is a non-empty string,
            otherwise False.
        """
        return isinstance(data, str) and len(data.strip()) > 0

    def process(self, data: str) -> Dict[str, str]:
        """
        Process a valid log entry into a structured format.

        Args:
            data (str): Raw log entry.

        Returns:
            Dict[str, str]: Dictionary containing the cleaned log entry.

        Raises:
            ValueError: If the log entry fails validation.
        """
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        return {
            "log": data.strip()
        }
