import numpy as np

#단일 객체 저장 및 불러오기.
array = np.arange(0,10)
np.save('saved.npy',array)

#프로그램을 동작시키면 saved.npy라는 하나의 파일이 생성됨.
#해당 파일은 압축된 형태로 제공(text 파일로 열어보아도 확인 어렵다.)

result = np.load('saved.npy')#저장되 잇는 numpy 파일 불러오기(load)
print(result)
print()
#복수 객체 저장 및 불러오기

#복수개의 numpy객체를 파일 형태로 저장하고자 할때 np.savez

array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz',array1 = array1,array2=array2)

data = np.load('saved.npz')
result1 = data['array1'] #저장했을때 사용했던 객체의 이름 인덱스로 데이터 불러온다.
result2 = data['array2']
print(result1)
print(result2)