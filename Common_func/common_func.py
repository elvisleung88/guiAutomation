import pyautogui
import applescript
import platform
import pygetwindow as gw
import time
from pyscreeze import ImageNotFoundException


#change window to 1200x600
def resizeWindow():
    if platform.system()=='Darwin':
        script = applescript.AppleScript('''
        tell application "System Events" to tell application process "BlueStacks"
            tell window 1
                set {size, position} to {{1200, 600}, {0, 30}}
            end tell
        end tell
        ''')
        #need permission first
        print(script.run())
        #1680*1050

    if platform.system()=='Windows':
        a = gw.getWindowsWithTitle('BlueStacks')[0]
        a.activate()
        a.moveTo(0,0)
        a.resizeTo(1200, 600)
        print("..resizeWindow")
        #1920*1080


#wait image until show up. last for 3 mins terminate
def waitUntilShow(img_path,confidence):
    timeout = time.time() + 60*3
    while find(img_path, confidence) == None:
        if time.time() > timeout:
            break
    return find(img_path, confidence)


def find(img_path,confidence):
    try:
        img = pyautogui.locateOnScreen(img_path,confidence=confidence)
    except TypeError:
        print("NO img")
        return None
    else:
        return img

def click(findQueue):
    if findQueue != None:
        x, y = pyautogui.center(findQueue)
        pyautogui.click(getXY(x,y))
        return True
    return False

def getXY(x,y):
    if (platform.system() == 'Windows'):
        return x,y
    else:
        return x/2,y/2

def findAll(img_path,confidence):
    try:
       imgs=list(pyautogui.locateAllOnScreen(img_path,confidence=confidence))
    except TypeError:
        return None
    else:
        return imgs
    finally:
        pass