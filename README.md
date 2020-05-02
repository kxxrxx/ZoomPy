# ZoomPy
Python script that automatically opens the Zoom app, joins the specified meeting, and records it.

Module used:
pyautogui - https://pyautogui.readthedocs.io/en/latest/
- Controls the keyboard and mouse

Requirements:
- Windows OS
- Zoom app
- Computer to be awake and signed on

Steps:

1. Include join.png in the same directory as Python file.
   - This tells the script where to click to join the meeting.

2. Update the meeting ID and password as strings under 'Meeting Info' section.
   - If there's no password, comment out:
    "meeting_pw" and
    "time.sleep(3)
     pag.press('enter', interval=1)
     pag.write(meeting_pw)
     pag.press('enter', interval=1)"

3. Update Zoom settings (mandatory) and set up Task Scheduler (optional).
    - Check steps in sections below.

3. Run ZoomPy.py.


Scheduling the Script (Optional):

To schedule the script to run automatically at certain times, you can use Task Scheduler by:

1. Pressing Windows key, search, and opening 'Task Scheduler'

2. Under Actions, click 'Create Task'

3. In General tab:
   - input the name of the task (ex: 'run ZoomPy script') in box for 'Name:'

4. In Actions tab:
   - Click 'New..'
   - For 'Program/script' box:
        - Input path to python.exe file.
   - For 'Add arguments (optional)' box:
        - Input python file, 'ZoomPy.py'.
   - For 'Start in (optional)' box:
        - Input path to the folder containing the Python script, 'ZoomPy.py'.

5. In Conditions tab:
    - Under Power,
        - Check 'Wake the computer to run this task':
    - If possible, (laptops)
        - Uncheck 'Start the task only if the computer is on AC power'
          and 'Stop if the computer switches to battery power'

6. In Triggers tab:
    - Click 'New..'
    - Update Settings, Start time, and Advanced Settings to your preferences.
    - Check 'Enabled' then press OK.

7. When done, press OK.


Update Zoom Settings:

a. Join audio by computer when joining a meeting (mandatory)
    - In Audio, check 'Automatically join audio by computer when joining a meeting'

b. Turn off the video when joining the meeting (to prevent accidents)
    - In Video, check 'Turn off my video when joining meeting'

c. Make the meeting full screen for the best recording (good for PPT, screensharing lectures etc.)
    - In General, check 'Enter full screen automatically when starting or joining a meeting'
