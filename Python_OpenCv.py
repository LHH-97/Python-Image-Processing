import cv2
#opencv는 BGR 형태로 데이터 표현되고,처리된다(not RGB). numpy객체 형태로
img_basic  = cv2.imread('puppy.jpg',cv2.IMREAD_COLOR)
#imread함수는 image를 읽어 numpy객체로 만드는 함수.
cv2.imshow('Image Basic',img_basic)#화면에 보여주고자 imshow함수 이용
cv2.waitKey(0)#이미지 보여주자마자 바로꺼지지 않도록 waitKey함수 사용
cv2.imwrite('result1.png',img_basic) #파일의 어떤 형태로써 저장 할 것인지

#destroyAllWindows함수는 위의 이미지 출력한다음 이미지 종료 한 다음 다시 아래 이미지 출력.
cv2.destroyAllWindows()

#이미지를 흑백컬러로
img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY)
#읽어들인 이미지를 cvtColor함수를 이용해 특정한 속성을 가지도록 바꿀수 있다.
#BGR형태로 이루어진 numpy 객체(img_basic)를 gray형태로 바꾸겠다. 2-->to의 의미.
cv2.imshow('Image Basic',img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png',img_gray)