# Basic Image Drawing Techniques

import cv2

image = cv2.imread("Phase-3/ukulele.png") # or "Phase-3\\ukulele.png"

# here we can't use "Phase-3\ukulele.png" as python interprets '\u' as Unicode escape sequence and it will throw a syntax error
# \uXXXX represents a Unicode character, where XXXX is a 4-digit hexadecimal number.
# print("\u00A9")  # Output: ©

print(image.shape)

# draw line
pt1= (50,200)
pt2= (250,40)

cv2.line(image, pt1, pt2, (0,0,255), 2)  # (B,G,R)

# draw rectangle
pt3= (100,205)
pt4= (165,270)

cv2.rectangle(image, pt3, pt4, (255,0,0), 2)

# draw circle
cv2.circle(image, (135,235), 20, (0,255,0), 2)

# labelling / adding text

text = "I play uke sometimes😉"  # doesn't interpret emojis

#text = "I play \nuke sometimes \n😉"  --- doesn't understand escape sequences

# text = """I play   --- also doesn't work
# uke sometimes
# 😉
# """

cv2.putText(image, text, (150,320), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1 )

cv2.imshow("Ukulele", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
