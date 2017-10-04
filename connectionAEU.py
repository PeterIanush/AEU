import pyodbc
import inputSqlGUI

class TakeDataSql ():
    """This class TakeDataSql working with data on sql, for warehaouse"""


    def __init__(self):
        """ This function for connection to db aeu on server UACVDB01\SQL2008EXPRESS"""
        connectionAeu = pyodbc.connect('Driver={SQL Server};'
                                       'Server=UACVDB01\SQL2008EXPRESS;'
                                       'Database=aeu;'
                                       'uid=sa;pwd=Prettl!@#4')
        self.connectionAeu = connectionAeu
        self.cursor = self.connectionAeu.cursor()



    def inputAeuSql(self):
        """ This funtion for input data to table CableWarehouse """
        readconn = self.connectionAeu
        cursor = self.cursor
        insertSQLcommand = ("INSERT INTO CableWarehouse "
                                              "(MaterialNumber, VendorBatch, PlaceNumber)"
                                              "VALUES (?,?,?)")
        valueMatNum = self.valueMatNum
        valueVenBat = self.valueVenBat
        valuePlace = self.valuePlace
        Values = [valueMatNum, valueVenBat, valuePlace]
        cursor.execute(insertSQLcommand, Values)
        readconn.commit()
        readconn.close()


    def readAeuSql(self):
        """ This funtion for reading data from table CableWarehouse"""
        pass





