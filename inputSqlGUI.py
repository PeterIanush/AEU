from tkinter import *
import connectionAEU

class WarehouseInputGUI():
    """ Here we are create GUI for input data to sql """

    def __init__(self):
        """Here we initialize GUI objects"""
        Tk.__init__(self)
        self.initialize()
        self.mainloop()

    def inittialize(self):
        """Here we initialize interface for enter data """
        self.title("Insert Your article")
        self.geometry('500x400+300+200')

    def checkInsert(self):
        """Here we are check corect data"""
        if len(self.valueMatNum.get())==3:
            self.dataList = connectionAEU.TakeDataSql(self.valueMatNum.get())
            print(self.dataList)
            print((self.dataList[0]))
            self.TestField.focus_set()

    def insertCheck(self):
        if self.valueVenBat.get()==self.dataList[0]:
            self.TesLable.config(text='Correct')
        else:
            self.TestLable.config(text='Wrong')

    def createInsert(self):
        """Here we are create objects for enter data"""
        self.valueMatNum = StringVar()
        self.valueMatNum.trace_add("write")

        self.valueVenBat = StringVar()
        self.valueVenBat.trace_add("write")

        self.valuePlace = StringVar()
        self.valuePlace.trace_add("write")

        self.MatNumField = Entry(self, textvariable=self.valueMatNum)
        self.MatNumField.place(x=100,y=100)
        self.MatNumField.focus_set()

        self.TestField = Entry(self,textvariable=self.valueVenBat)
        self.TestField.place(x=100,y=200)

        self.TesLable = Lable(self,text='')
        self.TesLable.place(x=300,y=200)