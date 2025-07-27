# Image Transformations & Manipulation

import cv2

image= cv2.imread("Phase-2\hearts.png")

print(image.shape)

#resizing
resized= cv2.resize(image,(550,550))

cv2.imshow("Resized Heart", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cropping / slicing / numpy slicing
cropped= image[74:150,74:150]
cv2.imshow("Cropped Heart", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image rotation and flipping
M = cv2.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), 45, 1)    # (centre,angle,scale)
rotated = cv2.warpAffine(image, M, (image.shape[0],image.shape[1]))

cv2.imshow("Rotated Hearts", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# flipped= cv2.flip("rotated", 0) ---- won't work as it accepts originally loaded image
flipped= cv2.flip(image, 0)

cv2.imshow("Flipped Hearts", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
