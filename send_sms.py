# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+91XXXXXXXXXX", from_="+1xxxxxxxxxx",
                                     body="Type in the message you want to send!!!")
