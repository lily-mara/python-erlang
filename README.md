Python-Erlang
=============

[![build status](https://travis-ci.org/natemara/python-erlang.svg?branch=master)](https://travis-ci.org/natemara/python-erlang)

This is the main repository for the `python-erlang` package. This package is
used to calculate various telecommunications statistics.

Install
-------

The simplest way to install is with pip. `pip install python-erlang` will
pull this package from PyPi and install it.

Usage
-----

As the package is currently in its infancy, the only useful function included
will calculate the number of lines needed to support the given usage in erlangs
and blocking rate using the Extended Erlang B formula.

```python
>>> import erlang
>>> erlang.extended_b_lines(12, 0.001)
24
```
