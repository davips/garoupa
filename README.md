# garoupa
**WARNING: This project is still subject to major changes, e.g., in the next rewrite.**

Incremental cryptography and flexible hash

<a title="fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Malabar_grouper_melb_aquarium.jpg"><img width="256" alt="Malabar grouper melb aquarium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg"></a>

**Creating flexible hashes**
<details>
<p>

```python3
from garoupa import Hash

# Binary strings are hashed by MD5.
a = Hash(b"Some text.")
print(f"Hex:\n{a.hex}")
"""
Hex:
5f2b51ca2fdc5baa31ec02e002f69aec
"""
```

```python3

# A shorter base-62 identifier is also provided as default.
print(a.id, "=", a)
"""
2ta4DsTtzJxNXItOSQfcfE = 2ta4DsTtzJxNXItOSQfcfE
"""
```

```python3

# Integers are not hashed, they are directly mapped to the hash space.
print(a.n)
"""
126501587258562921197401139372367452908
"""
```

```python3
print(Hash(126501587258562921197401139372367452908), "=", a)
"""
2ta4DsTtzJxNXItOSQfcfE = 2ta4DsTtzJxNXItOSQfcfE
"""
```

```python3

b = Hash(340282366920938463463374607431768211455)  # Largest posible number.
print(b)
"""
7n42DGM5Tflk9n8mt7Fhc7
"""
```


</p>
</details>

**Operations between flexible hashes**
<details>
<p>

```python3
from garoupa import Hash

# Hashes can be multiplied.
a = Hash(b"Some text.")
b = Hash(b"Other text.")
c = a * b
print(f"{a} * {b} = {c}")
"""
2ta4DsTtzJxNXItOSQfcfE * 1s2qEnAwwi16V2hCUYV8dY = 3EYMMabJR2Aj8rUtPiZ1gO
"""
```

```python3

# Multiplication can be reverted by the inverse hash. Zero is the identity hash.
print(f"{b} * {b.inv} = {b * b.inv} = 0")
"""
1s2qEnAwwi16V2hCUYV8dY * 1he9mgDNZUsKtjzHTFTWsW = 0000000000000000000000 = 0
"""
```

```python3

print(f"{c} * {b.inv} = {c * b.inv} = {a} = a")
"""
3EYMMabJR2Aj8rUtPiZ1gO * 1he9mgDNZUsKtjzHTFTWsW = 2ta4DsTtzJxNXItOSQfcfE = 2ta4DsTtzJxNXItOSQfcfE = a
"""
```

```python3

print(f"{a.inv} * {c} = {a.inv * c} = {b} = b")
"""
2PMEzPHCsQn8cSxy31ohvo * 3EYMMabJR2Aj8rUtPiZ1gO = 1s2qEnAwwi16V2hCUYV8dY = 1s2qEnAwwi16V2hCUYV8dY = b
"""
```

```python3

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
"""
3EYMMabJR2Aj8rUtPiZ1gO / 1s2qEnAwwi16V2hCUYV8dY = 2ta4DsTtzJxNXItOSQfcfE = a
"""
```

```python3

# Hash multiplication is not commutative.
print(f"{a * b} != {b * a}")
"""
3EYMMabJR2Aj8rUtPiZ1gO != 3SemNwugPbPPwm6wXaYFqi
"""
```

```python3

# Hash multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
"""
021EieFLdrV69bPx1ddPJA = 021EieFLdrV69bPx1ddPJA
"""
```


</p>
</details>

<<benchmark>>
