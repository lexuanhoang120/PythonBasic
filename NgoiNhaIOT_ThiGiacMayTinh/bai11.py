import cv2
import time

try:

    def mouse_event(event, x, y, f, img):
        if event == cv2.EVENT_LBUTTONDOWN:
            mouse_event.x0 = x
            mouse_event.y0 = y
            mouse_event.draw = True
        if event == cv2.EVENT_LBUTTONUP:
            mouse_event.x1 = x
            mouse_event.y1 = y
            mouse_event.draw = False
            miny = min(mouse_event.y0, mouse_event.y1)
            maxy = max(mouse_event.y0, mouse_event.y1)
            minx = min(mouse_event.x0, mouse_event.x1)
            maxx = max(mouse_event.x0, mouse_event.x1)
            mouse_event.img = img[miny:maxy, minx:maxx]
        if event == cv2.EVENT_MOUSEMOVE:
            mouse_event.x = x
            mouse_event.y = y


    mouse_event.img = None
    mouse_event.x0 = 0
    mouse_event.y0 = 0
    mouse_event.x1 = 0
    mouse_event.y1 = 0
    mouse_event.x = 0
    mouse_event.y = 0
    mouse_event.draw = False

    # cap = cv2.VideoCapture("tracking.mp4")
    cap = cv2.VideoCapture(0)

    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_time = 1000 / fps
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

        if mouse_event.draw:
            img_clone = cv2.rectangle(img_clone, (mouse_event.x0, mouse_event.y0), (mouse_event.x, mouse_event.y),
                                      (0, 0, 255), 2)
        if mouse_event.img is not None:
            tpt = cv2.matchTemplate(img_clone, mouse_event.img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(tpt)
            if max_val > .5:
                cv2.putText(img_clone, "%.2f" % max_val, max_loc, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                h, w, d = mouse_event.img.shape
                cv2.rectangle(img_clone, max_loc, (max_loc[0] + w, max_loc[1] + h), (255, 0, 0), 2)
            cv2.imshow("Sample", mouse_event.img)
            cv2.imshow("Compare", tpt)

        cv2.imshow("Video", img_clone)
        cv2.setMouseCallback("Video", mouse_event, img)

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
except Exception as e:
    print(e)
