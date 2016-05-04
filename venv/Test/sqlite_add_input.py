import sqlite3
conn = sqlite3.connect("trial.db")
print "db created"

conn.execute('''CREATE TABLE CONTACTS(ID INT PRIMARY KEY NOT NULL,NAME  TEXT NOT NULL,PHONENUMBER INT NOT NULL)''' )
#
# conn.execute("INSERT INTO CONTACTS(ID,NAME,PHONENUMBER)\
#                 VALUES(1,'Keem',+254701383210)");
#
# conn.execute("INSERT INTO CONTACTS(ID,NAME,PHONENUMBER)\
#                 VALUES(2,'Million',+254701000000)");
#
# conn.execute("INSERT INTO CONTACTS(ID,NAME,PHONENUMBER) \
#                 VALUES(3,'2Million',+254702000000)");
#
# conn.commit()

print "Table created Successfully"


conn.close()


















































#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    my_file add -n <name> -p <phonenumber>
    my_myfile (-i | --interactive)
    my_my_file (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from add_contact import ContactEntry


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class AddNumbers (cmd.Cmd):
    intro = 'This is my contact list!' \
        + ' (type help for a list of commands.)'
    prompt = '(my_file) '
    file = None

    @docopt_cmd
    def do_add_contact(self,name, my_number):
        print ContactEntry().add_contact(name , my_number)



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    AddNumbers().cmdloop()

print(opt)
