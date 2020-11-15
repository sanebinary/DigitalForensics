import cv2
import numpy as np
from matplotlib import pyplot as pyplot

#Harris Corner Detection
susie = cv2.imread("../SHARED_DigitalForensics/Labworks/LabWork_2/susie.png")
gray = cv2.cvtColor(susie,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None)
susie[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',susie)

#SIFT:
lena = cv2.imread("../SHARED_DigitalForensics/Labworks/LabWork_2/lena.png")
gray2 = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp = sift.detect(lena, None)
lena2 = cv2.drawKeypoints(gray2, kp, lena)
cv2.imshow("Lena", lena)

key = cv2.waitKey(0)
if key == ord("q"):    
    sys.exit(0)
