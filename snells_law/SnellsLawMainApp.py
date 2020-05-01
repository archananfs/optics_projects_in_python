import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from qt5_example.snells_law.SnellsLawUi import *
import numpy as np


class SnellsLaw(QDialog):
    def __init__(self):

        QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.snellslaw_calc)
        self.ui.pushButton_graph.clicked.connect(self.graph_plot)
        self.show()



    def snellslaw_calc(self):
        n_1 = float(self.ui.lineEdit_n1.text())
        n_2 = float(self.ui.lineEdit_n2.text())
        theta1 = float(self.ui.lineEdit_theta.text())

        theta1_rad = (theta1 * np.pi) / 180
        theta2 = np.arcsin((n_1 * np.sin(theta1_rad)) / n_2)
        theta2_disp = theta2 * (180 / np.pi)

        self.ui.label_ans.setText("theta2 (degree): " + str(round(theta2_disp, 2)))



    def graph_plot(self):
        theta_incidence = np.linspace(-90, 90, 180)

        n_1 = float(self.ui.lineEdit_n1.text())
        n_2 = float(self.ui.lineEdit_n2.text())

        theta_medium2 = np.arcsin((n_1 * np.sin(theta_incidence*(np.pi/180)) / n_2))

        mpl = self.ui.Mplwidget.canvas
        mpl.ax.clear()
        mpl.ax.set_xlabel("Angle of Incidence")
        mpl.ax.set_ylabel("Refraction Angle")
        mpl.figure.suptitle("Snell's Law", fontsize=12, fontweight ='bold')
        mpl.ax.plot(theta_incidence, theta_medium2*(180/np.pi))

        mpl.draw()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = SnellsLaw()
    a.show()
    sys.exit(app.exec_())