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
from math import factorial

from hosh.algebra.cyclic import Z
from hosh.algebra.dihedral import D

# Direct product between:
#   symmetric group S4;
#   cyclic group Z5; and,
#   dihedral group D4.
from hosh.algebra.symmetric import S
from hosh.algebra.symmetric.perm import Perm

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
«[0, 2, 1, 3], 2, r4»	*	«[2, 0, 3, 1], 0, s1»	=	«[1, 0, 3, 2], 2, s1»
«[3, 1, 0, 2], 1, s2»	*	«[1, 0, 3, 2], 0, r0»	=	«[1, 3, 2, 0], 1, s2»
«[1, 0, 3, 2], 1, s7»	*	«[3, 0, 1, 2], 1, r6»	=	«[2, 1, 0, 3], 2, s1»
«[0, 2, 1, 3], 2, r1»	*	«[2, 1, 0, 3], 2, s1»	=	«[1, 2, 0, 3], 4, s2»
«[1, 3, 0, 2], 1, s4»	*	«[3, 0, 1, 2], 3, r4»	=	«[2, 1, 3, 0], 4, s0»
"""
```

```python3

# Operator ~ is another way of sampling. Group S35 modulo 2^128.
G = S(35, 2 ** 128)
print(~G)
"""
[17, 32, 23, 1, 20, 26, 16, 28, 13, 21, 27, 0, 31, 24, 29, 14, 4, 8, 7, 19, 10, 11, 18, 2, 30, 12, 34, 33, 3, 15, 22, 5, 6, 9, 25]
"""
```

```python3

# Manual element creation. Group S35 modulo 2^128.
last_perm_i = factorial(35) - 1
last_128bit = 2 ** 128 - 1
a = Perm(i=last_perm_i, n=35, m=last_128bit)
print(a.i, "=", last_perm_i % last_128bit, sep="\t")
"""
124676958757991025765413114570153656349	=	124676958757991025765413114570153656349
"""
```

```python3

# Inverse element. Group S4 modulo 20.
a = Perm(i=21, n=4, m=20)
b = Perm(i=17, n=4, m=20)
print(a, "*", -a, "=", (a * -a).i, "=", a * -a)
"""
[1, 0, 2, 3] * [1, 0, 2, 3] = 0 = [0, 1, 2, 3]
"""
```

```python3

print(a, "*", b, "=", a * b)
"""
[1, 0, 2, 3] * [1, 2, 3, 0] = [0, 2, 3, 1]
"""
```

```python3

print(a, "*", b, "*", -b, "=", a * b * -b)
"""
[1, 0, 2, 3] * [1, 2, 3, 0] * [3, 0, 1, 2] = [1, 0, 2, 3]
"""
```


</p>
</details>



### Features
