from mpmath import inf, iv, mpf, mpi
from mpmath.ctx_iv import ivmpf

from lib.interval_funcs import *

mpf.pretty = True
iv.pretty = True

Float = mpf
I = mpi

ivmpf.__and__ = intersection
ivmpf.__or__ = union
ivmpf.contained_ints = contained_ints
ivmpf.intersection = intersection
ivmpf.overlaps = overlaps
ivmpf.union = union

ivmpf.is_inf = is_inf
