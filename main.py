import pyautogui
import applescript
import azurelane
import platform
import pygetwindow as gw



def resizeWindow():
    if platform.system()=='Darwin':
        script = applescript.AppleScript('''
        tell application "System Events" to tell application process "BlueStacks"
            tell window 1
                set {size, position} to {{1200, 600}, {0, 0}}
            end tell
        end tell
        ''')
        #need permission first
        print(script.run())

    if platform.system()=='Windows':
        a = gw.getWindowsWithTitle('BlueStacks')[0]
        a.activate()
        a.moveTo(0,0)
        a.resizeTo(1200, 600)


def waitUntilShow(img_name,confidence):
    while find(img_name, confidence)==None:
        pass
    return find(img_name, confidence)

def find(img_name,confidence):
    try:
        img = pyautogui.locateOnScreen(img_name,confidence=confidence)
    except TypeError:
        print("NO img")
        return None
    else:
        return img


def findAll(img_name,confidence):
    try:
        imgs = pyautogui.locateAllOnScreen(img_name,confidence=confidence)
    except TypeError:
        print("NO img")
        return None
    else:
        return imgs
    finally:
        print("Done")

if __name__ == '__main__':
    resizeWindow()
    # x=find("test.png",confidence=0.5)
    # x,y=pyautogui.center(x)
    #
    # pyautogui.click(x/2,y/2)
    # print(x)
    # print("asd")
    # pyautogui.click(x / 2, y / 2)
    # print(find('chrome.png',0.6))

    #print(waitUntilShow('chrome.png',0.6))

    # for pos in findAll('chrome.png',0.6):
    #     print(pos)
    #     pyautogui.click(pos)