import cv2 as cv
import numpy as np
img = cv.imread('../SHARED_DigitalForensics/Labworks/LabWork_3/cadastre2.png',0)
kernel = np.ones((10,10),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow("Dilation", dilation)
cv.imwrite("thickest_extract.png", dilation)
kernel = np.ones((11,11),np.uint8)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow("Erosion", blackhat)
cv.imwrite("thinnest_extract.png", blackhat)
key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()