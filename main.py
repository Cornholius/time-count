from PyQt5 import QtWidgets
from GUI import Ui_Dialog
from sys import exit, argv
import sqlite3
import datetime


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
		self.start = datetime.datetime.now()

	def stop_time(self):
		self.stop = datetime.datetime(2020, 5, 22)
		# self.stop = datetime.datetime.now()
		self.delta = self.stop - self.start
		self.total_time()

	def total_time(self):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		sql = "UPDATE projects SET total_time = '{delta}' WHERE name = 'test'"
		cursor.execute(sql.format(delta=self.delta))
		db.commit()
		db.close()
		qwe = int(self.delta.total_seconds())
		hours = qwe // 3600
		qwe = qwe - (hours * 3600)
		minutes = qwe // 60
		total_time = '{:02}:{:02}'.format(int(hours), int(minutes))
		ui.total_time_count.display(str(total_time))
		self.total_price()

	def total_price(self):
		price = (self.delta.total_seconds() // 3600) * 340
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		sql = "UPDATE projects SET total_price = '{delta}' WHERE name = 'test'"
		cursor.execute(sql.format(delta=price))
		db.commit()
		db.close()
		ui.total_money_count.display(str(price))


q = Project()

"""блок с кнопками"""

ui.button_project_add.clicked.connect(Project.add_project)
ui.button_start_time.clicked.connect(q.start_time)
ui.button_stop_time.clicked.connect(q.stop_time)
exit(app.exec_())
