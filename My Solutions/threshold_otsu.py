import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
forme1 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme1.png", 0)
lena = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_2/lena.png", 0)
forme3 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme3.png", 0)

ret1, thresh1 = cv.threshold(forme1, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
ret2, thresh2 = cv.threshold(lena, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
ret3, thresh3 = cv.threshold(forme3, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imwrite("forme1_otsu.png", thresh1)
cv.imwrite("lena_otsu.png", thresh2)
cv.imwrite("forme3_otsu.png",thresh3)
print(ret1,ret2,ret3)