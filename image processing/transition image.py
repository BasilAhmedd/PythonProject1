import cv2
import numpy as np

# Load the image
image = cv2.imread(r"/lo6/butterfly.jpg")

if image is None:
    print("Error: Image could not be loaded. Check the file path.")
    exit()

rows, cols = image.shape[:2]

# Translation values
t_x = 500
t_y = 50

translation_matrix = np.float32([[1, 0, t_x], [0, 1, t_y]])

translated_image = cv2.warpAffine(image, translation_matrix, (cols + t_x, rows + t_y))

cv2.imshow("Original", image)
cv2.imshow("Translated", translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
