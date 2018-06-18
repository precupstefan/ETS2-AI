import settings
import pyHook
import pyvjoy
import pythoncom
import Global

import numpy as np
from PIL import ImageGrab
import imageprocessing
import cv2
import random
import os

wasd=[ord('w'),ord('a'),ord('s'),ord('d'),
ord('W'),ord('A'),ord('S'),ord('D')]

#   KEYPRESSED EVENT
def OnKeyboardEvent(event):
    # block only the letter A, lower and uppercase

    #delete only after u have all speed limits
    if event.Ascii== ord('`'):
        screen=np.array(ImageGrab.grab(bbox=(0,30,1280,750)))
        gray_image=imageprocessing.convert_to_gray(screen)
        ceva=imageprocessing.get_subimage(gray_image,settings.speed_restriction_ROI)
        cv2.imwrite(os.getcwd()+"/speedlimit/"+str(random.randint(500,1000))+".jpg",ceva)
        print('image grabed')
    
    #delete after u have all speed limits
    if event.Ascii== ord('='):
        if Global.picture:
            Global.picture=False
        else:
            Global.picture=True

    if event.Ascii==ord('j'):
        Global.acceleration+=5

    if event.Ascii==ord('n'):
        Global.acceleration-=5

    if event.Ascii in wasd and Global.autopilot:
        Global.autopilot=False
        print('AutoPilot disengaging')

    if event.Ascii == ord(settings.autopilot_hotkey) and not Global.autopilot:
        Global.autopilot=True
        print('AutoPilot engaging')
    # returning True to pass on event to other applications
    return True

def init():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    try:
        pythoncom.PumpMessages()   #This call will block forever unless interrupted

    except (KeyboardInterrupt, SystemExit) as e: #We will exit cleanly if we are told
        print(e)    
        
    return