#반복적 방법으로 구현
n, m = map(int, input().split())
length = list(map(int, input().split()))

def iterative_binary(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        total = 0
        for i in length:
            if i > mid:
                total = total + (i-mid)
        if total > target:
            start = mid + 1
        elif total < target:
            end = mid - 1
        else:
            return mid
        
print(iterative_binary(length,m,0,max(length)))