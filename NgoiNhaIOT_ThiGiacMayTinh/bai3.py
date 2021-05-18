import  cv2
import numpy as np
blue =0
green=0
red=0

def blue_function(pos):
    global blue
    blue=pos
def green_function(pos):
    global green
    green=pos
def red_function(pos):
    global red
    red=pos

cv2.namedWindow("Image")
cv2.createTrackbar("Blue: ","Image",0,255,blue_function)
cv2.createTrackbar("Green: ","Image",0,255,green_function)
cv2.createTrackbar("Red: ","Image",0,255,red_function)
while True:
    img=np.empty((600,800,3),np.uint8)
    img[:,:,0]=blue
    img[:,:,1]=green
    img[:,:,2]=red
    cv2.imshow("Image",img)
    if cv2.waitKey(10)==ord("q"):
        break
cv2.destroyAllWindows()

