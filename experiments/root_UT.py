from functools import reduce

import numpy as np


def recursive_coef1(k: int) -> int:
    if k == 2:
        return 1
    else:
        return recursive_coef1(k - 1) + (k - 1)


def recursive_coef2(k: int) -> int:
    if k == 2:
        return 0
    else:
        return recursive_coef1(k - 1) + recursive_coef2(k - 1)


def kth_root(x: np.array, p: int, k: int) -> np.array:
    # x: matrix in UT(4, p)
    # p: prime number
    # k: integer s.t. 2 <= k <= p-1
    # returns the kth root of x

    y = np.eye(4, dtype=np.uint64)

    divk = pow(k, -1, p)
    C1 = recursive_coef1(k)
    C2 = recursive_coef2(k)

    y[0, 1] = (x[0, 1] * divk) % p
    y[1, 2] = (x[1, 2] * divk) % p
    y[2, 3] = (x[2, 3] * divk) % p

    y[0, 2] = ((x[0, 2] - C1 * y[0, 1] * y[1, 2]) * divk) % p
    y[1, 3] = ((x[1, 3] - C1 * y[1, 2] * y[2, 3]) * divk) % p

    y[0, 3] = ((x[0, 3] - C1 * y[0, 1] * y[1, 3] - C1 * y[0, 2] * y[2, 3] - C2 * y[0, 1] * y[1, 2] * y[2, 3]) * divk) % p

    return y

###########################################################################
# x in UT(4, p)
# computes y such that y^k = x

p = 1099511627689
# p = 1097
k = 22

x = np.array([
    [1, 2, 3, 4],
    [0, 1, 5, 6],
    [0, 0, 1, 7],
    [0, 0, 0, 1]], dtype=np.uint64
)

y = kth_root(x, p, k)
print(f"\nx = \n{x}")
print(f"\ny = \n{y}")


def m(a, b):
    return (a @ b) % p


y7 = reduce(m, [y] * k)
print(f"\ny^{k} = \n{y7}")
print((y7 == x).all())

# print(timeit(lambda: kth_root(x, p, k), number=1000), "ms")
