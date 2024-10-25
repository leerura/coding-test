#p2 재귀함수 이진탐색을 이용한 풀이
n = int(input())
have = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

have.sort()

def binary(array, target, start, end):
    if start > end:
        return "no"
    mid = (start+end)//2
    if target < array[mid]:
        return binary(array,target,start,mid-1)
    elif target > array[mid]:
        return binary(array,target,mid+1,end)
    else:
        return "yes"
    
for i in want:
    print(binary(have, i, 0, len(have)-1), end=" ")