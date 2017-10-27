import pyodbc

class TakeDataSql ():
    """This class TakeDataSql working with data in sql, for Cablewarehaouse"""

    def __init__(self, uidSql, passSql):
        """ This function for connection to db aeu on server UACVDB01\SQL2008EXPRESS"""
        self.logi = uidSql
        self.pas = passSql
        self.st = 0
        try:
            self.connectionAeu = pyodbc.connect('Driver={SQL Server};'
                                            'Server=UACVDB01\SQL2008EXPRESS;'
                                            'Database=aeu;'
                                            'uid=%s;pwd=%s' % (uidSql, passSql))
            self.cursor = self.connectionAeu.cursor()
            self.st = 0
        except pyodbc.Error:
            self.st = 1

    def Save(self, ValueInterf):
        """ This funtion for input data to table CableWarehouse """
        try:
            cursor = self.cursor
            cursor.execute("INSERT INTO CableWarehouse(material,identificator,vendor_batch,place,state, description) VALUES(?, ?, ?, ?, ?, ?)", ValueInterf)
            self.connectionAeu.commit()
        except pyodbc.Error:
            print('Try to save')


    def Delete(self, valueInterf):
        """This function delete data from sql"""
        try:
            cursor = self.cursor
            cursor.execute("DELETE FROM CableWarehouse WHERE id = '%s'" % valueInterf)
            self.connectionAeu.commit()
        except pyodbc.Error:
            print('Incorect string')

    def SelectPassword(self, login):
        """------ This funtion for reading data from table CableWarehouse -------"""
        try:

            cursor = self.cursor
            selectSQLcommand = ("SELECT * FROM LoginPassWareH WHERE login='%s'"% login)
            cursor.execute(selectSQLcommand)
            self.Pasresults = cursor.fetchall()
        except pyodbc.Error:
            print('Invalid')

    def VerifyMaterial(self, valueMatNum, valueVedorBatch):
        """----- This function using for verify material before save to DB CableWarehouse-----"""
        self.valueStatus = False
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
        except pyodbc.Error:
            print('incoret data for verify')

    def SearchMat(self, valMatN):
        """----- This function using for search label when verify if current material taken from warehouse -----"""
        try:
            cursor = self.cursor
            selectMat = ("SELECT TOP 1 * FROM CableWarehouse WHERE material = '%s' ORDER BY vendor_batch"% valMatN)
            cursor.execute(selectMat)
            self.resultsSearch = cursor.fetchall()
        except pyodbc.Error:
            print('Incorect DATA Search')

    def saveBeforeDelete(self, ValueDel):
        """----- This function using for save deleted material from DB CableWarehouse to CableWarehouseDeleted-----"""
        try:
            cursor = self.cursor
            cursor.execute("INSERT INTO CableWarehouseDeleted(material,identificator,vendor_batch,place,state,description) VALUES(?, ?, ?, ?, ?, ?)", ValueDel)
            self.connectionAeu.commit()
        except pyodbc.Error:
            print("Can't SAVE")








