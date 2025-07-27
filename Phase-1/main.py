# Basic Operation & Grayscale Conversion

import cv2

image = cv2.imread("Phase-1/daredevil.png")
image2 = cv2.imread("Phase-1/daredevil.png",0)   # direct grayscale conversion

cv2.imshow("Daredevil", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

success= cv2.imwrite("daredevil.jpg", image)

if success:
    print("image saved successfully")
else:
    print("failed")
    
print(image.shape)   
print(image2.shape)

print(image[150][125])   # gives the RGB 3d vector of that pixel

# grayscale conversion
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)