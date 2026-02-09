from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

from src.metaclasses.config_manager import ConfigManager


class StorageStrategy(ABC):
    """
    Abstract base class for storage strategies.

    Defines a common interface for different storage backends
    used to persist alert or metric data.
    """

    @abstractmethod
    def store(self, data: Any) -> None:
        """
        Persist data using the concrete storage strategy.

        Args:
            data (Any): Data to be stored.
        """
        pass


class FileStorageStrategy(StorageStrategy):
    """
    Storage strategy that persists data to a local file.
    """

    def __init__(self, filepath: str = "/app/data/storage.txt") -> None:
        """
        Initialize file-based storage.

        Ensures that the parent directory exists.

        Args:
            filepath (str): Path to the storage file.
        """
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

    def store(self, data: Any) -> None:
        """
        Append data to the storage file.

        Args:
            data (Any): Data to be written to the file.
        """
        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(f"{data}\n")


class DatabaseStorageStrategy(StorageStrategy):
    """
    Mock storage strategy simulating database persistence.
    """

    def store(self, data: Any) -> None:
        """
        Simulate storing data in a database.

        Args:
            data (Any): Data to be stored.
        """
        # Simulated database write
        print(f"[DB] Stored data: {data}")


class CloudStorageStrategy(StorageStrategy):
    """
    Mock storage strategy simulating cloud-based persistence.
    """

    def store(self, data: Any) -> None:
        """
        Simulate uploading data to cloud storage.

        Args:
            data (Any): Data to be uploaded.
        """
        # Simulated cloud upload
        print(f"[CLOUD] Uploaded data: {data}")


class StorageContext:
    """
    Context class for selecting and using storage strategies.

    Chooses a concrete storage strategy at runtime based on
    configuration and delegates storage operations to it.
    """

    def __init__(self) -> None:
        """
        Initialize the storage context.

        Loads configuration and selects the appropriate
        storage strategy.
        """
        self._config = ConfigManager()
        self._strategy = self._select_strategy()

    def _select_strategy(self) -> StorageStrategy:
        """
        Select a storage strategy based on configuration.

        Returns:
            StorageStrategy: Selected concrete storage strategy.

        Raises:
            ValueError: If the configured backend is unsupported.
        """
        backend = self._config.get("STORAGE_BACKEND")

        if backend == "file":
            return FileStorageStrategy()
        if backend == "db":
            return DatabaseStorageStrategy()
        if backend == "cloud":
            return CloudStorageStrategy()

        raise ValueError(f"Unsupported storage backend: {backend}")

    def set_strategy(self, backend: str) -> None:
        """
        Explicitly switch the storage strategy at runtime.

        This method is useful for testing, demonstrations,
        or examiner-driven configuration changes.

        Args:
            backend (str): Storage backend identifier
                ("file", "db", or "cloud").
        """
        self._config._config["STORAGE_BACKEND"] = backend
        self._strategy = self._select_strategy()

    def store(self, data: Any) -> None:
        """
        Store data using the currently selected strategy.

        Args:
            data (Any): Data to be persisted.
        """
        self._strategy.store(data)
