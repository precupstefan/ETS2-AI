import cv2
import os
import numpy as np
from PIL import Image

def train():
    img=[]
    labels=[]
    speedRecognizer = cv2.face_LBPHFaceRecognizer.create()
    for filename in os.listdir(os.getcwd()+"/speeds"):
        image=cv2.imread(os.getcwd()+"/speeds/"+filename,cv2.IMREAD_GRAYSCALE)
        img.append(image)
        labels.append( int(filename.rsplit( ".", 1 )[ 0 ] ))
    speedRecognizer.train(img, np.array(labels))
    print('Training was succesful')
    return speedRecognizer



