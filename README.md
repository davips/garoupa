![test](https://github.com/davips/hoshy/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/hoshy/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/hoshy)

# hoshy
Cryptographic hash (half-blake3) and operators - see package hosh for a faster, native (compiled) approach.
The only external dependence is blake3.

Hoshy hosts also some niceties for group theory experimentation.

## Python installation
### from package
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI
pip install hoshy
```

### from source
```bash
cd my-project
git clone https://github.com/davips/hoshy ../hoshy
pip install -e ../hoshy
```


### Examples
**Basic operations**
<details>
<p>

```python3
from hosh import Hash

# Hashes can be multiplied.
a = Hash(blob=b"Some large binary content...")
b = Hash(blob=b"Some other binary content. Might be, e.g., an action or another large content.")
c = a * b
print(f"{a} * {b} = {c}")
"""
0v58YxIhaae5NfYuXsoC1i * 04orKjYHAZraYORILOVwos = 3yT1A5oLlW2HpjSkgzo2yg
"""
```

```python3
print(~b)
# Multiplication can be reverted by the inverse hash. Zero is the identity hash.
print(f"{b} * {~b} = {b * ~b} = 0")
"""
211eErwhEiGnit0beo4tjo
04orKjYHAZraYORILOVwos * 211eErwhEiGnit0beo4tjo = 0000000000000000000000 = 0
"""
```

```python3

print(f"{b} * {Hash(0)} = {b * Hash(0)} = b")
"""
04orKjYHAZraYORILOVwos * 0000000000000000000000 = 04orKjYHAZraYORILOVwos = b
"""
```

```python3

print(f"{c} * {~b} = {c * ~b} = {a} = a")
"""
3yT1A5oLlW2HpjSkgzo2yg * 211eErwhEiGnit0beo4tjo = 0v58YxIhaae5NfYuXsoC1i = 0v58YxIhaae5NfYuXsoC1i = a
"""
```

```python3

print(f"{~a} * {c} = {~a * c} = {b} = b")
"""
4q4X1jczNK2eKCV4uxEPNk * 3yT1A5oLlW2HpjSkgzo2yg = 04orKjYHAZraYORILOVwos = 04orKjYHAZraYORILOVwos = b
"""
```

```python3

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
"""
3yT1A5oLlW2HpjSkgzo2yg / 04orKjYHAZraYORILOVwos = 0v58YxIhaae5NfYuXsoC1i = a
"""
```

```python3

# Hash multiplication is not expected to be commutative.
print(f"{a * b} != {b * a}")
"""
3yT1A5oLlW2HpjSkgzo2yg != 4AvOF9Fbhakd26mosfuuvR
"""
```

```python3

# Hash multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
"""
51UdYbEAGI5mVogE4aFFKe = 51UdYbEAGI5mVogE4aFFKe
"""
```

```python3


```


</p>
</details>

**Abstract algebra module**
<details>
<p>

```python3
from itertools import islice
from hosh.algebra.cyclic import Z
from hosh.algebra.dihedral import D
from hosh.algebra.symmetric import S

# Direct product between:
#   symmetric group S4;
#   cyclic group Z5; and,
#   dihedral group D4.
G = S(4) * Z(5) * D(4)
print(G)
"""
S4×Z5×D4
"""
```

```python3

# Sampling and operating over some pairs.
fetch5 = islice(G, 0, 5)
for a, b in zip(fetch5, G):
    print(a, "*", b, "=", a * b, sep="\t")
"""
«[2, 0, 3, 1], 0, s7»	*	«[3, 0, 1, 2], 1, s3»	=	«[1, 2, 0, 3], 1, r0»
«[0, 3, 1, 2], 3, s4»	*	«[1, 0, 3, 2], 0, r5»	=	«[3, 0, 2, 1], 3, s3»
«[0, 1, 2, 3], 3, s3»	*	«[2, 0, 3, 1], 3, s3»	=	«[2, 0, 3, 1], 1, r0»
«[1, 2, 0, 3], 2, r7»	*	«[1, 2, 0, 3], 1, s2»	=	«[2, 0, 1, 3], 3, s1»
«[0, 2, 1, 3], 1, r1»	*	«[0, 3, 1, 2], 2, s1»	=	«[0, 3, 2, 1], 3, s2»
"""
```


</p>
</details>



### Features
