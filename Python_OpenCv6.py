#image 크기 조절
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('puppy.jpg')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))#matplotlib에서 image 출력하기 위해 BGR을 RGB형식으로 바꿔준다.
plt.show()
print(image.shape)
expand = cv2.resize(image,None,fx = 2.0,fy = 2.0,interpolation = cv2.INTER_CUBIC)#사이즈를 크게.
plt.imshow(cv2.cvtColor(expand,cv2.COLOR_BGR2RGB))
plt.show()

shrink = cv2.resize(image,None,fx = 0.8,fy = 0.8,interpolation = cv2.INTER_AREA)#사이즈 작게
plt.imshow(cv2.cvtColor(shrink,cv2.COLOR_BGR2RGB))
plt.show()
