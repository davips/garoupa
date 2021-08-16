# Basic operations
from garoupa import Hosh

# Hoshes (operable hash-based elements) can be multiplied.
from garoupa import identity64

a = Hosh(blob=b"Some large binary content...")
b = Hosh(blob=b"Some other binary content. Might be, e.g., an action or another large content.")
c = a * b
print(f"{a} * {b} = {c}")
# ...
print(~b)
# Multiplication can be reverted by the inverse hosh. Zero is the identity hosh.
print(f"{b} * {~b} = {b * ~b} = 0")
# ...

print(f"{b} * {identity64} = {b * identity64} = b")
# ...

print(f"{c} * {~b} = {c * ~b} = {a} = a")
# ...

print(f"{~a} * {c} = {~a * c} = {b} = b")
# ...

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
# ...

# Hosh multiplication is not expected to be commutative.
print(f"{a * b} != {b * a}")
# ...

# Hosh multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
# ...

