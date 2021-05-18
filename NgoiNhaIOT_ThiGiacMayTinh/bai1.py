import cv2
# read the image
image = cv2.imread("3.png")
# set the color
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cutting image
image = image[200:500,100:600]
# present the image in the window
cv2.imshow("Image",image)
cv2.waitKey()
