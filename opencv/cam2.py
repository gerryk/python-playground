import cv2.cv as cv
import cv2
cv2.namedWindow("camera", 0)
capture = cv.CaptureFromCAM(0)
while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    if cv.WaitKey(10) == 27:
        break
        cv.DestroyAllWindows()
