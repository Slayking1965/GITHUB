from twilio.rest import Client

account = "ACf379516d48782a4504820653c6bab995"
token = "fd5d328d962d0756e517a9c3dba22643"

client = Client(account, token)

message = client.messages.create(to="+918081236235", from_="+12693593195",
                             body="Hello,don't ask who I am if you try to trace this number. I will crack into into your phone and will steal your information and upload in dark web. Beware, you motherfuckers")
#print response back from Twilio
print (message)
