from mpmath import mpi


def test_nothing():
    b = mpi(0.1)
    assert mpi('0.1') in b is False
