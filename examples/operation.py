# Basic operations
from garoupa import Hosh, ø  # ø is a shortcut for identity32 (AltGr+O in most keyboards)

# Hoshes (operable hash-based elements) can be multiplied.
a = Hosh(content=b"Some large binary content...")
b = Hosh(content=b"Some other binary content. Might be, e.g., an action or another large content.")
c = a * b
print(f"{a} * {b} = {c}")
# ...
print(~b)
# Multiplication can be reverted by the inverse hosh. Zero is the identity hosh.
print(f"{b} * {~b} = {b * ~b} = 0")
# ...

print(f"{b} * {ø} = {b * ø} = b")
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

