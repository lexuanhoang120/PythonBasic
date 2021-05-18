import cv2
import time
cap = cv2.VideoCapture("bida.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 1000/fps

bg = cv2.createBackgroundSubtractorMOG2()
ret = True
while ret:
    pre_time = time.time()
    ret,img = cap.read()




    bgmask = bg.apply(img)

    bgmask = cv2.merge([bgmask,bgmask,bgmask])

    result = cv2.bitwise_and(bgmask,img)

    cv2.imshow("Video", img)
    cv2.imshow("bgmask", bgmask)
    cv2.imshow("result", result)
    delta_time = (time.time() - pre_time)*1000


    if delta_time > wait_time:
        delay_time = 1
    else:
        delay_time = wait_time - delta_time
    if cv2.waitKey(int (delay_time)) == ord('q'):
        break
cv2.destroyAllWindows()
