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
			base_name = "insert into PROJECTS (name) values ('{project}')"
			cursor.execute(base_name.format(project=new_project))
			ui.project_add_input.clear()
			db.commit()
			db.close()

	def start_time(self):
		ui.total_time_count.update()
		self.start = datetime.datetime.now()

	def stop_time(self):
		self.stop = datetime.datetime(2020, 5, 22)
		# self.stop = datetime.datetime.now()
		self.delta = self.stop - self.start
		self.total_time()

	def total_time(self):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		project_name = ui.projects_list.currentText()
		seconds = int(self.delta.total_seconds())
		hours = seconds // 3600
		seconds = seconds - (hours * 3600)
		minutes = seconds // 60
		sql_time = "SELECT total_time FROM projects WHERE name '{project_name}'"
		cursor.execute(sql_time.format(project_name=project_name))
		time_before = cursor.fetchone()
		print(type(time_before), type(self.delta))
		total_time = time_before + self.delta
		sql = "UPDATE projects SET total_time = '{delta}' WHERE name = '{project_name}'"
		cursor.execute(sql.format(delta=self.delta, project_name=project_name))
		db.commit()
		db.close()

		total_time = '{:02}:{:02}'.format(int(hours), int(minutes))
		ui.total_time_count.display(str(total_time))
		self.total_price()

	def total_price(self):
		price = (self.delta.total_seconds() // 3600) * 340
		project_name = ui.projects_list.currentText()
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		sql = "UPDATE projects SET total_price = '{delta}' WHERE name = '{project_name}'"
		cursor.execute(sql.format(delta=price, project_name=project_name))
		db.commit()
		db.close()
		ui.total_money_count.display(str(price))

	def project_list(self):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		sql = "SELECT name FROM projects"
		cursor.execute(sql)
		row = cursor.fetchall()
		db.close()
		pr_list = []
		for item in row:
			for pr_name in item:
				pr_list.append(str(pr_name))
		return pr_list


q = Project()
# q.project_list()

"""блок с кнопками"""

ui.button_project_add.clicked.connect(Project.add_project)
ui.button_start_time.clicked.connect(q.start_time)
ui.button_stop_time.clicked.connect(q.stop_time)
ui.projects_list.addItems(q.project_list())

exit(app.exec_())
