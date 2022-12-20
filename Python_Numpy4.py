import numpy as np
#numpy의 마스킹 연산.
array1 = np.arange(16).reshape(4,4)
print(array1,end = '\n\n')

#마스킹 연산 수행
array2 = array1 <10
print(array2,end = '\n\n')

#마스킹 연산 활용
array1[array2] = 50
#array1 에 마스킹 연산이 수행된 배열(array2)을 넣으면 그 조건을 만족하는 데이터만 작업(50을 넣는다)을 해준다.
print(array1,end = '\n\n')

#집계 함수사용하기
array3 = np.arange(16).reshape(4,4)
print("최대값: ",np.max(array3))
print("최솟값: ",np.min(array3))
print("합계 : ",np.sum(array3))
print("평균값 : ",np.mean(array3),end = '\n\n')
print(array3,end = '\n\n')

print(np.sum(array3,axis = 0)) #axis가 0일때 행기준으로 더한다. axis가 1일때 열기준



