from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  550 Y:  394 RGB: ( 85,  87, 116)
#X:  637 Y:  394 RGB: ( 89,  91, 117)
#X:  723 Y:  383 RGB: ( 89,  91, 118)
#X:  815 Y:  376 RGB: (  0,   0,   0)

def click(x,y) :
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


time.sleep(5)

while keyboard.is_pressed('q') == False :

    if pyautogui.pixel(550, 400)[0] == 0 :
        click(550,400)
    elif pyautogui.pixel(637, 400)[0] == 0 :
        click(637,400)
    elif pyautogui.pixel(723, 400)[0] == 0 :
        click(723,400)
    elif pyautogui.pixel(815, 400)[0] == 0 :
        click(815,400)




