from logging import getLevelName
from os import O_NDELAY
from re import L, S
import sys
import mysql.connector
from gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from mysql.connector import Error

try:

    mydb = mysql.connector.connect(user='root',
                                host='127.0.0.1',
                                password='database_2021',
                                database='database_game')
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)


mycursor = mydb.cursor()

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


# Insert Tasks
# Tname = 'task2'
# Reward = '100'
# Cname = 'mina'
# sql = "INSERT INTO Task (Tname, Reward, Cname) \
#     VALUES (%s, %s, %s)"
# val = (Tname, Reward, Cname)
# mycursor.execute(sql, val)

# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# Insert Pet
# Pname = 'pet1'
# Hungry = '100'
# Cname = 'mina'
# sql = "INSERT INTO Pet (Pname, Hungry, Cname) \
#     VALUES (%s, %s, %s)"
# val = (Pname, Hungry, Cname)

# mycursor.execute(sql, val)

# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.on_binding_ui()
        self.text_browser_init()
    
    def text_browser_init(self):
        self.textBrowser.clear()
    
    def set_table_widget(self, data, attr_names):
        self.tableWidget.setRowCount(len(data))
        if (len(data) == 0):
            pass
        else:
            self.tableWidget.setColumnCount(len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[row])):
                newitem = QTableWidgetItem(str(data[row][col]))
                self.tableWidget.setItem(row, col, newitem)

        self.tableWidget.setHorizontalHeaderLabels(attr_names)


    def on_binding_ui(self):
        self.pushButton.clicked.connect(self.sql_input)
        self.pushButton_2.clicked.connect(self.create_character)
        self.pushButton_3.clicked.connect(self.check_task)
        self.pushButton_4.clicked.connect(self.check_pet)
        self.pushButton_5.clicked.connect(self.create_guild)
        self.pushButton_6.clicked.connect(self.check_guild)
        self.pushButton_7.clicked.connect(self.create_account)
        self.pushButton_8.clicked.connect(self.create_task)
        self.pushButton_9.clicked.connect(self.create_pet)
        self.pushButton_10.clicked.connect(self.change_guild)

    def create_account(self):
        sql = "INSERT INTO Account (Account_number, Password, Email) VALUES (%s, %s, %s)"
        account_number = self.lineEdit_8.text()
        password = self.lineEdit_7.text()
        email = self.lineEdit_9.text()
        val = (account_number, password, email)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            print("Duplicate entry " + val[0] + ", please change")

        print(mycursor.rowcount, "record inserted.")

    def create_character(self):
        account_number = self.lineEdit_19.text()
        try:
            sql = f"SELECT * FROM Account WHERE Account_number='{account_number}'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            print(myresult)
        except:
            print("please create account")

        print("access account successful")
        cname = self.lineEdit.text()
        occupation = self.lineEdit_2.text()

        if occupation == 'warrior':
            Speed = '800'
            HP = '2000'
            MP = '800'
            Power = '2000'
        elif occupation == 'mage':
            Speed = '1000'
            HP = '1000'
            MP = '2000'
            Power = '600'
        elif occupation == 'assassin':
            Speed = '2000'
            HP = '1600'
            MP = '1200'
            Power = '700'
        else:
            Speed = '100'
            HP = '100'
            MP = '100'
            Power = '100'

        Gname = 'noob'
        try:
            sql = "INSERT INTO  Role (Cname, Occupation, Speed, HP, MP, Power, \
            Anumber, Gname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (cname, occupation, Speed, HP, MP, Power, account_number, Gname)
            mycursor.execute(sql, val)
            mydb.commit()
            self.textBrowser.append(str(mycursor.rowcount)+ "record inserted.")
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")
    

    def check_task(self):
        # task_str = 0
        # try:
        #     task_str = self.lineEdit_3.text()
        #     task_id = int(task_str)
        # except:
        #     print("please input integer")
        cname = self.lineEdit_32.text()

        sql = "SHOW COLUMNS FROM Task"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        attr_names = []
        for i in myresult:
            attr_names.append(i[0])


        mycursor.execute(f"SELECT * FROM Task WHERE Cname = '{cname}'")
        myresult = mycursor.fetchall()
        self.set_table_widget(myresult, attr_names)
        


    def check_pet(self):
        cname = self.lineEdit_33.text()
        sql = "SHOW COLUMNS FROM Pet"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        attr_names = []
        # print(myresult)
        for i in myresult:
            attr_names.append(i[0])

        mycursor.execute(f"SELECT * FROM Pet WHERE Cname = '{cname}'")
        myresult = mycursor.fetchall()
        self.set_table_widget(myresult, attr_names)

    def create_guild(self):
        self.textBrowser.clear()
        try:
            cname = self.lineEdit_20.text()
            sql = "INSERT INTO Guild (Gname, Address, Level, Cname) \
                VALUES (%s, %s, %s, %s)"
            Gname = self.lineEdit_5.text()
            Address = self.lineEdit_10.text()
            val = (Gname, Address, '1', cname)
            mycursor.execute(sql, val)
            mydb.commit()
            self.textBrowser.append(str(mycursor.rowcount)+ "record inserted.")
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")
    
    def change_guild(self):
        self.textBrowser.clear()
        try:
            cname = self.lineEdit_11.text()
            sql = f"UPDATE role set Gname='{cname}'"
            mycursor.execute(sql)
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")
        
        self.textBrowser.append(str(mycursor.rowcount)+ "record inserted.")
    
    def check_guild(self):
        self.textBrowser.clear()
        cname = self.lineEdit_20.text()
        sql = "SHOW COLUMNS FROM Guild"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        attr_names = []
        for i in myresult:
            attr_names.append(i[0])
        try:
            mycursor.execute(f"SELECT * FROM Guild WHERE Cname='{cname}'")
            myresult = mycursor.fetchall()
            self.set_table_widget(myresult, attr_names)
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    def create_task(self):
        self.textBrowser.clear()
        try:
            cname = self.lineEdit_32.text()
            sql = "INSERT INTO Task (Tname, Reward, Cname) VALUES (%s, %s, %s)"
            Tname = self.lineEdit_3.text()
            val = (Tname, '100', cname)
            mycursor.execute(sql, val)
            mydb.commit()
            self.textBrowser.append(str(mycursor.rowcount)+ "record inserted.")
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")


    
    def create_pet(self):
        self.textBrowser.clear()
        try:
            cname = self.lineEdit_33.text()
            sql = "INSERT INTO Pet (Pname, Hungry, Cname) VALUES (%s, %s, %s)"
            Pname = self.lineEdit_4.text()
            val = (Pname, '100', cname)
            mycursor.execute(sql, val)
            mydb.commit()
            self.textBrowser.append(str(mycursor.rowcount)+ "record inserted.")
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")


    def sql_input(self):
        try:
            sql_str = str(self.textEdit.toPlainText())
            mycursor.execute(sql_str)
            
            myresult = mycursor.fetchall()
            for i in myresult:
                print(i)
        except mysql.connector.Error as err:
            self.textBrowser.append(f"Something went wrong: {err}")

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
