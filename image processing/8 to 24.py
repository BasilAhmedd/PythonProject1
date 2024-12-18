import cv2
import numpy as np

# Load the grayscale image
grayscale_image = cv2.imread(r"/lo6/butterfly.jpg",
                             cv2.IMREAD_GRAYSCALE)

# Ensure the image is loaded successfully
if grayscale_image is None:
    print("Error: Image could not be loaded. Check the file path.")
    exit()

# Convert grayscale to RGB
rgb_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2RGB)

# Set the blue and green channels to 0 (creating an "R-only" effect)
rgb_image[:, :, 0] = 128
# rgb_image[:, :, 1] = 0
rgb_image[:, :, 2] = 64

bgr_image_for_display = cv2.cvtColor(rgb_image,cv2.COLOR_BGR2RGB)


# Display the images
cv2.imshow("Grey", grayscale_image)
cv2.imshow("RGB (Red Only)", rgb_image)

# Wait for a key press and close the display windows
cv2.waitKey(0)
cv2.destroyAllWindows()
