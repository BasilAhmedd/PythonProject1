# import cv2
# import numpy as np
#
# img = np.ones((512,512,3),np.uint8)*255
#
# start_point = (100,100)
# end_point = (400,400)
# color = (0,255,255)
# thickness = 20
# cv2.line(img,start_point,end_point,color,thickness)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Create a white image
img = np.ones((512, 512, 3), np.uint8) * 255

# Define the color (BGR format) and thickness of the lines
color = (0, 255, 255)  # Yellow
thickness = 20

# Draw the first diagonal line (top-left to bottom-right)
start_point1 = (100, 100)
end_point1 = (400, 400)
cv2.line(img, start_point1, end_point1, color, thickness)

# Draw the second diagonal line (top-right to bottom-left)
start_point2 = (400, 100)
end_point2 = (100, 400)
cv2.line(img, start_point2, end_point2, color, thickness)

# Display the image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
