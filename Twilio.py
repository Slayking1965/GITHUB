Account SID from twilio.com/console
account_sid = "ACf379516d48782a4504820653c6bab995"
# Your Auth Token from twilio.com/console
auth_token  = "fd5d328d962d0756e517a9c3dba22643"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12693593195", 
    from_="+12693593195"from twilio.rest import Client

# Your ,
    body="Hello from Python!")

print(message.sid)