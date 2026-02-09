def process_metrics(metrics: list[float]) -> list[float]:
    """
    Process metrics using an optimized implementation.

    The average is computed once, reducing time complexity
    from O(n²) to O(n).

    Args:
        metrics (list[float]): List of metric values.

    Returns:
        list[float]: Values greater than the computed average.
    """
    avg = sum(metrics) / len(metrics)
    return [value for value in metrics if value > avg]
