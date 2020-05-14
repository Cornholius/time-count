from PySide2 import QtWidgets, QtCore
from GUI import Ui_Dialog
from sys import exit, argv


app = QtWidgets.QApplication(argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()


class Project:

	def add_project(self):
		pass

















"""блок с кнопками"""

ui.button_project_add.clicked.connect(qwe)




exit(app.exec_())
