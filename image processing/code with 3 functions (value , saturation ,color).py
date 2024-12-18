import cv2
import numpy as np


def adjust_hue(image, hue_shift):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue_channel = hsv_image[:, :, 0]
    hue_channel = (hue_channel + hue_shift) % 180  # Wrap around hue values
    hsv_image[:, :, 0] = hue_channel
    return hsv_image


def adjust_value(hsv_image, value_increase):

    value_channel = hsv_image[:, :, 2]
    value_channel = np.clip(value_channel + value_increase, 0, 255)
    hsv_image[:, :, 2] = value_channel
    return hsv_image


def adjust_saturation(hsv_image, saturation_scale):

    saturation_channel = hsv_image[:, :, 1]
    saturation_channel = np.clip(saturation_channel * saturation_scale, 0, 255)
    hsv_image[:, :, 1] = saturation_channel
    return hsv_image


# Main script
if __name__ == "__main__":
    image = cv2.imread(r"/lo6/butterfly.jpg")
    if image is None:
        print("Error: Image not found.")
        exit()

    # Step 1: Adjust hue
    hsv_image = adjust_hue(image, hue_shift=30)

    # Step 2: Adjust value (brightness)
    hsv_image = adjust_value(hsv_image, value_increase=50)

    # Step 3: Adjust saturation
    hsv_image = adjust_saturation(hsv_image, saturation_scale=1.5)

    # Convert back to BGR for display
    modified_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Display original and modified images
    cv2.imshow("Original", image)
    cv2.imshow("Modified", modified_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
