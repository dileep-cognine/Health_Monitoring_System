from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class for all data processors.
    Enforces a consistent interface across processors.
    """

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate input data before processing.
        """
        raise NotImplementedError

    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Process validated data and return the result.
        """
        raise NotImplementedError
