import numpy as np
cimport numpy as np
cimport cython
from numpy.polynomial.legendre import leggauss
from cython.parallel import prange

DTYPE = np.float64
ctypedef np.float64_t DTYPE_t
ctypedef DTYPE_t (*f_type)(DTYPE_t)

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
def gl_integrate_1d(func, np.ndarray[DTYPE_t, ndim=1] grid, np.int_t roots_count):
    (roots, weights) = leggauss(roots_count)
    cdef DTYPE_t sum = 0.0
    cdef DTYPE_t inner_sum
    for grid_i in range(grid.shape[0] - 1):
        inner_sum = 0.0
        for root_i in range(roots_count):
            inner_sum += weights[root_i] * func(
                (grid[grid_i + 1] + grid[grid_i]) / 2.0 + ((grid[grid_i + 1] - grid[grid_i]) / 2.0) * roots[root_i])
        sum += ((grid[grid_i + 1] - grid[grid_i]) / 2.0) * inner_sum
    return sum
