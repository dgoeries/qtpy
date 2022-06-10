# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtLocation classes and functions."""

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    QtBindingsNotFoundError,
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.QtLocation import *
elif PYQT6:
    raise QtBindingMissingModuleError(name='QtLocation')
elif PYSIDE2:
    from PySide2.QtLocation import *
elif PYSIDE6:
    raise QtBindingMissingModuleError(name='QtLocation')
else:
    raise QtBindingsNotFoundError()
