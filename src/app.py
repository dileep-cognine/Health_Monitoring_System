import asyncio
from src.metaclasses.config_manager import ConfigManager
from src.patterns.observer import MetricMonitor, AlertObserver


class MonitoringApp:
    """
    Main application class for the monitoring system.

    Coordinates configuration loading, metric collection,
    threshold evaluation, and alert notification.
    """

    def __init__(self) -> None:
        """
        Initialize the monitoring application.

        Sets up configuration, metric monitor, and registers
        alert observers.
        """
        self._config = ConfigManager()
        self._monitor = MetricMonitor()
        self._monitor.register_observer(AlertObserver())

    async def run_once(self):
        """
        Execute a single monitoring cycle.

        Fetches metrics from configured endpoints and evaluates
        them against thresholds.
        """
        endpoints = self._config.get("METRIC_ENDPOINTS", [])

        for endpoint in endpoints:
            metrics = await self._fetcher.fetch_metrics(endpoint)

            if metrics:
                self._monitor.update_metrics(metrics)

    async def run_forever(self):
        """
        Run the monitoring loop continuously.

        Periodically executes monitoring cycles based on the
        configured polling interval and handles graceful shutdown.
        """
        interval = int(self._config.get("POLL_INTERVAL", 5))

        print(" Monitoring system running continuously")

        try:
            while True:
                await self.run_once()
                await asyncio.sleep(interval)

        except asyncio.CancelledError:
            print(" Monitoring system shutting down gracefully...")
            raise


def main():
    """
    Application entry point.

    Starts the monitoring system and handles user-initiated shutdown.
    """
    app = MonitoringApp()

    try:
        asyncio.run(app.run_forever())
    except KeyboardInterrupt:
        print(" Shutdown requested by user")


if __name__ == "__main__":
    main()
