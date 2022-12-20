import cv2
import matplotlib.pyplot as plt
#OpenCv를 활용한 ROI(관심있는 부분) 추출

image = cv2.imread('puppy.jpg')
roi = image[200:350,50:400] # 이 부분이 관심있는 부분 (roi).
#x(행)부분 200~300 즉 높이를 의미, y(열)부분 50~200 너비부분의 범위.
image[0:150,0:350] = roi
#범위가 달라지면 오류발생. 복사한 크기와 붙여넣기하는 크기가 같아야 한다.
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()