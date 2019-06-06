import numpy as np
import cv2 as cv
from tracker.centroidtracker import CentroidTracker
from tracker.trackableobject import TrackableObject
import imutils
from imutils.video import WebcamVideoStream



def FindPoint(x1, y1, x2, y2, x, y) : 
    if (x > x1 and x < x2 and 
        y > y1 and y < y2) : 
        return True
    else : 
        return False
# fourcc = cv.VideoWriter_fourcc('m','j','p','g')

fourcc = cv.VideoWriter_fourcc('M','J','P','G')
cap = cv.VideoCapture(r'C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\2.mp4')
# cap = cv.VideoCapture(1 + cv.CAP_DSHOW)

cap.set(cv.CAP_PROP_FOURCC, fourcc)
# #Decrease frame size
# # cap.set(5, 10)
# cap.set(cv.CAP_PROP_FPS, 120)
# # cap.set(cv.CAP_PROP_EXPOSURE, -7 )
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# vs = WebcamVideoStream(src=1).start()

fgbg = cv.createBackgroundSubtractorMOG2()
kernel_dil = np.ones((20,20),np.uint8)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))

ct = CentroidTracker()
trackableObjects = {}
# 418 37
# 1357 86
# 429 814
# 1405 750
totalHit = 0
WaitingFrame = 0
i = 0
# (H, W) = (1600, 869)
(H, W) = (1920, 1080)

while(1):
    rec,frame = cap.read()
    fps = cap.get(cv.CAP_PROP_FPS)
    print("fps = " + str(fps))
    # Fourcc = cap.get(cv.CAP_PROP_FOURCC)
    # print("fourcc = " + str(Fourcc))
    # WaitingFrame += 1
    # if WaitingFrame > 1 : 
    #     # if W is None or H is None:
    #     #     (H, W) = frame.shape[:2]
        
    #     # cv.circle(frame, (155, 120), 5, (0, 0, 255), -1)
    #     # cv.circle(frame, (480, 120), 5, (0, 0, 255), -1)
    #     # cv.circle(frame, (20, 475), 5, (0, 0, 255), -1)
    #     # cv.circle(frame, (620, 475), 5, (0, 0, 255), -1)

    #     # pts1 = np.float32([[418,37], [1357,86], [429,814], [1405,750]])
    #     # pts2 = np.float32([[0, 0], [1920, 0], [0, 1080], [1920, 1080]])
    #     # matrix = cv.getPerspectiveTransform(pts1, pts2)

    #     # frame = cv.warpPerspective(frame, matrix, (1920, 1080))

    #     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #     gray = cv.bilateralFilter(gray, 11, 17, 17)
    #     edged = cv.Canny(gray, 5, 20)
    rects = []
    #     # cnts = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #     # cnts = imutils.grab_contours(cnts)
    #     # cnts = sorted(cnts, key = cv.contourArea, reverse = True)[:10]
    #     # screenCnt = None
    #     # for c in cnts:  
    #     #     peri = cv.arcLength(c, True)
    #     #     cv.drawContours(frame, [c], -1, (0, 255, 0), 3)
    #     #     approx = cv.approxPolyDP(c, 0.015 * peri, True)
    #     #     if (len(approx) == 4):
    #     #         screenCnt = approx
    #     #         break

        
    if rec == True:
        fgmask = fgbg.apply(frame)
        fgmask[fgmask==127]=0
        fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
        dilation = cv.dilate(fgmask,kernel_dil,iterations=1)
        (contours,hierarchy) = cv.findContours(dilation,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area = cv.contourArea(contour)
            if(area> 700):
                x,y,w,h = cv.boundingRect(contour)
                # rects.append(cv.boundingRect(contour))
                # print("x and y: "+ str(x) +" "+ str(y))
                w = w*2
                h = h*2
                rects.append((x,y,w,h))
                img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                roi_bullet = frame[y:y+h,x:x+w]
                cv.imwrite(r"C:\Users\Nuttaphon\Documents\NerfGun\TestWithBrio_27_05_19\2_Object_"+str(i)+".jpg",roi_bullet)
                i+=1
            pass

        # objects = ct.update(rects)

    #         # cv.rectangle(frame, (685, 222), (819, 575),(0,255,0),2)
    #         # # cv.rectangle(frame, (200, 200), (900, 600),(0,255,0),2)
    #         # for (objectID, centroid) in objects.items():
                
    #         #     TrackObject = trackableObjects.get(objectID, None)

    #         #     if TrackObject is None:
    #         #         TrackObject = TrackableObject(objectID, centroid)
    #         #     else: 
    #         #         y = [c[1] for c in TrackObject.centroids]
    #         #         direction = centroid[1] - np.mean(y)
    #         #         TrackObject.centroids.append(centroid)
    #         #         if not TrackObject.counted:
    #         #             # totalHit += 1
    #         #             # TrackObject.counted = True
    #         #             print("x and y: "+ str(centroid[0]) +" "+ str(centroid[1]))
    #         #             if  (FindPoint(685, 222, 819, 575, centroid[0], centroid[1])) :
    #         #                 totalHit += 1
    #         #                 TrackObject.counted = True

    #         #     trackableObjects[objectID] = TrackObject
    #         #     text = "ID {}".format(objectID)
    #         #     cv.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
    #         #         cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    #         #     cv.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

    #     info = [
    #         ("Score: ", totalHit),
    #     ]
    #     for (i, (k, v)) in enumerate(info):
    #         text = "{}: {}".format(k, v)
    #         cv.putText(frame, text, (10, 800 - ((i * 20) + 20)),cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv.imshow('frame',frame)
    if cv.waitKey(30) & 0xff ==ord("q"):
        break

cap.release()
# vs.stop()
cv.destroyAllWindows()