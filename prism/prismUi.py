# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prism.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 486)
        self.Mplwidget = Mpl_Widget(Dialog)
        self.Mplwidget.setGeometry(QtCore.QRect(320, 90, 700, 550))
        self.Mplwidget.setObjectName("Mplwidget")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 100, 271, 411))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_n = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_theta = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_theta.setObjectName("lineEdit_theta")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_apex = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_apex.setObjectName("lineEdit_apex")
        self.pushButton_calc = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_calc.setFont(font)
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.label_7 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_def = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_def.setObjectName("lineEdit_def")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Plot"))
        self.label.setText(_translate("Dialog", "Refractive index (n)"))
        self.label_3.setText(_translate("Dialog", "Angle of incidence (theta)"))
        self.label_5.setText(_translate("Dialog", "Apex Angle (alpha)"))
        self.pushButton_calc.setText(_translate("Dialog", "Calculate"))
        self.label_7.setText(_translate("Dialog", "Deflection Angle"))
from fresnels_theory.mplwidget import Mpl_Widget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
