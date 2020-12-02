import pyautogui


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
    # print(find('chrome.png',0.6))

    #print(waitUntilShow('chrome.png',0.6))

    # for pos in findAll('chrome.png',0.6):
    #     print(pos)
    #     pyautogui.click(pos)