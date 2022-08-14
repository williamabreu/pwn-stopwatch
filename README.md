# PWN Stopwatch

A module to measure how long a function takes to run

## Usage

See an example of usage of the stopwatch decorator:

```python
from pwn_stopwatch import stopwatch
from time import sleep

@stopwatch
def zzz(n: int) -> None:
    sleep(n)
```
```
>>> res = zzz(1)
>>> print(res.elapsed_time)
1s 11ms
```
