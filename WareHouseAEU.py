"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
--------------------------PROGRAM--FOR--TEMPORARY--WAREHOUSE--ON--AEU----------------------
1. This program can add data to DB CableWarehouse on cellular warehouse for production
    What class we using for this task?
    -WarehouseMain -> LoginWidget -> MainButton -> inputUI
2. This program have secure module for work with different premission with data
    What class we using for this task?
    - WarehouseMain -> LoginWidget -> MainButton
3. This program can search find  a tube with a coil of cable along the SAP number and if You
take this coil, program clear data about this coil from DB
    What class we using for this task?
    - WarehouseMain -> LoginWidget -> MainButton -> SearchLable
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
import connectionAEU

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QDesktopWidget,
                             QStackedWidget,qApp, QLabel, QLineEdit,
                             QHBoxLayout,QVBoxLayout)


from PyQt5.QtGui import QIcon, QFont, QPixmap, QIntValidator
from PyQt5.QtCore import QCoreApplication
from PyQt5.Qt import QMainWindow


class WarehouseMain(QMainWindow):

    """----- Create Main Wondow and using QStackedWidget -----"""
    def __init__(self, parent=None):
        super(WarehouseMain, self).__init__(parent)
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        self.loginWidget = LoginWidget(self)
        self.loginWidget.button.clicked.connect(self.UIinit)
        self.setWindowIcon(QIcon('.\images\scanner.png'))
        self.centralWidget.addWidget(self.loginWidget)
        self.setGeometry(300, 300, 848, 280)
        self.show()

    def UIinit(self):
        """----- Initializate Main Button widget -----"""
        self.mainbtn = MainButton(self)
        self.centralWidget.addWidget(self.mainbtn)
        self.centralWidget.setCurrentWidget(self.mainbtn)

        self.mainbtn.btnInitUI.clicked.connect(self.UIinput)
        self.mainbtn.btnSearchUI.clicked.connect(self.UIsearch)

        self.logi = self.loginWidget.login.text()
        self.pas = self.loginWidget.password.text()


    def UIinput(self):
        """----- Initializate Input Window widget -----"""
        self.inpbtn = inputUI(self)
        self.centralWidget.addWidget(self.inpbtn)
        self.centralWidget.setCurrentWidget(self.inpbtn)
        self.inpbtn.qleMatNum.setFocus()
        self.inpbtn.bbtn.clicked.connect(self.UIinit)


    def UIsearch(self):
        """----- Initializate Search Window widget -----"""
        self.searchbtn = SearchUI(self)
        self.centralWidget.addWidget(self.searchbtn)
        self.centralWidget.setCurrentWidget(self.searchbtn)
        self.searchbtn.qleSMatNum.setFocus()
        self.searchbtn.sbbtn.clicked.connect(self.UIinit)

class MainButton(QWidget):
    """----- This class create UI for select input or search UI -----"""
    def __init__(self, parent=None):

        """----- Create main layout with 2 buttons for select -----"""
        super(MainButton, self).__init__(parent)
        layout = QVBoxLayout()

        self.btnInitUI = QPushButton('INPUT TO DB WAREHOUSE')
        self.btnInitUI.setToolTip('Ця кнопка <b>кнопка для вводу даних в БД тимчасового складу виробництва</b>')

        self.btnSearchUI = QPushButton('SEARCH PLACE')
        self.btnSearchUI.setToolTip('Ця кнопка<b>для пошуку матеріалів на тимачовому складі виробництва</b>')

        layout.addWidget(self.btnInitUI)
        layout.addWidget(self.btnSearchUI)

        self.btnInitUI.setFont(QFont("Arial", 14))
        self.btnSearchUI.setFont(QFont("Arial", 14))

        # Create label with background picture
        pixmap = QPixmap(".\images\impg7.png")
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()

        #hide button for cheking premission
        self.btnSearchUI.hide()
        self.btnInitUI.hide()
        self.validPrem()
        self.setGeometry(10, 10, 400, 200)
        self.setLayout(layout)

    def validPrem(self):
        """----- This fu8nction for validate Login premission to program interfice -----"""
        permSearch = 'WHT-Search'
        permInput = 'WHT-Input'
        permAll = 'all'
        if qApp.groupPerm == permSearch:
            self.btnInitUI.show()
        elif qApp.groupPerm == permInput:
            self.btnSearchUI.show()
        elif qApp.groupPerm == permAll:
            self.btnSearchUI.show()
            self.btnInitUI.show()
        else:
            print('You loser')

class LoginWidget(QWidget):
    """----- This class create UI for login widget and here verifying login data -----"""
    def __init__(self, parent=None):

        # Create layout for from Logining
        super(LoginWidget, self).__init__(parent)
        layout = QVBoxLayout()

        # Lable for login
        logLay = QLabel()
        logLay.setFont(QFont("Arial Black", 14))
        logLay.setText("<font color='red'>Login - ></font>")

        # LableEdit edit for login
        self.login = QLineEdit()
        self.login.setFocus()
        self.login.returnPressed.connect(self.returnPrEntLog)

        # Lable for password
        pasLay = QLabel()
        pasLay.setFont(QFont("Arial Black", 14))
        pasLay.setText("<font color='red'>Password - ></font>")

        # LableEdit for password
        self.password = QLineEdit()
        self.password.returnPressed.connect(self.returnPrEntPass)

        #Lable edit for password with hint method
        self.password.setEchoMode(QLineEdit.Password)

        # Convert to text input data
        self.textLogin = self.login.text()
        self.textPassword = self.password.text()

        # Create layout for error UI
        self.connLog = QLabel()
        self.connLog.setFont(QFont("Arial Black", 8))
        self.connLog.setText("<font color='blue'>--------- INPUT YOUR LOGIN AND PASSWORD ----</font>")
        self.connLog.show()

        #Create lable with picture but need chek some problem
        pixmap = QPixmap("D:\LearnPython\AEU\password.pgn")
        pixmap.devicePixelRatio()
        self.lblLogining = QLabel(self)
        self.lblLogining.setPixmap(pixmap)
        self.lblLogining.show()

        # Create button LOGIN
        self.button = QPushButton("NEXT")
        self.button.hide()
        self.button.setFont(QFont("Arial", 14))
        self.button.setToolTip('Ця кнопка <b>для входу в с систему тимчасового складу</b>')

        # Create background picture lable
        pixmap = QPixmap(".\images\impg7.png")
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()

        # Add widget to layout
        layout.addWidget(logLay)
        layout.addWidget(self.login)
        layout.addWidget(pasLay)
        layout.addWidget(self.password)
        layout.addWidget(self.button)
        layout.addWidget(self.lblLogining)
        layout.addWidget(self.connLog)

        self.center()
        self.setGeometry(10, 10, 400, 200)
        self.setLayout(layout)

    def validAccess(self):
        """----- This function for validate input Login and Password here using methon from connectionAEU.SelectPassword -----"""

        # Convert to text input data
        logText = self.login.text()
        pasText = self.password.text()

        # connectionAEU.SelectPassword
        qApp.con = connectionAEU.TakeDataSql(logText, pasText)

        # connectionAEU.SelectPassword.st
        st = qApp.con.st

        # Checking input login and password with DB LoginPassWareH
        if st == 0:
            self.connLog.setText("<font color='green'>------- CONNECTED ------</font>")
            qApp.con.SelectPassword(logText)
            rowLogin = qApp.con.Pasresults
            for raw in rowLogin:
                self.logName = raw[1]
                self.pasName = raw[2]
                qApp.groupPerm = raw[4]

            if self.logName == logText:
                self.button.show()
                self.button.setFocus()
            else:
                self.login.setFocus()

        else:
            self.connLog.setText("<font color='red'>------ INCORECT YOUR LOGIN OR PASSWORD -----</font>")
            self.login.clear()
            self.password.clear()
            self.login.setFocus()


    def returnPrEntLog(self):
        """----- Change focus cursor to password LableEdit -----"""
        self.password.setFocus()


    def returnPrEntPass(self):
        """----- Call function for validate login and password  -----"""
        self.validAccess()


    def center(self):
        """----- Set window to center display -----"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class inputUI(QWidget):
    #This class work with input data to DB WareHouse
    def __init__(self, parent=None):
        super(inputUI, self).__init__(parent)
        layout = QHBoxLayout()
        pixmap = QPixmap(".\images\impg7.png")
        # Background for input layout
        self.lblInput = QLabel(self)
        self.lblInput.setPixmap(pixmap)
        self.lblInput.show()
        # Button for close apllication
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('Ця кнопка <b>ЗАВЕРШИТЬ РОБОТУ ПРОГРАМИ</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(700, 240)
        # Button for back to previous menu
        self.bbtn = QPushButton('BACK', self)
        self.bbtn.setToolTip('Ця кнопка<b> поверне вас в попереднє меню</b>')
        self.bbtn.resize(self.bbtn.sizeHint())
        self.bbtn.move(10, 240)

        self.setGeometry(400, 400, 600, 400)
        self.inputLable()
        self.setLayout(layout)

    def inputLable(self):
        """----- Here  create lable for input data UI-----"""

        # Create lable for description
        self.lblMatNum = QLabel(self)
        #self.lblident = QLabel(self)
        self.lblVenBat = QLabel(self)
        self.lblPlace = QLabel(self)

        # Text and text options for labels
        self.lblMatNum.setText("<font color='red'>Mat. Number-></font>")
        #self.lblident.setText("<font color='red'>Identificator--></font>")
        self.lblVenBat.setText("<font color='red'>Batch-------------></font>")
        self.lblPlace.setText("<font color='red'>Place-------------></font>")

        # Fonts for labels
        self.lblMatNum.setFont(QFont("Arial Black", 18))
        #self.lblident.setFont(QFont("Arial Black", 18))
        self.lblVenBat.setFont(QFont("Arial Black", 18))
        self.lblPlace.setFont(QFont("Arial Black", 18))

        # Size properties description labels
        self.lblMatNum.resize(300, 45)
        #self.lblident.resize(300, 45)
        self.lblVenBat.resize(300, 45)
        self.lblPlace.resize(300, 45)

        # Label Edit for material with parameters
        self.qleMatNum = QLineEdit(self)
        self.qleMatNum.setValidator(QIntValidator())
        self.qleMatNum.setMaxLength(8)

        self.qleMatNum.setFocus()
        self.qleMatNum.setToolTip('Сюди<b> проскануйте штрих код матеріалу з SAP бірки (лівий верхній куток!)</b>')
        self.qleMatNum.returnPressed.connect(self.changeFocustoVen)

        # Label Edit for identifitator with parameters
        """self.qleIdent = QLineEdit(self)
        self.qleIdent.setValidator(QIntValidator())
        self.qleIdent.setMaxLength(8)
        self.qleIdent.setFocus()
        self.qleIdent.setToolTip('Сюди <b> проскануйте штрих код ідентифікатор матеріалу з SAP бірки</b>')
        self.qleIdent.returnPressed.connect(self.changeFocustoVen)"""

        # Label Edit for Bath with parameters
        self.qleVenBat = QLineEdit(self)
        self.qleVenBat.setValidator(QIntValidator())
        self.qleVenBat.setMaxLength(10)
        self.qleVenBat.setToolTip('Сюди<b> проскануйте будь ласка шрих код Batch матеріалу з SAP бірки (з права!)</b>')
        self.qleVenBat.returnPressed.connect(self.changeFocustoPlasce)

        # Label Edit for Place with parameters
        self.qlePlace = QLineEdit(self)
        self.qlePlace.setMaxLength(9)
        self.qlePlace.setInputMask('w9e-99-99')
        self.qlePlace.setToolTip('Сюди <b>проскануйте будь ласка шрих код місця на складі який знадить на стелажі</b>')
        self.qlePlace.returnPressed.connect(self.verifyData)

        # Fonts for labels edit
        self.qleMatNum.setFont(QFont("Arial", 28))
        #self.qleIdent.setFont(QFont("Arial", 28))
        self.qleVenBat.setFont(QFont("Arial", 28))
        self.qlePlace.setFont(QFont("Arial", 28))

        # Size properties for label edit
        self.qleMatNum.resize(300, 55)
        self.qlePlace.resize(300, 55)
        #self.qleIdent.resize(300, 55)
        self.qleVenBat.resize(300, 55)

        # Posiotion properties for label edit
        self.qleMatNum.move(300,15)
        #self.qleIdent.move(300, 85)
        self.qleVenBat.move(300, 95)
        self.qlePlace.move(300, 165)

        # Posiotion properties for label desrption
        self.lblMatNum.move(105, 15)
        #self.lblident.move(105, 85)
        self.lblVenBat.move(105, 95)
        self.lblPlace.move(105, 165)

        # Verify lable with properties
        self.lblVerifyVenBat = QLabel(self)
        self.lblVerifyVenBat.setText("<font color='red'>'IN PROCESS'</font>")
        self.lblVerifyVenBat.setFont(QFont("Arial Black", 14))
        self.lblVerifyVenBat.resize(300, 25)
        self.lblVerifyVenBat.move(270, 240)

        self.setGeometry(400, 400, 600, 280)

    def verifyData(self):

        """----- In this function we verify data before add to db warehouse -----"""
        # convert to text string data from input interface for validation with DB
        self.textMatNum = self.qleMatNum.text()
        self.textVenBat = self.qleVenBat.text()
        self.textPlace = self.qlePlace.text()
        self.textIdent = '90909090'#self.qleIdent.text()

        #call fontion from connectionAEU.VerifyMaterial with 2 parametras
        qApp.con.VerifyMaterial(self.textMatNum, self.textVenBat)

        #here validation data
        if qApp.con.results == []:
            self.lblVerifyVenBat.setText("<font color='green'>*Correct data save to db*</font>")
            self.MsSqlWriter()
        else:
            self.lblVerifyVenBat.setText("<font color='red'>Incorret data scan another BC!!!</font>")
            self.qleMatNum.clear()
            #self.qleIdent.clear()
            self.qleVenBat.clear()
            self.qlePlace.clear()
            self.qleMatNum.setFocus()

    def MsSqlWriter(self):
        # This class work with data from UI and input to DB Warehouse
        #Take login what we used for connect to DB
        login = qApp.con.logi

        #Create list for write to DB
        status = 'wait'
        descript = login
        self.qleValues = []
        self.qleValues.append(self.textMatNum)
        self.qleValues.append(self.textIdent)
        self.qleValues.append(self.textVenBat)
        self.qleValues.append(self.textPlace)
        self.qleValues.append(status)
        self.qleValues.append(descript)

        #method for verify data
        if len(self.qleValues) != []:
            self.qleMatNum.clear()
            #self.qleIdent.clear()
            self.qleVenBat.clear()
            self.qlePlace.clear()
            self.qleMatNum.setFocus()
            qApp.con.Save(self.qleValues)
        else:
            print('incorect data')

    """def changeFocustoIdent(self):
        # set cursor to identificator label
        self.qleIdent.setFocus()"""

    def changeFocustoVen(self):
        # set cursor to identificator label
        self.qleVenBat.setFocus()

    def changeFocustoPlasce(self):
        # set cursor to Place label
        self.qlePlace.setFocus()

    def changeFocusBtn(self):
        # set cursor to button ok label
        self.btnOk.setFocus()

class SearchUI(QWidget):
    """----- This class create UI for search material and method for work with this data -----"""
    def __init__(self, parent=None):
        super(SearchUI, self).__init__(parent)
        #create layout for search UI
        layout = QHBoxLayout()

        #Label for background
        pixmap = QPixmap(".\images\impg7.png")
        self.lblSearch = QLabel(self)
        self.lblSearch.setPixmap(pixmap)
        self.lblSearch.show()

        #Quit button for close program
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('Ця кнопка <b>ДЛЯ ЗАВЕРШЕННЯ ПРОГРАМИ</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(765, 240)

        #Back button for back to previous menu
        self.sbbtn = QPushButton('BACK', self)
        self.sbbtn.setToolTip('Ця кнопка <b>для повернення до попереднього меню</b>')
        self.sbbtn.resize(self.sbbtn.sizeHint())
        self.sbbtn.move(10, 240)

        self.setGeometry(400, 400, 600, 280)
        self.SearchLable()
        self.setLayout(layout)

    def SearchLable(self):
        """----- Here lable for input data -----"""

        #labels desctription
        self.lblSMatNum = QLabel(self)
        #self.lblSIdent = QLabel(self)
        self.lblSVenBat = QLabel(self)
        self.lblSPlace = QLabel(self)

        #information labels about status material in DB
        self.lblDeleteSmNum = QLabel(self)
        #self.lblDeleteSident = QLabel(self)
        self.lblDeleteSvBatch = QLabel(self)
        self.lblDeleteSpl = QLabel(self)
        self.lblDeleteSdescription = QLabel(self)

        #Fonts color and text for descrption labels
        self.lblSMatNum.setText("<font color='red'>S_Mat. Number></font>")
        #self.lblSIdent.setText("<font color='red'>S_Identificator-></font>")
        self.lblSVenBat.setText("<font color='red'>S_Batch------------></font>")
        self.lblSPlace.setText("<font color='red'>S_Place------------></font>")

        #Fonts for descrption labels
        self.lblSPlace.setFont(QFont("Arial Black", 16))
        self.lblSVenBat.setFont(QFont("Arial Black", 16))
        #self.lblSIdent.setFont(QFont("Arial Black", 16))
        self.lblSMatNum.setFont(QFont("Arial Black", 16))

        #size description labels
        self.lblSMatNum.resize(300, 55)
        #self.lblSIdent.resize(300, 55)
        self.lblSVenBat.resize(300, 55)
        self.lblSPlace.resize(300, 55)

        #Font color and text for status label
        self.lblDeleteSmNum.setText("<font color='orange'> in process></font>")
        #self.lblDeleteSident.setText("<font color='orange'> in process></font>")
        self.lblDeleteSvBatch.setText("<font color='orange'> in process></font>")
        self.lblDeleteSpl.setText("<font color='orange'> in process></font>")
        self.lblDeleteSdescription.setText("<font color='orange'>responsible></font>")

        #Font for status label
        self.lblDeleteSmNum.setFont(QFont("Arial Black", 12))
        #self.lblDeleteSident.setFont(QFont("Arial Black", 12))
        self.lblDeleteSvBatch.setFont(QFont("Arial Black", 12))
        self.lblDeleteSpl.setFont(QFont("Arial Black", 12))
        self.lblDeleteSdescription.setFont(QFont("Arial Black", 12))

        #size for status label
        self.lblDeleteSmNum.resize(200, 55)
        #self.lblDeleteSident.resize(200, 55)
        self.lblDeleteSvBatch.resize(200, 55)
        self.lblDeleteSpl.resize(200, 55)
        self.lblDeleteSdescription.resize(200, 55)

        #Label edit for Material number with properties
        self.qleSMatNum = QLineEdit(self)
        self.qleSMatNum.setValidator(QIntValidator())
        self.qleSMatNum.setMaxLength(8)
        self.qleSMatNum.setFocus()
        self.qleSMatNum.returnPressed.connect(self.changeSFocustoVen)
        self.qleSMatNum.returnPressed.connect(self.verifyDataSql)

        # Label edit for Identificator with properties
        """self.qleSIdent = QLineEdit(self)
        self.qleSIdent.setValidator(QIntValidator())
        self.qleSIdent.setMaxLength(8)
        self.qleSIdent.setFocus()
        self.qleSIdent.returnPressed.connect(self.changeSFocustoVen)
        self.qleSIdent.returnPressed.connect(self.aprSidentificator)"""

        # Label edit for Batch number with properties
        self.qleSVenBat = QLineEdit(self)
        self.qleSVenBat.setValidator(QIntValidator())
        self.qleSVenBat.setMaxLength(10)
        self.qleSVenBat.returnPressed.connect(self.changeSFocustoPlasce)
        self.qleSVenBat.returnPressed.connect(self.aprSvBatch)

        # Label edit for Place with properties
        self.qleSPlace = QLineEdit(self)
        self.qleSPlace.setMaxLength(9)
        self.qleSPlace.setInputMask('w9e-99-99')
        self.qleSPlace.returnPressed.connect(self.aprSpl)

        #Tooltip for label edit
        self.qleSVenBat.setToolTip('Сюди <b>потрібно занести просканувавши штрих код SAP Batch номеру матеріалу і якщо маркер з ліва зелений ви просканували коректні дані</b>')
        #self.qleSIdent.setToolTip('Сюди <b>потрібно занести просканувавши штрих код ідентифікатора і якщо маркер з ліва зелений ви просканували коректні дані</b>')
        self.qleSMatNum.setToolTip('Сюди <b>потрібно занести просканувавши шрих код SAP номеру матеріала і якщо маркер з ліва зелений ви просканували коректні дані</b>')
        self.qleSPlace.setToolTip('Сюди <b>потрібнозанести просканувавши штрих код складо-місця і якщо маркер з ліва зелений ви просканували коректні дані</b>')

        #Font for label edit
        self.qleSMatNum.setFont(QFont("Arial", 22))
        #self.qleSIdent.setFont(QFont("Arial", 22))
        self.qleSVenBat.setFont(QFont("Arial", 22))
        self.qleSPlace.setFont(QFont("Arial", 22))

        #position for label edit(pixel)
        self.qleSMatNum.move(270, 15)
        #self.qleSIdent.move(270, 85)
        self.qleSVenBat.move(270, 95)
        self.qleSPlace.move(270, 165)

        #size for label edit
        self.qleSMatNum.resize(300, 55)
        self.qleSVenBat.resize(300, 55)
        #self.qleSIdent.resize(300, 55)
        self.qleSPlace.resize(300, 55)

        #position label description
        self.lblSMatNum.move(85, 15)
        #self.lblSIdent.move(85, 85)
        self.lblSVenBat.move(85, 95)
        self.lblSPlace.move(85, 165)

        #position status label
        self.lblDeleteSmNum.move(570, 15)
        #self.lblDeleteSident.move(570, 85)
        self.lblDeleteSvBatch.move(570, 95)
        self.lblDeleteSpl.move(570, 165)
        self.lblDeleteSdescription.move(570, 240)

        #proces informer
        self.aprlbl = QLabel()
        self.aprlbl.setFont(QFont("Arial", 12))
        self.aprlbl.resize(300, 45)
        self.aprlbl.move(270, 240)

        self.setGeometry(400, 400, 600, 280)

    def verifyDataSql(self):
        """----- This class for verify data exists searched material on DB -----"""
        #convert to string material number
        findMat = self.qleSMatNum.text()

        #call method Search material from connectionAEU.SearchMat with parameters
        qApp.con.SearchMat(findMat)

        #create object with searching results
        sMat = qApp.con.resultsSearch

        #method checking if current material data and change font color and set text to atatus label
        if sMat != []:
            delList = qApp.con.resultsSearch
            for raw in delList:
                self.Sid = raw[0]
                self.SmNum = raw[1]
                #self.Sident = raw[2]
                self.SvBatch = raw[3]
                self.Spl = raw[4]
                self.Sdescription = raw[7]
            self.lblDeleteSmNum.setText("<font color='green'> in process>%s</font>" % self.SmNum)
            #self.lblDeleteSident.setText("<font color='orange'> in process>%s</font>" % self.Sident)
            self.lblDeleteSvBatch.setText("<font color='orange'> in process>%s</font>" % self.SvBatch)
            self.lblDeleteSpl.setText("<font color='orange'> in process>%s</font>" % self.Spl)
            self.lblDeleteSdescription.setText("<font color='orange'>Responsible>%s</font>" % self.Sdescription)
        else:
            self.qleSMatNum.clear()
            self.lblDeleteSmNum.setText("<font color='Blue'>in process>>dont find in DB</font>")
            self.qleSMatNum.setFocus()

    def changeSFocustoVen(self):
        # set cursor to Batch label
        self.qleSVenBat.setFocus()

    def changeSFocustoPlasce(self):
        # set cursor to Place label
        self.qleSPlace.setFocus()

    """def changeSFocustoIdent(self):
        # set cursor to Identificator label
        self.qleSIdent.setFocus()"""

    """def aprSidentificator(self):
        #method for verification of current input data to identificator label edit
        findIdent = self.qleSIdent.text()
        a = int(findIdent)
        b = int(self.Sident)
        if a == b:
            self.lblDeleteSident.setText("<font color='green'> in process>%s</font>" % self.Sident)
            self.qleSVenBat.setFocus()
        else:
            self.qleSIdent.clear()
            self.lblDeleteSident.setText("<font color='red'> in process>%s</font>" % self.Sident)
            self.qleSIdent.setFocus()"""

    def aprSvBatch(self):
        # method for verification of current input data to Batch label edit
        findVB = self.qleSVenBat.text()
        a = int(findVB)
        b = int(self.SvBatch)
        if a == b:
            self.lblDeleteSvBatch.setText("<font color='green'> in process>%s</font>" % self.SvBatch)
            self.qleSPlace.setFocus()
        else:
            self.qleSVenBat.clear()
            self.lblDeleteSvBatch.setText("<font color='red'> in process>%s</font>" % self.SvBatch)
            self.qleSVenBat.setFocus()

    def aprSpl(self):
        # #method for verification of current input data to Place label edit

        findpl = self.qleSPlace.text()
        a = findpl
        b = self.Spl
        if a == b:
            self.lblDeleteSpl.setText("<font color='green'> in process>%s</font>" % self.Spl)
            self.aprlbl.setText("<font color='green'>correct>%s</font>" % self.Spl)
            self.writeToWHDeleted()
            qApp.con.Delete(self.Sid)
            self.qleSMatNum.clear()
            #self.qleSIdent.clear()
            self.qleSVenBat.clear()
            self.qleSPlace.clear()
            self.qleSMatNum.setFocus()
        else:
            self.qleSPlace.clear()
            self.lblDeleteSpl.setText("<font color='red'> in process>%s</font>" % self.Spl)
            self.aprlbl.setText("<font color='red'>incorrect>%s</font>" % self.Spl)
            self.qleSPlace.setFocus()

    def writeToWHDeleted(self):
        #method for write searching data to CabelwarehouseDeleted DB

        valueDel = []
        state = 'deleted'
        Sident = '90909090'
        valueDel.append(self.SmNum)
        valueDel.append(Sident)
        valueDel.append(self.SvBatch)
        valueDel.append(self.Spl)
        valueDel.append(state)
        valueDel.append(qApp.con.logi)
        qApp.con.saveBeforeDelete(valueDel)

if __name__ == '__main__':
    app = QApplication([])
    window = WarehouseMain()
    window.show()
    app.exec()


