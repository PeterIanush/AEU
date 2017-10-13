import connectionAEU
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget,
                             QStackedWidget, QAction, qApp, QLabel, QLineEdit,
                             QHBoxLayout, QInputDialog, QStackedLayout,
                             QListWidget, QFormLayout)


from PyQt5.QtGui import QIcon, QFont, QPixmap, QIntValidator, QRegExpValidator, QKeyEvent
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot



class WarehouseInput (QWidget):
    """ Here we are create GUI for input data to sql """
    def __init__(self, parent = None):
        """Here we initialize GUI objects"""
        super(WarehouseInput, self).__init__(parent)

        self.loginingStak = QWidget()
        self.inputStak = QWidget()
        self.searchStak = QWidget()

        self.mainLable = QHBoxLayout()
        self.mainLable.addWidget(self.loginingStak)
        self.mainLable.addWidget (self.inputStak)
        self.mainLable.addWidget (self.searchStak)

        self.loginingUI()
        self.inputUI()
        self.searchUI()


        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.loginingStak)
        self.Stack.addWidget(self.inputStak)
        self.Stack.addWidget(self.searchStak)

        hbox = QHBoxLayout(self)
        #hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.setGeometry(450, 450, 450, 220)
        self.setWindowTitle('Temporary Warehouse on Production')
        self.center()
        self.show()

    def loginingUI(self):

        layout = QHBoxLayout()
        layout.addWidget(QLineEdit("FirstName"))
        layout.addWidget(QLineEdit("SecondNAme"))
        #layout.addRow("Password", QLineEdit.setInputMask())
        pixmap = QPixmap("D:\LearnPython\AEU\logining.png")
        pixmap.devicePixelRatio()
        self.lblLogining = QLabel(self)
        self.lblLogining.setPixmap(pixmap)
        self.loginingStak.setLayout(layout)
        self.setWindowTitle('Logining')
        self.btnOk = QPushButton('OK')




    def inputUI(self):
        """Here we initialize interface for enter data """

        #self.setLayout(QFormLayout)
        QToolTip.setFont(QFont('SansSerif', 20))

        self.setToolTip('This is a <b>Input data for warehouse</b> widget')

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
        #self.exitAPP()


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

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()
        self.center()

    def inputLable(self):
        """Here lable for input data"""
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
        #qlePlace.setValidator(QRegExpValidator('W'))
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

    def saveSql(self):

        conn = connectionAEU.TakeDataSql()

        self.qleValues = []

        textMatNum = self.qleMatNum.text()
        textVenBat = self.qleVenBat.text()
        textPlace = self.qlePlace.text()

        print(textMatNum, textVenBat, textPlace)

        self.qleValues.append(textMatNum)
        self.qleValues.append(textVenBat)
        self.qleValues.append(textPlace)

        print(self.qleValues)


        if len(self.qleValues) != 0:
            conn.inputAeuSql(self.qleValues)
            self.qleMatNum.clear()
            self.qleVenBat.clear()
            self.qlePlace.clear()
            self.qleMatNum.setFocus()
        else:
            print('incorect data')

    def searchUI(self):
        pass

    """   hbox = QHBoxLayout(self)
        pixmap = QPixmap("D:\LearnPython\AEU\logining.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)


        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.btn = QPushButton('Search Place', self)
        self.btn.setGeometry(80, 75, 100, 50)
        self.btnInput = QPushButton('Input to DB', self)
        self.btnInput.setGeometry(80, 140, 100, 50)
        self.btn.clicked.connect(self.inputUI)

        self.setGeometry(300, 300, 260, 150)
        self.setWindowTitle('Logining')
        self.show()
        #self.btn.clicked.connect()
        self.center()
        
        """

    def changeFocustoVen(self):

        self.qleVenBat.setFocus()

    def changeFocustoPlasce(self):

        self.qlePlace.setFocus()

    def display(self, i):
        self.Stack.setCurrentIndex(i)

def main():
    app = QApplication(sys.argv)
    ex = WarehouseInput()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

