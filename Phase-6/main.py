# Edge Detection & Thresholding

import cv2
import numpy as np

img = cv2.imread('Phase-6/tulip.jpg', 0) # grayscale image

# Edge Detection

edges = cv2.Canny(img, 40, 130) # Canny Edge Detection (img , threshold1, threshold2)
# below threshold1 (REJECTED)=> convert to 0 (black)
# above threshold2 (STRONG EDGE)=> convert to 255 (white)
# between threshold1 and threshold2 (WEAK EDGE)=> kept only if connected to a 'strong edge'

# Why Two Thresholds?
# Using two thresholds:
# - Reduces false positives (from noise)
# - Preserves real edges (even if slightly weak)
# - Makes edge detection more robust and clean

cv2.imshow('Original Image', img)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Thresholding

img = cv2.imread('Phase-6/tulip.jpg', 0) # grayscale image

print(cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)) # returns threshold value and thresholded image
# cv2.THRESH_BINARY: Pixels above 127 become 255 (white), and equal and below to it become 0

ret, threshold = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', img)
cv2.imshow('Thresholded', threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Bitwise Operations

img1 = np.zeros((300, 300), dtype='uint8')
img2 = np.zeros((300, 300), dtype='uint8') 

cv2.circle(img1, (120, 150), 100, 255, -1) # Draw a filled circle on img1
cv2.rectangle(img2, (80, 50), (28 0, 250), 255, -1) # Draw a filled rectangle on img2

bitwise_and = cv2.bitwise_and(img1, img2) # AND operation
bitwise_or = cv2.bitwise_or(img1, img2)  # OR operation
bitwise_not =cv2.bitwise_not(img1) # NOT operation 

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise NOT', bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows() 