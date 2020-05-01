# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fresnelUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1486, 718)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(580, 0, 131, 19))
        self.label_8.setObjectName("label_8")
        self.pushButton_plot = QtWidgets.QPushButton(Dialog)
        self.pushButton_plot.setGeometry(QtCore.QRect(530, 270, 191, 28))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.Mplwidget1 = MPL_WIDGET(Dialog)
        self.Mplwidget1.setGeometry(QtCore.QRect(10, 310, 600, 500))
        self.Mplwidget1.setObjectName("Mplwidget1")
        self.Mplwidget2 = MPL_WIDGET(Dialog)
        self.Mplwidget2.setGeometry(QtCore.QRect(620, 310, 600, 500))
        self.Mplwidget2.setObjectName("Mplwidget2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(340, 30, 231, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_n2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_n2.setObjectName("lineEdit_n2")
        self.gridLayout.addWidget(self.lineEdit_n2, 3, 0, 1, 1)
        self.pushButton_cal = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cal.setAutoFillBackground(False)
        self.pushButton_cal.setFlat(False)
        self.pushButton_cal.setObjectName("pushButton_cal")
        self.gridLayout.addWidget(self.pushButton_cal, 6, 0, 2, 1)
        self.lineEdit_theta1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_theta1.setObjectName("lineEdit_theta1")
        self.gridLayout.addWidget(self.lineEdit_theta1, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_n1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_n1.setObjectName("lineEdit_n1")
        self.gridLayout.addWidget(self.lineEdit_n1, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(690, 30, 191, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_rparallel = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rparallel.setFrameShape(QtWidgets.QFrame.Box)
        self.label_rparallel.setText("")
        self.label_rparallel.setObjectName("label_rparallel")
        self.verticalLayout.addWidget(self.label_rparallel)
        self.label_rperp = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rperp.setFrameShape(QtWidgets.QFrame.Box)
        self.label_rperp.setText("")
        self.label_rperp.setObjectName("label_rperp")
        self.verticalLayout.addWidget(self.label_rperp)
        self.label_tparallel = QtWidgets.QLabel(self.layoutWidget1)
        self.label_tparallel.setFrameShape(QtWidgets.QFrame.Box)
        self.label_tparallel.setText("")
        self.label_tparallel.setObjectName("label_tparallel")
        self.verticalLayout.addWidget(self.label_tparallel)
        self.label_tperp = QtWidgets.QLabel(self.layoutWidget1)
        self.label_tperp.setFrameShape(QtWidgets.QFrame.Box)
        self.label_tperp.setText("")
        self.label_tperp.setObjectName("label_tperp")
        self.verticalLayout.addWidget(self.label_tperp)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Fresnel\'s Theory "))
        self.pushButton_plot.setText(_translate("Dialog", "Plot"))
        self.pushButton_cal.setText(_translate("Dialog", "Calculate"))
        self.label_2.setText(_translate("Dialog", "RI of medium2(n2)"))
        self.label_3.setText(_translate("Dialog", "theta1 (degree)"))
        self.label.setText(_translate("Dialog", "RI of medium1(n1)"))
from optics_projects_in_python.fresnels_theory.mplwidget import MPL_WIDGET


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
