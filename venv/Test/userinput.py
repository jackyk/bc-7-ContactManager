from storage import ContactStorage

class ContactList:

    '''
    Create a contact list from users input,
        Confirm how many times it appears
        Store it in ContactStorage

    '''

    def __init__(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def name_number(self,x):
        name=raw_input("Input your name ")
        phonenumber=input("Give out your phone number ")

        searched_name = input()

        my_contacts = {}
        my_contacts[phonenumber]=name

        for phonenumber ,name in my_contacts.iteritems:
            if name == searched_name:
                results = name.append(phonenumber)

        # for i in x.split():
        #     if i.isdigit():
        #         i = int(i)
        #
        # if i in my_contacts:
        #     my_contacts[i] += 1
        #
        # else:
        #     my_contacts[i] = 1

        calldb = ContactStorage()
        calldb.user_input(name,phonenumber)


all_contacts=ContactList('name','phonenumber')
all_contacts.name_number()
print my_contacts
