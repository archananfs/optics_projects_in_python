from numpy import sin, cos, array, linspace, arcsin, sqrt, pi
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from prism.prismUi import *

class DeflectionAngle(QDialog):
    def __init__(self):

        QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_calc.clicked.connect(self.calculation)
        self.ui.pushButton.clicked.connect(self.graph_plot)
        self.show()

    def calculation(self):
        n = float(self.ui.lineEdit_n.text())
        alpha = float(self.ui.lineEdit_apex.text()) * (pi/180)
        theta = float(self.ui.lineEdit_theta.text()) * (pi/180)

        a = (sqrt(n**2 - sin(theta)**2)*sin(alpha) - (sin(theta)*cos(alpha)))
        theta_deflection = theta - alpha + arcsin(a)
        theta_deflection = theta_deflection*(180/pi)
        self.ui.lineEdit_def.setText(str(round(theta_deflection, 4)))

    def graph_plot(self):
        theta = linspace(0, 90, 100)
        theta_rad = theta*(pi/180)
        n = float(self.ui.lineEdit_n.text())
        alpha = array([5, 10, 30, 60])
        alpha_rad = alpha*(pi/180)
        theta_deflist = []

        for ele in range(len(alpha_rad)):
            a = (sqrt(n ** 2 - sin(theta_rad) ** 2) * sin(alpha_rad[ele]) - (sin(theta_rad) * cos(alpha_rad[ele])))
            theta_deflection = theta_rad - alpha_rad[ele] + arcsin(a)
            theta_deflection = theta_deflection * (180 / pi)
            theta_deflist.append(theta_deflection)

        plot1 = self.ui.Mplwidget.canvas
        plot1.ax.clear()
        plot1.ax.set_xlabel("Angle of incidence")
        plot1.ax.set_ylabel("Angle of Deflection")
        plot1.figure.suptitle("Deflection in Prism", fontsize=12, fontweight='bold')

        for i in range(len(theta_deflist)):
            plot1.ax.plot(theta, theta_deflist[i], label="alpha ={} degree".format(alpha[i]))
            plot1.ax.legend()

        plot1.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = DeflectionAngle()
    a.show()
    sys.exit(app.exec_())


