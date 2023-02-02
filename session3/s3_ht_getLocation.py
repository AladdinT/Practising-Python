'''
Session 3
Home Task:
    Get your location 
'''

import requests
url = requests.get("https://api.ipify.org/?format=json")
myIP =  str(url.json()['ip']) 
url = requests.get("https://ipinfo.io/"+ myIP +"/geo")
city = url.json()['city']
region = url.json()['region']
country = url.json()['country']
location = url.json()['loc']

print(f"City :{city} \nRegion :{region},{country} \nLocation :{location}" )
