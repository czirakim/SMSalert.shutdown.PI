# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from vault import account,token,from_number,to_number

def sendSMS(message):
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
  account_sid = account
  auth_token = token
  client = Client(account_sid, auth_token)

  message = client.messages \
                .create(
                     body=message,
                     from_=from_number,
                     to=to_number
                 )

  print(message.sid)
