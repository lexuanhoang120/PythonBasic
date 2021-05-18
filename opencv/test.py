from PIL import Image
import cv2

img = Image.open("image.jpg")
img2 = img.resize((1200, 600))
img2.show()
img2.save("img2.jpg")
img.thumbnail((1200, 600))
img.save("img3.jpg")


