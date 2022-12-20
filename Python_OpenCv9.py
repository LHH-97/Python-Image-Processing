import cv2
import matplotlib.pyplot as plt

image = cv2.imread('sea.jpg', cv2.IMREAD_GRAYSCALE)
#OpenCv의 GRAYSCALE이란?
images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) #임계값 127을 넘어가면 픽셀값을 255로.
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_GRAY2RGB))
    plt.show()
