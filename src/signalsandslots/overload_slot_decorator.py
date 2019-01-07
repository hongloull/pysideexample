#!/usr/bin/env python

from PySide import QtCore


# define a new slot that receives a C 'int' or a 'str'
# and has 'saySomething' as its name
@QtCore.Slot(int)
@QtCore.Slot(str)
def saySomething(stuff):
    print(stuff)


class Communicate(QtCore.QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speakNumber = QtCore.Signal(int)
    speakWord = QtCore.Signal(str)


someone = Communicate()
# connect signal and slot properly
someone.speakNumber.connect(saySomething)
someone.speakWord.connect(saySomething)
# emit each 'speak' signal
someone.speakNumber.emit(10)
someone.speakWord.emit("Hello everybody!")


class Communicate2(QtCore.QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = QtCore.Signal((int,), (str,))


someone = Communicate2()
# connect signal and slot. As 'int' is the default
# we have to specify the str when connecting the
# second signal
someone.speak.connect(saySomething)
someone.speak[str].connect(saySomething)

# emit 'speak' signal with different arguments.
# we have to specify the str as int is the default
someone.speak.emit(10)
someone.speak[str].emit("Hello everybody!")
