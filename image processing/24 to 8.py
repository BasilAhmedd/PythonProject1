import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread(r"C:\Users\basel.abdella\PycharmProjects\PythonProject1\butterfly.jpg")

# Ensure the image is loaded successfully
if image is None:
    print("Error: Image could not be loaded. Check the file path.")
    exit()

grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)





# Display the images
cv2.imshow("Grey", grey_image)
cv2.imshow("original", image)

# Wait for a key press and close the display windows
cv2.waitKey(0)
cv2.destroyAllWindows()
