import sys
import tracemalloc
from _thread import interrupt_main
from contextlib import contextmanager
from functools import wraps
from threading import Timer
from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class Comparable(Protocol):
    def __ge__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...

    def __le__(self, other: Any) -> bool:
        ...

    def __lt__(self, other: Any) -> bool:
        ...


CT = TypeVar("CT", bound=Comparable)


def recursion_limit(limit: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            limit_old = sys.getrecursionlimit()
            sys.setrecursionlimit(limit)
            value = func(*args, **kwargs)
            sys.setrecursionlimit(limit_old)
            return value

        return wrapper

    return decorator


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    timer = Timer(seconds, lambda: interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt as e:
        raise TimeoutException("operation timed out") from e
    finally:
        timer.cancel()


TRACE_FILTERS = (
    tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
    tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
    tracemalloc.Filter(False, "<unknown>"),
    tracemalloc.Filter(False, __file__),
    tracemalloc.Filter(False, tracemalloc.__file__),
)


# Not working?
@contextmanager
def memory_limit(size: int):
    if not tracemalloc.is_tracing():
        tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot()

    yield

    snapshot2 = tracemalloc.take_snapshot().filter_traces(TRACE_FILTERS)
    snapshot1 = snapshot1.filter_traces(TRACE_FILTERS)

    snapshot = snapshot2.compare_to(snapshot1, "lineno")

    try:
        used_size = sum(stat.size_diff for stat in snapshot)
        if used_size > size:
            raise AttributeError(
                f"Memory usage {used_size} exceeded the threshold {size}"
            )
    finally:
        tracemalloc.stop()
