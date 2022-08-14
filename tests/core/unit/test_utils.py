import pytest

from pwn_stopwatch.core.utils import seconds_to_human_friendly
from tests.core.conftest import SECONDS_TO_HUMAN_FRIENDLY_PARAMS


@pytest.mark.parametrize(
    "seconds, expected_response", SECONDS_TO_HUMAN_FRIENDLY_PARAMS
)
def test_seconds_to_human_friendly(seconds, expected_response):
    response = seconds_to_human_friendly(seconds)
    assert response == expected_response
