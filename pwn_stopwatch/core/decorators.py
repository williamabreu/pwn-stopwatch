from time import perf_counter
from typing import Any, Callable, TypeVar

from pwn_stopwatch.core.models import StopwatchResponse

T = TypeVar("T")


def stopwatch(func: Callable[..., T]) -> Callable[..., StopwatchResponse[T]]:
    def wrapper(*args: Any, **kwargs: Any) -> StopwatchResponse[T]:
        # Start the stopwatch.
        start = perf_counter()
        # Perform the function call.
        response = func(*args, **kwargs)
        # Stop the stopwatch.
        stop = perf_counter()

        return StopwatchResponse.create(
            elapsed_time_s=stop - start, return_value=response
        )

    return wrapper
