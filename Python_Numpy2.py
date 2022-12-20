import numpy as np
#Numpy 의 연산.
array = np.random.randint(1,10,size = 4).reshape(2,2) #2차원 배열생성
result_array = array*100 #array 배열의 각 요소에 100을 곱한다.
print(result_array)
print()
#numpy의 브로드캐스트 연산. 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환.
array1 = np.arange(4).reshape(2,2) #(2x2)
array2 = np.arange(2) #(1x2) -->이 배열이 아래쪽으로 늘어나서 array1에 더해지게 된다.(numpy 연산)
array3 = array1 + array2

print(array1,end = '\n\n')
print(array2,end = '\n\n')
print(array3)
print()

array4 = [[i for i in range(2)]for j in range(2)]
array5 = [[1,2]]
array6 = array4 + array5

print(array6)