from mpmath import *

from utils import possible_inputs_from_rounded


def test_rounding_2_digits():
    inp = mpf('123.45')
    outp = possible_inputs_from_rounded(inp, digits=2)
    assert mpf('123.445') in outp
    assert mpf('123.45499999') in outp
