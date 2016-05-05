from contactdb import ContactStore

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
        # return result

        for i in result:
            print str(i[1]), i[2]


        # return contact_list

        # if contact not in contact_list:
        #     contact.append(contact_list)






# new_list = ContactEntry('name' ,'my_number')
# print new_list.add_contact()
