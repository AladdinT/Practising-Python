'''
Session 3
Task2:
    1-Write a code to suggest automatically activates for you 
    2-Get your public IP
'''
#################### Write a code to suggest automatically activates for you #################
import requests
from mylib.chrome import openUrl
url = requests.get("http://www.boredapi.com/api/activity")

print(end="\n")
print('Categoty : ' + url.json()['type'])
print('Activity : ' + url.json()['activity'])
if ( str(url.json()['link']) != ""):
    print('Link : ' + url.json()['link'])
    if( str(input("Open Url ? (y/n) :  " )) == "y"):
        openUrl(str(url.json()['link']))

print(end="\n")

##############################################################################################

######################### Get your public IP #################################################

import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Correct IP Address : " + IPAddr )

#Question : API provides a different ip than cmd> ipconfig
#  what's the differnece ?
#  python http server works only with address obtained from ipconfig 

url = requests.get("https://api.ipify.org/?format=json")
print("IP Address : " + str(url.json()['ip']) + " ??" )

##############################################################################################

############################## Host a server #################################################
import os
import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print(type(IPAddr))

openUrl(IPAddr+":8000")
os.system("python -m http.server --directory .")
##############################################################################################
