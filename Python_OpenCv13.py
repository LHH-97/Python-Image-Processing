
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('sea.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)#127보다 큰값은-->255,그렇지 않은 값은-->0

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()
#입력이 되는 image는 GrayScale Threshold 전처리 과정이 필요하다.

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
#기존 강의의 코드에서 [0]부분과 같이 수정해주었다. OpenCv의 버전이 바뀌어 나타나는 오류인것 같다.
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4) # -1: 모든 Contour 다 그리기.,0:첫번째 contour 출력

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()