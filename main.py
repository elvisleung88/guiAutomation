from Azurelane.azurelane import Azurelane
from Common_func.common_func import *


if __name__ == '__main__':
    resizeWindow()
    az = Azurelane("camp34", 10, 3, True, 5, 5)

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