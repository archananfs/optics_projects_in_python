import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from optics_projects_in_python.youngs_double_slit_interference.youngsdoubleslitUi import *
import numpy as np


class Youngs_Interference(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_plot.clicked.connect(self.graph_plot)
        self.show()

    def graph_plot(self):
        lamda = float(self.ui.lineEdit_lambda.text())*1.E-9
        a = float(self.ui.lineEdit_a.text())*1.E-3
        D = float(self.ui.lineEdit_D.text())*1.E-2
        I_o = float(self.ui.lineEdit_intensity.text())

        x = np.linspace(-0.2, 0.2, 100)
        y = np.linspace(-0.2, 0.2, 100)
        I = 4*I_o*(np.cos(y*a*np.pi/D/lamda))**2
        plot1 = self.ui.mplwidget1.canvas
        plot1.ax.clear()
        plot1.figure.suptitle("Intensity Variation", fontsize=12, fontweight='bold')
        plot1.ax.set_xlabel("Distance")
        plot1.ax.set_ylabel("Intensity")
        plot1.ax.plot(y, I)
        plot1.draw()

        # second plot
        X,Y = np.meshgrid(x, y)
        I_im = 4*I_o*(np.cos(Y*a*np.pi/D/lamda))**2
        plot2 = self.ui.mplwidget2.canvas
        plot2.ax.clear()
        cp = plot2.ax.contourf(X, Y, I_im, cmap='gist_heat')
        plot2.ax.set_xlabel("X(cm)")
        plot2.ax.set_ylabel("Y(cm)")
        plot2.figure.colorbar(cp)
        plot2.figure.suptitle("Intensity Variation of fringes", fontsize=12,
                              fontweight='bold')
        plot2.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Youngs_Interference()
    a.show()
    sys.exit(app.exec_())