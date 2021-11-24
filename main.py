import sys
from PyQt5.uic import loadUi  # ignore this errors
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import sqlite3

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(r"C:\Users\auto_\Python project\miit\welcomescreen.ui", self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi(r"C:\Users\auto_\Python project\miit\login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")
        else:
            with sqlite3.connect("shop_data.db") as conn:
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS login_info (
                            username TEXT,
                            password TEXT
                            )""")
                cur.execute('SELECT password FROM login_info WHERE username =\''+user+"\'")
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    print("Succesfully logged in.")
                else:
                    print("error!!!!")
                    self.error.setText("Invalid username or password")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi(r"C:\Users\auto_\Python project\miit\createacc.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password) # hidden password
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)  # hidden confirmpassword
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.error.setText("Please input all fields.")

        elif password != confirmpassword:
            self.error.setText("Passwords do not match!")
        else:
            with sqlite3.connect("shop_data.db") as conn:
                cur = conn.cursor()
                user_info = [user, password]
                cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)
                fillprofile = FillProfileScreen()
                widget.addWidget(fillprofile)
                widget.setCurrentIndex(widget.currentIndex()+1)

class FillProfileScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi(r"C:\Users\auto_\Python project\miit\fillprofile.ui", self)


class Adminprofile(QDialog):
    def __init__(self):
        super(Adminprofile, self).__init__()
        loadUi(r"C:\Users\auto_\Python project\miit\Adminprofile.ui", self)


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
