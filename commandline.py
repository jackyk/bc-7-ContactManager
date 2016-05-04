"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    contact_manager -n <name> -p<phonenumber> [--timeout=<seconds>]
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


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(contact_manager) '
    file = None

    @docopt_cmd
    def do_add_contact(self,args):
        """Usage: add_contact -n <name> -p <phonenumber>"""
        # print/ args['<name>'], "number is ", args['<phonenumber>']

        new_contact=ContactEntry(args['<name>'], args['<phonenumber>'])
        new_contact.add_contact()

    def do_quit(self, args):
        """Quits out of Interactive Mode."""

        print('Awesome saving contacts')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
