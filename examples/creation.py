# Creating flexible hashes
from garoupa import Hash

# Binary strings are hashed by MD5.
a = Hash(b"Some text.")
print(f"Hex:\n{a.hex}")
# ...

# A shorter base-62 identifier is also provided as default.
print(a.id, "=", a)
# ...

# Integers are not hashed, they are directly mapped to the hash space.
print(a.n)
# ...
print(Hash(126501587258562921197401139372367452908), "=", a)
# ...

b = Hash(340282366920938463463374607431768211455)  # Largest posible number.
print(b)
# ...
