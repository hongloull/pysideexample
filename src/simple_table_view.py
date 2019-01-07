from PySide.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide.QtGui import QTableView, QApplication, QColor, QWidget, QVBoxLayout

import sys


class SimpleTableModel(QAbstractTableModel):
    def __init__(self, mlist):
        super(SimpleTableModel, self).__init__()
        self._items = mlist

    # We need to tell the view how many rows we have present in our data.
    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    def columnCount(self, *args, **kwargs):
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
            # The view is asking for the actual data, so, just return the
            # item it's asking for.
            return self._items[index.row()][index.column()]
        elif role == Qt.BackgroundRole:
            # Here, it's asking for some background decoration.
            # Let's mix it up a bit: mod the row number to get even or odd,
            # and return different
            # colours depending.
            if index.row() % 2 == 0:
                return QColor(Qt.gray)
            else:
                return QColor(Qt.lightGray)
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