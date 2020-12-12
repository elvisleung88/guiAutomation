import pyautogui
# from pyscreeze import ImageNotFoundException
import time
from Common_func.common_func import *
import numpy as np
from scipy import spatial

class Azurelane:
    camplist={
        "camp34": "camp34.PNG",
        "camp43": "camp43.PNG"
    }
    imagePath="Azurelane/"
    enenmy=["lv1.PNG","lv2.PNG","lv3.PNG"]
    numfight = 0

    def __init__(self,camp,loop,boss,safe,teamA,teamB):
        self.camp=self.camplist[camp]
        self.loop=loop
        self.midOffset=-50
        self.boss=boss
        self.safe=safe
        self.teamA=teamA
        self.teamB=teamB
        self.currentTeam = self.teamA


        self.debug()

        # self.opening()
        # self.fightSelect()
        # self.closing()
        # self.findAdds()
        # self.findBoss()
        # self.infoPop()
        # self.findClosest(610,314)

    def setImgPath(self):

        self.imagePath = "Azurelane/"

    def debug(self):
        # time.sleep(5)
        # print(pyautogui.position())
        # pyautogui.moveTo(20, 20)
        print(pyautogui.size())
        pyClick(find(self.imagePath+'icon.PNG',0.7))
        # print(pyautogui.position())

        if pyClick(find(self.imagePath +'camp43_d.png' , 0.6)):
            print("okm")


        # if find(self.imagePath + "debug.PNG", 0.5) != None:
        #     x, y = pyautogui.center(find(self.imagePath + "icon.PNG", 0.5))
        #     print(x, y)
        #     pyautogui.click(x / 2, y / 2)
        #
        # time.sleep(1)
        # if find(self.imagePath + self.camp, 0.9) != None:
        #     click(find(self.imagePath + self.camp, 0.9))
        # time.sleep(1)
        # return
        #
        # click(find(self.imagePath + "start1.PNG", 0.8))
        # time.sleep(1)


    def closing(self):
        entry=waitUntilShow(self.imagePath + "ending1.PNG", 0.7)
        print("...closing")
        if entry!=None:
            time.sleep(2)
            click(entry)
            if click(waitUntilShow(self.imagePath + "continue.PNG", 0.7)):
                time.sleep(1)
                if click(waitUntilShow(self.imagePath + "endconfirm.PNG", 0.6)):
                    time.sleep(6)

    def walking(self,posX,posY):
        # walking reclick if infopop
        time.sleep(5)
        if self.infoPop():
            pyautogui.click(posX,posX)

        #if trap


    def findAdds(self):
        for i,val in reversed(list(enumerate(self.enenmy,start=1))):
            imgs=findAll(self.imagePath+val,0.6)
            if imgs:
                print("Found lv", i, "Adds")
                for item in imgs:
                    pos = pyautogui.center(item)
                    self.checkReach(pos.x,pos.y,11,27)
                    break

                break
            else:
                print("No lv",i, "Adds")


    def checkReachBoss(self,x,y):
        pyautogui.click(x, y)
        time.sleep(1)
        if find(self.imagePath + "cantreach.PNG", 0.5) != None:
            nearbys = self.nearby(x, y)
            print(nearbys)
            pt = np.array([[x, y]])
            distance, index = spatial.KDTree(nearbys).query(pt)
            nearest = nearbys[spatial.KDTree(nearbys).query(pt)[1]]
            return self.checkReach(nearest[0][0], nearest[0][1])        #not ok
        else:
            return True      #ok


    def checkReach(self,x,y,xOffset=0,yOffset=0):
        pyautogui.click(x+xOffset,y+yOffset)
        self.walking(x+xOffset,y+yOffset)
        time.sleep(1)
        if find(self.imagePath+"cantreach.PNG",0.5)!=None:
            nearbys = self.nearby(x, y)
            pt = np.array([[x, y]])
            nearest = nearbys[spatial.KDTree(nearbys).query(pt)[1]]
            print("nearrrrr %i %i",nearest[0][0],nearest[0][1])


            while abs(x - nearest[0][0])<5 and abs(y-nearest[0][1])<5:
                distance, index = spatial.KDTree(nearbys).query(pt)
                nearbys = np.delete(nearbys, int(index), 0)
                nearest = nearbys[spatial.KDTree(nearbys).query(pt)[1]]

            # print(nearbys)
            time.sleep(2)
            return self.checkReach(nearest[0][0], nearest[0][1],xOffset,yOffset) #Not Ok
        else:
            self.closing()
            self.numfight += 1
            self.currentTeam -= 1
            return False    #ok

    def nearby(self,x,y):
        #return a point's nearby enemies
        enemyList= np.zeros(shape=(0,2),dtype=int)
        for i in self.enenmy:
            imgs=findAll(self.imagePath+i,0.6)
            if imgs:
                for item in imgs:
                    pos = pyautogui.center(item)
                    itemPos = np.array([[pos.x, pos.y]])
                    enemyList = np.vstack((enemyList, itemPos))
        return enemyList


    def findBoss(self):
        time.sleep(3)
        boss = find(self.imagePath + "boss.PNG", 0.7)
        if boss!=None:
            boss = pyautogui.center(boss)
            time.sleep(1)

            if not self.checkReachBoss(boss.x,boss.y):
                self.findBoss(self)
            self.walking(boss.x,boss.y)
            self.closing()
            
        

    def infoPop(self):
        flag=False

        if click(find(self.imagePath+"continue.PNG",0.7)):
            flag = True

        # sell
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


        #normal info pop
        if find(self.imagePath+"info.PNG",0.7)!=None:
            flag=True
            if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                time.sleep(1)
                if click(waitUntilShow(self.imagePath + "confirm.PNG", 0.7)):
                    time.sleep(1)





    def fightSelect(self):
        while self.numfight < self.boss:
            if find(self.imagePath + "question.PNG", 0.7)!=None:
                pos=pyautogui.center(find(self.imagePath + "question.PNG", 0.7))
                pyautogui.click(pos.x + 8, pos.y + 37)
                print("clicked question")

                if find(self.imagePath + "cantreach.PNG", 0.5) != None:
                    print("...cant reach")
                    time.sleep(3)
                    closetPos = self.findClosest(pos.x, pos.y)
                    pyautogui.click(closetPos[0] + 11, closetPos[1] + 27)
                    self.walking(closetPos[0] + 11, closetPos[1] + 27)
                    self.closing()
                    pyautogui.click(pos.x + 8, pos.y + 37)

                time.sleep(5)
                if self.infoPop():
                    click(find(self.imagePath + "question.PNG", 0.7))
                else:
                    time.sleep(3) #new enemy on map

            self.infoPop()
            time.sleep(1)
            self.findAdds()

        time.sleep(3)
        self.infoPop()
        self.findBoss()




    def opening(self):
        for k in range(self.loop):
            self.infoPop()
            time.sleep(1)

            if find(self.imagePath+"icon.PNG",0.5) != None:
                x,y=pyautogui.center(find(self.imagePath+"icon.PNG",0.5))
                print(x,y)
                pyautogui.click(x/2, y/2)

            time.sleep(1)
            if find(self.imagePath + self.camp, 0.9)!=None:
                click(find(self.imagePath+self.camp, 0.9))
            time.sleep(1)
            return

            click(find(self.imagePath+"start1.PNG", 0.8))
            time.sleep(1)

            click(find(self.imagePath+"start2.PNG", 0.8))
            time.sleep(4)

            x, y = pyautogui.center(find(self.imagePath+"pos.PNG", 0.8))
            pyautogui.moveTo(x,y-100)
            pyautogui.drag(0, self.midOffset,0.5, button='left')
            self.fightSelect()