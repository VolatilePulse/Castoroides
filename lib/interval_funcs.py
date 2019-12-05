from math import ceil, floor
from typing import Iterable

from mpmath import inf
from mpmath import mpf as Float
from mpmath import mpi as I


class IntervalError(Exception):
    pass


def hull() -> I:
    pass


def intersection(iv1: I, iv2: I) -> I:
    lower = max(iv1.a, iv2.a)
    upper = min(iv1.b, iv2.b)
    if lower <= upper:
        return I(lower, upper)
    return None


def union(iv1: I, iv2: I) -> I:
    if not overlaps(iv1, iv2):
        raise IntervalError(f'{iv1} doesn\'t overlap {iv2}')
    lower = min(iv1.a, iv2.a)
    upper = max(iv1.b, iv2.b)
    return I(lower, upper)


def overlaps(iv1: I, iv2: I) -> I:
    return (iv1.a < iv2.b and iv1.a > iv2.a) or (iv1.b < iv2.b and iv1.b > iv2.b)


def contained_ints(iv: I, extend_down=False, extend_up=False) -> Iterable[int]:
    if iv.is_inf():
        raise IntervalError(f'{iv} contains infinity')
    lower = floor(Float(iv.a)) if extend_down else ceil(Float(iv.a))
    upper = ceil(Float(iv.b)) if extend_up else floor(Float(iv.b))

    # range doesn't include the 'stop' value, increment one over it
    for i in range(lower, upper + 1):
        yield i


def is_inf(iv: I) -> bool:
    return inf in abs(iv)
