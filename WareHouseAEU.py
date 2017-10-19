"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
--------------------------PROGRAM--FOR--TEMPORARY--WAREHOUSE--ON--AEU----------------------
1. This program can add data to DB CableWarehouse on cellular warehouse for production
    What class we using for this task?
    -
2. This program have secure module for work with different premission with data
    What class we using for this task?
    -
3. This program can search find  a tube with a coil of cable along the SAP number and if You
take this coil, program clear data about this coil from DB
    What class we using for this task?
    -
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
import connectionAEU
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget,
                             QStackedWidget, QAction, qApp, QLabel, QLineEdit,
                             QHBoxLayout, QInputDialog, QStackedLayout,
                             QListWidget, QFormLayout)


from PyQt5.QtGui import QIcon, QFont, QPixmap, QIntValidator, QRegExpValidator, QKeyEvent
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.Qt import QMainWindow


class WarehouseMain(QMainWindow):

    #Create Main Wondow and using QStackedWidget
    def __init__(self, parent=None):
        super(WarehouseMain, self).__init__(parent)
        self.centralWinget = QStackedWidget()
        self.setCentralWidget(self.centralWinget)
        loginWidget = LoginWidget(self)

        loginWidget.button.clicked.connect(self.UIinit)
        self.centralWinget.setCurrentWidget(loginWidget)


    def UIinit(self):
        self.mainbtn = MainButton(self)
        self.centralWidget.addWidget(self.mainbtn)
        self.centralWinget.setCurrentWidget(self.mainbtn)

class MainButton(QWidget):
    def __init__(self, parent=None):

        #Creat main layout with 2 buttons for select
        super(MainButton, self).__init__(parent)
        layout = QHBoxLayout()
        self.uiInit = inputUI(self)
        self.uiSearch = SearchUI(self)
        self.btnInitUI = QPushButton('<b>INPUT TO DB WAREHOUSE</b>')
        self.btnSearchUI = QPushButton('<b>SEARCH PLACE</b>')
        layout.addWidget(self.btnInitUI)
        layout.addWidget(self.btnSearchUI)
        self.btnInitUI.clicked.connect(self.uiInit)
        self.btnSearchUI.clicked.connect(self.uiSearch)
        self.setLayout(layout)

class LoginWidget(QWidget):
    def __init__(self, parent=None):

        #Create layout for from Logining
        super(LoginWidget, self).__init__(parent)
        layout = QHBoxLayout()


        #Lable edit fot login
        layout.addWidget(QLabel("Login - >"))
        login = QLineEdit()


        layout.addWidget(login)

        #Lable edit for password with hint method
        layout.addWidget(QLabel("Password - >"))
        password = QLineEdit()
        password.setEchoMode(QLineEdit.Password)
        layout.addWidget(password)

        #Convert to text input data
        self.textLogin = login.text()
        self.textPassword = password.text()

        #Create lable with picture but need chek some problem
        pixmap = QPixmap("D:\LearnPython\AEU\password.pgn")
        pixmap.devicePixelRatio()
        self.lblLogining = QLabel(self)
        self.lblLogining.setPixmap(pixmap)

        #Create button LOGIN
        self.button = QPushButton("LOGIN")
        layout.addWidget(self.button)
        self.setLayout(layout)


class ErrorLoginWidget(QWidget):
    def __init__(self, parent=None):

        #Create layout for error UI
        super(ErrorLoginWidget, self).__init__(parent)
        layout = QFormLayout()
        self.label= QLabel('Invalid Password or Login please try again or call to support center')
        layout.addWidget(self.label)
        self.setLayout(layout)


class showDialog(QWidget):
    def __init__(self,parent=None):
        #This create layout for dialog answer
        super(showDialog, self).__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel("Info %s" % self.info)
        layout.addWidget(self.label)
        self.setLayout(layout)

class eventWidget(QWidget):
    def __init__(self):

        self.closeevent()
        self.center()
        self.tooltip()

    def closeevent(self, event):
        #Create message box with close event
        reply = QMessageBox.question(self, 'Quit Message',
                                     "Are You sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        #Set window to center display
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def tooltip(self, infoToolTip):
        #Create Tool Tip massege
        QToolTip.setFont(QFont('SansSerif', 14))

        self.setToolTip('This is a <b>%s</b>' % infoToolTip)

class inputUI(QWidget):
    #This class work with input data to DB WareHouse
    def __init__(self, parent=None):
        super(inputUI, self).__init__(parent)
        layout = QFormLayout()
        pixmap = QPixmap("D:\LearnPython\AEU\Input.png")

        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QuitButton</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(400, 410)

        self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))

        self.inputLable()
        self.setLayout(layout)

    def inputLable(self):
        #Here lable for input data
        self.lblMatNum = QLabel(self)
        self.lblVenBat = QLabel(self)
        self.lblPlace = QLabel(self)

        self.lblMatNum.setText('MatNum >')
        self.lblMatNum.setFont(QFont("Arial", 12))
        self.lblVenBat.setText('VenBat >')
        self.lblVenBat.setFont(QFont("Arial", 12))
        self.lblPlace.setText('Place>')
        self.lblPlace.setFont(QFont("Arial", 11))

        self.qleMatNum = QLineEdit(self)
        self.qleMatNum.setValidator(QIntValidator())
        self.qleMatNum.setMaxLength(8)
        self.qleMatNum.move(215, 305)
        self.qleMatNum.setFocus()
        self.qleMatNum.returnPressed.connect(self.changeFocustoVen)

        self.qleVenBat = QLineEdit(self)
        self.qleVenBat.setValidator(QIntValidator())
        self.qleVenBat.setMaxLength(10)
        self.qleVenBat.returnPressed.connect(self.changeFocustoPlasce)

        self.qlePlace = QLineEdit(self)
        # qlePlace.setValidator(QRegExpValidator('W'))
        self.qlePlace.setMaxLength(9)
        self.qlePlace.setInputMask('w9e-99-99')
        self.qlePlace.setFont(QFont("Arial", 14))
        self.qlePlace.returnPressed.connect(self.saveSql)

        self.qleMatNum.move(215, 305)
        self.qleVenBat.move(215, 335)
        self.qlePlace.move(215, 365)

        self.lblMatNum.move(140, 305)
        self.lblVenBat.move(150, 335)
        self.lblPlace.move(170, 365)

class MsSqlValidator():
    #This class work with data from UI and input to DB Warehouse
    def __init__(self, textMN, textVB, textP):
        self.conn = connectionAEU.TakeDataSql()

        qle = inputUI.inputLable()

        self.qleValues = []
        textMatNum = textMN

class SearchUI(QWidget):
    def __init__(self, parent=None):
        super(SearchUI, self).__init__(parent)
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = WarehouseMain()
    window.show()
    app.exec()


