![test](https://github.com/davips/garoupa/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/garoupa/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/garoupa)

# garoupa
Cryptographic hash, abstract algebra and operators - see package [hosh](https://github.com/davips/hosh) for a faster, native (compiled) hash/ops approach.

<p>
<a title="fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Malabar_grouper_melb_aquarium.jpg"><img width="120" alt="Malabar grouper melb aquarium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg"></a>
<br>
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
<<operation>>

<<groups>>

<<commutativity>>

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

**Groups benefit from methods from module 'hash'**
<details>
<p>

```python3
from garoupa.algebra.matrix import M
m = ~M(23)
print(repr(m.hash))
```
<a href="https://github.com/davips/garoupa/blob/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png">
<img src="https://raw.githubusercontent.com/davips/garoupa/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png" alt="Colored base-62 representation" width="380" height="18">
</a>
</p>
</details>


### Features
