# Operations between flexible hashes
from garoupa import Hash

# Hashes can be multiplied.
a = Hash(b"Some text.")
b = Hash(b"Other text.")
c = a * b
print(f"{a} * {b} = {c}")
# ...

# Multiplication can be reverted by the inverse hash. Zero is the identity hash.
print(f"{b} * {b.inv} = {b * b.inv} = 0")
# ...

print(f"{c} * {b.inv} = {c * b.inv} = {a} = a")
# ...

print(f"{a.inv} * {c} = {a.inv * c} = {b} = b")
# ...

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
# ...

# Hash multiplication is not commutative.
print(f"{a * b} != {b * a}")
# ...

# Hash multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
# ...
