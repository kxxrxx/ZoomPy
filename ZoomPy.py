# This script automatically opens the Zoom app, joins the specified meeting, and records it.

import pyautogui as pag
import time

# Joining Zoom Meeting:

# update meeting info
meeting_id = '734757637'
# meeting_pw = '230931'
# adjust how long the recording to be in minutes (max 120 minutes)
meeting_dur = 50
# screen recording are sent to This PC -> Videos

# esc clicked to ensure that the win key will open up correctly in the next step
pag.press('esc', interval=0.1)

time.sleep(0.2)

# simulates pressing the windows key, searching 'zoom, and opening the app
pag.press('win', interval=0.1)
pag.write('zoom')
pag.press('enter', interval=0.5)


# time buffer while Zoom loads
time.sleep(10)


# simulates clicking join meeting
x,y = pag.locateCenterOnScreen('join.png')
pag.click(x,y)

# simulates entering the meeting info (ID and password)
pag.press('enter', interval=1)
# the interval of 1 second is important, if not there, then the meeting id will not be inputted
pag.write(meeting_id)
pag.press('enter', interval=1)

# comment out if there's no password
#time.sleep(3)
#pag.press('enter', interval=1)
#pag.write(meeting_pw)
#pag.press('enter', interval=1)


# Recording meeting using Windows Game Bar:

# time delay while meeting is loading

time.sleep(5)

# opens Windows Game Bar
pag.hotkey('win', 'g')
time.sleep(1)
# begins screen recording
pag.hotkey('win', 'alt', 'r')
time.sleep(1)
# closes Windows game bar
pag.hotkey('win', 'g')

# records time amount in seconds
time.sleep(meeting_dur * 60)

# ends screen recording
pag.hotkey('win', 'alt', 'r')
time.sleep(2)

# closes Zoom
pag.hotkey('alt', 'f4')
time.sleep(0.5)
pag.hotkey('alt', 'f4')