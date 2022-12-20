import numpy as np

array1 = np.arange(0,8).reshape(2,4)
array2 = np.arange(8,16).reshape(2,4)
array3 = np.concatenate([array1,array2],axis = 0)
#concatenate 메소드는 배열을 합쳐주는(연결) 역할의 메소드이다.
#axis는 연결의 방향을 나타낸다. 2차원 배열일때는 axis = 0(행기준) or 1(열기준)
print(array3)

array4 = np.arange(8).reshape(2,4)
left,right = np.split(array4,[2],axis = 1)#열 기준(axis = 1) index[2]를 기준으로 나눈다.
print(left.shape) #shape는 배열의 형태를 나타낸다.
print(right.shape)
print(right[1][1])

