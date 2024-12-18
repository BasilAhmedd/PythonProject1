import cv2
import numpy as np

# Create a white image
img = np.ones((512, 512, 3), np.uint8) * 255

# Define the center, radius, color, and thickness of the circle
center = (256, 256)  # Center of the circle (x, y)
radius = 100  # Radius of the circle
color = (0, 255, 255)  # Yellow (BGR format)
thickness = 20  # Thickness of the circle's outline (-1 for filled circle)

# Draw the circle
cv2.circle(img, center, radius, color, thickness)

# Display the image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
