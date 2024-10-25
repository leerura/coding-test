#p2 반복적 방법의 이진탐색을 이용한 풀이
n = int(input())
have = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

have.sort()

def binary(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 'yes'
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

for i in want:
    print(binary(have, i, 0, len(have)-1), end=" ") 
