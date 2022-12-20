import cv2
import matplotlib.pyplot as plt

image = cv2.imread('bird.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.IMREAD_GRAYSCALE 을 통해 사진을 읽어들이면, Gray색상으로 사진을 읽어들인다는 것을 확인하였다.
cv2.imshow('Image Basic',image)
cv2.waitKey(0)