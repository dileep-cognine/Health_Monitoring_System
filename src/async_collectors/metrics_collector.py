import asyncio
from typing import List, Dict, Any
import aiohttp

from src.metaclasses.config_manager import ConfigManager


class AsyncMetricsCollector:
    """
    Asynchronously collects system or application metrics
    from multiple HTTP endpoints using aiohttp.

    This class is designed for high-concurrency environments
    where metrics must be fetched in parallel with timeout handling.
    """

    def __init__(self) -> None:
        """
        Initialize the AsyncMetricsCollector.

        Loads configuration values such as request timeout
        using the ConfigManager.
        """
        self._config = ConfigManager()
        self._timeout = self._config.get("ASYNC_TIMEOUT")

    async def _fetch_metrics(
        self,
        session: aiohttp.ClientSession,
        url: str
    ) -> Dict[str, Any]:
        """
        Fetch metrics from a single HTTP endpoint.

        Args:
            session (aiohttp.ClientSession): Shared HTTP session.
            url (str): Metrics endpoint URL.

        Returns:
            Dict[str, Any]: Parsed JSON response on success,
            or an error dictionary containing the failure reason.
        """
        try:
            async with session.get(url, timeout=self._timeout) as response:
                response.raise_for_status()
                return await response.json()

        except asyncio.TimeoutError:
            return {"error": "timeout", "url": url}

        except aiohttp.ClientError as exc:
            return {"error": str(exc), "url": url}

    async def collect(
        self,
        endpoints: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Collect metrics concurrently from multiple endpoints.

        Args:
            endpoints (List[str]): List of metrics endpoint URLs.

        Returns:
            List[Dict[str, Any]]: List of metric responses or error objects,
            one per endpoint, preserving input order.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self._fetch_metrics(session, url))
                for url in endpoints
            ]

            return await asyncio.gather(*tasks, return_exceptions=False)


async def shutdown(tasks: List[asyncio.Task]) -> None:
    """
    Gracefully cancel and await completion of asyncio tasks.

    This ensures all tasks are properly cancelled and any
    cancellation exceptions are suppressed.

    Args:
        tasks (List[asyncio.Task]): List of running asyncio tasks.
    """
    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)
