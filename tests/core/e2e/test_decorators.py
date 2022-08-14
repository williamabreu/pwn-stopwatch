from pwn_stopwatch.core.decorators import stopwatch


@stopwatch
def foo(val):
    return val


def test_stopwatch():
    stopwatch_response = foo("dummy")
    assert stopwatch_response.return_value == "dummy"
    assert isinstance(stopwatch_response.elapsed_time_s, float)
    assert isinstance(stopwatch_response.elapsed_time, str)
