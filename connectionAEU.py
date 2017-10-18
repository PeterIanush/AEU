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

        cursor.execute(insertSQLcommand, ValueInterf)
        readconn.commit()
        readconn.close()


    def readAeuSql(self, login):
        """ This funtion for reading data from table CableWarehouse"""

        readconn = self.connectionAeu
        cursor = self.cursor
        selectSQLcommand = ("SELECT Login,Password FROM LoginPassWareH WHERE Login='%s'" % login)
        print(selectSQLcommand)
        cursor.execute(selectSQLcommand)
        results = cursor.fetchall()
        if results != None:
            for row in results:
                self.logName = row[0]
                self.pasName = row[1]

                print("logName=%s, pasName=%s" % (self.logName, self.pasName))
        else:
            print("Incorect password")


        readconn.close()

    def verifySql(self, valueVerifySql):

        readconn = self.connectionAeu
        cursor =self.cursor
        selectVerifySql = ("SELECT [MaterialNumber], [VendorBatch], [PlaceNumber] \
                              FROM [aeu].[dbo].[CableWarehouse] WHERE [MaterialNumber] = '%s'" % valueVerifySql)
        cursor.execute(selectVerifySql)
        print(cursor.execute(selectVerifySql))
        results = cursor.fetchall()
        for raw in results:
            self.matNum = raw[0]
            self.vendBunch = raw[1]
            self.place = raw[2]
            print("Material Number - > %s, Vendor Bunch - > %s, Place - > %s" % (self.matNum, self.vendBunch, self.place))
        readconn.close()







