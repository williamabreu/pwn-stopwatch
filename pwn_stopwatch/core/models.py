from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from pwn_stopwatch.core.utils import seconds_to_human_friendly

T = TypeVar("T")


@dataclass(frozen=True)
class StopwatchResponse(Generic[T]):
    elapsed_time_s: float  # seconds
    return_value: T

    @classmethod
    def create(
        cls, elapsed_time_s: float, return_value: T
    ) -> StopwatchResponse:
        return cls(elapsed_time_s=elapsed_time_s, return_value=return_value)

    @property
    def elapsed_time(self) -> str:
        return seconds_to_human_friendly(self.elapsed_time_s)
