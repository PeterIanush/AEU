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
            self.connectionAeu.commit()
        except pyodbc.Error:
            print('Try to save')


    def Delete(self, valueInterf):
        """This function delete data from sql"""
        try:
            cursor = self.cursor
            print("List fro delete - >", valueInterf)
            cursor.execute("DELETE FROM CableWarehouse WHERE id = '%s'" % valueInterf)
            self.connectionAeu.commit()
        except pyodbc.Error:
            print('Incorect string')



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
        else:
            print("Incorect password")


    def VerifyMaterial(self, valueMatNum, valueVedorBatch):

        self.valueStatus = False
        print(valueMatNum, valueVedorBatch)
        try:
            cursor =self.cursor
            selectVerifySql = ("SELECT [material], [vendor_batch], [place] \
                                  FROM [aeu].[dbo].[CableWarehouse] WHERE [material] = '%s' AND [vendor_batch] = '%s'" % (valueMatNum, valueVedorBatch))
            cursor.execute(selectVerifySql)
            self.results = cursor.fetchall()

            for raw in self.results:
                self.matNum = raw[0]
                self.vendBunch = raw[1]
                self.place = raw[2]
                print("Material Number- > %s, Vendor Bunch- > %s, Place- > %s" % (self.matNum, self.vendBunch, self.place))

        except pyodbc.Error:
            print('incoret data for verify')

    def SearchMat(self, valMatN):

        try:
            cursor = self.cursor
            selectMat = ("SELECT TOP 1 * FROM CableWarehouse WHERE material = '%s' ORDER BY vendor_batch"% valMatN)
            cursor.execute(selectMat)
            self.resultsSearch = cursor.fetchall()
        except pyodbc.Error:
            print('Incorect DATA Search')








