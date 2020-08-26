# https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python
from twilio.rest import Client

account_sid = "You really think i will acually put the real number here? lol"
auth_token = "You really think i will acually put the real number here? lol"
twilio_number = "You really think i will acually put the real number here? lol"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello World!',
         from_= twilio_number,
         to='You really think i will acually put the real number here? lol'
     )

print(message.sid)