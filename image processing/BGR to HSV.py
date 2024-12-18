import cv2
import numpy as np

image = cv2.imread(r"/lo6/butterfly.jpg")

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

hue_channel = hsv_image[:,:,0]
hue_channel = (hue_channel + 30) % 180
hsv_image[:,:,0] = hue_channel


modified_image = cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR)


cv2.imshow("original" ,  image)
cv2.imshow("modified" ,  modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()