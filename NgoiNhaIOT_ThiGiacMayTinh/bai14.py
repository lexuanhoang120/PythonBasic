import cv2
import numpy as np
from myFunc import getPath, selPic
import time
from matplotlib import path

cap = cv2.VideoCapture("bida.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 1000 / fps

bg = cv2.createBackgroundSubtractorMOG2()
ret = True
while ret:
    pre_time = time.time()
    ret, img = cap.read()

    bgmask = bg.apply(img)
    bgmask = cv2.erode(bgmask, np.ones((5, 5)))

    if getPath() is not None:

        p = path.Path(np.array(getPath()))
        poly = np.array([getPath()])
        cv2.polylines(img, [poly], True, (255, 0, 0), 2)

        contours, _ = cv2.findContours(bgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        count = 0
        if len(contours) > 0:
            for c in contours:
                M = cv2.moments(c)
                x = int(M['m10'] / (M['m00'] + 1))
                y = int(M['m01'] / (M['m00'] + 1))

                if p.contains_point((x, y)):
                    count = count + 1
                    cv2.putText(img, str(count), (x, y), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255))

    bgmask = cv2.merge([bgmask, bgmask, bgmask])
    result = cv2.bitwise_and(bgmask, img)

    selPic("Video", img)
    cv2.imshow("Video", img)
    cv2.imshow("bgmask", bgmask)
    cv2.imshow("result", result)
    delta_time = (time.time() - pre_time) * 1000

    if delta_time > wait_time:
        delay_time = 1
    else:
        delay_time = wait_time - delta_time
    if cv2.waitKey(int(delay_time)) == ord('q'):
        break
cv2.destroyAllWindows()
