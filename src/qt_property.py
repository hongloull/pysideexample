"""
PySide provides a Property function which allows for declaring properties
that simultaneously behave both as Qt and Python properties, and have their
setters and getters defined as Python functions.
"""

from PySide import QtCore


class PropertyExample(QtCore.QObject):
    def __init__(self, strValue='', intValue=0):
        super(PropertyExample, self).__init__()
        self._strValue = strValue
        self._intValue = intValue

    def getStrValue(self):
        return self._strValue

    def setStrValue(self, strValue):
        self._strValue = strValue

    def getIntValue(self):
        return self._intValue

    def setIntValue(self, value):
        self._intValue = value

    @QtCore.Signal
    def _valueChanged(self):
        print('value changed')

    @QtCore.Slot(int)
    def _notify(self, value):
        print('value changed to {0}'.format(value))

    strValue = QtCore.Property(unicode, getStrValue, setStrValue)
    intValue = QtCore.Property(int, getIntValue, setIntValue,
                               notify=_valueChanged)


foo = PropertyExample(strValue='hello world')
print(foo.strValue)
foo.strValue = 'hello maya'
print(foo.strValue)
print(foo.intValue)
foo.intValue = 1
