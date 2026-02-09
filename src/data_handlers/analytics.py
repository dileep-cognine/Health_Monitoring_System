import pandas as pd
import numpy as np
from typing import Dict


class MetricsAnalytics:
    """
    Performs statistical analysis and anomaly detection on numeric metrics.

    This class converts raw metric data into a Pandas DataFrame and provides
    utility methods for percentile analysis and anomaly detection.
    """

    def __init__(self, metrics: Dict[str, list[float]]) -> None:
        """
        Initialize MetricsAnalytics with metric data.

        Args:
            metrics (Dict[str, list[float]]): Dictionary where keys are metric
            names and values are lists of numeric observations.
        """
        self.df = pd.DataFrame(metrics)

    def percentiles(self) -> pd.DataFrame:
        """
        Compute key percentiles for all metrics.

        Returns:
            pd.DataFrame: DataFrame containing 25th, 50th, 75th,
            and 95th percentiles for each metric.
        """
        return self.df.quantile([0.25, 0.50, 0.75, 0.95])

    def detect_anomalies(self) -> pd.DataFrame:
        """
        Detect anomalies using the Interquartile Range (IQR) method.

        This approach is robust for small and non-normally distributed datasets.

        Returns:
            pd.DataFrame: Rows containing anomalous values across all metrics.
        """
        anomalies = pd.DataFrame()

        for column in self.df.columns:
            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)
            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            mask = (self.df[column] < lower) | (self.df[column] > upper)
            anomalies = pd.concat([anomalies, self.df[mask]])

        return anomalies.drop_duplicates()
