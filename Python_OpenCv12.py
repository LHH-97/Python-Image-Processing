#OpenCv 도형 그리기.
import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
image = np.full((512,512,3),255,np.uint8)

image = cv2.line(image,(0,0),(255,255),(255,0,0),3)
#(0,0)부터 (255,255)까지 일자로 선을 긋고, 색깔은 R G B로 해서 빨강 값을 255로 만든것.
#matplotlib는 RGB 형식을 따르고,(255가 첫번째 이기에 빨강이 255이다.) 마지막 두께는 3이다.
plt.imshow(image)
plt.show()
'''
image = np.full((512,512,3),255,np.uint8)
image = cv2.rectangle(image,(20,20),(255,255),(255,0,0),3)

plt.imshow(image)
plt.show()