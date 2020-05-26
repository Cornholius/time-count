# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI_M.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 285)
        self.button_project_add = QtWidgets.QPushButton(Dialog)
        self.button_project_add.setGeometry(QtCore.QRect(240, 20, 100, 23))
        self.button_project_add.setObjectName("button_project_add")
        self.project_add_input = QtWidgets.QLineEdit(Dialog)
        self.project_add_input.setGeometry(QtCore.QRect(20, 20, 200, 25))
        self.project_add_input.setObjectName("project_add_input")
        self.projects_list = QtWidgets.QComboBox(Dialog)
        self.projects_list.setGeometry(QtCore.QRect(20, 55, 200, 25))
        self.projects_list.setObjectName("projects_list")
        self.button_start_time = QtWidgets.QPushButton(Dialog)
        self.button_start_time.setGeometry(QtCore.QRect(30, 175, 140, 90))
        self.button_start_time.setObjectName("button_start_time")
        self.button_stop_time = QtWidgets.QPushButton(Dialog)
        self.button_stop_time.setGeometry(QtCore.QRect(190, 175, 140, 90))
        self.button_stop_time.setObjectName("button_stop_time")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 90, 320, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 145, 320, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.total_time_count = QtWidgets.QLabel(Dialog)
        self.total_time_count.setGeometry(QtCore.QRect(20, 110, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_time_count.setFont(font)
        self.total_time_count.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.total_time_count.setObjectName("total_money_count")
        self.total_price_count = QtWidgets.QLabel(Dialog)
        self.total_price_count.setGeometry(QtCore.QRect(190, 110, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_price_count.setFont(font)
        self.total_price_count.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.total_price_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_price_count.setObjectName("total_price_count")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Time count"))
        self.button_project_add.setText(_translate("Dialog", "Создать проект"))
        self.button_start_time.setText(_translate("Dialog", "Старт"))
        self.button_stop_time.setText(_translate("Dialog", "Стоп"))
        self.total_time_count.setText(_translate("Dialog", ""))
        self.total_price_count.setText(_translate("Dialog", ""))
