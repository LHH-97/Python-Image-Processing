import cv2
import matplotlib.pyplot as plt

image_1 = cv2.imread('bird.jpg')
image_2 = cv2.imread('sea.jpg')
image_3 = cv2.resize(image_1,dsize = (1280,853),interpolation = cv2.INTER_AREA)
#image_1 과 image_2의 픽셀크기가 달라 두 image를 합칠수 없었고,cv2.resize로 픽셀크기를 변경하였다.

print(image_3.shape,image_1.size)
print(image_2.shape,image_2.size)

result = cv2.add(image_3,image_2)
plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
plt.show()

result = image_3+image_2
plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
plt.show()
