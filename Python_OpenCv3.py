import cv2
import matplotlib.pyplot as plt
import time
#opencv 활용해 특정 범위 픽셀 변경
image = cv2.imread('puppy.jpg')
start_time = time.time()
#개별적인 픽셀 일일히 접근
for i in range(0,100):
    for j in range(0,100):
        image[i,j] = [255,255,255]
print("---%s seconds ---" %(time.time() - start_time))


start_time1 = time.time()
#범위 지정해 그 값을 동일한 값으로 채워 넣는 방법.
image[0:100,0:100] = [0,0,0]
print("---%s seconds --- "%(time.time() - start_time1))
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

#두 연산 모두 특정 범위의 픽셀값들을 바꾸지만 아래쪽이 훨씬 빠르게 수행되었다... 아래쪽은 0.0