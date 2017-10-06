import connectionAEU
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget,
                             QMainWindow, QAction, qApp, QLabel, QLineEdit)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication



class WarehouseInput (QWidget):
    """ Here we are create GUI for input data to sql """

    def __init__(self):
        """Here we initialize GUI objects"""
        super().__init__()

        self.initUI()





    def initUI(self):
        """Here we initialize interface for enter data """
        QToolTip.setFont(QFont('SansSerif', 20))

        self.setToolTip('This is a <b>Input data for warehouse</b> widget')

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QuitButton</b>')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(370, 190)


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
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(160, 50)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

    def onChanged(self,text):

        self.lbl.setText(text)
        self.lbl.adjustSize()






if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = WarehouseInput()
    sys.exit(app.exec_())
