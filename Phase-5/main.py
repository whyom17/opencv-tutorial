# Image Filtering & Blurring

import cv2
import numpy as np

# Different Blurs
img1= cv2.imread("Phase-5\stephen_curry.webp")

blur= cv2.blur(img1 , (5,5))
blur_gaussian= cv2.GaussianBlur(img1 , (5,5) , 0)
blur_median= cv2.medianBlur(img1 , 5)

# Gaussian Blur is smoother and more natural-looking than classical (box) blur.

# Rule of Thumb :
# If you're manually choosing sigma, let OpenCV figure out kernel size.
# If you're manually choosing kernel size, leave sigma = 0.

cv2.imshow("Original Image", img1)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian Blur", blur_gaussian)
cv2.imshow("Median Blur", blur_median)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Noise Reduction
img2= cv2.imread("Phase-5\cow-salt-peper.png")

blur= cv2.blur(img2 , (7,7))
blur_gaussian= cv2.GaussianBlur(img2 , (7,7) , 0)
blur_median= cv2.medianBlur(img2 , 7)  # better than others for noise reduction

cv2.imshow("Original Image", img2)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian Blur", blur_gaussian)
cv2.imshow("Median Blur", blur_median)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Sharpening
img3= cv2.imread("Phase-5\minecraft.webp")

kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]])

sharpened = cv2.filter2D(img3, -1, kernel)

cv2.imshow("Original Image", img3)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()