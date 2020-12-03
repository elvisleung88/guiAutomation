import pyautogui
# from pyscreeze import ImageNotFoundException
import time
from Common_func.common_func import *

class Azurelane:

    camplist={
        "camp34": "camp34.PNG",
        "camp43": "camp43.PNG"
    }
    imagePath="Azurelane/"

    enenmy=["lv3.PNG","lv2.PNG","lv1.PNG"]


    def __init__(self,camp,loop,boss,safe,teamA,teamB):
        self.camp=self.camplist[camp]
        self.loop=loop
        self.midOffset=-50
        self.boss=boss
        self.safe=safe
        self.teamA=teamA
        self.teamB=teamB

        # self.opening()
        # self.fightSelect()
        self.closing()
        # self.findAdds()
        # print(pyautogui.position())

    def closing(self):
        if click(waitUntilShow(self.imagePath + "ending1.PNG", 0.7)):
            time.sleep(2)
            pyautogui.click()
            time.sleep(3)
            if click(waitUntilShow(self.imagePath + "continue.PNG", 0.7)):
                time.sleep(1)
                pyautogui.click()
                if click(waitUntilShow(self.imagePath + "endconfirm.PNG", 0.7)):
                    time.sleep(10)

    def findAdds(self):
        for i in self.enenmy:
            imgs=findAll(self.imagePath+i,0.6)
            if imgs:
                print("Found lv Adds")
                for item in imgs:
                    pos = pyautogui.center(item)
                    pyautogui.click(pos.x + 11, pos.y + 27)
                    print("click Adds")
                    # cant reach
                    # if find(self.imagePath+"cantreach.PNG",0.7)!=None:
                    #     continue

                    time.sleep(5)
                    if self.infoPop():
                        pyautogui.click(pos.x + 11, pos.y + 27)

                    self.closing()
                    break

                break
            else:
                print("No lv Adds")

    def findBoss(self):
        pass


    def infoPop(self):
        flag=False

        #normal info pop
        if click(find(self.imagePath+"info.PNG",0.7)):
            flag=True
            time.sleep(1)
            if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                time.sleep(1)
                if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                    time.sleep(1)
                    pass

        #sell
        if click(find(self.imagePath + "sell1.PNG", 0.7)):
            flag = True
            time.sleep(1)
            if click(waitUntilShow(self.imagePath + "sell2.PNG", 0.7)):
                time.sleep(1)
                if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                    time.sleep(1)
                    if click(waitUntilShow(self.imagePath + "continue.PNG", 0.7)):
                        time.sleep(1)
                        if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                            time.sleep(1)
                            if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                                time.sleep(1)
                                if click(waitUntilShow(self.imagePath + "continue.PNG", 0.7)):
                                    time.sleep(1)
                                    if click(waitUntilShow(self.imagePath + "back.PNG", 0.7)):
                                        time.sleep(1)



    def fightSelect(self):
        numfight = 0
        currentTeam = self.teamA  # 5 or 6

        while numfight < self.boss:


            # if exists("1603255764271.png"):
            #     click("1603255764271.png")
            #     closing()
            #     numfight = numfight + 1
            #     currentTeam = currentTeam - 1
            #     continue
            #
            # if exists("1603254579622.png"):
            #     click(Pattern("1603254579622.png").targetOffset(-2, 70))
            #     if not exists("1603271060760.png"):
            #         if exists("1603256109488.png"):
            #             click(wait("1603256109488.png", FOREVER))
            #         continue

            self.infoPop()
            self.findAdds()

            numfight+=1
            currentTeam-=1

        time.sleep(3)
        self.infoPop()



    def opening(self):
        # for k in range(self.loop):
            if find(self.imagePath+"icon.PNG",0.5) != None:
                x,y=pyautogui.center(find(self.imagePath+"icon.PNG",0.5))
                pyautogui.click(x, y)
            time.sleep(1)

            x, y = pyautogui.center(find(self.imagePath+self.camp, 0.8))
            pyautogui.click(x, y)
            time.sleep(1)

            x, y = pyautogui.center(find(self.imagePath+"start1.PNG", 0.8))
            pyautogui.click(x, y)
            time.sleep(1)

            x, y = pyautogui.center(find(self.imagePath+"start2.PNG", 0.8))
            pyautogui.click(x, y)
            time.sleep(4)

            x, y = pyautogui.center(find(self.imagePath+"pos.PNG", 0.8))
            pyautogui.moveTo(x,y-100)
            pyautogui.drag(0, self.midOffset,0.5, button='left')
            self.fightSelect()