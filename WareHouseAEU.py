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
                             QListWidget, QFormLayout, QVBoxLayout, QGroupBox)


from PyQt5.QtGui import QIcon, QFont, QPixmap, QIntValidator, QRegExpValidator, QKeyEvent
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.Qt import QMainWindow


class WarehouseMain(QMainWindow):

    #Create Main Wondow and using QStackedWidget
    def __init__(self, parent=None):
        super(WarehouseMain, self).__init__(parent)
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        loginWidget = LoginWidget(self)
        loginWidget.button.clicked.connect(self.UIinit)
        self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))



        self.centralWidget.addWidget(loginWidget)
        self.setGeometry(300, 300, 420, 200)
        self.show()

    def UIinit(self):
        #Initializate Main Button widget
        self.mainbtn = MainButton(self)
        self.centralWidget.addWidget(self.mainbtn)
        self.centralWidget.setCurrentWidget(self.mainbtn)
        self.mainbtn.btnInitUI.clicked.connect(self.UIinput)
        self.mainbtn.btnSearchUI.clicked.connect(self.UIsearch)


    def erroLWidget(self):
        self.eLWidget = ErrorLoginWidget(self)
        self.centralWinget.addWidget(self.eLWidget)
        self.centralWinget.setCurrentWidget(self.eLWidget)

    def UIinput(self):
        self.inpbtn = inputUI(self)
        self.centralWidget.addWidget(self.inpbtn)
        self.centralWidget.setCurrentWidget(self.inpbtn)
        self.inpbtn.qlePlace.returnPressed.connect(self.DBhelper)

    def DBhelper(self):
        self.dbhelper = MsSqlValidator(self)


    def UIsearch(self):
        self.searchbtn = SearchUI(self)
        self.centralWidget.addWidget(self.searchbtn)
        self.centralWidget.setCurrentWidget(self.searchbtn)


class MainButton(QWidget):
    def __init__(self, parent=None):

        #Creat main layout with 2 buttons for select
        super(MainButton, self).__init__(parent)
        layout = QVBoxLayout()
        #self.centralWidget2 = QStackedWidget()
        self.btnInitUI = QPushButton('INPUT TO DB WAREHOUSE')
        self.btnSearchUI = QPushButton('SEARCH PLACE')
        layout.addWidget(self.btnInitUI)
        layout.addWidget(self.btnSearchUI)
        self.btnInitUI.setFont(QFont("Arial", 14))
        self.btnSearchUI.setFont(QFont("Arial", 14))

        pixmap = QPixmap("D:\LearnPython\AEU\impg7.jpg")
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()
        self.setGeometry(10, 10, 400, 200)
        self.setLayout(layout)

class LoginWidget(QWidget):
    def __init__(self, parent=None):

        #Create layout for from Logining
        super(LoginWidget, self).__init__(parent)

        layout = QVBoxLayout()

        #Lable edit fot login
        layout.addWidget(QLabel("Login - >"))
        self.login = QLineEdit()
        layout.addWidget(self.login)
        layout.addWidget(QLabel("Password - >"))
        self.password = QLineEdit()
        layout.addWidget(self.password)
        #Lable edit for password with hint method
        self.password.setEchoMode(QLineEdit.Password)


        #Convert to text input data
        self.textLogin = self.login.text()
        self.textPassword = self.password.text()

        #Create lable with picture but need chek some problem
        pixmap = QPixmap("D:\LearnPython\AEU\password.pgn")
        pixmap.devicePixelRatio()
        self.lblLogining = QLabel(self)
        self.lblLogining.setPixmap(pixmap)
        self.lblLogining.show()
        #Create button LOGIN
        self.button = QPushButton("LOGIN")
        layout.addWidget(self.button)
        layout.addWidget(self.lblLogining)
        self.button.setFont(QFont("Arial", 14))
        self.button.clicked.connect(self.validAccess)

        pixmap = QPixmap("D:\LearnPython\AEU\impg7.jpg")
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()

        self.setGeometry(10, 10, 400, 200)
        self.setLayout(layout)

    def validAccess(self):
        loginValid = self.login.text()
        paswordValid = self.password.text()
        self.conn = connectionAEU.TakeDataSql(loginValid, paswordValid)




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
        layout = QHBoxLayout()
        pixmap = QPixmap("D:\LearnPython\AEU\impg7.jpg")
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()

        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QuitButton</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(330, 170)

        #self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))
        self.setGeometry(100, 100, 400, 200)
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
        self.lblPlace.setFont(QFont("Arial", 12))

        self.qleMatNum = QLineEdit(self)
        self.qleMatNum.setValidator(QIntValidator())
        self.qleMatNum.setMaxLength(8)
        #self.qleMatNum.move(215, 305)
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
        self.qlePlace.returnPressed.connect(self.MsSqlValidator)

        self.qleMatNum.move(165,35)
        self.qleVenBat.move(165, 75)
        self.qlePlace.move(165, 125)

        self.lblMatNum.move(95, 35)
        self.lblVenBat.move(100, 75)
        self.lblPlace.move(115, 125)
        self.setGeometry(100, 100, 400, 200)

    def changeFocustoVen(self):

        self.qleVenBat.setFocus()

    def changeFocustoPlasce(self):

        self.qlePlace.setFocus()

    def changeFocusBtn(self):

        self.btnOk.setFocus()

    def MsSqlValidator(self):

        self.qleValues = []
        textMatNum = self.qleMatNum.text()
        textVenBat = self.qleVenBat.text()
        textPlace = self.qlePlace.text()
        self.qleValues.append(textMatNum)
        self.qleValues.append(textVenBat)
        self.qleValues.append(textPlace)
        print(self.qleValues)
        self.conn = connectionAEU.TakeDataSql()
        verifyValue = self.conn.VerifyMaterial(textMatNum)

        if len(self.qleValues) != 0:
            self.conn.Save(self.qleValues)
            self.qleMatNum.clear()
            self.qleVenBat.clear()
            self.qlePlace.clear()
            self.qleMatNum.setFocus()
        else:
            print('incorect data')

"""class MsSqlValidator():
    #This class work with data from UI and input to DB Warehouse
    def __init__(self):

        self.qleValues = []
        textMatNum = inputUI.qleMatNum()
        textVenBat = inputUI.qleVenBat()
        textPlace = inputUI.qlePlace()
        self.qleValues.append(textMatNum)
        self.qleValues.append(textVenBat)
        self.qleValues.append(textPlace)

        self.conn = connectionAEU.TakeDataSql.Save(self.qleValues)"""


class SearchUI(QWidget):
    def __init__(self, parent=None):
        super(SearchUI, self).__init__(parent)

        layout = QHBoxLayout()
        pixmap = QPixmap("D:\LearnPython\AEU\impg7.jpg")
        self.lblSearch = QLabel(self)
        self.lblSearch.setPixmap(pixmap)
        self.lblSearch.show()

        self.lblSearch = QLabel(self)
        self.lblSearch.setPixmap(pixmap)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QuitButton</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(330, 170)
        # self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))
        self.setGeometry(100, 100, 400, 200)
        self.SearchLable()
        self.setLayout(layout)

    def SearchLable(self):
        # Here lable for input data
        self.lblSMatNum = QLabel(self)
        self.lblSVenBat = QLabel(self)
        self.lblSPlace = QLabel(self)

        self.lblSMatNum.setText('MatNum >')
        self.lblSMatNum.setFont(QFont("Arial", 12))
        self.lblSVenBat.setText('VenBat >')
        self.lblSVenBat.setFont(QFont("Arial", 12))
        self.lblSPlace.setText('Place>')
        self.lblSPlace.setFont(QFont("Arial", 12))

        self.qleSMatNum = QLineEdit(self)
        self.qleSMatNum.setValidator(QIntValidator())
        self.qleSMatNum.setMaxLength(8)
        # self.qleMatNum.move(215, 305)
        self.qleSMatNum.setFocus()
        #self.qleSMatNum.returnPressed.connect(self.changeFocustoVen)

        self.qleSVenBat = QLineEdit(self)
        self.qleSVenBat.setValidator(QIntValidator())
        self.qleSVenBat.setMaxLength(10)
        #self.qleSVenBat.returnPressed.connect(self.changeFocustoPlasce)

        self.qleSPlace = QLineEdit(self)
        self.qleSPlace.setInputMask('w9e-99-99')
        self.qleSPlace.setFont(QFont("Arial", 14))
        #self.qleSPlace.returnPressed.connect(self.MsSqlValidator)



        self.qleSMatNum.move(165, 35)
        self.qleSVenBat.move(165, 75)
        self.qleSPlace.move(165, 125)

        self.lblSMatNum.move(95, 35)
        self.lblSVenBat.move(100, 75)
        self.lblSPlace.move(115, 125)
        self.setGeometry(100, 100, 400, 200)

    def changeSFocustoVen(self):

        self.qleSVenBat.setFocus()

    def changeSFocustoPlasce(self):

        self.qleSPlace.setFocus()

    def changeSFocusBtn(self):

        self.btnOk.setFocus()

if __name__ == '__main__':
    app = QApplication([])
    window = WarehouseMain()
    window.show()
    app.exec()


