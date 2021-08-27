from sympy import Matrix, simplify, solve, pprint
from sympy.physics.units.quantities import Quantity
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

"""
Example of conversion of a matrix expression into a linear system. 
"""
p = Quantity('p')

x0 = Quantity('x0')
x1 = Quantity('x1')
x2 = Quantity('x2')
x3 = Quantity('x3')
x4 = Quantity('x4')
x5 = Quantity('x5')

f0 = Quantity('f0')
f1 = Quantity('f1')
f2 = Quantity('f2')
f3 = Quantity('f3')
f4 = Quantity('f4')
f5 = Quantity('f5')

X = Matrix([[1, x4, x1, x0],
            [0, 1, x2, x3],
            [0, 0, 1, x5],
            [0, 0, 0, 1]])
F = Matrix([[1, f4, f1, f0],
            [0, 1, f2, f3],
            [0, 0, 1, f5],
            [0, 0, 0, 1]])
Z = Matrix([[1, a, b, c],
            [0, 1, d, e],
            [0, 0, 1, f],
            [0, 0, 0, 1]])
# ? = Matrix([[1, g, h, i],
#             [0, 1, j, k],
#             [0, 0, 1, l],
#             [0, 0, 0, 1]])

I = Matrix.eye(4, 4)
#
#
# # ex = simplify((((X * F%p) * Z%p) * (Z * F%p)%p) - I)
# ex = simplify(X * F * Z * (Z * F).inv() - I)
# # ex = simplify((F * X * Z) * (Z * F).inv() - I)
# # print(repr(ex))
# sol = solve(ex)
#
# pprint(sol)

"""
   -(-f4 + x4)      -(-4⋅f1 + f2⋅f4 - f2⋅x4 + f4⋅x2 + 4⋅x1 - x2⋅x4)     
a: ────────────, b: ────────────────────────────────────────────────, 
        2                                  8                                

   -(-8⋅f0 + 2⋅f1⋅f5 + 2⋅f1⋅x5 - f2⋅f4⋅f5 - f2⋅f4⋅x5 - f2⋅f5⋅x4 - f2⋅x4⋅x5 + 2⋅f3⋅f4- 2⋅f3⋅x4 + 2⋅f4⋅f5⋅x2 - 2⋅f4⋅x2⋅x5 + 2⋅f4⋅x3 - 2⋅f5⋅x1 + 4⋅f5⋅x2⋅x4 + 8⋅x0 -2⋅x1⋅x5 - 2⋅x3⋅x4)
c: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                    16                                                                    

   -(-f2 + x2)      -f2⋅f5 - f2⋅x5 + 4⋅f3 + f5⋅x2 + x2⋅x5 - 4⋅x3
d: ────────────, e: ────────────────────────────────────────────
        2                                8              

   -(-f5 + x5) 
f: ────────────
        2      
"""

A = Matrix([[1, a, b, c, d],
            [0, 1, e, f, g],
            [0, 0, 1, h, i],
            [0, 0, 0, 1, j],
            [0, 0, 0, 0, 1]])
B = Matrix([[1, q, r, s, t],
            [0, 1, u, v, w],
            [0, 0, 1, x, y],
            [0, 0, 0, 1, z],
            [0, 0, 0, 0, 1]])

pprint(A * B)

A = Matrix([[1, a, b, c],
            [0, 1, d, e],
            [0, 0, 1, f],
            [0, 0, 0, 1]])
B = Matrix([[1, q, r, s],
            [0, 1, t, u],
            [0, 0, 1, v],
            [0, 0, 0, 1]])
print()
pprint(A * B)
# pprint(solve(A*B-B*A))
exit()

p=4000000000
pprint(solve(p ** 3 * x ** 3 - 2 ** 192))
