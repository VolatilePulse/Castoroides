from lib.intervals import *


def test_interval_functions():
    iv1 = I(2, 10)
    iv2 = I(0, 5)

    assert iv1 & iv2 == I(2, 5)
    assert iv1 | iv2 == I(0, 10)
    assert iv1.overlaps(iv2)

    assert not iv1.is_inf()
    assert I(-inf, 0).is_inf()

    assert list(iv2.contained_ints()) == [0, 1, 2, 3, 4, 5]
