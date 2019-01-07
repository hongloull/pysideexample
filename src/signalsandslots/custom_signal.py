#!/usr/bin/env python

import sys
from PySide import QtCore


# Slots are assigned and overloaded using the decorator QtCore.Slot().
# define a new slot that receives a string and has
# 'saySomeWords' as its name
@QtCore.Slot(str)
def saySomeWords(words):
    print(words)


class Communicate(QtCore.QObject):
    # create a new signal on the fly and name it 'speak'
    speak = QtCore.Signal(str)


someone = Communicate()
# connect signal and slot
someone.speak.connect(saySomeWords)
# emit 'speak' signal
someone.speak.emit("Hello everybody!")
