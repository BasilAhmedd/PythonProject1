import cv2
import imutils

# Load the image
image = cv2.imread(r"C:\Users\basel.abdella\PycharmProjects\PythonProject1\butterfly.jpg")

if image is None:
    print("Error: Image could not be loaded. Check the file path.")
    exit()

rotated = imutils.rotate(image , 180)

cv2.imshow("Original", image)
cv2.imshow("rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
