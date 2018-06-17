import cv2
import pytesseract
from PIL import Image
import random
import os
import Global

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def convert_to_gray(original_image):
    return cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

def get_lanes(gray_image):
    return cv2.Canny(gray_image,threshold1=100,threshold2=200)

def get_subimage(img,region):
    return cv2.bitwise_not(img[region[0]:region[1],region[2]:region[3]])

def detect_speed(img,region):
    img=get_subimage(img,region)
    value, value1 = Global.speed_recognizer.predict(img)
    Global.speed_current=value
    #Global.update_current_speed(value)
    return

def detect_speed_limit(img,region):
    img=get_subimage(img,region)
    value, value1= Global.speed_limit_recognizer.predict(img)
    Global.speed_limit=value


