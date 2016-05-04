from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from storage import user_input
# Specify your login credentials


username = "jackyk"
apikey   = "695a771b995a729dfc94f5e563b2adeb786ba67c719af9f480f6b756c590a2a4"
# Specify the numbers that you want to send to in a comma-separated list
# Please ensure you include the country code (+254 for Kenya)
to = {}
# And of course we want our recipients to know what we really do
message = ""
# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)
# Any gateway errors will be captured by our custom Exception class below,
# so wrap the call in a try-catch block
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
