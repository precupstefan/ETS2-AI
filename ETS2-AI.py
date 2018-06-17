# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:17:14 2018

@author: psa97

install vJoy from http://vjoystick.sourceforge.net/
Install pyvjoy from https://github.com/tidzo/pyvjoy
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyvjoy
import pyHook,pythoncom,sys
import key_grab
import settings
import threading
import imageprocessing
import speedinfo



def press_buttons():
    
    controller.set_axis(pyvjoy.HID_USAGE_SL1,0x8000)
# else:
    controller.set_axis(pyvjoy.HID_USAGE_SL1,0x0)
      
    return 
#
#   CAPTURE THE GAME GAME WINDOW
#   GAME MUST BE TOP LEFT CORNER
#   REZOLUTION 1280x720
#

def main():
    #load speeds
    speedinfo.load()
    speedinfo.load_speedlimit()
    # initialize keygrabing
    key_thread= threading.Thread(target=key_grab.init)
    key_thread.daemon=True
    key_thread.start()


    last_time_speedcheck=time.time()

    while(True):

        #   Capture image acording to game resolution
        screen=np.array(ImageGrab.grab(bbox=(0,30,1280,750)))

        gray_image=imageprocessing.convert_to_gray(screen)

        if time.time()-last_time_speedcheck>settings.speed_check_interval :
            #speedinfo.adjust_speed(gray_image,settings.speed_current_ROI,speedrecognizer)
            imageprocessing.detect_speed(gray_image,settings.speed_current_ROI)
            imageprocessing.detect_speed_limit(gray_image,settings.speed_restriction_ROI)
            speedinfo.test()
            last_time_speedcheck=time.time()
        
        #cv2.imshow('ETS2_AI',imageprocessing.get_subimage(gray_image,settings.speed_current_ROI))
        cv2.imshow('ETS2_AI',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    #   Place Image at desired location. Delete this line if no location is desired
        cv2.moveWindow('ETS2_AI',1281,0)
        
        
        if cv2.waitKey(25) & 0XFF ==ord('q'):
            cv2.destroyAllWindows()
            break




controller=settings.controller

main()