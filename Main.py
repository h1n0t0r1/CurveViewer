import sys
from PyQt5 import Qt
from os.path import expanduser
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileSystemModel, QTreeView, QVBoxLayout

from Misc import PlotCanvas, MyMplCanvas


class Program(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Create Plot Canvas
        self.canvas = MyMplCanvas(self, 6, 5)

        # Create File Tree View

        # Container for treeview, needed bcz treeview work only with box layout
        self.container = QWidget(self)
        self.container.resize(550, 700)
        self.container.move(620, 50)

        self.model = QFileSystemModel()
        self.path = '{}\\Desktop'.format(expanduser('~'))
        self.model.setRootPath('')

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle("Dir View")
        self.tree.sortByColumn(1, 0)
        # self.tree.setRootIndex(self.model.index(self.path))

        self.tree.resize(550, 700)
        self.tree.setColumnWidth(0, 200)
        # self.tree.clicked.connect(self.file_selected)
        self.tree.selectionModel().selectionChanged.connect(self.file_selected)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.container.setLayout(windowLayout)

        # Program Settings
        self.setWindowTitle('Curve Viewer by Automationpro')
        self.setWindowIcon(QIcon('img\\icon.png'))
        self.show()
        self.resize(1200, 800)
        self.move(200, 200)

    def file_selected(self):
        try:
            selected = self.tree.selectedIndexes()
            file = selected[0].data()
            if file.lower().endswith(('.xlsx')):
                path = self.model.filePath(selected[0])
                self.extract_data(path)
        except:
            pass

    def extract_data(self, f):
        # self.canvas.plot([0])
        try:
            dataFrame1 = pd.read_excel(f, sheetname="Data", parse_cols=[1])
            dataFrame2 = pd.read_excel(f, sheetname="Data", parse_cols=[0])
            data = [dataFrame1, dataFrame2]

            file_only = f.split('/')  # [1]
            if len(file_only) > 1:
                file_only = file_only[len(file_only) - 1]
                data.append(file_only)
            else:
                file_only = file_only[0]

            self.canvas.plot(data)
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())