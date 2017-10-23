import pyodbc
import WareHouseAEU


class TakeDataSql():
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
            self.valueDescr = (uidSql + "." + passSql)
            print(self.valueDescr)
        except pyodbc.Error:
            print('Galyak')
            self.status = 2

    def Save(self, ValueInterf):
        """ This funtion for input data to table CableWarehouse """

        print(ValueInterf)

        try:
            cursor = self.cursor
            print("List - >", ValueInterf)
            cursor.execute("INSERT INTO CableWarehouse(material,identificator,vendor_batch,place,state, description) VALUES(?, ?, ?, ?, ?, ?)", ValueInterf)
            self.connectionAeu.commit()
        except pyodbc.Error:

            print('Try to save')
