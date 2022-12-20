import cv2
#OpenCv를 활용한 이미지 크기 및 픽셀 정보 확인

image = cv2.imread('puppy.jpg')
#픽셀 수 및 이미지 크기 확인
print(image.shape) #높이 1080픽셀,너비 1440픽셀
print(image.size)
#이미지 Numpy 객체의 특정 x축의 y축의 픽셀을 가져올수 있다. 즉 px는 하나의 픽셀에 대한 정보
px = image[100,100]
#B G R 순서로 출력된다.
print(px)
#R값만 출력하기
print(px[2])