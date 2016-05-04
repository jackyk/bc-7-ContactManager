#Select user

import sqlite3

conn = sqlite3.connect("userinput.db")
# print "db created"

cursor = conn.execute("SELECT ID, NAME , PHONENUMBER from CONTACTLIST")

for rows in cursor:
    print "NAME =", rows[0]
    print "PHONENUMBER =", rows[1]

conn.close()
# print 'Please work Successfully'











'''
#Delete user
conn = sqlite3.connect('userinput.db')
print "db created"

cursor = conn.execute("UPDATE CONTACTLIST set PHONENUMBER = +25473000000")
conn.commit
print "Total numer of rows updated" ,conn.total_changes
for row in cursor:
    print "NAME ==", row[0]
    print "PHONENUMBER ==", row[1]
'''
