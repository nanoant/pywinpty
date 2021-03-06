# -*- coding: utf-8 -*-
"""
Pywinpty
========
This package provides a Cython wrapper around winpty C++ library.
"""

# yapf: disable

# Local imports
from .ptyprocess import PtyProcess
from .winpty_wrapper import PTY


# yapf: enable

PTY
PtyProcess
VERSION_INFO = (0, 6, 'dev0')
__version__ = '.'.join(map(str, VERSION_INFO))
