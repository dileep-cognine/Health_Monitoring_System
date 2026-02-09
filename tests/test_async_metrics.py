import pytest
# from src.async_collectors.metrics_collector import fetch_metrics
from src.async_collectors.metrics_collector import AsyncMetricsCollector

"""
Test suite for asynchronous metrics collection.

These tests focus on the public async API (`collect`) rather than
private implementation details such as `_fetch_metrics`.
"""


@pytest.mark.asyncio
async def test_async_fetch():
    """
    Verify that the async metrics collector returns a list.

    This test validates the structure of the response when
    invoking the public `collect` method with no endpoints.
    """
    collector = AsyncMetricsCollector()

    # Use a fake endpoint list (structure test only, no real HTTP)
    results = await collector.collect([])

    assert isinstance(results, list)

