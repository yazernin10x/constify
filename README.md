[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-%233776AB?style=flat&logo=python&logoColor=%23FFD43B)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/License-MIT-%234FC08D?style=flat)](https://choosealicense.com/licenses/mit/)
[![Coverage Status](https://coveralls.io/repos/github/yazernin10x/constify/badge.svg?branch=main)](https://coveralls.io/github/yazernin10x/constify?branch=main)
[![Unit Tests](https://github.com/yazernin10x/constify/actions/workflows/test.yml/badge.svg)](https://github.com/yazernin10x/constify/actions/workflows/test.yml)
[![Setuptools](https://img.shields.io/badge/Setuptools-Packaged-%23FFD242?style=flat)](https://setuptools.pypa.io/en/latest/setuptools.html)
[![Tox](https://img.shields.io/badge/Tox-Passing-%238ACA3E?style=flat)](https://tox.wiki/en/latest/config.html)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/MyPy-Checked-%232A6ACB)](https://mypy-lang.org/)

# Constify

The `constify` library provides the `freezeparams` decorator to make mutable default values and arguments passed to functions immutable.

## Why use the `freezeparams` decorator ?

[[1]](#sources) The default value of a parameter is evaluated only once, which can lead to unexpected behavior if the value is a mutable object, such as a list or a dictionary. For example, the following function accumulates arguments across calls:

### Example
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]
```

To prevent this default value from being shared, the function can be rewritten as follows:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

This solution is effective, but with multiple mutable default values, it requires many checks. The `freezeparams` decorator simplifies the use of mutable objects as default values and arguments.

## Installation

```bash
pip install constify
```

## Usage

```python
from constify import freezeparams

@freezeparams
def add_to(value, liste=[]):
    liste.append(value)
    return liste

# Default value remains unchanged
print(add_to(56))  # [56]
print(add_to(value=98))  # [98]

# Passed list remains intact
my_list = [1, 2]
print(add_to(3, my_list))  # [1, 2, 3]
print(my_list)  # [1, 2]
```

Simple and effective!

## Sources

[1] https://docs.python.org/3.13/tutorial/controlflow.html#default-argument-values

