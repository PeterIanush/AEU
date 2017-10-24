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
                             QHBoxLayout, QInputDialog, QStackedLayout, QFrame,
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
        self.loginWidget = LoginWidget(self)
        self.loginWidget.button.clicked.connect(self.UIinit)
        self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))
        #stateLable = QLabel("_           __", self)
        #self.stateLable.move(510, 240)

        self.centralWidget.addWidget(self.loginWidget)

        self.setGeometry(300, 300, 848, 280)
        self.show()

    def UIinit(self):
        #Initializate Main Button widget
        self.mainbtn = MainButton(self)
        self.centralWidget.addWidget(self.mainbtn)
        self.centralWidget.setCurrentWidget(self.mainbtn)

        self.mainbtn.btnInitUI.clicked.connect(self.UIinput)
        self.mainbtn.btnSearchUI.clicked.connect(self.UIsearch)

        self.logi = self.loginWidget.login.text()
        print(self.logi)
        self.pas = self.loginWidget.password.text()
        print(self.pas)
        qApp.con = connectionAEU.TakeDataSql(self.logi, self.pas)



    def connectedLWidget(self):

        self.okLable = self.stateLable.setText("connected")

    def erroLWidget(self):

        self.erroLable = self.stateLable.setText("Try Again")


    def UIinput(self):
        self.inpbtn = inputUI(self)

        self.centralWidget.addWidget(self.inpbtn)
        self.centralWidget.setCurrentWidget(self.inpbtn)
        self.inpbtn.qleMatNum.setFocus()
        self.inpbtn.bbtn.clicked.connect(self.UIinit)
        #self.inpbtn.qlePlace.returnPressed.connect(self.dbHelper)


    def UIsearch(self):
        self.searchbtn = SearchUI(self)
        self.centralWidget.addWidget(self.searchbtn)
        self.centralWidget.setCurrentWidget(self.searchbtn)
        self.searchbtn.qleSMatNum.setFocus()
        self.searchbtn.sbbtn.clicked.connect(self.UIinit)



class MainButton(QWidget):
    def __init__(self, parent=None):

        #Creat main layout with 2 buttons for select
        super(MainButton, self).__init__(parent)
        layout = QVBoxLayout()
        #self.centralWidget2 = QStackedWidget()
        self.btnInitUI = QPushButton('INPUT TO DB WAREHOUSE')
        self.btnInitUI.setToolTip('This is a <b>button for input data wires to temporary warehouse</b>')
        self.btnSearchUI = QPushButton('SEARCH PLACE')
        self.btnSearchUI.setToolTip('This is a <b>button for search place wires to temporary warehouse</b>')
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
        logLay = QLabel()
        logLay.setFont(QFont("Arial Black", 14))
        logLay.setText("<font color='red'>Login - ></font>")

        layout.addWidget(logLay)
        self.login = QLineEdit()
        layout.addWidget(self.login)
        self.login.setFocus()
        self.login.returnPressed.connect(self.returnPrEntLog)
        pasLay = QLabel()
        pasLay.setFont(QFont("Arial Black", 14))
        pasLay.setText("<font color='red'>Password - ></font>")
        layout.addWidget(pasLay)
        self.password = QLineEdit()
        layout.addWidget(self.password)
        self.password.returnPressed.connect(self.returnPrEntPass)
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
        self.button.setToolTip('This is a <b>are Logining button to Warehouse system</b>')


        pixmap = QPixmap("D:\LearnPython\AEU\impg7.jpg")
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()

        self.setGeometry(10, 10, 400, 200)
        self.setLayout(layout)

    def validAccess(self):

        self.connLogin = connectionAEU.TakeDataSql.status()
        if self.connLogin.status == 1:
            self.state = QLabel("__   __", self)
            self.state.setFont(QFont("Arial", 20))
            self.state.stateLable.setText("connected")
        else:
            self.state.stateLable.setText("Try Again")

    def returnPrEntLog(self):
        self.password.setFocus()

    def returnPrEntPass(self):
        self.button.setFocus()

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
        qbtn.move(610, 240)

        self.bbtn = QPushButton('BACK', self)
        self.bbtn.setToolTip('This is a <b>button for back to previous menu</b>')
        self.bbtn.resize(self.bbtn.sizeHint())
        self.bbtn.move(10, 240)

        #self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))
        self.setGeometry(300, 300, 600, 400)
        self.inputLable()

        self.setLayout(layout)

    def inputLable(self):
        #Here lable for input data
        self.lblMatNum = QLabel(self)
        self.lblident = QLabel(self)
        self.lblVenBat = QLabel(self)
        self.lblPlace = QLabel(self)

        self.lblMatNum.setText("<font color='red'>Mat. Number-></font>")
        self.lblMatNum.setFont(QFont("Arial Black", 12))
        self.lblMatNum.resize(200, 25)

        self.lblident.setText("<font color='red'>Identificator--></font>")
        self.lblident.setFont(QFont("Arial Black", 12))
        self.lblident.resize(200, 25)

        self.lblVenBat.setText("<font color='red'>Vendor Batch></font>")
        self.lblVenBat.setFont(QFont("Arial Black", 12))
        self.lblVenBat.resize(200, 25)

        self.lblPlace.setText("<font color='red'>Place--------------></font>")
        self.lblPlace.setFont(QFont("Arial Black", 12))
        self.lblPlace.resize(200, 25)


        self.qleMatNum = QLineEdit(self)
        self.qleMatNum.setValidator(QIntValidator())
        self.qleMatNum.setMaxLength(8)
        self.qleMatNum.setFont(QFont("Arial", 14))
        self.qleMatNum.setFocus()
        self.qleMatNum.setToolTip('Here <b>You need scan SAP material from SAP lablel</b>')
        self.qleMatNum.returnPressed.connect(self.changeFocustoIdent)

        self.qleIdent = QLineEdit(self)
        self.qleIdent.setValidator(QIntValidator())
        self.qleIdent.setMaxLength(8)
        self.qleIdent.setFont(QFont("Arial", 14))
        self.qleIdent.setFocus()
        self.qleIdent.setToolTip('Here <b>You need scan identificator material from SAP lablel</b>')
        self.qleIdent.returnPressed.connect(self.changeFocustoVen)

        self.qleVenBat = QLineEdit(self)
        self.qleVenBat.setValidator(QIntValidator())
        self.qleVenBat.setMaxLength(10)
        self.qleVenBat.setFont(QFont("Arial", 14))
        self.qleVenBat.setToolTip('Here <b>You need scan Vendor batch material from SAP lablel</b>')
        self.qleVenBat.returnPressed.connect(self.changeFocustoPlasce)

        self.qlePlace = QLineEdit(self)
        # qlePlace.setValidator(QRegExpValidator('W'))
        self.qlePlace.setMaxLength(9)
        self.qlePlace.setInputMask('w9e-99-99')
        self.qlePlace.setFont(QFont("Arial", 14))
        self.qlePlace.setToolTip('Here <b>You need scan Place material from lablel warehouse place</b>')
        self.qlePlace.returnPressed.connect(self.verifyData)

        self.qleMatNum.move(165,15)
        self.qleIdent.move(165, 45)
        self.qleVenBat.move(165, 75)
        self.qlePlace.move(165, 105)

        self.lblMatNum.move(35, 15)
        self.lblident.move(35, 45)
        self.lblVenBat.move(35, 75)
        self.lblPlace.move(35, 105)

        self.lblVerifyVenBat = QLabel(self)
        self.lblVerifyVenBat.resize(400, 25)
        self.lblVerifyVenBat.move(300, 15)

        self.setGeometry(400, 400, 600, 280)

    def verifyData(self):
        #In this function we verify data before add to db warehouse

        self.lblVerifyVenBat.setText("<font color='red'>'--------'></font>")
        self.lblVerifyVenBat.setFont(QFont("Arial Black", 14))
        self.textMatNum = self.qleMatNum.text()
        self.textVenBat = self.qleVenBat.text()
        self.textPlace = self.qlePlace.text()
        self.textIdent = self.qleIdent.text()
        qApp.con.VerifyMaterial(self.textMatNum, self.textVenBat)
        if qApp.con.results == []:
            print(qApp.con.results)
            self.lblVerifyVenBat.setText("<font color='green'>*Correct data save to db*</font>")
            self.MsSqlWriter()
        else:
            self.lblVerifyVenBat.setText("<font color='red'>Incorret data scan another BC!!!</font>")
            self.qleMatNum.clear()
            self.qleIdent.clear()
            self.qleVenBat.clear()
            self.qlePlace.clear()
            self.qleMatNum.setFocus()

    def MsSqlWriter(self):
        # This class work with data from UI and input to DB Warehouse
        login = qApp.con.logi

        self.qleValues = []
        self.qleValues.append(self.textMatNum)
        self.qleValues.append(self.textIdent)
        self.qleValues.append(self.textVenBat)
        self.qleValues.append(self.textPlace)
        status = 'wait'
        descript = login
        self.qleValues.append(status)
        self.qleValues.append(descript)
        if len(self.qleValues) != []:
            print(self.qleValues)
            self.qleMatNum.clear()
            self.qleIdent.clear()
            self.qleVenBat.clear()
            self.qlePlace.clear()
            self.qleMatNum.setFocus()
            qApp.con.Save(self.qleValues)
        else:
            print('incorect data')

    def changeFocustoIdent(self):

        self.qleIdent.setFocus()

    def changeFocustoVen(self):

        self.qleVenBat.setFocus()

    def changeFocustoPlasce(self):

        self.qlePlace.setFocus()

    def changeFocusBtn(self):

        self.btnOk.setFocus()

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
        qbtn.move(610, 240)

        self.sbbtn = QPushButton('BACK', self)
        self.sbbtn.setToolTip('This is a <b>button for back to previous menu</b>')
        self.sbbtn.resize(self.sbbtn.sizeHint())
        self.sbbtn.move(10, 240)

        # self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))
        self.setGeometry(300, 300, 600, 280)
        print('main serch ok')
        self.SearchLable()
        self.setLayout(layout)

    def SearchLable(self):
        # Here lable for input data
        self.lblSMatNum = QLabel(self)
        self.lblSIdent = QLabel(self)
        self.lblSVenBat = QLabel(self)
        self.lblSPlace = QLabel(self)
        self.lblDeleteSmNum = QLabel(self)
        self.lblDeleteSident = QLabel(self)
        self.lblDeleteSvBatch = QLabel(self)
        self.lblDeleteSpl = QLabel(self)
        self.lblDeleteSdescription = QLabel(self)


        self.lblSMatNum.setText("<font color='red'>SMat. Number-></font>")
        self.lblSMatNum.setFont(QFont("Arial Black", 12))
        self.lblSMatNum.resize(200, 25)
        self.lblSIdent.setText("<font color='red'>SIdentificator--></font>")
        self.lblSIdent.setFont(QFont("Arial Black", 12))
        self.lblSIdent.resize(200, 25)
        self.lblSVenBat.setText("<font color='red'>SVendor Batch></font>")
        self.lblSVenBat.setFont(QFont("Arial Black", 12))
        self.lblSVenBat.resize(200, 25)
        self.lblSPlace.setText("<font color='red'>SPlace--------------></font>")
        self.lblSPlace.setFont(QFont("Arial Black", 12))
        self.lblSPlace.resize(200, 25)
        self.lblDeleteSmNum.setText("<font color='red'>List for delete></font>")
        self.lblDeleteSmNum.setFont(QFont("Arial Black", 12))
        self.lblDeleteSmNum.resize(250, 25)
        self.lblDeleteSident.setText("<font color='red'>List for delete></font>")
        self.lblDeleteSident.setFont(QFont("Arial Black", 12))
        self.lblDeleteSident.resize(250, 25)
        self.lblDeleteSvBatch.setText("<font color='red'>List for delete></font>")
        self.lblDeleteSvBatch.setFont(QFont("Arial Black", 12))
        self.lblDeleteSvBatch.resize(250, 25)
        self.lblDeleteSpl.setText("<font color='red'>List for delete></font>")
        self.lblDeleteSpl.setFont(QFont("Arial Black", 12))
        self.lblDeleteSpl.resize(250, 25)
        self.lblDeleteSdescription.setText("<font color='red'>List for delete></font>")
        self.lblDeleteSdescription.setFont(QFont("Arial Black", 12))
        self.lblDeleteSdescription.resize(250, 25)

        self.qleSMatNum = QLineEdit(self)
        self.qleSMatNum.setValidator(QIntValidator())
        self.qleSMatNum.setMaxLength(8)
        self.qleSMatNum.setFont(QFont("Arial", 14))
        self.qleSMatNum.setFocus()
        self.qleSMatNum.setToolTip('Here <b>You need scan SAP material from SAP lablel</b>')
        self.qleSMatNum.returnPressed.connect(self.changeSFocustoIdent)
        self.qleSMatNum.returnPressed.connect(self.verifyDataSql)

        self.qleSIdent = QLineEdit(self)
        self.qleSIdent.setValidator(QIntValidator())
        self.qleSIdent.setMaxLength(8)
        self.qleSIdent.setFont(QFont("Arial", 14))
        self.qleSIdent.setFocus()
        self.qleSIdent.setToolTip('Here <b>You need scan SIdentificator material from SAP lablel</b>')
        self.qleSIdent.returnPressed.connect(self.changeSFocustoVen)
        self.qleSIdent.returnPressed.connect(self.aprSidentificator)

        self.qleSVenBat = QLineEdit(self)
        self.qleSVenBat.setValidator(QIntValidator())
        self.qleSVenBat.setMaxLength(10)
        self.qleSVenBat.setFont(QFont("Arial", 14))
        self.qleSVenBat.setToolTip('Here <b>You need scan Vendor batch material from SAP lablel</b>')
        self.qleSVenBat.returnPressed.connect(self.changeSFocustoPlasce)
        self.qleSVenBat.returnPressed.connect(self.aprSvBatch)

        self.qleSPlace = QLineEdit(self)
        # qleSPlace.setValidator(QRegExpValidator('W'))
        self.qleSPlace.setMaxLength(9)
        self.qleSPlace.setInputMask('w9e-99-99')
        self.qleSPlace.setFont(QFont("Arial", 14))
        self.qleSPlace.setToolTip('Here <b>You need scan SPlace material from lablel warehouse SPlace</b>')
        self.qleSPlace.returnPressed.connect(self.aprSpl)


        self.qleSMatNum.move(165, 15)
        self.qleSIdent.move(165, 45)
        self.qleSVenBat.move(165, 75)
        self.qleSPlace.move(165, 105)

        self.lblSMatNum.move(35, 15)
        self.lblSIdent.move(35, 45)
        self.lblSVenBat.move(35, 75)
        self.lblSPlace.move(35, 105)
        self.lblDeleteSmNum.move(270, 15)
        self.lblDeleteSident.move(270, 45)
        self.lblDeleteSvBatch.move(270, 75)
        self.lblDeleteSpl.move(270, 105)
        self.lblDeleteSdescription.move(270, 135)

        self.setGeometry(400, 400, 600, 280)

    def verifyDataSql(self):
        #self.valueSearch = []
        findMat = self.qleSMatNum.text()
        #self.valueSearch.append(findMat)
        print('Ok search', findMat)
        qApp.con.SearchMat(findMat)
        print('Ok search')
        delList = qApp.con.resultsSearch
        for raw in delList:
            self.SmNum = raw[1]
            self.Sident = raw[2]
            self.SvBatch = raw[3]
            self.Spl = raw[4]
            self.Sdescription = raw[7]
        self.lblDeleteSmNum.setText("<font color='green'>delete>%s</font>" % self.SmNum)
        self.lblDeleteSident.setText("<font color='red'>delete>%s</font>" % self.Sident)
        self.lblDeleteSvBatch.setText("<font color='red'>delete>%s</font>" % self.SvBatch)
        self.lblDeleteSpl.setText("<font color='red'>delete>%s</font>" % self.Spl)
        self.lblDeleteSdescription.setText("<font color='red'>delete>%s</font>" % self.Sdescription)

    def changeSFocustoVen(self):

        self.qleSVenBat.setFocus()

    def changeSFocustoPlasce(self):

        self.qleSPlace.setFocus()

    def changeSFocustoIdent(self):
        self.qleSIdent.setFocus()

    def aprSidentificator(self):
        findIdent = self.qleSIdent.text()
        a = int(findIdent)
        b = int(self.Sident)
        if a == b:
            self.lblDeleteSident.setText("<font color='green'>delete>%s</font>" % self.Sident)
            self.qleSVenBat.setFocus()
        else:
            self.qleSIdent.clear()
            self.qleSIdent.setFocus()

    def aprSvBatch(self):
        findVB = self.qleSVenBat.text()
        a = int(findVB)
        b = int(self.SvBatch)
        if a == b:
            self.lblDeleteSvBatch.setText("<font color='green'>delete>%s</font>" % self.SvBatch)
            self.qleSPlace.setFocus()
        else:
            self.qleSVenBat.clear()
            self.qleSVenBat.setFocus()

    def aprSpl(self):
        findpl = self.qleSPlace.text()
        a = int(findpl)
        b = int(self.Spl)
        if a == b:
            self.lblDeleteSpl.setText("<font color='green'>delete>%s</font>" % self.Spl)
            self.qleSMatNum.setFocus()
        else:
            self.qleSPlace.clear()
            self.qleSPlace.setFocus()





if __name__ == '__main__':
    app = QApplication([])

    window = WarehouseMain()
    window.show()
    app.exec()


