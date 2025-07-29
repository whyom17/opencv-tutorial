# Colorspaces

import cv2

img = cv2.imread("Phase-5\parrot.webp")  # Load the image in BGR format

# Switiching BGR  to RGB Colorspace
img_rgb =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Converting BGR to Grayscale
# Grayscale is a single channel image, where each pixel represents the intensity of light.
img_gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Hue, Saturation, Value
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original Image", img)
cv2.imshow("RGB Image", img_rgb)
cv2.imshow("GRAY Image", img_gray)
cv2.imshow("HSV Image", img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()