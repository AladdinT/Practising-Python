
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


myFavURL = {
    'fb' : 'facbook.com' ,
    'yt' : 'youtube.com' ,
    'insta' : 'instagram.com',
    'udacity' : 'https://classroom.udacity.com/',
    'mySchedule' : 'shorturl.at/deKY0'
}

def openUrl (url):
    webbrowser.get(chrome_path).open(url)

def printFav ():
    for key in myFavURL:
        print(key , end= "   ,  ")
    print(end="\n")
