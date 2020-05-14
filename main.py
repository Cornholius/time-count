from PyQt5 import QtWidgets, QtCore
from GUI import Ui_Dialog
from sys import exit, argv
import sqlite3


app = QtWidgets.QApplication(argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()


class Project:

	def add_project(self):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		new_project = ui.project_add_input.text()
		if new_project is not '':
			base_name = "insert into PROJECTS (project_name) values ('{project}')"
			cursor.execute(base_name.format(project=new_project))
			ui.project_add_input.clear()
			db.commit()
			db.close()

	def start_time(self):
		pass







"""блок с кнопками"""

ui.button_project_add.clicked.connect(Project.add_project)
ui.button_start_time.clicked.connect(Project.start_time)
ui.button_stop_time.clicked.connect(Project.add_project)

exit(app.exec_())
