from contactdb import ContactStore
# from smsApi import SendSms


class ContactEntry:

    def __init__(self, name, my_number):
        self.name = name
        self.my_number = my_number

    def add_contact(self):

        contact_list = {}
        # name = raw_input("Enter your name ")
        # my_number = input("Enter your Phone number ")

        contact_list[self.my_number] = self.name

        connect_db = ContactStore()
        connect_db.contact_add(self.name, self.my_number)

class ContactSearch:

    def __init__(self, name):
        self.name = name

    def search_contact_list(self):

        search_from_db = ContactStore()
        result = search_from_db.contact_search(self.name)

        for i in result:
            print str(i[1]), i[2]

        return result




    # def send_sms():
    #     send_one_way = AfricasTalkingGateway()
    #     send_one_way.sendMessage(self.to_, self.message_)
    #
