import sys
from PyQt5.QtCore import *
from PyQt5 import QtGui
from  PyQt5.QtWidgets import *
from PyQt5.Qt import *
class loginGUI(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(300, 300)

        self.addTool()
        self.Centr = QtGui.QWidget()
        self.setCentralWidget(self.Centr)

        self.stack = QtGui.QStackedLayout(self.Centr)  # Создать экземпляр класса QStackedLayout
        self.stack.addWidget(self.addWindowOne())  # добавить компонент в конец контейнера
        self.stack.addWidget(self.addWindowTwo())
        self.currentStack(0)  # делает видимым компонент с указанным индексом

    def addTool(self):
        """ создаём панель инструментов"""

        self.toolbar = self.addToolBar('windows')
        nameAct = ['window 1', 'window 2']
        for index, name in enumerate(nameAct):
            name = QtGui.QAction(name, self)
            self.connect(name, QtCore.SIGNAL('triggered()'), self.switchWindow(index))
            self.toolbar.addAction(name)

    def addWindowOne(self):
        wind = QtGui.QWidget()
        wind.setStyleSheet('background-color: {0};'.format('#A2D9EE'))
        return wind

    def addWindowTwo(self, ):
        wind = QtGui.QWidget()
        wind.setStyleSheet('background-color: {0};'.format('#A2EECE'))
        return wind

    def currentStack(self, current_id):
        self.stack.setCurrentIndex(current_id)

    def switchWindow(self, index):
        def f():
            self.currentStack(index)

        return f

    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())