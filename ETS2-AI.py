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
import Global
import os
import random

def display_image(image):

    cv2.rectangle(image,(settings.speed_current_ROI[2],settings.speed_current_ROI[0]),(settings.speed_current_ROI[3],settings.speed_current_ROI[1]),(0,255,0),2)
    cv2.rectangle(image,(settings.speed_restriction_ROI[2],settings.speed_restriction_ROI[0]),(settings.speed_restriction_ROI[3],settings.speed_restriction_ROI[1]),(0,255,0),2)

    cv2.imshow('ETS2_AI',cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
#   Place Image at desired location. Delete this line if no location is desired
    cv2.moveWindow('ETS2_AI',1281,0)
    return

def reset_controls():
    controller.set_axis(pyvjoy.HID_USAGE_SL1,0)
    return

def manage_speed():
    speedinfo.calculate_acceleration()
    controller.set_axis(pyvjoy.HID_USAGE_SL1,int(327.68*Global.acceleration))
    return 
#
#   CAPTURE THE GAME GAME WINDOW
#   GAME MUST BE TOP LEFT CORNERq
#   REZOLUTION 1280x720
#

def display_info():
    print('Autopilot: {} .You are crusing at {} in a {} limit zone. Acceleration at {}'.format(Global.autopilot,Global.speed_current,Global.speed_limit,Global.acceleration))
    return 

def main():
    #load speeds
    speedinfo.load()
    speedinfo.load_speedlimit()

    # initialize keygrabing
    key_thread= threading.Thread(target=key_grab.init)
    key_thread.daemon=True
    key_thread.start()

    last_time_speedcheck=time.time()

    #delete after having all speed pictures
    i=500

    while(True):

        #   Capture image acording to game resolution
        screen=np.array(ImageGrab.grab(bbox=(0,30,1280,750)))

        gray_image=imageprocessing.convert_to_gray(screen)
        
        if time.time()-last_time_speedcheck>settings.speed_check_interval :
            #speedinfo.adjust_speed(gray_image,settings.speed_current_ROI,speedrecognizer)
            imageprocessing.detect_speed(gray_image,settings.speed_current_ROI)
            imageprocessing.detect_speed_limit(gray_image,settings.speed_restriction_ROI)
            last_time_speedcheck=time.time()
        

        if Global.autopilot:
            manage_speed()
        else:
            reset_controls()


        display_image(screen)
        display_info()
        


        ##delete after u have pictures of every speed x10
        if Global.picture:
            ceva=imageprocessing.get_subimage(gray_image,settings.speed_current_ROI)
            cv2.imwrite(os.getcwd()+"/speedlimit/"+str(i)+".jpg",ceva)
            print('image grabed')
            i+=1
        
        
        if cv2.waitKey(25) & 0XFF ==ord('q'):
            cv2.destroyAllWindows()
            break




controller=settings.controller

main()