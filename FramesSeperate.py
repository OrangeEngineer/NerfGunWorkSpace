import numpy as np
import cv2

cap = cv2.VideoCapture(r"C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\2.mp4")
i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame1
    cv2.imwrite(r"C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\2_"+str(i)+".jpg",frame)
    i+=1
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()