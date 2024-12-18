import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern

# Load the grayscale image
image_path = "butterfly.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image has been loaded properly
if image is None:
    raise FileNotFoundError(f"Image at path '{image_path}' could not be loaded. Please check the file path.")

# LBP parameters
radius = 1
n_points = 8 * radius

# Compute the LBP
lbp = local_binary_pattern(image, n_points, radius, method="uniform")

# Compute the LBP histogram
lbp_hist, _ = np.histogram(
    lbp.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2)
)

# Normalize the histogram
lbp_hist = lbp_hist.astype("float")
lbp_hist /= (lbp_hist.sum() + 1e-6)  # Prevent division by zero with a small constant

# Plot the original image, LBP image, and the histogram
plt.figure(figsize=(15, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# LBP Image
plt.subplot(1, 3, 2)
plt.imshow(lbp, cmap='gray')
plt.title("LBP Image (After Effect)")
plt.axis('off')

# LBP Histogram
plt.subplot(1, 3, 3)
plt.bar(range(len(lbp_hist)), lbp_hist, width=0.7, align='center', color='blue', alpha=0.7)
plt.title("LBP Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency (Normalized)")
plt.xticks(range(len(lbp_hist)))
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()
