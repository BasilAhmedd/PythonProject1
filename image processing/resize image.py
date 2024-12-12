import cv2

image = cv2.imread(r"C:\Users\basel.abdella\PycharmProjects\PythonProject1\butterfly.jpg")

(h,w) = image.shape[:2]

new_w = int(w*0.5)
new_h = int(h*0.5)
new_w1 = int(w*2)
new_h1 = int(h*2)

scaled_image = cv2.resize(image,(new_w,new_h))
scaled_image1 = cv2.resize(image,(new_w1,new_h1))

cv2.imshow("image",image)
cv2.imshow("scaled",scaled_image)
cv2.imshow("scaled1",scaled_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
