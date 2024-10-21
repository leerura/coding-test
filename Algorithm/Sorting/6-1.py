#선택 정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #일단 앞에 부터 가져와
    min_index = i
    for j in range(i+1, len(array)): # i 바로 뒤에꺼부터 확인
        if array[min_index] > array[j]: #뒤에가 더 작으면
            min_index = j
    array[i],array[min_index] = array[min_index],array[i] #스와프

print(array)
