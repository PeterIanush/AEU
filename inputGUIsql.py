import connectionAEU
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget,
                             QMainWindow, QAction, qApp, QLabel, QLineEdit,
                             QHBoxLayout, QInputDialog)


from PyQt5.QtGui import QIcon, QFont, QPixmap, QIntValidator, QRegExpValidator, QKeyEvent
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot



class WarehouseInput (QWidget):
    """ Here we are create GUI for input data to sql """

    def __init__(self):
        """Here we initialize GUI objects"""
        super().__init__()

        #self.initUI()

        self.initUIUser()







    def initUI(self):
        """Here we initialize interface for enter data """
        QToolTip.setFont(QFont('SansSerif', 20))

        self.setToolTip('This is a <b>Input data for warehouse</b> widget')

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("D:\LearnPython\AEU\Input.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)



        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QuitButton</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(400, 410)


        self.setGeometry(450, 450, 450, 220)
        self.setWindowTitle('Temporary Warehouse on Production')
        self.setWindowIcon(QIcon('D:\LearnPython\AEU\scanner.png'))
        self.center()
        self.inputLable()
        #self.exitAPP()
        self.show()

    def closeEvent(self, event):
        """Here creat messageBox for close """
        reply = QMessageBox.question(self, 'Message',
                                     "Are You sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """Here put program to center monitor after launch """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def exitAPP(self):
        """Here create status bar but we need check """
        exitAction = QAction(QIcon('D:\LearnPython\AEU\exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

    def inputLable(self):
        """Here lable for input data"""

        self.qleValues = []

        self.lblMatNum = QLabel(self)
        self.lblVenBat = QLabel(self)
        self.lblPlace = QLabel(self)

        self.lblMatNum.setText('MatNum >')
        self.lblMatNum.setFont(QFont("Arial", 12))
        self.lblVenBat.setText('VenBat >')
        self.lblVenBat.setFont(QFont("Arial", 12))
        self.lblPlace.setText('Place>')
        self.lblPlace.setFont(QFont("Arial", 11))

        qleMatNum = QLineEdit(self)
        qleMatNum.setValidator(QIntValidator())
        qleMatNum.setMaxLength(9)
        qleMatNum.move(215, 305)
        #ent = qleMatNum.keyPressEvent(QKeyEvent.Enter)
        if qleMatNum.maxLength() == 8:
            qleMatNum.text()
            self.qleValues.append(qleMatNum)
            qleMatNum.setFocus(self.qleVenBat, QKeyEvent.Enter)
        else:
            print('Incorect input', qleMatNum)
        """if qleMatNum.editingFinished(ent):
            self.qleValues.append(qleMatNum)"""


        self.qleVenBat = QLineEdit(self)
        self.qleVenBat.setValidator(QIntValidator())
        self.qleVenBat.setMaxLength(11)
        """if qleVenBat.keyPressEvent(QKeyEvent.Enter):
            qleVenBat.text()
            self.qleValues.append(qleVenBat)"""


        qlePlace = QLineEdit(self)
        #qlePlace.setValidator(QRegExpValidator('W'))
        qlePlace.setMaxLength(10)
        qlePlace.setInputMask('w9e-99-99')
        qlePlace.setFont(QFont("Arial", 14))

        qleMatNum.move(215, 305)
        self.qleVenBat.move(215, 335)
        qlePlace.move(215, 365)

        self.lblMatNum.move(140, 305)
        self.lblVenBat.move(150, 335)
        self.lblPlace.move(170, 365)




        qP = qlePlace.text()
        self.qleValues.append(qlePlace)

        return self.qleValues
        a = WarehouseInput.writeAeuSql()



    def enterPressFocus(event):
        event.focusNextChild()

    def writeAeuSql(self):
        print(self.qleValues)
        conn = connectionAEU.TakeDataSql()
        value = self.qleValues
        conn.inputAeuSql(value)

    def initUIUser(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("D:\LearnPython\AEU\logining.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)


        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.btn = QPushButton('Search Place', self)
        self.btn.setGeometry(80, 75, 100, 50)
        self.btnInput = QPushButton('Input to DB', self)
        self.btnInput.setGeometry(80, 140, 100, 50)
        self.btn.clicked.connect(self.initUI)
        """self.FirstName = QLineEdit(self)
        self.FirstName.move(130, 20)
        self.SecondName = QLineEdit(self)
        self.SecondName.move(130, 45)
        if self.btn.clicked:
            loginF = self.FirstName.text()
            loginL = self.SecondName.text()
            uidSql = str(loginF + '.' + loginL)
            print('uid for sql >', uidSql)
            self.btn.clicked.connect(self.initUI)"""
        self.setGeometry(300, 300, 260, 150)
        self.setWindowTitle('Logining')
        self.show()
        #self.btn.clicked.connect()
        self.center()

    def showDialog(self):

        self.firstName = QInputDialog.getText(self, 'Input login', 'Enter your login')

        if self.firstName:
            login = str(self.firstName)
            print(login)
            #self.FirstName.connect()








if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = WarehouseInput()
    sys.exit(app.exec_())
