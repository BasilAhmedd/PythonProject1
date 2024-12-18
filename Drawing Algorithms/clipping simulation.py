import cv2
import numpy as np

img = np.ones((400,400,3),np.uint8) * 255

cv2.rectangle(img,(100,100),(300,300),(0,255,0),2)

cv2.line(img,(50,50),(350,350),(255,0,0),2)
cv2.line(img,(150,150),(150,350),(0,0,255),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()