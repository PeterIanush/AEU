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
        #Values = ValueInterf
        cursor.execute(insertSQLcommand, ValueInterf)
        readconn.commit()
        readconn.close()


    def readAeuSql(self, login):
        """ This funtion for reading data from table CableWarehouse"""

        readconn = self.connectionAeu
        cursor = self.cursor
        selectSQLcommand = ("SELECT * FROM LoginPassWareH WHERE (Login = 'login'), Password")

        try:
            # Execute the SQL command
            cursor.execute(selectSQLcommand)
            results = cursor.fetchall()
            for row in results:
                self.logName = row[0]
                self.pasName = row[1]
            print("logName=%s, pasName=%s" % (self.logName, self.pasName))
        except:
            print("Incorect password")

        readconn.close()







