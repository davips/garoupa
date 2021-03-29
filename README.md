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
3dJZQ80zDmZ0d2EhdruHwBs3acMQtezc91uMCjUQR1A * XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B = i9dyLxtlaQqf8aMQegwcCNVLiHNkJlmPJL0lwdAXlNX
"""
```

```python3
print(~b)
# Multiplication can be reverted by the inverse hash. Zero is the identity hash.
print(f"{b} * {~b} = {b * ~b} = 0")
"""
Cz69OcxEd0v7BKuKqkGkiMGj80b5VfOc6Z9VJXPUH1S
XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B * Cz69OcxEd0v7BKuKqkGkiMGj80b5VfOc6Z9VJXPUH1S = 0000000000000000000000000000000000000000000 = 0
"""
```

```python3

print(f"{b} * {identity} = {b * identity} = b")
"""
XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B * 0000000000000000000000000000000000000000000 = XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B = b
"""
```

```python3

print(f"{c} * {~b} = {c * ~b} = {a} = a")
"""
i9dyLxtlaQqf8aMQegwcCNVLiHNkJlmPJL0lwdAXlNX * Cz69OcxEd0v7BKuKqkGkiMGj80b5VfOc6Z9VJXPUH1S = 3dJZQ80zDmZ0d2EhdruHwBs3acMQtezc91uMCjUQR1A = 3dJZQ80zDmZ0d2EhdruHwBs3acMQtezc91uMCjUQR1A = a
"""
```

```python3

print(f"{~a} * {c} = {~a * c} = {b} = b")
"""
WCFaSatsNteo7XQqg4vYj1ovIFrBmlougnckldBwnuf * i9dyLxtlaQqf8aMQegwcCNVLiHNkJlmPJL0lwdAXlNX = XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B = XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B = b
"""
```

```python3

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
"""
i9dyLxtlaQqf8aMQegwcCNVLiHNkJlmPJL0lwdAXlNX / XdQj1SPgqbr4kwx38O2JznVJI7j7Pax67a0muwVB92B = 3dJZQ80zDmZ0d2EhdruHwBs3acMQtezc91uMCjUQR1A = a
"""
```

```python3

# Hash multiplication is not expected to be commutative.
print(f"{a * b} != {b * a}")
"""
i9dyLxtlaQqf8aMQegwcCNVLiHNkJlmPJL0lwdAXlNX != Tm9M9q8WIQbCyMAxyiMYs4O9RN9QJnWZXJ4zaRgpEaF
"""
```

```python3

# Hash multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
"""
cJBwPoh2kg2pzExxTOE5vtNrlcahIoMitcRoIbJbR8A = cJBwPoh2kg2pzExxTOE5vtNrlcahIoMitcRoIbJbR8A
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
«[3, 2, 0, 1], 3, r7»	*	«[1, 2, 0, 3], 3, r3»	=	«[2, 0, 3, 1], 1, r2»
«[3, 2, 0, 1], 2, s6»	*	«[1, 0, 3, 2], 1, r1»	=	«[2, 3, 1, 0], 3, s1»
«[2, 0, 1, 3], 1, r1»	*	«[0, 1, 3, 2], 1, r7»	=	«[2, 0, 3, 1], 2, r0»
«[3, 1, 0, 2], 1, r6»	*	«[1, 0, 2, 3], 1, r7»	=	«[1, 3, 0, 2], 2, r1»
«[3, 0, 1, 2], 3, s4»	*	«[1, 2, 0, 3], 0, r3»	=	«[0, 1, 3, 2], 3, s1»
"""
```

```python3

# Operator ~ is another way of sampling.
G = S(12)
print(~G)
"""
[2, 4, 11, 0, 8, 10, 1, 6, 3, 5, 7, 9]
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
from itertools import product

from garoupa.algebra.cyclic import Z
from garoupa.algebra.cyclic.nat import Nat
from garoupa.algebra.dihedral import D


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        print(a, a.i)
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
r0 0
r1 1
r2 2
r3 3
r4 4
r5 5
r6 6
r7 7
s0 0
s1 1
s2 2
s3 3
s4 4
s5 5
s6 6
s7 7
             |D8| = 16:              112/256:  4 bits	43.75 %
"""
```

```python3

traverse(D(8) ^ 2)
"""
«r0, r0» 0
«r0, r1» 1
«r0, r2» 2
«r0, r3» 3
«r0, r4» 4
«r0, r5» 5
«r0, r6» 6
«r0, r7» 7
«r0, s0» 0
«r0, s1» 1
«r0, s2» 2
«r0, s3» 3
«r0, s4» 4
«r0, s5» 5
«r0, s6» 6
«r0, s7» 7
«r1, r0» 16
«r1, r1» 17
«r1, r2» 18
«r1, r3» 19
«r1, r4» 20
«r1, r5» 21
«r1, r6» 22
«r1, r7» 23
«r1, s0» 8
«r1, s1» 9
«r1, s2» 10
«r1, s3» 11
«r1, s4» 12
«r1, s5» 13
«r1, s6» 14
«r1, s7» 15
«r2, r0» 32
«r2, r1» 33
«r2, r2» 34
«r2, r3» 35
«r2, r4» 36
«r2, r5» 37
«r2, r6» 38
«r2, r7» 39
«r2, s0» 16
«r2, s1» 17
«r2, s2» 18
«r2, s3» 19
«r2, s4» 20
«r2, s5» 21
«r2, s6» 22
«r2, s7» 23
«r3, r0» 48
«r3, r1» 49
«r3, r2» 50
«r3, r3» 51
«r3, r4» 52
«r3, r5» 53
«r3, r6» 54
«r3, r7» 55
«r3, s0» 24
«r3, s1» 25
«r3, s2» 26
«r3, s3» 27
«r3, s4» 28
«r3, s5» 29
«r3, s6» 30
«r3, s7» 31
«r4, r0» 64
«r4, r1» 65
«r4, r2» 66
«r4, r3» 67
«r4, r4» 68
«r4, r5» 69
«r4, r6» 70
«r4, r7» 71
«r4, s0» 32
«r4, s1» 33
«r4, s2» 34
«r4, s3» 35
«r4, s4» 36
«r4, s5» 37
«r4, s6» 38
«r4, s7» 39
«r5, r0» 80
«r5, r1» 81
«r5, r2» 82
«r5, r3» 83
«r5, r4» 84
«r5, r5» 85
«r5, r6» 86
«r5, r7» 87
«r5, s0» 40
«r5, s1» 41
«r5, s2» 42
«r5, s3» 43
«r5, s4» 44
«r5, s5» 45
«r5, s6» 46
«r5, s7» 47
«r6, r0» 96
«r6, r1» 97
«r6, r2» 98
«r6, r3» 99
«r6, r4» 100
«r6, r5» 101
«r6, r6» 102
«r6, r7» 103
«r6, s0» 48
«r6, s1» 49
«r6, s2» 50
«r6, s3» 51
«r6, s4» 52
«r6, s5» 53
«r6, s6» 54
«r6, s7» 55
«r7, r0» 112
«r7, r1» 113
«r7, r2» 114
«r7, r3» 115
«r7, r4» 116
«r7, r5» 117
«r7, r6» 118
«r7, r7» 119
«r7, s0» 56
«r7, s1» 57
«r7, s2» 58
«r7, s3» 59
«r7, s4» 60
«r7, s5» 61
«r7, s6» 62
«r7, s7» 63
«s0, r0» 0
«s0, r1» 1
«s0, r2» 2
«s0, r3» 3
«s0, r4» 4
«s0, r5» 5
«s0, r6» 6
«s0, r7» 7
«s0, s0» 0
«s0, s1» 1
«s0, s2» 2
«s0, s3» 3
«s0, s4» 4
«s0, s5» 5
«s0, s6» 6
«s0, s7» 7
«s1, r0» 16
«s1, r1» 17
«s1, r2» 18
«s1, r3» 19
«s1, r4» 20
«s1, r5» 21
«s1, r6» 22
«s1, r7» 23
«s1, s0» 8
«s1, s1» 9
«s1, s2» 10
«s1, s3» 11
«s1, s4» 12
«s1, s5» 13
«s1, s6» 14
«s1, s7» 15
«s2, r0» 32
«s2, r1» 33
«s2, r2» 34
«s2, r3» 35
«s2, r4» 36
«s2, r5» 37
«s2, r6» 38
«s2, r7» 39
«s2, s0» 16
«s2, s1» 17
«s2, s2» 18
«s2, s3» 19
«s2, s4» 20
«s2, s5» 21
«s2, s6» 22
«s2, s7» 23
«s3, r0» 48
«s3, r1» 49
«s3, r2» 50
«s3, r3» 51
«s3, r4» 52
«s3, r5» 53
«s3, r6» 54
«s3, r7» 55
«s3, s0» 24
«s3, s1» 25
«s3, s2» 26
«s3, s3» 27
«s3, s4» 28
«s3, s5» 29
«s3, s6» 30
«s3, s7» 31
«s4, r0» 64
«s4, r1» 65
«s4, r2» 66
«s4, r3» 67
«s4, r4» 68
«s4, r5» 69
«s4, r6» 70
«s4, r7» 71
«s4, s0» 32
«s4, s1» 33
«s4, s2» 34
«s4, s3» 35
«s4, s4» 36
«s4, s5» 37
«s4, s6» 38
«s4, s7» 39
«s5, r0» 80
«s5, r1» 81
«s5, r2» 82
«s5, r3» 83
«s5, r4» 84
«s5, r5» 85
«s5, r6» 86
«s5, r7» 87
«s5, s0» 40
«s5, s1» 41
«s5, s2» 42
«s5, s3» 43
«s5, s4» 44
«s5, s5» 45
«s5, s6» 46
«s5, s7» 47
«s6, r0» 96
«s6, r1» 97
«s6, r2» 98
«s6, r3» 99
«s6, r4» 100
«s6, r5» 101
«s6, r6» 102
«s6, r7» 103
«s6, s0» 48
«s6, s1» 49
«s6, s2» 50
«s6, s3» 51
«s6, s4» 52
«s6, s5» 53
«s6, s6» 54
«s6, s7» 55
«s7, r0» 112
«s7, r1» 113
«s7, r2» 114
«s7, r3» 115
«s7, r4» 116
«s7, r5» 117
«s7, r6» 118
«s7, r7» 119
«s7, s0» 56
«s7, s1» 57
«s7, s2» 58
«s7, s3» 59
«s7, s4» 60
«s7, s5» 61
«s7, s6» 62
«s7, s7» 63
          |D8×D8| = 256:         12544/65536:  8 bits	19.140625 %
"""
```

```python3

# Z4!
traverse(Z(4) * Z(3) * Z(2))
"""
«0, 0, 0» 0
«0, 0, 1» 1
«0, 1, 0» 2
«0, 1, 1» 3
«0, 2, 0» 4
«0, 2, 1» 5
«1, 0, 0» 6
«1, 0, 1» 7
«1, 1, 0» 8
«1, 1, 1» 9
«1, 2, 0» 10
«1, 2, 1» 11
«2, 0, 0» 12
«2, 0, 1» 13
«2, 1, 0» 14
«2, 1, 1» 15
«2, 2, 0» 16
«2, 2, 1» 17
«3, 0, 0» 18
«3, 0, 1» 19
«3, 1, 0» 20
«3, 1, 1» 21
«3, 2, 0» 22
«3, 2, 1» 23
       |Z4×Z3×Z2| = 24:              576/576:  4 bits	100.0 %
"""
```

```python3

# Large groups (sampling is needed).
Gs = [D(8) ^ 3, D(8) ^ 4, D(8) ^ 5]
for G in Gs:
    i, count = 0, 0
    for a, b in product(G, G):
        if a * b == b * a:
            count += 1
        if i >= 300_000:
            break
        i += 1
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t~{100 * count / i} %", sep="")
"""
       |D8×D8×D8| = 4096:       15872/300000:  12 bits	~5.290666666666667 %
    |D8×D8×D8×D8| = 65536:      12288/300000:  16 bits	~4.096 %
 |D8×D8×D8×D8×D8| = 1048576:        0/300000:  20 bits	~0.0 %
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
