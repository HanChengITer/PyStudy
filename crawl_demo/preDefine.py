# -*- coding:utf-8 -*-
import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

PYTHON_BIG_VERSION = sys.version[:1]
PYTHON_SMALL_VERSION = sys.version[:6]
