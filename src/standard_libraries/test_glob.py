"""File Wildcards.

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

The glob module provides a function for making file lists from directory wildcard searches:
"""

import glob
import os


def test_glob():
    """File Wildcards."""

    # == operator for lists relies on the order of elements in the list.
    # In some cases (like on Linux Mint, python3.6) the glob() function returns list
    # in reverse order then  it might be expected. Thus lets sort both lists before comparison
    # using sorted() built-in function.

    path = os.path.join('src', 'standard_libraries', 'glob_files')
    assert sorted(glob.glob(os.path.join(path, '*.txt'))) == sorted([
        os.path.join(path, 'first_file.txt'),
        os.path.join(path, 'second_file.txt')
    ])
