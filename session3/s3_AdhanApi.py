'''
Session Lab of reading and presenting data from json api url
'''

from datetime import datetime
import requests
import vlc  

url = requests.get("https://api.aladhan.com/v1/timingsByCity?city=Giza&country=Arab%20Rebuplic%20Egypt&method=8")
my_media = vlc.MediaPlayer("D:\EmbeddedLinux\Workspace\session3\mylib\Azan.mp3")  

#Prints Day & Date
timeNow = datetime.now().strftime("%H:%M")
print('\nDate : '+ str(url.json()['data']['date']['gregorian'] ['weekday']['en']) +' '+ url.json()['data']['date']['readable'] )
print("Time : " + str(timeNow) )

#prints Hijri date
print('Hijri : '+url.json()['data']['date']['hijri']['date']) 

#prints prayers timing
print('\n******* Prayers Timing ******')
str_timings = str( url.json()['data']['timings'])[1:-85]
str_timings = str_timings.replace("'","")
str_timings = str_timings.replace(", ","\n")
print(str_timings) 
print('*****************************\n')

while True :
    if(timeNow in str_timings):
        my_media.play()
  

  