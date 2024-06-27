import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

Image = 'C:\projectofml\OSR\imag2.jpg'
reader = easyocr.Reader(['en'],gpu=True)
result  = reader.readtext(Image)
# print(result)
# top_left = tuple(result[0][0][0])
# bottom_right = tuple(result[0][0][2])
# text = result[0][1]
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.imread(Image)
# img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
# img = cv2.putText(img,text,top_left,font,.5,(255,255,255),2,cv2.LINE_AA)
# plt.imshow(img)
# plt.show()

img1  = cv2.imread(Image)
for detection in result:
    top_left1 = tuple([int(val) for val in detection[0][0] ])
    bottom_right1 = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = cv2.rectangle(img1,top_left1,bottom_right1,(0,255,0),5)
    img1 = cv2.putText(img1,text,top_left1,font,2,(255,255,255),2,cv2.LINE_AA)
    plt.figure(figsize=(10,10))
    plt.imshow(img1)
    plt.show()
    