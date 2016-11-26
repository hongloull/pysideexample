#! /user/bin/env python
from PySide import QtCore


class Communication(QtCore.QObject):
    # Signals are runtime objects owned by instances, they are not class
    # attributes, can not call Communication.speak.
    speak = QtCore.Signal(str)

    def __init__(self):
        super(Communication, self).__init__()

    def speaking(self):
        self.speak.emit('hello world')


c = Communication()
c.speaking()
