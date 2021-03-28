![test](https://github.com/davips/garoupa/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/garoupa/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/garoupa)

# garoupa
Incremental cryptography and flexible hash

<a title="fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Malabar_grouper_melb_aquarium.jpg"><img width="256" alt="Malabar grouper melb aquarium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg"></a>

[Latest version](https://github.com/davips/garoupa)

## Installation
### as a standalone lib.
```bash
# Set up a virtualenv. 
python3.7 -m venv venv
source venv/bin/activate

# Install from PyPI...
pip install --upgrade pip
pip install -U garoupa

# ...or, install from updated source code.
pip install git+https://github.com/davips/garoupa
```

### as an editable lib inside your project.
```bash
cd your-project
source venv/bin/activate
git clone https://github.com/davips/garoupa ../garoupa
pip install --upgrade pip
pip install -e ../garoupa
```

## Examples

<<creation>>

<<operation>>





**Timing tradeoff startup/repetition**
<details>
<p>

```python3
from timeit import timeit

from garoupa import Hash


def f():
    return Hash(12431434) * Hash(895784)


def f_compiled():
    return Hash(12431434, compiled=True) * Hash(895784, compiled=True)

t = timeit(f, number=1)
print("Normal warm up time:", round(t, 2), "s")
"""
Normal warm up time: 0.0 s
"""
```
```python3
t = timeit(f, number=100000)
print("Normal time:", round(t * 10, 2), "us")
"""
Normal time: 52.25 us
"""
```
```python3
t = timeit(f_compiled, number=1)
print("Compiled warm up time:", round(t, 2), "s")
"""
Compiled warm up time: 2.28 s
"""
```
```python3
t = timeit(f_compiled, number=100000)
print("Compiled time:", round(t * 10, 2), "us")
"""
Compiled time: 7.59 us
"""
```
</p>
</details>






## Features / TODO

* [ ] Features / TODO
