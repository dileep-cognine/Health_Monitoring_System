import gc
import weakref
from typing import Any


class DataCache:
    """
    Lightweight in-memory cache using weak references.

    Weak references allow cached objects to be garbage-collected
    automatically when no longer in use, preventing memory leaks.
    """

    def __init__(self, max_size: int = 100) -> None:
        """
        Initialize the cache.

        Args:
            max_size (int): Maximum number of items allowed in the cache.
        """
        self._cache: weakref.WeakValueDictionary[str, Any] = (
            weakref.WeakValueDictionary()
        )
        self._max_size = max_size

    def set(self, key: str, value: Any) -> None:
        """
        Store a value in the cache.

        Automatically evicts entries if cache size exceeds the limit.

        Args:
            key (str): Cache key.
            value (Any): Object to cache.
        """
        if len(self._cache) >= self._max_size:
            self._evict()

        self._cache[key] = value

    def get(self, key: str) -> Any | None:
        """
        Retrieve a value from the cache.

        Args:
            key (str): Cache key.

        Returns:
            Any | None: Cached object if present, otherwise None.
        """
        return self._cache.get(key)

    def _evict(self) -> None:
        """
        Evict the least-recently inserted item and trigger garbage collection.

        This helps reclaim memory and maintain cache size constraints.
        """
        try:
            first_key = next(iter(self._cache))
            del self._cache[first_key]
        except StopIteration:
            pass

        gc.collect()
