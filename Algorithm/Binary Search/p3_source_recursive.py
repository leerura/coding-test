#재귀적 방법으로 구현
n, m = map(int, input().split())
length = list(map(int, input().split()))

def binary(array, target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    cut = 0
    for i in array:
        if i> mid:
            cut = cut + (i - mid)
    if cut > target:
        return binary(array,target,mid+1,end)
    elif cut < target:
        return binary(array,target,start, mid-1)
    else:
        return mid
    
print(binary(length,m,0,max(length)))

