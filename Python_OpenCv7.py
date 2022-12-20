:quit()#이미지 위치 변경
import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
image = cv2.imread('puppy.jpg')

height,width = image.shape[:2]

M = np.float32([[1,0,50],[0,1,10]])
#여기서의 x는 열을 의미한다. right로 50만큼 이동. ,아래쪽으로 10만큼.
dst = cv2.warpAffine(image,M,(width,height))
cv2.imshow('Image',dst)
cv2.waitKey(0)
'''
#이미지 회전 Affine 변환하나로 이미지 회전 취할 수있다.
image = cv2.imread('puppy.jpg')
height,width = image.shape[:2]

M = cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
#너비(x축)의 중간, 높이의 중간,angle(회전 각도)를 90(반시계 방향), scale 값 = 0.5 크기를 반으로 줄임

dst = cv2.warpAffine(image,M,(width,height))

plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.show()
