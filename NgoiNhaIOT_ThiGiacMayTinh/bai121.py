import  cv2
import numpy as np
import myFunc as mf
try:
    cap = cv2.VideoCapture(0)

    while 1:
        img = cap.read()[1]
        if mf.getImg() is None:
            roi = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        else:
            roi = cv2.cvtColor(mf.getImg(),cv2.COLOR_BGR2HSV)

        h = np.mean(roi[:,:,0])
        s = np.mean(roi[:,:,1])
        v = np.mean(roi[:,:,2])

        l = np.array([h-30,s-30,v-30])
        u = np.array([h+30,s+30,v+30])

        mask = cv2.inRange(cv2.cvtColor(img,cv2.COLOR_BGR2HSV),l,u)

        contour,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contour)>0:
            dt = []
            for c in contour:
                dt.append(cv2.contourArea(c))
            max_i=np.argmax(dt)

            max_c = contour[max_i]
            cv2.polylines(img,[max_c],True,(0,255,0),2)


        cv2.imshow("webcam",img)
        cv2.imshow("Mask",mask)
        mf.selPic("webcam",img)



        key = cv2.waitKey(10)
        if key ==ord("q"):
            break
    cv2.destroyAllWindows()
except Exception as e:
    print(e)
