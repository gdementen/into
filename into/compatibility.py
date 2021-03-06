from __future__ import absolute_import, division, print_function

import sys
import itertools
import os

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
ON_TRAVIS_CI = 'TRAVIS_PYTHON_VERSION' in os.environ

if sys.version_info[0] >= 3:
    unicode = str
    map = map
    range = range
else:
    unicode = unicode
    map = itertools.imap
    range = xrange


def skipif(cond, **kwargs):
    def _(func):
        if cond:
            return None
        else:
            return func
    return _
