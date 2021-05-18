import cv2
import time

def Mouse_event(event, x, y, f, img):

    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_event.x0 = x
        Mouse_event.y0 = y
        Mouse_event.draw = True
    if event == cv2.EVENT_LBUTTONUP:
        Mouse_event.x1 = x
        Mouse_event.y1 = y
        Mouse_event.draw = False
        miny = min(Mouse_event.y0,Mouse_event.y1)
        maxy = max(Mouse_event.y0, Mouse_event.y1)

        minx = min(Mouse_event.x0, Mouse_event.x1)
        maxx = max(Mouse_event.x0, Mouse_event.x1)
        Mouse_event.img = img[miny:maxy,minx:maxx]
    if event == cv2.EVENT_MOUSEMOVE:
        Mouse_event.x = x
        Mouse_event.y = y


Mouse_event.img = None
Mouse_event.x0 =0
Mouse_event.y0 =0
Mouse_event.x1 =0
Mouse_event.y1 =0
Mouse_event.x =0
Mouse_event.y =0
Mouse_event.draw = False


cap = cv2.VideoCapture(0)
 # fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 0
# print fps

play = True
while True:
    pre_time = time.time()

    if play:
        ret, img = cap.read()
    if img is None:
        img = temp_img
    else:
        temp_img = img
    img_clone = img.copy()

    if Mouse_event.draw:
        img_clone = cv2.rectangle(img_clone,(Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
    if Mouse_event.img is not None:
        tpt = cv2.matchTemplate(img_clone,Mouse_event.img,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(tpt)

        if max_val > .5:
            cv2.putText(img_clone,"%.2f" %max_val,max_loc,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2 )
            h,w,d = Mouse_event.img.shape
            cv2.rectangle(img_clone,max_loc,(max_loc[0]+w,max_loc[1]+h),(255,0,0),2)

        cv2.imshow("Sample", Mouse_event.img)
        cv2.imshow("Compare", tpt)
    cv2.imshow("Video", img_clone)
    cv2.setMouseCallback("Video",Mouse_event,img)

    delta_time = (time.time() - pre_time) * 1000
    if delta_time > wait_time:
        delay_time = 1
    else:
        delay_time = wait_time - delta_time
    key = cv2.waitKey(int(delay_time))
    if key == ord('q'):
        break
    if key == ord(' '):
        play = not play
cv2.destroyAllWindows()
