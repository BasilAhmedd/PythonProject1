import cv2
from skimage.restoration import denoise_tv_chambolle

image = cv2.imread(r"/lo6/butterfly.jpg", cv2.IMREAD_GRAYSCALE)

lambda_range = 0.1

tv_denoised = denoise_tv_chambolle(image, weight=lambda_range)
cv2.imshow("Original", image)
cv2.imshow("TV Regularized", tv_denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()