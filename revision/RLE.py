import cv2
import numpy as np


# Function for Run-Length Encoding
def run_length_encode(data):
    compressed = []
    current_value = data[0]
    count = 1

    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = value
            count = 1

    compressed.append((current_value, count))
    return compressed


# Load an image (grayscale for simplicity)
image_path = r"/lo6/butterfly.jpg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found. Please check the path.")
else:
    # Flatten the image row-wise
    flattened = img.flatten()

    # Apply Run-Length Encoding (RLE)
    rle_result = run_length_encode(flattened)

    # Print some of the RLE result to keep it concise
    print("Run-Length Encoding Result (first 100 values):")
    print(rle_result[:100])

    # Display the original image
    cv2.imshow("Original Image", img)

    # Wait and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
