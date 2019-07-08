[![codecov](https://codecov.io/gh/OmarElawady/ascii-table/branch/master/graph/badge.svg)](https://codecov.io/gh/OmarElawady/ascii-table)
[![Build Status](https://travis-ci.com/OmarElawady/ascii-table.svg?branch=master)](https://travis-ci.com/OmarElawady/ascii-table)

Ascii Table
===========

This is a script to print tables to the console.

Full [documentation](https://omarelawady.github.io/asciitable/doc/).

Usage
=====

```python
t = Table()
t.set_headers(["ID", "Name", "Date"])
t.add_row(["1", "Aaaa", "2018-10-2"])
t.add_row(["2", "bbvbbba", "2018-10-2"])
t.add_row(["399", "CCC", "1018-5-2"])
t.print_table()
```
