from typing import Generator


def read_log_file(filepath: str) -> Generator[str, None, None]:
    """
    Read a log file line by line using a generator.

    This approach uses O(1) memory and is suitable for large files.

    Args:
        filepath (str): Path to the log file.

    Yields:
        str: Stripped log line.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def filter_lines(
    lines: Generator[str, None, None],
    keyword: str
) -> Generator[str, None, None]:
    """
    Filter log lines that contain a specific keyword.

    Args:
        lines (Generator[str]): Generator of log lines.
        keyword (str): Keyword to filter by.

    Yields:
        str: Log lines containing the keyword.
    """
    for line in lines:
        if keyword in line:
            yield line


def parse_metrics(
    lines: Generator[str, None, None]
) -> Generator[dict, None, None]:
    """
    Parse metric lines into structured dictionaries.

    Expected input format:
        METRIC_NAME=VALUE

    Args:
        lines (Generator[str]): Generator of metric log lines.

    Yields:
        dict: Parsed metric with keys "metric" and "value".
    """
    for line in lines:
        try:
            metric, value = line.split("=")
            yield {
                "metric": metric,
                "value": float(value)
            }
        except ValueError:
            continue
