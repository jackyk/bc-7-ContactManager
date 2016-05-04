import sqlite3

class ContactStore:

    def __init__(self):
        self.db_1 = sqlite3.connect("contacts.db")
        self.cursor = self.db_1.cursor()

        self.db_1.execute("CREATE TABLE IF NOT EXISTS C_LIST1(ID INT PRIMARY KEY AUTOINCREMENT, NAME TEXT ,PHONENUMBER TEXT)")

    def contact_add(self, name, my_number):
        '''
        call number function
        '''
        with self.db_1:
        #commmits and closes connecction
            self.db_1.execute("INSERT INTO C_LIST1(NAME ,PHONENUMBER) VALUES('%s', '%s')" % (name, my_number))

            # pass
    # def search_contact(self)
