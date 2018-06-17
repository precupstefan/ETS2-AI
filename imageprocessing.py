import cv2
import pytesseract
from PIL import Image
import random
import os
import speedinfo
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def convert_to_gray(original_image):
    return cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

def get_lanes(gray_image):
    return cv2.Canny(gray_image,threshold1=100,threshold2=200)

def get_subimage(img,region):
    return cv2.bitwise_not(img[region[0]:region[1],region[2]:region[3]])

def get_speed(img,region,speedrecognizer):
    img=get_subimage(img,region)
    value=speedrecognizer.predict(img)
    print('You are crusing at {}'.format(value))
    return 


