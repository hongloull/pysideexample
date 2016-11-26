from PySide.QtCore import Qt, QModelIndex
from PySide.QtGui import QTreeView, QApplication, QWidget, \
    QVBoxLayout, QStandardItemModel, QStandardItem

import sys


class SimpleTreeModel(QStandardItemModel):
    def __init__(self):
        super(SimpleTreeModel, self).__init__()
        self._loadData()

    # We need to tell the view how many rows we have present in our data.
    def rowCount(self, parent=QModelIndex):
        return 3

    # We need to tell the view how many columns we have present in our data.
    def columnCount(self, parent=QModelIndex):
        return 2

    def _loadData(self):
        # populate data
        self.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
        for i in range(3):
            parent = QStandardItem('Family {}'.format(i))
            for j in range(3):
                child1 = QStandardItem('Child {}'.format(i * 3 + j))
                child2 = QStandardItem('row: {}, col: {}'.format(i, j + 1))
                child3 = QStandardItem('row: {}, col: {}'.format(i, j + 2))
                parent.appendRow([child1, child2, child3])
            self.appendRow(parent)


class SimpleTreeView(QTreeView):
    def __init__(self, parent=None):
        QTreeView.__init__(self, parent)


class MyMainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()

        self._model = SimpleTreeModel()

        self._view = SimpleTreeView()
        self._view.setModel(self._model)

        vbox.addWidget(self._view)
        self.setLayout(vbox)

        self._connectSignals()

    def _connectSignals(self):
        # print selected item's text
        selModel = self._view.selectionModel()
        selModel.selectionChanged.connect(self._onSelectionChanged)

    def _onSelectionChanged(self):
        index = self._view.selectionModel().currentIndex()
        selectedText = index.data(Qt.DisplayRole)
        print(selectedText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
    sys.exit()
