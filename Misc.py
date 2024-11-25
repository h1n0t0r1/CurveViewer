from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def plot(self,data, color='red', title=''):
        self.axes.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data, color)
        ax.set_title(title)
        ax.grid(color='b', linestyle='-', linewidth=0.5)
        self.draw()

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        # self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)




    def plot(self, data, color='red', title='filename'):
        self.axes.cla()
        self.axes.plot(data[1], data[0], color)
        self.axes.set_xlabel('Position')
        self.axes.set_ylabel('Force')
        self.axes.grid(color='b', linestyle='-', linewidth=0.5)
        if title == 'filename':
            self.axes.set_title(data[2])
        self.draw()

    def pie(self, data, labels=None, colors=None, shadow=False, legend=False):
        self.axes.cla()
        self.axes.pie(data, colors=colors, labels=labels, autopct = '%1.2f%%', shadow=shadow)
        # self.axes.legend(labels, loc='best')

