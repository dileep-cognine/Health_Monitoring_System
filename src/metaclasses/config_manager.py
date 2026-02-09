from typing import Any, Dict, Optional
from src.metaclasses.singleton_meta import SingletonMeta


class ConfigManager(metaclass=SingletonMeta):
    """
    Centralized configuration manager implemented as a Singleton.

    This class provides global access to application configuration values
    and ensures only one configuration instance exists across the system.
    """

    REQUIRED_KEYS = {
        "METRIC_THRESHOLD",
        "ASYNC_TIMEOUT",
        "STORAGE_BACKEND",
    }

    _config: Dict[str, Any] = {
        "METRIC_THRESHOLD": 90.0,
        "ASYNC_TIMEOUT": 5,
        "STORAGE_BACKEND": "file",
        "METRIC_ENDPOINTS": []
    }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Retrieve a configuration value.

        Args:
            key (str): Configuration key to retrieve.
            default (Optional[Any]): Value to return if key is not found.

        Returns:
            Any: Configuration value associated with the key.

        Raises:
            KeyError: If the key is missing and no default is provided.
        """
        if key in self._config:
            return self._config[key]

        if default is not None:
            return default

        raise KeyError(f"Missing config key: {key}")

    def set(self, key: str, value: Any) -> None:
        """
        Update or add a configuration value at runtime.

        Args:
            key (str): Configuration key.
            value (Any): Value to associate with the key.
        """
        self._config[key] = value
