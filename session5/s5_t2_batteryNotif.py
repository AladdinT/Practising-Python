'''
Session 5
Task 2:
    Notify your battery percentage
'''
from pynotifier import Notification
import psutil

battery = psutil.sensors_battery()
percent = battery.percent
print(percent)
Notification("Your Battery Status ", "Your Battery is " +str(percent) + "% Charged" , duration=10).send()