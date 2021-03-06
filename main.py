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
            base_name = "insert into PROJECTS (name, total_time, total_price) values ('{project}', 0, 0)"
            cursor.execute(base_name.format(project=new_project))
            ui.project_add_input.clear()
            db.commit()
            db.close()
            ui.projects_list.addItem(new_project)
            ui.projects_list.update()

    def create_base(self):
        hour_cost = 340
        sql_create_projects = """CREATE TABLE if not exists 
                projects (name TEXT, total_time INT, total_price INT)"""
        sql_create_settings = """CREATE TABLE if not exists
                settings (hour_cost INT)"""
        sql_hour_price = """INSERT into settings (hour_cost) values ('{hour_cost}')"""
        sql_check_hour_price = """SELECT hour_cost FROM settings"""
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute(sql_create_projects)
        cursor.execute(sql_create_settings)
        cursor.execute(sql_check_hour_price)
        hour_cost_now = cursor.fetchone()
        if hour_cost_now is None:
            cursor.execute(sql_hour_price.format(hour_cost=hour_cost))
        db.commit()
        db.close()

    def start_time(self):
        ui.button_start_time.hide()
        ui.button_stop_time.show()
        ui.total_price_count.setText('Таймер запущен, идёт подсчёт')
        self.start = datetime.datetime.now()

    def stop_time(self):
        ui.button_start_time.show()
        ui.button_stop_time.hide()
        self.stop = datetime.datetime.now()
        self.delta = self.stop - self.start
        self.total_time()

    def total_time(self):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        project_name = ui.projects_list.currentText()
        sql_time = "SELECT total_time FROM projects WHERE (name='{project_name}')"
        cursor.execute(sql_time.format(project_name=project_name))
        seconds_before = cursor.fetchone()[0]
        seconds_now = int(self.delta.total_seconds())
        self.total_seconds = seconds_before + seconds_now
        hours = self.total_seconds // 3600
        minutes = (self.total_seconds % 3600) // 60
        seconds = (self.total_seconds % 3600) % 60
        print(self.total_seconds)
        print(hours)
        print(minutes)
        print(seconds)
        self.display_time = '{hours}:{minutes}:{seconds}'.format(hours=hours, minutes=minutes, seconds=seconds)
        sql = "UPDATE projects SET total_time = '{delta}' WHERE name = '{project_name}'"
        cursor.execute(sql.format(delta=self.total_seconds, project_name=project_name))
        db.commit()
        db.close()
        self.total_price()

    def total_price(self):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        slq_hour_cost = "SELECT hour_cost FROM settings"
        cursor.execute(slq_hour_cost)
        hour_cost = cursor.fetchone()[0]
        project_name = ui.projects_list.currentText()
        price = (self.total_seconds // 3600) * hour_cost
        sql = "UPDATE projects SET total_price = '{delta}' WHERE name = '{project_name}'"
        cursor.execute(sql.format(delta=price, project_name=project_name))
        db.commit()
        db.close()
        display_price = '     {price} руб.'.format(price=price)
        ui.total_price_count.setText(self.display_time + display_price)

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
q.create_base()
ui.button_stop_time.hide()

"""блок с кнопками"""

ui.button_project_add.clicked.connect(Project.add_project)
ui.button_start_time.clicked.connect(q.start_time)
ui.button_stop_time.clicked.connect(q.stop_time)
ui.projects_list.addItems(q.project_list())

exit(app.exec_())
q.create_base()