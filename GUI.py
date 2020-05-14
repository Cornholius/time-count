# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 360)
        self.button_project_add = QtWidgets.QPushButton(Dialog)
        self.button_project_add.setGeometry(QtCore.QRect(300, 20, 140, 23))
        self.button_project_add.setObjectName("button_project_add")
        self.project_add_input = QtWidgets.QLineEdit(Dialog)
        self.project_add_input.setGeometry(QtCore.QRect(20, 20, 260, 25))
        self.project_add_input.setObjectName("project_add_input")
        self.projects_list = QtWidgets.QComboBox(Dialog)
        self.projects_list.setGeometry(QtCore.QRect(20, 55, 260, 25))
        self.projects_list.setObjectName("projects_list")
        self.button_start_time = QtWidgets.QPushButton(Dialog)
        self.button_start_time.setGeometry(QtCore.QRect(300, 140, 140, 90))
        self.button_start_time.setObjectName("button_start_time")
        self.button_stop_time = QtWidgets.QPushButton(Dialog)
        self.button_stop_time.setGeometry(QtCore.QRect(300, 250, 140, 90))
        self.button_stop_time.setObjectName("button_stop_time")
        self.total_time_count = QtWidgets.QLCDNumber(Dialog)
        self.total_time_count.setGeometry(QtCore.QRect(20, 140, 220, 60))
        self.total_time_count.setObjectName("total_time_count")
        self.total_money_count = QtWidgets.QLCDNumber(Dialog)
        self.total_money_count.setGeometry(QtCore.QRect(20, 220, 220, 60))
        self.total_money_count.setObjectName("total_money_count")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_project_add.setText(_translate("Dialog", "Добавить проект"))
        self.button_start_time.setText(_translate("Dialog", "Старт"))
        self.button_stop_time.setText(_translate("Dialog", "Стоп"))
