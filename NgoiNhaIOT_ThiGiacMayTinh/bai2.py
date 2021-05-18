import cv2
import numpy as np
img = np.empty((600,800,3))
img[0:600,0:8000,(1,2,0)]=255

for i in range(0,600,50):
    cv2.line(img,(0,i),(800,i),(0,0,0),1)
    cv2.putText(img,str(i),(10,i),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
for i in range(0,800,50):
    cv2.line(img,(i,0),(i,600),(0,0,0),1)
    cv2.putText(img,str(i),(i,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))

cv2.circle(img,(50,100),50,(0,0,255))
cv2.ellipse(img,(300,300),(50,100),0,90,180,(111,0,22))
pts = np.array(((0,0),(100,50),(300,100),(100,100)),np.int32)
pts = [pts.reshape((4,1,2))]
print(pts)
cv2.polylines(img,pts,True,(0,0,0),thickness=10)

cv2.imshow("Image",img)
cv2.waitKey()
