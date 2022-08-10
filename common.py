import sys
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
