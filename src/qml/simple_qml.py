#!/usr/bin/env python
# -'''- coding: utf-8 -'''-

"""
QML is a declarative language designed to describe the user interface of a
program: both what it looks like, and how it behaves. In QML, a user
interface is specified as a tree of objects with properties. In this tutorial
we will show how you can make a simple Hello World application with PySide
and QML.
"""

import sys
from PySide import QtCore, QtGui
from PySide.QtDeclarative import QDeclarativeView

# Create Qt application and the QDeclarative view
app = QtGui.QApplication(sys.argv)
view = QDeclarativeView()
# Create an URL to the QML file
url = QtCore.QUrl('view.qml')
# Set the QML file and show
view.setSource(url)
view.show()
# Enter Qt main loop
sys.exit(app.exec_())
