# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_calc.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(753, 833)
        self.Mplwidget = MPL_WIDGET(Dialog)
        self.Mplwidget.setGeometry(QtCore.QRect(90, 230, 600, 500))
        self.Mplwidget.setObjectName("Mplwidget")
        self.pushButton_graph = QtWidgets.QPushButton(Dialog)
        self.pushButton_graph.setGeometry(QtCore.QRect(400, 140, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_graph.setFont(font)
        self.pushButton_graph.setObjectName("pushButton_graph")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(400, 10, 231, 121))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_ans = QtWidgets.QLabel(self.splitter)
        self.label_ans.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ans.setText("")
        self.label_ans.setObjectName("label_ans")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(170, 0, 181, 181))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.lineEdit_n1 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_n1.setObjectName("lineEdit_n1")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_n2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_n2.setObjectName("lineEdit_n2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_theta = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_theta.setObjectName("lineEdit_theta")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_graph.setText(_translate("Dialog", "Graph"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">RI (n1)</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">RI (n2)</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">theta1(degree)</span></p></body></html>"))
from optics_projects_in_python.fresnels_theory.mplwidget import MPL_WIDGET


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
