from AfricasTalkingGateway import  AfricasTalkingGateway, AfricasTalkingGatewayException

# class TestMessage:
def __init__(self, phone_number, msg):
    self.phone_number=  phone_number
    self.msg = msg

def my_message(self):
    username="jackyk"
    apiKey= "695a771b995a729dfc94f5e563b2adeb786ba67c719af9f480f6b756c590a2a4"
    to = self.phone_number
    message = self.msg

    gateway = AfricasTalkingGateway(username,apiKey)


    try:
# Thats it, hit send and we'll take care of the rest.

        results = gateway.sendMessage(to, message)

        for recipient in results:
# status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                recipient['status'],
                                                recipient['messageId'],
                                                recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)



# to_whom=(+254701383210, "Test Monday")
name_1= my_message( +254701383210, "Test Monday")
name_1.results()
#Phill =  TestMessage(+254716636162, "Test Monday Phill")
#print Jackyk.my_message()
# print Phill.my_message()
