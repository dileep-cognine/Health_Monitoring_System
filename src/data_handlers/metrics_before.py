def process_metrics(metrics: list[float]) -> list[float]:
    """
    Process metrics using an inefficient implementation.

    This version recalculates the average for every element,
    resulting in poor performance for large datasets.

    Args:
        metrics (list[float]): List of metric values.

    Returns:
        list[float]: Values greater than the computed average.
    """
    result = []
    for value in metrics:
        if value > sum(metrics) / len(metrics):  # repeated computation
            result.append(value)
    return result
