# fresnel theory top calculate reflection and transmittance coeficience

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from qt5_example.fresnelstheory.fresnelUi import *
import matplotlib.pyplot as plt
import numpy as np


class MyApp(QDialog):
    def __init__(self):

        QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_cal.clicked.connect(self.calculation)
        self.ui.pushButton_plot.clicked.connect(self.graph_plot)
        self.show()

    def calculation(self):
        n_1 = float(self.ui.lineEdit_n1.text())
        n_2 = float(self.ui.lineEdit_n2.text())
        theta1 = float(self.ui.lineEdit_theta1.text())
        theta1_rad = theta1*np.pi/180
        theta2_rad = np.arcsin((n_1/n_2)*np.sin(theta1_rad))

        # parallel component of reflection Coefficient
        r_parallel = ((n_2*np.cos(theta1_rad))-(n_1*np.cos(theta2_rad)))/(n_2*np.cos(theta1_rad)+ n_1*np.cos(theta2_rad))
        self.ui.label_rparallel.setText("r||: " + str(round(r_parallel, 4)))

        # perpendicular component of reflection Coefficient
        r_perpendicular = (n_1*np.cos(theta1_rad) - (n_2*np.cos(theta2_rad)))/(n_1*np.cos(theta1_rad) + (n_2*np.cos(theta2_rad)))
        self.ui.label_rperp.setText("r|_: " + str(round(r_perpendicular, 4)))

        # parallel component of transmission Coefficient
        t_parallel = 2*n_1*np.cos(theta1_rad) / (n_2 * np.cos(theta1_rad) + n_1 * np.cos(theta2_rad))
        self.ui.label_tparallel.setText("t||: " + str(round(t_parallel, 4)))

        # perpendicular component of reflection Coefficient
        t_perpendicular = 2*n_1*np.cos(theta1_rad) / (
                    n_1 * np.cos(theta1_rad) + (n_2 * np.cos(theta2_rad)))
        self.ui.label_tperp.setText("t|_: " + str(round(t_perpendicular, 4)))

    def graph_plot(self):
        n_1 = float(self.ui.lineEdit_n1.text())
        n_2 = float(self.ui.lineEdit_n2.text())
        theta1= np.linspace(0, 90, 18)
        theta1_rad = theta1 * np.pi / 180
        theta2 = np.arcsin((n_1/n_2)*np.sin(theta1_rad))

        r_parallel = ((n_2 * np.cos(theta1_rad)) - (n_1 * np.cos(theta2))) / (
                    n_2 * np.cos(theta1_rad) + n_1 * np.cos(theta2))
        r_perpendicular = (n_1 * np.cos(theta1_rad) - (n_2 * np.cos(theta2))) / (
                    n_1 * np.cos(theta1_rad) + (n_2 * np.cos(theta2)))
        t_parallel = 2 * n_1 * np.cos(theta1_rad) / (n_2 * np.cos(theta1_rad) + n_1 * np.cos(theta2))
        t_perpendicular = 2 * n_1 * np.cos(theta1_rad) / (
                n_1 * np.cos(theta1_rad) + (n_2 * np.cos(theta2)))

        labels = ["r||", "r|_", "t|_", "t||"]
        plot1 = self.ui.Mplwidget1.canvas
        plot1.ax.clear()
        plot1.ax.set_xlabel("Angle of incidence")
        plot1.ax.set_ylabel("Coefficient value")
        plot1.figure.suptitle("Fresnel's Law", fontsize=12, fontweight='bold')
        plot1.ax.plot(theta1, r_parallel, label="r||")
        plot1.ax.plot( theta1, r_perpendicular, label="r|_")
        plot1.ax.plot(theta1, t_perpendicular, label = "t|_")
        plot1.ax.plot(theta1, t_parallel, label = "t||")
        plot1.ax.legend()

        plot1.draw()

        # Reflectance
        R_par = r_parallel**2
        R_perp = r_perpendicular**2

        # Second graph
        plot2 = self.ui.Mplwidget2.canvas
        plot2.ax.clear()
        plot2.ax.set_xlabel("Angle of incidence")
        plot2.ax.set_ylabel("Reflectance value")
        plot2.figure.suptitle("Reflectance v/s Angle of Incidence", fontsize=12, fontweight='bold')
        plot2.ax.plot(theta1, R_par, label="R_parallel")
        plot2.ax.plot(theta1, R_perp, label = "R_perpendicular")
        plot2.ax.legend()
        plot2.draw()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MyApp()
    a.show()
    sys.exit(app.exec_())