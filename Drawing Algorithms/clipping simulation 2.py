import cv2
import numpy as np

# Create a white canvas
img = np.ones((400, 400, 3), np.uint8) * 255

# Draw the rectangle
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 2)

# Define rectangle bounds
x_min, y_min, x_max, y_max = 100, 100, 300, 300

# Blue diagonal line (initial values)
x1, y1, x2, y2 = 50, 50, 350, 350

# Clip line to rectangle bounds
x1 = max(x1, x_min)
y1 = max(y1, y_min)
x2 = min(x2, x_max)
y2 = min(y2, y_max)

# Draw the clipped blue line
cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Red vertical line (initial values)
x1, y1, x2, y2 = 150, 50, 150, 350

# Clip line to rectangle bounds
x1 = max(x1, x_min)
y1 = max(y1, y_min)
x2 = min(x2, x_max)
y2 = min(y2, y_max)

# Draw the clipped red line
cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the final image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()