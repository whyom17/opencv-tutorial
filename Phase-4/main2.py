# Saving Video 

import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # fetching width
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # fetching height

codec = cv2.VideoWriter_fourcc(*'XVID')  # creates a FourCC code (a 4-character code) used to specify the video compression format.
# 'mp4v' – MPEG-4 codec for .mp4 files

recorded = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width,frame_height))

while True:
        
    success, image = cap.read()
    
    if not success:
        break
    
    recorded.write(image)  # compresses and stores each image as the next frame in your video file
    cv2.imshow("Recording Live", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
recorded.release()
cv2.destroyAllWindows()
    
    