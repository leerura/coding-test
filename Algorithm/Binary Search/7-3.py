#반복문을 이용한 이진탐색
array = [0,2,4,6,8,10,12,14,16,18]

def binary_search(array, target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid -1
        else:
            start = mid + 1
    return None

print(binary_search(array, 4, 0 ,len(array)-1))




