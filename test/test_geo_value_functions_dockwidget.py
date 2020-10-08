# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'serranoycandela@gmail.com'
__date__ = '2020-09-07'
__copyright__ = 'Copyright 2020, LANCIS'

import unittest

from PyQt5.QtGui import QDockWidget

from geo_value_functions_dockwidget import geo_value_functionsDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class geo_value_functionsDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = geo_value_functionsDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(geo_value_functionsDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

