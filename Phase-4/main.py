# Working with Video & Webcam

import cv2

cap = cv2.VideoCapture(0)  # uses default webcam

while True :
    a=cap.read()
    print(a)
    
    ret, frame= cap.read()   # (True, array(...))
    
    if not ret:
        print ("Could not read frame")
        break
    
    cv2.imshow("WebCam Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):   # Adds a minimum delay of 1 millisecond per iteration
        #  ord('q')- Converts the character 'q' to its ASCII value, which is 113.
        # & 0xFF (bitwise AND operation)
        # 0xFF = 11111111 in binary (i.e. 255)
        # Bit Masking it with the keycode returned by waitKey()
        
        print("Quitting ...")
        break

cap.release()   # Releases the webcam for other apps to use
cv2.destroyAllWindows()

# ONE OF THE FRAMES READ BY WEBCAM EVERY 1 ms

# #(True, array([[[183, 175, 158],
#         [183, 175, 159],
#         [183, 173, 159],
#         ...,
#         [243, 244, 240],
#         [243, 244, 240],
#         [243, 244, 240]],

#        [[185, 176, 159],
#         [185, 176, 160],
#         [184, 174, 160],
#         ...,
#         [243, 244, 240],
#         [243, 244, 240],
#         [243, 244, 240]],

#        [[188, 178, 161],
#         [188, 178, 162],
#         [186, 176, 162],
#         ...,
#         [243, 244, 240],
#         [243, 244, 240],
#         [243, 244, 240]],

#        ...,

#        [[110,  60,  60],
#         [108,  58,  58],
#         [105,  55,  55],
#         ...,
#         [ 58,  34,  41],
#         [ 58,  37,  43],
#         [ 57,  38,  44]],

#        [[108,  61,  60],
#         [106,  59,  58],
#         [104,  57,  56],
#         ...,
#         [ 57,  34,  42],
#         [ 56,  35,  44],
#         [ 56,  36,  45]],

#        [[107,  62,  61],
#         [105,  60,  59],
#         [105,  60,  59],
#         ...,
#         [ 56,  33,  42],
#         [ 55,  34,  43],
#         [ 56,  35,  45]]], shape=(480, 640, 3), dtype=uint8))

#Key Insight:
# cv2.waitKey(1) does not set the frame capture rate to 1000 frames per second.
# That 1 ms delay is just a minimum pause that OpenCV uses to:
# - Allow GUI events like keypresses.
# - Let your system breathe between frame updates.

# It’s important to note: it doesn’t actively check for a new photo every 1 ms. 
# Instead, your loop structure is constantly reading frames as fast as the system allows — and waitKey(1) just gives it breathing room between iterations.

# waitKey(1)- returns -1 {if no key is pressed}
#           - returns a keycode/ ASCII value of that key {if key is pressed} 
