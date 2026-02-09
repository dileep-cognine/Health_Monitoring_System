import sqlite3


def insert_metric(conn: sqlite3.Connection, metric: str, value: float) -> None:
    """
    Insert a metric record into the database securely.

    This function uses a parameterized SQL query to prevent
    SQL injection attacks and ensure safe data insertion.

    Args:
        conn (sqlite3.Connection): Active SQLite database connection.
        metric (str): Name of the metric.
        value (float): Numeric value of the metric.

    Returns:
        None
    """
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO metrics (metric, value) VALUES (?, ?)",
        (metric, value),
    )
    conn.commit()
