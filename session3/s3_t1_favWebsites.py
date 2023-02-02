'''
Session 3
Task 1:
    1-Make your module that contain favourite websites and have function 
    called Firefox take url and open website 
    2- then make main file and print menu of sites for user and let him choice
'''

import mylib.chrome as chrome
#from mylib.chrome import printFav, chromeURL

#print all my favourite urls
chrome.printFav()

#get the desired url 
key = str(input('Choose your website : '))

#open url from chrome
chrome.openUrl(chrome.myFavURL[key])
