import numpy as np
#Numpy practice
array = np.array([1,2,3])
print(array.size)
print(array.dtype) #Numpy 배열 객체의 dtype int32(or 64)
print(array[2])

print()

array1 = np.arange(4)
print(array1)

print()

array2 = np.zeros((4,4),dtype=float)
print(array2,end='\n\n')

array3 = np.ones((3,3),dtype=str)
print(array3,end = '\n\n')

array4 = np.random.randint(0,10,(3,3)) # random.randint는 범위에 있는 int 값을 랜덤하게 반환
print(array4,end = '\n\n')

array5 = np.random.normal(0,1,(3,3)) #np.random.normal 은 정규분포 함수
print(array5)

