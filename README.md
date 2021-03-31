![test](https://github.com/davips/garoupa/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/garoupa/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/garoupa)

# garoupa
Cryptographic hash, abstract algebra and operators - see package [hosh](https://github.com/davips/hosh) for a faster, native (compiled) hash/ops approach.

<p>
<a title="fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Malabar_grouper_melb_aquarium.jpg"><img width="120" alt="Malabar grouper melb aquarium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg"></a>
<a href="https://github.com/davips/hosh/blob/main/colored-id.png">
<img src="https://raw.githubusercontent.com/davips/hosh/main/colored-id.png" alt="Colored base-62 representation" width="500" height="130">
</a>
</p>




[Latest version](https://github.com/davips/garoupa)

Garoupa hosts also some niceties for group theory experimentation.

## Python installation
### from package
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI
pip install garoupa
```

### from source
```bash
cd my-project
git clone https://github.com/davips/garoupa ../garoupa
pip install -e ../garoupa
```


### Examples
**Basic operations**
<details>
<p>

```python3
from garoupa import Hash

# Hashes can be multiplied.
from garoupa.hash import identity

a = Hash(blob=b"Some large binary content...")
b = Hash(blob=b"Some other binary content. Might be, e.g., an action or another large content.")
c = a * b
print(f"{a} * {b} = {c}")
"""
3dJZQ80zDmZ1hyah8Bj14GFU4gxRr7N2RY5My0iKJn0 * XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 = R1BiZy1F4HTc9zWSiofC4gV3VhT7GMqs02w5tefxnVk
"""
```

```python3
print(~b)
# Multiplication can be reverted by the inverse hash. Zero is the identity hash.
print(f"{b} * {~b} = {b * ~b} = 0")
"""
IdNlCrGCIPtypjF4xCZd4yb9YFeDiycRIwVM39yRIIJ
XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 * IdNlCrGCIPtypjF4xCZd4yb9YFeDiycRIwVM39yRIIJ = 0000000000000000000000000000000000000000000 = 0
"""
```

```python3

print(f"{b} * {identity} = {b * identity} = b")
"""
XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 * 0000000000000000000000000000000000000000000 = XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 = b
"""
```

```python3

print(f"{c} * {~b} = {c * ~b} = {a} = a")
"""
R1BiZy1F4HTc9zWSiofC4gV3VhT7GMqs02w5tefxnVk * IdNlCrGCIPtypjF4xCZd4yb9YFeDiycRIwVM39yRIIJ = 3dJZQ80zDmZ1hyah8Bj14GFU4gxRr7N2RY5My0iKJn0 = 3dJZQ80zDmZ1hyah8Bj14GFU4gxRr7N2RY5My0iKJn0 = a
"""
```

```python3

print(f"{~a} * {c} = {~a * c} = {b} = b")
"""
ncbPkmmO3z9Bskk3dweIvlWghWyGZpfcE7Zqh6AZ4tj * R1BiZy1F4HTc9zWSiofC4gV3VhT7GMqs02w5tefxnVk = XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 = XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 = b
"""
```

```python3

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
"""
R1BiZy1F4HTc9zWSiofC4gV3VhT7GMqs02w5tefxnVk / XdQj1SPgqbpRK2uFx4ShKttP6Mc0qHZgLdo6GTk6FO6 = 3dJZQ80zDmZ1hyah8Bj14GFU4gxRr7N2RY5My0iKJn0 = a
"""
```

```python3

# Hash multiplication is not expected to be commutative.
print(f"{a * b} != {b * a}")
"""
R1BiZy1F4HTc9zWSiofC4gV3VhT7GMqs02w5tefxnVk != eP4HWUGNBLd8fNiqMpPaGsT7iFL3nSPjdgbpxMgF4BA
"""
```

```python3

# Hash multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
"""
M7Acfgmx7M9uv1ZJ7YryKY9xfqnX6oL31gCaSssid6d = M7Acfgmx7M9uv1ZJ7YryKY9xfqnX6oL31gCaSssid6d
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

from garoupa.algebra.cyclic import Z
from garoupa.algebra.dihedral import D

# Direct product between:
#   symmetric group S4;
#   cyclic group Z5; and,
#   dihedral group D4.
from garoupa.algebra.symmetric import S
from garoupa.algebra.symmetric.perm import Perm

G = S(4) * Z(5) * D(4)
print(G)
"""
S4×Z5×D4
"""
```

```python3

# Operating over 5 sampled pairs.
for a, b in islice(zip(G, G), 0, 5):
    print(a, "*", b, "=", a * b, sep="\t")
"""
«[1, 0, 3, 2], 3, s6»	*	«[2, 1, 0, 3], 1, s0»	=	«[3, 0, 1, 2], 4, r2»
«[0, 1, 3, 2], 3, s7»	*	«[2, 0, 3, 1], 3, s3»	=	«[3, 0, 2, 1], 1, r0»
«[2, 1, 0, 3], 1, s7»	*	«[0, 1, 2, 3], 0, s2»	=	«[2, 1, 0, 3], 1, r1»
«[0, 2, 1, 3], 1, r4»	*	«[3, 0, 2, 1], 3, r2»	=	«[3, 0, 1, 2], 4, r2»
«[0, 3, 1, 2], 2, r6»	*	«[3, 1, 0, 2], 1, r4»	=	«[2, 3, 0, 1], 3, r2»
"""
```

```python3

# Operator ~ is another way of sampling.
G = S(12)
print(~G)
"""
[0, 11, 8, 2, 1, 9, 7, 4, 10, 6, 3, 5]
"""
```

```python3

# Manual element creation.
last_perm_i = factorial(12) - 1
a = Perm(i=last_perm_i, n=12)
print("Last element of S35:", a)
"""
Last element of S35: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
```

```python3

# Inverse element. Group S4.
a = Perm(i=21, n=4)
b = Perm(i=17, n=4)
print(a, "*", ~a, "=", (a * ~a).i, "=", a * ~a, "= identity")
"""
[1, 3, 2, 0] * [3, 0, 2, 1] = 0 = [0, 1, 2, 3] = identity
"""
```

```python3

print(a, "*", b, "=", a * b)
"""
[1, 3, 2, 0] * [1, 2, 3, 0] = [3, 2, 0, 1]
"""
```

```python3

print(a, "*", b, "*", ~b, "=", a * b * ~b, "= a")
"""
[1, 3, 2, 0] * [1, 2, 3, 0] * [3, 0, 1, 2] = [1, 3, 2, 0] = a
"""
```

```python3


```


</p>
</details>

**Commutativity degree of groups**
<details>
<p>

```python3

from garoupa.algebra.cyclic import Z
from garoupa.algebra.dihedral import D
from garoupa.algebra.matrix.m import M


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        for b in list(G.sorted())[idx + 1:]:
            if a * b == b * a:
                count += 2
            i += 2
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t{100 * count / i} %", sep="")


# Dihedral
traverse(D(8))
"""
             |D8| = 16:              112/256:  4.0 bits	43.75 %
"""
```

```python3
traverse(D(8) ^ 2)
"""
          |D8×D8| = 256:         12544/65536:  8.0 bits	19.140625 %
"""
```

```python3

# Z4!
traverse(Z(4) * Z(3) * Z(2))
"""
       |Z4×Z3×Z2| = 24:              576/576:  4.584962500721157 bits	100.0 %
"""
```

```python3

# M 3x3 %4
traverse(M(3, 4))

# Large groups (sampling is needed).
Gs = [D(8) ^ 3, D(8) ^ 4, D(8) ^ 5]
for G in Gs:
    i, count = 0, 0
    for a, b in zip(G, G):
        if a * b == b * a:
            count += 1
        if i >= 10_000:
            break
        i += 1
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t~{100 * count / i} %", sep="")
"""
           |M3%4| = 64:            2560/4096:  6.0 bits	62.5 %
       |D8×D8×D8| = 4096:          854/10000:  12.0 bits	~8.54 %
    |D8×D8×D8×D8| = 65536:         351/10000:  16.0 bits	~3.51 %
 |D8×D8×D8×D8×D8| = 1048576:       164/10000:  20.0 bits	~1.64 %
"""
```


</p>
</details>

**Tendence of commutativity on Mn**
<details>
<p>

```python3
from itertools import chain

from garoupa.algebra.matrix.m import M
from garoupa.algebra.matrix.m8bit import M8bit


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        for b in list(G.sorted())[idx + 1:]:
            if a * b == b * a:
                count += 2
            i += 2
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t{100 * count / i} %", sep="")


M1_4 = map(M, range(1, 5))
for G in chain(M1_4, [M8bit(), M(5)]):
    traverse(G)
# ...
for G in map(M, range(6, 11)):
    i, count = 0, 0
    for a, b in zip(G, G):
        if a * b == b * a:
            count += 1
        i += 1
        if i >= 1_000_000:
            break
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t~{100 * count / i} %", sep="")

"""
|M1| = 1:                        1/1:  0 bits	100.0 %
|M2| = 2:                        4/4:  1 bits	100.0 %
|M3| = 8:                      40/64:  3 bits	62.5 %
|M4| = 64:                 1024/4096:  6 bits	25.0 %
|M8bit| = 256:              14848/65536:  8 bits	22.65625 %
|M5| = 1024:           62464/1048576:  10 bits	5.95703125 %
|M6| = 32768:              286/32768:  15 bits	0.872802734375 %
|M7| = 2097152:          683/1000000:  21 bits	0.0683 %
|M8| = 268435456:         30/1000000:  28 bits	0.003 %
|M9| = 68719476736:        1/1000000:  36 bits	0.0001 %
|M10| = 35184372088832:     0/1000000:  45 bits	0.0 %
"""
```
</p>
</details>





### Features
