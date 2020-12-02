
def opening(camp,loop,midOffset,boss,safe,teamA,teamB):
    # for k in range(loop):
    x,y=pyautogui.locateCenterOnScreen(camp,confidence=0.8)
    pyautogui.click(x/2,y/2)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen("start.png", confidence=0.5)
    pyautogui.click(x / 2, y / 2)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen("start2.png", confidence=0.5)
    pyautogui.click(x / 2, y / 2)
    time.sleep(4)
    x, y = pyautogui.locateCenterOnScreen("pos.png",grayscale=True,confidence=0.7)
    pyautogui.moveTo(x/2,y/2+midOffset)
    pyautogui.drag(0, -100,0.5, button='left')
    fightSelect(boss, teamA, teamB, safe)