import cv2 as cv
import numpy as np
img = cv.imread('../SHARED_DigitalForensics/Labworks/LabWork_3/cadastre1.png',0)
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(thresh1, cv.MORPH_OPEN, kernel)
cv.imshow("Opening", thresh1)
cv.imwrite("text_extract_open.png", opening)
key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()