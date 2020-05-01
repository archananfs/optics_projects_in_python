import sys
import numpy as np

from PyQt5 import QtWidgets ,QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        # Create a canvas

        canvas1 = FigureCanvas(Figure(figsize=(7, 7)))
        layout.addWidget(canvas1)
        self.addToolBar(NavigationToolbar(canvas1, self))

        # equations

        lamda = np.linspace(0.001, 4, 100)
        h = 6.62607015*1.E-34 # planks constant Unit - J.s
        c = 3*1.E+8           # speed of light Unit = m/s
        k = 1.380649*1.E-23
        Temp = [2500, 3000, 4000] # Temperature
        energy_density = []

        for T in Temp:
            a = 2*h*c**2/((lamda*1.E-6)**5)
            b = np.exp(h*c/((lamda*1.E-6)*k*T))-1
            u = a/b

            energy_density.append(u)

        #plotting graphs in canvas1

        self.canvas1_ax = canvas1.figure.subplots()
        self.canvas1_ax.plot(lamda, energy_density[0], label="T=2500K")
        self.canvas1_ax.plot(lamda, energy_density[1], label="T=3000K")
        self.canvas1_ax.plot(lamda, energy_density[2], label="T=4000K")
        self.canvas1_ax.legend()
        canvas1.figure.suptitle("Planck's law of black-body radiation", fontsize =14, fontweight='bold')
        self.canvas1_ax.set_xlabel("Wavelength in microns")
        self.canvas1_ax.set_ylabel("Energy Density (W·sr−1·m−3)")



if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = Window()
    app.show()
    qapp.exec_()