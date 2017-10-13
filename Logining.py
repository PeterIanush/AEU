import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
from PyQt5.Qt import *
class loginGUI(QWidget):

    def __init__(self, name='', message='', widget=None, parent=None):
        QWidget.__init__(self, parent)

        self.setQbjectName(name)
        self.WindowTitle(name)

        # the dafault label
        self.lbl = QLabel(message)
        self.lbl.setAlignment(Qt.AlignCenter)

        #the stack holding the label and setting page
        self.stak = QStackedWidget()
        self.stak.addWidget(self.lbl)

        #the scroller holding thr stak
        self.scroller =QScrollArea()
        self.scroller.setWidget(self.stak)
        self.scroller.setWidgetResizable(True)

        #add the scroller
        self.setWidget(self.scroller)

        if widget:
            self.placeWidget(widget)