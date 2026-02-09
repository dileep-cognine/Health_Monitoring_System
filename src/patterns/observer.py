from abc import ABC, abstractmethod
from typing import List, Dict, Any

from src.metaclasses.config_manager import ConfigManager
from src.processors.alerts import AlertProcessor
from src.patterns.strategy import StorageContext


class Observer(ABC):
    """
    Abstract base class for observers in the Observer pattern.

    Concrete observers must implement the `update` method to
    react to notifications from the subject.
    """

    @abstractmethod
    def update(self, data: Dict[str, Any]) -> None:
        """
        Receive updates from the subject.

        Args:
            data (Dict[str, Any]): Payload containing update information.
        """
        pass


class MetricMonitor:
    """
    Subject in the Observer pattern that monitors metric values.

    This class evaluates incoming metrics against a configured
    threshold and notifies registered observers when the threshold
    is breached.
    """

    def __init__(self) -> None:
        """
        Initialize the MetricMonitor.

        Sets up the observer list and loads configuration values.
        """
        self._observers: List[Observer] = []
        self._config = ConfigManager()

    def register_observer(self, observer: Observer) -> None:
        """
        Register an observer to receive metric updates.

        Args:
            observer (Observer): Observer instance to register.
        """
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """
        Remove a previously registered observer.

        Args:
            observer (Observer): Observer instance to remove.
        """
        self._observers.remove(observer)

    def notify_observers(self, data: Dict[str, Any]) -> None:
        """
        Notify all registered observers with metric data.

        Args:
            data (Dict[str, Any]): Metric information to broadcast.
        """
        for observer in self._observers:
            observer.update(data)

    def update_metrics(self, metrics: Dict[str, float]) -> None:
        """
        Evaluate metrics and notify observers if thresholds are exceeded.

        Args:
            metrics (Dict[str, float]): Mapping of metric names to values.
        """
        threshold = self._config.get("METRIC_THRESHOLD")

        for metric, value in metrics.items():
            if value > threshold:
                self.notify_observers({
                    "metric": metric,
                    "value": value
                })


class AlertObserver(Observer):
    """
    Observer that handles alert generation and persistence.

    When notified, this observer processes alert data and stores
    the resulting alert using a configurable storage strategy.
    """

    def __init__(self) -> None:
        """
        Initialize the AlertObserver.

        Sets up alert processing, storage strategy,
        and a test-accessible last alert record.
        """
        self._processor = AlertProcessor()
        self._storage = StorageContext()
        self.last_alert: Dict[str, Any] | None = None  # initialize for test

    def update(self, data: Dict[str, Any]) -> None:
        """
        Handle notification when a metric exceeds the threshold.

        Args:
            data (Dict[str, Any]): Alert payload containing metric
            name and value.
        """
        metric = data["metric"]
        value = data["value"]

        # store last alert for testing
        self.last_alert = (metric, value)

        # real processing (optional, future-proof)
        alert_message = self._processor.process(data)
        self._storage.store(alert_message)
