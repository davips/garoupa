# Basic operations
from hosh import Hash

# Hashes can be multiplied.
a = Hash(blob=b"Some large binary content...")
b = Hash(blob=b"Some other binary content. Might be, e.g., an action or another large content.")
c = a * b
print(f"{a} * {b} = {c}")
# ...
print(~b)
# Multiplication can be reverted by the inverse hash. Zero is the identity hash.
print(f"{b} * {~b} = {b * ~b} = 0")
# ...

print(f"{c} * {~b} = {c * ~b} = {a} = a")
# ...

print(f"{~a} * {c} = {~a * c} = {b} = b")
# ...

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
# ...

# Hash multiplication is not expected to be commutative.
print(f"{a * b} != {b * a}")
# ...

# Hash multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
# ...

