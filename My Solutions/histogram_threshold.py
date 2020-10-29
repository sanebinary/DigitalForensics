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
plt.savefig('histogram.png')
plt.show()