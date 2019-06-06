import numpy as np
import cv2 as cv
from tracker.centroidtracker import CentroidTracker
from tracker.trackableobject import TrackableObject
import imutils
from imutils.video import WebcamVideoStream

# fourcc = cv.VideoWriter_fourcc('m','j','p','g')

fourcc = cv.VideoWriter_fourcc('M','J','P','G')
# cap = cv.VideoCapture(r"C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\2.mp4")
cap = cv.VideoCapture(1 + cv.CAP_DSHOW)
# cap = cv.VideoCapture(1)

cap.set(cv.CAP_PROP_FOURCC, fourcc)
# #Decrease frame size
# # cap.set(5, 10)
cap.set(cv.CAP_PROP_FPS, 120)
# # cap.set(cv.CAP_PROP_EXPOSURE, -7 )
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# vs = WebcamVideoStream(src=1).start()
out = cv.VideoWriter(r'C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\outpy3.mp4',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height),True)

while(1):
    rec,frame = cap.read()
    fps = cap.get(cv.CAP_PROP_FPS)
    # cv.imwrite(r"C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\2_"+str(i)+".jpg",frame)
    # i+=1
    out.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(30) & 0xff ==ord("q"):
        break

cap.release()
out.release()
# vs.stop()
cv.destroyAllWindows()