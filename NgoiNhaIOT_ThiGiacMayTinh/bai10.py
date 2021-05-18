import cv2
import time


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

cap = cv2.VideoCapture("tracking.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = 1000 / fps

while True:
    pre_time = time.time()
    ret, img = cap.read()
    img_clone = img.copy()

    if mouse_event.draw:
        img_clone = cv2.rectangle(img_clone, (mouse_event.x0, mouse_event.y0), (mouse_event.x, mouse_event.y),
                                  (0, 0, 255))
    if mouse_event.img is not None:
        cv2.imshow("Sample", mouse_event.img)

    cv2.imshow("Video", img_clone)
    cv2.setMouseCallback("Video", mouse_event, img)

    delta_time = (time.time() - pre_time) * 1000
    if delta_time > wait_time:
        delay_time = 1
    else:
        delay_time = wait_time - delta_time

    if cv2.waitKey(int(wait_time)) == ord("q"):
        break
cv2.destroyAllWindows()
