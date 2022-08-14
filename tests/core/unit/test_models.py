from uuid import uuid4

import pytest

from pwn_stopwatch.core.models import StopwatchResponse
from tests.core.conftest import SECONDS_TO_HUMAN_FRIENDLY_PARAMS


@pytest.mark.parametrize(
    "seconds, expected_response", SECONDS_TO_HUMAN_FRIENDLY_PARAMS
)
def test_stopwatch_response(seconds, expected_response):
    rand_value = uuid4()
    stopwatch_response = StopwatchResponse.create(seconds, rand_value)
    assert stopwatch_response.elapsed_time_s == seconds
    assert stopwatch_response.elapsed_time == expected_response
    assert stopwatch_response.return_value == rand_value
