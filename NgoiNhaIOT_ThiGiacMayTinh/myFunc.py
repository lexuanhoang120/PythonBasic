import cv2
import time
import numpy as np
minBlue=0
maxBlue=255

minGreen=0
maxGreen=255

minRed=0
maxRed=255

func=None
def showPanel(name):
    def Min_Blue(pos):
        global minBlue
        minBlue = pos
    def Min_Green(pos):
        global minGreen
        minGreen = pos

    def Min_Red(pos):
        global minRed
        minRed = pos

    def Max_Blue(pos):
        global maxBlue
        maxBlue = pos
    def Max_Green(pos):
        global maxGreen
        maxGreen = pos
    def Max_Red(pos):
        global maxRed
        maxRed = pos

    cv2.namedWindow(name)
    cv2.createTrackbar("Min blue",name,0,255,Min_Blue)
    cv2.createTrackbar("Min green",name,0,255,Min_Green)
    cv2.createTrackbar("Min red",name,0,255,Min_Red)

    cv2.createTrackbar("Max blue",name,255,255,Max_Blue)
    cv2.createTrackbar("Max green",name,255,255,Max_Green)
    cv2.createTrackbar("Max red",name,255,255,Max_Red)


def Mouse_event(event, x, y, f, img):

    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_event.x0 = x
        Mouse_event.y0 = y
        Mouse_event.pts = []
        Mouse_event.pts.append((x,y))
        Mouse_event.draw = True

    if event == cv2.EVENT_LBUTTONUP:
        Mouse_event.x1 = x
        Mouse_event.y1 = y
        Mouse_event.draw = False
        miny = min(Mouse_event.y0,Mouse_event.y1)
        maxy = max(Mouse_event.y0, Mouse_event.y1)

        minx = min(Mouse_event.x0, Mouse_event.x1)
        maxx = max(Mouse_event.x0, Mouse_event.x1)
        if miny==maxy:
            maxy=maxy+1
        if minx==maxx:
            maxx=maxx+1
        Mouse_event.img = img[miny:maxy,minx:maxx]

        if func is not None:

            func()
    if event == cv2.EVENT_MOUSEMOVE:
        Mouse_event.x = x
        Mouse_event.y = y
        if Mouse_event.draw:
            Mouse_event.pts.append((x,y))




Mouse_event.img = None
Mouse_event.x0 =0
Mouse_event.y0 =0
Mouse_event.x1 =0
Mouse_event.y1 =0
Mouse_event.x =0
Mouse_event.y =0
Mouse_event.draw = False

Mouse_event.addPoint = False
Mouse_event.pts = []

def setOnUp(f):
    global func
    func=f
def selPic(winname,img):
    cv2.setMouseCallback(winname,Mouse_event,img)
    if Mouse_event.draw:
        img = cv2.rectangle(img,(Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
    if Mouse_event.img is not None:
        cv2.imshow("ROI IMG", Mouse_event.img)
def getImg():
    return Mouse_event.img
def getPath():
    if len(Mouse_event.pts)>0:
        return Mouse_event.pts
    else:
        return None
