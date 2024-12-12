import cv2

salted_image = cv2.imread(r'C:\Users\basel.abdella\PycharmProjects\PythonProject1\sp_img_gray_noise_heavy.png')
if salted_image is None:
    print("Error: Image not found or could not be loaded.")
    exit()

denoised_image5 = cv2.medianBlur(salted_image, ksize=5)
denoised_image3 = cv2.medianBlur(salted_image, ksize=3)
denoised_image7 = cv2.medianBlur(salted_image, ksize=7)
denoised_image9 = cv2.medianBlur(salted_image, ksize=9)

cv2.imshow("Original", salted_image)
cv2.imshow("Filtered 5", denoised_image5)
cv2.imshow("Filtered 7", denoised_image7)
cv2.imshow("Filtered 9", denoised_image9)
cv2.imshow("Filtered 3", denoised_image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
