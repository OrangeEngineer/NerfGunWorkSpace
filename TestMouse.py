import cv2
import numpy as np

ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ix,iy = x,y
        print(ix,iy)

# Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
#Decrease frame size
cap.set(3, 1920)
#cv2.CAP_PROP_FRAME_WIDTH
cap.set(4, 1080)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    ret, frame = cap.read()
    cv2.imshow('image',frame)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(ix,iy)
cap.release()
cv2.destroyAllWindows()