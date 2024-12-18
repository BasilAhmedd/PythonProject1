import cv2
import numpy as np

image = cv2.imread(r"/lo6/butterfly.jpg")

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

saturation_channel = hsv_image[:,:,1]
saturation_channel = np.clip(saturation_channel*1.5, 0, 255)
hsv_image[:,:,1] = saturation_channel

modified_image = cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR)

cv2.imshow("original" ,  image)
cv2.imshow("modified" ,  modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()