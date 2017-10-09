import pyodbc
import inputGUIsql

class TakeDataSql ():
    """This class TakeDataSql working with data on sql, for warehaouse"""


    def __init__(self):
        """ This function for connection to db aeu on server UACVDB01\SQL2008EXPRESS"""
        self.connectionAeu = pyodbc.connect('Driver={SQL Server};'
                                       'Server=UACVDB01\SQL2008EXPRESS;'
                                       'Database=aeu;'
                                       'uid=sa;pwd=Prettl!@#4')
        self.cursor = self.connectionAeu.cursor()


    def inputAeuSql(self, ValueInterf):
        """ This funtion for input data to table CableWarehouse """

        readconn = self.connectionAeu
        cursor = self.cursor
        insertSQLcommand = ("INSERT INTO CableWarehouse "
                                              "(MaterialNumber, VendorBatch, PlaceNumber)"
                                              "VALUES (?,?,?)")

        #valueMatNum = self.d
        #valueVenBat = self.valueVenBat
        #valuePlace = self.valuePlace
        Values = ValueInterf
        cursor.execute(insertSQLcommand, Values)
        readconn.commit()
        readconn.close()


    def readAeuSql(self):
        """ This funtion for reading data from table CableWarehouse"""
        pass





