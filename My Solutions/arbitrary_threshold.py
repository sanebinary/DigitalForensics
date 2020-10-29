import cv2 as cv
import sys

forme1 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme1.png", 0)
house8 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/house8.png", 0)
woman = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/femme.png", 0)

ret,thresh1 = cv.threshold(forme1, 200, 255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(house8, 200, 255, cv.THRESH_BINARY)
ret,thresh3 = cv.threshold(woman, 200, 255, cv.THRESH_BINARY)

cv.imwrite("forme1_thresh.png", thresh1)
cv.imwrite("house8_thresh.png", thresh2)
cv.imwrite("woman_thresh.png", thresh3)

ret,thresh1 = cv.threshold(forme1, 127, 255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(house8, 127, 255, cv.THRESH_BINARY)
ret,thresh3 = cv.threshold(woman, 127, 255, cv.THRESH_BINARY)

cv.imwrite("forme1_thresh_127.png", thresh1)
cv.imwrite("house8_thresh_127.png", thresh2)
cv.imwrite("woman_thresh_127.png", thresh3)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()