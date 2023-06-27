from pyautogui import press, typewrite, keyDown, keyUp

keyDown('alt')
for i in range(1000000):
    press('tab')
keyUp('alt')
