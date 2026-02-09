from src.data_handlers.analytics import MetricsAnalytics


def test_percentiles():
    """
    Verify that percentile calculation includes the 95th percentile.

    This test ensures that the `percentiles` method returns
    a DataFrame indexed with expected percentile values.
    """
    data = {"cpu": [10, 20, 30, 40, 100]}
    analytics = MetricsAnalytics(data)
    p = analytics.percentiles()
    assert 0.95 in p.index


def test_anomaly_detection():
    """
    Verify that anomaly detection identifies outliers.

    This test checks that the IQR-based anomaly detection
    flags extreme values as anomalies.
    """
    data = {"cpu": [10, 20, 30, 40, 1000]}
    analytics = MetricsAnalytics(data)
    anomalies = analytics.detect_anomalies()
    assert not anomalies.empty
