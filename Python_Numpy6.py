import numpy as np

#Numpy 각 열을 기준으로 정렬
array  = np.array([[2,7,1,6,8],[8,3,4,2,5]]) #이차원 형태의 배열
print(array)
print()
array.sort(axis=0) #axis=0 기준을 행으로 삼게되면 각각의 열 에 비교해서 더 큰 행이 아래로 내려간다.
print(array)
print()
#균일한 간격으로 데이터 생성
array1 = np.linspace(0,10,5)# 시작값과 끝값사이 몇개 데이터.(0~10사이 5개 데이터가 채워진다.)
print(array1)
print()
#난수의 재연(실행마다 결과 동일)
np.random.seed(8) #어떤 값을 기준으로 난수를 생성할 것인지 설정. ,난수의 생성패턴을 동일하게 관리한다.
print(np.random.randint(0,10,(3,3)))
print()

#Numpy 배열 객체 복사
array2 = np.arange(0,10)
array3 = array2.copy()
array3[0] = 99
print(array2)
print()
#중복된 원소 제거
array5 = np.array([1,1,2,3,3,4,2])
print(np.unique(array5))

#array4 = np.array4([1,1,2,3,4,1,2]), numpy의 array메소드이다...
#print(np.unique(array4))