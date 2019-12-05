from lib.intervals import *

HALF = Float(1) / Float(2)


def possible_inputs_from_rounded(n, digits=2) -> I:
    exp = Float(10)**digits
    shifted = n * exp
    valid_range = I(shifted - HALF, shifted + HALF)
    return valid_range / exp
