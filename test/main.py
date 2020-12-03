import pyautogui as ag
from pyscreeze import ImageNotFoundException
import time




def runCamp(camp,loop,midOffset,boss,safe,teamA,teamB):
    iconx, icony = ag.locateCenterOnScreen('icon.png', confidence=0.5)
    ag.click(iconx / 2, icony / 2)
    ag.dragTo(100, 200, button='left')
    print("done")



def findAdds():
    enemySize=["lv3.png","lv2.png","lv1.png"]
    if exist(enemySize[0]):
        pass
    if exist(enemySize[1]):
        pass
    if exist(enemySize[2]):
        pass



def exist(img):
    try:
        x, y = ag.locateCenterOnScreen(img, confidence=0.4)
        ag.click(x / 2 + 52, y / 2 + 63)
        return True
    except:
        print("cant find img:%s"%img)
        return False

def closing():
    while(True):
        if exist("win.png"):
            x, y = ag.locateCenterOnScreen("win.png", grayscale=True, confidence=0.5)
            ag.click(x / 2, y / 2)
            time.sleep(3)

            x, y = ag.locateCenterOnScreen("continue.png", grayscale=True, confidence=0.7)
            ag.click(x/2,y/2)
            time.sleep(3)
            x, y = ag.locateCenterOnScreen("confirm.png", grayscale=True, confidence=0.5)
            ag.click(x / 2, y / 2)

            break
        else:
            time.sleep(2)
            continue

def fightSelect(boss,teamA,teamB,safe):
    numfight = 0
    currentTeam = teamA  # 5 or 6

    while numfight < boss:
        if exists("1603255764271.png"):
            click("1603255764271.png")
            closing()
            numfight = numfight + 1
            currentTeam = currentTeam - 1
            continue

        if exists("1603254579622.png"):
            click(Pattern("1603254579622.png").targetOffset(-2, 70))
            if not exists("1603271060760.png"):
                if exists("1603256109488.png"):
                    click(wait("1603256109488.png", FOREVER))
                continue

        infoPop()
        findAdds()
        numfight = numfight + 1
        currentTeam = currentTeam - 1

    time.sleep(3)
    infoPop()
    findBoss(R, safe)

def opening(camp,loop,midOffset,boss,safe,teamA,teamB):
    for k in range(loop):
        x,y=ag.locateCenterOnScreen(camp,confidence=0.8)
        ag.click(x/2,y/2)
        time.sleep(1)
        x, y = ag.locateCenterOnScreen("start.png", confidence=0.5)
        ag.click(x / 2, y / 2)
        time.sleep(1)
        x, y = ag.locateCenterOnScreen("start2.png", confidence=0.5)
        ag.click(x / 2, y / 2)
        time.sleep(4)
        x, y = ag.locateCenterOnScreen("pos.png",grayscale=True,confidence=0.7)
        ag.moveTo(x/2,y/2+midOffset)
        ag.drag(0, -100,0.5, button='left')
        fightSelect(boss, teamA, teamB, safe)



if __name__ == '__main__':
    camp43="camp43.png"
    iconx, icony = ag.locateCenterOnScreen('icon.png',grayscale=True,confidence=0.7)
    ag.click(iconx / 2, icony / 2)

    # opening(camp43, 5, -100, 3, True, 5, 5) #loop, y offset, boss, 安海,teamA, teamB
    findAdds()
    print("Done")





