#재귀함수를 이용한 이진탐색(binary_search by recursive function)
array = [0,2,4,6,8,10,12,14,16,18]

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return array[start]
    elif target < array[mid]:
        return binary_search(array,target,start, mid-1)
    elif target > array[mid]:
        return binary_search(array,target, mid+1, end)

print(binary_search(array, 4, 0 ,len(array)-1))