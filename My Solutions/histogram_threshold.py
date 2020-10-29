import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
forme1 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme1.png", 0)
house8 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/house8.png", 0)
woman = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/femme.png", 0)
forme3 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme3.png", 0)

plt.subplot(3,3,1),plt.hist(forme1.ravel(), 256, [0, 256])
plt.subplot(3,3,2),plt.hist(house8.ravel(), 256, [0, 256])
plt.subplot(3,3,3),plt.hist(woman.ravel(), 256, [0, 256])
plt.subplot(3,3,4),plt.hist(forme3.ravel(), 256, [0, 256])

forme1 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme1.png", 0)
house8 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/house8.png", 0)
woman = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/femme.png", 0)
forme3 = cv.imread("../SHARED_DigitalForensics/Labworks/LabWork_3/forme3.png", 0)

ret,thresh1 = cv.threshold(forme1, 125, 255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(house8, 100, 255, cv.THRESH_BINARY)
ret,thresh3 = cv.threshold(woman, 60, 255, cv.THRESH_BINARY)
ret,thresh4 = cv.threshold(forme3, 90, 255, cv.THRESH_BINARY)

cv.imwrite("forme1_thresh_histogram.png", thresh1)
cv.imwrite("house8_thresh_histogram.png", thresh2)
cv.imwrite("woman_thresh_histogram.png", thresh3)
cv.imwrite("forme3_thresh_histogram.png", thresh4)


key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()
plt.savefig('histogram.png')
plt.show()