#  Copyright (c) 2021. Gabriel Dalforno
#  This file is part of the garoupa project.
#  Please respect the license - more about this in the section (*) below.
#
#  garoupa is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  garoupa is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with garoupa.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.

import numpy as np


p = 4294967291  
n = 4


def order(p:int)->int:
    """Order of the group"""
    return p**6


def PU(p:int)->float:
    """Degree of commutativity"""
    return (2*(p**3) + p**2 - 2*p)/orderU(p)


def order_hist(p:int)->dict:
    """Order histogram"""
    return {
        1:1,
        p:order(p)-1
    }


def product(U:np.ndarray, V:np.ndarray)->np.ndarray:
    """Multiply two matrices mod p"""
    return (U@V)%p


def invert(U:np.ndarray)->np.ndarray:
    """Computes inverse mod p"""
    A1 = (-U[0, 1])%p
    A4 = (-U[1, 2])%p
    A6 = (-U[2, 3])%p
    A2 = (-U[0, 1]*A4 - U[0, 2])%p
    A5 = (-U[1, 2]*A6 - U[1, 3])%p
    A3 = (-U[0, 1]*A5 - U[0, 2]*A6 - U[0, 3])%p
    return np.array([
            [1, A1, A2, A3],
            [0, 1, A4, A5],
            [0, 0, 1, A6],
            [0, 0, 0, 1]
    ])


def power(U:np.ndarray, k:int)->np.ndarray:
    """Computes U^k mod p"""
    return np.linalg.matrix_power(U, k)%p


def int_to_elem(N:int)->np.ndarray:
    """Maps integer to unitriangular matrix mod p"""
    assert N>=0 and N<p**6
    A = np.zeros(6)
    i = 0
    while N!=0:
        N, r = divmod(N, p)
        A[i] = r
        i += 1
    return np.array([
        [1, A[0], A[4], A[5]],
        [0, 1, A[2], A[3]],
        [0, 0, 1, A[1]],
        [0, 0, 0, 1]
    ], dtype=np.int64)


def elem_to_int(U:np.ndarray)->int:
    """Maps unitriangular matrix mod p to integer"""
    A = [U[0, 1], U[2, 3], U[1, 2], U[1, 3], U[0, 2], U[0, 3]]
    N = 0
    for k in range(6):
        N += A[k]*(p**k)
    return int(N)


#### More elegant solution to invert a matrix, but an overkill for n=4 ####
#def solve(U:np.ndarray, b:np.ndarray)->np.ndarray:
#    """Solves Ux=b mod p"""
#    x = np.zeros(n, dtype=np.int64)
#    for i in range(1, n+1):
#        x[n-i] = b[n-i]
#        for j in range(i-1, 0, -1):
#            x[n-i] += (-U[n-i,n-j]*x[n-j])%p
#    return x


#def invert(U:np.ndarray)->np.ndarray:
#    """Computes inverse mod p"""
#    V = np.zeros([n, n], dtype=np.int64)
#    for i in range(n):
#        b = np.zeros(n, dtype=np.int64)
#        b[i] = 1
#        V[:,i] = solve(U, b)
#    return V
