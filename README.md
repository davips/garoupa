![test](https://github.com/davips/garoupa/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/garoupa/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/garoupa)

# GaROUPa
<p>
<a title="fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Malabar_grouper_melb_aquarium.jpg"><img width="120" alt="Malabar grouper melb aquarium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg"></a>
</p>

GaROUPa is a package containing some groups from abstract algebra and a flexible operable hash, briefly explained in the presentation (ongoing work):

[![image](https://raw.githubusercontent.com/davips/garoupa/main/examples/capa-slides-gdocs.png)](https://docs.google.com/presentation/d/e/2PACX-1vSCTHD6FeLET6lKgexiqJQ6c4viu0F_60kjoDe0x2mm8RqdhkWOiRA4QN3Zr-QLCq9CsPs_qkAAgxso/embed?start=false&loop=false&delayms=3000)


Screenshot of usage in an interactive session:

<p>
<a href="https://github.com/davips/garoupa/blob/main/examples/frontimg.png">
<img src="https://raw.githubusercontent.com/davips/garoupa/main/examples/frontimg.png" alt="Colored base-62 representation" width="400" height="230">
</a>
</p>



[PyPI package](https://pypi.org/project/garoupa)

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
git clone https://github.com/davips/garoupa
cd garoupa
poetry install
```

### Examples
**Basic operations**
<details>
<p>

```python3
from garoupa import Hosh

# Hoshes (operable hash-based elements) can be multiplied.
from garoupa import identity64

a = Hosh(blob=b"Some large binary content...")
b = Hosh(blob=b"Some other binary content. Might be, e.g., an action or another large content.")
c = a * b
print(f"{a} * {b} = {c}")
"""
1WCCD1p4Msmn2hvbiaHOPcYw8qQnGMai5zFZE68xr2kymjdnq6CEysKx7AUZGDqK * hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz = jFnCCFpU-8kJY2h3HBB-CjTgm.LJZerGkOUT09EENs.7F75nK8w91lPl9gOIWe62
"""
```

```python3
print(~b)
# Multiplication can be reverted by the inverse hosh. Zero is the identity hosh.
print(f"{b} * {~b} = {b * ~b} = 0")
"""
Khf00n.bNZZF6fe7CB8.0UaG6rgeXrGfUVwMDON29e8yuXoZzq6ZCVfWEoBk6KDc
hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz * Khf00n.bNZZF6fe7CB8.0UaG6rgeXrGfUVwMDON29e8yuXoZzq6ZCVfWEoBk6KDc = 0000000000000000000000000000000000000000000000000000000000000000 = 0
"""
```

```python3

print(f"{b} * {identity64} = {b * identity64} = b")
"""
hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz * 0000000000000000000000000000000000000000000000000000000000000000 = hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz = b
"""
```

```python3

print(f"{c} * {~b} = {c * ~b} = {a} = a")
"""
jFnCCFpU-8kJY2h3HBB-CjTgm.LJZerGkOUT09EENs.7F75nK8w91lPl9gOIWe62 * Khf00n.bNZZF6fe7CB8.0UaG6rgeXrGfUVwMDON29e8yuXoZzq6ZCVfWEoBk6KDc = 1WCCD1p4Msmn2hvbiaHOPcYw8qQnGMai5zFZE68xr2kymjdnq6CEysKx7AUZGDqK = 1WCCD1p4Msmn2hvbiaHOPcYw8qQnGMai5zFZE68xr2kymjdnq6CEysKx7AUZGDqK = a
"""
```

```python3

print(f"{~a} * {c} = {~a * c} = {b} = b")
"""
-5ppo-CXfdBEZKwQJRno1iP6a0I1pTGJLUOa5yvjIjEYAfE3FQ8gNQAxzmT4O6P- * jFnCCFpU-8kJY2h3HBB-CjTgm.LJZerGkOUT09EENs.7F75nK8w91lPl9gOIWe62 = hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz = hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz = b
"""
```

```python3

# Division is shorthand for reversion.
print(f"{c} / {b} = {c / b} = a")
"""
jFnCCFpU-8kJY2h3HBB-CjTgm.LJZerGkOUT09EENs.7F75nK8w91lPl9gOIWe62 / hKM..E0QdH-mVMNUpqWbPw56-IEDesW1UHyA7k8BYF5JYIli-c-fSuQagYp.mCNz = 1WCCD1p4Msmn2hvbiaHOPcYw8qQnGMai5zFZE68xr2kymjdnq6CEysKx7AUZGDqK = a
"""
```

```python3

# Hosh multiplication is not expected to be commutative.
print(f"{a * b} != {b * a}")
"""
jFnCCFpU-8kJY2h3HBB-CjTgm.LJZerGkOUT09EENs.7F75nK8w91lPl9gOIWe62 != jFnCCFpU-8kJY2h3HBB-CsB9NaEYXZlsV3Pmu.WFL2pQpx6gvFcTN-gR54d5f0K2
"""
```

```python3

# Hosh multiplication is associative.
print(f"{a * (b * c)} = {(a * b) * c}")
"""
DiLddiPNYgBrU4y7nbb-mm73.unoKH6Ux.AktmuBlx6q51QMs6sjNOGj4Cgvxojn = DiLddiPNYgBrU4y7nbb-mm73.unoKH6Ux.AktmuBlx6q51QMs6sjNOGj4Cgvxojn
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
from garoupa.algebra.symmetric import Perm
from garoupa.algebra.symmetric import S

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

# Operating over 5 sampled pairs.
for a, b in islice(zip(G, G), 0, 5):
    print(a, "*", b, "=", a * b, sep="\t")
"""
«[2, 0, 1, 3], 2, ds0»	*	«[2, 0, 3, 1], 1, ds7»	=	«[1, 2, 3, 0], 3, dr1»
«[0, 3, 1, 2], 3, ds3»	*	«[1, 0, 3, 2], 0, dr0»	=	«[3, 0, 2, 1], 3, ds3»
«[3, 0, 1, 2], 3, ds0»	*	«[1, 0, 3, 2], 2, ds5»	=	«[0, 3, 2, 1], 0, dr3»
«[2, 1, 0, 3], 3, dr0»	*	«[1, 0, 2, 3], 0, dr6»	=	«[1, 2, 0, 3], 3, dr2»
«[1, 3, 0, 2], 3, ds1»	*	«[0, 2, 1, 3], 0, ds1»	=	«[1, 0, 3, 2], 3, dr0»
"""
```

```python3

# Operator ~ is another way of sampling.
G = S(12)
print(~G)
"""
[11, 1, 4, 6, 8, 9, 10, 7, 0, 2, 5, 3]
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
       |D8×D8×D8| = 4096:          798/10000:  12.0 bits	~7.98 %
    |D8×D8×D8×D8| = 65536:         351/10000:  16.0 bits	~3.51 %
 |D8×D8×D8×D8×D8| = 1048576:       169/10000:  20.0 bits	~1.69 %
"""
```


</p>
</details>

**Detect identity after many repetitions**
<details>
<p>

```python3

import operator
from datetime import datetime
from functools import reduce
from math import log, inf
from sys import argv

from garoupa.algebra.dihedral import D
from garoupa.algebra.symmetric import S

example = len(argv) == 1 or (not argv[1].isdecimal() and argv[1][0] not in ["p", "s", "d"])

primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997, 1009]

if example:
    limit, sample = 30, 100
    lst = []  # See *.
    for n in primes[:5]:
        lst.append(D(n, seed=n))
    G = reduce(operator.mul, lst)
else:
    limit, sample = int(argv[2]), int(argv[3]) if len(argv) > 2 else 1_000_000_000_000
    if argv[1] == "s25d":
        G = S(25) * reduce(operator.mul, [D(n) for n in primes[:9]])
    elif argv[1] == "s57":
        G = S(57)
    elif argv[1] == "p384":
        G = reduce(operator.mul, [D(n) for n in primes[:51]])
    elif argv[1] == "p64":
        G = reduce(operator.mul, [D(n) for n in primes[:12]])
    elif argv[1] == "p96":
        G = reduce(operator.mul, [D(n) for n in primes[:16]])
    elif argv[1] == "p128":
        G = reduce(operator.mul, [D(n) for n in primes[:21]])
    elif argv[1] == "p256":
        G = reduce(operator.mul, [D(n) for n in primes[:37]])
    elif argv[1] == "64":
        G = reduce(operator.mul, [D(n) for n in range(5, 31, 2)])
    elif argv[1] == "96":
        G = reduce(operator.mul, [D(n) for n in range(5, 41, 2)])
    elif argv[1] == "128":
        G = reduce(operator.mul, [D(n) for n in range(5, 51, 2)])
    else:
        G = reduce(operator.mul, [D(n) for n in range(5, 86, 2)])

print(f"{G.bits} bits   Pc: {G.comm_degree}  order: {G.order} {G}", flush=True)
print("--------------------------------------------------------------", flush=True)
for hist in G.sampled_orders(sample=sample, limit=limit):
    tot = sum(hist.values())
    bad = 0  # See *.
    for k, v in hist.items():
        if k[0] <= limit:
            bad += v
    print(hist, flush=True)
    hist = hist.copy()
    if (inf, inf) in hist:
        del hist[(inf, inf)]
    hist = {int((k[0] + k[1]) / 2): v for k, v in hist.items()}
    print(f"\nbits: {log(G.order, 2):.2f}  Pc: {G.comm_degree or -1:.2e}   a^<{limit}=0: {bad}/{tot} = {bad / tot:.2e}",
          G, G._pi_core(hist), datetime.now().strftime("%d/%m/%Y %H:%M:%S"), flush=True)
# * -> [Explicit FOR due to autogeneration of README through eval]
"""
21.376617194973697 bits   Pc: 0.004113533525298232  order: 2722720 D5×D7×D11×D13×D17
--------------------------------------------------------------
{(-1, 10): 9, (9, 20): 7, (19, 30): 9, (inf, inf): 75}

bits: 21.38  Pc: 4.11e-03   a^<30=0: 25/100 = 2.50e-01 D5×D7×D11×D13×D17 0.125 15/08/2021 22:53:55
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

**Groups benefit from methods from the module 'hosh'**
<details>
<p>

```python3
from garoupa.algebra.matrix import M

m = ~M(23)
print(repr(m.hosh))
```
<a href="https://github.com/davips/garoupa/blob/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png">
<img src="https://raw.githubusercontent.com/davips/garoupa/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png" alt="Colored base-62 representation" width="380" height="18">
</a>
</p>
</details>



### Features
* [x] Create noncommutative identifiers from binary content
* [ ] Create commutative identifiers from binary content
  * [ ] Create elements from H
  * [ ] Create elements from H


### Performance
See package [hosh](https://pypi.org/project/hosh) for faster, native (compiled) hash operations.
However, only future major version `2.*.*` or higher of hosh will be compatible with garoupa operable hashes.
