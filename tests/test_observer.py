from src.patterns.observer import MetricMonitor
from src.patterns.observer import AlertObserver


def test_alert_trigger():
    """
    Verify that an alert is triggered when a metric exceeds the threshold.

    This test ensures that the MetricMonitor notifies registered observers
    and that the AlertObserver records the alert when the threshold is crossed.
    """
    monitor = MetricMonitor()
    observer = AlertObserver()
    monitor.register_observer(observer)

    d = {"cpu": 95.0}
    monitor.update_metrics(d)

    assert observer.last_alert is not None