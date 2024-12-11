import cv2
import numpy as np
from scipy.signal import wiener
from matplotlib import pyplot as plt

# Step 1: Load the Image
# Replace with the path to your image
image_path = "D:/OIP.jpg"  # Example input image path
bgr_image = cv2.imread(image_path)  # Read image in its original color format

if bgr_image is None:
    print(f"Error: Unable to load the image from {image_path}. Ensure the file exists.")
    exit()

# Step 2: Convert the Image to YUV Color Space
yuv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2YUV)

# Step 3: Extract the Y (luminance) Channel
y_channel = yuv_image[:, :, 0]  # Luminance/brightness data for further processing

# Step 4: Apply Wiener Filtering to the Y Channel
# Wiener filter on the Y channel to reduce noise
# Note: Ensure the Y channel is casted to float to avoid overflow/precision issues
y_channel_denoised = wiener(y_channel.astype(float), (5, 5))  # Filter size set to 5x5
y_channel_denoised = np.clip(y_channel_denoised, 0, 255).astype(np.uint8)  # Convert back to uint8

# Step 5: Perform Histogram Equalization on the Denoised Y Channel
y_channel_enhanced = cv2.equalizeHist(y_channel_denoised)

# Step 6: Reduce Brightness in the Enhanced Image
brightness_factor = 0.8  # Reduce brightness by multiplying the Y channel by 0.8 (adjustable)
y_channel_enhanced = np.clip(y_channel_enhanced * brightness_factor, 0, 255).astype(np.uint8)

# Step 7: Replace the Original Y Channel with the Enhanced One in YUV Image
yuv_image[:, :, 0] = y_channel_enhanced  # Replace the processed Y channel

# Step 8: Convert the Processed YUV Image Back to BGR Color Space
enhanced_bgr_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

# Step 9: Display and Compare Results
plt.figure(figsize=(15, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.title("Original Image (BGR)")
plt.imshow(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
plt.axis("off")

# Wiener Filtered Image
plt.subplot(1, 3, 2)
plt.title("Denoised Image (Wiener Filter)")
plt.imshow(y_channel_denoised, cmap='gray')  # Show the Wiener-filtered Y channel
plt.axis("off")

# Enhanced (Final) Image
plt.subplot(1, 3, 3)
plt.title("Enhanced Image with Reduced Brightness")
plt.imshow(cv2.cvtColor(enhanced_bgr_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
plt.axis("off")

plt.tight_layout()
plt.show()

