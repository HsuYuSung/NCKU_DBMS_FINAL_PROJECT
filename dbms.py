from os import O_NDELAY
import sys
import mysql.connector
from gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from mysql.connector import Error

try:

    cnx = mysql.connector.connect(user='root',
                                host='127.0.0.1',
                                password='database_2021',
                                database='database_game')
    if cnx.is_connected():
        db_Info = cnx.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = cnx.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)


mycursor = cnx.cursor()

# sql = "INSERT INTO Account (Account_number, Password, Email) VALUES (%s, %s, %s)"
# # val = [
# #     ("eva1999", "pass_eva", "eva@gmail.com"),
# #     ("john1999", "pass_john", "john@gmail.com"),
# #     ("elsa1999", "pass_elsa", "elsa@gmail.com"),
# #     ("pan1999", "pass_pan", "pan@gmail.com"),
# # ]
# val = ("nana1999", "pass_nana", "nana@gmail.com")




# mycursor.execute("SELECT * FROM account")
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.on_binding_ui()
        self.change_name()
    
    def change_name(self):
        self.tab.setWindowTitle('gogo')
        self.tab_2.setWindowTitle('check')

    def on_binding_ui(self):
        self.pushButton.clicked.connect(self.sql_input)
        self.pushButton_2.clicked.connect(self.create_character)
        self.pushButton_3.clicked.connect(self.check_task)
        self.pushButton_4.clicked.connect(self.check_pet)
        self.pushButton_5.clicked.connect(self.create_guild)
        self.pushButton_6.clicked.connect(self.check_guild)
        self.pushButton_7.clicked.connect(self.create_account)
    
    def sql_input(self):
        sql_str = str(self.textEdit.toPlainText())
        mycursor.execute(sql_str)

        myresult = mycursor.fetchall()
        for i in myresult:
            print(i)

    def create_account(self):
        sql = "INSERT INTO Account ()"
        print("create account")

    def create_character(self):
        cname = self.lineEdit.text()
        occupation = self.lineEdit_2.text()
        sql = "INSERT INTO account ()"
        print(cname, occupation)
    
    def check_task(self):
        task_str = 0
        try:
            task_str = self.lineEdit_3.text()
            task_id = int(task_str)
        except:
            print("please input integer")
        print(task_id)

    def check_pet(self):
        pet_str = 0
        try:
            pet_str = self.lineEdit_4.text()
            pet_id = int(pet_str)
        except:
            print("please input integer")

        print(pet_str)

    def create_guild(self):
        print('create_guild')
    
    def check_guild(self):
        print('check_guild')
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
