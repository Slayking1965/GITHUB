import json
import jwt
import pandas
import requests
from datetime import datetime, timedelta, time
from decouple import config, Csv

key = config('key')
secret = config('secret')
payload = {'iss': secret,'exp': datetime.now() + timedelta(hours=2)}
authEmail = config('authEmail')

encoded = jwt.encode(payload, key, algorithm='HS256')

BASE_URL = 'https://api.zoom.us/v2/'
meeting_dashboard = BASE_URL + 'metrics/meetings'
daily = BASE_URL + "report/daily"
endpoint = meeting_dashboard
# endpoint = BASE_URL + 'users/' + userid + '/meetings'

# Last week report
startDate = datetime(year=datetime.today().year, month=datetime.today().month, day=datetime.today().day, hour=0, minute=0, second=1) - timedelta(days=datetime.today().isoweekday() % 7 + 7) # last Monday
endDate = datetime(year=datetime.today().year, month=datetime.today().month, day=datetime.today().day, hour=23, minute=59, second=59) - timedelta(days=datetime.today().isoweekday() % 7) # last Sunday

response = requests.get(endpoint, 
                        {"access_token":encoded, 
                         "type":"past", 
                         'from':startDate, 
                         "to":endDate, 
                         "page_size":300})

report = {'topic':[],'participants':[],'duration':[]}
for meeting in response.json()['meetings']:
    report['topic'].append(meeting['topic'])
    report["participants"].append(meeting['participants'])
    report["duration"].append(meeting['duration'])

# Write to CSV
filename = "ZoomReport_weekOf_"+datetime.strftime(startDate, "%Y-%m-%d")+".csv"
pd.DataFrame(report).to_csv(filename)

# Send email
import email, mimetypes, smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

smtpServer = "smtp.example.com"
port = 587 #STARTTLS
password = config('password')
senderEmail = "sender@example.com"
receiverEmail = ["aaa@bbb.com",]
ccEmail = ['cc@bbb.com',]

subject = filename
body = "Attached is the Zoom report for the period between " + datetime.strftime(startDate, "%Y-%m-%d") + " and " + datetime.strftime(endDate, "%Y-%m-%d")

message = MIMEMultipart()
message["From"] = senderEmail
message["To"] = ",".join(receiverEmail)
message["Cc"] = ",".join(ccEmail)
message["Subject"] = subject

message.attach(MIMEText(body))

ctype, encoding = mimetypes.guess_type(filename)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"
    
maintype, subtype = ctype.split("/",1)

if maintype == "text":
    # print("text")
    fp = open(filename)
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    # print("image")
    fp = open(filename, "rb")
    attachment = MIMEImage(fp.read(), _subtype = subtype)
    fp.close()
elif maintype == "audio":
    # print("audio")
    fp = open(filename, "rb")
    attachment = MIMEAudio(fp.read(), _subtype = subtype)
    fp.close()
else:
    # print("other")
    fp = open(filename, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    
attachment.add_header("Content-Disposition", "attachment", filename=filename)
message.attach(attachment)
text = message.as_string()

context = ssl.create_default_context()
try:
    # Establish connection
    server = smtplib.SMTP(smtpServer, port)
    server.ehlo()
    server.starttls(context=context) # Secure the connection
    server.ehlo()
    server.login(authEmail, password)
    
    # Send email
    server.sendmail(senderEmail, [receiverEmail] + BccEmail, text)
except Exception as e:
    print(e)
finally:
    server.quit()