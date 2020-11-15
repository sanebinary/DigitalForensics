import cv2
import numpy as np
from matplotlib import pyplot as plt

#Harris Corner Detection
susie1 = cv2.imread("../SHARED_DigitalForensics/Labworks/LabWork_2/susie.png", 0)
susie2 = cv2.imread("../SHARED_DigitalForensics/Labworks/LabWork_2/susie.png", 0)

# Initiate SIFT detector
sift = cv2.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(susie1,None)
kp2, des2 = sift.detectAndCompute(susie2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(susie1,kp1,susie2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3),plt.show()