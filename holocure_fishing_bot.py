from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

#down arrow: blue RGB: (51, 144, 246)
#up arrow: red RGB: (222,  41,  42)
#right arrow: green  RGB: (47, 234,  45) 
#left arrow: yellow RGB:(246, 196,  57)
#ok button: purple RGB: (185,  44, 223)

#fish position X:  942 Y:  265 RGB: ( 64,  64,  64)
time.sleep(2)

x_offset = 1140

y_offset = 715

VK_Z = 0x5A
VK_A = 0x41
VK_S = 0x53
VK_W = 0x57
VK_D = 0x44

VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28

def keyPressed(key_code):
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    time.sleep(0.05)
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)
    

while keyboard.is_pressed('q') == False:    
    keyPressed(VK_Z)
    time.sleep(0.5)
    flagIn = 0
    flagR, flagG, flagB = pyautogui.pixel(942, 265);
    if (flagR in range (60, 70) ) and (flagG in range (60, 70) ) and (flagB in range (60, 70) ):
        flagIn = 1

    while flagIn == 1:    
        flag = 0
        pic = pyautogui.screenshot(region=(x_offset,y_offset,80,80))

        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):

                r, g, b = pic.getpixel((x, y))

                if (r in range (40,70)) and (g in range(130,150)) and (b in range(240, 255)):
                    flag = 1
                    keyPressed(VK_DOWN)
                    time.sleep(0.05)
                    break
                elif (r in range (210,230)) and (g in range(35, 55)) and (b in range(35, 55)):
                    flag = 1                
                    keyPressed(VK_UP)
                    time.sleep(0.05)
                    break
                elif (r in range (18,50)) and (g in range(230, 255)) and (b in range(18, 50)):
                    flag = 1
                    keyPressed(VK_RIGHT)
                    time.sleep(0.05)
                    break
                elif (r in range (220,255)) and (g in range(180, 210)) and (b in range(50, 80)):
                    flag = 1
                    keyPressed(VK_LEFT)
                    time.sleep(0.05)
                    break
                elif (r in range (148,186)) and (g in range(40, 60)) and (b in range(170, 225)):
                    flag = 1
                    keyPressed(VK_Z)                    
                    time.sleep(0.05)
                    break
            if flag == 1:
                break
            
        okButtonR, okButtonG, okButtonB = pyautogui.pixel(790, 401); 

        if (okButtonR in range (60, 80) ) and (okButtonG in range (180, 200) ) and (okButtonB in range (240, 256) ):            
            flagIn = 0
            break
