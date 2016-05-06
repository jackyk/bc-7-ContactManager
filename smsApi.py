from AfricasTalkingGateway import AfricasTalkingGateway
from contacts import ContactSearch


class SendSms:

    username = "jackyk"
    apiKey = "695a771b995a729dfc94f5e563b2adeb786ba67c719af9f480f6b756c590a2a4"


    def __init__(self, to, message):
        self.to = to
        self.message = message

    def send_sms(self):
        name = self.to
        who_to_send = ContactSearch(name)
        contact = who_to_send.search_contact_list()

        # who_to_send.search_contact_list()

        #
        if (len(contact) > 0):
            tosend = AfricasTalkingGateway(SendSms.username, SendSms.apiKey)
            tosend.sendMessage(contact[0][2], self.message)
