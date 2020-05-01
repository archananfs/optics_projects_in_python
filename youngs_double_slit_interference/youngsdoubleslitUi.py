# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youngs_double_slit.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 453)
        self.mplwidget1 = MPL_WIDGET(Dialog)
        self.mplwidget1.setGeometry(QtCore.QRect(270, 20, 800, 400))
        self.mplwidget1.setObjectName("mplwidget1")
        self.mplwidget2 = MPL_WIDGET(Dialog)
        self.mplwidget2.setGeometry(QtCore.QRect(270, 430, 800, 500))
        self.mplwidget2.setObjectName("mplwidget2")
        self.pushButton_plot = QtWidgets.QPushButton(Dialog)
        self.pushButton_plot.setGeometry(QtCore.QRect(80, 290, 131, 41))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(400, 0, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(50, 20, 211, 261))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_lambda = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_lambda.setObjectName("lineEdit_lambda")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_intensity = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_intensity.setObjectName("lineEdit_intensity")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_a = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_D = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_D.setObjectName("lineEdit_D")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_plot.setText(_translate("Dialog", "PLOT"))
        self.label_5.setText(_translate("Dialog", "Youngs Double Slit Interference"))
        self.label.setText(_translate("Dialog", "Wavelength (nm)"))
        self.label_2.setText(_translate("Dialog", "Intensity  (W/m^2)"))
        self.label_3.setText(_translate("Dialog", "apertures distance (mm)"))
        self.label_4.setText(_translate("Dialog", "Screen Distance (cm)"))
from optics_projects_in_python.fresnels_theory.mplwidget import MPL_WIDGET


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
