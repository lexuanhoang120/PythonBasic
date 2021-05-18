import cv2
import time
try:
    cap = cv2.VideoCapture("bida.mp4")
    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_time = 1000 / fps

    bg = cv2.createBackgroundSubtractorMOG2()
    
    while True:
        pre_time = time.time()
        ret, img = cap.read()


        bgmask = bg.apply(img)
        bgmask = cv2.merge([bgmask, bgmask, bgmask])
        result = cv2.bitwise_and(bgmask,img)

        cv2.imshow("Video", img)
        cv2.imshow("Mask", bgmask)
        cv2.imshow("Result", result)
        delta_time = (time.time() - pre_time) * 1000

        if delta_time > wait_time:
            delay_time = 1
        else:
            delay_time = wait_time - delta_time

        if cv2.waitKey(int(wait_time)) == ord("q"):
            break
    cv2.destroyAllWindows()
except Exception as e:
    print(e)
