import sqlite3

class ContactStore:

    def __init__(self):
        self.db_2 = sqlite3.connect("Test.db")
        self.cursor = self.db_2.cursor()

        self.db_2.execute("CREATE TABLE IF NOT EXISTS Test1(ID INT PRIMARY KEY AUTOINCREMENT, NAME TEXT ,PHONENUMBER TEXT UNIQUE )")

    def contact_add(self, name, my_number):
        '''
        call number function
        '''
        with self.db_2:
        #commmits and closes connecction
            self.db_2.execute("INSERT INTO Test1(NAME ,PHONENUMBER) VALUES('{}', '{}')" .format(name, my_number))


    def contact_search(self, name):
        query = self.db_2.execute("SELECT * from Test1 WHERE NAME LIKE '%{}%'".format(name))
        # print query
        result = [i for i in query]
        query.close()
        return result
        # return query
