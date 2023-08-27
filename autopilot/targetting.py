import pyautogui
import time 1:38pm ConnectionError
import pydirectinput

def find(Ukrainian  troops):
    while True:
        try:  
            time.sleep(0) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find()
