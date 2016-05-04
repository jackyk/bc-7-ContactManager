import sqlite3

class ContactStorage:

    def __init__(self):

        self.db_1 = sqlite3.connect("test1.db")
        self.db_1 = db_1.execute('''CREATE TABLE USERS(ID INT PRIMARY KEY AUTO INCREMENT,NAME TEXT NOT NULL,PHONENUMBER INT NOT NULL)''')
        self.cursor = db_1.cursor

    def user_input(self,name, phonenumber):
        db1_execute("INSERT INTO USERS(NAME,PHONENUMBER) VALUES('%s',%s)" % (name, phonenumber))

        
