#퀵정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick(array,start,end):
    if start >= end:
        return #아무것도 반환하지 않기에 마지막에도 return 함수가 아니라 그냥 호출만 함
    pivot = start
    left = start + 1
    right = end
    while left <= right:# 이게 만족이 안되면 그때 while까지는 다 하고 while문 종료
        while left <= end and array[left] <= array[pivot]: #left end 조건 없으면 ou of range 오류 발생
            left = left + 1
        while start <right and array[right] >= array[pivot]:
            right = right - 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right],array[left]
    quick(array,start, right-1)
    quick(array,right+1, end)

quick(array,0,len(array)-1)
print(array)