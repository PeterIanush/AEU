import pyodbc
import WareHouseAEU


class TakeDataSql ():
    """This class TakeDataSql working with data on sql, for warehaouse"""


    def __init__(self, uidSql, passSql):
        """ This function for connection to db aeu on server UACVDB01\SQL2008EXPRESS"""


        self.logi = uidSql
        self.pas = passSql

        try:
            self.connectionAeu = pyodbc.connect('Driver={SQL Server};'
                                            'Server=UACVDB01\SQL2008EXPRESS;'
                                            'Database=aeu;'
                                            'uid=%s;pwd=%s' % (uidSql, passSql))


            self.cursor = self.connectionAeu.cursor()

            print('OK')
            self.status = 1
            self.valueDescr = (uidSql+"."+passSql)
            print(self.valueDescr)
        except pyodbc.Error:
            print('Galyak')
            self.status = 2





    def Save(self, ValueInterf):
        """ This funtion for input data to table CableWarehouse """
        try:
            cursor = self.cursor
            print("List - >", ValueInterf)
            cursor.execute("INSERT INTO CableWarehouse(material,identificator,vendor_batch,place,state, description) VALUES(?, ?, ?, ?, ?, ?)", ValueInterf)
        except pyodbc.Error:
            print('Try to save')
        self.connectionAeu.commit()



    def SelectPassword(self, login):
        """ This funtion for reading data from table CableWarehouse"""

        #readconn = self.connectionAeu
        cursor = self.cursor

        selectSQLcommand = ("SELECT Login,Password FROM LoginPassWareH WHERE Login='%s'" % login)
        print(selectSQLcommand)
        cursor.execute(selectSQLcommand)
        results = cursor.fetchall()
        if results != None:
            for row in results:
                self.logName = row[0]
                self.pasName = row[1]

                #print("logName=%s, pasName=%s" % (self.logName, self.pasName))
        else:
            print("Incorect password")




    def VerifyMaterial(self, valueVerifySql):

        readconn = self.connectionAeu
        cursor =self.cursor
        selectVerifySql = ("SELECT [material], [vendor_batch], [place] \
                              FROM [aeu].[dbo].[CableWarehouse] WHERE [material] = '%s'" % valueVerifySql)
        cursor.execute(selectVerifySql)
        print(cursor.execute(selectVerifySql))
        results = cursor.fetchall()
        for raw in results:
            self.matNum = raw[0]
            self.vendBunch = raw[1]
            self.place = raw[2]
            print("Material Number- > %s, Vendor Bunch- > %s, Place- > %s" % (self.matNum, self.vendBunch, self.place))








