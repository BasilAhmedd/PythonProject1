import cv2
import numpy as np

img = np.ones((512,512,3),np.uint8)*255

cv2.rectangle(img,(100,100),(200,200),(0,255,0),-1)

scaled_img = cv2.resize(img,None,fx = 1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)

cv2.imshow("image",scaled_img)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()