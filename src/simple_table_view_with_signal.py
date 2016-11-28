from PySide.QtCore import Qt, QAbstractTableModel, QModelIndex, QTimer, QTime
from PySide.QtGui import QTableView, QApplication, QWidget, QVBoxLayout

import sys


class SimpleTableModel(QAbstractTableModel):
    def __init__(self, mlist):
        super(SimpleTableModel, self).__init__()
        self._items = mlist

        self._timer = QTimer()
        # We need to tell the view every second that the time has changed and
        #  that it needs to be read again. We do this with a timer. In the
        # constructor, we set its interval to 1 second and connect its
        # timeout signal.
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._timerHit)
        self._timer.start()

    def _timerHit(self):
        index = QModelIndex()
        # emit a signal to make the view reread identified data
        self.dataChanged.emit(index, index)

    # We need to tell the view how many rows we have present in our data.
    def rowCount(self, parent=QModelIndex):
        return len(self._items)

    # We need to tell the view how many columns we have present in our data.
    def columnCount(self, parent=QModelIndex):
        return len(self._items[0])

    # data() is where the view asks us for all sorts of information about our
    # data:
    # this can be purely informational (the data itself), as well as all
    # sorts of 'extras'
    # such as how the data should be presented.
    #
    def data(self, index, role=Qt.DisplayRole):
        """
        :param index:
        :type index: `QtCore.QModelIndex`
        :param role:
        :type role: `Qt.ItemDataRole`
        :return:
        :rtype:
        """
        if role == Qt.DisplayRole:
            if index.row() == 0 and index.column() == 0:
                return QTime.currentTime().toString()
            else:
                # The view is asking for the actual data, so, just return the
                # item it's asking for.
                return self._items[index.row()][index.column()]
        else:
            # We don't care about anything else, so make sure to return an
            # empty QVariant.
            return


# This widget is our view of the readonly list.
# Obviously, in a real application, this will be more complex,
# with signals/etc usage, but
# for the scope of this tutorial, let's keep it simple, as always.
class SimpleTableView(QTableView):
    def __init__(self, parent=None):
        QTableView.__init__(self, parent)


class MyMainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()

        # create a data source
        m = SimpleTableModel([("col1", "row1"), ("col2", "row2")])
        # let's add one view
        v = SimpleTableView()
        v.setModel(m)

        vbox.addWidget(v)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
    sys.exit()