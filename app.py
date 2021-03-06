"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    contact_manager -n <name> -p <phonenumber> [--timeout=<seconds>]
    contact_manager search <name> [--timeout=<seconds>]
    contact_manager text <name> -m <message> [--timeout=<seconds>]
    contact_manager serial <port> [--baud=<n>] [--timeout=<seconds>]
    contact_manager (-i | --interactive)
    contact_manager (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from contacts import ContactEntry, ContactSearch
from smsApi import SendSms

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

            print("Request not delivered try again!")
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


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(contact_manager) '
    file = None


    def add_contact(self, name, number):
        new_contact = ContactEntry(name,number)
        new_contact.add_contact()

    def search(self, name):
        search_item = ContactSearch(name)
        search_item.search_contact_list()
        

    def sms(self, name, message):
        send_msg = SendSms(name, message)
        send_msg.send_sms()


    @docopt_cmd
    def do_add(self,args):
        """Usage: add -n <name> -p <phonenumber>"""
        # print/ args['<name>'], "number is ", args['<phonenumber>']
        self.add_contact(args['<name>'], args['<phonenumber>'])

    @docopt_cmd
    def do_search(self, args):
        """Usage: search search <name>"""
        self.search(args['<name>'])


    @docopt_cmd
    def do_text(self, args):
        """Usage: text <name> -m <message>..."""

        self.sms(args['<name>'],(" ".join(args['<message>'])))


    def do_quit(self, args):
        """Quits out of Interactive Mode."""

        print('Awesome saving contacts')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
