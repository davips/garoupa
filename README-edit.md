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
<<operation>>

<<groups>>

<<commutativity>>





### Features
