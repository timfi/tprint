# `tprint`

_Print python collections as tables_

[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)]("https://github.com/psf/black")
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tprint)](https://pypi.org/project/tprint)
[![PyPI - License](https://img.shields.io/pypi/l/tprint)](https://pypi.org/project/tprint)
[![PyPI](https://img.shields.io/pypi/v/tprint)](https://pypi.org/project/tprint)

## Example
```python
from tprint import tprint

data = {
    "a": (100, 2, 3, 4),
    "b": (1, 200, 3, 4),
    "c": (1, 2, 300, 4),
    "d": (1, 2, 3, 400),
}

# as rows
tprint(data)
"""
0 | 1   | 2   | 3   | 4  
--+-----+-----+-----+----
a | 100 | 2   | 3   | 4  
b | 1   | 200 | 3   | 4  
c | 1   | 2   | 300 | 4  
d | 1   | 2   | 3   | 400
"""

# as columns
tprint(data, as_columns=True)
"""
a   | b   | c   | d  
----+-----+-----+----
100 | 1   | 1   | 1  
2   | 200 | 2   | 2  
3   | 3   | 300 | 3  
4   | 4   | 4   | 400
"""
```

## Docs

### `tprint`
This is effectivly just the following snippet:
```python
def tprint(*args, **kwargs):
    print(tformat(*args, **kwargs))
```

### `tformat`
```python
def tformat(
    data: Union[Dict[str, Sequence], Sequence],
    *,
    as_columns: bool = False,
    headers: Optional[Sequence[str]] = None,
    alignments: Optional[str] = None,
    formattings: Optional[str] = None,
) -> str:
    """
    Format a dictionary or list as a table.
    
    :param data: table data
    :param as_columns: interpret given data as collection of columns
                       instead of as rows
    :param headers: sequence of column headers
                    (Defaults to enumerating the columns if headers
                     can't be extracted from data)
    :param alignments: string with alignments per column
                       (Defaults to left alignment for all columns
                        or those skipped with spaces)
    :param formattings: string with formattings per column
                        (Defaults to string casting for all columns
                         or those skipped with spaces)
    """
    ...
```

