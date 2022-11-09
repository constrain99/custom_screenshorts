import pyautogui
import win32api
import time
import os

directory = r'screenshorts\cd_slides'


isExist = os.path.exists(directory)

print(isExist)


if isExist==False:
    os.mkdir(directory)


length=len(os.listdir(directory))

if length==0:
    k=0
    i=0
    while k==0: 
        x=win32api.GetKeyState(0x1B)
        
        if x<0:
            print(x)
            
            myslide=pyautogui.screenshot()
            myslide.save(f'{directory}\photo{i}.png')
            i=i+1
        time.sleep(0.1)
        

else:

    k=0
    i=length+1
    while k==0: 
        x=win32api.GetKeyState(0x1B)
        
        if x<0:
            print(x)
            
            myslide=pyautogui.screenshot()
            myslide.save(f'{directory}\photo{i}.png')
            i=i+1
        time.sleep(0.1)


